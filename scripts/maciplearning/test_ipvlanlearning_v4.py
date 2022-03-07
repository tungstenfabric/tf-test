from __future__ import absolute_import, unicode_literals
from vnc_api.vnc_api import *
from vcenter import *
from tcutils.util import *
import test
import time
from builtins import str
from builtins import range
from vn_test import *
from vm_test import *
from floating_ip import *
from policy_test import *
from user_test import UserFixture
from multiple_vn_vm_test import *
from tcutils.wrappers import preposttest_wrapper
sys.path.append(os.path.realpath('tcutils/pkgs/Traffic'))
from common.connections import ContrailConnections
from common.device_connection import NetconfConnection, SSHConnection
from common.svc_health_check.base import BaseHC
from common.vrouter.base import BaseVrouterTest
from physical_router_fixture import PhysicalRouterFixture
from common.maciplearning.base import BaseMacIpLearningTest
from common.bgpaas.base import BaseBGPaaS
from common.static_route_table.base import StaticRouteTableBase

class TestIpVlanLearning(BaseVrouterTest, BaseMacIpLearningTest, BaseBGPaaS, StaticRouteTableBase):

    @classmethod
    def setUpClass(cls):
        super(TestIpVlanLearning, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        super(TestIpVlanLearning, cls).tearDownClass()
        
    @skip_because(min_nodes=2)
    def setUp(self):

        '''
        1. Create vm1 in vn1, compute1
        1. Create vm2 in vn1, compute1
        2. Create vm3 in vn1, compute2
        3. Create vm4 in vn2, compute2
        4. Assign policy between vn1 and vn2
        5. Create ips for ipvlan intfs with same subnet as eth0 for each vm
        6. Sets up contrail-tools
        '''
        super(TestIpVlanLearning, self).setUp()
        self.vn1_name = get_random_name('vn1')
        self.vn1_subnets = [get_random_cidr(mask=24)]
        self.vn2_name = get_random_name('vn2')
        self.vn2_subnets = [get_random_cidr(mask=24)]
        
        self.vm1_name = get_random_name('crpd-vm1')
        self.vm2_name = get_random_name('crpd-vm2')
        self.vm3_name = get_random_name('crpd-vm3')
        self.vm4_name = get_random_name('crpd-vm4')
        self.node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']

        self.node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']
        self.vn1_fixture = self.create_vn(
            vn_name=self.vn1_name, vn_subnets=self.vn1_subnets, orch=self.orchestrator)
        self.vn2_fixture = self.create_vn(
            vn_name=self.vn2_name, vn_subnets=self.vn2_subnets, orch=self.orchestrator)
        
        assert self.vn1_fixture.set_mac_ip_learning(), "Setting MAC-IP Learning on VN1 Fails"
        assert self.vn2_fixture.set_mac_ip_learning(), "Setting MAC-IP Learning on VN2 Fails"
        
        self.vm1_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='crpd-ipvlan',
            vm_name=self.vm1_name,
            node_name=self.node1)
        
        self.vm2_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='crpd-ipvlan',
            vm_name=self.vm2_name,
            node_name=self.node1)
        
        self.vm3_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='crpd-ipvlan',
            vm_name=self.vm3_name,
            node_name=self.node2)
        
        self.vm4_fixture = self.create_vm(
            vn_fixture=self.vn2_fixture,
            image_name='crpd-ipvlan',
            vm_name=self.vm4_name,
            node_name=self.node2)
        
        assert self.vm1_fixture.wait_till_vm_is_up()
        assert self.vm2_fixture.wait_till_vm_is_up()
        assert self.vm3_fixture.wait_till_vm_is_up()
        assert self.vm4_fixture.wait_till_vm_is_up()
        
        cmds = ['sudo docker load -i /tmp/crpd-latest.tgz']        
        self.vm1_fixture.run_cmd_on_vm(cmds)
        self.vm2_fixture.run_cmd_on_vm(cmds)
        self.vm3_fixture.run_cmd_on_vm(cmds)
        self.vm4_fixture.run_cmd_on_vm(cmds)
        rules = [
            {
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'any',
                'src_ports': 'any',
                'source_network': self.vn1_name,
                'dest_network': self.vn2_name,
                'dst_ports': 'any',
            },
        ]
        policy_name = get_random_name('policy_allow_all')
        policy_fixture = self.useFixture(
            PolicyFixture(
                policy_name=policy_name, rules_list=rules, inputs=self.inputs,
                connections=self.connections))
        policy_fq_name = [policy_fixture.policy_fq_name]
        self.vn1_fixture.bind_policies(policy_fq_name, self.vn1_fixture.vn_id)
        self.addCleanup(self.vn1_fixture.unbind_policies,
                        self.vn1_fixture.vn_id, [policy_fixture.policy_fq_name])
        self.vn2_fixture.bind_policies(policy_fq_name, self.vn2_fixture.vn_id)
        self.addCleanup(self.vn2_fixture.unbind_policies,
                        self.vn2_fixture.vn_id, [policy_fixture.policy_fq_name])
        self.vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        self.vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        self.logger.info("Checking the connectivity by doing PING test between VM")
        # Between V1 <==> VM2
        assert self.vm1_fixture.ping_to_ip(self.vm2_fixture.vm_ip)
        # Between V1 <==> VM3
        assert self.vm1_fixture.ping_to_ip(self.vm3_fixture.vm_ip)
        # Between V1 <==> VM4
        assert self.vm1_fixture.ping_to_ip(self.vm4_fixture.vm_ip)
        # Between V3 <==> VM2
        assert self.vm2_fixture.ping_to_ip(self.vm3_fixture.vm_ip)
        # Between V2 <==> VM4
        assert self.vm2_fixture.ping_to_ip(self.vm4_fixture.vm_ip)
        # Between V3 <==> VM4
        assert self.vm3_fixture.ping_to_ip(self.vm4_fixture.vm_ip)
       

        self.vm1_eth0_ip = self.get_intf_address('eth0', self.vm1_fixture)
        self.vm2_eth0_ip = self.get_intf_address('eth0', self.vm2_fixture)
        self.vm3_eth0_ip = self.get_intf_address('eth0', self.vm3_fixture)
        self.vm4_eth0_ip = self.get_intf_address('eth0', self.vm4_fixture)
        
        mac_cmd = ["ifconfig eth0 | grep ether | awk '{ print $2 }'"]
        self.vm1_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        self.vm2_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        self.vm3_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        self.vm4_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        
        #try:
        #    self.inputs.run_cmd_on_server(self.vm1_fixture.vm_node_ip, "contrail-tools")
        #    self.inputs.run_cmd_on_server(self.vm2_fixture.vm_node_ip, "contrail-tools")
        #except CommandTimeout:
        #    pass
        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_bfd_health_check_crpd_l2mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip)
            loip = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2', name='ipvlannet')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , network_name='ipvlannet', container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                            
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
            # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            try:
                evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                    vm1_vrf_id,
                    vxlanid=vn1_vxlan_id,
                    mac=self.vm1_mac_addr,
                    ip=container_ip[i] + "/32")['mac']
                
            except TypeError:
                evpn_route = None
                        
            assert evpn_route, "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route is not seen in inet table for %s' % container_ip[i])
            
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container"
           
        return True
    # end ttest_bfd_health_check_crpd_l2mode

        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_bfd_health_check_crpd_default_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create default IPVLAN Docker/Container Network on VM with out providing mode (Default is L2)
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip)
            loip = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, name='ipvlannet1')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i], network_name='ipvlannet1', container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                            
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
            # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            try:
                evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                    vm1_vrf_id,
                    vxlanid=vn1_vxlan_id,
                    mac=self.vm1_mac_addr,
                    ip=container_ip[i] + "/32")['mac']
                
            except TypeError:
                evpn_route = None
                        
            assert evpn_route, "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route is not seen in inet table for %s' % container_ip[i])
            
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container"
           
        return True
    # end ttest_bfd_health_check_crpd_l2mode
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_intra_vn_intra_compute_l2_mode(self):

        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm2_fixture.disable_interface_policy()
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        self.create_crpd_network(self.vm2_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm2_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1 + container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm2_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm2_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm2_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm1_name)
    
            state = self.get_bfd_state_crpd(self.vm2_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm2_name)
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm2_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm2_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            try:
                evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                    vm1_vrf_id,
                    vxlanid=vn1_vxlan_id,
                    mac=self.vm1_mac_addr,
                    ip=container_ip1[i] + "/32")['mac']
            except TypeError:
                evpn_route = None
                        
            assert evpn_route, "Mac route for container_ip is absent in EVPN table. "
            
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
                vm2_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm2_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm2_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm2_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm2_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route not seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM2")
        intf_details = self.agent_inspect[vm2_node_ip].get_vna_intf_details(self.vm2_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM2")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm2_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
        
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
           
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_intra_vn_inter_compute_l2_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm3_fixture.disable_interface_policy()
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        self.create_crpd_network(self.vm3_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm3_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1 + container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm3_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm3_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm3_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm1_fixture)
    
            state = self.get_bfd_state_crpd(self.vm3_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm3_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm3_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm3_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(
                vm3_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm3_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm3_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm3_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm3_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route not seen in inet table for %s' % container_ip2[i])
            
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM3")
        intf_details = self.agent_inspect[vm3_node_ip].get_vna_intf_details(self.vm3_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm3_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
        return True
    # end test_ipvlan_inter_vn_intra_compute_l2_mode
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_inter_vn_inter_compute_l2_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        
        subnet1 = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip1 = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        subnet2 = self.vn2_fixture.get_subnets()[0]['cidr'] 
        gw_ip2 = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet1, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet1, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet2, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet2, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet1, gw_ip1, ipvlan_mode='l2')
        self.create_crpd_network(self.vm4_fixture, subnet2, gw_ip2, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm4_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn2_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn2_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip1,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm4_fixture,
                                    gw_ip=gw_ip2,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm4_fixture, self.vn2_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm4_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm1_fixture)
    
            state = self.get_bfd_state_crpd(self.vm4_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm4_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm4_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm4_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(
                vm4_vrf_id,
                vxlanid=vn2_vxlan_id,
                mac=self.vm4_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn2_vxlan_id) + "-" + self.vm4_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm4_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm4_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM4")
        intf_details = self.agent_inspect[vm4_node_ip].get_vna_intf_details(self.vm4_fixture.tap_intf[self.vn2_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm4_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_inter_vn_intra_compute_l2_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        self.vm3_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        subnet1 = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip1 = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        subnet2 = self.vn2_fixture.get_subnets()[0]['cidr'] 
        gw_ip2 = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet1, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet1, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet2, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet2, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm3_fixture, subnet1, gw_ip1, ipvlan_mode='l2')
        self.create_crpd_network(self.vm4_fixture, subnet2, gw_ip2, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm3_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm4_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn2_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn2_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm3_fixture,
                                    gw_ip=gw_ip1,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm4_fixture,
                                    gw_ip=gw_ip2,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm3_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm3_name
        
        result = self.check_bfd_packets(self.vm4_fixture, self.vn2_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm4_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm3_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm3_fixture)
    
            state = self.get_bfd_state_crpd(self.vm4_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm4_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm3_fixture)
        vm4_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm4_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(
                vm3_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm3_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm3_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm3_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm3_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(
                vm4_vrf_id,
                vxlanid=vn2_vxlan_id,
                mac=self.vm4_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn2_vxlan_id) + "-" + self.vm4_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm4_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm4_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route not seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM3")
        intf_details = self.agent_inspect[vm3_node_ip].get_vna_intf_details(self.vm3_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm3_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM4")
        intf_details = self.agent_inspect[vm4_node_ip].get_vna_intf_details(self.vm4_fixture.tap_intf[self.vn2_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm4_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_inter_vn_inter_compute_default_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        subnet1 = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip1 = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        subnet2 = self.vn2_fixture.get_subnets()[0]['cidr'] 
        gw_ip2 = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet1, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet1, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet2, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet2, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet1, gw_ip1)
        self.create_crpd_network(self.vm4_fixture, subnet2, gw_ip2)
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm4_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn2_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn2_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip1,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm4_fixture,
                                    gw_ip=gw_ip2,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm4_fixture, self.vn2_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm4_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm1_fixture)
    
            state = self.get_bfd_state_crpd(self.vm4_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm4_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm4_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm4_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(
                vm4_vrf_id,
                vxlanid=vn2_vxlan_id,
                mac=self.vm4_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn2_vxlan_id) + "-" + self.vm4_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm4_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm4_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM4")
        intf_details = self.agent_inspect[vm4_node_ip].get_vna_intf_details(self.vm4_fixture.tap_intf[self.vn2_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm4_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
      
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_bfd_health_check_crpd_l2l3_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : vgarnepudi@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2_l3")
                
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        return True
    # end ttest_bfd_health_check_crpd_l2mode
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_intra_vn_intra_compute_l2l3_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm2_fixture.disable_interface_policy()
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2_l3")
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        self.create_crpd_network(self.vm2_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm2_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1 + container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm2_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm2_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm2_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm1_name)
    
            state = self.get_bfd_state_crpd(self.vm2_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm2_name)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm2_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm2_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
                vm2_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm2_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm2_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm2_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm2_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM2")
        intf_details = self.agent_inspect[vm2_node_ip].get_vna_intf_details(self.vm2_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm2_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
    
        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_intra_vn_inter_compute_l2l3_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm3_fixture.disable_interface_policy()
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2_l3")
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        self.create_crpd_network(self.vm3_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm3_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1 + container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm3_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm3_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm3_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm1_fixture)
    
            state = self.get_bfd_state_crpd(self.vm3_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm3_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm3_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm3_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(
                vm3_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm3_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm3_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm3_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm3_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
            
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM3")
        intf_details = self.agent_inspect[vm3_node_ip].get_vna_intf_details(self.vm3_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm3_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
        
        return True
    # end test_ipvlan_inter_vn_intra_compute_l2_mode
    
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_inter_vn_inter_compute_l2l3_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. Verify that only Expected number of Routes are Learned
               3. Verify that All the learned MAC are same as VMI MAC
               4. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        subnet1 = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip1 = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        subnet2 = self.vn2_fixture.get_subnets()[0]['cidr'] 
        gw_ip2 = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2_l3")
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet1, gw_ip1, ipvlan_mode='l2')
        self.create_crpd_network(self.vm4_fixture, subnet2, gw_ip2, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm4_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn2_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn2_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip1,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm4_fixture,
                                    gw_ip=gw_ip2,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm1_name
        
        result = self.check_bfd_packets(self.vm4_fixture, self.vn2_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm4_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm1_fixture)
    
            state = self.get_bfd_state_crpd(self.vm4_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm4_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vm4_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm4_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(
                vm4_vrf_id,
                vxlanid=vn2_vxlan_id,
                mac=self.vm4_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn2_vxlan_id) + "-" + self.vm4_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm4_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm4_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM4")
        intf_details = self.agent_inspect[vm4_node_ip].get_vna_intf_details(self.vm4_fixture.tap_intf[self.vn2_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm4_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_inter_vn_intra_compute_l2l3_mode(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm3_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        subnet1 = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip1 = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        subnet2 = self.vn2_fixture.get_subnets()[0]['cidr'] 
        gw_ip2 = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip1 = []
        container_ip2 = []
        lo_ip1 = []
        lo_ip2 = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip1.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip1.append(loip1)
            
            ip2 = get_an_ip(subnet, offset=30+i)
            container_ip2.append(ip2)
            loip2 = get_an_ip(subnet, offset=130+i)
            lo_ip2.append(loip2)
        
        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2_l3")
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm3_fixture, subnet1, gw_ip1, ipvlan_mode='l2')
        self.create_crpd_network(self.vm4_fixture, subnet2, gw_ip2, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm3_fixture, container_ip=container_ip1[i] , container_name=container_name[i])
            self.create_crpd_container(self.vm4_fixture, container_ip=container_ip2[i] , container_name=container_name[i])
                
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip1})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip2})
        self.attach_shc_to_vn(shc_fixture, self.vn2_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn2_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm3_fixture,
                                    gw_ip=gw_ip1,
                                    lo_ip=lo_ip1[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip1[i])
            
            self.config_bfd_on_crpd(self.vm4_fixture,
                                    gw_ip=gw_ip2,
                                    lo_ip=lo_ip2[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip2[i])
        
        result = self.check_bfd_packets(self.vm3_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm3_name
        
        result = self.check_bfd_packets(self.vm4_fixture, self.vn2_fixture)
        assert result, "BFD packets are not seen on %s" % self.vm4_name
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm3_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %son VM %s" % (container_name[i], self.vm3_fixture)
    
            state = self.get_bfd_state_crpd(self.vm4_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s on VM %s" % (container_name[i], self.vm4_fixture)
                    
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, container_ip2[i], count='10', container_name=container_name[i]), "Ping Fails from Container"
  
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm3_fixture)
        vm4_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm4_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        vn2_vxlan_id = self.vn2_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(
                vm3_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm3_mac_addr,
                ip=container_ip1[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm3_mac_addr + "-" + container_ip1[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm3_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm3_vrf_id,
                ip=container_ip1[i])
            assert route, ('Route seen in inet table for %s' % container_ip1[i])
            
            evpn_route = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(
                vm4_vrf_id,
                vxlanid=vn2_vxlan_id,
                mac=self.vm4_mac_addr,
                ip=container_ip2[i] + "/32")['mac']
            assert evpn_route == str(vn2_vxlan_id) + "-" + self.vm4_mac_addr + "-" + container_ip2[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm4_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm4_vrf_id,
                ip=container_ip2[i])
            assert route, ('Route seen in inet table for %s' % container_ip2[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm3_node_ip].get_vna_intf_details(self.vm3_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm3_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM4")
        intf_details = self.agent_inspect[vm4_node_ip].get_vna_intf_details(self.vm4_fixture.tap_intf[self.vn2_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM3"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM3")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm4_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM2"
                
        return True
    # end test_ipvlan_inter_vn_inter_compute_l2_mode
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_with_50(self):
        '''
        Description: Create more than 50 (51) IPvLAN interface per VMI and Verify that It only learns max 50 IPvLAN IP.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4. Create 50 cRPD Containers on VM.
        Pass criteria:
               1. Verify Contrails Learns Max 50 IPvLAN IPs.
               2. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 50
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, gw_ip, container_name=container_name[i]), "Ping Fails from Container"
                            
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
            # checking evpn table for target mac-ip
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
            
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
        
        return True
    # end ttest_bfd_health_check_crpd_l2mode
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_with_GT_50_negative(self):
        '''
        Description: Create more than 50 (51) IPvLAN interface per VMI and Verify that It only learns max 50 IPvLAN IP.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4. Create 51 cRPD Containers on VM.
        Pass criteria:
               1. Verify Contrails Learns Max 50 IPvLAN IPs.
               2. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 50
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
        for i in range(number_of_container):
            assert self.ping_from_crpd_container(self.vm1_fixture, gw_ip, container_name=container_name[i]), "Ping Fails from Container"
                            
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
            
        ip = get_an_ip(subnet, offset=60)
        self.create_crpd_container(self.vm1_fixture, container_ip=ip , container_name='crpd50')
        
        if not self.ping_from_crpd_container(self.vm1_fixture, gw_ip, container_name='crpd50'):
            self.logger.info ("EXPECTED : Ping should Fail as we are not supporting more than 50 IPvLAN Interface per VMI")
        else:
            self.logger.info ("NOT EXPECTED : Ping should not passed as we are not supporting more than 50 IPvLAN Interface per VMI")
            result = False
        
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=ip)['mac']
        except TypeError:
            evpn_route = None
            self.logger.info ("EXPECTED : Mac route should not present in EVPN table.")
        assert not evpn_route, "NOT EXPECTED : Mac route is present in EVPN table. "
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        return True
    # end test_negative_ipvlan_with_GT_50
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_health_check_detach(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
               6. Detach BFD health check from VN
        Pass criteria:
               1. Verify BFD session is Down after health check is removed from VN.
               2. No Crash is observed.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        self.detach_shc_from_vn(shc_fixture, self.vn1_fixture)
        time.sleep(10)
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Down", "BFD state is not Down on container %s after Detaching Health Check" % container_name[i]
            
        return True
    # end ttest_bfd_health_check_crpd_l2mode
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_with_BFD_vrouter_agent_restart(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
               6. Restart the vRouter Agent
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. No Crash is observed.
               3. Verify BFD session is back up and IPvlan is learnt after vRouter agent comes back up.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route not seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        self.logger.info(" ====> Restarting vRouter Agent <====")
        self.inputs.run_cmd_on_server(

            vm1_node_ip, "docker restart vrouter_vrouter-agent_1")
        time.sleep(120)
        
        assert self.vm1_fixture.wait_till_vm_up()
        time.sleep(30)
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
        
        return True
    # end ttest_bfd_health_check_crpd_l2mode
        
    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_ipvlan_with_BFD_controller_container_restart(self):
        '''
        Description: Run BFD on target IP for IPvLAN Enabled VN and verify BFD session is up as well as IPvLAN IP is learned.
        Test steps:
               1. Create a VM on VN1.
               2. set mac-ip learning flag on VN1
               3. Create IPVLAN Docker/Container Network on VM 
               4: Create 5 cRPD Containers on VM
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on each cRPD Container
               6. Restart the containers on controller node
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
               2. No Crash is observed.
               3. Verify BFD session is back up and IPvlan is learnt after containers comes back up.
        NOTE: Tcpdump utility must be installed on the computes.
        Maintainer : manasd@juniper.net
        '''
        
        restart_services = ['api-server','schema', 'config', 'control']
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
        # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route Not seen in inet table for %s' % container_ip[i])
            
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        self.logger.info(" ====> Restarting containers on Controller <====")
        for service in restart_services:
            self.inputs.restart_container(self.inputs.cfgm_ips, service)
        time.sleep(120)
        
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route Not seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
        
        return True
    # end test_ipvlan_with_BFD_controller_container_restart
    @preposttest_wrapper
    def test_bfd_health_check_vmi_flap_l2mode(self):
        '''
        Description: Run BFD on target IP and verify BFD session is up. Fail BFDD
        on target ip and check if target ip routes are deleted.
        Test steps:
               1. Create a cRPD vm with 3 vns.
               2. Create a test vm for netconf connection
               3. set mac-ip learning flag on test vn
               4. Create and attach BFD health check to the test vn
               5. Configure BFD on crpd
               6. flap the vmi on compute
               7. should not have any impact on MAC ip learning feature  for  existing configs and routes wrt MAC-IP leanring
               8. after flap the vmi ..there should not have any impact on the schema objects
               9. the bfd session and route entries to reflect on computes as before
                  and route entries and the existing Schema objects configs
        Pass criteria:
               1. Verify BFD session is up and IPvlan is learnt.
			   2. Health Check for the target ips should be working with out any issues and route entries should updated according to the MAC/ip bindings after did the vmi flap on computes
               3. existing mac/ip binding should reflect  in bfd sessions and the corresponding route tables
               Maintainer : vgarnepudi@juniper.net
         '''
        
        subnet = self.vn1_fixture.get_subnets()[0]['cidr'] 
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        
        container_name = []
        container_ip = []
        lo_ip = []
        number_of_container = 5
        
        for i in range(number_of_container):
            container_name.append("crpd"+str(i))
            ip1 = get_an_ip(subnet, offset=10+i)
            container_ip.append(ip1)
            loip1 = get_an_ip(subnet, offset=100+i)
            lo_ip.append(loip1)
        
        self.vn1_fixture.set_mac_ip_learning()
        self.create_crpd_network(self.vm1_fixture, subnet, gw_ip, ipvlan_mode='l2')
        
        for i in range(number_of_container):
            self.create_crpd_container(self.vm1_fixture, container_ip=container_ip[i] , container_name=container_name[i])
                  
        # creating BFD health check
        shc_fixture = self.create_hc(
            hc_type='vn-ip-list',
           probe_type='BFD',
            target_ip_list={
                'ip_address': container_ip})
        self.attach_shc_to_vn(shc_fixture, self.vn1_fixture)
        self.addCleanup(self.detach_shc_from_vn, shc_fixture, self.vn1_fixture)
        
        for i in range(number_of_container):
            self.config_bfd_on_crpd(self.vm1_fixture,
                                    gw_ip=gw_ip,
                                    lo_ip=lo_ip[i],
                                    container_name=container_name[i],
                                    containerIP=container_ip[i])
        
        result = self.check_bfd_packets(self.vm1_fixture, self.vn1_fixture)
        assert result, "BFD packets are not seen"
             
        for i in range(number_of_container):
            state = self.get_bfd_state_crpd(self.vm1_fixture, container_name=container_name[i])
            assert state == "Up", "BFD state is not up on container %s" % container_name[i]
                    
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        vn1_vxlan_id = self.vn1_fixture.get_vxlan_id()
        
            # checking evpn table for target mac-ip
        self.logger.info("checking evpn table for target IPvLAN MAC/IP")
        for i in range(number_of_container):
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=vn1_vxlan_id,
                mac=self.vm1_mac_addr,
                ip=container_ip[i] + "/32")['mac']
            assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN table. "
            # checking if route for target_ip is in crpd_vm inet table route
            inspect_h = self.agent_inspect[vm1_node_ip]
            route = inspect_h.get_vna_route(
                vrf_id=vm1_vrf_id,
                ip=container_ip[i])
            assert route, ('Route seen in inet table for %s' % container_ip[i])
        
        self.logger.info("Checking Number of MAC-IP Entries for TAP Interface of VM1")
        intf_details = self.agent_inspect[vm1_node_ip].get_vna_intf_details(self.vm1_fixture.tap_intf[self.vn1_fixture.vn_fq_name]['name'])
        mac_ip_list = intf_details[0].get("mac_ip_list")
        assert len(mac_ip_list) == number_of_container, "Number of MAC-IP List is Not correct as Expected for VM1"
        
        self.logger.info("Checking Learned MAC is same as VMI MAC for VM1")
        for l in mac_ip_list:
            for mac in l.values():
                assert mac == self.vm1_mac_addr, "Learned MAC is not same as VMI MAC for Container for VM1"
                
        # Restart the VM here
        self.logger.info('Rebooting the VM  %s' % (self.vm1_name))
        self.vm1_fixture.reboot()
        time.sleep(120)
        self.vm1_fixture.wait_till_vm_is_up()
        self.vm1_fixture.verify_on_setup()
        assert evpn_route == str(vn1_vxlan_id) + "-" + self.vm1_mac_addr + "-" + container_ip[i] + "/32", "Mac route for container_ip is absent in EVPN tablle. "
        assert state == "Up", "BFD state is not up on container %s" % contaiiner_name[i]
        return True
    # end test_bfd_health_check_vmi_flap_l2mode
    @preposttest_wrapper
    def test_check_bgpaas_with_macip_enabled_vns(self):
        '''
        1. After the setup is brought up ,if the contrail cluster is stable
           create the objects as specified in the Test Description
           project, virtual networks ,and enable mac-ip learning feature ,BFD HC template
        2. Verify that the compute populates route entries for learned MAC/ips with respective tables
        3. verify the reachability among the learned ip address inter ad intra VN
        4. Intra VN should to work
        5. now configure bgpaas and try pinging between the tenant vms and other vms
        6.now remove the bgpaas and verify the  reachability and route on compute
        '''
        vn1_name = get_random_name('bgpaas_vn1')
        vn1_subnets = [get_random_cidr()]
        vn1_fixture = self.create_vn(vn1_name, vn1_subnets)
        assert vn1_fixture.set_mac_ip_learning()
        bgpaas_vm1 = self.create_vm(vn1_fixture, 'bgpaas_vm1',
                                    image_name='ubuntu-bird')
        assert bgpaas_vm1.wait_till_vm_is_up()
        bgp_vm_port = bgpaas_vm1.vmi_ids[bgpaas_vm1.vn_fq_name]
        local_as = random.randint(29000,30000)
        local_ip = bgpaas_vm1.vm_ip
        gw_ip = vn1_fixture.get_subnets()[0]['gateway_ip']
        dns_ip = vn1_fixture.get_subnets()[0]['dns_server_address']
        neighbors = [gw_ip, dns_ip]
        peer_as=self.connections.vnc_lib_fixture.get_global_asn()
        bgpaas_fixture = self.create_bgpaas(
            bgpaas_shared=True, autonomous_system=local_as, bgpaas_ip_address=local_ip)
        self.logger.info('We will configure BGP on the VM')
        self.config_bgp_on_bird(bgpaas_vm1, local_ip,local_as,neighbors, peer_as)
        self.logger.info('Attaching the VMI to the BGPaaS object')
        self.attach_vmi_to_bgpaas(bgp_vm_port, bgpaas_fixture)
        assert bgpaas_fixture.verify_in_control_node(
            bgpaas_vm1), 'BGPaaS Session not seen in the control-node'
        op= bgpaas_vm1.run_cmd_on_vm(cmds=['birdc show protocols bfd1'], as_sudo=True)
        assert 'up' in op['birdc show protocols bfd1'], 'BFD session not UP'
        self.detach_vmi_from_bgpaas(bgp_vm_port, bgpaas_fixture)	
        time.sleep(30)	
        assert not bgpaas_fixture.verify_in_control_node(	
            bgpaas_vm1), 'BGPaaS Session should not be seen in the control-node after deleting vmi'	
    #end test
    @preposttest_wrapper
    def test_ipvlan_move_ip_across_computes_l2(self):
        '''
        Description: verify that when IP is moved across computes, IP move is detected and old routes are deleted correctly.vn forwarding mode is L2/L3
        Test steps:
               1.launch pod1 with MAC1/IP1 in VM1 in compute1
               2.verify routes corresponding to MAC1/IP pair learnt on VM interface of VM1
               3.initiate ping and verify flows on compute1
               4.destroy pod in VM1 and launch pod2 with MAC2/IP1 in VM2 in compute 2
               5.verify that routes of MAC1/IP1 are deleted and new routes for MAC2/IP1 are added
               6.verify that flows are deleted on compute 1 and created on compute 2
        Pass criteria: 
               1.evpn type 2 MAC route for MAC1 is deleted
               2.ecpn type 2 MAC route for MAC2 ias added
               3.derived bridge route for MAC1 is deleted
               4.derived bridge route for MAC2 is added
               On vRouter:
               1.Ensure MAC1 is deleted and MAC2 is added on bridge table
               2.flow should be deleted on compute1 and added on compute 2
        Maintainer : vgarnepudi@juniper.net
        '''
        vm5_name = get_random_name('vm5')
        vm5_fixture = self.create_vm(
        vn_fixture=self.vn2_fixture,
        image_name='ubuntu',
        vm_name=vm5_name,
        node_name=self.node2)
        assert vm5_fixture.wait_till_vm_is_up()
        cmds_vm2 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip link set dev ipvlan1 up',
                    'ip addr add %s/26 dev ipvlan1' % self.vm2_ipvlan_ip.split('/')[0]]
        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        mac_cmd = ['ifconfig ipvlan1 | grep ether | awk \'{ print $2 }\'']
        vm2_ipvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        # from vm5 to mac2 intf
        assert vm5_fixture.ping_to_ip(self.vm2_ipvlan_ip.split('/')[0])
        # checking evpn table
        vm5_node_ip = vm5_fixture.vm_node_ip
        vm5_vrf_id = self.get_vrf_id(self.vn2_fixture, vm5_fixture)
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm2_ipvlan_mac_addr,
            ip=self.vm2_ipvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm2_ipvlan_mac_addr + \
            "-" + self.vm2_ipvlan_ip, "Mac route for ipvlan1 is absent in EVPN table. "
        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm2_ipvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."
        # checking if ipvlan2 is present in vm3 inet table
        inspect_h = self.agent_inspect[vm5_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_ipvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_ipvlan_ip.split("/")[0]))
        vm5_mpls_label = route['routes'][0]['path_list'][0]['label']
        # checking if ipvlan2 is present in vm3 Vrouter inet table
        route = self.get_vrouter_route(self.vm2_ipvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_ipvlan_ip))
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_ipvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm2_ipvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        cmd = ['ip link set dev ipvlan1 down']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        cmds_vm3 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip link set dev ipvlan1 up',
                    'ip addr add %s/26 dev ipvlan1' % self.vm2_ipvlan_ip.split('/')[0]]
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        mac_cmd = ['ifconfig ipvlan1 | grep ether | awk \'{ print $2 }\'']
        vm3_ipvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        # deleting ip in arp cache to improve the time in which arp gets
        # updated
        cmd = ['arp -d %s' % (self.vm2_ipvlan_ip.split('/')[0])]
        vm5_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        time.sleep(30)
        assert vm5_fixture.ping_to_ip(self.vm2_ipvlan_ip.split('/')[0])
        # checking evpn table
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_ipvlan_mac_addr,
            ip=self.vm2_ipvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_ipvlan_mac_addr + \
            "-" + self.vm2_ipvlan_ip, "Mac route for ipvlan1 is absent in EVPN table. "
        # checking if route for ipvlan2 is deleted from vm5 evpn table
        try:
            evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
                vm5_vrf_id,
                vxlanid=self.vn2_vxlan_id,
                mac=vm2_ipvlan_mac_addr,
                ip=self.vm2_ipvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for ipvlan5 is present in EVPN table. "
        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm3_ipvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."
        # checking if route for ipvlan2 is not deleted from vm5 bridge table, as parent exists
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm2_ipvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer, "MAC1 bridge route is not present"
        # checking if route for ipvlan3 is present in vm5 inet table
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_ipvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_ipvlan_ip.split("/")[0]))
        assert vm5_mpls_label != route['routes'][0]['path_list'][0]['label'], "Mpls label has not changed."
        assert route['routes'][0]['path_list'][0]['nh']['type'] == 'tunnel', "Nh type is not tunnel."
        # checking if route for ipvlan3 is present vm5 Vrouter inet table
        route = self.get_vrouter_route(self.vm2_ipvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_ipvlan_ip))
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_ipvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_ipvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        return True
    # end test_ipvlan_move_ip_across_computes_l2    
    @preposttest_wrapper
    def test_ipvlan_static_route_table_inter_vn_inter_compute(self):
        '''
        Description:  Verify multiple network/static  route tables via ipvlan interfaces
        Test steps:
               1. Create netns instances inside the VMs
			   2. Create ipvlan intf on vm1 and vm2.
			   3. Add the ipvlan interfaces to the netns instances
			   4. Add multiple(say 3) addresses to the multiple(say 3) ipvlan interfaces
               5. Create and attach Network static routes with multiple(say   3) ipvlan interfaces
               6. ping vm1 to vm2
               7. make sure the routes are learned
        Pass criteria:
               1. Health Check for the target ips should be working with out any issues and route entries should updated according to the MAC/ip bindings after did the vmi flap on computes
               2. existing mac/ip binding should reflect  in bfd sessions and the corresponding route tables  
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        cmds_vm1 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip netns add testns',
                    'ip link set ipvlan1 netns testns',
                    'ip netns exec testns ip addr add %s dev ipvlan1' % (self.vm1_ipvlan_ip.split('/')[0] + "/26"),
                    'ip netns exec testns ip link set ipvlan1 up',
                    'ip netns exec testns ip addr add 192.168.1.3/24 dev ipvlan1']
        cmds_vm4 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip netns add testns',
                    'ip link set ipvlan1 netns testns',
                    'ip netns exec testns ip addr add %s dev ipvlan1' % (self.vm4_ipvlan_ip.split('/')[0] + "/26"),
                    'ip netns exec testns ip link set ipvlan1 up',
                    'ip netns exec testns ip addr add 192.168.1.4/24 dev ipvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        vn1_uuid = self.vn1_fixture.uuid
        vn2_uuid = self.vn2_fixture.uuid
     
        # Create Network Static route and attach to the VN  
        self.create_and_add_network_static_table_to_vn(prefix="192.168.1.3/32", next_hop=self.vm1_ipvlan_ip.split('/')[0], vn_uuid=vn1_uuid)
        self.create_and_add_network_static_table_to_vn(prefix="192.168.1.4/32", next_hop=self.vm4_ipvlan_ip.split('/')[0], vn_uuid=vn1_uuid)
        mac_cmd = ['ip netns exec testns ifconfig ipvlan1 | grep ether | awk \'{ print $2 }\'']
        vm1_ipvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd, as_sudo=True).values())[0]
        vm4_ipvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd, as_sudo=True).values())[0]
        # Ping Test between VMs
        assert self.vm1_fixture.ping_to_ip(self.vm4_fixture.vm_ip)
        
        # ping from ipvlan1 intf on vm1 to ipvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            self.vm4_ipvlan_ip.split('/')[0], netns="testns")
        # ping from ipvlan1 intf on vm4 to ipvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            self.vm1_ipvlan_ip.split('/')[0], netns="testns")
        # Test ping Between VMs over Secondary IPs inside NETNS
        self.logger.info("Test ping Between VMs over Secondary IPs inside NETNS")
        assert self.vm4_fixture.ping_to_ip("192.168.1.3", netns="testns")
        
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_ipvlan_mac_addr,
            ip=self.vm4_ipvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_ipvlan_mac_addr + \
            "-" + self.vm4_ipvlan_ip, "Mac route is absent in EVPN table. "
        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_ipvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_ipvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "
        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_ipvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."
        # checking if vm4_ipvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_ipvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (self.vm4_ipvlan_ip.split("/")[0]))
        # checking if vm4_ipvlan_ip is present in vm1 vrouter inet table
        route = self.get_vrouter_route(self.vm4_ipvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm4_ipvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route['prefix'] +
                "/" +
                route['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_ipvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of ipvlan intf on vm4 is not present in encap data."
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_ipvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_ipvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        cmd = ['ip netns delete testns']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # End of test_ipvlan_static_route_table_inter_vn_inter_compute
    @preposttest_wrapper
    def test_ipvlan_learn_route_on_controller_extend_to_MX(self):
        '''
        Description:  Automation coverage
        Test steps:
               1. Dynamically change forwarding mode for controller and verify that EVPN type 2 and L3VPN routes are updated accordingly.
        Pass criteria:
               1. create two vns and vms	
               2. create two static route table and add it to vns	
               3. check static routes are present in evpn table	
               4. check routes are exported to SDN(MX) gateway	
               	
        Maintainer : vgarnepudi@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        cmds_vm1 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip netns add testns',
                    'ip link set ipvlan1 netns testns',
                    'ip netns exec testns ip addr add %s dev ipvlan1' % (self.vm1_ipvlan_ip.split('/')[0] + "/26"),
                    'ip netns exec testns ip link set ipvlan1 up',
                    'ip netns exec testns ip addr add 192.168.1.3/24 dev ipvlan1']
        cmds_vm4 = ['ip link add ipvlan1 link ens3 type ipvlan mode l2',
                    'ip netns add testns',
                    'ip link set ipvlan1 netns testns',
                    'ip netns exec testns ip addr add %s dev ipvlan1' % (self.vm4_ipvlan_ip.split('/')[0] + "/26"),
                    'ip netns exec testns ip link set ipvlan1 up',
                    'ip netns exec testns ip addr add 192.168.1.4/24 dev ipvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        vn1_uuid = self.vn1_fixture.uuid
        vn2_uuid = self.vn2_fixture.uuid
     
        # Create Network Static route and attach to the VN  
        self.create_and_add_network_static_table_to_vn(prefix="192.168.1.3/32", next_hop=self.vm1_ipvlan_ip.split('/')[0], vn_uuid=vn1_uuid)
        self.create_and_add_network_static_table_to_vn(prefix="192.168.1.4/32", next_hop=self.vm4_ipvlan_ip.split('/')[0], vn_uuid=vn1_uuid)
        mac_cmd = ['ip netns exec testns ifconfig ipvlan1 | grep ether | awk \'{ print $2 }\'']
        vm1_ipvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd, as_sudo=True).values())[0]
        vm4_ipvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd, as_sudo=True).values())[0]
        # Ping Test between VMs
        assert self.vm1_fixture.ping_to_ip(self.vm4_fixture.vm_ip)
        
        # ping from ipvlan1 intf on vm1 to ipvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            self.vm4_ipvlan_ip.split('/')[0], netns="testns")
        # ping from ipvlan1 intf on vm4 to ipvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            self.vm1_ipvlan_ip.split('/')[0], netns="testns")
        # Test ping Between VMs over Secondary IPs inside NETNS
        self.logger.info("Test ping Between VMs over Secondary IPs inside NETNS")
        assert self.vm4_fixture.ping_to_ip("192.168.1.3", netns="testns")
        
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_ipvlan_mac_addr,
            ip=self.vm4_ipvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_ipvlan_mac_addr + \
            "-" + self.vm4_ipvlan_ip, "Mac route is absent in EVPN table. "
        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_ipvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_ipvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "
        self.logger.info("loginng into MX and verifying exported routes")	
        router_params = list(self.inputs.physical_routers_data.values())[0]	
        mx_ip=router_params['mgmt_ip']	
        mx_pswd=router_params['ssh_password']	
        mx_handle = NetconfConnection(host = mx_ip)	
        mx_handle.connect()	
        exp_route = ['192.168.1.3','193.168.1.4']	
        routes_output = mx_handle.get_config()	
        mx_handle.disconnect()	
        for exp_route in routes_output:	
            ret = re.search(exp_route, routes_output)	
            if ret:	
                self.logger.info("Route seen in MX: %s" % exp_route)	
                break	
            else:	
                assert False, "Route: %s not seen in MX" % exp_route
        cmd = ['ip netns delete testns']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # End of test_ipvlan_learn_route_on_controller_extend_to_MX

