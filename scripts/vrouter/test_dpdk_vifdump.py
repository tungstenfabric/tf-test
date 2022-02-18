'''
This FT automation implementation will check vifdump on vif0/1/2 interface
Tested on dpdk compute Bond configuration
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because
import test

class TestVifdump(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestVifdump, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestVifdump, cls).tearDownClass()

    def verify_vifdump_status(self,compute_ip):
        ''' check the vifdump on vif0/0,0/1,0/2 interface'''
        self.logger.info(compute_ip)
        vif_list_cmd = "vif --list | grep vif"
        vif_out = self.inputs.run_cmd_on_server(compute_ip, vif_list_cmd)
        assert vif_out, "no output for vif --list"
        assert "vif0/0" in vif_out, "vif0/0 not present"
        assert "vif0/1" in vif_out, "vif0/1 not present"
        assert "vif0/2" in vif_out, "vif0/2 not present"
        out = self.inputs.run_cmd_on_server(compute_ip,
            "contrail-tools vifdump -i 0 -n -c 3")
        assert "3 packets captured" in out, "vifdump on vif0/0 failed"
        self.logger.info(out)
        out = self.inputs.run_cmd_on_server(compute_ip,
            "contrail-tools vifdump -i 1 -n -c 3")
        assert "3 packets captured" in out, "vifdump on vif0/1 failed"
        self.logger.info(out)
        out = self.inputs.run_cmd_on_server(compute_ip,
            "contrail-tools vifdump -i 2 -n -c 3")
        assert "3 packets captured" in out, "vifdump on vif0/2 failed"
        self.logger.info(out)
        return True

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(dpdk_cluster=False)
    def test_vifdump_on_interface(self):
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[1],image_name='ubuntu-traffic')
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0],image_name='ubuntu-traffic')
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        client = client_fixtures[0]
        server = server_fixtures[0]
        #set parameters required for TCP traffic to send from src to dest VM
        proto = 'tcp'
        dport = 5201
        sport = 10001
        assert self.send_nc_traffic(client, server, sport, dport, proto), "tcp traffic failed"
        compute_ip = server.vm_node_ip
        self.verify_vifdump_status(compute_ip)
