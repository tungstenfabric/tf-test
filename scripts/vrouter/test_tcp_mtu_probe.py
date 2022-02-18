
'''
This FT automation implementation will check icmp/tcp traffic configuring different tcp_mtu_probe values

Tested on dpdk compute Bond configuration 
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because
import test

class TestMtuProbe(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestMtuProbe, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestMtuProbe, cls).tearDownClass()

    def configure_tcp_mtu_probe(self,client,server,value):
        change_mtu_probe = "echo " + str(value) + " > /proc/sys/net/ipv4/tcp_mtu_probing"
        cli_cmd = client.run_cmd_on_vm(cmds=[change_mtu_probe], as_sudo=True)
        svr_cmd = server.run_cmd_on_vm(cmds=[change_mtu_probe], as_sudo=True)
        self.logger.info(cli_cmd)
        self.logger.info(svr_cmd)
        return True

    def verify_icmp_traffic(self,client,server):
        assert client.ping_with_certainty(server.vm_ip,expectation=True), "ping failed"
        return True
       
    def verify_tcp_traffic(self,client,server, value):
        #set parameters required for TCP traffic to send from src to dest VM
        proto = 'tcp'
        dport = 5201 
        #change the source port for each iteration of sending tcp traffic
        sport = 10001
        if value is 1:
            sport += value 
        if value is 2:
            sport += value 
        assert self.send_nc_traffic(client, server, sport, dport, proto), "TCP traffic failed"
        return True
 
    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(min_nodes=2)
    def test_mtu_probe_inter_node(self):
        """ 
        Description: 
            check traffic configuring different tcp_mtu_probe vlaues on vm 
            MTU probing values: 0, 1, 2
            0 - Disabled (default)
            1 - Disabled by default, Enabled only when ICMP black hole detected
            2 - Always enabled, using the initial MSS value of tcp_base_mss
            system internally enables bit values for point 1&2
            For test purpose,
            Idea is to check traffic works fine on configuring values
            Vm's across compute node
        steps:
            1. create 1 VN and launch 2 VMs across compute node 
            2. client and server VMs across compute node
            3. configure tcp_mtu_probe to 0, 1, 2
            4. send icmp traffic assert if ping fails 
            5. send tcp traffic assert if tcp traffic fails
        Pass criteria:
            1. If icmp/tcp traffic work fine configuring tcp_mtu_probe values 
        """
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0],image_name='ubuntu-traffic')
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[1],image_name='ubuntu-traffic')
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        client = client_fixtures[0]
        server = server_fixtures[0]
        for value in range(0,3):
            self.configure_tcp_mtu_probe(client,server,value)
            self.verify_icmp_traffic(client,server)
            self.verify_tcp_traffic(client,server, value)
        return True

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    def test_mtu_probe_intra_node(self):
        """ 
        Description: 
            check traffic configuring different tcp_mtu_probe vlaues on vm 
            MTU probing values: 0, 1, 2
            0 - Disabled (default)
            1 - Disabled by default, Enabled only when ICMP black hole detected
            2 - Always enabled, using the initial MSS value of tcp_base_mss
            system internally enables bit values for point 1&2
            For test purpose,
            Idea is to check traffic works fine on configuring values
            Vm's across compute node
        steps:
            1. create 1 VN and launch 2 VMs in same compute node 
            2. client and server VMs in same compute node
            3. configure tcp_mtu_probe to 0, 1, 2
            4. send icmp traffic assert if ping fails 
            5. send tcp traffic assert if tcp traffic fails
        Pass criteria:
            1. If icmp/tcp traffic work fine configuring tcp_mtu_probe values 
        """
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0],image_name='ubuntu-traffic')
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0],image_name='ubuntu-traffic')
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        client = client_fixtures[0]
        server = server_fixtures[0]
        for value in range(0,3):
            self.configure_tcp_mtu_probe(client,server,value)
            self.verify_icmp_traffic(client,server)
            self.verify_tcp_traffic(client,server, value)
        return True
