from __future__ import absolute_import, unicode_literals
from vnc_api.vnc_api import *
from vcenter import *
import test
from tcutils.commands import ssh, execute_cmd, execute_cmd_out
import time
import inspect
from common import isolated_creds
from builtins import str
from builtins import range
import traffic_tests
from vn_test import *
from vm_test import *
from floating_ip import *
from policy_test import *
from user_test import UserFixture
from multiple_vn_vm_test import *
from tcutils.wrappers import preposttest_wrapper
sys.path.append(os.path.realpath('tcutils/pkgs/Traffic'))
from traffic.core.profile import create, ContinuousProfile
from tcutils.contrail_status_check import ContrailStatusChecker
from common.l3_mh.base import BaseL3Multihoming
from tcutils.cores import get_service_crashes
from tcutils.tcpdump_utils import *
from compute_node_test import ComputeNodeFixture

class TestL3Multihoming(BaseL3Multihoming):
    @classmethod
    def setUpClass(cls):
        super(TestL3Multihoming, cls).setUpClass()
        cls.l3mh_setup_check_done = False

    @classmethod
    def tearDownClass(cls):
        super(TestL3Multihoming, cls).tearDownClass()

    def setUp(self):
        super(TestL3Multihoming, self).setUp()
        if TestL3Multihoming.l3mh_setup_check_done:
            return
        l3mh_config = self.verify_vrouter_agent_l3_multihoming_parameters()
        if not l3mh_config:
            self.logger.error("L3 Multihoming configuration on compute FAILED")
            assert False
        vhost0_config = self.verify_vhost0_interface_on_l3mh_compute()
        if not vhost0_config:
            self.logger.error("L3 Multihoming vhost0 configuration on compute FAILED")
            assert False
        phy_intf_and_routes = self.verify_physical_interfaces_and_routes_in_default_vrf_on_l3mh_compute()
        if not phy_intf_and_routes:
            self.logger.error("L3 Multihoming physical interface and route verification on compute FAILED")
            assert False
        verify_bgp_and_loopback_ip = self.verify_compute_loopbackip_and_controller_connectivity()
        if not verify_bgp_and_loopback_ip:
            self.logger.error("loopback ip or control node ip not reachable from compute node")
            assert False
        TestL3Multihoming.l3mh_setup_check_done = True

    @preposttest_wrapper
    def test_contrail_status(self):
        '''
           Verify cluster has all contrail services Active,
           when l3 multihoming is enabled on computes.
        '''
        cluster_status, error_nodes = ContrailStatusChecker(self.inputs).wait_till_contrail_cluster_stable(tries=10)
        for key in error_nodes.keys():
            node_failed_services = error_nodes[key]
            if len(node_failed_services.keys()) > 1:
                self.logger.error("Multiple services failed to come up on host %s" %key)
            else:
                for service in node_failed_services.keys():
                    if 'nodemgr' in service:
                        self.logger.error("Ignore nodemgr service failed to come up on host %s due to possible failed ntp sync" %key)
                        cluster_status = True
        assert cluster_status, 'All nodes and services not up. Failure nodes are: %s' % (
                    error_nodes)

        crashes = get_service_crashes(self.inputs)
        if crashes:
            self.logger.info("Test is running with crashes in l3mh cluster: %s", crashes)
            assert False, "Crash seen in l3mh cluster test FAILED"

        return True
    # end test_contrail_status

    @preposttest_wrapper
    def test_dns_service(self):
        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):
            self.logger.info("Vdns is not supported on Dpdk compute TEST SKIPPED")
            return (False, "Skipping Test. ")
        self.vdns_with_cn_dns_agent_restart('')
        return True
    #end test_dns_service

    @preposttest_wrapper
    def test_traffic_with_policy(self):
        '''
        Create 2 Vns and allow icmp traffic between them and validate with pings
        Update the policy to deny the same traffic
        Check that pings fail
        Verify on vm delete routes for vm is removed
        '''

        result = True
        if len(self.inputs.compute_ips) < 2:
            return (False, 'Skipping Test. Need atleast two compute nodes')
        vn1_fixture = self.create_vn()
        vn2_fixture = self.create_vn()
        policy_name = get_random_name('policy1')
        rules = [
            {
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'icmp',
                'source_network': vn1_fixture.vn_name,
                'dest_network': vn2_fixture.vn_name,
            },
        ]

        policy_fixture = self.setup_policy_between_vns(vn1_fixture,
            vn2_fixture, rules)
        assert vn1_fixture.verify_on_setup()
        assert vn2_fixture.verify_on_setup()

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vm1_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm1-vn1'),
                              image_name='cirros',
                              node_name=vm1_node_name)
        vm12 = self.create_vm(vn1_fixture,
                              get_random_name('vm2-vn1'),
                              image_name='cirros',
                              node_name=vm2_node_name)
        vm2_fixture = self.create_vm(vn2_fixture)
        vm1_fixture.wait_till_vm_is_up()
        vm2_fixture.wait_till_vm_is_up()
        vm12.wait_till_vm_is_up()

        prefix_vm1 = vm1_fixture.vm_ip + '/32'
        vm1_vrf_id = vm1_fixture.get_vrf_id(vn1_fixture.vn_fq_name,
                                       vn1_fixture.vrf_name)
        vm1_route_on_local_compute = self.get_route_nh_from_host(self.inputs.compute_ips[0], vm1_vrf_id, prefix_vm1)
        vm1_route_on_local_compute[0]['nh']['type'] == "Encap"

        #Verify nexthops for vm route encap for local vm , tunnel for remote vm
        prefix_vm12 = vm12.vm_ip + '/32'
        vm2_remote_rt = self.get_route_nh_from_host(self.inputs.compute_ips[0], vm1_vrf_id, prefix_vm12)
        vm2_remote_rt[0]['nh']['type'] == "TUNNEL"
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
            'Ping failed between VNs with allow-policy')

        assert vm1_fixture.ping_with_certainty(vm12.vm_ip), (
            'Ping failed between vm in same network')
        # Deny the same traffic, verify ping fails
        policy_id = policy_fixture.get_id()
        rules[0]['simple_action'] = 'deny'
        policy_entries = policy_fixture.get_entries()
        if type(policy_entries) is PolicyEntriesType:
            policy_entries.policy_rule[0].action_list.simple_action = 'deny'
            p_rules = policy_entries
        else:
            policy_entries['policy_rule'][0]['action_list']['simple_action'] = 'deny'
            p_rules = {'policy': {'entries':policy_entries}}
        policy_fixture.update_policy(policy_id, p_rules)
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip,
            expectation=False), ('Ping passed between VNs with deny-policy')

        # simulate delete, Shutoff VM, verify vm routes get deleted
        self.logger.info(
            'Executing nova stop to shutoff the VMs %s and %s' % (vm1_fixture.vm_name, vm12.vm_name))
        vm1_fixture.vm_obj.stop()
        vm12.vm_obj.stop()
        assert vm1_fixture.wait_till_vm_status('SHUTOFF'), ('Unable to '
            ' shutoff a VM')
        assert vm12.wait_till_vm_status('SHUTOFF'), ('Unable to '
            ' shutoff a VM')

        # Vm shutoff results in delete of vm route verify nh set to drop for vm route
        self.logger.info(
            'Verifying VM route entry is removed from agent after shutoff')
        vm1_route_on_local_compute = self.get_route_nh_from_host(self.inputs.compute_ips[0], vm1_vrf_id, prefix_vm1)
        vm1_route_on_remote_compute = self.get_route_nh_from_host(self.inputs.compute_ips[1], vm1_vrf_id, prefix_vm1)
        vm2_local_rt = self.get_route_nh_from_host(self.inputs.compute_ips[1], vm1_vrf_id, prefix_vm12)
        vm2_remote_rt = self.get_route_nh_from_host(self.inputs.compute_ips[0], vm1_vrf_id, prefix_vm12)

        '''if vm1_route_on_local_compute[0]['nh']['type'] != "Drop":
            self.logger.info(
                'VM route entry %s is not removed from agent on compute %s  after shutoff' % (prefix_vm1, vm1_node_name))
            result = result and False
        if vm1_route_on_remote_compute[0]['nh']['type'] != "Drop":
            self.logger.info(
                'VM route entry %s is not removed from agent on compute %s  after shutoff' % (prefix_vm1, vm2_node_name))
            result = result and False
        if vm2_local_rt[0]['nh']['type'] != "Drop":
            self.logger.info(
                'VM route entry %s is not removed from agent on compute %s  after shutoff' % (prefix_vm12, vm2_node_name))
            result = result and False
        if vm2_remote_rt[0]['nh']['type'] != "Drop":
            self.logger.info(
                'VM route entry %s is not removed from agent on compute %s  after shutoff' % (prefix_vm12, vm1_node_name))
            result = result and False
        '''
        return result
        #end test_traffic_with_policy

    @preposttest_wrapper
    def test_flow_stickiness_workload_in_same_vn_same_compute(self):
        '''
            Launch vm1 and vm2 in vn1 on same compute.
            ping vm1 from vm2, verify ping passes
            undelay_gw_index is -1 in flow entry, verify flow is local
        '''
        result = True
        vn1_fixture = self.create_vn()
        assert vn1_fixture.verify_on_setup()

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm1_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm1-vn1'),
                              image_name='cirros',
                              node_name=vm1_node_name)
        vm2_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm2-vn1'),
                              image_name='cirros',
                              node_name=vm2_node_name)
        vm1_fixture.wait_till_vm_is_up()
        vm2_fixture.wait_till_vm_is_up()

        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
            'Ping failed between VMs in vn1')

        # underlay gw index checks

        inspect_h1 = self.agent_inspect[vm1_fixture.vm_node_ip]
        flow_rec1 = None

        vn_fq_name=vm1_fixture.vn_fq_name
        compute_node_fixture = self.useFixture(ComputeNodeFixture(
                self.connections, vm1_fixture.vm_node_ip))
        fwd_flow, rev_flow = compute_node_fixture.get_flow_entry(
                                    source_ip = vm1_fixture.vm_ip,
                                    dest_ip = vm2_fixture.vm_ip,
                                    dest_port = '0',
                                    proto = '1')
        if fwd_flow:
            sport = fwd_flow.source_port
            flow_rec1 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm1_fixture.vm_ip,
                dip=vm2_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec1 = None
        if flow_rec1 is not None:
            self.logger.info('Verifying underlay_gw_index in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'underlay_gw_index', '255')
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to -1 in given flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
            self.logger.info('Verifying local flow in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'local_flow', 'yes')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if rev_flow:
            sport = rev_flow.source_port
            flow_rec2 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm2_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm2_fixture.vm_ip,
                dip=vm1_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec2 = None
        if flow_rec2 is not None:
            self.logger.info('Verifying underlay_gw_index in reverse flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'underlay_gw_index', '255')
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to -1 in given flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
            self.logger.info('Verifying local flow in reverse flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'local_flow', 'yes')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        return result
    # end test_flow_stickiness_workload_in_same_vn_same_compute

    @preposttest_wrapper
    def test_flow_stickiness_workload_in_same_vn_different_compute(self):
        '''
           Launch vm1 and vm2 on different computes in vn1.
           verify ping passes vm1<->vm2
           verify underlay_gw_index in fwd and rev flow.
           verify local flow flag in fwd and rev flow.
        '''

        if len(self.inputs.compute_ips) < 2:
            return (False, 'Skipping Test. Need atleast two compute nodes')
        result = True
        vn1_fixture = self.create_vn()
        assert vn1_fixture.verify_on_setup()

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vm1_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm1-vn1'),
                              image_name='cirros',
                              node_name=vm1_node_name)
        vm2_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm2-vn1'),
                              image_name='cirros',
                              node_name=vm2_node_name)
        vm1_fixture.wait_till_vm_is_up()
        vm2_fixture.wait_till_vm_is_up()

        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
            'Ping failed between VMs in vn1')

        # underlay gw index checks

        inspect_h1 = self.agent_inspect[vm1_fixture.vm_node_ip]
        flow_rec1 = None

        vn_fq_name=vm1_fixture.vn_fq_name
        compute_node_fixture = self.useFixture(ComputeNodeFixture(
                self.connections, vm1_fixture.vm_node_ip))
        fwd_flow, rev_flow = compute_node_fixture.get_flow_entry(
                                    source_ip = vm1_fixture.vm_ip,
                                    dest_ip = vm2_fixture.vm_ip,
                                    dest_port = '0',
                                    proto = '1')
        if fwd_flow:
            sport = fwd_flow.source_port
            fwd_flow_gw_index = fwd_flow.items.get('underlay_gw_index', '-1')
            flow_rec1 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm1_fixture.vm_ip,
                dip=vm2_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec1 = None
        if flow_rec1 is not None:
            self.logger.info('Verifying underlay_gw_index in fwd flow record')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'underlay_gw_index', fwd_flow_gw_index)
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to %s in given flow. Flow details %s' %
                    (fwd_flow_gw_index, flow_rec1))
                result = result and False
            self.logger.info('Verifying flow is not local flow in fwd flow record')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'local_flow', 'no')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if rev_flow:
            sport = rev_flow.source_port
            rev_flow_gw_index = rev_flow.items.get('underlay_gw_index', '-1')
            flow_rec2 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm2_fixture.vm_ip,
                dip=vm1_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec2 = None
        if flow_rec2 is not None:
            self.logger.info('Verifying underlay_gw_index in reverse flow record')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'underlay_gw_index', rev_flow_gw_index)
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to %s in given reverse flow. Flow details %s' %
                    (rev_flow_gw_index, flow_rec2))
                result = result and False
            self.logger.info('Verifying local flow flag is not set in reverse flow record')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'local_flow', 'no')
            if match is False:
                self.logger.error(
                    'Test Failed. Rev Flow entry is not loal flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required rev flow not found')
            result = result and False

        if fwd_flow_gw_index and rev_flow_gw_index and (fwd_flow_gw_index != rev_flow_gw_index) and fwd_flow_gw_index != '-1':
            self.logger.error(
                "Test failed. Fwd flow gw index %s Rev flow gw index %s do not match" % (fwd_flow_gw_index, rev_flow_gw_index))
            result = result and False

        return result
    # end test_flow_stickiness_workload_in_same_vn_different_compute

    @preposttest_wrapper
    def test_flow_stickiness_workload_in_different_vn_same_compute(self):
        '''
           Launch vm1 in vn1 , vm2 in vn2 .
           verify ping from vm1 to vm2.
           verify same underlay gw index (-1 or 255) in fw and rev flow for ping.
           verify local flow flag is set in fwd and rev flow entry
        '''
        result = True
        vn1_fixture = self.create_vn()
        vn2_fixture = self.create_vn()
        policy_name = get_random_name('policy1')
        rules = [
            {
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'icmp',
                'source_network': vn1_fixture.vn_name,
                'dest_network': vn2_fixture.vn_name,
            },
        ]

        policy_fixture = self.setup_policy_between_vns(vn1_fixture,
            vn2_fixture, rules)
        assert vn1_fixture.verify_on_setup()
        assert vn2_fixture.verify_on_setup()

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm1_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm1-vn1'),
                              image_name='cirros',
                              node_name=vm1_node_name)
        vm2_fixture = self.create_vm(vn2_fixture,
                              get_random_name('vm1-vn2'),
                              image_name='cirros',
                              node_name=vm2_node_name)
        vm1_fixture.wait_till_vm_is_up()
        vm2_fixture.wait_till_vm_is_up()

        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
            'Ping failed between VMs')
        # underlay gw index checks

        inspect_h1 = self.agent_inspect[vm1_fixture.vm_node_ip]
        flow_rec1 = None

        vn_fq_name=vm1_fixture.vn_fq_name
        compute_node_fixture = self.useFixture(ComputeNodeFixture(
                self.connections, vm1_fixture.vm_node_ip))
        fwd_flow, rev_flow = compute_node_fixture.get_flow_entry(
                                    source_ip = vm1_fixture.vm_ip,
                                    dest_ip = vm2_fixture.vm_ip,
                                    dest_port = '0',
                                    proto = '1')
        if fwd_flow:
            sport = fwd_flow.source_port
            fwd_flow_gw_index = fwd_flow.items.get('underlay_gw_index', '255')
            flow_rec1 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm1_fixture.vm_ip,
                dip=vm2_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec1 = None
        if flow_rec1 is not None:
            self.logger.info('Verifying underlay_gw_index in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'underlay_gw_index', '255')
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to -1 in given flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
            self.logger.info('Verifying local flow in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'local_flow', 'yes')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if rev_flow:
            sport = rev_flow.source_port
            vn2_fq_name=vm2_fixture.vn_fq_name
            rev_flow_gw_index = rev_flow.items.get('underlay_gw_index', '255')
            flow_rec2 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm2_fixture.tap_intf[vn2_fq_name]['flow_key_idx'],
                sip=vm2_fixture.vm_ip,
                dip=vm1_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec2 = None
        if flow_rec2 is not None:
            self.logger.info('Verifying underlay_gw_index in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'underlay_gw_index', '255')
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to -1 in given flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
            self.logger.info('Verifying local flow in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'local_flow', 'yes')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if rev_flow_gw_index != '-1' or fwd_flow_gw_index != '-1':
            self.logger.error(
                "Test Failed. For local flow  underlay gw index is incorrect rev_flow_gw_index %s fwd_flow_gw_index %s "%
                (rev_flow_gw_index, fwd_flow_gw_index))
            result = result and False
        return result
    # end test_flow_stickiness_workload_in_different_vn_same_compute

    @preposttest_wrapper
    def test_flow_stickiness_workload_in_different_vn_different_compute(self):
        '''
           Launch vm1 in vn1 and vm2 in vn2, on different computes.
           Add policy vn1<=>vn2 ,verify ping vm1 to vm2.
           Verify underlay gw index is same in fwd and rev flow in agent and vrouter.
           verify both fwd and rev flows are not local flows.
        '''

        result = True
        if len(self.inputs.compute_ips) < 2:
            return (False, 'Skipping Test. Need atleast two compute nodes')
        vn1_fixture = self.create_vn()
        vn2_fixture = self.create_vn()
        policy_name = get_random_name('policy1')
        rules = [
            {
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'icmp',
                'source_network': vn1_fixture.vn_name,
                'dest_network': vn2_fixture.vn_name,
            },
        ]

        policy_fixture = self.setup_policy_between_vns(vn1_fixture,
            vn2_fixture, rules)
        assert vn1_fixture.verify_on_setup()
        assert vn2_fixture.verify_on_setup()

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vm1_fixture = self.create_vm(vn1_fixture,
                              get_random_name('vm1-vn1'),
                              image_name='cirros',
                              node_name=vm1_node_name)
        vm2_fixture = self.create_vm(vn2_fixture,
                              get_random_name('vm1-vn2'),
                              image_name='cirros',
                              node_name=vm2_node_name)
        vm1_fixture.wait_till_vm_is_up()
        vm2_fixture.wait_till_vm_is_up()

        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
            'Ping failed between VMs')
        # underlay gw index checks

        inspect_h1 = self.agent_inspect[vm1_fixture.vm_node_ip]
        flow_rec1 = None

        vn_fq_name=vm1_fixture.vn_fq_name
        compute_node_fixture = self.useFixture(ComputeNodeFixture(
                self.connections, vm1_fixture.vm_node_ip))
        fwd_flow, rev_flow = compute_node_fixture.get_flow_entry(
                                    source_ip = vm1_fixture.vm_ip,
                                    dest_ip = vm2_fixture.vm_ip,
                                    dest_port = '0',
                                    proto = '1')
        if fwd_flow:
            sport = fwd_flow.source_port
            fwd_flow_gw_index = fwd_flow.items.get('underlay_gw_index', '-1')
            flow_rec1 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm1_fixture.vm_ip,
                dip=vm2_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec1 = None
        if flow_rec1 is not None:
            self.logger.info('Verifying underlay_gw_index in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'underlay_gw_index', fwd_flow_gw_index)
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to %s in given flow. Flow details %s' %
                    (gw_index, flow_rec1))
                result = result and False
            self.logger.info('Verifying local flow in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec1, 'local_flow', 'no')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec1))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if rev_flow:
            sport = rev_flow.source_port
            rev_flow_gw_index = rev_flow.items.get('underlay_gw_index', '-1')
            vn2_fq_name=vm2_fixture.vn_fq_name
            flow_rec2 = inspect_h1.get_vna_fetchflowrecord(
                nh=vm1_fixture.tap_intf[vn_fq_name]['flow_key_idx'],
                sip=vm2_fixture.vm_ip,
                dip=vm1_fixture.vm_ip,
                sport=sport,
                dport='0',
                protocol='1')
        else:
            flow_rec2 = None
        if flow_rec2 is not None:
            self.logger.info('Verifying underlay_gw_index in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'underlay_gw_index', rev_flow_gw_index)
            if match is False:
                self.logger.error(
                    'Test Failed. underlay_gw_index is not set to %s in given flow. Flow details %s' %
                    (gw_index, flow_rec2))
                result = result and False
            self.logger.info('Verifying local flow in flow records')
            match = inspect_h1.match_item_in_flowrecord(
                flow_rec2, 'local_flow', 'no')
            if match is False:
                self.logger.error(
                    'Test Failed. Flow entry is not loal flow. Flow details %s' %
                    (flow_rec2))
                result = result and False
        else:
            self.logger.error(
                'Test Failed. Required flow not found')
            result = result and False

        if (fwd_flow_gw_index != rev_flow_gw_index) or fwd_flow_gw_index == '-1':
            self.logger.error(
                "Test failed. Fwd flow gw index %s Rev flow gw index %s do not match" % (fwd_flow_gw_index, rev_flow_gw_index))
            result = result and False

        return result
    # end test_flow_stickiness_workload_in_different_vn_different_compute

    @preposttest_wrapper
    def test_traffic_intra_vn_intra_compute(self):
        '''
        Description: L2 an L3 Traffic test between intra vn, intra compute VMs.
        Test Steps:
            1. Launch vm1 and vm2 in vn1 on same compute.
            2. Send l2 traffic using scapy from vm1 to vm2.
            3. Ping from vm1 to vm2.
            4. Send tcp traffic using scapy from vm1 to vm2.
        Pass Criteria:
            1. Verify no drop for l2 traffic.
            2. Verify ping is successful.
            3. Verify no drops for tcp traffic on vm2.
        '''
        vn1_name = get_random_name('vn1')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name,orch=self.orchestrator)
        vn1_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm2_name, node_name=node1)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()

        #ping test from vm1 to vm2
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)

        #send l2 traffic and verify
        mac1 = vm1_fixture.mac_addr[vn1_fixture.vn_fq_name]
        mac2 = vm2_fixture.mac_addr[vn1_fixture.vn_fq_name]
        filters = 'ether src %s and ether dst %s' %(mac1, mac2)
        vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf(
                                None, [vm2_fixture], None, filters=filters, pcap_on_vm=True)
        sleep(5)
        self.send_l2_traffic(vm1_fixture, mac1, mac2, "eth0")
        sleep(2)
        result_traffic_count = verify_tcpdump_count(self, None, 'eth0', vm_fix_pcap_pid_files=vm_fix_pcap_pid_files, exp_count=10, exact_match=False)
        assert result_traffic_count 
        #send l3 traffic and verify
        self.logger.info("Verify Traffic Ip Traffic ")
        send_vm_fixture = vm1_fixture
        recv_vm_fixture = vm2_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
        assert traffic_udp

    # end test_traffic_intra_vn_intra_compute

    @preposttest_wrapper
    def test_traffic_intra_vn_inter_compute(self):
        '''
        Description: L2 an L3 Traffic test between intra vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 and vm2 in vn1 on different computes.
            2. Send l2 traffic using scapy from vm1 to vm2.
            3. Ping from vm1 to vm2.
            4. Send tcp traffic using scapy from vm1 to vm2.
        Pass Criteria:
            1. Verify no drop for l2 traffic.
            2. Verify ping is successful.
            3. Verify no drops for tcp traffic on vm2.
        '''
        vn1_name = get_random_name('vn1')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name,orch=self.orchestrator)
        vn1_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm2_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()

        #ping test from vm1 to vm2
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)

        #send l2 traffic and verify
        mac1 = vm1_fixture.mac_addr[vn1_fixture.vn_fq_name]
        mac2 = vm2_fixture.mac_addr[vn1_fixture.vn_fq_name]
        filters = 'ether src %s and ether dst %s' %(mac1, mac2)
        vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf(
                                None, [vm2_fixture], None, filters=filters, pcap_on_vm=True)
        sleep(5)
        self.send_l2_traffic(vm1_fixture, mac1, mac2, "eth0")
        sleep(2)
        result_traffic_count = verify_tcpdump_count(self, None, 'eth0', vm_fix_pcap_pid_files=vm_fix_pcap_pid_files, exp_count=10, exact_match=False)
        assert result_traffic_count
        #send l3 traffic and verify
        self.logger.info("Verify Traffic Ip Traffic ")
        send_vm_fixture = vm1_fixture
        recv_vm_fixture = vm2_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
        assert traffic_udp
    # end test_traffic_intra_vn_inter_compute

    @preposttest_wrapper
    def test_traffic_inter_vn_inter_compute(self):
        '''
        Description: L3 Traffic test between inter vn, inter and intra compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2.
            4. Send tcp traffic using scapy from vm1 to vm2.
            5. Launch vm22 in vn2 on compute node1 same as vm1 compute.
            6. Send tcp traffic using scapy from vm1 to vm22.
        Pass Criteria:
            1. Verify ping is successful.
            2. Verify no drops for tcp traffic on vm2.
            3. Verify no drops for tcp traffic on vm22.
        '''
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name,orch=self.orchestrator)
        vn2_fixture = self.create_vn(vn_name=vn2_name,orch=self.orchestrator)
        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                vn2_fixture)
        vn1_fixture.read()
        vn2_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu-traffic', vm_name=vm2_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()

        # ping test from vm1 to vm2
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)

        #send l3 traffic and verify, inter vn inter
        self.logger.info("Verify Traffic Ip Traffic ")
        send_vm_fixture = vm1_fixture
        recv_vm_fixture = vm2_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
        assert traffic_udp
        # Launch vm22 on node1 same as vm1 compute
        vm22_name = get_random_name('vm22')
        vm22_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu-traffic', vm_name=vm22_name, node_name=node1)

        assert vm22_fixture.wait_till_vm_is_up()

        #send l3 traffic and verify
        self.logger.info("Verify Traffic Ip Traffic ")
        recv_vm_fixture = vm22_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
        assert traffic_udp
    # end test_traffic_inter_vn_inter_compute

    @preposttest_wrapper
    def test_traffic_ipv6_intra_and_inter_vn(self):
        '''
        Description: L2 an L3 ipv6 Traffic test between intra vn VMs and L3 ipv6 traffic test between inter vn VMs.
        Test Steps:
            1. Launch vm1, vm2 in ipv6 vn1 and vm3 in ipv6 vn2 on same compute.
            2. Set policy to allow all inter vn traffic.
            3. Send l2 traffic using scapy from vm1 to vm2.
            4. Ping from vm1 to vm2.
            5. Ping from vm1 to vm3.
        Pass Criteria:
            1. Verify no drops for l2 traffic on vm2.
            2. Verify ping is successful from vm1 to vm2.
            3. Verify ping is successful from vm1 to vm3.
        '''
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')
        vm3_name = get_random_name('vm3')
        vn1_v6_subnet = get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])
        vn2_v6_subnet = get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name'] 
        vn1_fixture = self.create_vn(vn_name=vn1_name, orch=self.orchestrator)
        vn2_fixture = self.create_vn(vn_name=vn2_name, orch=self.orchestrator)
        vn1_fixture.create_subnet({'cidr': vn1_v6_subnet})
        vn2_fixture.create_subnet({'cidr': vn2_v6_subnet})
        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                vn2_fixture)
        vn1_fixture.read()
        vn2_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm2_name, node_name=node1)
        vm3_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu-traffic', vm_name=vm3_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        assert vm3_fixture.wait_till_vm_is_up()

        #send l2 traffic and verify
        mac1 = vm1_fixture.mac_addr[vn1_fixture.vn_fq_name]
        mac2 = vm2_fixture.mac_addr[vn1_fixture.vn_fq_name]
        filters = 'ether src %s and ether dst %s' %(mac1, mac2)
        vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf( 
                                None, [vm2_fixture], None, filters=filters, pcap_on_vm=True)
        sleep(5)
        self.send_l2_traffic(vm1_fixture, mac1, mac2, "eth0")
        sleep(2)
        result_traffic_count = verify_tcpdump_count(self, None, 'eth0', vm_fix_pcap_pid_files=vm_fix_pcap_pid_files, exp_count=10, exact_match=False)
        assert result_traffic_count
        #send l3 traffic and verify
        self.logger.info("Verify Traffic Ip Traffic ")
        send_vm_fixture = vm1_fixture
        recv_vm_fixture = vm2_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
        assert traffic_udp

        #send l3 traffic and verify inter vn inter compute
        self.logger.info("Verify Traffic Ip Traffic ")
        send_vm_fixture = vm1_fixture
        recv_vm_fixture = vm3_fixture
        traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
        assert traffic_tcp
        traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=1111, dport=8004)
        assert traffic_udp
        # ping6 test from vm1 to vm2
        vm2_ip6 = self.get_ipv6_address("eth0", vm2_fixture)
        assert vm1_fixture.ping_to_ipv6(vm2_ip6)

        # ping6 test from vm1 to vm3
        vm3_ip6 = self.get_ipv6_address("eth0", vm3_fixture)
        assert vm1_fixture.ping_to_ipv6(vm3_ip6)
    # end test_traffic_ipv6_intra_and_inter_vn

    @preposttest_wrapper
    def test_traffic_intra_and_inter_vn_pkt_mode(self):
        '''
        Description: Packet Mode - L2 traffic test between intra vn VMs, L3 traffic test between inter vn VMs
        Test Steps:
            1. Launch vm1 in vn1 on compute 1.
            2. Launch vm2 in vn1 and vm3 in vn2 on compute 2.
            3. Disable flow mode policy on all VMs.
            4. Set policy to allow all inter vn traffic.
            5. Send l2 traffic using scapy from vm1 to vm2.
            6. Ping from vm1 to vm3.
        Pass Criteria:
            1. Verify no drops for l2 traffic on vm2.
            2. Verify ping is successful from vm1 to vm3.
            3. Verify load balancing of packets for L2 traffic on physical interfaces on compute 1.
            4. Verify load balancing of packets for L3 traffic on physical interfaces on compute 1.
        '''
        result = True
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')
        vm3_name = get_random_name('vm3')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name, orch=self.orchestrator)
        vn2_fixture = self.create_vn(vn_name=vn2_name, orch=self.orchestrator)
        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                vn2_fixture)
        vn1_fixture.read()
        vn2_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm2_name, node_name=node2)
        vm3_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu-traffic', vm_name=vm3_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        assert vm3_fixture.wait_till_vm_is_up()

        # Disable policies on VMs:
        vm1_fixture.disable_interface_policy()
        vm2_fixture.disable_interface_policy()
        vm3_fixture.disable_interface_policy()

        #send l2 traffic and verify intra vn l2 traffic
        mac1 = vm1_fixture.mac_addr[vn1_fixture.vn_fq_name]
        mac2 = vm2_fixture.mac_addr[vn1_fixture.vn_fq_name]
        filters = 'ether src %s and ether dst %s' %(mac1, mac2)
        vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf(
                                None, [vm2_fixture], None, filters=filters, pcap_on_vm=True)
        sleep(5)
        self.send_l2_traffic(vm1_fixture, mac1, mac2, "eth0")
        sleep(2)
        result_traffic_count = verify_tcpdump_count(self, None, 'eth0', vm_fix_pcap_pid_files=vm_fix_pcap_pid_files, exp_count=10, exact_match=False)
        assert result_traffic_count

        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):

            #send l3 traffic and verify intra and inter vn
            self.logger.info("Verify Traffic Ip Traffic ")
            send_vm_fixture = vm1_fixture
            recv_vm_fixture = vm2_fixture
            traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
            assert traffic_tcp
            traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
            assert traffic_udp
            recv_vm_fixture = vm3_fixture
            traffic_tcp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='tcp', sport=0, dport=20000)
            assert traffic_tcp
            traffic_udp = self.verify_traffic(send_vm_fixture, recv_vm_fixture,
                                        proto='udp', sport=10000, dport=20000)
            assert traffic_udp

            return True
    
        inspect_h1 = self.agent_inspect[vm1_fixture.vm_node_ip]
        physical_intf_list = inspect_h1.get_vna_interface_by_type('eth')
        vm1_host_ip = self.inputs.host_data[vm1_fixture.vm_node_ip]['host_ip']

        #send intra vn tcp traffic and verify
        tap_intf = vm2_fixture.tap_intf[vn1_fixture.vn_fq_name]['name']
        server_ip = self.inputs.host_data[vm2_fixture.vm_node_ip]['host_ip']
        pcap = {}
        session = {}
        for iface in physical_intf_list:
            pcap[iface],session[iface] = self.start_tcpdump(vm1_host_ip, vm1_fixture.vm_ip, iface, filters="udp")
        (pcap2, session2) = self.start_tcpdump(server_ip, vm1_fixture.vm_ip, tap_intf)
        sleep(10)
        self.send_tcp_traffic(vm1_fixture, str(vm1_fixture.vm_ip), str(vm2_fixture.vm_ip), 1, dport_range=(10001,10010))
        sleep(60)
        count = 0
        src_ip_octests = []
        src_ip_hex = ''
        src_ip_octests = vm1_fixture.vm_ip.split('.')
        for octet in src_ip_octests:
            if octet == src_ip_octests[2]:
                src_ip_hex = src_ip_hex + ' '
            octet = int(octet)
            octet = hex(octet)
            octet = octet.split("0x",1)[1]
            if len(octet) <= 1:
               octet = '0' + octet
            src_ip_hex = src_ip_hex + octet
        if src_ip_hex == '':
            self.logger.error("Error in calculating src ip in hex ")
            result = result and False 
        for iface in physical_intf_list:
            stop_tcpdump_for_intf(session[iface], pcap[iface])
            cmd = "sudo tcpdump -AXnnr %s | grep '%s' | wc -l" % (pcap[iface], src_ip_hex)
            out, err = execute_cmd_out(session[iface], cmd, self.logger)
            count += int(out.strip('\n'))
            if (count == 0):
                self.logger.error("Traffic not getting loadbalanced on interface %s" % iface)
                result = result and False
        stop_tcpdump_for_intf(session2, pcap2)
        assert (count == 10)
        assert verify_tcpdump_count(self, session2, pcap2, exp_count=10)

        # send inter vn tcp traffic and verify
        tap_intf2 = vm3_fixture.tap_intf[vn2_fixture.vn_fq_name]['name']
        server_ip2 = self.inputs.host_data[vm3_fixture.vm_node_ip]['host_ip']
        pcap1 = {}
        session1 = {}
        for iface in physical_intf_list:
            pcap1[iface],session1[iface] = self.start_tcpdump(vm1_host_ip, vm1_fixture.vm_ip, iface, filters="udp")
        (pcap3, session3) = self.start_tcpdump(server_ip2, vm1_fixture.vm_ip, tap_intf2)
        sleep(10)
        self.send_tcp_traffic(vm1_fixture, str(vm1_fixture.vm_ip), str(vm3_fixture.vm_ip), 1,dport_range=(10001,10010))
        sleep(60)
        count2 = 0
        for iface in physical_intf_list:
            stop_tcpdump_for_intf(session1[iface], pcap1[iface])
            cmd = "sudo tcpdump -AXnnr %s | grep '%s' | wc -l" % (pcap[iface], src_ip_hex)
            out, err = execute_cmd_out(session1[iface], cmd, self.logger)
            count2 += int(out.strip('\n'))
            if (count2 == 0):
                self.logger.error("Traffic not getting loadbalanced on interface %s" % iface)
                result = result and False
        stop_tcpdump_for_intf(session3, pcap3)
        assert (count2 == 20)
        assert verify_tcpdump_count(self, session3, pcap3, exp_count=10)
        return result
    # end test_traffic_intra_and_inter_vn_pkt_mode
