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
from tcutils.util import get_random_name
from tcutils.util import skip_because
from vnc_api.vnc_api import *
from interface_route_table_fixture import InterfaceRouteTableFixture


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

        vn1_irtb = self._create_interface_route_table(
            rvn1.get_uuid(), prefixes=[vn2.vn_subnets[0]['cidr']],
            community_action='accept-own')

        vn1_irtb_uuid = vn1_irtb.uuid
        static_routed_props_1 = self._create_static_route_props(
            unmanaged_device_peers[0].uuid, lr1.uuid,irb1_ip, vn1_irtb_uuid,
            peer1_irb_ip)

        irb2_ip = rvn2.get_an_ip(index=1)
        peer2_irb_ip = rvn2.get_an_ip(index=2)
        vn2_irtb = self._create_interface_route_table(
            rvn2.get_uuid(), prefixes=[vn1.vn_subnets[0]['cidr']],
            community_action='accept-own')

        vn2_irtb_uuid = vn2_irtb.uuid
        static_routed_props_2 = self._create_static_route_props(
             unmanaged_device_peers[0].uuid, lr2.uuid, irb2_ip, vn2_irtb_uuid,
            peer2_irb_ip)

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
            vn_fixture=rvn1, assign_ip=False, port_group_type="routed")

        bms_fix.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(ifc_name=bms_fix.mvlanintf, ip=peer1_irb_ip, sub_net=bms_fix.bms_ip_netmask))
        bms_fix.run_namespace("route add -net {vn} gw {gw_ip}".format(vn=vn1.vn_subnets[0]['cidr'], gw_ip=irb1_ip))

        bms_fix_1 = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=96,
            bond_name=bms_fix.bond_name,
            port_group_name=bms_fix.port_group_name,
            vn_fixture=rvn2, namespace=bms_fix.namespace, assign_ip=False, port_group_type="routed")

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

        pterm = self._create_routing_policy_term(protocols=['static'])
        rp_uuid = self._create_routing_policy(get_random_name("policy"), policy_term=pterm)

        bgp_routed_properties_1 = self._create_bgp_routed_properties(
            unmanaged_device_peers[0].uuid, lr1.uuid, irb1_ip, peer1_irb_ip, "65000", "64512", import_rp=[rp_uuid], export_rp=[rp_uuid])

        irb2_ip = rvn2.get_an_ip(index=1)
        peer2_irb_ip = rvn2.get_an_ip(index=2)

        bgp_routed_properties_2 = self._create_bgp_routed_properties(
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
            vn_fixture=rvn1, assign_ip=False,
            port_group_type="routed")

        bms_fix.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(
            ifc_name=bms_fix.mvlanintf, ip=peer1_irb_ip,
            sub_net=bms_fix.bms_ip_netmask))


        bms_fix_1 = self.create_bms(
            bms_name=firewall_bmses[0],
            vlan_id=96,
            bond_name=bms_fix.bond_name,
            port_group_name=bms_fix.port_group_name,
            vn_fixture=rvn2, namespace=bms_fix.namespace, assign_ip=False,
            port_group_type="routed")

        bms_fix_1.run_namespace("ifconfig {ifc_name} {ip}/{sub_net} up".format(
            ifc_name=bms_fix_1.mvlanintf, ip=peer2_irb_ip,
            sub_net=bms_fix_1.bms_ip_netmask))

        bird_config = self.generate_bird_conf(peer1_irb_ip, peer1_irb_ip, "65000", irb1_ip, "64512", peer2_irb_ip, "65000", irb2_ip, "64512")

        bms_fix_1.run("cat <<EOF > bird.conf \n{conf}\nEOF".format(conf=bird_config))
        bms_fix_1.run_namespace("bird -s bird.sock -c bird.conf -P bird.pid")

        self.do_ping_mesh([tenant_bms, tenant_bms_1])

        # Cleanup
        bms_fix_1.run("kill -9 `cat bird.pid`; rm -rf bird.pid bird.sock bird.conf")


    def _create_interface_route_table(self, rvn_uuid, prefixes,
                                      community_action=None):
        name = 'irt' + rvn_uuid
        irt_fixture = self.useFixture(InterfaceRouteTableFixture(
            connections=self.connections, name=name,
            prefixes=prefixes, community_action=community_action))
        irt_fixture.setUp()

        return irt_fixture
    # end create_irt

    @staticmethod
    def _create_static_route_props(pr_uuid, lr_uuid, interface_ip, irt_uuid,
                                   irt_next_hope):

        static_route_params = StaticRouteParameters(
            interface_route_table_uuid=[irt_uuid],
            next_hop_ip_address=[irt_next_hope]
        )
        return RoutedProperties(
            logical_router_uuid=lr_uuid,
            physical_router_uuid=pr_uuid,
            routed_interface_ip_address=interface_ip,
            routing_protocol='static-routes',
            bgp_params=None,
            static_route_params=static_route_params,
            routing_policy_params=None,
            bfd_params=None)

    @staticmethod
    def _create_bgp_routed_properties(pr_uuid, lr_uuid, interface_ip,
                                      peer_ip, peer_asn, local_asn,
                                      auth_type=None, auth_key=None,
                                      auth_key_id=None, import_rp=None, export_rp=None):

        auth_props = None
        if auth_key or auth_type or auth_key_id:
            auth_props = AuthenticationData(
                key_type=auth_type, key_items=[
                    AuthenticationKeyItem(key_id=auth_key_id,
                                          key=auth_key)])
        bgp_params = BgpParameters(
            peer_autonomous_system=peer_asn,
            peer_ip_address_list=[peer_ip],
            auth_data= auth_props,
            local_autonomous_system=local_asn,
            hold_time=90)

        rp_params = RoutingPolicyParameters(
            import_routing_policy_uuid=import_rp,
            export_routing_policy_uuid=export_rp)

        return RoutedProperties(
            logical_router_uuid=lr_uuid,
            physical_router_uuid=pr_uuid,
            routed_interface_ip_address=interface_ip,
            routing_protocol='bgp',
            bgp_params=bgp_params,
            bfd_params=BfdParameters(
                time_interval=10,
                detection_time_multiplier=4),
            static_route_params=None,
            routing_policy_params=rp_params)

    def _create_routing_policy(self, rp_name, policy_term, term_t='network-device'):
        rp = RoutingPolicy(name=rp_name, term_type=term_t)
        rp.set_routing_policy_entries(PolicyStatementType(term=[policy_term]))
        rp_uuid = self.connections.get_vnc_lib_h().routing_policy_create(rp)
        return rp_uuid
    # end _create_routing_policy

    def _create_routing_policy_term(self, protocols=[], prefixs=[],
                                   prefixtypes=[], extcommunity_list=[],
                                   extcommunity_match_all = False,
                                   community_match_all = False, action="accept",
                                   local_pref=None, med=None, asn_list=[],
                                   routes=[], route_types=[], route_values=[]):
        prefix_list = []
        for i in range(len(prefixs)):
            prefix_list.append(PrefixMatchType(prefix=prefixs[i],
                                               prefix_type=prefixtypes[i]))
        route_filter = None
        for i in range(len(routes)):
            if route_filter is None:
                route_filter = RouteFilterType()
            route_filter.add_route_filter_properties(
                RouteFilterProperties(route=routes[i],
                                      route_type=route_types[i],
                                      route_type_value=route_values[i]))
        tcond = TermMatchConditionType(
            protocol=protocols, prefix=prefix_list,
            community_match_all=community_match_all,
            extcommunity_list=extcommunity_list,
            extcommunity_match_all=extcommunity_match_all,
            route_filter=route_filter)
        aspath = ActionAsPathType(expand=AsListType(asn_list=asn_list))
        updateo = ActionUpdateType(as_path=aspath, local_pref=local_pref,
                                   med=med)
        taction = TermActionListType(action=action, update=updateo)
        term = PolicyTermType(term_match_condition=tcond,
                              term_action_list=taction)
        return term
    # end _create_routing_policy_term

    @staticmethod
    def generate_bird_conf(router_id, local_ip1, local_asn1, neighbour_ip1,
                           neighbour_asn1, local_ip2=None, local_asn2=None, neighbour_ip2=None,
                           neighbour_asn2=None):
        common_bird_config = """log syslog all;

    router id $ROUTER_ID;

    protocol direct {
             interface "bond0*";
    }

    protocol device {
             scan time 10;
    }

    # Export routes to kernel
    protocol kernel {
             scan time 15;
             export all;
             import all;
             learn;
    }"""
        left_bgp = """
    protocol bgp public_left_1 {
    	description "My BGP uplink";
            export all;
    	local $LOCAL_IP1 as $LOCAL_ASN1;
    	neighbor $NEIGHBOUR_IP1 as $NEIGHBOUR_ASN1;
    	graceful restart;
    }"""
        right_bgp = """
    protocol bgp public_right_1 {
            export all;
    	description "My BGP uplink";
    	local $LOCAL_IP2 as $LOCAL_ASN2;
    	neighbor $NEIGHBOUR_IP2 as $NEIGHBOUR_ASN2;
    	graceful restart;
    }"""

        final_config = common_bird_config.replace('$ROUTER_ID', router_id)

        left_bgp = left_bgp.replace('$LOCAL_IP1', local_ip1)
        left_bgp = left_bgp.replace('$LOCAL_ASN1', local_asn1)
        left_bgp = left_bgp.replace('$NEIGHBOUR_IP1', neighbour_ip1)
        left_bgp = left_bgp.replace('$NEIGHBOUR_ASN1', neighbour_asn1)

        final_config = final_config + left_bgp

        if neighbour_ip2 and neighbour_asn2:
            right_bgp = right_bgp.replace('$LOCAL_IP2', local_ip2)
            right_bgp = right_bgp.replace('$LOCAL_ASN2', local_asn2)
            right_bgp = right_bgp.replace('$NEIGHBOUR_IP2', neighbour_ip2)
            right_bgp = right_bgp.replace('$NEIGHBOUR_ASN2', neighbour_asn2)

            final_config = final_config + right_bgp

        return final_config
