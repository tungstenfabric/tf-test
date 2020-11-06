from __future__ import absolute_import
# Need to import path to test/fixtures and test/scripts/
# Ex : export PYTHONPATH='$PATH:/root/test/fixtures/:/root/test/scripts/'
#
# To run tests, you can do 'python -m testtools.run tests'. To run specific tests,
# You can do 'python -m testtools.run -l tests'
# Set the env variable PARAMS_FILE to point to your ini file. Else it will
# try to pick params.ini in PWD

from tcutils.wrappers import preposttest_wrapper
from common.contrail_fabric.base import BaseFabricTest
import test
import random
from tcutils.util import skip_because

class TestFabricEvpnType5(BaseFabricTest):

    @classmethod
    def setUpClass(cls):
        super(TestFabricEvpnType5, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestFabricEvpnType5, cls).tearDownClass()

    def is_test_applicable(self):
        result, msg = super(TestFabricEvpnType5,
                            self).is_test_applicable()
        if result:
            msg = 'No spines in the provided fabric topology'
            for device in self.inputs.physical_routers_data.keys():
                if self.get_role_from_inputs(device) == 'spine':
                    return (True, None)
        return False, msg

    @test.attr(type=['fabric_sanity'])
    @preposttest_wrapper
    def test_fabric_intervn_basic(self):
        '''
           Create VN vn1
           Create VNs per BMS node
           Create Logical Router and add all the VNs
           Create VM on vn1
           Create untagged BMS instances on respective VNs
           Check ping connectivity across all the instances
        '''
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        bms_fixtures = list(); bms_vns = dict()
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        for bms in self.get_bms_nodes():
            bms_vns[bms] = self.create_vn()
        self.create_logical_router([vn1, vn2]+list(bms_vns.values()))
        vm1 = self.create_vm(vn_fixture=vn1, image_name='ubuntu')
        vm2 = self.create_vm(vn_fixture=vn2, image_name='ubuntu')
        vlan = 3
        for bms in self.get_bms_nodes():
            bms_fixtures.append(self.create_bms(
                bms_name=bms,
                tor_port_vlan_tag=vlan,
                vn_fixture=bms_vns[bms]))
            vlan = vlan + 1
        vm1.wait_till_vm_is_up()
        self.do_ping_mesh(bms_fixtures+[vm1, vm2])

    @test.attr(type=['fabric_sanity'])
    @preposttest_wrapper
    def test_fabric_intervn_tagged(self):
        '''
           Create VN vn1
           Create VNs per BMS node
           Create VM on vn1
           Create Logical Router and add all the VNs
           Create tagged BMS instances on respective VNs
           Check ping connectivity across all the instances
        '''
        vlan = 10
        bms_fixtures = list(); bms_vns = dict()
        vn = self.create_vn()
        for bms in self.get_bms_nodes():
            bms_vns[bms] = self.create_vn()
        vm1 = self.create_vm(vn_fixture=vn, image_name='cirros')
        self.create_logical_router([vn]+list(bms_vns.values()))
        for bms in self.get_bms_nodes():
            bms_fixtures.append(self.create_bms(
                bms_name=bms,
                vn_fixture=bms_vns[bms], vlan_id=vlan))
            vlan = vlan + 10
        vm1.wait_till_vm_is_up()
        self.do_ping_mesh(bms_fixtures+[vm1])

    @preposttest_wrapper
    def test_evpn_type_5_vxlan_traffic_between_vn(self):
        '''
            Configure Encapsulation order as VxLAN, MPLSoverGRE, MPLSoverUDP
            Enable VxLAN Routing under that project settings
            Create Virtual Networks
            Create logical Routers and attach above created VNs
            Create VMs on Virtual Networks
            Verify traffic between accross Virtual Networks

        '''
        vn1 = self.create_vn(); vn2 = self.create_vn()
        vn3 = self.create_vn(); vn4 = self.create_vn()
        lr1 = self.create_logical_router([vn1, vn2], vni=70001)
        lr2 = self.create_logical_router([vn3, vn4], vni=70002)
        vm11 = self.create_vm(vn_fixture=vn1)
        vm12 = self.create_vm(vn_fixture=vn1)
        vm2 = self.create_vm(vn_fixture=vn2)
        vm3 = self.create_vm(vn_fixture=vn3)
        vm4 = self.create_vm(vn_fixture=vn4)
        bms1 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=10,
                vn_fixture=vn2)
        lr1.verify_on_setup()
        lr2.verify_on_setup()
        self.check_vms_booted([vm11, vm12, vm2, vm3, vm4])

        self.logger.info(
            "Verify Traffic between VN-1 and VN-2 on Logical Router: lr1")
        self.verify_traffic(vm11, vm2, 'udp', sport=10000, dport=20000)
        self.logger.info(
            "Verify Traffic between VN-3 and VN-4 on Logical Router: lr2")
        self.verify_traffic(vm3, vm4, 'udp', sport=10000, dport=20000)
        self.do_ping_mesh([vm11, vm2, bms1])
        # end test_evpn_type_5_vxlan_traffic_between_vn

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_evpn_type_5_vm_to_bms_remove_vn_from_lr(self):
        '''
            Configure Encapsulation order as VxLAN, MPLSoverGRE, MPLSoverUDP
            Enable VxLAN Routing under that project settings
            Create Virtual Networks
            Create a Logical Router and attach above created VNs
            Create a VM in VN1
            Assign an IP from VN2 to a BMS
            Verify traffic between VM to BMS
            Now remove VN2 from the LR
            Traffic across the VNs should fail

        '''
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        vn3 = self.create_vn()
        vm1 = self.create_vm(vn_fixture=vn1, image_name='cirros',
              node_name=self.inputs.compute_names[0])
        vm2 = self.create_vm(vn_fixture=vn2, image_name='cirros',
              node_name=self.inputs.compute_names[1])
        vm3 = self.create_vm(vn_fixture=vn3, image_name='cirros',
              node_name=self.inputs.compute_names[1])
        bms1 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=10,
                vn_fixture=vn1)
        lr = self.create_logical_router([vn1, vn2, vn3], vni=70001)
        lr.verify_on_setup()
        self.check_vms_booted([vm1, vm2, vm3])
        self.do_ping_mesh([vm1, vm2, vm3, bms1])

        self.logger.info(
            'Will disassociate VN2 from the LR. Traffic between the BMS and VM should fail')
        lr.remove_interface([vn2.vn_id])
        self.logger.debug(
            "Sleeping for 30 secs to allow config change to be pushed to the Spine")
        self.sleep(30)
        self.do_ping_test(vm1, vm2.vm_ip, expectation=False)
        self.do_ping_test(bms1, vm2.vm_ip, expectation=False)
        self.do_ping_test(vm3, vm2.vm_ip, expectation=False)
        self.do_ping_test(bms1, vm3.vm_ip)
        self.do_ping_test(vm3, bms1.bms_ip)
        self.do_ping_test(vm3, vm1.vm_ip)
        # end test_evpn_type_5_vm_to_bms_remove_vn_from_lr

    @skip_because(min_nodes=2)
    @preposttest_wrapper
    def test_evpn_type_5_vm_to_bms_remove_vni_from_lr(self):
        '''
            Configure Encapsulation order as VxLAN, MPLSoverGRE, MPLSoverUDP
            Enable VxLAN Routing under that project settings
            Create Virtual Networks
            Create a Logical Router and attach above created VNs
            Create a VM in VN1
            Assign an IP from VN2 to a BMS
            Verify traffic between VM to BMS
            Now remove the VNI from the LR
            Traffic across the VNs should continue to work

        '''
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        lr = self.create_logical_router([vn1, vn2], vni=70001)
        vm1 = self.create_vm(vn_fixture=vn1, image_name='cirros',
              node_name=self.inputs.compute_names[0])
        vm2 = self.create_vm(vn_fixture=vn2, image_name='cirros',
              node_name=self.inputs.compute_names[1])
        bms1 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=10,
                vn_fixture=vn2)
        lr.verify_on_setup()
        vm1.wait_till_vm_is_up()
        vm2.wait_till_vm_is_up()
        self.do_ping_mesh([bms1, vm1, vm2])
        self.logger.info(
            'Will delete the VNI associated with the LR. Traffic between the BMS and VM should pass with the system-generated VNI')
        lr.delete_vni()
        self.logger.debug(
            "Sleeping for 30 secs to allow config change to be pushed to the Spine")
        self.sleep(30)
        self.do_ping_mesh([bms1, vm1, vm2])
        # end test_evpn_type_5_vm_to_bms_remove_vni_from_lr

    #Dont think changing RT is supported, Believe RT can only be specified during create and cannot be updated
    @preposttest_wrapper
    def test_evpn_type_5_vm_to_bms_add_rt_to_lr(self):
        '''
            Configure Encapsulation order as VxLAN, MPLSoverGRE, MPLSoverUDP
            Enable VxLAN Routing under that project settings
            Create Virtual Networks
            Create a Logical Router and attach above created VNs
            Create a VM in VN1
            Assign an IP from VN2 to a BMS
            Verify traffic between VM to BMS
            Now add a new RT to the LR
            Traffic across the VNs should continue to work

        '''
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        lr = self.create_logical_router([vn1, vn2], vni=70001)
        vm1 = self.create_vm(vn_fixture=vn1, image_name='cirros',
              node_name=self.inputs.compute_names[0])
        vm2 = self.create_vm(vn_fixture=vn2, image_name='cirros',
              node_name=self.inputs.compute_names[0])
        bms1 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=10,
                vn_fixture=vn2)
        lr.verify_on_setup()
        vm1.wait_till_vm_is_up()
        vm2.wait_till_vm_is_up()
        self.do_ping_mesh([vm1, vm2, bms1])

        self.logger.info('Will add a new Route-Target to the LR.'
           'Traffic between the BMS and VM should continue to pass')
        lr.add_rt('target:64512:12345')
        self.logger.debug(
            "Sleeping for 60 secs to allow config change to be pushed to the Spine")
        self.sleep(60)
        self.do_ping_mesh([vm1, vm2, bms1])
        # end test_evpn_type_5_vm_to_bms_add_rt_to_lr

    @preposttest_wrapper
    def test_logical_router_static_route_update_in_lr_type5_vrf_on_qfx(self):
        '''
         1) Configure Encapsulation order as VxLAN, MPLSoverGRE, MPLSoverUDP
         2) Enable VxLAN Routing under that project settings
         3) Add vn1 and vn2.
         4) Launch a vm and bms in each of vn1 and vn2
         5) Create a logical router and attach it to vn1, vn2 and extend it to crb-gateway
         6) ping from vm to vm and bms to bms from vn1 to vn2
         7) Add static route in lr vrf on crb-gateway verify it gets copied to vn1 and vn2
         8) Verify vm to vm and bms to bms traffic
         9) Delete static route in lr vrf on crb gateway verify it gets removed from vn1 and vn2 vrf
         10) verify vm to vm and bms to bms traffic
         11) Verify path preference for route added by bgp peer has higher prefrence for same route updated in lr vrf
         12) Verify l2 traffic tests
        '''
        vn1 = self.create_vn();
        vn2 = self.create_vn()
        lr1 = self.create_logical_router([vn1, vn2], vni=70001)
        vm11 = self.create_vm(vn_fixture=vn1)
        vm21 = self.create_vm(vn_fixture=vn2)
        bms1 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=10,
                vn_fixture=vn1)
        bms2 = self.create_bms(
                bms_name=random.choice(self.get_bms_nodes()),
                tor_port_vlan_tag=20,
                vn_fixture=vn2)
        lr1.verify_on_setup()
        self.check_vms_booted([vm11, vm21])

        self.logger.info(
            "Verify Traffic between VN-1 and VN-2 on Logical Router: lr1")
        self.verify_traffic(vm11, vm21, 'udp', sport=10000, dport=20000)
        
        self.do_ping_mesh([vm11, vm21, bms1, bms2])

        vn_l2_vm1_name = 'VM1'
        vn_l2_vm2_name = 'VM2'

        vn_l2_vm1_fixture = self.create_vm(vn_fixture=vn1, image_name='ubuntu')
        vn_l2_vm2_fixture = self.create_vm(vn_fixture=vn1, image_name='ubuntu')

        assert vn_l2_vm1_fixture.verify_on_setup()
        assert vn_l2_vm2_fixture.verify_on_setup()

        #l2 traffic verification
        self.mac1=vn_l2_vm1_fixture.mac_addr[vn1.vn_fq_name]
        self.mac2=vn_l2_vm2_fixture.mac_addr[vn1.vn_fq_name]
        filters = 'ether src %s' %(self.mac1)
        tap_intf = vn_l2_vm2_fixture.tap_intf[vn1.vn_fq_name]['name']
        session,pcap = vn_l2_vm2_fixture.start_tcpdump(filters=filters,interface=tap_intf)
        sleep(20)
        self.send_l2_traffic(vn_l2_vm1_fixture,iface='eth1')
        result = verify_tcpdump_count(self, session, pcap, exp_count=10,mac=self.mac2)
        assert result, "L2 traffic verification failed"

        for device in self.inputs.physical_routers_data.keys():
            mgmt_ip = ''
            if self.get_role_from_inputs(device) == 'spine':
               mgmt_ip = device['mgmt_ip']
        self.logger.info(
            "Add static route on spine with mgmt ip %s " %mgmt_ip)
        if len(mgmt_ip) == 0:
            assert(False)
        rt_cmd = "set groups __contrail_overlay_evpn_type5__ routing-instances _contrail_%s_%s routing-options static route 0.0.0.0/0 next-table inet.0" %(name, id)
        static_rt_cmd="cli;edit;%s;commit;exit" % (rt_cmd)

        # Add default route on spine device in type5 lr vrf
        self.inputs.run_cmd_on_server(mgmt_ip, static_rt_cmd, username=self.inputs.fabrics[0]['username'], password=self.inputs.fabrics[0]['password'])
        time.sleep(1)
        # Verify route gets updated in bridge network vn1 conneted to lr1
        vm1_node_ip = vm11.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(vn1, vm11)
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in bridge vn inet table."

        # Verify route gets updated in internal vn for lr1 on compute node of vm1
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=lr1.vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in agent inet table."

        # Verify route gets updated in bridge network vn2 conneted to lr1
        vm2_node_ip = vm21.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(vn2, vm21)
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in bridge vn inet table."

        # Verify route gets updated in internal vn for lr1 on compute node of vm2
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=lr1.vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in agent inet table."

        # Verify traffic after static route add
        self.do_ping_mesh([vm11, vm21, bms1, bms2])

        # create a snat router with gateway set to external vn, attach vn11 and a private network
        vm1_name = get_random_name('vm_private')
        vn1_name = get_random_name('vn_private')
        vn1_subnets = [get_random_cidr()]
        self.allow_default_sg_to_allow_all_on_project(self.inputs.project_name)
        ext_vn_fixture = self.create_external_network(self.connections, self.inputs)
        ext_vn_fixture.verify_on_setup()
        vn1_fixture = self.create_vn(vn1_name, vn1_subnets)
        vn1_fixture.verify_on_setup()
        vm1_fixture = self.create_vm(vn1_fixture, vm1_name,
                                         image_name='ubuntu')
        vm1_fixture.wait_till_vm_is_up()

        router_name = get_random_name('router1')
        router_dict = self.create_router(router_name)
        router_rsp = self.quantum_h.router_gateway_set(
                router_dict['id'],
                ext_vn_fixture.vn_id)
        self.add_vn_to_router(router_dict['id'], vn1_fixture)
        self.add_vn_to_router(router_dict['id'], vn11)

        assert self.verify_snat(vm1_fixture)

        # vn11 is attached to both vxlan lr and snat lr , verify path for default route
        # added by snat lr has higher preference a than path added for static route update
        # from spine device in type5 lr vrf
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in bridge vn inet table."
        assert ['routes'][0]['path_list'][1]['peer'] == "EVPN-ROUTING"
        assert ['routes'][0]['path_list'][0]['peer'] != "EVPN-ROUTING"

        self.delete_vn_from_router(router_dict['id'], vn11)
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip="0.0.0.0")
        assert route, "Route is not present in bridge vn inet table."
        assert ['routes'][0]['path_list'][0]['peer'] == "EVPN-ROUTING"
        # Delete static route on spine device in type5 lr vrf
        rt_cmd = "set groups __contrail_overlay_evpn_type5__ routing-instances _contrail_%s_%s routing-options static route 0.0.0.0/0 discard" %(name, id)
        static_rt_cmd="cli;edit;%s;commit;exit" % (rt_cmd)
        # Add default route on spine device in type5 lr vrf
        self.inputs.run_cmd_on_server(mgmt_ip, static_rt_cmd, username=self.inputs.fabrics[0]['username'], password=self.inputs.fabrics[0]['password'])
        time.sleep(1)

        # Verify route gets deleted in bridge network vn1 conneted to lr1
        vm1_node_ip = vm11.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(vn1, vm11)
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip="0.0.0.0")
        assert not route, "Route is present in bridge vn inet table."

        # Verify route gets deleted in internal vn for lr1 on compute node of vm1
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=lr1.vrf_id,
            ip="0.0.0.0")
        assert not route, "Route is present in agent inet table."

        # Verify route gets deleted in bridge network vn2 conneted to lr1
        vm2_node_ip = vm21.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(vn2, vm21)
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip="0.0.0.0")
        assert not route, "Route is present in bridge vn inet table."

        # Verify route gets deleted in internal vn for lr1 on compute node of vm2
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=lr1.vrf_id,
            ip="0.0.0.0")
        assert not route, "Route is present in agent inet table."

        # Verify traffic after static route add
        self.do_ping_mesh([vm11, vm21, bms1, bms2])
