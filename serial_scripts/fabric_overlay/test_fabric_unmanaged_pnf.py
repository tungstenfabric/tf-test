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
from tcutils.util import get_random_name
from vnc_api.vnc_api import *


class TestFabricUnmanagedPNF(BaseFabricTest):

    @classmethod
    def setUpClass(cls):
        super(TestFabricUnmanagedPNF, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestFabricUnmanagedPNF, cls).tearDownClass()

    def is_test_applicable(self):
        result, msg = super(TestFabricUnmanagedPNF,
                            self).is_test_applicable()
        if result:
            msg = 'No Unmanaged PNF Peer device in the provided fabric ' \
                  'topology'
            bms_connected_2_spines = self.get_bms_nodes(role='spine')
            if len(bms_connected_2_spines) > 0:
                return True, None
        return False, msg

    @preposttest_wrapper
    def test_fabric_unmanaged_pnf_static(self):
        '''
           As part of this test cases 1) we cover only the CRB use cases. 2) We use the BMS device as external/unmanaged Firewall device.

           Steps:

           Create VN vn1
           Create VN (routed) rvn1
           Create VNs per BMS node
           Create Tenant VPG
           Create Routed VPG
           Create Interface Routing Table
           Create Logical Router with vn1 and rvn1
           Update the rvn1 with routed properties for static code
           Check ping connectivity across all the instances
        '''

        vn1 = self.create_vn()
        # rvn1 = self.create_vn(option='contrail', virtual_network_category='routed')
        rvn1 = self.create_vn()
        rvn1.update_vn_network_category(virtual_network_category='routed')
        vn2 = self.create_vn()
        # rvn2 = self.create_vn(option='contrail', virtual_network_category='routed')
        rvn2 = self.create_vn()
        rvn2.update_vn_network_category(virtual_network_category='routed')

        firewall_bmses = self.get_bms_nodes(role='spine')

        unmanaged_device_peers = self.get_associated_prouters(firewall_bmses[0])

        lr1 = self.create_logical_router([vn1, rvn1],
                                         devices=unmanaged_device_peers)
        lr2 = self.create_logical_router([vn2, rvn2],
                                         devices=unmanaged_device_peers)

        irb1_ip = rvn1.get_an_ip(index=1)
        peer1_irb_ip = rvn1.get_an_ip(index=2)

        vn1_irtb = self.create_interface_route_table(
            rvn1.get_uuid(), prefixes=[vn2.vn_subnets[0]['cidr']],
            community_action='accept-own')

        vn1_irtb_uuid = vn1_irtb.uuid
        static_routed_props_1 = \
            self.connections.orch.vnc_h.create_static_route_props(
                unmanaged_device_peers[0].uuid, lr1.uuid,irb1_ip, vn1_irtb_uuid, peer1_irb_ip)

        irb2_ip = rvn2.get_an_ip(index=1)
        peer2_irb_ip = rvn2.get_an_ip(index=2)
        vn2_irtb = self.create_interface_route_table(
            rvn2.get_uuid(), prefixes=[vn1.vn_subnets[0]['cidr']],
            community_action='accept-own')

        vn2_irtb_uuid = vn2_irtb.uuid
        static_routed_props_2 = \
            self.connections.orch.vnc_h.create_static_route_props(
                unmanaged_device_peers[0].uuid, lr2.uuid, irb2_ip, vn2_irtb_uuid, peer2_irb_ip)

        rvn1.update_vn_routed_properties(
            routed_properties=static_routed_props_1)
        rvn2.update_vn_routed_properties(
            routed_properties=static_routed_props_2)

        tenant_bmses = self.get_bms_nodes(role='leaf')

        tenant_bms = self.create_bms(
            bms_name=tenant_bmses[0],
            vlan_id=97,
            vn_fixture=vn1)

        tenant_bms_1 = self.create_bms(bms_name=tenant_bmses[0],
                        vlan_id=98,
                        bond_name=tenant_bms.bond_name,
                        port_group_name=tenant_bms.port_group_name,
                        vn_fixture=vn2)

        bms_fix = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=95,
            vn_fixture=rvn1, static_ip=True)

        bms_fix.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(ifc_name=bms_fix.mvlanintf, ip=peer1_irb_ip, sub_net=bms_fix.bms_ip_netmask))
        bms_fix.run_namespace("route add -net {vn} gw {gw_ip}".format(vn=vn1.vn_subnets[0]['cidr'], gw_ip=irb1_ip))

        bms_fix_1 = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=96,
            bond_name=bms_fix.bond_name,
            port_group_name=bms_fix.port_group_name,
            vn_fixture=rvn2, namespace=bms_fix.namespace, static_ip=True)

        bms_fix_1.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(ifc_name=bms_fix_1.mvlanintf, ip=peer2_irb_ip,sub_net=bms_fix_1.bms_ip_netmask))
        bms_fix_1.run_namespace("route add -net {vn} gw {gw_ip}".format(vn=vn2.vn_subnets[0]['cidr'], gw_ip=irb2_ip))

        self.do_ping_mesh([tenant_bms, tenant_bms_1])

    @preposttest_wrapper
    def test_fabric_unmanaged_pnf_ebgp(self):
        '''
           Create VN vn1
           Create VN (routed) rvn1
           Create VNs per BMS node
           Create Tenant VPG
           Create Routed VPG
           Create Routing Policy
           Create Logical Router with vn1 and rvn1
           Update the rvn1 with routed properties for eBGP
           Check ping connectivity across all the instances
        '''

        vn1 = self.create_vn()
        # rvn1 = self.create_vn(option='contrail', virtual_network_category='routed')
        rvn1 = self.create_vn()
        rvn1.update_vn_network_category(virtual_network_category='routed')
        vn2 = self.create_vn()
        # rvn2 = self.create_vn(option='contrail', virtual_network_category='routed')
        rvn2 = self.create_vn()
        rvn2.update_vn_network_category(virtual_network_category='routed')

        firewall_bmses = self.get_bms_nodes(role='spine')

        unmanaged_device_peers = self.get_associated_prouters(firewall_bmses[0])

        lr1 = self.create_logical_router([vn1, rvn1],
                                         devices=unmanaged_device_peers)
        lr2 = self.create_logical_router([vn2, rvn2],
                                         devices=unmanaged_device_peers)

        irb1_ip = rvn1.get_an_ip(index=1)
        peer1_irb_ip = rvn1.get_an_ip(index=2)

        pterm = self.connections.orch.vnc_h.create_routing_policy_term(protocols=['static'])
        rp_uuid = self.connections.orch.vnc_h.create_routing_policy(get_random_name("policy"), policy_term=pterm)

        bgp_routed_properties_1 = self.connections.orch.vnc_h.create_bgp_routed_properties(
            unmanaged_device_peers[0].uuid, lr1.uuid, irb1_ip, peer1_irb_ip, "65000", "64512", import_rp=[rp_uuid], export_rp=[rp_uuid])

        irb2_ip = rvn2.get_an_ip(index=1)
        peer2_irb_ip = rvn2.get_an_ip(index=2)

        bgp_routed_properties_2 = self.connections.orch.vnc_h.create_bgp_routed_properties(
            unmanaged_device_peers[0].uuid, lr2.uuid, irb2_ip, peer2_irb_ip, "65000", "64512", import_rp=[rp_uuid], export_rp=[rp_uuid])

        rvn1.update_vn_routed_properties(
            routed_properties=bgp_routed_properties_1)
        rvn2.update_vn_routed_properties(
            routed_properties=bgp_routed_properties_2)
        tenant_bmses = self.get_bms_nodes(role='leaf')

        tenant_bms = self.create_bms(
            bms_name=tenant_bmses[0],
            vlan_id=97,
            vn_fixture=vn1)

        tenant_bms_1 = self.create_bms(bms_name=tenant_bmses[0],
                                       vlan_id=98,
                                       bond_name=tenant_bms.bond_name,
                                       port_group_name=tenant_bms.port_group_name,
                                       vn_fixture=vn2)

        bms_fix = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=95,
            vn_fixture=rvn1, static_ip=True)

        bms_fix.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(
            ifc_name=bms_fix.mvlanintf, ip=peer1_irb_ip,
            sub_net=bms_fix.bms_ip_netmask))

        bms_fix_1 = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=96,
            bond_name=bms_fix.bond_name,
            port_group_name=bms_fix.port_group_name,
            vn_fixture=rvn2, namespace=bms_fix.namespace, static_ip=True)

        bms_fix_1.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(
            ifc_name=bms_fix_1.mvlanintf, ip=peer2_irb_ip,
            sub_net=bms_fix_1.bms_ip_netmask))

        bird_config = self.generate_bird_conf(peer1_irb_ip, peer1_irb_ip, "65000", irb1_ip, "64512", peer2_irb_ip, "65000", irb2_ip, "64512")

        bms_fix_1.run("cat <<EOF > bird.conf \n{conf}\nEOF".format(conf=bird_config))
        bms_fix_1.run_namespace("bird -s bird.sock -c bird.conf -P bird.pid")

        self.do_ping_mesh([tenant_bms, tenant_bms_1])

        # Cleanup
        bms_fix_1.run("kill -9 `cat bird.pid`; rm -rf bird.pid bird.sock bird.conf")
