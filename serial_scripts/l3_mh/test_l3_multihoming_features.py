from __future__ import absolute_import, unicode_literals
from serial_scripts.md5.base import Md5Base
from tcutils.traffic_utils.hping_traffic import Hping3
from common.gw_less_fwd.base import *
from common.dsnat.base import BaseDSNAT
from common.intf_mirroring.verify import VerifyIntfMirror
from scripts.intf_mirror.base import BaseIntfMirrorTest
from tcutils.tcpdump_utils import *
from tcutils.util import *
from common.neutron.base import BaseNeutronTest
from common.bgpaas.base import BaseBGPaaS
from common.openstack_libs import nova_client as mynovaclient
from common.device_connection import NetconfConnection
from compute_node_test import ComputeNodeFixture
from tcutils.cores import get_service_crashes
from common.l3_mh.base import BaseL3Multihoming
from tcutils.contrail_status_check import ContrailStatusChecker
from traffic.core.profile import create, ContinuousProfile
from vnc_api.vnc_api import *
import test
from tcutils.commands import ssh, execute_cmd, execute_cmd_out
import time
import inspect
from common import isolated_creds
from builtins import str
from builtins import range
import traffic_tests
from vn_test import *
from vm_test import *
from floating_ip import *
from policy_test import *
from user_test import UserFixture
from multiple_vn_vm_test import *
import random
from tcutils.wrappers import preposttest_wrapper
sys.path.append(os.path.realpath('tcutils/pkgs/Traffic'))


