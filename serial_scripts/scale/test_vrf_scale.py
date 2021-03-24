from __future__ import absolute_import
from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import *
import test
import logging

class TestScaleConfig(GenericTestBase):
    
    @classmethod
    def setUpClass(cls):
        super(TestScaleConfig, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(TestScaleConfig, cls).tearDownClass()
        
    
    @test.attr(type=['scale_vrf'])
    @preposttest_wrapper
    def test_control_node_vrf_scaling(self):
        '''
        1.scale vns with Fake VMs to 15k
        2.Verify creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 15000
        scaled_vns = 0
        restart_services = ['api-server','schema']
        
        n_vns = 15000
        n_vms = 1
        cmd = "python tools/scale/scale_fake_vms.py --api_server_ip %s --keystone_ip %s \
                --n_vns %s --vnc  --n_vms %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_vms)
        try:
            output= subprocess.check_output(cmd, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass
        
        cmd = "python tools/scale/activate-fakevm.py --computes %s --username %s \
                --password %s"%(self.inputs.cfgm_ips[1], self.inputs.cfgm_username[0],
                                                       self.inputs.cfgm_password[0])
        try:
            output= subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError:
            pass

        vns = self.verify_scale_objects(object_type='vn')
        assert self.inputs.verify_state()
        scaled_vns = scaled_vns + vns
        for service in restart_services:
            self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_vns = self.verify_scale_objects(object_type='vn')
        total_vrf = self.verify_scale_objects(object_type='vrf')
        assert (total_vrf/scale_number)*100 < 90, 'Not able to scale expected number of VRFs'
        self.logger.info('Total Vns scaled successfully')
        

    @test.attr(type=['scale_vrf'])
    @preposttest_wrapper
    def test_compute_node_vrf_scaling(self):
        '''
        1.scale vns with Fake VMs to 4k
        2.Verify creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 4000
        scaled_vns = 0
        restart_services = ['api-server','schema']
        
        n_vns = 4000
        n_vms = 1
        cmd = "python tools/scale/scale_fake_vms.py --api_server_ip %s --keystone_ip %s \
                --n_vns %s --vnc  --n_vms %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_vms)
        try:
            output= subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError:
            pass
        
        cmd = "python tools/scale/activate-fakevm.py --computes %s --username %s \
                --password %s"%(self.inputs.cfgm_ips[1], self.inputs.cfgm_username[0],
                                                       self.inputs.cfgm_password[0])
        try:
            output= subprocess.check_output(cmd, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass

        vns = self.verify_scale_objects(object_type='vn')
        assert self.inputs.verify_state()
        scaled_vns = scaled_vns + vns
        for service in restart_services:
            self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_vns = self.verify_scale_objects(object_type='vn')
        total_vrf = self.verify_scale_objects(object_type='vrf')
        assert (total_vrf/scale_number)*100 < 90, 'Not able to scale expected number of VRFs'
        self.logger.info('Total Vns scaled successfully')

    @test.attr(type=['scale_vrf'])
    @preposttest_wrapper
    def test_vm_scaling(self):
        '''
        1.scale Fake VMs to 15K per VN
        2.Verify creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 15000
        scaled_vns = 0
        restart_services = ['api-server','schema']
        
        n_vns = 1
        n_vms = 15000
        cmd = "python tools/scale/scale_fake_vms.py --api_server_ip %s --keystone_ip %s \
                --n_vns %s --vnc  --n_vms %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_vms)
        try:
            output= subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError:
            pass
        
        cmd = "python tools/scale/activate-fakevm.py --computes %s --username %s \
                --password %s"%(self.inputs.cfgm_ips[1], self.inputs.cfgm_username[0],
                                                       self.inputs.cfgm_password[0])
        try:
            output= subprocess.check_output(cmd, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass

        vns = self.verify_scale_objects(object_type='vn')
        assert self.inputs.verify_state()
        scaled_vns = scaled_vns + vns
        for service in restart_services:
            self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_vns = self.verify_scale_objects(object_type='vn')
        total_vrf = self.verify_scale_objects(object_type='vrf')
        assert (total_vrf/scale_number)*100 < 90, 'Not able to scale expected number of VMs'
        self.logger.info('Total Vns scaled successfully')


    @retry(tries=3)
    def verify_scale_objects(self, object_type='vn'):
        if object_type == 'vn':
            try:
                return len(self.connections.api_server_inspects[0].get_cs_vn_list())
            except:
                return False
        elif object_type == 'vrf':
            try:
                return len(self.connections.api_server_inspects[0].get_cs_routing_instances(total_vns))
            except:
                return False

