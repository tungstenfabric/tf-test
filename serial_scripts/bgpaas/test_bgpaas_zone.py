from tcutils.wrappers import preposttest_wrapper
from common.bgpaas.base import BaseBGPaaS
from common.neutron.base import BaseNeutronTest
import test
import time
from tcutils.util import *
from tcutils.tcpdump_utils import *
from common import isolated_creds

class TestBGPaasZone(BaseBGPaaS):

    @classmethod
    def setUpClass(cls):
        super(TestBGPaasZone, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestBGPaasZone, cls).tearDownClass()

    def basic_control_node_zone_setup(self,ctrl_zone=None):
        self.vms = []
        self.bgpaas_fixtures = []
        self.vn_subnets = [get_random_cidr()]
        self.local_as = 65000
        self.vn_name = get_random_name("cnz_vn")
        self.bgpaas_count = 2
        self.cnzs = []
        cnt = 0
        self.vn = self.create_vn(self.vn_name,self.vn_subnets)
        for i in range(0,2):
            self.vms.append(self.create_vm(vn_fixture=self.vn, image_name='ubuntu-bird'))
        self.client_vm = self.create_vm(vn_fixture=self.vn, image_name='ubuntu-bird')
        self.check_vms_booted(self.vms + [self.client_vm])
        for bgp_name in self.inputs.bgp_names:
            self.cnzs  +=  self.create_control_node_zones("test-zone",[bgp_name])
        self.vip = get_an_ip(self.vn_subnets[0],offset=20)
        if ctrl_zone is None:
            self.bgpaas_fixtures.append(self.create_and_attach_bgpaas(self.cnzs,
                                        self.vn,self.vms[0],self.local_as,self.vip,'primary'))
            self.bgpaas_fixtures.append(self.create_and_attach_bgpaas(self.cnzs,
                                        self.vn,self.vms[1],self.local_as,self.vip,'secondary'))
        else:
            self.bgpaas_fixtures.append(self.create_and_attach_bgpaas(self.cnzs,
                                       self.vn,self.vms[0],self.local_as,self.vip,ctrl_zone))
            self.bgpaas_fixtures.append(self.create_and_attach_bgpaas(self.cnzs,
                                       self.vn,self.vms[1],self.local_as,self.vip,ctrl_zone))
        for vm in self.vms:
            assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
            cnt += 1
        msg = 'ping from %s to %s failed'%(self.client_vm.name, self.vip)
        assert self.client_vm.ping_with_certainty(self.vip)
        return True

    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_bgp_control_node_zone(self):
        cnt = 0
        self.logger.info('executing bgp_control_zone test')
        assert self.basic_control_node_zone_setup()
        # update control node zone with different bgp routers
        self.update_control_node_zones(self.cnzs)
        self.flap_bgpaas_peering(self.vms)
        for vm in self.vms:
           assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
           cnt += 1
        assert self.client_vm.ping_with_certainty(self.vip)
        # remove zone from bgpaas and add new zone
        self.detach_zones_from_bgpaas(self.bgpaas_fixtures[0],primary=True)
        self.cnzs[0].remove_bgp_routers_from_zone()
        assert self.create_and_attach_bgpaas([self.cnzs[2]],self.vn,self.vms[0],
                                      self.local_as,self.vip,'primary',self.bgpaas_fixtures[0])
        self.flap_bgpaas_peering(self.vms)
        cnt = 0
        for vm in self.vms:
            assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
            cnt += 1
        assert self.client_vm.ping_with_certainty(self.vip)
        return

    @preposttest_wrapper
    def test_bgp_multiple_control_nodes_in_zone(self):
        self.logger.info('executing bgp_control_zone test')
        vms = []
        bgpaas_fixtures = []
        vn_subnets = [get_random_cidr()]
        local_as = 65000
        vn_name = get_random_name("cnz_vn")
        cnza=[]
        self.addCleanup(self.inputs.start_container, self.inputs.bgp_ips, 'control')
        vn = self.create_vn(vn_name,vn_subnets)
        for i in range(0,2):
            vms.append(self.create_vm(vn_fixture=vn, image_name='ubuntu-bird'))
        client_vm = self.create_vm(vn_fixture=vn, image_name='ubuntu-bird')
        self.check_vms_booted(vms + [client_vm])
        cnzs = self.create_control_node_zone("test-zone",self.inputs.bgp_names[:-1])
        cnzs += self.create_control_node_zones("test-zone",[self.inputs.bgp_names[-1]])
        vip = get_an_ip(vn_subnets[0],offset=20)
        bgpaas_fixtures.append(self.create_and_attach_bgpaas(cnzs,
                                                     vn,vms[0],local_as,vip,'both-zones'))
        assert self.verify_bgpaas_in_control_nodes_and_agent(bgpaas_fixtures[0],vms[0])
        msg = 'ping from %s to %s failed'%(client_vm.name, vip)
        assert client_vm.ping_with_certainty(vip)
        # stop one bgp control node zone
        self.inputs.stop_container(host_ips=self.inputs.bgp_ips[:-1],container='control')
        self.flap_bgpaas_peering(vms)
        self.inputs.start_container(host_ips=self.inputs.bgp_ips,container='control')
        assert self.verify_bgpaas_in_control_nodes_and_agent(bgpaas_fixtures[0],vms[0])
        assert client_vm.ping_with_certainty(vip)
        return True

    @preposttest_wrapper
    def test_bgp_control_node_zone_control_restart(self):
        cnt = 0
        self.logger.info('executing bgp_control_zone control restart test')
        self.addCleanup(self.inputs.start_container, self.inputs.bgp_ips, 'control')
        assert self.basic_control_node_zone_setup()
        self.inputs.stop_container(host_ips=self.inputs.bgp_ips,container='control')
        self.flap_bgpaas_peering(self.vms)
        self.inputs.start_container(host_ips=self.inputs.bgp_ips,container='control')
        for vm in self.vms:
            assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
            cnt += 1
        assert self.client_vm.ping_with_certainty(self.vip)
        return True

    @preposttest_wrapper
    def test_bgp_control_node_zone_agent_restart(self):
        self.logger.info('executing bgp_control_zone agent restart test')
        host_ips = []
        cnt = 0
        assert self.basic_control_node_zone_setup()
        for vm in self.vms:
            host_ips.append(vm.get_compute_host())
        self.inputs.restart_container(host_ips,'agent')
        for vm in self.vms:
            assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
            cnt += 1
        assert self.client_vm.ping_with_certainty(self.vip)
        return True

    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_bgp_control_node_zones_from_single_vnf(self):
        cnt = 0
        self.logger.info('executing bgp_control_zone agent restart test')
        host_ips = []
        assert self.basic_control_node_zone_setup('both-zones')
        for vm in self.vms:
            assert self.verify_bgpaas_in_control_nodes_and_agent(self.bgpaas_fixtures[cnt],vm)
            cnt += 1
        assert self.client_vm.ping_with_certainty(self.vip)
        return True

    def is_test_applicable(self):
        # check for atleast 3 control nodes
        if len(self.inputs.bgp_ips) < 3 :
            return (False, "control nodes are not sufficient")
        return (True,None)

