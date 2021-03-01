from __future__ import absolute_import
from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import *
import test

class TestScaleConfig(GenericTestBase):
    
    @classmethod
    def setUpClass(cls):
        super(TestScaleConfig, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(TestScaleConfig, cls).tearDownClass()
        
    
    @test.attr(type=['scale_vn'])
    @preposttest_wrapper
    def test_vn_scaling(self):
        '''
        1.scale vns to 20k in a batch of 5k vns each and timeit
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 20000
        scaled_vns = 0
        restart_services = ['api-server','schema']
        while scaled_vns < scale_number:
            n_vns = 200
            n_process = 25
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_vns %s --vnc  --n_process %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_process)
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
        assert (total_vns/scale_number)*100 < 90, 'Not able to scale expected number of Vns'
        self.logger.info('Total Vns scaled successfully')
        
        
    @test.attr(type=['scale_port'])
    @preposttest_wrapper
    def test_port_scaling(self):
        '''
        1. scale ports to 200k in batch of 50k ports each and timeit
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 200000
        scaled_ports = 0
        restart_services = ['api-server','schema']
        while scaled_ports < scale_number :
            n_ports = 200
            n_process = 25
            n_vns = 10
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_vns %s --vnc  --n_process %s --n_ports %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_process, n_ports)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            ports = self.verify_scale_objects(object_type='port')
            assert self.inputs.verify_state()
            scaled_ports = scaled_ports + ports
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_ports = self.verify_scale_objects(object_type='vn')
        assert (total_ports/scale_number)*100 < 90, 'Not able to scale expected number of ports'
        self.logger.info('Total ports scaled successfully')
    
    @test.attr(type=['scale_sg'])
    @preposttest_wrapper
    def test_security_group_scaling(self):
        '''
        1. scale sgs to 60k in batch of 20k sgs each and timeit
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 60000
        scaled_sgs = 0
        restart_services = ['api-server','schema']
        while scaled_sgs < scale_number :
            n_sgs = 500
            n_process = 40
            n_sg_rules = 1
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_sgs %s --vnc  --n_process %s --n_sg_rules %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_sgs, n_process, n_sg_rules)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            sgs = self.verify_scale_objects(object_type='sg')
            assert self.inputs.verify_state()
            scaled_sgs = scaled_sgs + sgs
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_sgs = self.verify_scale_objects(object_type='sg')
        assert (total_sgs/scale_number)*100 < 90, 'Not able to scale expected number of sgs'
        self.logger.info('Total sgs scaled successfully')
    
    @test.attr(type=['scale_sg_rules'])
    @preposttest_wrapper
    def test_security_group_rules_scaling(self):
        '''
        1. scale sgs_rules to 200k in batch of 200k rules each and timeit
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 200000
        scaled_sgs_rules = 0
        restart_services = ['api-server','schema']
        while scaled_sgs < scale_number :
            n_sgs = 10
            n_process = 30
            n_sg_rules = 200
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_sgs %s --vnc  --n_process %s --n_sg_rules %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_sgs, n_process, n_sg_rules)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            sgs_rules = self.verify_scale_objects(object_type='sg_rules')
            assert self.inputs.verify_state()
            scaled_sgs_rules = scaled_sgs_rules + sgs_rules
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_sgs_rules = self.verify_scale_objects(object_type='sg_rules')
        assert (total_sgs_rules/scale_number)*100 < 90, 'Not able to scale expected number of sgs_rules'
        self.logger.info('Total sgs_rules scaled successfully')
    
    @test.attr(type=['scale_np'])
    @preposttest_wrapper
    def test_network_policy_scaling(self):
        '''
        1.scale network policy to 50k 
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 50000
        scaled_nps = 0
        restart_services = ['api-server','schema']
        while scaled_nps < scale_number :
            n_policies = 1000
            n_process = 50
            n_policy_rules = 1
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_policies %s --vnc  --n_process %s --n_policy_rules %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_policies, n_process, n_policy_rules)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            nps = self.verify_scale_objects(object_type='np')
            assert self.inputs.verify_state()
            scaled_nps = scaled_nps + nps
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_nps = self.verify_scale_objects(object_type='np')
        assert (total_nps/scale_number)*100 < 90, 'Not able to scale expected number of network policies'
        self.logger.info('Total network policies scaled successfully')
    
    @test.attr(type=['scale_np_rules'])
    @preposttest_wrapper
    def test_network_policy_rulues_scaling(self):
        '''
        1.scale network policy to 100k 
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 100000
        scaled_np_rules = 0
        restart_services = ['api-server','schema']
        while scaled_nps_rules < scale_number :
            n_policies = 100
            n_process = 1
            n_policy_rules = 1000
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_policies %s --vnc  --n_process %s --n_policy_rules %s --project admin"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_policies, n_process, n_policy_rules)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            np_rules = self.verify_scale_objects(object_type='np_rules')
            assert self.inputs.verify_state()
            scaled_np_rules = scaled_np_rules + np_rules
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_np_rules = self.verify_scale_objects(object_type='np_rules')
        assert (total_np_rules/scale_number)*100 < 90, 'Not able to scale expected number of network policies rules'
        self.logger.info('Total network policies rules scaled successfully')
    
    
    @test.attr(type=['scale_fip'])
    @preposttest_wrapper
    def test_fip_scaling(self):
        '''
        1.scale fips to 60k in batch of 20k fips each and timeit
        2.Verify creation after each batch creation
        3.Verify contrail-status
        4.At the end of batch creation restart api-server,schema
        5.Verify contrail-status
        '''
        scale_number = 60000
        scaled_fips = 0
        restart_services = ['api-server','schema']
        while scaled_fips < scale_number :
            n_fips = 800
            n_process = 25
            cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                    --n_fips %s --vnc  --n_process %s --project admin"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                       n_vns, n_process)
            try:
                output= subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError:
                pass
            fips = self.verify_scale_objects(object_type='fips')
            assert self.inputs.verify_state()
            scaled_fips = scaled_fips + fips
            for service in restart_services:
                self.inputs.restart_containers(self.inputs.cfgm_ips, service)
        total_fips = self.verify_scale_objects(object_type=fips)
        assert (total_fips/scale_number)*100 < 90, 'Not able to scale expected number of fips'
        self.logger.info('Total fips scaled successfully')
    
    @retry(tries=3)
    def verify_scale_objects(self, object_type='vn'):
        if object_type == 'vn':
            try:
                return len(self.connections.api_server_inspects[0].get_cs_vn_list())
            except:
                return False
        elif object_type == 'ports':
            try:
                return len(self.connections.nova_h.list_ports())
            except:
                return False
        elif object_type == 'sgs':
            try:
                return len(self.connections.quantum_h.security_groups())
            except:
                return False
        elif object_type == 'sg_rules':
            try:
                return len(self.connections.quantum_h.security_group_rules())
            except:
                return False
        elif object_type == 'nps':
            try:
                return len(self.connections.quantum_h.policy())
            except:
                return False
        elif object_type == 'np_rules':
            try:
                return len(self.connections.quantum_h.policy_rules())
            except:
                return False
        elif object_type == 'fips':
            try:
                return len(self.connections.api_server_inspects[0].get_cs_fip_list())
            except:
                return False
