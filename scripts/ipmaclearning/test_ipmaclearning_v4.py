from __future__ import absolute_import, unicode_literals
from .base import BaseVnVmTest
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
from traffic.core.stream import Stream
from common.vrouter.base import BaseVrouterTest
from common.svc_health_check.base import BaseHC
from common.connections import ContrailConnections
from traffic.core.profile import create, ContinuousProfile
from traffic.core.helpers import Host
from traffic.core.helpers import Sender, Receiver
from common import isolated_creds
import inspect
import time
from tcutils.commands import ssh, execute_cmd, execute_cmd_out
from tcutils.util import get_subnet_broadcast
from tcutils.util import skip_because
import test
from common import isolated_creds
from vcenter import *

class TestIpMacLearning(BaseVrouterTest,BaseVnVmTest, BaseHC):
    
    def setUp(self):
        super(TestBasicVMVN, self).setUp()
        self.vn1_name = get_random_name('vn1')
        self.vn2_name = get_random_name('vn2')

        self.vm1_name = get_random_name('vm1')
        self.vm2_name = get_random_name('vm2')
        self.vm3_name = get_random_name('vm3')
        self.vm4_name = get_random_name('vm4')

        node1 = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        node2 = self.inputs.host_data[self.inputs.compute_ips[1]]['name']

        self.vn1_fixture = self.create_vn(vn_name=self.vn1_name,orch=self.orchestrator)
        self.vn2_fixture = self.create_vn(vn_name=self.vn2_name,orch=self.orchestrator)

        self.vm1_fixture = self.create_vm(vn_fixture=self.vn1_fixture, image_name='ubuntu-traffic', vm_name=self.vm1_name, node_name=node1)
        self.vm2_fixture = self.create_vm(vn_fixture=self.vn2_fixture, image_name='ubuntu-traffic', vm_name=self.vm2_name, node_name=node2)
        self.vm3_fixture = self.create_vm(vn_fixture=self.vn2_fixture, image_name='ubuntu-traffic', vm_name=self.vm3_name, node_name=node1)
        self.vm4_fixture = self.create_vm(vn_fixture=self.vn1_fixture, image_name='ubuntu-traffic', vm_name=self.vm4_name, node_name=node1)

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

        def get_intf_address(intf,pod):
            """
            Routine if to derive the ip address of the interface in a multi interface pod
            :param intf: name of the interface for which te ip address needed to be reutrned
            :param pod: name of the pod
            :return: ipv4 address of the interface
            """
            cmd = ["ifconfig "+intf+" | grep inet"]
            output = pod.run_cmd_on_vm(cmd)
            ip = re.search('inet\s+addr\s*:\s*(\d+.\d+.\d+.\d+)', output['ifconfig eth0 | grep inet'])
            ip_addr = ip.group(1)
            return ip_addr

        self.vm1_eth0_ip = get_intf_address('eth0',self.vm1_fixture)
        self.vm2_eth0_ip = get_intf_address('eth0',self.vm2_fixture)
        self.vm3_eth0_ip = get_intf_address('eth0',self.vm3_fixture)
        self.vm4_eth0_ip = get_intf_address('eth0',self.vm4_fixture)

        self.vm1_macvlan_ip = ".".join(self.vm1_eth0_ip.split(".")[:3]) + "." + str(int(self.vm1_eth0_ip.split(".")[3])+1) + "/26"
        self.vm2_macvlan_ip = ".".join(self.vm2_eth0_ip.split(".")[:3]) + "." + str(int(self.vm2_eth0_ip.split(".")[3])+1) + "/26"
        self.vm3_macvlan_ip = ".".join(self.vm3_eth0_ip.split(".")[:3]) + "." + str(int(self.vm3_eth0_ip.split(".")[3])+1) + "/26"
        self.vm4_macvlan_ip = ".".join(self.vm4_eth0_ip.split(".")[:3]) + "." + str(int(self.vm4_eth0_ip.split(".")[3])+1) + "/26"


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_2(self):
        '''
        Description:  Learn MAC_IPv4 bindings on VM interface in the same VN and same compute with forwarding mode L2.
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. On vrouter: Verify POD IP is added to inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        
        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm4_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm4_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm4_macvlan_ip))

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm4 pod ip
        inspect_h = self.agent_inspect[self.vm4_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        
        return True
    # end test_intra_vn_intra_compute_2
    
    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_2(self):
        ''' 
        Description: Learn MAC_IPv4 bindings on VM interface in the same VN and different compute with forwarding mode L2.
        Test steps:
               1. Create macvlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. On vrouter: Verify POD IP is added to inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm3_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd)

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip)

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm3_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm3_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm2 pod ip
        inspect_h = self.agent_inspect[self.vm2_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm3_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm3_macvlan_ip))

        # from vm3 to mac2 intf
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm3 pod ip
        inspect_h = self.agent_inspect[self.vm3_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True        
    # end test_intra_vn_inter_compute_2

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_l2l3mode_3(self):
        ''' 
        Description: Learn MAC_IPv4 bindings on VM interface in the same VN and same compute with forwarding mode L2/L3.
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. L3VPN route for IP1 and IP2
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table
        Maintainer : ybadaya@juniper.net
        '''
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2_l3") 
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]
        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm4_macvlan_ip, "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        route = self.get_vrouter_route(self.vm4_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm4_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm4_macvlan_ip, vm1_vrf_id)
        output = self.inputs.run_cmd_on_server(vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm4_macvlan_mac_addr, "Stitched mac address is invalid." 

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking inet table for vm6 pod ip
        inspect_h = self.agent_inspect[vm4_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm1_macvlan_ip.split("/")[0]))

        # checking Vrouter inet table for vm6 pod ip
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm1_macvlan_ip, vm4_vrf_id)
        output = self.inputs.run_cmd_on_server(self.vm4_fixture.vm_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm1_macvlan_mac_addr, "Stictched mac address is invalid."

        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2") 

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_3


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_l2l3mode_3(self):
        '''
        Description:  Learn MAC_IPv4 bindings on VM interface in the same VN and different compute with forwarding mode L2/L3.
        Test steps:
               1. Create macvlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. L3VPN route for IP1 and IP2
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table
        Maintainer : ybadaya@juniper.net
        '''
        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2_l3") 
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm3_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd)

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip)

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm3_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm3_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm2_vrf_id, ip=self.vm3_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm3_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet table
        route = self.get_vrouter_route(self.vm3_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm3_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm3_macvlan_ip, vm2_vrf_id)
        output = self.inputs.run_cmd_on_server(vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm3_macvlan_mac_addr, "Stictched mac address is invalid." 


        # from vm3 to mac2 intf
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan_ip2 route is present in vm3 inet table
        inspect_h = self.agent_inspect[vm3_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm3_vrf_id, ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm2_macvlan_ip.split("/")[0]))
        
        # checking if macvlan_ip2 route is present in vm3 vrouter inet table
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm2_macvlan_ip, vm3_vrf_id)
        output = self.inputs.run_cmd_on_server(vm3_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm2_macvlan_mac_addr, "Stictched mac address is invalid."

        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2")

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_inter_compute_3


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_vlan_4(self):
        '''
        Description: Learn MAC_IPv4 bindings on VLAN sub intf in same VN and same compute with forwarding mode as L2 only mode
        Test steps:
               1. Create macvlan intf on vlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. On vrouter: Verify POD IP is added to inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
		    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm4_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm4_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm4_macvlan_ip))

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm4 pod ip
        inspect_h = self.agent_inspect[self.vm4_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        cmd = ['ip link delete eth0.100',
               'ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        return True
    # end test_intra_vn_intra_compute_vlan_4


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_vlan_4(self):
        '''
        Description:  Learn MAC_IPv4 bindings on VLAN sub intf in same VN and different compute with forwarding mode as L2 only mode
        Test steps:
               1. Create macvlan intf on vlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. On vrouter: Verify POD IP is added to inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm2 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        cmds_vm3 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm3_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd)

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip)

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm3_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm3_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm2 pod ip
        inspect_h = self.agent_inspect[self.vm2_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm3_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm3_macvlan_ip))

        # from vm3 to mac2 intf
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm3 pod ip
        inspect_h = self.agent_inspect[self.vm3_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        cmd = ['ip link delete eth0.100',
               'ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True             
    # end test_intra_vn_inter_compute_vlan_4


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_vlan_l2l3mode_5(self):
        ''' 
        Description: Learn MAC_IPv4 bindings on VLAN sub intf in same vn and same compute with forwarding mode as  L2/L3 mode.
        Test steps:
               1. Create macvlan intf on vlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. L3VPN route for IP1 and IP2
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table
        Maintainer : ybadaya@juniper.net
        '''
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2_l3") 
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm4_macvlan_ip, "Mac route is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if vm4_macvlan_ip is present in vm1 inet table
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # checking if vm4_macvlan_ip is present in vm1 vrouter inet table
        route = self.get_vrouter_route(self.vm4_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm4_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm4_macvlan_ip, vm1_vrf_id)
        output = self.inputs.run_cmd_on_server(vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm4_macvlan_mac_addr, "Stitched mac address is invalid." 

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking inet table for vm6 pod ip
        inspect_h = self.agent_inspect[vm4_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm1_macvlan_ip.split("/")[0]))

        # checking Vrouter inet table for vm6 pod ip
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm1_macvlan_ip, vm4_vrf_id)
        output = self.inputs.run_cmd_on_server(self.vm4_fixture.vm_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm1_macvlan_mac_addr, "Stictched mac address is invalid."

        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2") 

        cmd = ['ip link delete eth0.100',
               'ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True        
    # end test_intra_vn_intra_compute_vlan_l2l3mode_5



    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_vlan_l2l3mode_5(self):
        '''
        Description: Learn MAC_IPv4 bindings on VLAN sub intf in same vn and diff compute with forwarding mode as  L2/L3 mode.
        Test steps:
               1. Create macvlan intf on vlan intf on vm2 and vm3.
        Pass criteria:
               1. Ping from vm to macvlan intf should go through fine.
               2. MAC/IP route should be present in evpn table
               3. derived bridge route with peer as EVPN for MAC1 and MAC2
               4. L3VPN route for IP1 and IP2
               5. On vrouter: Verify stitched mac addr is available
               6. On vrouter: Verify POD IP is added to inet table 
        Maintainer : ybadaya@juniper.net
        '''
        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2_l3")

        cmds_vm2 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        cmds_vm3 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm3_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd)

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip)

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm3_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm3_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan_ip3 is present in vm2 inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm2_vrf_id, ip=self.vm3_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm3_macvlan_ip.split("/")[0]))

        # checking if route for macvlan_ip3 is present in vm2 vrouter inet table
        route = self.get_vrouter_route(self.vm3_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm3_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm3_macvlan_ip, vm2_vrf_id)
        output = self.inputs.run_cmd_on_server(vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm3_macvlan_mac_addr, "Stictched mac address is invalid." 


        # from vm3 to mac2 intf
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan_ip2 route is present in vm3 inet table
        inspect_h = self.agent_inspect[vm3_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm3_vrf_id, ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm2_macvlan_ip.split("/")[0]))
        
        # checking if macvlan_ip2 route is present in vm3 vrouter inet table
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm2_macvlan_ip, vm3_vrf_id)
        output = self.inputs.run_cmd_on_server(vm3_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm2_macvlan_mac_addr, "Stictched mac address is invalid."

        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2")

        cmd = ['ip link delete eth0.100',
               'ip link delete macvlan1']
        self.vm5_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm7_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
        
    # end test_intra_vn_inter_compute_vlan_l2l3mode_5

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_inter_vn_intra_compute_intra_subnet_6(self):
        ''' 
        Description:  Verify Pod IPv4 connectivity on same compute, inter vn, intra subnet
        Test steps:
               1. Create macvlan intf on vm1 and vm3 
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]
        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm3_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)

        # from vm1 to mac3 intf
        assert self.vm1_fixture.ping_to_ip(self.vm3_macvlan_ip)

        # from vm3 to mac1
        assert self.vm3_fixture.ping_to_ip(self.vm1_macvlan_ip)

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_inter_vn_intra_compute_intra_subnet_6

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_inter_subnetvms_6(self):
        '''        
        Description: Verify Pod IPv4 connectivity on same compute, intra vn, inter subnet
        Test steps:
               1. Create a VN and launch 2 VMs in it on same compute, same subnet.
               2. Create macvlan intf on both the VMs.
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        vn1_name = get_random_name("vn1")
        (vm1_name, vm2_name) = (
            get_random_name('vm1'), get_random_name('vm2'))
        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        vn1_subnet_list = [get_random_cidr(), get_random_cidr()]
        vn1_subnets = [{'cidr': vn1_subnet_list[0], },
                       {'cidr': vn1_subnet_list[1], }]
        vm1_name = get_random_name('vn1-vm1')
        vm2_name = get_random_name('vn1-vm2')
        vn1_fixture = self.create_vn(vn1_name, vn1_subnets)

        self.logger.info('Create first VM in the VN')
        vm1_fixture = self.create_vm(vn1_fixture, vm1_name,
                                     image_name='ubuntu-traffic', node_name=vm1_node_name)

        # Create a second VM in second subnet
        port_obj = self.create_port(net_id=vn1_fixture.vn_id,
                       fixed_ips=[{'subnet_id': vn1_fixture.vn_subnet_objs[1]['id']}])
        vm2_fixture = self.create_vm(vn1_fixture, vn1_vm2_name,
                                     image_name='ubuntu-traffic',
                                     port_ids=[port_obj['id']], node_name=vm1_node_name)

        assert vm1_fixture.wait_till_vm_is_up()
        assert vm2_fixture.wait_till_vm_is_up()
        vm1_eth0_ip = self.get_intf_address('eth0',vm1_fixture)
        vm2_eth0_ip = self.get_intf_address('eth0',vm2_fixture)
        macvlan_ip1 = ".".join(vm1_eth0_ip.split(".")[:3]) + "." + str(int(vm1_eth0_ip.split(".")[3])+1) + "/26"
        macvlan_ip2 = ".".join(vm2_eth0_ip.split(".")[:3]) + "." + str(int(vm2_eth0_ip.split(".")[3])+1) + "/26"

        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % macvlan_ip1]
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % macvlan_ip2]
        vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        # from vm1 to mac2
        assert vm1_fixture.ping_to_ip(macvlan_ip2)

        # from vm2 to mac1
        assert vm2_fixture.ping_to_ip(macvlan_ip1)

        return True
    # end test_intra_vn_intra_compute_inter_subnetvms_6

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_inter_vn_inter_compute_7(self):
        '''
        Description:  Verify Pod IPv4 connectivity across computes, inter vn
        Test steps:
               1. Create macvlan intf on vm1 and vm2 
        Pass criteria: Ping between the VM and pod should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        # from vm1 to mac2
        assert self.vm1_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # from vm2 to mac1
        assert self.vm2_fixture.ping_to_ip(self.vm1_macvlan_ip)

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_inter_vn_inter_compute_7


    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_8(self):
        ''' 
        Description:  Verify that routes corresponding to MAC-IP pair are deleted after mac retries of ARP
        Test steps:
               1. Create macvlan intf on vm1 and vm4.
               2. Delete macvlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should not go
               2. MAC route should be deleted in evpn table
               3. Derived bridge route with peer as EVPN is deleted for MAC1 and MAC2
               4. POD IP is deleted from inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan1 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking inet table for vm4 pod ip
        inspect_h = self.agent_inspect[self.vm4_fixture.vm_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' % (self.vm1_macvlan_ip.split("/")[0]))

        return True
    # end test_intra_vn_intra_compute_8

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_HC_11(self):
        ''' 
        Description: Verify that routes corresponding to MAC-IP pairs learnt on VM interface goes down when health check on VM interface is down
        Test steps:
               1. Attach HC on vm1.
               2. Create macvlan intf on vm4.
               3. Detach HC on vm1.
        Pass criteria:
               1. Ping from vm1 to vm4 macvlan intf should not go
               2. MAC route should be deleted in vm1 evpn table
               3. Derived bridge route with peer as EVPN is deleted in vm1
               4. POD IP is deleted from vm1 inet table 
        Maintainer : ybadaya@juniper.net
        '''
        shc_fixture = self.create_hc(hc_type="link-local")
        self.attach_shc_to_vmi(shc_fixture, self.vm1_fixture)

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        
        self.detach_shc_from_vmi(shc_fixture, self.vm1_fixture)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
    # end test_intra_vn_intra_compute_HC_11

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_vlan_12(self):
        '''
        Description:  Verify that routes corresponding to MAC-IP pairs learnt on VM interface goes down when VLAN sub intf is deleted
        Test steps:
               1. Create macvlan intf on vlan intf on vm1 and vm4.
               2. Delete vlan intf on vm1 and vm4.
        Pass criteria:
               1. Ping from vm to macvlan intf should not go
               2. MAC route should be deleted in evpn table
               3. Derived bridge route with peer as EVPN is deleted for MAC1 and MAC2
               4. POD IP is deleted from inet table 
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip,
                    'ip link delete vlan']
        cmds_vm4 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip,
                    'ip link delete vlan']

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert not self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan4 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan1 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking inet table for vm4 pod ip
        inspect_h = self.agent_inspect[self.vm4_fixture.vm_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in vrouter for %s' % (self.vm1_macvlan_ip.split("/")[0]))

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_vlan_12

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_13(self):
        '''
        Description: verify that when IP is moved locally, routes get updated correctly. VN forwarding mode is L2
        Test steps:
               1. launch pod1 with MAC1/IP1 in vm1
               2. destroy pod1 and launch pod2 with MAC2/IP1 in vm4
        Pass criteria: 
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm4 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1 is deleted from vm4 evpn table
                                         Derived bridge route is deleted from vm4
               4. After pod2 is launched: MAC2 is added in vm1 evpn table
					  Derived bridge route is added in vm1
               5. On vrouter: New flow source nh should point to MAC2/IP1
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        mac1_nh_id = self.inputs.run_cmd_on_server(vm4_node_ip, "docker exec -ti vrouter_vrouter-agent_1 flow --match %s| grep -m 2 S\(nh\)| awk {'print $7'}" % self.vm1_macvlan_ip).split(":")[1].split(",")[0] 
        mac1_oif = self.inputs.run_cmd_on_server(vm4_node_ip, "docker exec -ti vrouter_vrouter-agent_1  nh --get %s | grep Oif | awk {'print $2'}" % mac1_nh_id).split(":")[1]

        # checking evpn table
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip))
['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm4 pod ip
        inspect_h = self.agent_inspect[self.vm4_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        vm3_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm1_macvlan_ip)

        vm1_node_ip = self.vm1_fixture.vm_node_ip
        mac2_nh_id = self.inputs.run_cmd_on_server(vm1_node_ip, "docker exec -ti vrouter_vrouter-agent_1 flow --match %s| grep -m 2 S\(nh\)| awk {'print $7'}" % self.vm1_macvlan_ip).split(":")[1].split(",")[0] 
        mac2_oif = self.inputs.run_cmd_on_server(vm1_node_ip, "docker exec -ti vrouter_vrouter-agent_1  nh --get %s | grep Oif | awk {'print $2'}" % mac2_nh_id).split(":")[1]
        assert mac1_oif != mac2_oif , "Oif has not changed."
        encap_data = self.inputs.run_cmd_on_server(vm1_node_ip, "docker exec -ti vrouter_vrouter-agent_1  nh --get %s | grep Encap\ Data" % mac2_nh_id)).split(":")[1][1:18]
        assert vm4_macvlan_mac_addr.replace(":", " ") == encap_data, "Mac2 is not present in encap data."
 
        # checking evpn table if MAC2 is added in vm1
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking MAC1 is deleted from vm4
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn4_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip))
['mac']
        assert not mac, "Mac route for macvlan1 is present in EVPN table. "

        # checking MAC2 is added in vm1 bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking MAC1 is deleted from vm4 bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking Vrouter inet table for vm1 pod ip
        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_intra_vn_intra_compute_13

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_14(self):
        ''' 
        Description: verify that when IP is moved across computes, IP move is detected and old routes are deleted correctly. VN forwarding mode is L2
        Test steps:
               1. launch pod1 with MAC1/IP1 in vm2
               2. destroy pod1 and launch pod2 with MAC2/IP1 in vm3
        Pass criteria: 
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm3 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1 is deleted from vm3 evpn table
                                         Derived bridge route is deleted from vm3
               4. After pod2 is launched: MAC2 is added in vm2 evpn table
                                          Derived bridge route is added in vm2
               5. On vrouter: flow is deleted on vm3 and added on vm2
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)

        # from vm3 to mac2 intf
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)
        flow = self.inputs.run_cmd_on_server(vm3_node_ip, "docker exec -ti vrouter_vrouter-agent_1 flow --match %s | grep %s | grep -v \"Listing\"" % (self.vm2_macvlan_ip, self.vm2_macvlan_ip)) 
        assert flow, "Flow not created."

        # checking evpn table
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking Vrouter inet table for vm3 pod ip
        inspect_h = self.agent_inspect[self.vm3_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        cmds_vm3 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd) 

        # from vm2 to mac3 intf
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        assert self.vm2_fixture.ping_to_ip(self.vm3_macvlan_ip)
        flow = self.inputs.run_cmd_on_server(vm2_node_ip, "docker exec -ti vrouter_vrouter-agent_1 flow --match %s | grep %s | grep -v \"Listing\"" % (self.vm2_macvlan_ip, self.vm2_macvlan_ip)) 
        assert flow, "Flow not created."

        # checking if flow got deleted in vm3
        flow = self.inputs.run_cmd_on_server(vm3_node_ip, "docker exec -ti vrouter_vrouter-agent_1 flow --match %s | grep %s | grep -v \"Listing\"" % (self.vm2_macvlan_ip, self.vm2_macvlan_ip)) 
        assert not flow, "Flow still exists."

        # checking evpn table
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm3_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm3_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking if route in vm3 evpn table is deleted
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert not mac, "Mac1 route is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route in vm3 bridge table is deleted
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking Vrouter inet table for vm2 pod ip
        inspect_h = self.agent_inspect[self.vm2_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        # checking Vrouter inet table if vm3 pod ip is deleted
        inspect_h = self.agent_inspect[self.vm3_fixture.vm_node_ip]
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert not route, ('Route seen in vrouter for %s' % (self.vm2_macvlan_ip))
        return True        
    # end test_intra_vn_inter_compute_14

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_l2l3mode_15(self):
        ''' 
        Description: verify that when IP is moved locally, routes get updated correctly. VN forwarding mode is L2/L3.
        Test steps:
               1. launch pod1 with MAC1/IP1 in vm1
               2. destroy pod1 and launch pod2 with MAC2/IP1 in vm4
        Pass criteria: 
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm4 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1/IP1 is deleted from vm4 evpn table
                                         Derived bridge route is deleted from vm4
               4. After pod2 is launched: MAC2/IP1 is added in vm1 evpn table
                                          Derived bridge route is added in vm1
                                          inet route is updated
                                          inet route stitched mac is updated to MAC2
                                          inet route mpls label and nh is changed
               5. On vrouter: Ip is added from to vm1 inet table and deleted from vm4 inet table
        Maintainer : ybadaya@juniper.net
        '''
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2_l3")
        cmds_vm1 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm1_macvlan_mac_addr = self.vm1_fixture.run_cmd_on_vm(mac_cmd)

        # from vm4 to mac1 intf
        assert self.vm4_fixture.ping_to_ip(self.vm1_macvlan_ip)

        # checking evpn table
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm1_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan_ip1 is present in vm4 inet table 
        inspect_h = self.agent_inspect[vm4_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm1_macvlan_ip.split("/")[0]))
        vm4_mpls_label = route['label']
        vm4_inet_nh_id = route['path_list'][0]['nh']['nh_index']       

        # checking if macvlan_ip1 is present in vm4 vrouter inet table
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm1_macvlan_ip, vm4_vrf_id)
        output = self.inputs.run_cmd_on_server(vm4_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm1_macvlan_mac_addr, "Stictched mac address is invalid."

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm1_macvlan_ip]

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm1_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "
     
        # checking if MAC got deleted from vm4 evpn table
        mac = self.agent_inspect[vm4_node_ip].get_vna_evpn_route(vm4_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm1_macvlan_mac_addr, ip=self.vm1_macvlan_ip)['mac']
        assert not mac, "Mac route present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm1_node_ip].get_vna_layer2_route(vm1_vrf_id, mac=vm4_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if MAC is deleted in vm4 bridge table
        peer = self.agent_inspect[vm4_node_ip].get_vna_layer2_route(vm4_vrf_id, mac=vm1_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking if macvlan4 route is there in inet table for vm1
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm1_macvlan_ip.split("/")[0]))
        assert vm4_mpls_label != route['label'], "Mpls label has not changed."
        assert vm4_inet_nh_id != route['path_list'][0]['nh']['nh_index'], "Nh has not changed." 

        # checking if macvlan4 route is present in vm1 Vrouter inet table
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        # checking vm4 inet table route for macvlan1 is deleted
        inspect_h = self.agent_inspect[vm4_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=self.vm1_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in inet table for %s' % (self.vm1_macvlan_ip.split("/")[0]))

        # checking vm4 Vrouter inet table route for macvlan1 is deleted
        route = self.get_vrouter_route(self.vm1_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert not route, ('Route seen in vrouter for %s' % (self.vm1_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm1_macvlan_ip, vm1_vrf_id)
        output = self.inputs.run_cmd_on_server(vm1_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm4_macvlan_mac_addr, "Stictched mac address is invalid." 

        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2")
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True        
    # end test_intra_vn_intra_compute_15

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_inter_compute_vlan_l2l3mode_16(self):
        ''' 
        Description: verify that when IP is moved across computes, IP move is detected and old routes are deleted correctly.vn forwarding mode is L2/L3
        Test steps:
               1. launch pod1 with MAC1/IP1 in vm2
               2. destroy pod1 and launch pod2 with MAC2/IP1 in vm3
        Pass criteria: 
               1. verify routes corresponding to MAC1/IP1 pair when pod1 is launched
               2. ping from vm3 to pod1 should go through fine when pod1 is launched
               3. After pod1 is deleted: MAC1/IP1 is deleted from vm3 evpn table
                                         Derived bridge route is deleted from vm3
               4. After pod2 is launched: MAC2/IP1 is added in vm2 evpn table
                                          Derived bridge route is added in vm2
                                          inet route is updated
                                          inet route stitched mac is updated to MAC2
                                          inet route mpls label is changed
             			          inet route nh is changed to tunnel nh	 
               5. On vrouter: Ip is added from to vm2 inet table and deleted from vm3 inet table
        Pass criteria: Ping between the VMs should go thru fine.
        Maintainer : ybadaya@juniper.net
        '''
        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2_l3")
        cmds_vm2 = ['ip link add macvlan1 link eth0 type macvlan',,
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        self.vm2_fixture.run_cmd_on_vm(cmds_vm2, as_sudo=True)

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm2_macvlan_mac_addr = self.vm2_fixture.run_cmd_on_vm(mac_cmd)

        # from vm3 to mac2 intf
        assert self.vm3_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm3_node_ip = self.vm3_fixture.vm_node_ip
        vm3_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm3_fixture)
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm2_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if macvlan2 is present in vm3 inet table
        inspect_h = self.agent_inspect[vm3_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm3_vrf_id, ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm2_macvlan_ip.split("/")[0]))
        vm3_mpls_label = route['label']

        # checking if macvlan2 is present in vm3 Vrouter inet table
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm2_macvlan_ip, vm3_vrf_id)
        output = self.inputs.run_cmd_on_server(vm3_node_ip, stitched_mac_cmd).split("(")[0]

        cmd = ['ip link delete macvlan1']
        self.vm2_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        cmds_vm3 = ['ip link add link eth0 name eth0.100 type vlan id 100',
                    'ip link add macvlan1 link eth0.100 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm2_macvlan_ip]

        self.vm3_fixture.run_cmd_on_vm(cmds_vm3, as_sudo=True)
        vm3_macvlan_mac_addr = self.vm3_fixture.run_cmd_on_vm(mac_cmd)

        # from vm2 to mac3 intf
        assert self.vm2_fixture.ping_to_ip(self.vm2_macvlan_ip)

        # checking evpn table
        vm2_node_ip = self.vm2_fixture.vm_node_ip
        vm2_vrf_id = self.get_vrf_id(self.vn2_fixture, self.vm2_fixture)
        mac = self.agent_inspect[vm2_node_ip].get_vna_evpn_route(vm2_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm3_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert mac == str(self.vn2_vxlan_id)+"-"+vm3_macvlan_mac_addr+"-"+self.vm2_macvlan_ip, "Mac route for macvlan1 is absent in EVPN table. "

        # checking if route for macvlan2 is deleted from vm3 evpn table
        mac = self.agent_inspect[vm3_node_ip].get_vna_evpn_route(vm3_vrf_id, vxlanid=self.vn2_vxlan_id , mac=vm2_macvlan_mac_addr, ip=self.vm2_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan5 is present in EVPN table. "

        # checking bridge table
        peer = self.agent_inspect[vm2_node_ip].get_vna_layer2_route(vm2_vrf_id, mac=vm3_macvlan_mac_addr)['peer']
        assert peer == "EVPN", "Peer is not EVPN."

        # checking if route for macvlan2 is deleted from vm3 bridge table
        peer = self.agent_inspect[vm3_node_ip].get_vna_layer2_route(vm3_vrf_id, mac=vm2_macvlan_mac_addr)['peer']
        assert not peer, "Peer is EVPN."

        # checking if route for macvlan3 is present in vm2 inet table
        inspect_h = self.agent_inspect[vm2_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm2_vrf_id, ip=self.vm2_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm2_macvlan_ip.split("/")[0]))
        assert vm3_mpls_label != route['label'], "Mpls label has not changed."
        assert route['path_list'][0]['nh']['type'] == 'tunnel', "Nh type is not tunnel."

        # checking if route for macvlan3 is present vm2 Vrouter inet table
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        # checking if route macvlan2 is deleted in vm3 inet table route
        inspect_h = self.agent_inspect[vm3_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm3_vrf_id, ip=self.vm2_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in inet table for %s' % (self.vm2_macvlan_ip.split("/")[0]))

        # checking if route for macvlan2 is deleted in vm3 vrouter inet table
        route = self.get_vrouter_route(self.vm2_macvlan_ip,
                                       vn_fixture=self.vn2_fixture,
                                       inspect_h=inspect_h)
        assert not route, ('Route seen in vrouter for %s' % (self.vm2_macvlan_ip))

        # checking stitched MAC addr
        stitched_mac_cmd = 'docker exec -ti vrouter_vrouter-agent_1 rt --get %s --vrf %d | awk \'{print $6}\'| grep \':\'' % (self.vm2_macvlan_ip, vm2_vrf_id)
        output = self.inputs.run_cmd_on_server(vm2_node_ip, stitched_mac_cmd).split("(")[0]
        assert output == vm3_macvlan_mac_addr, "Stictched mac address is invalid."

        self.vn2_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn2_name, forwarding_mode = "l2")
        self.vm3_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
        
    # end test_intra_vn_inter_compute_vlan_l2l3mode_16

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
    @preposttest_wrapper
    def test_intra_vn_intra_compute_19(self):
        '''
        Description: dynamically change forwarding mode VN  and verify that routes are added/deleted/updated accordingly for MAC-IP pair
        Test steps:
               1. launch pod1 on vm4 and change fwd mode from l2 to l2_l3
               2. Change fwd mode to l2 
        Pass criteria:
               1. When changed from l2 to l2_l3: vm4 macvlan ip is added to vm1 inet table
                                                 MAC/IP route added to evpn table
               2. When changed from l2_l3 to l2: vm4 macvlan ip is deleted from vm1 inet table
  						 MAC/IP route deleted from evpn table
               3. On vrouter: flags are updated in vif --list
                              pod ip is added to inet table  
        Maintainer : ybadaya@juniper.net
        '''
        cmds_vm4 = ['ip link add macvlan1 link eth0 type macvlan',
                    'ip link set dev macvlan1 up',
                    'ip addr add %s dev macvlan1' % self.vm4_macvlan_ip]

        self.vm4_fixture.run_cmd_on_vm(cmds_vm4, as_sudo=True)
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2_l3")

        mac_cmd = ['ifconfig macvlan1 | grep HWaddr | awk \'{ print $5 }\'']
        vm4_macvlan_mac_addr = self.vm4_fixture.run_cmd_on_vm(mac_cmd)

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert mac == str(self.vn1_vxlan_id)+"-"+vm4_macvlan_mac_addr+"-"+self.vm4_macvlan_ip, "Mac route for macvlan4 is absent in EVPN table. "

        # checking if route macvlan4 is in vm1 inet table route
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert route, ('No route seen in inet table for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # checking flag from vif --list
        vif_id = self.agent_inspect[ self.inputs.host_data[self.inputs.compute_ips[0]]['name'] ].get_vna_intf_details(self.vm1_fixture.get_tap_intf_of_vm()[0]['name'])[0]['index']
        flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" %(vif_id)
        flag = self.inputs.run_cmd_on_server(vm3_node_ip, flag_cmd).split(":")[1] 
        assert ("L2" in flag ) and ("L3" in flag), "L3L2 mode is not enabled."
 
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2")

        # from vm1 to mac4 intf
        assert self.vm1_fixture.ping_to_ip(self.vm4_macvlan_ip)

        # checking evpn table
        vm1_node_ip = self.vm1_fixture.vm_node_ip
        vm1_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm1_fixture)
        mac = self.agent_inspect[vm1_node_ip].get_vna_evpn_route(vm1_vrf_id, vxlanid=self.vn1_vxlan_id , mac=vm4_macvlan_mac_addr, ip=self.vm4_macvlan_ip)['mac']
        assert not mac, "Mac route for macvlan4 is not deleted in EVPN table. "

        # checking if route macvlan4 is in vm1 inet table route
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = inspect_h.get_vna_route(vrf_id= vm1_vrf_id, ip=self.vm4_macvlan_ip.split("/")[0])
        assert not route, ('Route seen in inet table for %s' % (self.vm4_macvlan_ip.split("/")[0]))

        # checking for macvlan4 ip in vm1 Vrouter inet table 
        inspect_h = self.agent_inspect[vm1_node_ip]
        route = self.get_vrouter_route(self.vm4_macvlan_ip,
                                       vn_fixture=self.vn1_fixture,
                                       inspect_h=inspect_h)
        assert route, ('No route seen in vrouter for %s' % (self.vm4_macvlan_ip))

        # checking flag from vif --list
        vif_id = self.agent_inspect[ self.inputs.host_data[self.inputs.compute_ips[0]]['name'] ].get_vna_intf_details(self.vm1_fixture.get_tap_intf_of_vm()[0]['name'])[0]['index']
        flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" %(vif_id)
        flag = self.inputs.run_cmd_on_server(vm3_node_ip, flag_cmd).split(":")[1] 
        assert "L2" in flag , "L2 mode is not enabled."

        cmd = ['ip link delete macvlan1']
        self.vm4_fixture.run_cmd_on_vm(cmd, as_sudo=True)

        return True
    # end test_intra_vn_intra_compute_19

    @test.attr(type=['suite1', 'upgrade','vrouter_gw', 'vcenter_compute', 'ci_contrail_go_kolla_ocata_sanity'])
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
        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2_l3")

        for i in range(1,51):        
            cmds_vm1 = ['ip link add macvlan%s link eth0 type macvlan' % i,
                        'ip link set dev macvlan%s up' % i,
                        'ip addr add %s/26 dev macvlan%s' % (".".join(self.vm1_eth0_ip.split(".")[:3]) + "." + str(int(self.vm1_eth0_ip.split(".")[3])+i), i)]

            self.vm1_fixture.run_cmd_on_vm(cmds_vm1, as_sudo=True)

        # checking inet table for vm6 pod ip
        vm4_node_ip = self.vm4_fixture.vm_node_ip
        vm4_vrf_id = self.get_vrf_id(self.vn1_fixture, self.vm4_fixture)
        inspect_h = self.agent_inspect[vm4_node_ip]
        for i in range(1,51):
            macvlan_ip = ".".join(self.vm1_eth0_ip.split(".")[:3]) + "." + str(int(self.vm1_eth0_ip.split(".")[3])+i)
            assert self.vm4_fixture.ping_to_ip(macvlan_ip)
            route = inspect_h.get_vna_route(vrf_id= vm4_vrf_id, ip=macvlan_ip)
            assert route, ('No route seen in inet table for %s' % (macvlan_ip))

        self.vn1_fixture.add_forwarding_mode(project_fq_name=self.inputs.project_fq_name, vn_name=self.vn1_name, forwarding_mode = "l2") 

        cmd = ['ip link delete macvlan1']
        self.vm1_fixture.run_cmd_on_vm(cmd, as_sudo=True)
        return True
    # end test_fifty_macvlans

