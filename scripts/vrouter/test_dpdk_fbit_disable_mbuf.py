'''
This FT automation implementation will perform to check feature bit negotiation on disable mergebuff dpdk
Tested on dpdk compute Bonded configuration
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because
import test
import time

#qcow2 image with mbuf disabled to be used to launch vm
image = 'contrail-nombuf-qcow2-image'

class TestFbitMergeBuffDisable(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestFbitMergeBuffDisable, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestFbitMergeBuffDisable, cls).tearDownClass()

    def check_fbit_with_disable_mbuf(self,compute_ip):
        cmd_get_fbit = "grep -irn \"SET FEATURES(original)\" /var/log/contrail/contrail-vrouter-dpdk.log"
        cmd_output = self.inputs.run_cmd_on_server(compute_ip,\
                cmd_get_fbit)
        self.logger.info(cmd_output)
        if cmd_output == '':
            assert False, "vrouter dpdk log not found"
        else:
            output = cmd_output.strip().split('\n')
        self.logger.info("output is :",output[-1])
        hex_value = output[-1].split()[-1]
        int_value = int(hex_value, base=16)
        BIT_POS = 19
        self.logger.info("value is :",str(bin(int_value))[BIT_POS])
        merge_buf_disable = str(bin(int_value))[BIT_POS]
        if merge_buf_disable != '0':
            assert False,"test case failed!"
        return True
    #end check_fbit_with_disable_mbuf

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    @skip_because(dpdk_cluster=False)
    def test_fbit_disable_mbuf_dpdk(self):
        '''
        Description: 
        steps:
            1. Launch 1 VN, 1 VM in compute node with qcow2 image
            2. verify fbit when mergebuff disabled on dpdk compute
        Pass criteria:
            1. verify feature bit negotiation bit when mergebuff is disabled  
        '''
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        vm_fixture = self.create_vms(vn_fixture= vn1_fixture,count=1,node_name=compute_hosts[0], image_name=image)
        self.verify_vms(vm_fixture)
        compute_ip = self.inputs.compute_ips[0]
        self.check_fbit_with_disable_mbuf(compute_ip)
        #restart dpdk container and verify 
        docker_output = self.inputs.run_cmd_on_server(compute_ip,\
            "docker restart vrouter_vrouter-agent-dpdk_1")
        self.logger.info("docker output status: " + docker_output)
        time.sleep(10)
        self.check_fbit_with_disable_mbuf(compute_ip)
        return True
