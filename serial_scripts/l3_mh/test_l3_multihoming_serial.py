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
from compute_node_test import ComputeNodeFixture
from common.device_connection import NetconfConnection

class TestSerialL3Multihoming(BaseL3Multihoming):
    @classmethod
    def setUpClass(cls):
        super(TestSerialL3Multihoming, cls).setUpClass()
        cls.l3mh_setup_check_done = False

    @classmethod
    def tearDownClass(cls):
        super(TestSerialL3Multihoming, cls).tearDownClass()

    def setUp(self):
        super(TestSerialL3Multihoming, self).setUp()
        if TestSerialL3Multihoming.l3mh_setup_check_done:
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
        TestSerialL3Multihoming.l3mh_setup_check_done = True

    @preposttest_wrapper
    def test_contrail_status_on_compute_with_agent_restart(self):
        '''
           Verify all contrail services become Active on compute,
           after agent restart, with l3 multihoming is enabled on computes.
        '''
        # Verify cluster status before agnet restart
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
        # Restart agent on all computes
        self.inputs.restart_service('contrail-vrouter-agent', self.inputs.compute_ips,
                                         container='agent')
        time.sleep(180)
        # Verify cluster status after agent container restart
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
    # end test_contrail_status_on_compute_with_agent_restart

    @preposttest_wrapper
    def test_inter_vn_traffic_with_logical_router(self):
        '''
           Dmac rewrite test
           ping from vm1 in vn1 to vn2 in vm2 on different computes
        '''
        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):
            self.logger.info("TEST SKIPPED DUE TO DPDK CRASH")
            return (False, "Skipping Test. ")
        self.addCleanup(self.set_encap_priority, encaps=self.get_encap_priority())
        self.set_encap_priority(['VXLAN', 'MPLSoGRE', 'MPLSoUDP'])
        self.addCleanup(self.vnc_h.disable_vxlan_routing())
        self.vnc_h.enable_vxlan_routing()
        self.allow_default_sg_to_allow_all_on_project(self.inputs.project_name)
        vn1 = self.create_vn()
        vn2 = self.create_vn()

        lr1 = self.create_logical_router([vn1, vn2], vni=70001)

        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vm2_node_name = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        #Launch VM on different compute nodes
        vm11 = self.create_vm(vn1,
                              get_random_name('vm1-vn1'),
                              image_name='ubuntu-traffic',
                              node_name=vm1_node_name)
        vm21 = self.create_vm(vn2,
                              get_random_name('vm1-vn2'),
                              image_name='ubuntu-traffic',
                              node_name=vm2_node_name)
        self.check_vms_booted([vm11, vm21])

        self.logger.info(
            "Verify Traffic between VN-1 and VN-2 on Logical Router: lr1")
        self.verify_traffic(vm11, vm21, 'udp', sport=10000, dport=20000)
        assert vm11.ping_with_certainty(vm21.vm_ip), (
            'Ping failed between VMs')

    @preposttest_wrapper
    def test_flow_stickiness_with_interface_flap_workload_in_different_vn_and_compute(self):
        '''
           Launch vm1 in vn1 and vm2 in vn2, on different computes.
           Add policy vn1<=>vn2 ,verify ping vm1 to vm2.
           Verify underlay gw index is same in fwd and rev flow in agent and vrouter.
           verify both fwd and rev flows are not local flows
           shutdown physical interface on compute0, verify ping, now it takes 2nd interface.
        '''
        result = True
        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):
            self.logger.info("Skipping Test. Physical interface flap not feasible for dpdk")
            return (False, "Skipping Test. ")
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
                    (fwd_flow_gw_index, flow_rec1))
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
                    (rev_flow_gw_index, flow_rec2))
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

        if fwd_flow:
            physical_intf_name = ''
            if fwd_flow_gw_index != -1:
                vif_dict = {}
                vif_dict = inspect_h1.get_vrouter_virtual_interface(fwd_flow_gw_index)
            physical_intf_name = vif_dict.get('name', None)
            physical_interface_addr_list = compute_node_fixture.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface_addr').split(' ')
            physical_interface_list = compute_node_fixture.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface').split(' ')
            conf_file_index = 0
            physical_intf_ip = ''
            for intf in physical_interface_list:
                if intf == physical_intf_name:
                    physical_intf_ip = physical_interface_addr_list[conf_file_index].split('/')[0]
                    break
                conf_file_index = conf_file_index +1
            loopback_ip = compute_node_fixture.get_option_value('VIRTUAL-HOST-INTERFACE', 'loopback_ip')
            device_creds = None
            if physical_intf_ip:
                device_creds= self.get_qfx_device_creds_from_port_ip(physical_intf_ip)
            if physical_intf_name and device_creds and loopback_ip and physical_intf_ip:
               self.logger.info("Shutdown %s interface on compute0 and del static rt on compute for lo:0" % physical_intf_name)
               loopback_ip_prefix = loopback_ip.split('/')[0] + '/32'
               add_cmd_on_qfx = "set routing-options static route %s next-hop %s " % (loopback_ip_prefix, physical_intf_ip)
               qfx_cmd = []
               qfx_cmd.append(add_cmd_on_qfx)
               device_handle = NetconfConnection(host = device_creds['mgmt_ip'], username=device_creds['ssh_username'],
                   password=device_creds['ssh_password'])
               device_handle.connect()
               self.addCleanup(device_handle.disconnect)
               self.addCleanup(device_handle.config, stmts = qfx_cmd, timeout = 120)
               qfx_del_cmd = "delete routing-options static route %s next-hop %s " % (loopback_ip_prefix, physical_intf_ip)
               cmd = "ip link set dev %s up" %(physical_intf_name)
               self.addCleanup(compute_node_fixture.execute_cmd, cmd, container=None)
               cmd_itf_down = "ip link set dev %s down" %(physical_intf_name)
               compute_node_fixture.execute_cmd(cmd_itf_down, container=None)
               cli_output = device_handle.config(stmts = [qfx_del_cmd], timeout = 120)
               time.sleep(5)
               assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip), (
               'Ping failed between VMs in vn1 on physical interface flap for %s' %physical_intf_name)
            else:
               self.logger.error(" No physical_intf  or qfx device ip found for fwd_flow_gw_index %s" % (fwd_flow_gw_index))
               result = result and False
        else:
            self.logger.error(" No fwd_flow found while trying interface flap")
            result = result and False
        return result
    # end test_flow_stickiness_with_interface_flap_workload_in_different_vn_and_compute

    @preposttest_wrapper
    def test_traffic_with_agent_restart(self):
        '''
        Description: L2 an L3 Traffic test between inter vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2, inter vn inter compute traffic test
            4. Launch vm31 and vm32 in vn3 on same compute, ping vm31 to vm32, intra vn intra compute.
            5. Launch vm12 in vn1 on node2, ping vm1 to vm12, inra vn inter compute traffic.
            6. Ping vm2 to vm12, inter vn intra compute traffic.
        Pass Criteria:
            1. Verify ping is successful.
            2. Restart agent on node2, repeat all traffic test verify no drops
        '''
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')
        vm12_name = get_random_name('vm12')

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
        vm12_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu-traffic', vm_name=vm12_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        assert vm12_fixture.wait_till_vm_is_up()

        vn3_fixture = self.create_vn()
        vn3_fixture.read()
        vm31_name = get_random_name('vm31')
        vm32_name = get_random_name('vm32')
        vm31_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu-traffic', vm_name=vm31_name, node_name=node2)
        vm32_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu-traffic', vm_name=vm32_name, node_name=node2)

        assert vm31_fixture.wait_till_vm_is_up()
        assert vm32_fixture.wait_till_vm_is_up()
        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)

        # Restart agent on node2
        self.inputs.run_cmd_on_server(
            vm2_fixture.vm_node_ip, "docker restart vrouter_vrouter-agent_1")
        time.sleep(120)

        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)
    # end test_traffic_with_agent_restart

    @preposttest_wrapper
    def test_traffic_with_compute_restart(self):
        '''
        Description: L2 an L3 Traffic test between inter vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2, inter vn inter compute traffic test
            4. Launch vm31 and vm32 in vn3 on same compute, ping vm31 to vm32, intra vn intra compute.
            5. Launch vm12 in vn1 on node2, ping vm1 to vm12, inra vn inter compute traffic.
            6. Ping vm2 to vm12, inter vn intra compute traffic.
        Pass Criteria:
            1. Verify ping is successful.
            2. Reboot node2, repeat all traffic test verify no drops
        '''
        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):
            self.logger.info("Skipping Test. Run After provisioning changes")
            return (False, "Skipping Test. ")
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')
        vm12_name = get_random_name('vm12')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name,orch=self.orchestrator)
        vn2_fixture = self.create_vn(vn_name=vn2_name,orch=self.orchestrator)
        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                vn2_fixture)
        vn1_fixture.read()
        vn2_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu', vm_name=vm2_name, node_name=node2)
        vm12_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu', vm_name=vm12_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        assert vm12_fixture.wait_till_vm_is_up()

        vn3_fixture = self.create_vn()
        vn3_fixture.read()
        vm31_name = get_random_name('vm31')
        vm32_name = get_random_name('vm32')
        vm31_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu', vm_name=vm31_name, node_name=node2)
        vm32_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu', vm_name=vm32_name, node_name=node2)

        assert vm31_fixture.wait_till_vm_is_up()
        assert vm32_fixture.wait_till_vm_is_up()

        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)

        # Reboot the node
        self.inputs.run_cmd_on_server(vm2_fixture.vm_node_ip, 'reboot')
        time.sleep(300)

        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)
    # end test_traffic_with_compute_restart

    @preposttest_wrapper
    def test_traffic_with_physical_interface_flap(self):
        '''
        Description: L2 an L3 Traffic test between inter vn, inter compute VMs.
        Test Steps:
            1. Launch vm1 in vn1 and vm2 in vn2 on different computes.
            2. Set policy to allow all inter vn traffic.
            3. Ping from vm1 to vm2, inter vn inter compute traffic test
            4. Launch vm31 and vm32 in vn3 on same compute, ping vm31 to vm32, intra vn intra compute.
            5. Launch vm12 in vn1 on node2, ping vm1 to vm12, inra vn inter compute traffic.
            6. Ping vm2 to vm12, inter vn intra compute traffic.
        Pass Criteria:
            1. Verify ping is successful.
            2. Do ifconfig down and up for physical interfaces on  node2, repeat all traffic test verify no drops
        '''
        if (self.is_dpdk_compute(self.inputs.compute_ips[0]) or self.is_dpdk_compute(self.inputs.compute_ips[1])):
            self.logger.info("Skipping Test. No physical interface flap on dpdk compute")
            return (False, "Skipping Test. ")
        vn1_name = get_random_name('vn1')
        vn2_name = get_random_name('vn2')
        vm1_name = get_random_name('vm1')
        vm2_name = get_random_name('vm2')
        vm12_name = get_random_name('vm12')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        vn1_fixture = self.create_vn(vn_name=vn1_name,orch=self.orchestrator)
        vn2_fixture = self.create_vn(vn_name=vn2_name,orch=self.orchestrator)
        policy_fixture = self.setup_only_policy_between_vns(vn1_fixture,
                vn2_fixture)
        vn1_fixture.read()
        vn2_fixture.read()
        vm1_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu', vm_name=vm1_name, node_name=node1)
        vm2_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu', vm_name=vm2_name, node_name=node2)
        vm12_fixture = self.create_vm(vn_fixture=vn1_fixture,
            image_name='ubuntu', vm_name=vm12_name, node_name=node2)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        assert vm12_fixture.wait_till_vm_is_up()

        vn3_fixture = self.create_vn()
        vn3_fixture.read()
        vm31_name = get_random_name('vm31')
        vm32_name = get_random_name('vm32')
        vm31_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu', vm_name=vm31_name, node_name=node2)
        vm32_fixture = self.create_vm(vn_fixture=vn3_fixture,
            image_name='ubuntu', vm_name=vm32_name, node_name=node2)

        assert vm31_fixture.wait_till_vm_is_up()
        assert vm32_fixture.wait_till_vm_is_up()

        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)
        # Restart physical interfaces
        inspect_h = self.agent_inspect[vm2_fixture.vm_node_ip]
        physical_intf_list = inspect_h.get_vna_interface_by_type('eth')
        for name in physical_intf_list:
            cmd = 'ifdown %s; sleep 5' % (name)
            self.inputs.run_cmd_on_server(
                vm2_fixture.vm_node_ip, cmd)
        for name in physical_intf_list:
            cmd = 'ifup %s; sleep 5' % (name)
            self.inputs.run_cmd_on_server(
                vm2_fixture.vm_node_ip, cmd)
        time.sleep(5)
        # ping test from vm1 to vm2, inter vn inter compute
        assert vm1_fixture.ping_with_certainty(vm2_fixture.vm_ip)
        # ping vm1 to vm12, intra vn inter compute trffic
        assert vm1_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm2 to vm12, inter vn intra compute
        assert vm2_fixture.ping_with_certainty(vm12_fixture.vm_ip)
        # ping vm31 to vm32, intra vn intra compute traffic
        assert vm31_fixture.ping_with_certainty(vm32_fixture.vm_ip)
    # end test_traffic_with_physical_interface_flap
