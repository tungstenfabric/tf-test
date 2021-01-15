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
from common.connections import ContrailConnections
from common.svc_health_check.base import BaseHC
from common.vrouter.base import BaseVrouterTest
from common.maciplearning.base import BaseMacIpLearningTest


class TestMacIp6Learning(BaseVrouterTest, BaseMacIpLearningTest, BaseHC):
    @classmethod
    def setUpClass(cls):
        super(TestMacIp6Learning, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestMacIp6Learning, cls).tearDownClass()

    def setUp(self):
        '''
        1. Create vm1 in vn1, compute1
        1. Create vm2 in vn2, compute2
        2. Create vm3 in vn2, compute1
        3. Create vm4 in vn1, compute1
        4. Assign policy between vn1 and vn2
        5. Create ips for macvlan intfs with same subnet as eth0 for each vm
        6. Sets up contrail-tools
        '''
        super(TestMacIp6Learning, self).setUp()
        self.vn1_name = get_random_name('vn1')
        self.vn2_name = get_random_name('vn2')

        self.vm1_name = get_random_name('vm1')
        self.vm2_name = get_random_name('vm2')
        self.vm3_name = get_random_name('vm3')
        self.vm4_name = get_random_name('vm4')

        self.node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        self.node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']

        self.vn1_fixture = self.create_vn(
            vn_name=self.vn1_name, orch=self.orchestrator)
        self.vn1_v6_subnet = get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])
        self.vn1_fixture.create_subnet({'cidr': self.vn1_v6_subnet})

        self.vn2_fixture = self.create_vn(
            vn_name=self.vn2_name, orch=self.orchestrator)
        self.vn2_v6_subnet = get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])
        self.vn2_fixture.create_subnet({'cidr': self.vn2_v6_subnet})

        assert self.vn1_fixture.set_mac_ip_learning()
        assert self.vn2_fixture.set_mac_ip_learning()

        self.vm1_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='ubuntu',
            vm_name=self.vm1_name,
            node_name=self.node1)
        self.vm2_fixture = self.create_vm(
            vn_fixture=self.vn2_fixture,
            image_name='ubuntu',
            vm_name=self.vm2_name,
            node_name=self.node2)
        self.vm3_fixture = self.create_vm(
            vn_fixture=self.vn2_fixture,
            image_name='ubuntu',
            vm_name=self.vm3_name,
            node_name=self.node1)
        self.vm4_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='ubuntu',
            vm_name=self.vm4_name,
            node_name=self.node1)

        assert self.vm1_fixture.wait_till_vm_is_up()
        assert self.vm2_fixture.wait_till_vm_is_up()
        assert self.vm3_fixture.wait_till_vm_is_up()
        assert self.vm4_fixture.wait_till_vm_is_up()

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

        self.vm1_eth0_ip = self.get_intf_address('eth0', self.vm1_fixture, True)
        self.vm2_eth0_ip = self.get_intf_address('eth0', self.vm2_fixture, True)
        self.vm3_eth0_ip = self.get_intf_address('eth0', self.vm3_fixture, True)
        self.vm4_eth0_ip = self.get_intf_address('eth0', self.vm4_fixture, True)

        self.vm1_macvlan_ip = ":".join(self.vm1_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(self.vm1_eth0_ip.split('/')[0].split(':')[-1]) + 5) + \
            '/128'
        self.vm2_macvlan_ip = ":".join(self.vm2_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(self.vm2_eth0_ip.split('/')[0].split(':')[-1]) + 5) + \
            '/128'
        self.vm3_macvlan_ip = ":".join(self.vm3_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(self.vm3_eth0_ip.split('/')[0].split(':')[-1]) + 5) + \
            '/128'
        self.vm4_macvlan_ip = ":".join(self.vm4_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(self.vm4_eth0_ip.split('/')[0].split(':')[-1]) + 5) + \
            '/128'

        try:
            self.inputs.run_cmd_on_server(self.vm1_fixture.vm_node_ip, "contrail-tools")
            self.inputs.run_cmd_on_server(self.vm2_fixture.vm_node_ip, "contrail-tools")
        except CommandTimeout:
            pass

    @preposttest_wrapper
    def test_maciplearning_flag(self):
        '''
        Description:  Enable MAC-IP learning on virtual network
        Pass criteria:
               1. Mac-Ip learning flag should be enabled on when we do vif --get for dual stack vmi on vn1
        Maintainer : ybadaya@juniper.net
        '''
        # checking flag from vif --get on vm1
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vif_id = self.agent_inspect[self.inputs.host_data[self.inputs.compute_ips[0]]['name']].get_vna_intf_details(
            self.vm1_fixture.get_tap_intf_of_vm()[0]['name'])[0]['index']
        flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" % (vif_id)
        flag = self.inputs.run_cmd_on_server(
            vm1_node_ip, flag_cmd).split(":")[1]
        assert "Ml" in flag, "Mac-ip learning flag is not enabled."

        return True
    # end test_maciplearning_flag

    @preposttest_wrapper
    def test_intra_vn_intra_compute_l2l3_pkt_mode(self):
        '''
        Description:  Learn MAC_IPv6 bindings on VM interface in the same VN and same compute with forwarding mode L2L3 and disabled policy (in Packet Mode).
        Test steps:
               1. Disable policy on vm1 and vm4
               2. Create macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent.
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh
        Maintainer : ybadaya@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()

        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            self.vm1_macvlan_ip.split('/')[0], intf="macvlan1")
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=self.vm4_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + self.vm4_macvlan_ip, "Mac route is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=self.vm4_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm4_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of macvlan intf on vm4 is not present in encap data."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_l2l3_pkt_mode

    @preposttest_wrapper
    def test_intra_vn_inter_compute_l2l3_pkt_mode(self):
        '''
        Description: Learn MAC_IPv6 bindings on VM interface in the same VN and different compute with forwarding mode L2L3 and disabled policy (in Packet Mode).
        Test steps:
               1. Disable policy on vm2 and vm3
               2. Create macvlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent.
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh, nh type is Tunnel
        Maintainer : ybadaya@juniper.net
        '''
        self.vm2_fixture.disable_interface_policy()
        self.vm3_fixture.disable_interface_policy()
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm2_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm3_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm2 to macvlan intf on vm3
        assert self.vm2_fixture.ping_to_ip(
            self.vm3_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm3 to macvlan intf on vm2
        assert self.vm3_fixture.ping_to_ip(
            self.vm2_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm3_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + self.vm3_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 agent inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip=self.vm3_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm3_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet
        # table
        route = inspect_h.get_vrouter_route_table(vm2_vrf_id,
                                        prefix=self.vm3_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm3_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm2_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Tunnel", "Nh type is not Tunnel."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm3_macvlan_ip, int(vm2_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_inter_compute_l2l3_pkt_mode

    @test.attr(type=['sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_l2l3(self):
        '''
        Description: Learn MAC_IPv6 bindings on VM interface in the same VN and same compute with forwarding mode L2/L3.
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent.
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            self.vm1_macvlan_ip.split('/')[0], intf="macvlan1")
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=self.vm4_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + self.vm4_macvlan_ip, "Mac route is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=self.vm4_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm4_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of macvlan intf on vm4 is not present in encap data."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_l2l3

    @preposttest_wrapper
    def test_intra_vn_inter_compute_l2l3(self):
        '''
        Description:  Learn MAC_IPv6 bindings on VM interface in the same VN and different compute with forwarding mode L2/L3.
        Test steps:
               1. Create macvlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent.
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh, nh type is Tunnel
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm2_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm3_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm2 to macvlan intf on vm3
        assert self.vm2_fixture.ping_to_ip(
            self.vm3_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm3 to macvlan intf on vm2
        assert self.vm3_fixture.ping_to_ip(
            self.vm2_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm3_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + self.vm3_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 agent inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip=self.vm3_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm3_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet
        # table
        route = inspect_h.get_vrouter_route_table(vm2_vrf_id,
                                        prefix=self.vm3_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm3_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm2_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Tunnel", "Nh type is not Tunnel."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm3_macvlan_ip, int(vm2_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_inter_compute_l2l3

    @preposttest_wrapper
    def test_intra_vn_intra_compute_vlan_pkt_mode_l2l3(self):
        '''
        Description: Learn MAC_IPv6 bindings on VLAN sub intf in same VN and same compute with forwarding mode as L2L3 only mode and disabled policy (in Packet mode)
        Test steps:
               1. Disable policy on vm1 and vm4
               2. Create macvlan intf on vlan intf on vm1 and vm4. Intf should be on diff subnet
               3. Create vlan vmi with parent vmi vm1 and vm4 respectively
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh
        Maintainer : ybadaya@juniper.net
        '''
        self.vm1_fixture.disable_interface_policy()
        self.vm4_fixture.disable_interface_policy()
        vn2_gw_ip = self.vn2_fixture.get_subnets()[1]['gateway_ip']
        vm1_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 5) + \
            '/128'
        vm1_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 6) + \
            '/128'
        vm4_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 7) + \
            '/128'
        vm4_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 8) + \
            '/128'
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm1_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm1_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm4_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm4_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        mac_cmd = ['ifconfig eth0.100 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_vlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_vlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        parent_vmi_vm1 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm1_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        parent_vmi_vm4 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm4_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm1,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm1_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm1_vlan_ip.split('/')[0]}])
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm4,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm4_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm4_vlan_ip.split('/')[0]}])

        # ping is reqd in order for mac ip learning
        assert self.vm1_fixture.ping_to_ip(vm4_vlan_macvlan_ip.split('/')[0])
        assert self.vm4_fixture.ping_to_ip(vm1_vlan_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            vm4_vlan_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            vm1_vlan_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=vm4_vlan_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + vm4_vlan_macvlan_ip, "Mac route is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=vm4_vlan_macvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (vm4_vlan_macvlan_ip.split("/")[0]))

        # checking if vm4_vlan_macvlan_ip is present in vm1 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=vm4_vlan_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (vm4_vlan_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of macvlan intf on vm4 is not present in encap data."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            vm4_vlan_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1',
               'ip link delete eth0.100']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_vlan_pkt_mode_l2l3

    @preposttest_wrapper
    def test_intra_vn_inter_compute_vlan_pkt_mode_l2l3(self):
        '''
        Description:  Learn MAC_IPv6 bindings on VLAN sub intf in same VN and different compute with forwarding mode as L2L3 only mode and disabled policy (in Packet Mode)
        Test steps:
               1. Disable policy on vm2 and vm3
               2. Create macvlan intf on vlan intf on vm2 and vm3.
               3. Create vlan vmi with parent vmi vm2 and vm3 respectively
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh, Nh type as Tunnel
        Maintainer : ybadaya@juniper.net
        '''
        self.vm2_fixture.disable_interface_policy()
        self.vm3_fixture.disable_interface_policy()
        vn1_gw_ip = self.vn1_fixture.get_subnets()[1]['gateway_ip']
        vm2_vlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 5) + \
            '/128'
        vm2_vlan_macvlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 6) + \
            '/128'
        vm3_vlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 7) + \
            '/128'
        vm3_vlan_macvlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 8) + \
            '/128'
        cmds_vm2 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm2_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm2_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm3_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm3_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        mac_cmd = ['ifconfig eth0.100 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_vlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_vlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        parent_vmi_vm2 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm2_fixture.get_vmi_id(self.vn2_fixture.vn_fq_name))
        parent_vmi_vm3 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm3_fixture.get_vmi_id(self.vn2_fixture.vn_fq_name))
        self.setup_vmi(self.vn1_fixture.uuid,
                       parent_vmi=parent_vmi_vm2,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm2_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn1_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm2_vlan_ip.split('/')[0]}])
        self.setup_vmi(self.vn1_fixture.uuid,
                       parent_vmi=parent_vmi_vm3,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm3_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn1_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm3_vlan_ip.split('/')[0]}])

        # ping is reqd in order for mac ip learning
        assert self.vm2_fixture.ping_to_ip(vm3_vlan_macvlan_ip.split('/')[0])
        assert self.vm3_fixture.ping_to_ip(vm2_vlan_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm2 to macvlan intf on vm3
        assert self.vm2_fixture.ping_to_ip(
            vm3_vlan_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm3 to macvlan intf on vm2
        assert self.vm3_fixture.ping_to_ip(
            vm2_vlan_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm2_fixture)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=vm3_vlan_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + vm3_vlan_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 agent inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip=vm3_vlan_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (vm3_vlan_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet
        # table
        route = inspect_h.get_vrouter_route_table(vm2_vrf_id,
                                        prefix=vm3_vlan_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (vm3_vlan_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm2_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Tunnel", "Nh type is not Tunnel."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            vm3_vlan_macvlan_ip, int(vm2_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1',
               'ip link delete eth0.100']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        return True
    # end test_intra_vn_inter_compute_vlan_pkt_mode_l2l3

    @preposttest_wrapper
    def test_intra_vn_intra_compute_vlan_l2l3(self):
        '''
        Description: Learn MAC_IPv6 bindings on VLAN sub intf in same vn and same compute with forwarding mode as  L2/L3 mode.
        Test steps:
               1. Create macvlan intf on vlan intf on vm1 and vm4. Intf should be on diff subnet
               2. Create vlan vmi with parent vmi vm1 and vm4 respectively
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh
        Maintainer : ybadaya@juniper.net
        '''
        vn2_gw_ip = self.vn2_fixture.get_subnets()[1]['gateway_ip']
        vm1_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 5) + \
            '/128'
        vm1_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 6) + \
            '/128'
        vm4_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 7) + \
            '/128'
        vm4_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 8) + \
            '/128'
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm1_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm1_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm4_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm4_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        mac_cmd = ['ifconfig eth0.100 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_vlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_vlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        parent_vmi_vm1 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm1_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        parent_vmi_vm4 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm4_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm1,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm1_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm1_vlan_ip.split('/')[0]}])
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm4,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm4_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm4_vlan_ip.split('/')[0]}])

        # ping is reqd in order for mac ip learning
        assert self.vm1_fixture.ping_to_ip(vm4_vlan_macvlan_ip.split('/')[0])
        assert self.vm4_fixture.ping_to_ip(vm1_vlan_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm4
        assert self.vm1_fixture.ping_to_ip(
            vm4_vlan_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert self.vm4_fixture.ping_to_ip(
            vm1_vlan_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=vm4_vlan_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + vm4_vlan_macvlan_ip, "Mac route is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=vm4_vlan_macvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (vm4_vlan_macvlan_ip.split("/")[0]))

        # checking if vm4_vlan_macvlan_ip is present in vm1 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=vm4_vlan_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (vm4_vlan_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of macvlan intf on vm4 is not present in encap data."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            vm4_vlan_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1',
               'ip link delete eth0.100']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_vlan_l2l3

    @preposttest_wrapper
    def test_intra_vn_inter_compute_vlan_l2l3(self):
        '''
        Description: Learn MAC_IPv6 bindings on VLAN sub intf in same vn and diff compute with forwarding mode as  L2/L3 mode.
        Test steps:
               1. Create macvlan intf on vlan intf on vm2 and vm3.
               2. Create vlan vmi with parent vmi vm2 and vm3 respectively
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh, Nh type as Tunnel
        Maintainer : ybadaya@juniper.net
        '''
        vn1_gw_ip = self.vn1_fixture.get_subnets()[1]['gateway_ip']
        vm2_vlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 5) + \
            '/128'
        vm2_vlan_macvlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 6) + \
            '/128'
        vm3_vlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 7) + \
            '/128'
        vm3_vlan_macvlan_ip = ":".join(vn1_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn1_gw_ip.split(':')[-1]) + 8) + \
            '/128'
        cmds_vm2 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm2_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm2_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm3_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm3_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        mac_cmd = ['ifconfig eth0.100 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_vlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_vlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        parent_vmi_vm2 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm2_fixture.get_vmi_id(self.vn2_fixture.vn_fq_name))
        parent_vmi_vm3 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm3_fixture.get_vmi_id(self.vn2_fixture.vn_fq_name))
        self.setup_vmi(self.vn1_fixture.uuid,
                       parent_vmi=parent_vmi_vm2,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm2_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn1_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm2_vlan_ip.split('/')[0]}])
        self.setup_vmi(self.vn1_fixture.uuid,
                       parent_vmi=parent_vmi_vm3,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm3_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn1_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm3_vlan_ip.split('/')[0]}])

        # ping is reqd in order for mac ip learning
        assert self.vm2_fixture.ping_to_ip(vm3_vlan_macvlan_ip.split('/')[0])
        assert self.vm3_fixture.ping_to_ip(vm2_vlan_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm2 to macvlan intf on vm3
        assert self.vm2_fixture.ping_to_ip(
            vm3_vlan_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm3 to macvlan intf on vm2
        assert self.vm3_fixture.ping_to_ip(
            vm2_vlan_macvlan_ip.split('/')[0], intf="macvlan1")

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm2_fixture)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=vm3_vlan_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + vm3_vlan_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 agent inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm2_vrf_id,
            ip=vm3_vlan_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (vm3_vlan_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet
        # table
        route = inspect_h.get_vrouter_route_table(vm2_vrf_id,
                                        prefix=vm3_vlan_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (vm3_vlan_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm2_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm2_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Tunnel", "Nh type is not Tunnel."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            vm3_vlan_macvlan_ip, int(vm2_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link delete macvlan1',
               'ip link delete eth0.100']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        return True
    # end test_intra_vn_inter_compute_vlan_l2l3

    @preposttest_wrapper
    def test_inter_vn_intra_compute_intra_subnet(self):
        '''
        Description:  Verify Pod IPv6 connectivity on same compute, inter vn, intra subnet
        Test steps:
               1. Create macvlan intf on vm1 and vm3
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm3_macvlan_ip.split('/')[0]+'/64'),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        time.sleep(30)
        assert self.vm1_fixture.ping_to_ip(self.vn1_fixture.get_subnets()[1]['gateway_ip'], intf="macvlan1")
        assert self.vm3_fixture.ping_to_ip(self.vn2_fixture.get_subnets()[1]['gateway_ip'], intf="macvlan1")
        # from vm1 to mac3 intf
        assert self.vm1_fixture.ping_to_ip(self.vm3_macvlan_ip.split('/')[0])
        # from vm3 to mac1
        assert self.vm3_fixture.ping_to_ip(self.vm1_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm3
        assert self.vm1_fixture.ping_to_ip(
            self.vm3_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm3 to macvlan intf on vm1
        assert self.vm3_fixture.ping_to_ip(
            self.vm1_macvlan_ip.split('/')[0], intf="macvlan1")

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_inter_vn_intra_compute_intra_subnet

    @preposttest_wrapper
    def test_intra_vn_inter_subnet_intra_compute(self):
        '''
        Description: Verify Pod IPv6 connectivity on same compute, intra vn, inter subnet
        Test steps:
               1. Create a VN and launch 2 VMs in it on same compute, diff subnet.
               2. Set mac-ip learning flag on created vn
               3. Create macvlan intf on both the VMs
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        vn1_name = get_random_name("vn1")
        vn1_subnet_list = [get_random_cidr(),get_random_cidr()]
        vn1_subnet_list_v6 = [get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min']),
                           get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])]
        vn1_subnets = [{'cidr': vn1_subnet_list[0], },
                       {'cidr': vn1_subnet_list[1], }]
        vn1_subnets_v6 = [{'cidr': vn1_subnet_list_v6[0], },
                          {'cidr': vn1_subnet_list_v6[1], }]
        vm1_name = get_random_name('vn1-vm1')
        vm2_name = get_random_name('vn1-vm2')
        vn1_fixture = self.create_vn(vn1_name, vn1_subnets)
        vn1_fixture.create_subnet(vn1_subnets_v6[0])
        vn1_fixture.create_subnet(vn1_subnets_v6[1])
        assert vn1_fixture.set_mac_ip_learning()
        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        self.logger.info('Create first VM in the VN')
        vm1_fixture = self.create_vm(vn1_fixture, vm1_name,
                                     image_name='ubuntu', node_name=node1)
        # Create a second VM in second subnet
        port_obj = self.create_port(net_id=vn1_fixture.vn_id,
                                    fixed_ips=[{'subnet_id': vn1_fixture.vn_subnet_objs[1]['id']},
                                               {'subnet_id': vn1_fixture.vn_subnet_objs[3]['id']}])
        vm2_fixture = self.create_vm(vn1_fixture, vm2_name,
                                     image_name='ubuntu',
                                     port_ids=[port_obj['id']], node_name=node1)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        vm1_eth0_ip = self.get_intf_address('eth0', vm1_fixture, True)
        vm2_eth0_ip = self.get_intf_address('eth0', vm2_fixture, True)
        macvlan_ip1 = ":".join(vm1_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(vm1_eth0_ip.split('/')[0].split(':')[-1]) + 5)
        macvlan_ip2 = ":".join(vm2_eth0_ip.split('/')[0].split(
            ':')[:-1]) + ":" + str(int(vm2_eth0_ip.split('/')[0].split(':')[-1]) + 5)

        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (macvlan_ip1 + "/" + \
                            vn1_subnet_list_v6[0].split('/')[1]),
                    'ifup --force eth0']
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (macvlan_ip2 + "/" + \
                            vn1_subnet_list_v6[1].split('/')[1]),
                    'ifup --force eth0']
        vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        assert vm2_fixture.ping_to_ip(vn1_fixture.vn_subnet_objs[3]['gateway_ip'], intf="macvlan1")
        assert vm1_fixture.ping_to_ip(vn1_fixture.vn_subnet_objs[2]['gateway_ip'], intf="macvlan1")
        # from vm1 to macvlan intf on vm2
        assert vm1_fixture.ping_to_ip(macvlan_ip2)
        # from vm2 to macvlan intf on vm1
        assert vm2_fixture.ping_to_ip(macvlan_ip1)
        # ping from macvlan1 intf on vm1 to macvlan intf on vm2
        assert vm1_fixture.ping_to_ip(macvlan_ip2, intf="macvlan1")
        # ping from macvlan1 intf on vm2 to macvlan intf on vm1
        assert vm2_fixture.ping_to_ip(macvlan_ip1, intf="macvlan1")

        return True
    # end test_intra_vn_inter_subnet_intra_compute

    @preposttest_wrapper
    def test_inter_vn_inter_compute(self):
        '''
        Description:  Verify Pod IPv6 connectivity across computes, inter vn
        Test steps:
               1. Create macvlan intf on vm1 and vm2
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm2_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        self.vm2_fixture.ping_to_ip(self.vn2_fixture.get_subnets()[1]['gateway_ip'], intf="macvlan1")
        self.vm1_fixture.ping_to_ip(self.vn1_fixture.get_subnets()[1]['gateway_ip'], intf="macvlan1")
        # from vm1 to mac2
        assert self.vm1_fixture.ping_to_ip(self.vm2_macvlan_ip.split('/')[0])
        # from vm2 to mac1
        assert self.vm2_fixture.ping_to_ip(self.vm1_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm2
        assert self.vm1_fixture.ping_to_ip(
            self.vm2_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert self.vm2_fixture.ping_to_ip(
            self.vm1_macvlan_ip.split('/')[0], intf="macvlan1")

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_inter_vn_inter_compute

    @preposttest_wrapper
    def test_delete_macvlan_intf(self):
        '''
        Description:  Verify that routes corresponding to MAC-IP pair are deleted after mac retries of NS
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
               2. Delete macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should not go
               2. MAC route should be deleted in evpn table
               3. Derived bridge route with peer as EVPN is deleted for MAC2
               4. POD IP is deleted from inet table in agent and vrouter
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        time.sleep(60)
        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # 0 ip should also be deleted
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip="0.0.0.0/32")['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "Mac bridge route is present."

        # checking if vm4_macvlan_ip is absent in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in agent inet table for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        # checking route in vrouter got deleted
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), self.vm4_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route not deleted in vrouter inet table."
        return True
    # end test_delete_macvlan_intf

    @preposttest_wrapper
    def test_delete_vmi(self):
        '''
        Description: Verify that routes corresponding to MAC-IP pairs learnt on VM interface goes down when VM interface is down with forwarding mode L2/L3.
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
               2. Delete vm4.
        Pass criteria:
               1. Ping from vm1 to macvlan intf created on vm4 should not go through.
               2. MAC/IP route should be deleted in evpn table
               3. derived bridge route deleted for MAC2
               4. L3VPN route for  IP2 deleted
               5. On vrouter: Verify stitched mac addr is deleted
               6. On vrouter: Verify POD IP is removed from inet table
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        self.delete_vm(self.vm4_fixture)

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route is present in EVPN table. "

        # 0 ip should not be present
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip="0.0.0.0/32")['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "Mac is not present in bridge table."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in agent inet table for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking route in vrouter got deleted
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), self.vm4_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route not deleted in vrouter inet table."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert not output, "Stitched mac address is present."

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_delete_vmi

    @preposttest_wrapper
    def test_health_check_detach(self):
        '''
        Description: Verify that routes corresponding to MAC-IP pairs learnt on VM interface are intact when health check on VM interface is down
        Test steps:
               1. Attach HC on vm4.
               2. Create macvlan intf on vm4.
               3. Detach HC on vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP and MAC/0-IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC2
               4. L3VPN route for IP2 in agent.
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table, Encap data replaced with MAC2 in nh
        Maintainer : ybadaya@juniper.net
        '''
        shc_fixture = self.create_hc(hc_type="link-local")
        self.attach_shc_to_vmi(shc_fixture, self.vm4_fixture)
        self.addCleanup(self.detach_shc_from_vmi, shc_fixture, self.vm4_fixture)
        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        self.detach_shc_from_vmi(shc_fixture, self.vm4_fixture)
        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=self.vm4_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + self.vm4_macvlan_ip, "Mac route is absent in EVPN table. "

        # 0 ip should also be present
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + "0.0.0.0/32", "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
            vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in agent inet table for %s' %
                       (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=self.vm4_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm4_macvlan_ip))
        nh_id = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools rt --dump %s --family inet6 | grep %s | awk '{print $5}' " %
            (vm1_vrf_id,
             route[0]['prefix'] +
                "/" +
                route[0]['prefix_len']))
        nh_type = self.inputs.run_cmd_on_server(
            vm1_node_ip,
            "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" %
            nh_id).split(":")[1]
        assert nh_type == "Encap", "Nh type is not Encap."
        encap_data = self.inputs.run_cmd_on_server(
            vm1_node_ip, r"contrail-tools  nh --get %s | grep Encap\ Data" % nh_id).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(
            ":", " ") == encap_data, "Mac of macvlan intf on vm4 is not present in encap data."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
    # end test_health_check_detach

    @preposttest_wrapper
    def test_health_check_failure(self):
        '''
        Description: Verify that routes corresponding to MAC-IP pairs learnt on VM interface gets deleted when health check on VM interface fails
        Test steps:
               1. Attach HC on vm4.
               2. Create macvlan intf on vm4.
               3. Ignore icmp pkts on vm4 to make HC fail
        Pass criteria:
               1. Ping from vm1 to vm4 macvlan intf should not go through
               2. MAC route should be deleted in vm1 evpn table
               3. Derived bridge route should be deleted in vm1
               4. POD IP is deleted vm1 inet table in agent and vrouter
               5. Stitched mac addr gets deleted
        Maintainer : ybadaya@juniper.net
        '''
        shc_fixture = self.create_hc(hc_type="link-local")
        self.attach_shc_to_vmi(shc_fixture, self.vm4_fixture)
        self.addCleanup(self.detach_shc_from_vmi, shc_fixture, self.vm4_fixture)
        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        ignore_icmp = ["echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all"]
        self.vm4_fixture.run_cmd_on_vm(ignore_icmp, as_sudo=True)
        time.sleep(30)
        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])
        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route is present in EVPN table. "

        # 0 ip should not be present
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip="0.0.0.0/32")['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC2 bridge route is present."

        # checking if vm4_macvlan_ip is present in vm1 agent inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in agent inet table for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking if route in vrouter inet table got deleted
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), self.vm4_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route not deleted in vrouter inet table."

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm4_macvlan_ip, int(vm1_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert not output, "Stitched mac address is present."
        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
    # end test_health_check_failure

    @preposttest_wrapper
    def test_delete_vlan_intf(self):
        '''
        Description:  Verify that routes corresponding to MAC-IP pairs learnt on VM interface goes down when VLAN sub intf is deleted
        Test steps:
               1. Create macvlan intf on vlan intf on vm1 and vm4. Intf subnet is diff.
               2. Create vlan vmi on vm1 and vm4 respectively
               3. Delete vlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should not go
               2. MAC route should be deleted in evpn table
               3. Derived bridge route with peer as EVPN is deleted for MAC2
               4. POD IP is deleted from inet table in agent and vrouter
        Maintainer : ybadaya@juniper.net
        '''
        vn2_gw_ip = self.vn2_fixture.get_subnets()[1]['gateway_ip']
        vm1_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 5) + \
            '/128'
        vm1_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 6) + \
            '/128'
        vm4_vlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 7) + \
            '/128'
        vm4_vlan_macvlan_ip = ":".join(vn2_gw_ip.split(
            ':')[:-1]) + ":" + str(int(vn2_gw_ip.split(':')[-1]) + 8) + \
            '/128'
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm1_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm1_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link set dev eth0.100 up',
                    'ip -6 addr add %s dev eth0.100 scope global' % (
                        vm4_vlan_ip.split('/')[0] + "/64"),
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (
                        vm4_vlan_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        mac_cmd = ['ifconfig eth0.100 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_vlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_vlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        parent_vmi_vm1 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm1_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        parent_vmi_vm4 = self.vnc_lib.virtual_machine_interface_read(
            id=self.vm4_fixture.get_vmi_id(self.vn1_fixture.vn_fq_name))
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm1,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm1_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm1_vlan_ip.split('/')[0]}])
        self.setup_vmi(self.vn2_fixture.uuid,
                       parent_vmi=parent_vmi_vm4,
                       api_type="contrail",
                       project_obj=self.project.project_obj,
                       vlan_id="100",
                       mac_address=vm4_vlan_mac_addr,
                       fixed_ips=[{'subnet_id': self.get_cidr_mask_vmi_id(self.vn2_fixture, ipv6=True)['v6'][2],
                                   'ip_address':vm4_vlan_ip.split('/')[0]}])

        delete_vlan_cmd = ['ip link delete eth0.100']
        self.vm1_fixture.run_cmd_on_vm(delete_vlan_cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(delete_vlan_cmd, as_sudo=True)
        time.sleep(60)

        assert not self.vm1_fixture.ping_to_ip(vm4_vlan_macvlan_ip.split('/')[0])
        assert not self.vm4_fixture.ping_to_ip(vm1_vlan_macvlan_ip.split('/')[0])
        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            vm4_vlan_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=vm4_vlan_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # 0 ip should also be deleted
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip="0.0.0.0/32")['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC2 bridge route is present"

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=vm4_vlan_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' %
                           (vm4_vlan_macvlan_ip.split("/")[0]))

        # checking Vrouter inet table in vm1 for vm4_vlan_macvlan_ip
        # checking route in vrouter got deleted
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), vm4_vlan_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route not deleted in vrouter inet table."
        return True
    # end test_delete_vlan_intf

    @preposttest_wrapper
    def test_move_ip_locally_l2l3(self):
        '''
        Description: verify that when IP is moved locally, routes get updated correctly. VN forwarding mode is L2/L3.
        Test steps:
               1. Create vm - vm5 with same vn and compute as vm1 and vm4
               2. launch pod1 with MAC1/IP1 in vm1
               3. bring down pod1 and launch pod2 with MAC2/IP1 in vm4
        Pass criteria:
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm5 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1/IP1 is deleted from vm5 evpn table
                                         Derived bridge route is deleted from vm5
               4. After pod2 is launched: MAC2/IP1 is added in vm5 evpn table
                                          Derived bridge route is added in vm5
                                          inet route is updated
                                          stitched mac addr is updated with MAC2
                                          inet route mpls label and nh is changed
               5. On vrouter: Ip is updated in vm5 inet table
        Maintainer : ybadaya@juniper.net
        '''
        vm5_name = get_random_name('vm5')
        vm5_fixture = self.create_vm(
            vn_fixture=self.vn1_fixture,
            image_name='ubuntu',
            vm_name=vm5_name,
            node_name=self.node1)
        assert vm5_fixture.wait_till_vm_is_up()

        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm5 to mac1 intf
        assert vm5_fixture.ping_to_ip(self.vm1_macvlan_ip.split('/')[0])
        # checking evpn table
        vm5_node_ip = vm5_fixture.vm_node_ip
        vm5_vrf_id = self.get_vrf_id(self.vn1_fixture, vm5_fixture)
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm1_macvlan_mac_addr,
            ip=self.vm1_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm1_macvlan_mac_addr + \
            "-" + self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm1_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan_ip1 is present in vm5 inet table
        inspect_h = self.agent_inspect[vm5_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm1_macvlan_ip.split("/")[0]))
        vm5_mpls_label = route['routes'][0]['path_list'][0]['label']
        vm5_inet_nh_id = route['routes'][0]['path_list'][0]['nh']['nh_index']

        # checking if macvlan_ip1 is present in vm5 vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm1_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm1_macvlan_ip))
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm1_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm1_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        cmd = ['ip link set dev macvlan1 down']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        assert self.vm4_fixture.ping_to_ip(self.vn1_fixture.get_subnets()[1]['gateway_ip'] , intf="macvlan1")
        time.sleep(60)

        # from vm5 to mac4 intf
        # sometimes there is little loss in packets observed while pinging, retrying to ensure pod is reachable
        ping_to_macvlan = False
        for i in range(0,4):
            if (vm5_fixture.ping_to_ip(self.vm1_macvlan_ip.split('/')[0])):
                ping_to_macvlan = True
                break
            self.logger.warn("Retrying ping")
        assert ping_to_macvlan, "Ping to macvlan failed."
        # checking evpn table
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=self.vm1_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking if MAC got deleted from vm4 evpn table
        try:
            evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
                vm5_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm1_macvlan_mac_addr,
                ip=self.vm1_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if MAC is deleted in vm4 bridge table
        try:
            peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
                vm5_vrf_id, mac=vm1_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC1 bridge route is present"

        # checking if macvlan4 route is there in inet table for vm1
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm1_macvlan_ip.split("/")[0]))
        assert vm5_mpls_label != route['routes'][0]['path_list'][0]['label'], "Mpls label has not changed."
        assert vm5_inet_nh_id != route['routes'][0]['path_list'][0]['nh']['nh_index'], "Nh has not changed."

        # checking if macvlan4 route is present in vm5 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm1_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm1_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm1_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm4_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        return True
    # end test_move_ip_locally_l2l3

    @preposttest_wrapper
    def test_move_ip_across_computes_l2l3(self):
        '''
        Description: verify that when IP is moved across computes, IP move is detected and old routes are deleted correctly.vn forwarding mode is L2/L3
        Test steps:
               1. Create vm - vm5 with same vn and compute as vm2
               2. launch pod1 with MAC1/IP1 in vm2
               3. bring down pod1 and launch pod2 with MAC2/IP1 in vm3
        Pass criteria:
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm5 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1/IP1 is deleted from vm5 evpn table
                                         Derived bridge route is deleted from vm5
               4. After pod2 is launched: MAC2/IP1 is added in vm5 evpn table
                                          Derived bridge route is added in vm5
                                          inet route is updated
                                          stitched mac addr is updated with MAC2
                                          inet route mpls label is changed
                                          inet route nh is changed to tunnel nh
               5. On vrouter: Ip is updated in vm5
        Pass criteria: Ping between the VMs should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        vm5_name = get_random_name('vm5')
        vm5_fixture = self.create_vm(
            vn_fixture=self.vn2_fixture,
            image_name='ubuntu',
            vm_name=vm5_name,
            node_name=self.node2)
        assert vm5_fixture.wait_till_vm_is_up()
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s/64 dev macvlan1 scope global' % self.vm2_macvlan_ip.split('/')[0],
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm5 to mac2 intf
        assert vm5_fixture.ping_to_ip(self.vm2_macvlan_ip.split('/')[0])

        # checking evpn table
        vm5_node_ip = vm5_fixture.vm_node_ip
        vm5_vrf_id = self.get_vrf_id(self.vn2_fixture, vm5_fixture)
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm2_macvlan_mac_addr,
            ip=self.vm2_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm2_macvlan_mac_addr + \
            "-" + self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm2_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan2 is present in vm3 inet table
        inspect_h = self.agent_inspect[vm5_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_macvlan_ip.split("/")[0]))
        vm5_mpls_label = route['routes'][0]['path_list'][0]['label']

        # checking if macvlan2 is present in vm5 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm2_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm2_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmd = ['ip link set dev macvlan1 down']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s/64 dev macvlan1 scope global' % self.vm2_macvlan_ip.split('/')[0],
                    'ifup --force eth0']
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        assert self.vm3_fixture.ping_to_ip(self.vn2_fixture.get_subnets()[1]['gateway_ip'] , intf="macvlan1")
        time.sleep(60)

        # sometimes there is little loss in packets observed while pinging, retrying to ensure pod is reachable
        ping_to_macvlan = False
        for i in range(0,4):
            if (vm5_fixture.ping_to_ip(self.vm2_macvlan_ip.split('/')[0])):
                ping_to_macvlan = True
                break
            self.logger.warn("Retrying ping")
        assert ping_to_macvlan, "Ping to macvlan failed."
        # checking evpn table
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm2_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking if route for macvlan2 is deleted from vm5 evpn table
        try:
            evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
                vm5_vrf_id,
                vxlanid=self.vn2_vxlan_id,
                mac=vm2_macvlan_mac_addr,
                ip=self.vm2_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan5 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan2 is deleted from vm5 bridge table
        try:
            peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
                vm5_vrf_id, mac=vm2_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC1 bridge route is present"

        # checking if route for macvlan3 is present in vm5 inet table
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_macvlan_ip.split("/")[0]))
        assert vm5_mpls_label != route['routes'][0]['path_list'][0]['label'], "Mpls label has not changed."
        assert route['routes'][0]['path_list'][0]['nh']['type'] == 'tunnel', "Nh type is not tunnel."

        # checking if route for macvlan3 is present vm5 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm2_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_macvlan_ip))
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        return True
    # end test_move_ip_across_computes_l2l3

    @preposttest_wrapper
    def test_move_ip_across_computes_pkt_mode_l2l3(self):
        '''
        Description: verify that when IP is moved across computes, IP move is detected and old routes are deleted correctly.vn forwarding mode is L2/L3 and disabled policy (in Packet Mode)
        Test steps:
               1. Disable policy in vm5, vm2 and vm3
               2. Create vm - vm5 with same vn and compute as vm2
               3. launch pod1 with MAC1/IP1 in vm2
               4. bring down pod1 and launch pod2 with MAC2/IP1 in vm3
        Pass criteria:
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm5 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1/IP1 is deleted from vm5 evpn table
                                         Derived bridge route is deleted from vm5
               4. After pod2 is launched: MAC2/IP1 is added in vm5 evpn table
                                          Derived bridge route is added in vm5
                                          inet route is updated
                                          stitched mac addr is updated with MAC2
                                          inet route mpls label is changed
                                          inet route nh is changed to tunnel nh
               5. On vrouter: Ip is updated in vm5
        Pass criteria: Ping between the VMs should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        vm5_name = get_random_name('vm5')
        vm5_fixture = self.create_vm(
            vn_fixture=self.vn2_fixture,
            image_name='ubuntu',
            vm_name=vm5_name,
            node_name=self.node2)
        assert vm5_fixture.wait_till_vm_is_up()
        vm5_fixture.disable_interface_policy()
        self.vm2_fixture.disable_interface_policy()
        self.vm3_fixture.disable_interface_policy()
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s/64 dev macvlan1 scope global' % self.vm2_macvlan_ip.split('/')[0],
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm5 to mac2 intf
        assert vm5_fixture.ping_to_ip(self.vm2_macvlan_ip.split('/')[0])

        # checking evpn table
        vm5_node_ip = vm5_fixture.vm_node_ip
        vm5_vrf_id = self.get_vrf_id(self.vn2_fixture, vm5_fixture)
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm2_macvlan_mac_addr,
            ip=self.vm2_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm2_macvlan_mac_addr + \
            "-" + self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm2_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan2 is present in vm5 inet table
        inspect_h = self.agent_inspect[vm5_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_macvlan_ip.split("/")[0]))
        vm5_mpls_label = route['routes'][0]['path_list'][0]['label']

        # checking if macvlan2 is present in vm5 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm2_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm2_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s/64 dev macvlan1 scope global' % self.vm2_macvlan_ip.split('/')[0],
                    'ifup --force eth0']

        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        cmd = ['ip link set dev macvlan1 down']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        assert self.vm3_fixture.ping_to_ip(self.vn2_fixture.get_subnets()[1]['gateway_ip'] , intf="macvlan1")
        time.sleep(60)

        # sometimes there is little loss in packets observed while pinging, retrying to ensure pod is reachable
        for i in range(0,4):
            if (vm5_fixture.ping_to_ip(self.vm2_macvlan_ip.split('/')[0])):
                ping_to_macvlan = True
                break
            self.logger.warn("Retrying ping")
        assert ping_to_macvlan, "Ping to macvlan failed."

        # checking evpn table
        evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
            vm5_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm2_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + \
            "-" + self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking if route for macvlan2 is deleted from vm5 evpn table
        try:
            evpn_route = self.agent_inspect[vm5_node_ip].get_vna_evpn_route(
                vm5_vrf_id,
                vxlanid=self.vn2_vxlan_id,
                mac=vm2_macvlan_mac_addr,
                ip=self.vm2_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan5 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
            vm5_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan2 is deleted from vm5 bridge table
        try:
            peer = self.agent_inspect[vm5_node_ip].get_vna_layer2_route(
                vm5_vrf_id, mac=vm2_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC1 bridge route is present"

        # checking if route for macvlan3 is present in vm5 inet table
        route = inspect_h.get_vna_route(
            vrf_id=vm5_vrf_id,
            ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm2_macvlan_ip.split("/")[0]))
        assert vm5_mpls_label != route['routes'][0]['path_list'][0]['label'], "Mpls label has not changed."
        assert route['routes'][0]['path_list'][0]['nh']['type'] == 'tunnel', "Nh type is not tunnel."

        # checking if route for macvlan3 is present vm5 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm5_vrf_id,
                                        prefix=self.vm2_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert route, ('No route seen in vrouter for %s' %
                       (self.vm2_macvlan_ip))
        # checking stitched MAC addr
        stitched_mac_cmd = 'contrail-tools rt --get %s --vrf %d --family inet6 | awk \'{print $6}\'| grep \':\'' % (
            self.vm2_macvlan_ip, int(vm5_vrf_id))
        output = self.inputs.run_cmd_on_server(
            vm5_node_ip, stitched_mac_cmd).split("(")[0]
        assert EUI(output, dialect=mac_unix_expanded) == EUI(
            vm3_macvlan_mac_addr, dialect=mac_unix_expanded), "Stitched mac address is invalid."
        return True
    # end test_move_ip_across_computes_pkt_mode_l2l3

    @preposttest_wrapper
    def test_dynamically_disable_maciplearningflag(self):
        '''
        Description: Dynamically disable MAC-IP learning on VN and verify that all routes correspoding to learnt MAC-IP pairs are deleted
        Test steps:
               2. Create macvlan intf on vm4.
               3. Disable mac-ip learning flag on vm4.
        Pass criteria:
               1. Ping from vm1 to vm4 macvlan intf should not go
               2. MAC route should be deleted in vm1 evpn table
               3. Derived bridge route with peer as EVPN is deleted in vm1
               4. POD IP is deleted from vm1 agent and vrouter inet table
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        assert self.vn1_fixture.set_mac_ip_learning(
            mac_ip_learning_enable=False)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC Bridge route is present "

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking route in vrouter got deleted
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), self.vm4_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route not deleted in vrouter inet table."

        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
    # end test_dynamically_disable_maciplearningflag

    @preposttest_wrapper
    def test_change_fwding_mode(self):
        '''
        Description: dynamically change forwarding mode VN  and verify that routes are added/deleted/updated accordingly for MAC-IP pair
        Test steps:
               1. launch pod1 on vm4
               2. Change fwd mode from l2_l3 to l2
        Pass criteria:
               1. When changed from l2 to l2_l3: vm4 macvlan ip is added to vm1 inet table
                                                 MAC/IP route added to evpn table
               2. When changed from l2_l3 to l2: vm4 macvlan ip is deleted from vm1 inet table
                                                 MAC/IP route deleted from evpn table
               3. On vrouter: flags are updated in vif --list
                              pod ip is added to inet table
        Maintainer : ybadaya@juniper.net
        '''
        # checking flag from vif --list
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vif_id = self.agent_inspect[self.inputs.host_data[self.inputs.compute_ips[0]]['name']].get_vna_intf_details(
            self.vm1_fixture.get_tap_intf_of_vm()[0]['name'])[0]['index']
        flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" % (vif_id)
        flag = self.inputs.run_cmd_on_server(
            vm1_node_ip, flag_cmd).split(":")[1]
        assert ("L2" in flag) and ("L3" in flag), "L3L2 mode is not enabled."

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
            vm1_vrf_id,
            vxlanid=self.vn1_vxlan_id,
            mac=vm4_macvlan_mac_addr,
            ip=self.vm4_macvlan_ip)['mac']
        assert evpn_route == str(self.vn1_vxlan_id) + "-" + vm4_macvlan_mac_addr + \
            "-" + self.vm4_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking if route macvlan4 is in vm1 inet table route
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' %
                       (self.vm4_macvlan_ip.split("/")[0]))

        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l2")

        # checking flag from vif --list
        vif_id = self.agent_inspect[self.inputs.host_data[self.inputs.compute_ips[0]]['name']].get_vna_intf_details(
            self.vm1_fixture.get_tap_intf_of_vm()[0]['name'])[0]['index']
        flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" % (vif_id)
        flag = self.inputs.run_cmd_on_server(
            vm1_node_ip, flag_cmd).split(":")[1]
        assert "L2" in flag, "L2 mode is not enabled."

        # checking evpn table
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is not deleted in EVPN table. "

        # checking if route macvlan4 is in vm1 inet table route
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in inet table for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking for macvlan4 ip in vm1 Vrouter inet table
        route = inspect_h.get_vrouter_route_table(vm1_vrf_id,
                                        prefix=self.vm4_macvlan_ip.split('/')[0],
                                        prefix_len='128',
                                        get_nh_details=True,
                                        v6=True)
        assert not route, ('No route seen in vrouter for %s' %
                           (self.vm4_macvlan_ip))

        return True
    # end test_change_fwding_mode

    @preposttest_wrapper
    def test_fifty_macvlans(self):
        '''
        Description: Creating 50 macvlans on a VMI and checking if 50 inet routes are updated.
        Test steps:
               1. Create 50 macvlan intfs on vm1
        Pass criteria:
               1. Ping between vm4 and macvlans should go thru fine.
               2. macvlan ip is added to inet route
        Maintainer : ybadaya@juniper.net
        '''
        for i in range(1, 51):
            macvlan_ip = ":".join(self.vm1_eth0_ip.split('/')[0].split(
                ':')[:-1]) + ":" + str(int(self.vm1_eth0_ip.split('/')[0].split(':')[-1]) + 5 + i)
            cmds_vm1 = ['ip link add macvlan%d link eth0 type macvlan' % i,
                        'ip link set dev macvlan%d up' % i,
                        'ip -6 addr add %s/64 dev macvlan%d scope global' % (macvlan_ip, i),
                        'ifup --force eth0']

            self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)

        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        inspect_h = self.agent_inspect[vm4_node_ip]
        for i in range(1, 51):
            macvlan_ip = ":".join(self.vm1_eth0_ip.split('/')[0].split(
                ':')[:-1]) + ":" + str(int(self.vm1_eth0_ip.split('/')[0].split(':')[-1]) + 5 + i)
            self.logger.info('Starting ping to macvlan%d' % i)
            # sometimes there is little loss in packets observed while pinging, retrying to ensure pod is reachable
            ping_to_macvlan = False
            for j in range(0,4):
                if(self.vm4_fixture.ping_to_ip(macvlan_ip)):
                    ping_to_macvlan = True
                    break
                self.logger.warn("Retrying ping")
            assert ping_to_macvlan, ("Ping to macvlan%d failed" % i)
            route = inspect_h.get_vna_route(vrf_id=vm4_vrf_id, ip=macvlan_ip)
            assert route, ('No route seen in inet table for %s' % (macvlan_ip))

        return True
    # end test_fifty_macvlans

    @preposttest_wrapper
    def test_vrouter_agent_restart(self):
        '''
        Description: Routes are re-learnt when vrouter_agent container is restarted. Forwarding mode = L2L3
        Test steps:
               1. Create macvlan intf on vm2 and vm3.
        Pass criteria:
               1. After restart : MAC route should be present in evpn table
                                  derived bridge route with peer as EVPN for MAC1 and MAC2
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm2_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm3_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = list(
            self.vm2_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm3_macvlan_mac_addr = list(
            self.vm3_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip.split('/')[0])
        # checking from vm2 to mac3 intf
        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm3_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + "-" + \
            self.vm3_macvlan_ip , "Mac route for macvlan intf of vm3 is absent in vm2 EVPN table."

        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + "-" + \
            "0.0.0.0/32", "Mac route for macvlan intf of vm3 is absent in vm2 EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        self.inputs.run_cmd_on_server(
            vm2_node_ip, "docker restart vrouter_vrouter-agent_1")
        time.sleep(120)
        # sometimes there is little loss in packets observed while pinging, retrying to ensure pod is reachable
        ping_to_macvlan = False
        for j in range(0,4):
            if(self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip.split('/')[0])):
                ping_to_macvlan = True
                break
            self.logger.warn("Retrying ping")
        assert ping_to_macvlan, ("Ping to macvlan failed after restart.")
        time.sleep(120)
        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip=self.vm3_macvlan_ip)['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + "-" + \
            self.vm3_macvlan_ip , "Mac route for macvlan intf of vm3 is absent in vm2 EVPN table."

        evpn_route = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(
            vm2_vrf_id,
            vxlanid=self.vn2_vxlan_id,
            mac=vm3_macvlan_mac_addr,
            ip="0.0.0.0/32")['mac']
        assert evpn_route == str(self.vn2_vxlan_id) + "-" + vm3_macvlan_mac_addr + "-" + \
            "0.0.0.0/32", "Mac route for macvlan intf of vm3 is absent in vm2 EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(
            vm2_vrf_id, mac=vm3_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        assert peer == "EVPN", "Peer is not EVPN."
        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_vrouter_agent_restart

    @preposttest_wrapper
    def test_diff_subnet_macvlanip(self):
        '''
        Description: validate that IP is not learned if it does not belong to same subnet of interface.
        Test steps:
               1. Create macvlan intf on vm4 with different subnet from eth0.
        Pass criteria:
               1. Ping from vm1 to vm4 macvlan intf should not go
               2. MAC route should not be in vm1 evpn table
               3. Derived bridge route with peer as EVPN is not in vm1
               4. POD IP is absent from vm1 agent and vrouter inet table
        Maintainer : ybadaya@juniper.net
        '''
        cidr = get_random_cidr(af='v6', mask=SUBNET_MASK['v6']['min'])
        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (get_random_ip(cidr) + "/64"),
                    'ifup --force eth0']
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        try:
            evpn_route = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(
                vm1_vrf_id,
                vxlanid=self.vn1_vxlan_id,
                mac=vm4_macvlan_mac_addr,
                ip=self.vm4_macvlan_ip)['mac']
        except TypeError:
            evpn_route = None
        assert not evpn_route, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        try:
            peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(
                vm1_vrf_id, mac=vm4_macvlan_mac_addr)['routes'][0]['path_list'][0]['peer']
        except TypeError:
            peer = None
        assert not peer, "MAC Bridge route is present "

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(
            vrf_id=vm1_vrf_id,
            ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' %
                           (self.vm4_macvlan_ip.split("/")[0]))

        # checking route in vrouter
        route_ppl_cmd = 'contrail-tools rt --dump %d --family inet6 | grep %s | awk \'{print $2}\'' % (
            int(vm1_vrf_id), self.vm4_macvlan_ip.split('/')[0])
        output = self.inputs.run_cmd_on_server(vm1_node_ip, route_ppl_cmd)
        assert output != "128", "Route present in vrouter inet table."

        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_diff_subnet_macvlanip

    @preposttest_wrapper
    def test_in_l3_mode(self):
        '''
        Description: Set forwarding mode as L3 only and test if ping to target ip works  .
        Pass criteria:
               1. Ping to target ip should not go through.
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm1_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip -6 addr add %s dev macvlan1 scope global' % (self.vm4_macvlan_ip.split('/')[0] + "/64"),
                    'ifup --force eth0']
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = list(
            self.vm1_fixture.run_cmd_on_vm(mac_cmd).values())[0]
        vm4_macvlan_mac_addr = list(
            self.vm4_fixture.run_cmd_on_vm(mac_cmd).values())[0]

        self.vn1_fixture.add_forwarding_mode(
            project_fq_name=self.inputs.project_fq_name,
            vn_name=self.vn1_name,
            forwarding_mode="l3")

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0])
        # ping from macvlan1 intf on vm1 to macvlan intf on vm4
        assert not self.vm1_fixture.ping_to_ip(
            self.vm4_macvlan_ip.split('/')[0], intf="macvlan1")
        # ping from macvlan1 intf on vm4 to macvlan intf on vm1
        assert not self.vm4_fixture.ping_to_ip(
            self.vm1_macvlan_ip.split('/')[0], intf="macvlan1")

        return True
    # end test_in_l3_mode

