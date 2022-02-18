'''
This FT automation implementation will perform GRO & GSO test
Test performed on dpdk bond configuration
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
import test
from tcutils.util import skip_because
from tcutils.contrail_status_check import ContrailStatusChecker 
from common.contrail_services import *
import time

class TestGroGso(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestGroGso, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestGroGso, cls).tearDownClass()

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(min_nodes=2, dpdk_cluster=False)
    def test_dpdk_gro_gso(self):
        '''
        Description: 
        Verify tcp traffic flow for intra-VN inter-Node traffic
        Vm's across compute node
        steps:
            1. create 1 VN and launch 2 VMs in each compute node 
            2. client VMs on same node and server VM on different node.
            3. Clear vif0/0 interface before sending traffic
            4. Send TCP traffic client to server port 5201 using iperf3  
            5. Read pps on physical interface vif 0/0 
            6. disable gro and gso feature configuring on vhost config 
            7. ifdown/ifup vhost0 to update config
            8. Repeat step 3 & 4
            9. Compare the TCP traffic pps in enable/disable case
        Pass criteria:
            1. If pps is more in feature enable case than disable 

        '''
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[1], image_name='ubuntu-traffic')
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0], image_name='ubuntu-traffic')
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        compute_ip = self.inputs.compute_ips[0]
        clr_cmd = "vif --clear 0"
        clr_out = self.inputs.run_cmd_on_server(compute_ip, clr_cmd)
        assert clr_out, "no output for vif --clear 0"
        #set parameters required for TCP traffic to send from src to dest VM
        proto = 'tcp'
        dport = 5201 
        sport = 10001
        assert self.send_nc_traffic(client_fixtures[0], server_fixtures[0], sport, dport, proto), "tcp traffic failed"
        vif_get_cmd = "vif --get 0 | grep bytes"
        vif_get_out = self.inputs.run_cmd_on_server(compute_ip, vif_get_cmd)
        assert vif_get_out, "no output for vif --get 0"
        self.logger.info(vif_get_out) 
        output = vif_get_out.strip().split('\r\n\t')
        rx_byte_cnt_en_gso = 0
        tx_byte_cnt_en_gro = 0
        self.logger.info(output)
        for line in output:
            if "bytes" not in line:
                assert False, "byte count is not present"
            else:
                if "RX packets" in line:
                    result = line.split()
                    byte_string = result[2].split(":")
                    rx_byte_cnt_en_gso = int(byte_string[1])
                if "TX packets" in line:
                    result = line.split()
                    byte_string = result[2].split(":")
                    tx_byte_cnt_en_gro = int(byte_string[1])
        self.logger.info(rx_byte_cnt_en_gso)   
        self.logger.info(tx_byte_cnt_en_gro)
        ifcfg_vhost0_path = "/etc/sysconfig/network-scripts/ifcfg-vhost0"
        cat_com = "cat " + ifcfg_vhost0_path
        self.inputs.run_cmd_on_server(compute_ip,\
                "cp " + ifcfg_vhost0_path + " /etc/sysconfig/network-scripts/ifcfg-vhost0.bkp")
        dpdk_add_command = "DPDK_COMMAND_ADDITIONAL_ARGS=\"--no-gso --no-gro\""
        command = "echo " + dpdk_add_command + " >> " + ifcfg_vhost0_path
        self.inputs.run_cmd_on_server(compute_ip,\
            command)
        self.logger.info(command)

        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
            "docker stop vrouter_vrouter-agent_1")
        self.logger.info("docker output status: " + docker_output)

        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
            "docker stop vrouter_vrouter-agent-dpdk_1")
        self.logger.info("docker output status: " + docker_output)
        
        ifdown_output = self.inputs.run_cmd_on_server(compute_ip,\
            "ifdown vhost0")
        self.logger.info("if output status: " + ifdown_output)

        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
            "docker start vrouter_vrouter-agent_1")
        self.logger.info("docker output status: " + docker_output)
        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
            "docker start vrouter_vrouter-agent-dpdk_1")
        self.logger.info("docker output status: " + docker_output)
        ifup_output = self.inputs.run_cmd_on_server(compute_ip,\
            "ifup vhost0")
        self.logger.info("if output status: " + ifup_output)
        cluster_status, error_nodes = ContrailStatusChecker(self.inputs
                ).wait_till_contrail_cluster_stable(compute_ip, tries=20)
        assert cluster_status, 'error nodes and services:%s' % (error_nodes)
        out = self.inputs.run_cmd_on_server(compute_ip,\
            "ifconfig vhost0 | head -n 1")
        assert out, "no output of ifconfig vhost command"
        if not "vhost0" in out:
            assert False, "vhost0 is not available"
        else:
            if not "UP" in out:
                assert False, "vhost0 is not UP"
        self.logger.info(out)
        #adding delay as facing issue while running tcp traffic
        time.sleep(180)
        clear_vif0 = self.inputs.run_cmd_on_server(compute_ip,"vif --clear 0")
        assert clear_vif0, "clear --vif error"
        ''' parameters for tcp traffic ''' 
        assert self.send_nc_traffic(client_fixtures[0], server_fixtures[0], sport, dport, proto), "tcp traffic failed"
        vif_get_out = self.inputs.run_cmd_on_server(
            compute_ip,"vif --get 0 | grep bytes")
        assert vif_get_out, "no output for vif --get 0"
        self.logger.info(vif_get_out)
        output = vif_get_out.strip().split('\r\n')
        rx_byte_cnt_dis_gso = 0
        tx_byte_cnt_dis_gro = 0
        for line in output:
            if "bytes" not in line:
                assert False, "byte count is not present"
            else:
                if "RX packets" in line:
                    result = line.split()
                    byte_string = result[2].split(":")
                    rx_byte_cnt_dis_gso = int(byte_string[1])
                if "TX packets" in line:
                    result = line.split()
                    byte_string = result[2].split(":")
                    tx_byte_cnt_dis_gro = int(byte_string[1])
        self.logger.info(rx_byte_cnt_dis_gso)
        self.logger.info(tx_byte_cnt_dis_gro)
        assert rx_byte_cnt_en_gso > rx_byte_cnt_dis_gso, "gso test failed"
        assert tx_byte_cnt_en_gro > tx_byte_cnt_dis_gro, "gro test failed"
        self.inputs.run_cmd_on_server(compute_ip,\
            "cat " + ifcfg_vhost0_path + ".bkp > "  + ifcfg_vhost0_path)
        return True
