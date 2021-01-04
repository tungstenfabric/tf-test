from __future__ import absolute_import
from tcutils.wrappers import preposttest_wrapper
import os
import test
from vn_test import *
from vm_test import * 
from tcutils.util import *
from vcenter import *
from common.contrail_test_init import *
from common.base import *
from common.device_connection import NetconfConnection
from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device

class TestNHLimit(GenericTestBase):
    vn_fixtures=[]
    vm_fixtures=[]
    def verify_nh_indexes(self, compute, Range):
        cmd = "contrail-tools nh --list | grep Id | wc -l"
        nh_indexes = run_cmd_on_server(cmd, compute, username='root', password='c0ntrail123')
        if Range[0] <= int(nh_indexes) <= Range[1]:
            self.logger.debug("nh_indexes are populated and in range")
        else:
            assert False, "nh_indexes are not in range"
    
    def set_nh_limit(self, nh_limit, compute, agent_mode=None, mpls_limit=None, modify=False):
        if modify == True:
            if agent_mode == 'dpdk':
                if mpls_limit is not None:
                    nh_mpls_limit_cmd = '''sed -i '/# base command/ a DPDK_COMMAND_ADDITIONAL_ARGS="--vr_nexthops= --vr_mpls_labels="' entrypoint.sh'''
                    updated_cmd = nh_mpls_limit_cmd[:71] + nh_limit + nh_mpls_limit_cmd[71:89] + mpls_limit + nh_mpls_limit_cmd[89:]
                else:
                    nh_limit_cmd = '''sed -i '/# base command/ a DPDK_COMMAND_ADDITIONAL_ARGS="--vr_nexthops="' entrypoint.sh'''
                    updated_cmd = nh_limit_cmd[:71] + nh_limit + nh_limit_cmd[71:]
                cmds = ['docker cp contrail-vrouter-agent-dpdk:/entrypoint.sh .', 'cp entrypoint.sh entrypoint_backup.sh', updated_cmd]
                for cmd in cmds:
                    run_cmd_on_server(cmd, compute, username='root', password='c0ntrail123')

            else:
                if mpls_limit is not None:
                    nh_mpls_limit_cmd = '''sed -i '/VROUTER_GATEWAY/ a VROUTER_MODULE_OPTIONS="vr_nexthops= vr_mpls_labels="' /etc/contrail/common_vrouter.env'''
                    updated_cmd = nh_mpls_limit_cmd[:64] + nh_limit + nh_mpls_limit_cmd[64:80] + mpls_limit +  nh_mpls_limit_cmd[80:]
                else:
                    nh_limit_cmd = '''sed -i '/VROUTER_GATEWAY/ a VROUTER_MODULE_OPTIONS="vr_nexthops="' /etc/contrail/common_vrouter.env'''
                    updated_cmd = nh_limit_cmd[:64] + nh_limit + nh_limit_cmd[64:]
                agent_file_backup_cmd = "cp /etc/contrail/common_vrouter.env /etc/contrail/common_vrouter_backup.env"
                cmds = [agent_file_backup_cmd, updated_cmd]
                for cmd in cmds:
                    run_cmd_on_server(cmd, compute, username='root', password='c0ntrail123')   
            
        if agent_mode == 'dpdk':
            cmds = ['docker cp entrypoint.sh contrail-vrouter-agent-dpdk:/entrypoint.sh', 'docker stop vrouter_vrouter-agent-dpdk_1', 'docker start vrouter_vrouter-agent-dpdk_1'] 
        else:
            cmds = ['docker stop vrouter_vrouter-agent_1', 'ifdown vhost0', 'cd /etc/contrail/vrouter/; docker-compose down; docker-compose up -d']
        for cmd in cmds:
            run_cmd_on_server(cmd, compute, username='root', password='c0ntrail123')
        self.verify_nh_limit(compute, nh_limit, mpls_limit)

    def verify_nh_limit(self, compute, nh_limit, mpls_limit=None):
        verify_nh_limit_cmd = "contrail-tools vrouter --info | awk '{print $3}' | awk 'NR==6'" 
        nh_limit_set=run_cmd_on_server(verify_nh_limit_cmd, compute, username='root', password='c0ntrail123')
        if nh_limit_set==nh_limit:
            self.logger.debug('Desired nh_limit %s is set on agent side' % nh_limit_set)
        else:
            assert False, "Proper nh_limit is not set"
            self.logger.debug('nhlimit set is %s' % nh_limit_set) 
        if mpls_limit is not None:
            verify_mpls_limit_cmd = "contrail-tools vrouter --info | awk '{print $4}' | awk 'NR==7'"
            mpls_limit_set=run_cmd_on_server(verify_mpls_limit_cmd, compute, username='root', password='c0ntrail123')
            if mpls_limit_set==mpls_limit:
                self.logger.debug('Desired mpls_limit %s is set on agent side' % mpls_limit_set)
            else:
                assert False, "Proper mpls_limit is not set"
                self.logger.debug('mplslimit set is %s' % mpls_limit_set)
 
    def reset_nh_limit(self, compute, agent_mode=None):
        nh_limit = '524288'
        mpls_limit = '5120'
        if agent_mode == 'dpdk':
            cmds = ['mv -f entrypoint_backup.sh entrypoint.sh']
        else:
            cmds = ['mv -f /etc/contrail/common_vrouter_backup.env /etc/contrail/common_vrouter.env']
        for cmd in cmds:
            run_cmd_on_server(cmd, compute, username='root', password='c0ntrail123')
        self.set_nh_limit(nh_limit=nh_limit, compute=compute, agent_mode=agent_mode, mpls_limit=mpls_limit)

    def add_routes_using_rtgen_mx_side(self, logicalsystem, table, subnet, count):
        rtgen_cmd = 'rtgen --op add --logical-system --table --prefix --count --next-hop-type reject'
        index_words = ['--logical-system', '--table', '--prefix', '--count']
        substring_list = []
        for i in range(len(index_words)):
            substring_list.append(rtgen_cmd.find(index_words[i]) + len(index_words[i]))
        updated_rtgen_cmd = rtgen_cmd[:substring_list[0] + 1] + logicalsystem + rtgen_cmd[substring_list[0]:substring_list[1] + 1] + table + rtgen_cmd[substring_list[1]:substring_list[2] + 1] + subnet + rtgen_cmd[substring_list[2]:substring_list[3] + 1] + count + rtgen_cmd[substring_list[3]:]
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        dev=Device(host=mx_params['mgmt_ip'], user=mx_params['ssh_username'], password=mx_params['ssh_password'])
        ss = StartShell(dev)
        ss.open()
        updated_rtgen_cmd_result = ss.run(updated_rtgen_cmd)
        print(updated_rtgen_cmd_result)
        ss.close()

    def remove_routes_mx_side(self, logicalsystem):
         deactivate_cmd = 'deactivate logical-systems ' + logicalsystem
         activate_cmd = 'activate logical-systems ' + logicalsystem
         cmds = [[deactivate_cmd], [activate_cmd]]
         mx_params = list(self.inputs.physical_routers_data.values())[0]
         nhLS_netconf = NetconfConnection(mx_params['mgmt_ip'])
         nhLS_netconf.connect()
         for i in range(len(cmds)):
             nhLS_netconf.config(cmds[i])
         nhLS_netconf.disconnect()
          

    def create_vmvn_for_nhlimittest(self, compute, vn_count):
        for i in range(vn_count):
            vn_fixture = self.create_vn()
            assert vn_fixture.verify_on_setup()
            self.vn_fixtures.append(vn_fixture)
            vn_fixture.add_route_target(router_asn=64512, route_target_number=190)
            vm_fixture = self.create_vm(vn_fixture= vn_fixture, node_name=compute)
            assert vm_fixture.wait_till_vm_is_up()
            assert vm_fixture.verify_on_setup()
            self.vm_fixtures.append(vm_fixture)
        vn1_name = self.vn_fixtures[0].vn_fq_name
        vn2_name = self.vn_fixtures[1].vn_fq_name
        rule1 = self._get_network_policy_rule(src_vn=vn1_name, dst_vn=vn2_name, action='pass')
        rule2 = self._get_network_policy_rule(src_vn=vn2_name, dst_vn=vn1_name, action='pass')
        vn12_pol = self.create_policy(rules=[rule1, rule2])
        self.apply_policy(vn12_pol, [self.vn_fixtures[0], self.vn_fixtures[1]])
        
    
    def get_compute(self, agent_mode=None):
        dpdk_computes=[]
        kernel_computes=[]
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get('vrouter').get('AGENT_MODE') == 'dpdk':
                dpdk_computes.append(self.inputs.host_data[host]['name'])
            else:
                kernel_computes.append(self.inputs.host_data[host]['name'])
        if agent_mode=='dpdk':
            return dpdk_computes[0]
        else:
            return kernel_computes[0]

    def get_prefix_count(self, nh_limit, vn_count):
        return str(int(int(nh_limit)/vn_count))

    def ping_after_nh_index(self):
        assert self.vm_fixtures[0].ping_with_certainty(self.vm_fixtures[1].vm_ip)

