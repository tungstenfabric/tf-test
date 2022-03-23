'''
This FT automation implementation will perform mtu config test on vhost0
'''
from builtins import str
import os
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
from tcutils.contrail_status_check import ContrailStatusChecker 
from tcutils.util import skip_because
from common.contrail_services import *
import test

class TestMtu(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestMtu, cls).setUpClass()
        cls.agent_inspect_h = cls.connections.agent_inspect

    @classmethod
    def tearDownClass(cls):
        super(TestMtu, cls).tearDownClass()

    def configure_vhost_mtu_and_verify(self,compute_ip):
        """
        1- Check the configured mtu on vhost interface
        2- configure MTU on vhost0 interface as 9k
        3- Read mtu value for vhost0 interface and verify
        4- If-down/up vhost0 interface
        5- Check vhost0 interface status
        6- Restore the mtu configuration
        """
        self.logger.info(compute_ip)
        cmd = "ifconfig vhost0 | head -n 1"
        out = self.inputs.run_cmd_on_server(compute_ip, cmd)
        assert out, "no output of ifconfig command"
        if "vhost0:" and "UP" not in out:
            assert out, "vhost is not UP" 
        else:
            if not "mtu 9000" in out:
                out1 = self.inputs.run_cmd_on_server(compute_ip,\
                        "ifconfig vhost0 mtu 9000")
                self.logger.info(out1)
            else:
                self.logger.info("vhost mtu is 9000")

        out = self.inputs.run_cmd_on_server(compute_ip, cmd)
        assert out, "no output of ifconfig vhost command"
        if "vhost0" and "UP" not in out:
           assert out, "vhost is not UP"
        else:
            if not "mtu 9000" in out:
                assert out, "Error while setting mtu to 9000"
            self.logger.info(out)

        self.inputs.stop_service('contrail-vrouter-agent-dpdk', [compute_ip], container='agent-dpdk')
        self.inputs.stop_service('contrail-vrouter-agent', [compute_ip], container='agent')
        self.addCleanup(self.inputs.start_service, 'contrail-vrouter-agent-dpdk', [compute_ip], container='agent-dpdk', verify_service=False)
        self.addCleanup(self.inputs.start_service, 'contrail-vrouter-agent', [compute_ip], container='agent')
        resp = self.inputs.run_cmd_on_server(compute_ip, "ifdown vhost0")
        self.addCleanup(self.inputs.run_cmd_on_server, compute_ip, "ifup vhost0")
        self.logger.info(resp)
        self.inputs.start_service('contrail-vrouter-agent-dpdk', [compute_ip], container='agent-dpdk', verify_service=False)
        self.inputs.start_service('contrail-vrouter-agent', [compute_ip], container='agent')
        cluster_status, error_nodes = ContrailStatusChecker(self.inputs
                ).wait_till_contrail_cluster_stable(compute_ip, refresh=True)
        assert cluster_status, 'error nodes and services:%s' % (error_nodes)
        out = self.inputs.run_cmd_on_server(compute_ip, cmd)
        assert out, "no output of ifconfig vhost command"
        if "vhost0" and "UP" not in out:
           assert out, "vhost is not UP"
        self.logger.info(out)
        return True
    #end configure_vhost_mtu_and_verify

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(dpdk_cluster=False)
    def test_mtu_config(self):
        ''' test mtu config on computes '''
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0], image_name='cirros')
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[1], image_name='cirros')
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        assert client_fixtures[0].ping_with_certainty(server_fixtures[0].vm_ip, expectation=True), "ping failed"
        compute_ip = client_fixtures[0].vm_node_ip
        self.configure_vhost_mtu_and_verify(compute_ip)
        client_fixtures[0].get_local_ip(refresh=True)
        assert client_fixtures[0].ping_with_certainty(server_fixtures[0].vm_ip, expectation=True), "ping failed"
        return True
     #end test_mtu_config