class TestSerialL3MultihomingFeatures(
        BaseL3Multihoming, BaseIntfMirrorTest, VerifyIntfMirror, GWLessFWDTestBase, BaseDSNAT, Md5Base):
    @classmethod
    def setUpClass(cls):
        super(TestSerialL3MultihomingFeatures, cls).setUpClass()
        cls.l3mh_setup_check_done = False

    @classmethod
    def tearDownClass(cls):
        super(TestSerialL3MultihomingFeatures, cls).tearDownClass()

    def setUp(self):
        super(TestSerialL3MultihomingFeatures, self).setUp()
        if TestSerialL3MultihomingFeatures.l3mh_setup_check_done:
            return
        if not self.inputs.inputs.l3mh_cidr:
            return (
                False, 'This script runs on l3mh setup only, and you need to provide a L3MH_CIDR knob in yaml file')
        dpdk_found = False
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    dpdk_found = True
        assert dpdk_found, 'This script needs atleadt 1 dpdk node to work, no dpdk found'
        TestSerialL3MultihomingFeatures.l3mh_setup_check_done = True

    def spawn_dpdk_flavors(self):
        self.obj1 = mynovaclient.Client(
            '2', session=self.nova_h.auth_h.get_session(
                scope='project'), region_name='regionOne')
        self.obj1.flavors.create(name='cirros_dpdk', vcpus=1, ram=64, disk=10)
        self.obj1.flavors.create(
            name='ubuntu_traffic_dpdk',
            vcpus=1,
            ram=1024,
            disk=10)
        self.obj1.flavors.create(
            name='bgpaas_dpdk', vcpus=2, ram=2048, disk=40)
        for fl_list in ['cirros_dpdk', 'ubuntu_traffic_dpdk', 'bgpaas_dpdk']:
            flavor = self.obj1.flavors.find(name=fl_list)
            flavor.set_keys({'hw:mem_page_size': 'large'})

    def configure_spine_leaf(self):
        for i in range(len(list(self.inputs.physical_routers_data.values()))):
            router_params = list(self.inputs.physical_routers_data.values())[i]
            cmd = []
            if router_params['role'] == 'spine':
                cmd.append(
                    'set protocols bgp group reflector-peers type internal')
                cmd.append(
                    'set protocols bgp group reflector-peers family inet unicast')
                cmd.append(
                    'set protocols bgp group reflector-peers family inet6 unicast')
                cmd.append(
                    'set protocols bgp group reflector-peers family inet6-vpn unicast')
                cmd.append(
                    'set protocols bgp group reflector-peers export send-direct')
                cmd.append(
                    'set protocols bgp group reflector-peers cluster %s' %
                    router_params['spine_control_ip'])
                cmd.append('set protocols bgp group reflector-peers multipath')
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet unicast add-path receive' %
                    router_params['leaf1_control_ip'])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet unicast add-path send path-count 2' %
                    router_params['leaf1_control_ip'])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet unicast add-path receive' %
                    router_params['leaf2_control_ip'])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet unicast add-path send path-count 2' %
                    router_params['leaf2_control_ip'])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet unicast' %
                    self.inputs.bgp_control_ips[0])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet-vpn unicast' %
                    self.inputs.bgp_control_ips[0])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family inet6 unicast' %
                    self.inputs.bgp_control_ips[0])
                cmd.append(
                    'set protocols bgp group reflector-peers neighbor %s family route-target' %
                    self.inputs.bgp_control_ips[0])
                cmd.append(
                    'set vlans vlan-l3mh-controller vlan-id %s' %
                    router_params['spine_dev_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-controller l3-interface irb.%s' %
                    router_params['spine_dev_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway1 vlan-id %s' %
                    router_params['spine_gw1_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway1 l3-interface irb.%s' %
                    router_params['spine_gw1_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 vlan-id %s' %
                    router_params['spine_gw2_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 l3-interface irb.%s' %
                    router_params['spine_gw2_vlan'])

            elif router_params['role'] == 'leaf1':
                cmd.append(
                    'set protocols bgp group route-reflector type internal')
                cmd.append(
                    'set protocols bgp group route-reflector local-address %s' %
                    router_params['leaf1_control_ip'])
                cmd.append(
                    'set protocols bgp group route-reflector export send-direct')
                cmd.append(
                    'set protocols bgp group route-reflector export EXP-FILTER')
                cmd.append('set protocols bgp group route-reflector multipath')
                cmd.append(
                    'set protocols bgp group route-reflector neighbor %s family inet unicast add-path receive' %
                    router_params['spine_control_ip'])
                cmd.append(
                    'set protocols bgp group route-reflector neighbor %s family inet unicast add-path send path-count 2' %
                    router_params['spine_control_ip'])
                cmd.append(
                    'set vlans rhosp_dev_1716 vlan-id %s' %
                    router_params['leaf1_dev_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-10 vlan-id %s' %
                    router_params['leaf1_l3mh_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-10 l3-interface irb.%s' %
                    router_params['leaf1_l3mh_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 vlan-id %s' %
                    router_params['leaf1_gw_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 l3-interface irb.%s' %
                    router_params['leaf1_gw_vlan'])
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf1_control_agent1_gw_vlan'],
                     router_params['leaf1_control_gw1_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf1_int_agent1_gw_vlan'],
                     router_params['leaf1_int_gw1_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf1_l3mh_agent2_gw_vlan'],
                     router_params['leaf1_l3mh_gw2_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf1_l3mh_agent1_gw_vlan'],
                     router_params['leaf1_l3mh_gw1_vlan']))
            elif router_params['role'] == 'leaf2':
                cmd.append(
                    'set protocols bgp group route-reflector type internal')
                cmd.append(
                    'set protocols bgp group route-reflector local-address %s' %
                    router_params['leaf2_control_ip'])
                cmd.append(
                    'set protocols bgp group route-reflector export send-direct')
                cmd.append(
                    'set protocols bgp group route-reflector export EXP-FILTER')
                cmd.append('set protocols bgp group route-reflector multipath')
                cmd.append(
                    'set protocols bgp group route-reflector neighbor %s family inet unicast add-path receive' %
                    router_params['spine_control_ip'])
                cmd.append(
                    'set protocols bgp group route-reflector neighbor %s family inet unicast add-path send path-count 2' %
                    router_params['spine_control_ip'])
                cmd.append(
                    'set vlans rhosp_dev_1716 vlan-id %s' %
                    router_params['leaf2_dev_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-10 vlan-id %s' %
                    router_params['leaf2_l3mh_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-10 l3-interface irb.%s' %
                    router_params['leaf2_l3mh_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 vlan-id %s' %
                    router_params['leaf2_gw_vlan'])
                cmd.append(
                    'set vlans vlan-l3mh-gateway2 l3-interface irb.%s' %
                    router_params['leaf2_gw_vlan'])
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf2_control_agent1_gw_vlan'],
                     router_params['leaf2_control_gw1_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf2_int_agent1_gw_vlan'],
                     router_params['leaf2_int_gw1_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf2_l3mh_agent2_gw_vlan'],
                     router_params['leaf2_l3mh_gw2_vlan']))
                cmd.append(
                    'set routing-options static route %s next-hop %s' %
                    (router_params['leaf2_l3mh_agent1_gw_vlan'],
                     router_params['leaf2_l3mh_gw1_vlan']))

            mx_handle = NetconfConnection(host=router_params['mgmt_ip'])
            mx_handle.connect()
            cli_output = mx_handle.config(stmts=cmd, timeout=120)

    def check_routes_on_boxes(self):

        for i in range(len(list(self.inputs.physical_routers_data.values()))):
            router_params = list(self.inputs.physical_routers_data.values())[i]
            mx_handle = NetconfConnection(host=router_params['mgmt_ip'])
            mx_handle.connect()
            cli_output = mx_handle.get_config()
            if router_params['role'] == 'spine':
                assert router_params['spine_dev_vlan'] in cmd, 'No spine dev vlan found'
                assert router_params['spine_gw1_vlan'] in cmd, 'No spine gw vlan found'
                assert router_params['spine_gw2_vlan'] in cmd, 'No spine gw vlan found'
            elif router_params['role'] == 'leaf1':
                assert router_params['leaf1_dev_vlan'] in cmd, 'No leaf dev vlan found'
                assert router_params['leaf1_gw_vlan'] in cmd, 'No leaf gw vlan found'
            elif router_params['role'] == 'leaf2':
                assert router_params['leaf2_dev_vlan'] in cmd, 'No leaf dev vlan found'
                assert router_params['leaf2_gw_vlan'] in cmd, 'No leaf gw vlan found'

    def scale_vms_vns_policy(self):
        # get vn and vm names

        self.vn1_name = get_random_name('vn1')
        self.vn2_name = get_random_name('vn2')
        self.vn3_name = get_random_name('vn3')
        self.vn4_name = get_random_name('vn4')
        self.vn5_name = get_random_name('vn5')
        self.vn6_name = get_random_name('vn6')
        self.vn7_name = get_random_name('vn7')
        self.vn8_name = get_random_name('vn8')
        self.vn9_name = get_random_name('vn9')
        self.vn10_name = get_random_name('vn10')
        self.vm1_name = get_random_name('vm1')
        self.vm2_name = get_random_name('vm2')
        self.vm3_name = get_random_name('vm3')
        self.vm4_name = get_random_name('vm4')
        self.vm5_name = get_random_name('vm5')
        self.vm6_name = get_random_name('vm6')
        self.vm7_name = get_random_name('vm7')
        self.vm8_name = get_random_name('vm8')
        self.vm9_name = get_random_name('vm9')
        self.vm10_name = get_random_name('vm10')

        # get dpdk compute

        self.node1 = []
        self.node2 = []
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    self.node1.append(self.inputs.host_data[host]['name'])
            else:
                self.node2.append(self.inputs.host_data[host]['name'])

        # create vns
        self.vn1_fixture = self.create_vn(
            vn_name=self.vn1_name, orch=self.orchestrator)
        self.vn2_fixture = self.create_vn(
            vn_name=self.vn2_name, orch=self.orchestrator)
        self.vn3_fixture = self.create_vn(
            vn_name=self.vn3_name, orch=self.orchestrator)
        self.vn4_fixture = self.create_vn(
            vn_name=self.vn4_name, orch=self.orchestrator)
        self.vn5_fixture = self.create_vn(
            vn_name=self.vn5_name, orch=self.orchestrator)
        self.vn6_fixture = self.create_vn(
            vn_name=self.vn6_name, orch=self.orchestrator)
        self.vn7_fixture = self.create_vn(
            vn_name=self.vn7_name, orch=self.orchestrator)
        self.vn8_fixture = self.create_vn(
            vn_name=self.vn8_name, orch=self.orchestrator)
        self.vn9_fixture = self.create_vn(
            vn_name=self.vn9_name, orch=self.orchestrator)
        self.vn10_fixture = self.create_vn(
            vn_name=self.vn10_name, orch=self.orchestrator)

        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                                                            vn2_fixture)
        self.vn1_fixture.read()
        self.vn2_fixture.read()
        self.vn3_fixture.read()
        self.vn4_fixture.read()
        self.vn5_fixture.read()
        self.vn6_fixture.read()
        self.vn7_fixture.read()
        self.vn8_fixture.read()
        self.vn9_fixture.read()
        self.vn10_fixture.read()

        # create vms

        self.vm1_fixture = self.create_vm(vn_fixture=self.vn1_fixture,
                                          image_name='cirros', vm_name=self.vm1_name, node_name=self.node1[0], flavor='cirros_dpdk')
        self.vm2_fixture = self.create_vm(vn_fixture=self.vn2_fixture,
                                          image_name='cirros', vm_name=self.vm2_name, node_name=self.node2[0])
        self.vm3_fixture = self.create_vm(vn_fixture=self.vn3_fixture,
                                          image_name='cirros', vm_name=self.vm3_name, node_name=self.node1[0], flavor='cirros_dpdk')
        self.vm4_fixture = self.create_vm(vn_fixture=self.vn4_fixture,
                                          image_name='cirros', vm_name=self.vm4_name, node_name=self.node2[0])
        self.vm5_fixture = self.create_vm(vn_fixture=self.vn5_fixture,
                                          image_name='cirros', vm_name=self.vm5_name, node_name=self.node1[0], flavor='cirros_dpdk')
        self.vm6_fixture = self.create_vm(vn_fixture=self.vn2_fixture,
                                          image_name='cirros', vm_name=self.vm6_name, node_name=self.node2[0])
        assert self.vm1_fixture.wait_till_vm_is_up()
        assert self.vm2_fixture.wait_till_vm_is_up()
        assert self.vm3_fixture.wait_till_vm_is_up()
        assert self.vm4_fixture.wait_till_vm_is_up()
        assert self.vm5_fixture.wait_till_vm_is_up()
        assert self.vm6_fixture.wait_till_vm_is_up()

        self.vn2_port1 = self.setup_only_vmi(self.vn1_fixture.uuid)
        self.vn1_port1 = self.setup_only_vmi(self.vn1_fixture.uuid,
                                             parent_vmi=self.vn2_port1.vmi_obj,
                                             vlan_id=random.randint(20, 80),
                                             api_type='contrail',
                                             mac_address=self.vn2_port1.mac_address)

        self.vn1_port2 = self.setup_only_vmi(self.vn2_fixture.uuid)
        self.vn2_port2 = self.setup_only_vmi(self.vn2_fixture.uuid,
                                             parent_vmi=self.vn1_port2.vmi_obj,
                                             vlan_id=random.randint(20, 80),
                                             api_type='contrail',
                                             mac_address=self.vn1_port2.mac_address)

        interface = 'eth0.%s' % (random.randint(20, 80))
        vm1_sub_intf_ip = self.vn1_port1.get_ip_addresses()[0]
        assert self.vm1_fixture.wait_till_interface_created(interface,
                                                            ip=vm1_sub_intf_ip)[0]

        interface = 'eth0.%s' % (random.randint(20, 80))
        vm2_sub_intf_ip = self.vn2_port1.get_ip_addresses()[0]
        assert self.vm2_fixture.wait_till_interface_created(interface,
                                                            ip=vm2_sub_intf_ip)[0]

    def feature_check(self):
        destport = random.randint(1000, 60000)
        baseport = random.randint(1000, 60000)
        # Create flows using hping
        hping_h = Hping3(vm1_fixture,
                         vm2_fixture,
                         syn=True,
                         destport=destport,
                         baseport=baseport,
                         count=10,
                         interval=2)
        hping_h.start(wait=False)
        self.verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn3_vn3()

        self.bgpaas_vm = self.create_vm(vn_fixture=self.vn1_fixture, vm_name='bgpaas_vm1',
                                        image_name='ubuntu-bird', node_name=self.node1[0], flavor='ubuntu_traffic_dpdk')
        self.bgpaas_vm2 = self.create_vm(self.vn2_fixture, 'bgpaas_vm2',
                                         image_name='ubuntu-bird', node_name=self.node2[0])
        assert self.bgpaas_vm.wait_till_vm_is_up()
        assert self.bgpaas_vm2.wait_till_vm_is_up()
        bgp_vm_port = bgpaas_vm.vmi_ids[self.bgpaas_vm.vn_fq_name]
        local_as = random.randint(29000, 30000)
        local_ip = self.bgpaas_vm.vm_ip
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        dns_ip = self.vn1_fixture.get_subnets()[0]['dns_server_address']
        neighbors = [gw_ip, dns_ip]
        peer_as = self.connections.vnc_lib_fixture.get_global_asn()
        self.bgpaas_fixture = self.create_bgpaas(
            bgpaas_shared=True, autonomous_system=local_as, bgpaas_ip_address=local_ip)
        self.config_bgp_on_bird(
            self.bgpaas_vm,
            local_ip,
            local_as,
            neighbors,
            peer_as)
        self.attach_vmi_to_bgpaas(bgp_vm_port, self.bgpaas_fixture)
        self.addCleanup(self.detach_vmi_from_bgpaas,
                        bgp_vm_port, self.bgpaas_fixture)
        agent = self.bgpaas_vm.vm_node_ip
        assert self.bgpaas_fixture.verify_in_control_node(
            self.bgpaas_vm), 'BGPaaS Session not seen in the control-node'

        bgp_vm_port = self.bgpaas_vm2.vmi_ids[self.bgpaas_vm2.vn_fq_name]
        local_as = random.randint(29000, 30000)
        local_ip = self.bgpaas_vm2.vm_ip
        gw_ip = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        dns_ip = self.vn2_fixture.get_subnets()[0]['dns_server_address']
        neighbors = [gw_ip, dns_ip]
        peer_as = self.connections.vnc_lib_fixture.get_global_asn()
        self.bgpaas_fixture2 = self.create_bgpaas(
            bgpaas_shared=True, autonomous_system=local_as, bgpaas_ip_address=local_ip)
        self.config_bgp_on_bird(
            self.bgpaas_vm2,
            local_ip,
            local_as,
            neighbors,
            peer_as)
        self.attach_vmi_to_bgpaas(bgp_vm_port, self.bgpaas_fixture2)
        self.addCleanup(self.detach_vmi_from_bgpaas,
                        bgp_vm_port, self.bgpaas_fixture2)
        agent = self.bgpaas_vm2.vm_node_ip
        assert self.bgpaas_fixture2.verify_in_control_node(
            self.bgpaas_vm2), 'BGPaaS Session not seen in the control-node'

    def change_and_check_encap(self):
        self.logger.info("Read the existing encap priority")
        existing_encap = self.connections.read_vrouter_config_encap()
        self.logger.info('Setting new Encap before continuing')
        config_id = self.connections.update_vrouter_config_encap(
            'MPLSoGRE', 'VXLAN', 'MPLSoUDP')
        self.logger.info('Created.UUID is %s' % (config_id))

        configured_encap_list = [
            str('MPLSoGRE'), str('VXLAN'), str('MPLSoUDP')]
        if existing_encap != configured_encap_list:
            self.addCleanup(
                self.connections.update_vrouter_config_encap,
                existing_encap[0],
                existing_encap[1],
                existing_encap[2])
        encap_list = self.connections.read_vrouter_config_encap()
        if configured_encap_list != encap_list:

            self.logger.error(
                "Configured Encap Priority order is NOT matching with expected order. Configured: %s ,Expected: %s" %
                (configured_encap_list, encap_list))
            assert False
        else:
            self.logger.info(
                "Configured Encap Priority order is matching with expected order. Configured: %s ,Expected: %s" %
                (configured_encap_list, encap_list))

    @preposttest_wrapper
    def test_l3mh_multi_dimensional(self):
        '''
        Description: L2 an L3 Traffic test between inter vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2, inter vn inter compute traffic test
            4. Launch vm31 and vm32 in vn3 on same compute, ping vm31 to vm32, intra vn intra compute.
            5. Launch vm12 in vn1 on node2, ping vm1 to vm12, inra vn inter compute traffic.
            6. Ping vm2 to vm12, inter vn intra compute traffic.
        Pass Criteria:
            1. Verify ping is successful.
            2. Configure bgpaas and confim if bgpaas works.
        '''
        self.spawn_dpdk_flavors()
        assert self.check_bgp_status(), "BGP between nodes not up after per peer match"
        self.configure_spine_leaf()
        self.check_routes_on_boxes()
        self.scale_vms_vns_policy()
        self.feature_check()

        # ping test from vm1 to vm2, inter vn inter compute
        assert self.vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)

        # Restart agent on node2
        self.inputs.restart_service(
            'contrail-vrouter-agent', [node], container='agent')
        cluster_status, error_nodes = ContrailStatusChecker(
        ).wait_till_contrail_cluster_stable(nodes=[node])
        assert cluster_status, 'Hash of error nodes and services : %s' % (
            error_nodes)

        # make sure bgpaas session and traffic is not affected after restart
        assert self.bgpaas_fixture.verify_in_control_node(
            self.bgpaas_vm), 'BGPaaS Session not seen in the control-node'
        assert self.bgpaas_fixture2.verify_in_control_node(
            self.bgpaas_vm2), 'BGPaaS Session not seen in the control-node'

        # lets try changing the encap now
        self.change_and_check_encap()

        assert self.vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
    # end test_bgpaas_l3mh

    @preposttest_wrapper
    def test_dsnat_l3mh(self):
        '''
            create a VN and enable fabric SNAT
            launch two VMs in that VN
            verify ping between the VN and ping to the external IP
            disable fabric SNAT
            verify that the ping the external IP fails
        '''

        self.logger.info(
            "Create VN, enable FABRIC SNAT and verify its routing instance")
        vn_fixture = self.create_vn_enable_fabric_snat()

        test_vm1 = self.create_vm(vn_fixture, get_random_name('test_vm1'),
                                  image_name='ubuntu')
        test_vm2 = self.create_vm(vn_fixture, get_random_name('test_vm2'),
                                  image_name='ubuntu')
        assert test_vm1.wait_till_vm_is_up()
        assert test_vm2.wait_till_vm_is_up()

        assert test_vm1.verify_fabric_ip_as_floating_ip(vn_fixture.vn_fq_name)
        assert test_vm2.verify_fabric_ip_as_floating_ip(vn_fixture.vn_fq_name)

        assert test_vm1.ping_with_certainty(test_vm2.vm_ip)
        # with DSNAT enabled on VN, verify the ping to the external IP
        cfgm_ip = self.inputs.get_host_data_ip(self.inputs.cfgm_names[0])
        assert test_vm1.ping_with_certainty(cfgm_ip)

        self.logger.info(
            "disable fabric SNAT, and verify the ping to the external IP and inter VN")
        self.vnc_h.set_fabric_snat(vn_fixture.uuid, False)
        assert vn_fixture.verify_routing_instance_snat()
        assert not test_vm1.verify_fabric_ip_as_floating_ip(vn_fixture.vn_fq_name), (
            'FIP list of VMI expected to be empty')

        assert test_vm1.ping_with_certainty(test_vm2.vm_ip)
        assert test_vm1.ping_with_certainty(cfgm_ip, expectation=False)

    @preposttest_wrapper
    def test_l3mh_fabric_forwarding(self):
        '''
        Description: L2 an L3 Traffic test between inter vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2, inter vn inter compute traffic test
            4. Launch vm31 and vm32 in vn3 on same compute, ping vm31 to vm32, intra vn intra compute.
            5. Launch vm12 in vn1 on node2, ping vm1 to vm12, inra vn inter compute traffic.
            6. Ping vm2 to vm12, inter vn intra compute traffic.
        Pass Criteria:
            1. Verify ping is successful.
            2. Validate the fabric forwarding feature
        '''
        if (len(self.inputs.compute_ips) < 2):
            raise self.skipTest(
                "Skipping Test. At least 2 compute node required to run the test")

        # if not self.inputs.fabric_gw_info:
        #     raise self.skipTest(
        #        "Skipping Test. Fabric gateway is required to run the test")

        # VN parameters. IP Fabric forwarding is enabled on vn1.
        vn = {'count': 1,
              'vn1': {'subnet': get_random_cidr(), 'ip_fabric': True},
              }

        # VMI parameters
        vmi = {'count': 2,
               'vmi1': {'vn': 'vn1'},
               'vmi2': {'vn': 'vn1'},
               }

        # VM parameters
        vm = {'count': 2, 'launch_mode': 'distribute',
              'vm1': {'vn': ['vn1'], 'vmi': ['vmi1']},
              'vm2': {'vn': ['vn1'], 'vmi': ['vmi2']},
              }

        # Setup VNs, VMs as per user configuration
        ret_dict = self.setup_gw_less_fwd(vn=vn, vmi=vmi, vm=vm)
        vn_fixtures = ret_dict['vn_fixtures']
        vm_fixtures = ret_dict['vm_fixtures']

        # Verify Gateway less forward functionality. As IP Fabric forwarding
        # is enabled on vn1, traffic should go through underlay between VMs
        # As there is no explicit policy to allow traffic between VN and
        # "ip-fbric" network, ping from vhost to VM and VM to vhost should fail

        self.logger.info("-- SCENARIO: 1 Verifying gateway less forward "
                         "functionality without explicit policy --")
        self.verify_gw_less_fwd(ret_dict)
        # Policy parameters. Configuring a policy between between ip-fabric vn
        # and vn1 to allow communication between compute node and VMs in vn1.
        policy = {'count': 1,
                  'p1': {
                      'rules': [
                          {
                              'direction': '<>',
                              'protocol': 'any',
                              'source_network': 'default-domain:default-project:ip-fabric',
                              'dest_network': 'vn1',
                              'src_ports': 'any',
                              'dst_ports': 'any'
                          },
                      ]
                  }
                  }

        # Configure policy as per user configuration
        policy_fixtures = self.setup_policy(policy=policy,
                                            vn_fixtures=vn_fixtures)
        ret_dict['policy_fixtures'] = policy_fixtures

        # Verify Gateway less forward functionality. As IP Fabric forwarding
        # is enabled on vn1, traffic should go through underlay. Also, as
        # there is explicit policy to allow traffic between VN and "ip-fabric"
        # network, ping from vhost to VM and VM to vhost should be successful.

        self.logger.info("-- SCENARIO: 2 Verifying gateway less forward "
                         "functionality with explicit policy --")
        self.verify_gw_less_fwd(ret_dict)

        # Restart physical interfaces
        inspect_h = self.agent_inspect[vm_fixtures['vm2'].vm_node_ip]
        physical_intf_list = inspect_h.get_vna_interface_by_type('eth')
        for name in physical_intf_list:
            cmd = 'ifdown %s; sleep 5' % (name)
            self.inputs.run_cmd_on_server(
                vm_fixtures['vm2'].vm_node_ip, cmd)
        for name in physical_intf_list:
            cmd = 'ifup %s; sleep 5' % (name)
            self.inputs.run_cmd_on_server(
                vm_fixtures['vm2'].vm_node_ip, cmd)
        time.sleep(5)

        # Now, remove IP fabric provider network configuration on vn1
        vn1_fixture = vn_fixtures['vn1']
        ip_fab_vn_obj = self.get_ip_fab_vn()
        vn1_fixture.del_ip_fabric_provider_nw(ip_fab_vn_obj)

        time.sleep(2)

        # Verify Gateway less forward functionality. As IP Fabric forwarding
        # is disabled on vn1, traffic should go through overlay

        self.logger.info("-- SCENARIO: 3 Verifying gateway less forward "
                         "functionality when IP farwarding is disabled--")
        self.verify_gw_less_fwd(ret_dict=ret_dict)

    # end test_l3mh_fabric_forwarding