class TestNHLimitKernel(TestNHLimit):
    subnet = '11.1.1.1/32'
    logicalsystem = ['nh_LS100', 'nh_LS200']
    table =  ['_proj_LS100.inet.0', '_proj_LS200.inet.0']
    agent_mode=None
    vn_count = 10
    @preposttest_wrapper
    def test_nh_limit_one_million(self):
        '''
        Description: Change nhLimit to 1 million and verify the number of nh indexes on agent side.
        Test Steps: 
                   1. Pump routes on mx side
                   2. Set 1 million nh limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify 1 million nh_indexes on agent side
                   5. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit = '1000000'
        count = self.get_prefix_count(nh_limit, self.vn_count)
        nh_index_Range=[]
        nh_index_Range.append(int(nh_limit) - 5)
        nh_index_Range.append(int(nh_limit))
        compute = self.get_compute()
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit, compute=compute, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute=compute)

    @preposttest_wrapper
    def test_nh_limit_change(self):
        '''
        Test Steps:
                   1. Pump routes 800000 on mx side
                   2. Set 600000 nh limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify that only 600000 nh_indexes are on agent side
                   5. Verify ping between any two VMs
                   6. Set 800000 nh limit on agent side
                   7. Verify that 800000 nh_indexes are on agent side
                   8. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit1 = '600000'
        nh_limit2 = '800000'
        count = self.get_prefix_count(nh_limit2, self.vn_count)
        nh_index_Range1=[]
        nh_index_Range.append(int(nh_limit1) - 5)
        nh_index_Range.append(int(nh_limit1))
        nh_index_Range2=[]
        nh_index_Range.append(int(nh_limit2) - 5)
        nh_index_Range.append(int(nh_limit2))
        compute = self.get_compute()
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit1, compute=compute, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range1)
        self.ping_after_nh_index()
        self.reset_nh_limit(compute=compute)
        self.set_nh_limit(nh_limit=nh_limit2, compute=compute, modify=True)
        self.verify_nh_indexes(compute, nh_index_Range2)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute=compute)

    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_nh_limit_change_with_mpls(self):
        '''
        Test Steps:
                   1. Pump routes 800000 on mx side
                   2. Set 600000 nh limit and 10000 mpls_limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify that only 600000 nh_indexes are on agent side
                   5. Verify ping between any two VMs
                   6. Set 800000 nh limit on agent side
                   7. Verify that 800000 nh_indexes are on agent side
                   8. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit1 = '600000'
        nh_limit2 = '800000'
        mpls_limit = '10000'
        count = self.get_prefix_count(nh_limit2, self.vn_count)
        nh_index_Range1=[]
        nh_index_Range.append(int(nh_limit1) - 5)
        nh_index_Range.append(int(nh_limit1))
        nh_index_Range2=[]
        nh_index_Range.append(int(nh_limit2) - 5)
        nh_index_Range.append(int(nh_limit2))
        compute = self.get_compute()
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit1, compute=compute, mpls_limit=mpls_limit, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range1)
        self.ping_after_nh_index()
        self.reset_nh_limit(compute=compute)
        self.set_nh_limit(nh_limit=nh_limit2, compute=compute, modify=True)
        self.verify_nh_indexes(compute, nh_index_Range2)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute=compute)


    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_default_nh_limit(self):
        '''
        Description: Verify default nh_limit and verify the number of nh indexes on agent side.
        Test Steps:
                   1. Verify default nh_limit as 524288 and default mpls_limit on agent side
                   2. Pump routes on mx side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify 524288 nh_indexes on agent side
                   5. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit = '524288'
        mpls_limit = '5120'
        count = self.get_prefix_count(nh_limit, self.vn_count)
        nh_index_Range=[]
        nh_index_Range.append(int(nh_limit) - 5)
        nh_index_Range.append(int(nh_limit))
        compute = self.get_compute()
        self.verify_nh_limit(compute, nh_limit, mpls_limit)
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)

