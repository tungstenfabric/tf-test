'''
This FT automation implementation will check the bond configuration status

Tested on dpdk compute Bond configuration 
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because
from tcutils.contrail_status_check import ContrailStatusChecker 
from common.contrail_services import *
import test

class TestDpdkBondStatus(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestDpdkBondStatus, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestDpdkBondStatus, cls).tearDownClass()

    def check_phy_interface_status(self,compute_ip):
        """ function to check the physical interface staus"""
        self.logger.info(compute_ip)
        cmd = "vif --get 0 | grep Interface"
        vif_out = self.inputs.run_cmd_on_server(compute_ip, cmd)
        assert vif_out, "no output of vif --list"
        self.logger.info(vif_out)
        output = vif_out.strip().split('\r\n')
        for line in output:
            self.logger.info(output)
            keys = ["Fabric Interface","Slave Interface"]
            if any(word in line for word in keys):
                if "Fabric Interface:" in  line:
                    assert "Status: UP" in line,"Interface Status is not up"
                if "Slave Interface" in line:
                    assert "Status: UP" in line, "Interface Status is not UP"
            else:
                continue
        return True
    #end check_phy_interface_status

    def dpdk_bond_status(self,compute_ip):
        """ 
           1- check physical interface status on all compute nodes
           2- bring-down vhost interface
           3- bring-down and bring-up bond interface
           4- bring-up vhost interface
           5- repeat step1
        """
        self.check_phy_interface_status(compute_ip)
        self.logger.info("Stoping vrouter agent and dpdk containers")
        dpdk_docker = self.inputs.run_cmd_on_server(compute_ip,\
                "docker stop vrouter_vrouter-agent-dpdk_1")
        self.logger.info(dpdk_docker)
        agent_docker = self.inputs.run_cmd_on_server(compute_ip,\
                "docker stop vrouter_vrouter-agent_1")
        self.logger.info(agent_docker)
        self.inputs.run_cmd_on_server(compute_ip,\
                "ifdown vhost0")
        self.logger.info("Bringing down bond interface")
        nmcli_output = self.inputs.run_cmd_on_server(compute_ip,\
                "nmcli connection down bond0")
        nmcli_output =  self.inputs.run_cmd_on_server(compute_ip,\
                "nmcli connection up bond0")
        self.logger.info(nmcli_output)
        self.logger.info("starting the containers")
        docker_output =  self.inputs.run_cmd_on_server(compute_ip,\
                "docker start vrouter_vrouter-agent_1")
        self.logger.info(docker_output)
        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
                "docker start vrouter_vrouter-agent-dpdk_1")
        self.logger.info(docker_output)
        self.inputs.run_cmd_on_server(compute_ip, "ifup vhost0")
        cluster_status, error_nodes = ContrailStatusChecker(self.inputs
                ).wait_till_contrail_cluster_stable(compute_ip, tries=20)
        assert cluster_status, 'error nodes and services:%s' % (error_nodes)
        self.check_phy_interface_status(compute_ip)
        return True
    #end dpdk_bond_status
        
    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(dpdk_cluster=False)
    def test_dpdk_bond_status(self):
        """ check dpdk bond status on compute node """
        compute_ip = self.inputs.compute_ips[0]
        self.dpdk_bond_status(compute_ip)
        return True
