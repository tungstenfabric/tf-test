from __future__ import absolute_import
from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import *
import test
from alarm_test import *
from policy_test import *
import time
from datetime import datetime

class TestScaleAlarm(GenericTestBase):
    
    @classmethod
    def setUpClass(cls):
        super(TestScaleAlarm, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(TestScaleAlarm, cls).tearDownClass()
    
    @test.attr(type=['scale_alarm'])
    @preposttest_wrapper
    def test_alarm_scaling(self):
        '''
        1.scale alarms to 1k  and timeit
        2.Verify creation of alarms
        3.Verify contrail-status
        4.At the end of batch creation restart alarm-gen
        5.Verify contrail-status
        '''
        scale_number = 1000
        scaled_vns = 0
        restart_services = ['analytics-api','alarmgen']
        exp1 = {'operation': '>=', 'operand1': "UveVirtualNetworkConfig.total_acl_rules",
                'operand2': {'json_value': '1'}}
        project_name = self.project.project_name
        alarm_name = get_random_name('scale_alarm')
        alarm_fix = self.create_alarm(
            [exp1], alarm_name, ['virtual-network'], parent_type='global', project_fixture=self.project )
        pol_fix = self.create_policy()
        n_vns = scale_number
        n_process = 1
        cmd = "python tools/scale/scale_config.py --api_server_ip %s --keystone_ip %s \
                --n_vns %s --vnc  --n_process %s --project %s"%(self.inputs.cfgm_ips[0], self.inputs.cfgm_ips[0],
                                                    n_vns, n_process, project_name)
        try:
            output= subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError:
            pass
        vns = self.get_vn_list()
        self.bind_policy(pol_fix, vns)
        self.check_alarms(scale_number)
        assert self.inputs.verify_state()
        for service in restart_services:
            self.inputs.restart_containers(self.inputs.collector_ips, service)
        self.delete_vns(vns)
        self.logger.info('Total alarms scaled successfully')

    def create_alarm(self, exp_list, alarm_name='test_alarm', uve_keys=[], parent_type='global', project_fixture=None):
        alarm_fix = self.useFixture(AlarmFixture(
            connections=self.connections,
            alarm_name=alarm_name, parent_obj_type=parent_type,
            uve_keys=uve_keys, project_fixture=project_fixture))
        alarm_rules = alarm_fix.configure_alarm_rules(exp_list)
        alarm_fix.create(alarm_rules)
        self.logger.info('Alarm %s created successfully' %
                         alarm_fix.alarm_name)
        return alarm_fix
    
    def create_policy(self):
        policy_name = get_random_name('policy')
        rules = [
            {
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'any', 'src_ports': 'any',
                'dst_ports': 'any',
                'source_network': 'any',
                'dest_network': 'any',
            },
        ]
        return self.useFixture(PolicyFixture(project_fixture=self.project,
                        policy_name=policy_name, rules_list=rules, inputs=self.inputs,
                        connections=self.connections))
    
    def bind_policy(self, pol_fix,vn_list=[]):
        try:
            for vn_id in vn_list:
                vn_obj = self.vnc_lib.virtual_network_read(id=vn_id)
                policy_obj = self.vnc_lib.network_policy_read(fq_name=pol_fix.policy_fq_name)
                vn_obj.add_network_policy(policy_obj,VirtualNetworkPolicyType(sequence=SequenceType(major=0, minor=0)))
                self.vnc_lib.virtual_network_update(vn_obj)
        except:
            pass
    
    def unbind_policy(self, pol_fix, vn_list=[]):
        try:
            for vn_id in vn_list:
                vn_obj = self.vnc_lib.virtual_network_read(id=vn_id)
                policy_obj = self.vnc_lib.network_policy_read(fq_name=pol_fix.policy_fq_name)
                vn_obj.del_network_policy(policy_obj)
                self.vnc_lib.virtual_network_update(vn_obj)
        except:
            pass
    def delete_vns(self,vn_list=[]):
        try:
            for vn_id in vn_list:
                self.vnc_lib.virtual_network_delete(id=vn_id)
        except:
            pass
        while True:
            if not len(self.get_vn_list()):
                break;

    def get_vn_list(self):
        vns = self.vnc_lib.virtual_networks_list(parent_id=self.project.uuid)['virtual-networks']
        vn_uuids = []
        for vn in vns:
            vn_uuids.append(vn['uuid'])
        return vn_uuids
    
    def delete(self, pol_fix, vn_list=[]):
        #self.unbind_policy(pol_fix, vn_list)
        self.delete_vns(vn_list)
    
    def check_alarms(self, scale_number):
        no_alarms = 0
        start_time = datetime.now()
        while no_alarms <= scale_number:
            alarms = self.connections.ops_inspect.get_ops_alarms()['virtual-network']
            no_alarms =  len(alarms)
            self.logger.info('Alarms raised %s'%no_alarms)
            time.sleep(15)
        self.logger.info('Total alarms raised %s'%no_alarms)
        end_time = datetime.now() - start_time
        self.logger.info('Time taken to raise all alarms %s'%end_time)