class TestNHLimitDpdk(TestNHLimit):
    subnet = '11.1.1.1/32'
    logicalsystem = ['nh_LS100', 'nh_LS200']
    table =  ['_proj_LS100.inet.0', '_proj_LS200.inet.0']
    agent_mode='dpdk'
    vn_count = 10
    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_nh_limit_one_million(self):
        '''
        Description: Change nhLimit to 1 million and verify the number of nh indexes on agent side.
        Test Steps:
                   1. Pump routes on mx side
                   2. Set 1 million nh limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify 1 million nh_indexes on agent side
                   5. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit = '1000000'
        count = self.get_prefix_count(nh_limit, self.vn_count)
        nh_index_Range=[]
        nh_index_Range.append(int(nh_limit) - 5)
        nh_index_Range.append(int(nh_limit))
        compute = self.get_compute(self.agent_mode)
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit, compute=compute, agent_mode=self.agent_mode, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute, self.agent_mode)

    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_nh_limit_change(self):
        '''
        Test Steps:
                   1. Pump routes 800000 on mx side
                   2. Set 600000 nh limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify that only 600000 nh_indexes are on agent side
                   5. Verify ping between any two VMs
                   6. Set 800000 nh limit on agent side
                   7. Verify that 800000 nh_indexes are on agent side
                   8. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit1 = '600000'
        nh_limit2 = '800000'
        count = self.get_prefix_count(nh_limit2, self.vn_count)
        nh_index_Range1=[]
        nh_index_Range.append(int(nh_limit1) - 5)
        nh_index_Range.append(int(nh_limit1))
        nh_index_Range2=[]
        nh_index_Range.append(int(nh_limit2) - 5)
        nh_index_Range.append(int(nh_limit2))
        compute = self.get_compute()
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit1, compute=compute, agent_mode=self.agent_mode, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range1)
        self.ping_after_nh_index()
        self.reset_nh_limit(compute=compute, agent_mode=self.agent_mode)
        self.set_nh_limit(nh_limit=nh_limit2, compute=compute, agent_mode=self.agent_mode, modify=True)
        self.verify_nh_indexes(compute, nh_index_Range2)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute=compute, agent_mode=self.agent_mode)

    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_nh_limit_change_with_mpls(self):
        '''
        Test Steps:
                   1. Pump routes 800000 on mx side
                   2. Set 600000 nh limit and 10000 mpls_limit on agent side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify that only 600000 nh_indexes are on agent side
                   5. Verify ping between any two VMs
                   6. Set 800000 nh limit on agent side
                   7. Verify that 800000 nh_indexes are on agent side
                   8. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit1 = '600000'
        nh_limit2 = '800000'
        mpls_limit = '10000'
        count = self.get_prefix_count(nh_limit2, self.vn_count)
        nh_index_Range1=[]
        nh_index_Range.append(int(nh_limit1) - 5)
        nh_index_Range.append(int(nh_limit1))
        nh_index_Range2=[]
        nh_index_Range.append(int(nh_limit2) - 5)
        nh_index_Range.append(int(nh_limit2))
        compute = self.get_compute()
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.set_nh_limit(nh_limit=nh_limit1, compute=compute, agent_mode=self.agent_mode, modify=True)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range1)
        self.ping_after_nh_index()
        self.reset_nh_limit(compute=compute, agent_mode=self.agent_mode)
        self.set_nh_limit(nh_limit=nh_limit2, compute=compute, agent_mode=self.agent_mode, mpls_limit=mpls_limit, modify=True)
        self.verify_nh_indexes(compute, nh_index_Range2)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)
        self.reset_nh_limit(compute=compute, agent_mode=self.agent_mode)

    @test.attr(type=['nh_limit_test'])
    @preposttest_wrapper
    def test_default_nh_limit(self):
        '''
        Description: Verify default nh_limit and verify the number of nh indexes on agent side.
        Test Steps:
                   1. Verify default nh_limit as 524288 and default mpls_limit on agent side
                   2. Pump routes on mx side
                   3. Create 10 VNs with route target and 1 VM in each VN on any one compute
                   4. Verify 524288 nh_indexes on agent side
                   5. Verify ping between any two VMs
        Pass criteria: Nh limit should be properly set and nh indexes should be same in number as nh_limit
        Maintainer: rsetru@juniper.net
        '''
        nh_limit = '524288'
        mpls_limit = '5120'
        count = self.get_prefix_count(nh_limit, self.vn_count)
        nh_index_Range=[]
        nh_index_Range.append(int(nh_limit) - 5)
        nh_index_Range.append(int(nh_limit))
        compute = self.get_compute(self.agent_mode)
        self.verify_nh_limit(compute, nh_limit, mpls_limit)
        for i in range(len(self.logicalsystem)):
            self.add_routes_using_rtgen_mx_side(self.logicalsystem[i], self.table[i], self.subnet, count)
        self.create_vmvn_for_nhlimittest(compute, self.vn_count)
        self.verify_nh_indexes(compute, nh_index_Range)
        self.ping_after_nh_index()
        for log_sys in self.logicalsystem:
            self.remove_routes_mx_side(log_sys)

