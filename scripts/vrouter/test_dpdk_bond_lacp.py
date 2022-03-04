"""
This FT automation implementation will check LACP convergence and configure
LACP_RATE  bond interface configuration
Tested on dpdk compute Bonded configuration
"""
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
import test
from tcutils.util import skip_because
from tcutils.contrail_status_check import ContrailStatusChecker
from common.contrail_services import *
class TestLacp(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestLacp, cls).setUpClass()
        cls.agent_inspect_h = cls.connections.agent_inspect

    @classmethod
    def tearDownClass(cls):
        super(TestLacp, cls).tearDownClass()

    def bond_lacp_config(self,compute_ip):
        """ 
        1- Read current LACP configuration
        2- configure LACP_RATE 1 in ifcfg-vhost
        3- verify LACP configured convergence values
        """ 
        #import pdb;pdb.set_trace()
        ifcfg_vhost0_path = "/etc/sysconfig/network-scripts/ifcfg-vhost0"
        cat_cmd = "cat " + ifcfg_vhost0_path
        self.inputs.run_cmd_on_server(compute_ip,\
                "cp " + ifcfg_vhost0_path + " /etc/sysconfig/network-scripts/ifcfg-vhost0.bkp")
        out = self.inputs.run_cmd_on_server(compute_ip,"cat_cmd")
        if "LACP_RATE" in out:
            if "LACP_RATE=1" in out:
                self.logger.info("LACP_RATE is already 1")
            else:
                com = "sed -i 's/LACP_RATE=0/LACP_RATE=1/g' /etc/sysconfig/network-scripts/ifcfg-vhost0"
                out = self.inputs.run_cmd_on_server(compute_ip)
        else:
            command = "echo \"LACP_RATE=1\" >> /etc/sysconfig/network-scripts/ifcfg-vhost0"
            self.inputs.run_cmd_on_server(compute_ip, command)
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
        bond0_output = self.inputs.run_cmd_on_server(compute_ip,\
                "cat /proc/net/bonding/bond0")
        self.logger.info(bond0_output)
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
        self.logger.info("ifup vhost0")
        self.inputs.run_cmd_on_server(compute_ip,\
                "ifup vhost0")
        cluster_status, error_nodes = ContrailStatusChecker(self.inputs
                ).wait_till_contrail_cluster_stable(compute_ip, tries=20)
        assert cluster_status, 'error nodes and services:%s' % (error_nodes)

        ifcfg_vhost_cmd = " ifconfig vhost0 | head -n 1"
        ifcfg_vh_out = self.inputs.run_cmd_on_server(compute_ip,\
                ifcfg_vhost_cmd)
        ''' check vhost0 is UP post ifdown/ifup vhost'''
        self.logger.info(ifcfg_vh_out)
        if ifcfg_vh_out == '':
            assert False, "no output of ifconfig  vhost command"
        else:
           if not "vhost0" in ifcfg_vh_out:
               assert False, "vhost0 is not available"
           else:
               if not "UP" in ifcfg_vh_out:
                    assert False, "vhost0 is not UP"
           self.logger.info(ifcfg_vh_out)
            
        '''Use dpdkinfo tool command to check the bond LACP status'''
        dpdkinfo_cmd = "contrail-tools dpdkinfo -b | grep LACP"
        dpdkinfo_out = self.inputs.run_cmd_on_server(compute_ip, dpdkinfo_cmd)
        self.logger.info(dpdkinfo_out)
        if dpdkinfo_out == '':
            assert False, "no output of dpdkinfo command"
        else:
            if not "LACP Rate" in dpdkinfo_out:
                assert False, "lacp_rate is not available"
            else:
                if not "fast" in dpdkinfo_out:
                    assert False, "lacp config failed"
            self.logger.info(dpdkinfo_out)
        '''Restore initial LACP configuration'''
        self.inputs.run_cmd_on_server(compute_ip,\
            "cat " + ifcfg_vhost0_path + ".bkp > "  + ifcfg_vhost0_path)
        return True 
    #end bond_lacp_config

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(min_nodes=2, dpdk_cluster=False)
    def test_bond_lacp_config(self):
        ''' configure LACP on bond interface of dpdk computes'''
        compute_ip = self.inputs.compute_ips[0]
        self.bond_lacp_config(compute_ip)
        return True
