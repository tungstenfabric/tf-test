from __future__ import absolute_import, unicode_literals
from serial_scripts.md5.base import Md5Base
from tcutils.traffic_utils.hping_traffic import Hping3
from common.gw_less_fwd.base import *
from common.dsnat.base import BaseDSNAT
from common.intf_mirroring.verify import VerifyIntfMirror
from scripts.intf_mirror.base import BaseIntfMirrorTest
from tcutils.tcpdump_utils import *
from tcutils.util import *
from common.neutron.base import BaseNeutronTest
from common.bgpaas.base import BaseBGPaaS
from common.openstack_libs import nova_client as mynovaclient
from common.device_connection import NetconfConnection
from compute_node_test import ComputeNodeFixture
from tcutils.cores import get_service_crashes
from common.l3_mh.base import BaseL3Multihoming
from tcutils.contrail_status_check import ContrailStatusChecker
from traffic.core.profile import create, ContinuousProfile
from vnc_api.vnc_api import *
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
import random
from tcutils.wrappers import preposttest_wrapper
sys.path.append(os.path.realpath('tcutils/pkgs/Traffic'))


class TestSerialL3MultihomingFeatures(
        BaseL3Multihoming, BaseIntfMirrorTest, VerifyIntfMirror, GWLessFWDTestBase, BaseDSNAT, Md5Base, BaseBGPaaS):
    @classmethod
    def setUpClass(cls):
        super(TestSerialL3MultihomingFeatures, cls).setUpClass()
        cls.l3mh_setup_check_done = False

    @classmethod
    def tearDownClass(cls):
        super(TestSerialL3MultihomingFeatures, cls).tearDownClass()

    def setUp(self):
        super(TestSerialL3MultihomingFeatures, self).setUp()
        if TestSerialL3MultihomingFeatures.l3mh_setup_check_done:
            return
        if not self.inputs.inputs.l3mh_cidr:
            return (
                False, 'This script runs on l3mh setup only, and you need to provide a L3MH_CIDR knob in yaml file')
        dpdk_found = False
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    dpdk_found = True
        assert dpdk_found, 'This script needs atleadt 1 dpdk node to work, no dpdk found'
        TestSerialL3MultihomingFeatures.l3mh_setup_check_done = True

    def spawn_dpdk_flavors(self):
        self.obj1 = mynovaclient.Client(
            '2', session=self.nova_h.auth_h.get_session(
                scope='project'), region_name='regionOne')
        self.obj1.flavors.create(name='cirros_dpdk', vcpus=1, ram=1024, disk=10)
        self.obj1.flavors.create(
            name='ubuntu_traffic_dpdk',
            vcpus=1,
            ram=1024,
            disk=10)
        self.obj1.flavors.create(
            name='bgpaas_dpdk', vcpus=2, ram=2048, disk=40)
        for fl_list in ['cirros_dpdk', 'ubuntu_traffic_dpdk', 'bgpaas_dpdk']:
            flavor = self.obj1.flavors.find(name=fl_list)
            flavor.set_keys({'hw:mem_page_size': 'large'})
        self.addCleanup(self.delete_flavors)

    def delete_flavors(self):
        flavor_list = self.orch.get_flavor_list()
        for flavor in flavor_list:
            if 'dpdk' in flavor.name:
                self.obj1.flavors.delete(flavor)

    def configure_spine_leaf(self):

        for i in range(len(list(self.inputs.l3mh_routers_data.values()))):
            router_params = list(self.inputs.l3mh_routers_data.values())[i]
            cmd = []
            if router_params['role'] == 'spine':
                cmd.append('set system services ssh root-login allow')
                cmd.append('set system services telnet')
                cmd.append('set system services netconf ssh')
                cmd.append('set interfaces et-0/0/23 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces et-0/0/23 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway2')
                cmd.append('set interfaces xe-0/0/35:0 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces xe-0/0/35:0 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway1')
                cmd.append('set interfaces xe-0/0/35:1 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/35:1 unit 0 family ethernet-switching vlan members vlan-l3mh-controller')
                cmd.append('set interfaces irb unit 2000 family inet address 20.1.1.100/24')
                cmd.append('set interfaces irb unit 3000 family inet address 30.1.1.100/24')
                cmd.append('set interfaces irb unit 3211 family inet address 10.1.1.100/24')
                cmd.append('set interfaces lo0 unit 0 family inet address 100.100.1.1/32')
                cmd.append('set routing-options static route 10.209.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 10.206.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 10.212.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 192.168.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 172.17.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 17.27.0.0/16 next-hop 10.204.219.254')
                cmd.append('set routing-options static route 100.100.1.3/32 next-hop 10.1.1.1')
                cmd.append('set routing-options static route 100.100.1.4/32 next-hop 20.1.1.1')
                cmd.append('set routing-options static route 77.77.1.100/32 next-hop 10.204.216.245')
                cmd.append('set routing-options static route 0.0.0.0/0 next-hop 10.204.216.245')
                cmd.append('set routing-options router-id 100.100.1.1')
                cmd.append('set routing-options autonomous-system 64512')
                cmd.append('set protocols bgp group reflector-peers type internal')
                cmd.append('set protocols bgp group reflector-peers family inet unicast')
                cmd.append('set protocols bgp group reflector-peers family inet6 unicast')
                cmd.append('set protocols bgp group reflector-peers family inet6-vpn unicast')
                cmd.append('set protocols bgp group reflector-peers export send-direct')
                cmd.append('set protocols bgp group reflector-peers cluster 100.100.1.1')
                cmd.append('set protocols bgp group reflector-peers multipath')
                cmd.append('set protocols bgp group reflector-peers neighbor 100.100.1.3 family inet unicast add-path receive')
                cmd.append('set protocols bgp group reflector-peers neighbor 100.100.1.3 family inet unicast add-path send path-count 2')
                cmd.append('set protocols bgp group reflector-peers neighbor 100.100.1.4 family inet unicast add-path receive')
                cmd.append('set protocols bgp group reflector-peers neighbor 100.100.1.4 family inet unicast add-path send path-count 2')
                cmd.append('set protocols bgp group reflector-peers neighbor %s family inet unicast' % self.inputs.bgp_control_ips[0])
                cmd.append('set protocols bgp group reflector-peers neighbor %s family inet-vpn unicast' % self.inputs.bgp_control_ips[0])
                cmd.append('set protocols bgp group reflector-peers neighbor %s family inet6 unicast' % self.inputs.bgp_control_ips[0])
                cmd.append('set protocols bgp group reflector-peers neighbor %s family route-target' % self.inputs.bgp_control_ips[0])
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol direct')
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol local')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface lo0.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface irb.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 then accept')
                cmd.append('set policy-options policy-statement export-bgp term 2 then reject')
                cmd.append('set policy-options policy-statement send-direct term 2 from protocol direct')
                cmd.append('set policy-options policy-statement send-direct term 2 then accept')
                cmd.append('set vlans vlan-l3mh-controller vlan-id 3000')
                cmd.append('set vlans vlan-l3mh-controller l3-interface irb.3000')
                cmd.append('set vlans vlan-l3mh-gateway1 vlan-id 3211')
                cmd.append('set vlans vlan-l3mh-gateway1 l3-interface irb.3211')
                cmd.append('set vlans vlan-l3mh-gateway2 vlan-id 2000')
                cmd.append('set vlans vlan-l3mh-gateway2 l3-interface irb.2000')

            if router_params['role'] == 'leaf1':
                cmd.append('set system services ssh root-login allow')
                cmd.append('set system services netconf ssh')
                cmd.append('set chassis aggregated-devices ethernet device-count 30')
                cmd.append('set interfaces xe-0/0/5 ether-options 802.3ad ae0')
                cmd.append('set interfaces xe-0/0/10 ether-options 802.3ad ae1')
                cmd.append('set interfaces xe-0/0/12 unit 0 enable')
                cmd.append('set interfaces xe-0/0/12 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/12 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway1')
                cmd.append('set interfaces xe-0/0/12 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces ge-0/0/13 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/13 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/13 ether-options 802.3ad ae2')
                cmd.append('set interfaces ge-0/0/14 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/14 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/14 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/14 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway1')
                cmd.append('set interfaces xe-0/0/14 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces ge-0/0/15 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/15 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/15 ether-options 802.3ad ae3')
                cmd.append('set interfaces ge-0/0/16 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/16 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/16 unit 0 family inet address 50.1.1.2/24')
                cmd.append('set interfaces ge-0/0/24 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/24 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/24 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces xe-0/0/24 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces xe-0/0/24 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway1')
                cmd.append('set interfaces xe-0/0/24 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces ge-0/0/25 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/25 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/25 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/25 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway1')
                cmd.append('set interfaces xe-0/0/25 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces ge-0/0/34 native-vlan-id 760')
                cmd.append('set interfaces ge-0/0/34 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ge-0/0/34 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/34 unit 0 family ethernet-switching vlan members ffu-rhosp-tenant')
                cmd.append('set interfaces xe-0/0/34 ether-options 802.3ad ae10')
                cmd.append('set interfaces ge-0/0/35 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/35 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/35 ether-options 802.3ad ae10')
                cmd.append('set interfaces ge-0/0/37 native-vlan-id 760')
                cmd.append('set interfaces ge-0/0/37 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ge-0/0/37 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/37 unit 0 family ethernet-switching vlan members ffu-rhosp-tenant')
                cmd.append('set interfaces xe-0/0/37 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces xe-0/0/37 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces ge-0/0/43 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/43 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/43 unit 0 family inet address 4.4.4.2/24')
                cmd.append('set interfaces ge-0/0/44 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/44 ether-options 802.3ad ae0')
                cmd.append('set interfaces ge-0/0/45 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/45 enable')
                cmd.append('set interfaces xe-0/0/45 ether-options 802.3ad ae1')
                cmd.append('set interfaces ge-0/0/46 unit 0 family ethernet-switching')
                cmd.append('set interfaces xe-0/0/46 ether-options 802.3ad ae2')
                cmd.append('set interfaces ge-0/0/47 unit 0 family ethernet-switching vlan members default')
                cmd.append('set interfaces ge-0/0/47 unit 0 family ethernet-switching storm-control default')
                cmd.append('set interfaces xe-0/0/47 ether-options 802.3ad ae3')
                cmd.append('set interfaces ae1 native-vlan-id 760')
                cmd.append('set interfaces ae1 mtu 9216')
                cmd.append('set interfaces ae1 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae1 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ae1 unit 0 family ethernet-switching vlan members ffu-rhosp-tenant')
                cmd.append('set interfaces ae2 native-vlan-id 760')
                cmd.append('set interfaces ae2 mtu 9216')
                cmd.append('set interfaces ae2 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae2 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ae2 unit 0 family ethernet-switching vlan members ffu-rhosp-tenant')
                cmd.append('set interfaces ae3 native-vlan-id 760')
                cmd.append('set interfaces ae3 mtu 9216')
                cmd.append('set interfaces ae3 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae3 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ae3 unit 0 family ethernet-switching vlan members ffu-rhosp-tenant')
                cmd.append('set interfaces ae10 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae10 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces ae10 unit 0 family ethernet-switching vlan members nfs-vlan')
                cmd.append('set interfaces irb unit 3211 family inet address 10.1.1.1/24')
                cmd.append('set interfaces lo0 unit 0 family inet address 100.100.1.3/32')
                cmd.append('set policy-options policy-statement EXP-FILTER term STAT from protocol static')
                cmd.append('set policy-options policy-statement EXP-FILTER term STAT then accept')
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol direct')
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol local')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface lo0.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface irb.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 then accept')
                cmd.append('set policy-options policy-statement export-bgp term 2 then reject')
                cmd.append('set policy-options policy-statement send-direct term 2 from protocol direct')
                cmd.append('set policy-options policy-statement send-direct term 2 then accept')
                cmd.append('set routing-options static route 0.0.0.0/0 next-hop 10.204.217.254')
                cmd.append('set routing-options static route 192.168.1.0/29 next-hop 50.1.1.1')
                cmd.append('set routing-options static route 100.100.1.1/32 next-hop 10.1.1.100')
                cmd.append('set routing-options static route 108.1.1.5/32 next-hop 10.1.1.50')
                cmd.append('set routing-options static route 108.1.1.6/32 next-hop 10.1.1.60')
                cmd.append('set routing-options router-id 100.100.1.3')
                cmd.append('set routing-options autonomous-system 64512')
                cmd.append('set protocols bgp multipath')
                cmd.append('set protocols bgp group route-reflector type internal')
                cmd.append('set protocols bgp group route-reflector local-address 100.100.1.3')
                cmd.append('set protocols bgp group route-reflector export send-direct')
                cmd.append('set protocols bgp group route-reflector export EXP-FILTER')
                cmd.append('set protocols bgp group route-reflector multipath')
                cmd.append('set protocols bgp group route-reflector neighbor 100.100.1.1 family inet unicast add-path receive')
                cmd.append('set protocols bgp group route-reflector neighbor 100.100.1.1 family inet unicast add-path send path-count 2')
                cmd.append('set protocols ospf area 0.0.0.0 interface all')
                cmd.append('set protocols ospf area 0.0.0.0 interface em0.0 disable')
                cmd.append('set protocols ospf area 0.0.0.0 interface xe-0/0/43.0 disable')
                cmd.append('set vlans default vlan-id 1')
                cmd.append('set vlans default l3-interface irb.0')
                cmd.append('set vlans ffu-rhosp-tenant vlan-id 760')
                cmd.append('set vlans nfs-vlan vlan-id 1111')
                cmd.append('set vlans vlan-l3mh-gateway1 vlan-id 3211')
                cmd.append('set vlans vlan-l3mh-gateway1 l3-interface irb.3211')

            if router_params['role'] == 'leaf2':
                cmd.append('set system services ssh root-login allow')
                cmd.append('set system services netconf ssh')
                cmd.append('set chassis aggregated-devices ethernet device-count 6')
                cmd.append('set interfaces et-0/0/0 mtu 9216')
                cmd.append('set interfaces et-0/0/0 unit 0 family inet address 172.16.254.18/30')
                cmd.append('set interfaces et-0/0/1 mtu 9216')
                cmd.append('set interfaces et-0/0/1 unit 0 family inet address 172.16.254.10/30')
                cmd.append('set interfaces et-0/0/2 mtu 9216')
                cmd.append('set interfaces et-0/0/2 unit 0 family inet address 172.16.254.2/30')
                cmd.append('set interfaces xe-0/0/8:0 mtu 9216')
                cmd.append('set interfaces xe-0/0/8:0 unit 0 family inet address 172.16.254.26/30')
                cmd.append('set interfaces et-0/0/15 unit 0 family inet address 11.11.11.202/24')
                cmd.append('set interfaces et-0/0/23 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces et-0/0/23 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway2')
                cmd.append('set interfaces xe-0/0/28:3 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/28:3 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway2')
                cmd.append('set interfaces xe-0/0/29:0 enable')
                cmd.append('set interfaces xe-0/0/29:1 enable')
                cmd.append('set interfaces xe-0/0/30:2 unit 0 family inet address 192.168.1.202/24')
                cmd.append('set interfaces xe-0/0/31:0 enable')
                cmd.append('set interfaces xe-0/0/31:0 ether-options 802.3ad ae2')
                cmd.append('set interfaces xe-0/0/31:1 enable')
                cmd.append('set interfaces xe-0/0/31:1 ether-options 802.3ad ae2')
                cmd.append('set interfaces xe-0/0/31:2 enable')
                cmd.append('set interfaces xe-0/0/31:2 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/31:2 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces xe-0/0/31:3 enable')
                cmd.append('set interfaces xe-0/0/32:0 enable')
                cmd.append('set interfaces xe-0/0/32:0 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/32:0 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway2')
                cmd.append('set interfaces xe-0/0/32:2 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces xe-0/0/32:2 unit 0 family ethernet-switching vlan members vlan-l3mh-gateway2')
                cmd.append('set interfaces et-0/0/35 unit 0 family inet address 10.10.10.202/24')
                cmd.append('set interfaces ae0 enable')
                cmd.append('set interfaces ae0 mtu 9100')
                cmd.append('set interfaces ae0 aggregated-ether-options link-speed 10g')
                cmd.append('set interfaces ae0 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae0 aggregated-ether-options lacp periodic slow')
                cmd.append('set interfaces ae0 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ae0 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces ae1 enable')
                cmd.append('set interfaces ae1 mtu 9100')
                cmd.append('set interfaces ae1 aggregated-ether-options link-speed 10g')
                cmd.append('set interfaces ae1 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae1 aggregated-ether-options lacp periodic slow')
                cmd.append('set interfaces ae1 unit 0 family ethernet-switching interface-mode trunk')
                cmd.append('set interfaces ae1 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces ae2 enable')
                cmd.append('set interfaces ae2 mtu 9100')
                cmd.append('set interfaces ae2 aggregated-ether-options link-speed 10g')
                cmd.append('set interfaces ae2 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae2 aggregated-ether-options lacp periodic slow')
                cmd.append('set interfaces ae2 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces ae2 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces ae3 enable')
                cmd.append('set interfaces ae3 mtu 9100')
                cmd.append('set interfaces ae3 aggregated-ether-options link-speed 10g')
                cmd.append('set interfaces ae3 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae3 aggregated-ether-options lacp periodic slow')
                cmd.append('set interfaces ae3 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces ae3 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces ae4 enable')
                cmd.append('set interfaces ae4 mtu 9100')
                cmd.append('set interfaces ae4 aggregated-ether-options link-speed 10g')
                cmd.append('set interfaces ae4 aggregated-ether-options lacp active')
                cmd.append('set interfaces ae4 aggregated-ether-options lacp periodic slow')
                cmd.append('set interfaces ae4 unit 0 family ethernet-switching interface-mode access')
                cmd.append('set interfaces ae4 unit 0 family ethernet-switching vlan members rhosp_dev_1716')
                cmd.append('set interfaces em0 unit 0 family inet address 10.204.216.202/24')
                cmd.append('set interfaces irb unit 10 family inet')
                cmd.append('set interfaces irb unit 2000 family inet address 20.1.1.1/24')
                cmd.append('set interfaces lo0 unit 0 family inet address 172.16.255.4/32')
                cmd.append('set interfaces lo0 unit 0 family inet address 100.100.1.4/32')
                cmd.append('set routing-options static route 192.168.1.0/24 next-hop 172.16.254.25')
                cmd.append('set routing-options static route 0.0.0.0/0 next-hop 10.204.216.254')
                cmd.append('set routing-options static route 172.16.255.156/32 next-hop 192.168.1.156')
                cmd.append('set routing-options static route 100.100.1.1/32 next-hop 20.1.1.100')
                cmd.append('set routing-options static route 108.1.1.6/32 next-hop 20.1.1.60')
                cmd.append('set routing-options static route 108.1.1.5/32 next-hop 20.1.1.50')
                cmd.append('set routing-options router-id 100.100.1.4')
                cmd.append('set routing-options autonomous-system 64512')
                cmd.append('set protocols bgp multipath')
                cmd.append('set protocols bgp group IPFAB-UNDER type external')
                cmd.append('set protocols bgp group IPFAB-UNDER mtu-discovery')
                cmd.append('set protocols bgp group IPFAB-UNDER export BGP-IPFAB-UNDER-EXP')
                cmd.append('set protocols bgp group IPFAB-UNDER local-as 65201')
                cmd.append('set protocols bgp group IPFAB-UNDER multipath multiple-as')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.1 description jio-leaf1')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.1 peer-as 65001')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.9 description jio-leaf2')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.9 peer-as 65002')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.17 description jio-leaf3')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.17 peer-as 65003')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.25 description jio-vmx1')
                cmd.append('set protocols bgp group IPFAB-UNDER neighbor 172.16.254.25 peer-as 65203')
                cmd.append('set protocols bgp group route-reflector type internal')
                cmd.append('set protocols bgp group route-reflector local-address 100.100.1.4')
                cmd.append('set protocols bgp group route-reflector export send-direct')
                cmd.append('set protocols bgp group route-reflector export EXP-FILTER')
                cmd.append('set protocols bgp group route-reflector multipath')
                cmd.append('set protocols bgp group route-reflector neighbor 100.100.1.1 family inet unicast add-path receive')
                cmd.append('set protocols bgp group route-reflector neighbor 100.100.1.1 family inet unicast add-path send path-count 2')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term LOOPBACK from protocol direct')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term LOOPBACK from interface lo0.0')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term LOOPBACK then community set IPFAB-LEAF')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term LOOPBACK then accept')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term SERVERS from protocol direct')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term SERVERS from interface irb.10')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term SERVERS then community set IPFAB-LEAF')
                cmd.append('set policy-options policy-statement BGP-IPFAB-UNDER-EXP term SERVERS then accept')
                cmd.append('set policy-options policy-statement EXP-FILTER term STAT from protocol static')
                cmd.append('set policy-options policy-statement EXP-FILTER term STAT then accept')
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol direct')
                cmd.append('set policy-options policy-statement export-bgp term 1 from protocol local')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface lo0.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 from interface irb.0')
                cmd.append('set policy-options policy-statement export-bgp term 1 then accept')
                cmd.append('set policy-options policy-statement export-bgp term 2 then reject')
                cmd.append('set policy-options policy-statement pplb then load-balance per-packet')
                cmd.append('set policy-options policy-statement pplb then accept')
                cmd.append('set policy-options policy-statement send-direct term 2 from protocol direct')
                cmd.append('set policy-options policy-statement send-direct term 2 then accept')
                cmd.append('set policy-options community IPFAB-LEAF members 64512:2001')
                cmd.append('set vlans rhosp_dev_1716 vlan-id 3211')
                cmd.append('set vlans vlan-l3mh-10 vlan-id 10')
                cmd.append('set vlans vlan-l3mh-10 l3-interface irb.10')
                cmd.append('set vlans vlan-l3mh-gateway2 vlan-id 2000')
                cmd.append('set vlans vlan-l3mh-gateway2 l3-interface irb.2000')

            mx_handle = NetconfConnection(host=router_params['mgmt_ip'])
            mx_handle.connect()
            cli_output = mx_handle.config(stmts=cmd, timeout=120)

    def check_routes_on_boxes(self):

        for i in range(len(list(self.inputs.l3mh_routers_data.values()))):
            router_params = list(self.inputs.l3mh_routers_data.values())[i]
            mx_handle = NetconfConnection(host=router_params['mgmt_ip'])
            mx_handle.connect()
            cli_output = mx_handle.get_config()
            if router_params['role'] == 'spine':
                assert router_params['spine_dev_vlan'] in cmd, 'No spine dev vlan found'
                assert router_params['spine_gw1_vlan'] in cmd, 'No spine gw vlan found'
                assert router_params['spine_gw2_vlan'] in cmd, 'No spine gw vlan found'
            elif router_params['role'] == 'leaf1':
                assert router_params['leaf1_dev_vlan'] in cmd, 'No leaf dev vlan found'
                assert router_params['leaf1_gw_vlan'] in cmd, 'No leaf gw vlan found'
            elif router_params['role'] == 'leaf2':
                assert router_params['leaf2_dev_vlan'] in cmd, 'No leaf dev vlan found'
                assert router_params['leaf2_gw_vlan'] in cmd, 'No leaf gw vlan found'

    def scale_vms_vns_policy(self):
        # get vn and vm names

        self.vn1_name = get_random_name('vn1')
        self.vn2_name = get_random_name('vn2')
        self.vn3_name = get_random_name('vn3')
        self.vn4_name = get_random_name('vn4')
        self.vn5_name = get_random_name('vn5')
        self.vn6_name = get_random_name('vn6')
        self.vn7_name = get_random_name('vn7')
        self.vn8_name = get_random_name('vn8')
        self.vn9_name = get_random_name('vn9')
        self.vn10_name = get_random_name('vn10')
        self.vm1_name = get_random_name('vm1')
        self.vm2_name = get_random_name('vm2')
        self.vm3_name = get_random_name('vm3')
        self.vm4_name = get_random_name('vm4')
        self.vm5_name = get_random_name('vm5')
        self.vm6_name = get_random_name('vm6')
        self.vm7_name = get_random_name('vm7')
        self.vm8_name = get_random_name('vm8')

        # get dpdk compute

        self.node1 = []
        self.node2 = []
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    self.node1.append(self.inputs.host_data[host]['name'])
            else:
                self.node2.append(self.inputs.host_data[host]['name'])

        # create vns
        self.vn1_fixture = self.create_vn(
            vn_name=self.vn1_name, orch=self.orchestrator)
        self.vn2_fixture = self.create_vn(
            vn_name=self.vn2_name, orch=self.orchestrator)
        self.vn3_fixture = self.create_vn(
            vn_name=self.vn3_name, orch=self.orchestrator)
        self.vn4_fixture = self.create_vn(
            vn_name=self.vn4_name, orch=self.orchestrator)
        self.vn5_fixture = self.create_vn(
            vn_name=self.vn5_name, orch=self.orchestrator)
        self.vn6_fixture = self.create_vn(
            vn_name=self.vn6_name, orch=self.orchestrator)
        self.vn7_fixture = self.create_vn(
            vn_name=self.vn7_name, orch=self.orchestrator)
        self.vn8_fixture = self.create_vn(
            vn_name=self.vn8_name, orch=self.orchestrator)

        policy_fixture = self.setup_only_policy_between_vns(self.vn1_fixture,
                                                            self.vn2_fixture)
        self.vn1_fixture.read()
        self.vn2_fixture.read()
        self.vn3_fixture.read()
        self.vn4_fixture.read()
        self.vn5_fixture.read()
        self.vn6_fixture.read()
        self.vn7_fixture.read()
        self.vn8_fixture.read()

        # create vms
        self.vm2_fixture = self.create_vm(vn_fixture=self.vn2_fixture,
                                          image_name='cirros', vm_name=self.vm2_name, node_name=self.node2[0])
        self.vm1_fixture = self.create_vm(vn_fixture=self.vn1_fixture,
                                          image_name='cirros', vm_name=self.vm1_name, node_name=self.node1[0], flavor='ubuntu_traffic_dpdk')

        inspect_h = self.agent_inspect[self.vm2_fixture.vm_node_ip]
        cmd = 'ip addr add 108.1.1.5/32 dev vhost0; sleep 5'
        self.inputs.run_cmd_on_server(self.vm2_fixture.vm_node_ip, cmd)

        inspect_h = self.agent_inspect[self.vm1_fixture.vm_node_ip]
        cmd = 'ip addr add 108.1.1.6/32 dev vhost0; sleep 5'
        self.inputs.run_cmd_on_server(self.vm1_fixture.vm_node_ip, cmd)
        assert self.vm2_fixture.wait_till_vm_is_up()
        assert self.vm1_fixture.wait_till_vm_is_up()
        self.vm1_fixture.ping_with_certainty(self.vm2_fixture.vm_ip)
        self.vm3_fixture = self.create_vm(vn_fixture=self.vn3_fixture,
                                          image_name='cirros', vm_name=self.vm3_name, node_name=self.node1[0], flavor='cirros_dpdk')
        self.vm4_fixture = self.create_vm(vn_fixture=self.vn4_fixture,
                                          image_name='cirros', vm_name=self.vm4_name, node_name=self.node1[0], flavor='cirros_dpdk')
        assert self.vm3_fixture.wait_till_vm_is_up()
        assert self.vm4_fixture.wait_till_vm_is_up()

        self.logger.info(
            "Create VN, enable FABRIC SNAT and verify its routing instance")
        vn_fixture = self.create_vn_enable_fabric_snat()

        test_vm1 = self.create_vm(vn_fixture, get_random_name('test_vm1'),
                                  image_name='ubuntu')
        test_vm2 = self.create_vm(vn_fixture, get_random_name('test_vm2'),
                                  image_name='ubuntu')
        assert test_vm1.wait_till_vm_is_up()
        assert test_vm2.wait_till_vm_is_up()

    def feature_check(self):
        destport = random.randint(1000, 60000)
        baseport = random.randint(1000, 60000)
        # Create flows using hping
        hping_h = Hping3(self.vm1_fixture,
                         self.vm2_fixture,
                         syn=True,
                         destport=destport,
                         baseport=baseport,
                         count=10,
                         interval=2)
        hping_h.start(wait=False)

        test_vm = self.create_vm(self.vn1_fixture, 'test_vm',
                                 image_name='ubuntu-traffic')
        assert test_vm.wait_till_vm_is_up()

        self.bgpaas_vm = self.create_vm(self.vn1_fixture, 'bgpaas_vm1',
                                    image_name='vsrx')
        assert self.bgpaas_vm.wait_till_vm_is_up()
        autonomous_system1 = 63500

        bgpaas_fixture1 = self.create_bgpaas(
            bgpaas_shared=True, autonomous_system=autonomous_system1, bgpaas_ip_address=self.bgpaas_vm.vm_ip)
        port1 = self.bgpaas_vm.vmi_ids[self.bgpaas_vm.vn_fq_name]

        address_families = []
        address_families = ['inet', 'inet6']
        gw_ip = self.vn1_fixture.get_subnets()[0]['gateway_ip']
        dns_ip = self.vn1_fixture.get_subnets()[0]['dns_server_address']
        neighbors = [gw_ip, dns_ip]
        self.config_bgp_on_vsrx(src_vm=test_vm, dst_vm=self.bgpaas_vm, bgp_ip=self.bgpaas_vm.vm_ip, lo_ip=self.bgpaas_vm.vm_ip,
                                address_families=address_families, autonomous_system=autonomous_system1, neighbors=neighbors, bfd_enabled=False)
        self.attach_vmi_to_bgpaas(port1, bgpaas_fixture1)
        self.addCleanup(self.detach_vmi_from_bgpaas,
                        port1, bgpaas_fixture1)
        time.sleep(60)
        assert bgpaas_fixture1.verify_in_control_node(self.bgpaas_vm), 'BGPaaS Session not seen in the control-node'

        test_vm1 = self.create_vm(self.vn2_fixture, 'test_vm2',
                                 image_name='ubuntu-traffic')
        assert test_vm1.wait_till_vm_is_up()

        self.bgpaas_vm2 = self.create_vm(self.vn2_fixture, 'bgpaas_vm2',
                                    image_name='vsrx')
        assert self.bgpaas_vm2.wait_till_vm_is_up()
        autonomous_system2 = 63600

        bgpaas_fixture2 = self.create_bgpaas(
            bgpaas_shared=True, autonomous_system=autonomous_system2, bgpaas_ip_address=self.bgpaas_vm2.vm_ip)
        port2 = self.bgpaas_vm2.vmi_ids[self.bgpaas_vm2.vn_fq_name]

        address_families = []
        address_families = ['inet', 'inet6']
        gw_ip = self.vn2_fixture.get_subnets()[0]['gateway_ip']
        dns_ip = self.vn2_fixture.get_subnets()[0]['dns_server_address']
        neighbors = [gw_ip, dns_ip]
        self.config_bgp_on_vsrx(src_vm=test_vm1, dst_vm=self.bgpaas_vm2, bgp_ip=self.bgpaas_vm2.vm_ip, lo_ip=self.bgpaas_vm2.vm_ip,
                                address_families=address_families, autonomous_system=autonomous_system2, neighbors=neighbors, bfd_enabled=False)
        self.attach_vmi_to_bgpaas(port2, bgpaas_fixture2)
        self.addCleanup(self.detach_vmi_from_bgpaas,
                        port2, bgpaas_fixture2)
        time.sleep(60)
        assert bgpaas_fixture2.verify_in_control_node(self.bgpaas_vm2), 'BGPaaS Session not seen in the control-node'

    def change_and_check_encap(self):
        self.logger.info("Read the existing encap priority")
        existing_encap = self.connections.read_vrouter_config_encap()
        self.logger.info('Setting new Encap before continuing')
        config_id = self.connections.update_vrouter_config_encap(
            'MPLSoGRE', 'VXLAN', 'MPLSoUDP')
        self.logger.info('Created.UUID is %s' % (config_id))

        configured_encap_list = [
            str('MPLSoGRE'), str('VXLAN'), str('MPLSoUDP')]
        if existing_encap != configured_encap_list:
            self.addCleanup(
                self.connections.update_vrouter_config_encap,
                existing_encap[0],
                existing_encap[1],
                existing_encap[2])
        encap_list = self.connections.read_vrouter_config_encap()
        if configured_encap_list != encap_list:

            self.logger.error(
                "Configured Encap Priority order is NOT matching with expected order. Configured: %s ,Expected: %s" %
                (configured_encap_list, encap_list))
            assert False
        else:
            self.logger.info(
                "Configured Encap Priority order is matching with expected order. Configured: %s ,Expected: %s" %
                (configured_encap_list, encap_list))

    @test.attr(type=['l3mh_regression'])
    @preposttest_wrapper
    def test_l3mh_multi_dimensional(self):
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
            2. Configure bgpaas and confim if bgpaas works.
        '''
        self.spawn_dpdk_flavors()
        assert self.check_bgp_status(), "BGP between nodes not up after per peer match"
        self.configure_spine_leaf()
        self.scale_vms_vns_policy()
        self.feature_check()
        # ping test from vm1 to vm2, inter vn inter compute
        assert self.vm1_fixture.ping_with_certainty(self.vm2_fixture.vm_ip)

        # Restart physical interfaces
        inspect_h = self.agent_inspect[self.vm2_fixture.vm_node_ip]
        physical_intf_list = inspect_h.get_vna_interface_by_type('eth')
        cmd = 'ifdown %s; sleep 10' % (physical_intf_list[0])
        self.inputs.run_cmd_on_server(self.vm2_fixture.vm_node_ip, cmd)

        cmd = 'ifup %s; sleep 10' % (physical_intf_list[0])
        self.inputs.run_cmd_on_server(self.vm2_fixture.vm_node_ip, cmd)

        assert self.vm1_fixture.ping_with_certainty(self.vm2_fixture.vm_ip)

    # end test_bgpaas_l3mh

    @test.attr(type=['l3mh_regression'])
    @preposttest_wrapper
    def test_mirroring_l3mh(self):
        '''
            verify that interface mirroring works
        '''
        self.node1 = []
        self.node2 = []
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    self.node1.append(self.inputs.host_data[host]['name'])
            else:
                self.node2.append(self.inputs.host_data[host]['name'])

        compute_nodes = [self.node2[0],self.node2[0],self.node2[0]]
        self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf=False, ipv6=False)

    @test.attr(type=['l3mh_regression'])
    @preposttest_wrapper
    def test_encap_l3mh(self):
        '''
            verify that changing encap works 
        '''
        self.change_and_check_encap()

    @test.attr(type=['l3mh_regression'])
    @preposttest_wrapper
    def test_restart_l3mh(self):
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
            2. Validate the fabric forwarding feature
        '''
        if (len(self.inputs.compute_ips) < 2):
            raise self.skipTest(
                "Skipping Test. At least 2 compute node required to run the test")

        # VN parameters. IP Fabric forwarding is enabled on vn1.
        vn = {'count': 1,
              'vn1': {'subnet': get_random_cidr(), 'ip_fabric': True},
              }

        # VMI parameters
        vmi = {'count': 2,
               'vmi1': {'vn': 'vn1'},
               'vmi2': {'vn': 'vn1'},
               }

        # VM parameters
        vm = {'count': 2, 'launch_mode': 'distribute',
              'vm1': {'vn': ['vn1'], 'vmi': ['vmi1']},
              'vm2': {'vn': ['vn1'], 'vmi': ['vmi2']},
              }

        # Setup VNs, VMs as per user configuration
        ret_dict = self.setup_gw_less_fwd(vn=vn, vmi=vmi, vm=vm)
        vn_fixtures = ret_dict['vn_fixtures']
        vm_fixtures = ret_dict['vm_fixtures']

        # Verify Gateway less forward functionality. As IP Fabric forwarding
        # is enabled on vn1, traffic should go through underlay between VMs
        # As there is no explicit policy to allow traffic between VN and
        # "ip-fbric" network, ping from vhost to VM and VM to vhost should fail

        self.node1 = []
        self.node2 = []
        for host in self.inputs.compute_ips:
            if self.inputs.host_data[host]['roles'].get(
                    'vrouter').get('AGENT_MODE'):
                if 'dpdk' in self.inputs.host_data[host]['roles'].get(
                        'vrouter').get('AGENT_MODE'):
                    self.node1.append(self.inputs.host_data[host]['name'])
            else:
                self.node2.append(self.inputs.host_data[host]['name'])

        self.inputs.restart_service(
            'contrail-vrouter-agent', [self.node1[0]], container='agent')
        cluster_status, error_nodes = ContrailStatusChecker(
        ).wait_till_contrail_cluster_stable(nodes=[self.node1[0]])
        assert cluster_status, 'Hash of error nodes and services : %s' % (
            error_nodes)

    # end test_l3mh_fabric_forwarding
