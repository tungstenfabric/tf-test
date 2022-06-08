from common.max_flows.base import BaseMaxFlowsTest
import time
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because
from compute_node_test import ComputeNodeFixture

class TestMaxFlows(BaseMaxFlowsTest):

    DEFAULT_FLOW_TIMEOUT = 120

    @classmethod
    def setUpClass(cls):
        super(TestMaxFlows, cls).setUpClass(flow_timeout=cls.DEFAULT_FLOW_TIMEOUT)

    @classmethod
    def tearDownClass(cls):
        super(TestMaxFlows, cls).tearDownClass()

    def waiting_for_flow_timeout(self):
        self.logger.info("Sleeping for flow timeout (%d seconds)..." % (self.DEFAULT_FLOW_TIMEOUT))
        time.sleep(self.DEFAULT_FLOW_TIMEOUT)
        self.logger.info("Sleeping for flow timeout (%d seconds)...Completed" % (self.DEFAULT_FLOW_TIMEOUT))

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_max_flows_vn_level(self):
        '''
        Description:
                Verify max_flows functionality at VN level
        Test steps:
               1.Create a vn1 and vn2
               2.configure max_flows as 1000 @ vn1
               3.Launch  vm11, vm12 and vm13 on vn1 network
               4.Launch vm21 and vm22 on vn2 network
               5.Verify traffic between the VMs
               6.send 2000 flows traffic from vm11 to vm12 , it should allow only 1000 flows
               7.send 2000 flows traffic from vm11 to vm13, it should all only 1000 flows
               8.Modify the max_flows value as 1500, verify traffic between vm11 and vm12
               9.send 2000 flows traffic from vm21 to vm22, it should allow all the traffic
               10.Delete the max_flows @ vn1 ( by setting the value as 0 )
               11.send 2000 flows traffic from vm11 to vm12 , it should allow all the traffic
        Pass criteria:
               Number of flows should be created as per max_flows configured at VN level.
               Other VNs should not be imapacted
               After deleting max_flows configuration, it should allow all the flows.
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])
        vn2_fix = self.create_vn('vn2', ['22.0.0.0/24'])

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm21_fix = self.create_vm(vm_name='vm21',
                                  vn_fixture=vn2_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm22_fix = self.create_vm(vm_name='vm22',
                                  vn_fixture=vn2_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])

        # Setting MAX Flows only on VN-1
        vn1_max_flows = 1000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm21_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm22_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm12_fix),
                                     (vm11_fix, vm13_fix),
                                     (vm21_fix, vm22_fix)])

        self.waiting_for_flow_timeout()

        flows_to_create = vn1_max_flows * 2
        # Verify Max_flows functionality on VN level
        # Source and Destination VMs on different Compute
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm12_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VN level Max Flows Provisioning is working "\
                             "for VMs on different computes")
        assert total_flow_count == vn1_max_flows, \
                "VN level Max Flows Provisioning is not working for VMs on "\
                "different compute"

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VN level
        # Source and Destination VMs on same Compute
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VN level Max Flows Provisioning is working "\
                             "for VMs on same compute")
        assert total_flow_count == vn1_max_flows, \
                "VMs are the part of the same Compute - VN level Max Flows "\
                "Provisioning is not working"

        self.waiting_for_flow_timeout()

        # Modifiy max flows to differnet values
        # Setting MAX Flows on VN-1
        vn1_max_flows_modified = vn1_max_flows + 500
        flows_to_create = vn1_max_flows_modified + 500
        vn1_fix.set_max_flows(max_flows=vn1_max_flows_modified)
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm12_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=vn1_max_flows_modified)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows_modified))
        if total_flow_count == vn1_max_flows_modified:
            self.logger.info("VN level Max Flows Provisioning is working fine "\
                             "as per modified value")
        assert total_flow_count == vn1_max_flows_modified, \
                "VN level Max Flows is not working as per modified value"

        # check other VN-2 should allow all the flows
        total_flow_count = self.verify_max_flows_limit(
                src=vm21_fix,
                dst=vm22_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=flows_to_create)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % ('Not Configured'))
        if total_flow_count >= flows_to_create:
            self.logger.info("VN-2 is allowing all the flows")
        assert total_flow_count >= flows_to_create, \
                "Other VN (VN-2) impacted due to VN level max flows \
                 configuration @ VN-1"

        self.waiting_for_flow_timeout()

        # Reset the VN level Max flows to default value (0)
        vn1_fix.set_max_flows(max_flows=0)
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm12_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=flows_to_create)
        self.logger.info("Total Obtained Flow Count: %d" % (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                            'Deleted - It should allow the flows'))
        if total_flow_count >= flows_to_create:
            self.logger.info("VN level Max Flows Provisioning is deleted \
                              properly")
        assert total_flow_count >= flows_to_create, \
                "VN level Max Flows Provisioning is not deleted properly"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_max_flows_vmi_level(self):
        '''
        Description:
                Verify max_flows functionality at VMI level
        Test steps:
               1.Create a virtual network (vn1)
               2.Launch  vm11, vm12 and vm13 on vn1 network
               3.Configure vmi level max_flows as 500, 700 and 800 on vmi11, vmi12 and vmi13 respectively
               5.Verify traffic between the VMs
               6.send 1000 flows traffic from vm11 to vm13 , it should allow only 500 flows @vmi11
               7.send 1400 flows traffic from vm12 to vm13, it should all only 700 flows @vmi12
               8.Increment and Decrement the max_flows value on vm11 and vm12 respectively
               9.verify modified values are enforced by sending traffic
               10.Delete the max_flows @ all VMIs ( by setting the value as 0 )
               11.send traffics across vm11, vm12 and vm13 , it should allow all the traffic
        Pass criteria:
               Number of flows should be created as per max_flows configured at VMI level.
               After modification, it should work as per modified value
               After deleting max_flows configuration, it should allow all the flows.
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)
        vmi13_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  port_ids=[vmi13_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])

        # Setting MAX Flows
        vmi11_max_flows = 500
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)
        vmi12_max_flows = 700
        vmi12_fix.set_max_flows(max_flows=vmi12_max_flows)
        vmi13_max_flows = 800
        vmi13_fix.set_max_flows(max_flows=vmi13_max_flows)

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)
        vm11_inspect = self.agent_inspect[vm11_fix.vm_node_ip]
        vm12_inspect = self.agent_inspect[vm12_fix.vm_node_ip]
        vm13_inspect = self.agent_inspect[vm13_fix.vm_node_ip]

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        # check drop-new-flows is unset
        self.logger.info("checking drop_new_flows flag before sending traffics")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm12_tap_intf = vm12_inspect.get_vna_tap_interface_by_ip(vm12_fix.vm_ip)
        vm13_tap_intf = vm13_inspect.get_vna_tap_interface_by_ip(vm13_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm11_fix.vm_name,
                            vm11_drop_new_flows))
        vm12_drop_new_flows = vm12_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm12_fix.vm_name,
                            vm12_drop_new_flows))
        vm13_drop_new_flows = vm13_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm13_fix.vm_name,
                            vm13_drop_new_flows))

        if vm11_drop_new_flows != 'false' or vm11_drop_new_flows != 'false'\
                or vm13_drop_new_flows != 'false' :
            assert False, "drop_new_flows flag is set before sending traffics"

        self.waiting_for_flow_timeout()

        # save pre-traffic flow count on VMI13
        pre_flow_count_vm13 = self.get_total_flow_count(
                dest_ip=vm13_fix.vm_ip,
                vrf_id=vm13_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm13_fix.get_local_ip(),
                vrouter_fixture=vm13_vrouter_fixture)
        # get_total_flow_count counts regular, dns & metadata flow entries
        # counts both the forward and reverse direction flow entries
        # this results in double counting when only source or destionation
        # is specified.
        pre_flow_count_vm13 //= 2

        # Verify Max_flows functionality on VMI level
        total_flow_count_vm11 = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 500,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']

        total_flow_count_vm12 = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi12_max_flows + 200,
                verify_at='src',
                expected_flow_count=vmi12_max_flows)
        vm12_tap_intf = vm12_inspect.get_vna_tap_interface_by_ip(vm12_fix.vm_ip)
        vm12_drop_new_flows = vm12_tap_intf[0]['drop_new_flows']

        total_flow_count_vm13 = self.get_total_flow_count(
                dest_ip=vm13_fix.vm_ip,
                vrf_id=vm13_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm13_fix.get_local_ip(),
                vrouter_fixture=vm13_vrouter_fixture)
        vm13_tap_intf = vm13_inspect.get_vna_tap_interface_by_ip(vm13_fix.vm_ip)
        vm13_drop_new_flows = vm13_tap_intf[0]['drop_new_flows']

        # check drop-new-flows in set, since max-flows level was exceeded
        self.logger.info("checking drop_new_flows flag after traffic")
        self.logger.info("%s drop_new_flows: %s" % (vm11_fix.vm_name,
                            vm11_drop_new_flows))
        vm12_drop_new_flows = vm12_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm12_fix.vm_name,
                            vm12_drop_new_flows))
        vm13_drop_new_flows = vm13_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm13_fix.vm_name,
                            vm13_drop_new_flows))
        if vm11_drop_new_flows != 'true' or vm11_drop_new_flows != 'true' \
                or vm13_drop_new_flows != 'true' :
            assert False, "drop_new_flows flag is NOT set even after \
                           max_flows exceeded.."

        # verify that only max-flows were allowed
        self.logger.info("Total Obtained Flow Count @ vm11: %d"% (
                            total_flow_count_vm11))
        self.logger.info("Total Expected Flow Count @ vm11: %d" % (
                            vmi11_max_flows))
        self.logger.info("Total Obtained Flow Count @ vm12: %d"% (
                            total_flow_count_vm12))
        self.logger.info("Total Expected Flow Count @ vm12: %d" % (
                            vmi12_max_flows))
        self.logger.info("Total Obtained Flow Count @ vm13: %d"% (
                            total_flow_count_vm13))
        self.logger.info("Total Expected Flow Count @ vm13: %d" % (
                            vmi13_max_flows))
        self.logger.info("Pre Flow Count @ vm13: %d" % (pre_flow_count_vm13))
        total_flow_count_vm13 -= pre_flow_count_vm13
        self.logger.info("Adjusted Total Expected Flow Count @ vm13: %d" % (
                            total_flow_count_vm13))
        if total_flow_count_vm11 == vmi11_max_flows:
            self.logger.info("VMI level (vm11) Max Flows Provisioning is fine")
        if total_flow_count_vm12 == vmi12_max_flows:
            self.logger.info("VMI level (vm12) Max Flows Provisioning is fine")
        if total_flow_count_vm13 == vmi13_max_flows:
            self.logger.info("VMI level (vm13) Max Flows Provisioning is fine")
        assert total_flow_count_vm11 == vmi11_max_flows, \
            "VMI (vm11) level Provisioning is not working"
        assert total_flow_count_vm12 == vmi12_max_flows, \
            "VMI (vm12) level Provisioning is not working"
        assert total_flow_count_vm13 == vmi13_max_flows, \
            "VMI (vm13) level Provisioning is not working"

        self.waiting_for_flow_timeout()

        # check drop-new-flows are cleared after flows expire
        self.logger.info("checking drop_new_flows flag after flow timeout")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm12_tap_intf = vm12_inspect.get_vna_tap_interface_by_ip(vm12_fix.vm_ip)
        vm13_tap_intf = vm13_inspect.get_vna_tap_interface_by_ip(vm13_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm11_fix.vm_name,
                            vm11_drop_new_flows))
        vm12_drop_new_flows = vm12_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm12_fix.vm_name,
                            vm12_drop_new_flows))
        vm13_drop_new_flows = vm13_tap_intf[0]['drop_new_flows']
        self.logger.info("%s drop_new_flows: %s" % (vm13_fix.vm_name,
                            vm13_drop_new_flows))
        if vm11_drop_new_flows != 'false' or vm11_drop_new_flows != 'false' or\
                vm13_drop_new_flows != 'false' :
            assert False, \
                "drop_new_flows flag is set even after flows timedout..."

        # Modifiy max flows to differnet values
        # increase MAX Flows on VMI 11
        # decrease MAX Flows on VMI 12
        # unchanged MAX Flows on VMI 13
        vmi11_max_flows_modified = vmi11_max_flows + 50
        vmi12_max_flows_modified = vmi12_max_flows - 50
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows_modified)
        vmi12_fix.set_max_flows(max_flows=vmi12_max_flows_modified)

        # save pre-traffic flow count on VMI13
        pre_flow_count_vm13 = self.get_total_flow_count(
                dest_ip=vm13_fix.vm_ip,
                vrf_id=vm13_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm13_fix.get_local_ip(),
                vrouter_fixture=vm13_vrouter_fixture)
        # get_total_flow_count counts regular, dns & metadata flow entries
        # counts both the forward and reverse direction flow entries
        # this results in double countine when only source or destionation
        # is specified
        pre_flow_count_vm13 /= 2

        total_flow_count_vm11 = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows_modified * 2,
                verify_at='src',
                expected_flow_count=vmi11_max_flows_modified)
        total_flow_count_vm12 = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi12_max_flows_modified + 100,
                verify_at='src',
                expected_flow_count=vmi12_max_flows_modified)
        total_flow_count_vm13 = self.get_total_flow_count(
                dest_ip=vm13_fix.vm_ip,
                vrf_id=vm13_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm13_fix.get_local_ip(),
                vrouter_fixture=vm13_vrouter_fixture)

        # verify that only max-flows were allowed as per modified config
        self.logger.info("Total Obtained Flow Count @ vm11: %d"% (
                            total_flow_count_vm11))
        self.logger.info("Total Expected Flow Count @ vm11: %d" % (
                            vmi11_max_flows_modified))
        self.logger.info("Total Obtained Flow Count @ vm12: %d"% (
                            total_flow_count_vm12))
        self.logger.info("Total Expected Flow Count @ vm12: %d" % (
                            vmi12_max_flows_modified))
        self.logger.info("Total Obtained Flow Count @ vm13: %d"% (
                            total_flow_count_vm13))
        self.logger.info("Total Expected Flow Count @ vm13: %d" % (
                            vmi13_max_flows))
        self.logger.info("Pre Flow Count @ vm13: %d" % (pre_flow_count_vm13))
        total_flow_count_vm13 -= pre_flow_count_vm13
        self.logger.info("Adjusted Total Expected Flow Count @ vm13: %d" % (
                            total_flow_count_vm13))
        if total_flow_count_vm11 == vmi11_max_flows_modified:
            self.logger.info("VMI(vm11) level Max Flows Provisioning is "\
                             "working as per modified value")
        if total_flow_count_vm12 == vmi12_max_flows_modified:
            self.logger.info("VMI level (vm12) Max Flows Provisioning is "\
                             "working as per modified value")
        if total_flow_count_vm13 == vmi13_max_flows:
            self.logger.info("VMI level (vm12) Max Flows Provisioning is "\
                             "working unchanged")
        assert total_flow_count_vm11 == vmi11_max_flows_modified, \
            "VMI (vm11) level Max Flows is not working as per modified value"
        assert total_flow_count_vm12 == vmi12_max_flows_modified, \
            "VMI (vm12) level Max Flows is not working as per modified value"
        assert total_flow_count_vm13 == vmi13_max_flows, \
            "VMI (vm13) level Provisioning was changed, is not working"

        self.waiting_for_flow_timeout()

        # Reset the VMI level Max flows to default value (0)
        vmi11_fix.set_max_flows(max_flows=0)
        vmi12_fix.set_max_flows(max_flows=0)
        vmi13_fix.set_max_flows(max_flows=0)

        flows_to_create = 1000
        total_flow_count_vm11 = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=flows_to_create)
        total_flow_count_vm12 = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=flows_to_create,
                verify_at='src',
                expected_flow_count=flows_to_create)
        total_flow_count_vm13 = self.get_total_flow_count(
                dest_ip=vm13_fix.vm_ip,
                vrf_id=vm13_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm13_fix.get_local_ip(),
                vrouter_fixture=vm13_vrouter_fixture)

        # verify that all the flows were allowed
        self.logger.info("Total Obtained Flow Count @ vm11: %d"% (
                                total_flow_count_vm11))
        self.logger.info("Total Expected Flow Count @ vm11: %d" % (
                                flows_to_create))
        self.logger.info("Total Obtained Flow Count @ vm12: %d"% (
                                total_flow_count_vm12))
        self.logger.info("Total Expected Flow Count @ vm12: %d" % (
                                flows_to_create))
        self.logger.info("Total Obtained Flow Count @ vm13: %d"% (
                                total_flow_count_vm13))
        self.logger.info("Total Expected Flow Count @ vm13: %d" % (
                                flows_to_create * 2))
        if total_flow_count_vm11 >= flows_to_create:
            self.logger.info("VMI(vm11) level Max Flows is deleted properly")
        if total_flow_count_vm12 >= flows_to_create:
            self.logger.info("VMI(vm12) level Max Flows is deleted properly")
        if total_flow_count_vm13 >= flows_to_create * 2:
            self.logger.info("VMI(vm13) level Max Flows is deleted properly")
        assert total_flow_count_vm11 >= flows_to_create, \
                "VMI (vm11) level Provisioning is not deleted properly"
        assert total_flow_count_vm12 >= flows_to_create, \
                "VMI (vm12) level Provisioning is not deleted properly"
        assert total_flow_count_vm13 >= flows_to_create * 2, \
                "VMI (vm13) level Provisioning is not deleted properly"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_max_flows_precedence(self):
        '''
        Description:
                Verify precedence order between VMI level and VN level configuration
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch  vm11, vm12 and vm13 on vn1 network
               3.configure max_flows as 400 @ VN level (vn1)
               4.configure max_flows as 1000 and 2000 on VMIs ( vmi11 and vmi13) respectively
               5.send traffic between vm11 and vm12 and it should allow only 1000 flows
               6.send traffic between vm12 and vm13 , it should all only 400 flows
               7.Delete VMI level configuration @ vmi11 (max_flows=0)
               8.Now send traffic between vm11 and vm12 and it should allow only 400 flows
        Pass criteria:
               VMI level is preferred when max_flows configured @ both VMI and VN level
               After removing configration from VMI level, it should use VN level value
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)
        vmi13_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  port_ids=[vmi13_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])

        # Setting MAX Flows
        vn1_max_flows = 400
        vmi11_max_flows = 1000
        vmi13_max_flows = 2000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)
        vmi13_fix.set_max_flows(max_flows=vmi13_max_flows)

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 300,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("VMI level precedence over VN level is working")
        assert total_flow_count == vmi11_max_flows, \
                "VMI level precedence over VN level failed"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("No VMI level configuration - VN level "\
                             "max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "No VMI level configuration - VN level not applied"

        self.waiting_for_flow_timeout()

        # Reset the VN level Max flows to default value (0)
        vmi11_fix.set_max_flows(max_flows=0)

        # Verify Max_flows functionality on VN level is applied when
        # configuration at VMI level is reset
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                            'VMI level Deleted - Should use VN level'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VMI level deleted properly, VN level applied")
        assert total_flow_count == vn1_max_flows, \
                    "VMI level Max Flows Provisioning is not deleted properly"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_max_flows_precedence_with_max_vm_flows(self):
        '''
        Description:
                Verify precedence order between VMI level and VN level configuration
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch  vm11, vm12 and vm13 on vn1 network
               3.configure max_flows as 400 @ VN level (vn1)
               4.configure max_flows as 1000 and 2000 on VMIs ( vmi11 and vmi13) respectively
               5.configure max_vm_flows as 0.02 @ vm11 (vm level)
               6.send traffic between vm11 and vm12 and it should allow only 1000 flows
               7.send traffic between vm12 and vm13 , it should all only 400 flows
               8.Delete VMI level configuration @ vmi11 (max_flows=0)
               9.Now send traffic between vm11 and vm12
               10.It should allow only 400 flows, as per VN level configuration
               11.Delete VN level configration @ vn1 (max_flows=0)
               12.Now send traffic between vm11 and vm12
               13.It should allow only ~120 flows, as per max_vm_flows configuration
        Pass criteria:
               Precedence order:  VMI > VN > max_vm_flows
               After removing configration from VMI level, it should use VN level value
               After removing VN level, it should use VM level ( max_vm_flows)
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)
        vmi13_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  port_ids=[vmi13_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)

        # Setting MAX Flows
        vn1_max_flows = 400
        vmi11_max_flows = 1000
        vmi13_max_flows = 2000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)
        vmi13_fix.set_max_flows(max_flows=vmi13_max_flows)
        vm11_vrouter_fixture.set_per_vm_flow_limit(0.02)
        self.addCleanup(self.cleanup_test_max_vm_flows_vrouter_config, [vm11_vrouter_fixture])
        self.logger.info("Sleeping for 360 secs...")
        time.sleep(360)
        self.logger.info("Sleeping for 360 secs...Completed")

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level and Compute level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 300,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("VMI level has precedence over VN & compute level")
        assert total_flow_count == vmi11_max_flows, \
                "VMI level precendence over VN & Compute level not working"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration and has precendence over Compute level
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("No VMI level configuration - VN level "\
                             "max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "No VMI (VMI12) level, VN level not taking effect"

        self.waiting_for_flow_timeout()

        # Reset the VMI level Max flows to default value (0)
        vmi11_fix.set_max_flows(max_flows=0)

        # Verify VN level configuration takes effect when VMI level is deleted
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                'VMI level Deleted - Should use VN level'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VN level has precedence over compute level "\
                             "VMI level is deleted")
        assert total_flow_count == vn1_max_flows, \
                "VN level precendence over Compute level not working "\
                "when VMI level is deleted"

        self.waiting_for_flow_timeout()

        # Reset the VN level Max flows to default value (0)
        vn1_fix.set_max_flows(max_flows=0)

        # Verify Compute level configuration takes effect when
        # VMI & VN level is deleted
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows,
                verify_at='src',
                expected_flow_count=120)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
            'VMI & VN level Deleted - Should use Compute level'))
        self.logger.info("Total Expected Flow Count: ~120 flows(0.02*512K)")
        #if total_flow_count < 130 and total_flow_count > 100:
        if 100 < total_flow_count < 130:
            self.logger.info("VN level is deleted properly and it uses "\
                             "max_vm_flows Value")
        else:
            assert False, "VN level Max Flows Provisioning is not deleted "\
                          "properly, it should use max_vm_flows level value"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_max_flows_vn_level_already_has_some_vmis(self):
        '''
        Description:
                Verify max_flows functionality at VN which already has some VMIs
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch  vm11, vm12  vn1 network
               3.configure max_flows as 1000 @ vn1
               4.send traffic between vm11 and vm12 and it should allow only 1000 flows
               4.Launch 1 more VM(vm13) on vn1 network
               5.Verify traffic between the vm13 and vm12, it shouls allow only 1000 flows
        Pass criteria:
               Number of flows should be created as per max_flows configured at VN level.
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create 2 of the VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm12_fix)])

        # Setting MAX Flows VN-1
        vn1_max_flows = 1000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm12_fix,
                flow_count=vn1_max_flows + 100,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VN level Max Flows Provisioning working for "\
                             "pre-existing VMs")
        assert total_flow_count == vn1_max_flows, \
            "VN level Max Flows Provisioning not working on "\
            "pre-existing VMs"

        self.logger.info("Creating 1 more VM on the same VN....")
        # Create the 3rd VM
        vm13_fix = self.create_vm(vm_name='vm13',
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm13_fix, vm12_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VN level for the new VM
        total_flow_count = self.verify_max_flows_limit(
                src=vm13_fix,
                dst=vm12_fix,
                flow_count=vn1_max_flows + 250,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VN level Max Flows Provisioning working for new VM")
        assert total_flow_count == vn1_max_flows, \
            "VN level Max Flows Provisioning not working on new VM"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_drop_new_flows_flag(self):
        '''
        Description:
               Verify Drop new flows flag is set once flow count value exceeds max_flows
               and flag is set as false after flow count value reduces below 90% max_flows
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch VMs( vm11, vm12) on vn1 network
               3.configure max_flows as 1000 @ VMI (vmi11)
               4.create 15% (150) of max flows
               5.wait for 60 secs
               6.create 85+% of flows, should only allow 1000 flows and drop_new_flags should be set
               7.wait for 60 secs, the first set (15%) of flows should expire
               8.drop_new_flows flag should be removed (False),onces flows reduces below <90%
        Pass criteria:
               drop_new_flows flag should be set when flow rate exceeds max_flows
               flag should be removed once number of flows reduces to <=90% of max_flows
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])

        vm11_inspect = self.agent_inspect[vm11_fix.vm_node_ip]
        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm12_fix)])

        # Setting MAX Flows only on VMI 11
        vmi11_max_flows = 1000
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)

        # ensure drop-new-flows is unset before creating flows
        self.logger.info("drop_new_flows flag values @ vifs before sending traffics...")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                    vm11_drop_new_flows))
        if vm11_drop_new_flows != 'false':
            assert False, "drop_new_flows flag is set before sending traffics"

        self.waiting_for_flow_timeout()

        # create 20% of the target flows
        vmi11_max_flows_high = int(vmi11_max_flows * 0.9)
        vmi11_max_flows_low = int(vmi11_max_flows * 0.2)
        self.create_flows(src_ip=vm11_fix.vm_ip,
                          dst_ip=vm12_fix.vm_ip,
                          flow_count=vmi11_max_flows_low,
                          vm_fix=vm11_fix)
        total_flow_count = self.get_total_flow_count(
                source_ip=vm11_fix.vm_ip,
                dest_ip=vm12_fix.vm_ip,
                vrf_id=vm11_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm11_fix.get_local_ip(),
                vrouter_fixture=vm11_vrouter_fixture)
        self.logger.info("Total Obtained Flow Count: %d"% (
                            total_flow_count))
        self.logger.info("Total Expected Flow Count: about %d" % (
                            vmi11_max_flows_low))

        # wait and create flows to exceed beyond configured max flows
        sleep_time = 60
        self.logger.info('waiting %d secs before restarting traffic' % sleep_time)
        time.sleep(sleep_time)
        self.create_flows(src_ip=vm11_fix.vm_ip,
                          dst_ip=vm12_fix.vm_ip,
                          flow_count=vmi11_max_flows_high,
                          vm_fix=vm11_fix,
                          sport=2500)
        total_flow_count = self.get_total_flow_count(
                source_ip=vm11_fix.vm_ip,
                dest_ip=vm12_fix.vm_ip,
                vrf_id=vm11_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm11_fix.get_local_ip(),
                vrouter_fixture=vm11_vrouter_fixture)
        self.logger.info("Total Obtained Flow Count: %d"% (
                            total_flow_count))
        self.logger.info("Total Expected Flow Count: about %d" % (
                            vmi11_max_flows))

        # verify the drop-new-flows flags is set, traffic exceeeds configured
        # max-flow level
        self.logger.info("drop_new_flows flag values @ vifs after max_flows exceeds..")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                        vm11_drop_new_flows))
        if vm11_drop_new_flows != 'true':
            assert False, "drop_new_flows flag is NOT set after max_flows execeeded.."

        # wait for first set of flows to expire
        # no.of flows should drop below 90% of the target
        # drop-new-flows flags should be unset
        sleep_time = self.DEFAULT_FLOW_TIMEOUT - 30
        self.logger.info('waiting %d secs for some flows to expire' % sleep_time)
        time.sleep(sleep_time)
        total_flow_count = self.get_total_flow_count(
                source_ip=vm11_fix.vm_ip,
                dest_ip=vm12_fix.vm_ip,
                vrf_id=vm11_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm11_fix.get_local_ip(),
                vrouter_fixture=vm11_vrouter_fixture)
        self.logger.info("Total Obtained Flow Count: %d" % (
                            total_flow_count))
        self.logger.info("Total Expected Flow Count: < %d" % (
                            vmi11_max_flows_high))
        if total_flow_count < vmi11_max_flows_high:
            self.logger.info("flows scaled down to below 90%")
        assert total_flow_count <= vmi11_max_flows_high, \
                "flows did not scale down below 90%"

        # verify the drop-new-flows flags is unset, now the flows < 90%
        self.logger.info("drop_new_flows flag values after flows < 90%")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                        vm11_drop_new_flows))
        if vm11_drop_new_flows != 'false':
            assert False, "drop_new_flows flag is set even after flowcount "\
                          " to reduces < 90% of max_flows"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_dropstats(self):
        '''
        Description:
           Verify VN max_flows with values as  -1
           Verify VMI max_flows with values as  -1
           Verify vrouter drop_stats are incremented properly after exceeding max_flows limit
           Verify clearing dropstats counter
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch VMs( vm11, vm12) on vn1 network
               3.Try configuring max_flows as -1 @ VN level
               4.Try configuring max_flows as -1 @ VMI level
               5.Configure VMI level max_flows as 1000 @ vmi11
               4.send traffic (1000 flows)  between vm11 and vm12
               5.verify dropstats (New Flow Drops), it should not be increated
               6.send traffic (2000 flows) between vm11 and vm12
               7.verify dropstats (New Flow Drop), it should be increated
               8.clear dropstats values using dropstats --clear
               9.verify counter (New Flow Drop) value
        Pass criteria:
               It should NOT allow configuration of negative values (-1)
               dropstats(New Flow Drop) should not be incremented when flows are <= max_flows
               dropstats(New Flow Drop) should be incremented when flows are > max_flows
               Counter value should become 0 after doing clear dropstats
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)

        # Try configuring negative value @ VN level ...
        self.logger.info("Try Configuring negative value @ VN level ...")
        try:
            vn1_fix.set_max_flows(max_flows=-1)
        except Exception as exp :
            self.logger.info(str(exp))
            self.logger.info("Not able to configure negative value (-1) "\
                             "@ VN level max_flows")
        else:
            assert False, \
                "Able to configure negative value (-1) @ VN level max_flows"

        self.logger.info("Try Configuring negative value @ VMI level ...")
        try:
            vmi11_fix.set_max_flows(max_flows=-1)
        except Exception as exp :
            self.logger.info(str(exp))
            self.logger.info("Not able to configure negative value (-1) "\
                             "@ VMI level max_flows")
        else:
            assert False, \
                "Able to configure negative value (-1) @ VMI level max_flows"

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])

        vm11_inspect = self.agent_inspect[vm11_fix.vm_node_ip]
        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm12_fix)])

        # Setting MAX Flows only on VMI 11
        vmi11_max_flows = 1000
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)

        # ensure drop-new-flows is unset
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                    vm11_drop_new_flows))
        if vm11_drop_new_flows != 'false':
            assert False, "drop_new_flows flag is set before sending traffics"

        # cache dropstats counter
        dropstats = vm11_inspect.get_agent_vrouter_drop_stats()
        pre_traffic_drop_count = int(dropstats['ds_drop_new_flow'])
        self.logger.info("cache pre-traffic ds_drop_new_flow: %d" % (
                            pre_traffic_drop_count))
 
        self.waiting_for_flow_timeout()

        # save pre-traffic flow count
        pre_flow_count = self.get_total_flow_count(
                dest_ip=vm11_fix.vm_ip,
                vrf_id=vm11_vrouter_fixture.get_vrf_id(vn1_fix.vn_fq_name),
                metadata_ip=vm11_fix.get_local_ip(),
                vrouter_fixture=vm11_vrouter_fixture)
        # get_total_flow_count counts regular, dns & metadata flow entries
        # counts both the forward and reverse direction flow entries
        # this results in double counting when only source or destionation
        # is specified.
        pre_flow_count /= 2

        # create exactly configured max-flow, number of flows
        # close enough is good enough
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm11_fix,
                flow_count=vmi11_max_flows - pre_flow_count,
                verify_at='dst',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))

        # verify drop-new-flows is unset, since traffic didn't exceed
        # configured max-flows
        self.logger.info("drop_new_flows flag values before max_flows exceeds")
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                    vm11_drop_new_flows))
        if vm11_drop_new_flows != 'false':
            assert False, \
                "drop_new_flows flag is set even before max_flows execeeded"

        # check no increase in dropstats
        dropstats = vm11_inspect.get_agent_vrouter_drop_stats()
        post_traffic_drop_count = int(dropstats['ds_drop_new_flow'])
        self.logger.info("post-traffic ds_drop_new_flow: %d" % (
                            post_traffic_drop_count))
        if pre_traffic_drop_count == post_traffic_drop_count:
            self.logger.info("Dropstats for 'New Flow Drops' is not "\
                             "incremented when num of flows <= max_flows")
        else:
            assert False, "Dropstats for 'New Flow Drops' is incremented "\
                          "when num of flows <= max_flows"

        self.waiting_for_flow_timeout()

        flows_to_create = vmi11_max_flows + 500
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm11_fix,
                flow_count=flows_to_create,
                verify_at='dst',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))

        # verify drop-new-flows is set
        vm11_tap_intf = vm11_inspect.get_vna_tap_interface_by_ip(vm11_fix.vm_ip)
        vm11_drop_new_flows = vm11_tap_intf[0]['drop_new_flows']
        self.logger.info("drop_new_flows flag value @ vm11: %s " % (
                    vm11_drop_new_flows))
        if vm11_drop_new_flows != 'true':
            assert False, \
                "drop_new_flows flag is unset when max_flows execeeded"

        # verify proportional increase in drop counter
        # two flows correspond to single traffic stream and traffic is
        # unidirectional, so would expect to seen counter increase by
        # half the additional flows over and above max-flows
        expected_drop = (flows_to_create - vmi11_max_flows) // 2
        expected_drop_high = expected_drop + 10
        expected_drop_low = expected_drop - 10
        time_taken = 0
        for i in range(6, 0, -1):
            time.sleep(10)
            time_taken += 10
            dropstats = vm11_inspect.get_agent_vrouter_drop_stats()
            post_traffic_drop_count = int(dropstats['ds_drop_new_flow'])
            drop_count_diff  = post_traffic_drop_count - pre_traffic_drop_count
            self.logger.info("%d: New Flow Drops %d expected: %d" % (i,
                                    drop_count_diff, expected_drop))
            if expected_drop_low <= drop_count_diff <= expected_drop_high:
                self.logger.info("New Flow Drops stats value detected "\
                                 "after %d seconds" % time_taken)
                break
        else:
            assert False, \
            "Dropstats for 'New Flow Drops' is NOT incremented"

        # Verify clearing drop stats
        self.inputs.run_cmd_on_server(vm11_fix.vm_node_ip,
                "contrail-tools dropstats --clear")
        time_taken = 0
        for i in range(6, 0, -1):
            time.sleep(10)
            time_taken += 10
            dropstats = vm11_inspect.get_agent_vrouter_drop_stats()
            cleared_drop_count = int(dropstats['ds_drop_new_flow'])
            self.logger.info("%d: New Flow Drops cleared? %d " % (i,
                                cleared_drop_count))
            if cleared_drop_count <= 10:
                self.logger.info("New Flow Drops cleared after "\
                                 "%d seconds" % time_taken)
                break
        else:
            assert False, "Dropstats(Drop New Flows) is NOT cleared"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_restart_vrouter_agent(self):
        '''
        Description:
               Verify VMI level functionality after restart of Vrouter Agent
        Test steps:
               1.Create a virtual network (vn1)
               2.Launch  vm11, vm12 and vm13 on vn1 network
               3.Configure vmi level max_flows as 1000, 2000 and 3000 on vmi11, vmi12 and vmi13 respectively
               5.Verify traffic between the VMs
               6.send 2000 flows traffic from vm11 to vm13 , it should allow only 1000 flows @vmi11
               7.send 4000 flows traffic from vm12 to vm13, it should all only 2000 flows @vmi12
               8.Modify the max_flows value as 1500 @ vmi11
               9.verify sending traffic between vm11 and vm13, now it should all 1500 flows
               10.Delete the max_flows @ all VMIs ( by setting the value as 0 )
               11.send traffics across vm11, vm12 and vm13 , it should allow all the traffic
        Pass criteria:
               Number of flows should be created as per max_flows configured at VMI level.
               After modification, it should work as per modified value
               After deleting max_flows configuration, it should allow all the flows.
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)
        vmi13_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  port_ids=[vmi13_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])

        # Setting MAX Flows
        vn1_max_flows = 400
        vmi11_max_flows = 1000
        vmi13_max_flows = 2000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)
        vmi13_fix.set_max_flows(max_flows=vmi13_max_flows)

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 350,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("VMI level precedence over VN level is working")
        assert total_flow_count == vmi11_max_flows, \
                "VMI level precedence over VN level failed"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("No VMI level configuration - VN level "\
                             "max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "No VMI level configuration - VN level not applied"

        self.logger.info("Restarting Vrouter Agent...")
        self.inputs.restart_service('contrail-vrouter-agent', [vm11_fix.vm_node_ip], container='agent', verify_service=True)
        self.inputs.restart_service('contrail-vrouter-agent', [vm12_fix.vm_node_ip], container='agent', verify_service=True)
        self.logger.info("After Agent restart, Sleeping for 180 secs...")
        time.sleep(180)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 200,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("After Agent restart: VMI level precedence "\
                             "over VN level is working")
        assert total_flow_count == vmi11_max_flows, \
                "After Agent restart: VMI level precedence over VN level failed"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("After Agent restart: No VMI level configuration "\
                             " - VN level max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "After Agent restart: No VMI level configuration - VN level "\
                "not applied"

        self.waiting_for_flow_timeout()

        # Reset the VN level Max flows to default value (0)
        vmi11_fix.set_max_flows(max_flows=0)

        # Verify Max_flows functionality on VN level is applied when
        # configuration at VMI level is reset
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                            'VMI level Deleted - Should use VN level'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("VMI level deleted properly, VN level applied")
        assert total_flow_count == vn1_max_flows, \
                    "VMI level Max Flows Provisioning is not deleted properly"

        self.logger.info("Restarting Vrouter Agent...")
        self.inputs.restart_service('contrail-vrouter-agent', [vm11_fix.vm_node_ip], container='agent', verify_service=True)
        self.inputs.restart_service('contrail-vrouter-agent', [vm12_fix.vm_node_ip], container='agent', verify_service=True)
        self.logger.info("After Agent restart, Sleeping for 180 secs...")
        time.sleep(180)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm12_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VN level is applied when
        # configuration at VMI level is reset
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                            'VMI level Deleted - Should use VN level'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("After Agent restart: VMI level deleted properly,"\
                             " VN level applied")
        assert total_flow_count == vn1_max_flows, \
                    "After Agent restart: VMI level Max Flows Provisioning " \
                    "is not deleted and VN level not applied"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("After Agent restart: No VMI level configuration "\
                             "- VN level max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "After Agent restart: No VMI level configuration - VN level "\
                "not applied"

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_restart_vm(self):
        '''
        Description:
               Verify VMI level functionality after restart of VM
        Test steps:
               1.Create a virtaul network (vn1)
               2.Launch VMs( vm11, vm12) on vn1 network
               3.configure max_flows as 1000 @ VMI (vmi11)
               4.send traffic (2000 flows)  between vm11 and vm12
               5.it should allow only 1000 flows and drop_new_flows should be set (true)
               6.Keep sending 90% of flows @ every 60 seconds
               7.wait for flow timeout to happens
               8.drop_new_flows flag should be removed (False),onces flows reduces below <90%
        Pass criteria:
               drop_new_flows flag should be set when flow rate exceeds max_flows
               flag should be removed once number of flows reduces to <=90% of max_flows
        Maintainer : mmohan@juniper.net
        '''

        # Create Virtual Networks (VNs)
        vn1_fix = self.create_vn('vn1', ['21.0.0.0/24'])

        # Create VMIs
        vmi11_fix = self.setup_vmi(vn1_fix.uuid)
        vmi12_fix = self.setup_vmi(vn1_fix.uuid)
        vmi13_fix = self.setup_vmi(vn1_fix.uuid)

        # Create VMs
        compute_nodes = self.orch.get_hosts()
        vm11_fix = self.create_vm(vm_name='vm11',
                                  port_ids=[vmi11_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])
        vm12_fix = self.create_vm(vm_name='vm12',
                                  port_ids=[vmi12_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[1])
        vm13_fix = self.create_vm(vm_name='vm13',
                                  port_ids=[vmi13_fix.uuid],
                                  vn_fixture=vn1_fix,
                                  image_name='ubuntu-traffic-py3',
                                  node_name=compute_nodes[0])

        # Setting MAX Flows
        vn1_max_flows = 400
        vmi11_max_flows = 1000
        vmi13_max_flows = 2000
        vn1_fix.set_max_flows(max_flows=vn1_max_flows)
        vmi11_fix.set_max_flows(max_flows=vmi11_max_flows)
        vmi13_fix.set_max_flows(max_flows=vmi13_max_flows)

        vm11_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm11_fix.vm_node_ip)
        vm12_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm12_fix.vm_node_ip)
        vm13_vrouter_fixture = ComputeNodeFixture(self.connections,
                                                  vm13_fix.vm_node_ip)

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 700,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("VMI level precedence over VN level is working")
        assert total_flow_count == vmi11_max_flows, \
                "VMI level precedence over VN level failed"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("No VMI level configuration - VN level "\
                             "max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "No VMI level configuration - VN level not applied"

        # Restart the VMs
        self.logger.info('Rebooting the VMs...')
        cmd_to_reboot_vm = ['sudo reboot']
        vm11_fix.run_cmd_on_vm(cmds=cmd_to_reboot_vm)
        vm12_fix.run_cmd_on_vm(cmds=cmd_to_reboot_vm)
        assert vm11_fix.wait_till_vm_boots(), \
                    "%s vm did not boot up" % vm11_fix.name
        assert vm12_fix.wait_till_vm_boots(), \
                    "%s vm did not boot up" % vm12_fix.name

        # verify connectivity between vms
        self.verify_vms_and_traffic([(vm11_fix, vm13_fix),
                                     (vm12_fix, vm13_fix)])

        self.waiting_for_flow_timeout()

        #self.logger.info("After VM restart, Sleeping for 180 secs...")
        #self.waiting_for_flow_timeout()
        #time.sleep(240)

        # Verify Max_flows functionality on VMI level has precedence over
        # VN level
        total_flow_count = self.verify_max_flows_limit(
                src=vm11_fix,
                dst=vm13_fix,
                flow_count=vmi11_max_flows + 400,
                verify_at='src',
                expected_flow_count=vmi11_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %d" % (vmi11_max_flows))
        if total_flow_count == vmi11_max_flows:
            self.logger.info("VMI level precedence over VN level is working")
        assert total_flow_count == vmi11_max_flows, \
                "VMI level precedence over VN level failed"

        # Verify Max_flows functionality on VN level is applied in the absence
        # of VMI level configuration
        total_flow_count = self.verify_max_flows_limit(
                src=vm12_fix,
                dst=vm13_fix,
                flow_count=vmi13_max_flows,
                verify_at='src',
                expected_flow_count=vn1_max_flows)
        self.logger.info("Total Obtained Flow Count: %d"% (total_flow_count))
        self.logger.info("Total Expected Flow Count: %s" % (
                    'Not VMI level Configured - Should use VN level value'))
        self.logger.info("Total Expected Flow Count: %d" % (vn1_max_flows))
        if total_flow_count == vn1_max_flows:
            self.logger.info("No VMI level configuration - VN level "\
                             "max flows is used correctly")
        assert total_flow_count == vn1_max_flows, \
                "No VMI level configuration - VN level not applied"
