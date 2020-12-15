
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from builtins import str
from builtins import range
from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailVirtualNetwork(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, VIRTUAL_NETWORK_NETWORK_ID, ADDRESS_ALLOCATION_MODE, IGMP_ENABLE, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN, VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH, ROUTE_TARGET_LIST, ROUTE_TARGET_LIST_ROUTE_TARGET, MAC_LEARNING_ENABLED, PORT_SECURITY_ENABLED, FABRIC_SNAT, PBB_ETREE_ENABLE, DISPLAY_NAME, VIRTUAL_NETWORK_ROUTED_PROPERTIES, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID, VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS, MAC_AGING_TIME, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, MULTI_POLICY_SERVICE_CHAINS_ENABLED, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, MAC_LIMIT_CONTROL, MAC_LIMIT_CONTROL_MAC_LIMIT, MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION, VIRTUAL_NETWORK_PROPERTIES, VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT, VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID, VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER, VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE, VIRTUAL_NETWORK_PROPERTIES_RPF, VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION, VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS, ECMP_HASHING_INCLUDE_FIELDS, ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP, ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT, PROVIDER_PROPERTIES, PROVIDER_PROPERTIES_SEGMENTATION_ID, PROVIDER_PROPERTIES_PHYSICAL_NETWORK, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, IS_SHARED, VIRTUAL_NETWORK_CATEGORY, IMPORT_ROUTE_TARGET_LIST, IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET, MAC_MOVE_CONTROL, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT, MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION, ROUTER_EXTERNAL, IS_PROVIDER_NETWORK, PBB_EVPN_ENABLE, EXPORT_ROUTE_TARGET_LIST, EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET, FLOOD_UNKNOWN_UNICAST, LAYER2_CONTROL_WORD, EXTERNAL_IPAM, ROUTING_POLICY_REFS, ROUTING_POLICY_REFS_DATA, ROUTING_POLICY_REFS_DATA_SEQUENCE, SECURITY_LOGGING_OBJECT_REFS, NETWORK_POLICY_REFS, NETWORK_POLICY_REFS_DATA, NETWORK_POLICY_REFS_DATA_SEQUENCE, NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR, NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR, NETWORK_POLICY_REFS_DATA_TIMER, NETWORK_POLICY_REFS_DATA_TIMER_START_TIME, NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL, NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL, NETWORK_POLICY_REFS_DATA_TIMER_END_TIME, QOS_CONFIG_REFS, VIRTUAL_NETWORK_REFS, TAG_REFS, ROUTE_TABLE_REFS, BGPVPN_REFS, MULTICAST_POLICY_REFS, NETWORK_IPAM_REFS, NETWORK_IPAM_REFS_DATA, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER, NETWORK_IPAM_REFS_DATA_HOST_ROUTES, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, INTENT_MAP_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'virtual_network_network_id', 'address_allocation_mode', 'igmp_enable', 'virtual_network_fat_flow_protocols', 'virtual_network_fat_flow_protocols_fat_flow_protocol', 'virtual_network_fat_flow_protocols_fat_flow_protocol_protocol', 'virtual_network_fat_flow_protocols_fat_flow_protocol_port', 'virtual_network_fat_flow_protocols_fat_flow_protocol_ignore_address', 'virtual_network_fat_flow_protocols_fat_flow_protocol_source_prefix', 'virtual_network_fat_flow_protocols_fat_flow_protocol_source_prefix_ip_prefix', 'virtual_network_fat_flow_protocols_fat_flow_protocol_source_prefix_ip_prefix_len', 'virtual_network_fat_flow_protocols_fat_flow_protocol_source_aggregate_prefix_length', 'virtual_network_fat_flow_protocols_fat_flow_protocol_destination_prefix', 'virtual_network_fat_flow_protocols_fat_flow_protocol_destination_prefix_ip_prefix', 'virtual_network_fat_flow_protocols_fat_flow_protocol_destination_prefix_ip_prefix_len', 'virtual_network_fat_flow_protocols_fat_flow_protocol_destination_aggregate_prefix_length', 'route_target_list', 'route_target_list_route_target', 'mac_learning_enabled', 'port_security_enabled', 'fabric_snat', 'pbb_etree_enable', 'display_name', 'virtual_network_routed_properties', 'virtual_network_routed_properties_routed_properties', 'virtual_network_routed_properties_routed_properties_physical_router_uuid', 'virtual_network_routed_properties_routed_properties_logical_router_uuid', 'virtual_network_routed_properties_routed_properties_routed_interface_ip_address', 'virtual_network_routed_properties_routed_properties_loopback_ip_address', 'virtual_network_routed_properties_routed_properties_routing_protocol', 'virtual_network_routed_properties_routed_properties_bgp_params', 'virtual_network_routed_properties_routed_properties_bgp_params_peer_autonomous_system', 'virtual_network_routed_properties_routed_properties_bgp_params_peer_ip_address', 'virtual_network_routed_properties_routed_properties_bgp_params_peer_ip_address_list', 'virtual_network_routed_properties_routed_properties_bgp_params_hold_time', 'virtual_network_routed_properties_routed_properties_bgp_params_auth_data', 'virtual_network_routed_properties_routed_properties_bgp_params_auth_data_key_type', 'virtual_network_routed_properties_routed_properties_bgp_params_auth_data_key_items', 'virtual_network_routed_properties_routed_properties_bgp_params_auth_data_key_items_key_id', 'virtual_network_routed_properties_routed_properties_bgp_params_auth_data_key_items_key', 'virtual_network_routed_properties_routed_properties_bgp_params_local_autonomous_system', 'virtual_network_routed_properties_routed_properties_bgp_params_multihop_ttl', 'virtual_network_routed_properties_routed_properties_ospf_params', 'virtual_network_routed_properties_routed_properties_ospf_params_auth_data', 'virtual_network_routed_properties_routed_properties_ospf_params_auth_data_key_type', 'virtual_network_routed_properties_routed_properties_ospf_params_auth_data_key_items', 'virtual_network_routed_properties_routed_properties_ospf_params_auth_data_key_items_key_id', 'virtual_network_routed_properties_routed_properties_ospf_params_auth_data_key_items_key', 'virtual_network_routed_properties_routed_properties_ospf_params_hello_interval', 'virtual_network_routed_properties_routed_properties_ospf_params_dead_interval', 'virtual_network_routed_properties_routed_properties_ospf_params_area_id', 'virtual_network_routed_properties_routed_properties_ospf_params_area_type', 'virtual_network_routed_properties_routed_properties_ospf_params_advertise_loopback', 'virtual_network_routed_properties_routed_properties_ospf_params_orignate_summary_lsa', 'virtual_network_routed_properties_routed_properties_pim_params', 'virtual_network_routed_properties_routed_properties_pim_params_rp_ip_address', 'virtual_network_routed_properties_routed_properties_pim_params_mode', 'virtual_network_routed_properties_routed_properties_pim_params_enable_all_interfaces', 'virtual_network_routed_properties_routed_properties_static_route_params', 'virtual_network_routed_properties_routed_properties_static_route_params_interface_route_table_uuid', 'virtual_network_routed_properties_routed_properties_static_route_params_next_hop_ip_address', 'virtual_network_routed_properties_routed_properties_bfd_params', 'virtual_network_routed_properties_routed_properties_bfd_params_time_interval', 'virtual_network_routed_properties_routed_properties_bfd_params_detection_time_multiplier', 'virtual_network_routed_properties_routed_properties_routing_policy_params', 'virtual_network_routed_properties_routed_properties_routing_policy_params_import_routing_policy_uuid', 'virtual_network_routed_properties_routed_properties_routing_policy_params_export_routing_policy_uuid', 'virtual_network_routed_properties_shared_across_all_lrs', 'mac_aging_time', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'multi_policy_service_chains_enabled', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'mac_limit_control', 'mac_limit_control_mac_limit', 'mac_limit_control_mac_limit_action', 'virtual_network_properties', 'virtual_network_properties_allow_transit', 'virtual_network_properties_network_id', 'virtual_network_properties_vxlan_network_identifier', 'virtual_network_properties_forwarding_mode', 'virtual_network_properties_rpf', 'virtual_network_properties_mirror_destination', 'virtual_network_properties_max_flows', 'ecmp_hashing_include_fields', 'ecmp_hashing_include_fields_hashing_configured', 'ecmp_hashing_include_fields_source_ip', 'ecmp_hashing_include_fields_destination_ip', 'ecmp_hashing_include_fields_ip_protocol', 'ecmp_hashing_include_fields_source_port', 'ecmp_hashing_include_fields_destination_port', 'provider_properties', 'provider_properties_segmentation_id', 'provider_properties_physical_network', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'is_shared', 'virtual_network_category', 'import_route_target_list', 'import_route_target_list_route_target', 'mac_move_control', 'mac_move_control_mac_move_limit', 'mac_move_control_mac_move_time_window', 'mac_move_control_mac_move_limit_action', 'router_external', 'is_provider_network', 'pbb_evpn_enable', 'export_route_target_list', 'export_route_target_list_route_target', 'flood_unknown_unicast', 'layer2_control_word', 'external_ipam', 'routing_policy_refs', 'routing_policy_refs_data', 'routing_policy_refs_data_sequence', 'security_logging_object_refs', 'network_policy_refs', 'network_policy_refs_data', 'network_policy_refs_data_sequence', 'network_policy_refs_data_sequence_major', 'network_policy_refs_data_sequence_minor', 'network_policy_refs_data_timer', 'network_policy_refs_data_timer_start_time', 'network_policy_refs_data_timer_on_interval', 'network_policy_refs_data_timer_off_interval', 'network_policy_refs_data_timer_end_time', 'qos_config_refs', 'virtual_network_refs', 'tag_refs', 'route_table_refs', 'bgpvpn_refs', 'multicast_policy_refs', 'network_ipam_refs', 'network_ipam_refs_data', 'network_ipam_refs_data_ipam_subnets', 'network_ipam_refs_data_ipam_subnets_subnet', 'network_ipam_refs_data_ipam_subnets_subnet_ip_prefix', 'network_ipam_refs_data_ipam_subnets_subnet_ip_prefix_len', 'network_ipam_refs_data_ipam_subnets_default_gateway', 'network_ipam_refs_data_ipam_subnets_dns_server_address', 'network_ipam_refs_data_ipam_subnets_subnet_uuid', 'network_ipam_refs_data_ipam_subnets_enable_dhcp', 'network_ipam_refs_data_ipam_subnets_dns_nameservers', 'network_ipam_refs_data_ipam_subnets_allocation_pools', 'network_ipam_refs_data_ipam_subnets_allocation_pools_start', 'network_ipam_refs_data_ipam_subnets_allocation_pools_end', 'network_ipam_refs_data_ipam_subnets_allocation_pools_vrouter_specific_pool', 'network_ipam_refs_data_ipam_subnets_addr_from_start', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_name', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_value', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_value_bytes', 'network_ipam_refs_data_ipam_subnets_host_routes', 'network_ipam_refs_data_ipam_subnets_host_routes_route', 'network_ipam_refs_data_ipam_subnets_host_routes_route_prefix', 'network_ipam_refs_data_ipam_subnets_host_routes_route_next_hop', 'network_ipam_refs_data_ipam_subnets_host_routes_route_next_hop_type', 'network_ipam_refs_data_ipam_subnets_host_routes_route_community_attributes', 'network_ipam_refs_data_ipam_subnets_host_routes_route_community_attributes_community_attribute', 'network_ipam_refs_data_ipam_subnets_subnet_name', 'network_ipam_refs_data_ipam_subnets_alloc_unit', 'network_ipam_refs_data_ipam_subnets_created', 'network_ipam_refs_data_ipam_subnets_last_modified', 'network_ipam_refs_data_ipam_subnets_subscriber_tag', 'network_ipam_refs_data_ipam_subnets_vlan_tag', 'network_ipam_refs_data_ipam_subnets_dhcp_relay_server', 'network_ipam_refs_data_host_routes', 'network_ipam_refs_data_host_routes_route', 'network_ipam_refs_data_host_routes_route_prefix', 'network_ipam_refs_data_host_routes_route_next_hop', 'network_ipam_refs_data_host_routes_route_next_hop_type', 'network_ipam_refs_data_host_routes_route_community_attributes', 'network_ipam_refs_data_host_routes_route_community_attributes_community_attribute', 'intent_map_refs', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_NETWORK_ID: properties.Schema(
            properties.Schema.INTEGER,
            _('VIRTUAL_NETWORK_NETWORK_ID.'),
            update_allowed=True,
            required=False,
        ),
        ADDRESS_ALLOCATION_MODE: properties.Schema(
            properties.Schema.STRING,
            _('ADDRESS_ALLOCATION_MODE.'),
            update_allowed=True,
            required=False,
        ),
        IGMP_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IGMP_ENABLE.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'none', u'source', u'destination']),
                                ],
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        MAC_LEARNING_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('MAC_LEARNING_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        PORT_SECURITY_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PORT_SECURITY_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        FABRIC_SNAT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FABRIC_SNAT.'),
            update_allowed=True,
            required=False,
        ),
        PBB_ETREE_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PBB_ETREE_ENABLE.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_ROUTED_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'static-routes', u'bgp', u'ospf', u'pim']),
                                ],
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(0, 65535),
                                        ],
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.AllowedValues([u'md5']),
                                                ],
                                            ),
                                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS: properties.Schema(
                                                properties.Schema.LIST,
                                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            constraints=[
                                                                constraints.Range(0, 63),
                                                            ],
                                                        ),
                                                        VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.AllowedValues([u'md5']),
                                                ],
                                            ),
                                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS: properties.Schema(
                                                properties.Schema.LIST,
                                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            constraints=[
                                                                constraints.Range(0, 63),
                                                            ],
                                                        ),
                                                        VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'nssa', u'stub', u'backbone']),
                                        ],
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'sparse', u'sparse-dense', u'dense']),
                                        ],
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                        }
                    )
                ),
                VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        MAC_AGING_TIME: properties.Schema(
            properties.Schema.INTEGER,
            _('MAC_AGING_TIME.'),
            update_allowed=True,
            required=False,
        ),
        ID_PERMS: properties.Schema(
            properties.Schema.MAP,
            _('ID_PERMS.'),
            update_allowed=True,
            required=False,
            schema={
                ID_PERMS_PERMISSIONS: properties.Schema(
                    properties.Schema.MAP,
                    _('ID_PERMS_PERMISSIONS.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        ID_PERMS_PERMISSIONS_OWNER: properties.Schema(
                            properties.Schema.STRING,
                            _('ID_PERMS_PERMISSIONS_OWNER.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ID_PERMS_PERMISSIONS_OWNER_ACCESS: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ID_PERMS_PERMISSIONS_OWNER_ACCESS.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(0, 7),
                            ],
                        ),
                        ID_PERMS_PERMISSIONS_GROUP: properties.Schema(
                            properties.Schema.STRING,
                            _('ID_PERMS_PERMISSIONS_GROUP.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ID_PERMS_PERMISSIONS_GROUP_ACCESS: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ID_PERMS_PERMISSIONS_GROUP_ACCESS.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(0, 7),
                            ],
                        ),
                        ID_PERMS_PERMISSIONS_OTHER_ACCESS: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ID_PERMS_PERMISSIONS_OTHER_ACCESS.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(0, 7),
                            ],
                        ),
                    }
                ),
                ID_PERMS_UUID: properties.Schema(
                    properties.Schema.MAP,
                    _('ID_PERMS_UUID.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        ID_PERMS_UUID_UUID_MSLONG: properties.Schema(
                            properties.Schema.MAP,
                            _('ID_PERMS_UUID_UUID_MSLONG.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ID_PERMS_UUID_UUID_LSLONG: properties.Schema(
                            properties.Schema.MAP,
                            _('ID_PERMS_UUID_UUID_LSLONG.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                ID_PERMS_ENABLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ID_PERMS_ENABLE.'),
                    update_allowed=True,
                    required=False,
                ),
                ID_PERMS_CREATED: properties.Schema(
                    properties.Schema.INTEGER,
                    _('ID_PERMS_CREATED.'),
                    update_allowed=True,
                    required=False,
                ),
                ID_PERMS_LAST_MODIFIED: properties.Schema(
                    properties.Schema.INTEGER,
                    _('ID_PERMS_LAST_MODIFIED.'),
                    update_allowed=True,
                    required=False,
                ),
                ID_PERMS_DESCRIPTION: properties.Schema(
                    properties.Schema.STRING,
                    _('ID_PERMS_DESCRIPTION.'),
                    update_allowed=True,
                    required=False,
                ),
                ID_PERMS_USER_VISIBLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ID_PERMS_USER_VISIBLE.'),
                    update_allowed=True,
                    required=False,
                ),
                ID_PERMS_CREATOR: properties.Schema(
                    properties.Schema.STRING,
                    _('ID_PERMS_CREATOR.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        MULTI_POLICY_SERVICE_CHAINS_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('MULTI_POLICY_SERVICE_CHAINS_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        MAC_LIMIT_CONTROL: properties.Schema(
            properties.Schema.MAP,
            _('MAC_LIMIT_CONTROL.'),
            update_allowed=True,
            required=False,
            schema={
                MAC_LIMIT_CONTROL_MAC_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_LIMIT_CONTROL_MAC_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'log', u'alarm', u'shutdown', u'drop']),
                    ],
                ),
            }
        ),
        VIRTUAL_NETWORK_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_NETWORK_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(1, 16777215),
                    ],
                ),
                VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'l2_l3', u'l2', u'l3']),
                    ],
                ),
                VIRTUAL_NETWORK_PROPERTIES_RPF: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_NETWORK_PROPERTIES_RPF.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'enable', u'disable']),
                    ],
                ),
                VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 4294967296),
                    ],
                ),
            }
        ),
        ECMP_HASHING_INCLUDE_FIELDS: properties.Schema(
            properties.Schema.MAP,
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
            update_allowed=True,
            required=False,
            schema={
                ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PROVIDER_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('PROVIDER_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                PROVIDER_PROPERTIES_SEGMENTATION_ID: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PROVIDER_PROPERTIES_SEGMENTATION_ID.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 4094),
                    ],
                ),
                PROVIDER_PROPERTIES_PHYSICAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('PROVIDER_PROPERTIES_PHYSICAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PERMS2: properties.Schema(
            properties.Schema.MAP,
            _('PERMS2.'),
            update_allowed=True,
            required=False,
            schema={
                PERMS2_OWNER: properties.Schema(
                    properties.Schema.STRING,
                    _('PERMS2_OWNER.'),
                    update_allowed=True,
                    required=False,
                ),
                PERMS2_OWNER_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_OWNER_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_GLOBAL_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_GLOBAL_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_SHARE: properties.Schema(
                    properties.Schema.LIST,
                    _('PERMS2_SHARE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PERMS2_SHARE_TENANT: properties.Schema(
                                properties.Schema.STRING,
                                _('PERMS2_SHARE_TENANT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PERMS2_SHARE_TENANT_ACCESS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('PERMS2_SHARE_TENANT_ACCESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 7),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        IS_SHARED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IS_SHARED.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_CATEGORY: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK_CATEGORY.'),
            update_allowed=True,
            required=False,
        ),
        IMPORT_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('IMPORT_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        MAC_MOVE_CONTROL: properties.Schema(
            properties.Schema.MAP,
            _('MAC_MOVE_CONTROL.'),
            update_allowed=True,
            required=False,
            schema={
                MAC_MOVE_CONTROL_MAC_MOVE_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW: properties.Schema(
                    properties.Schema.INTEGER,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(1, 60),
                    ],
                ),
                MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'log', u'alarm', u'shutdown', u'drop']),
                    ],
                ),
            }
        ),
        ROUTER_EXTERNAL: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTER_EXTERNAL.'),
            update_allowed=True,
            required=False,
        ),
        IS_PROVIDER_NETWORK: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IS_PROVIDER_NETWORK.'),
            update_allowed=True,
            required=False,
        ),
        PBB_EVPN_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PBB_EVPN_ENABLE.'),
            update_allowed=True,
            required=False,
        ),
        EXPORT_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('EXPORT_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        FLOOD_UNKNOWN_UNICAST: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FLOOD_UNKNOWN_UNICAST.'),
            update_allowed=True,
            required=False,
        ),
        LAYER2_CONTROL_WORD: properties.Schema(
            properties.Schema.BOOLEAN,
            _('LAYER2_CONTROL_WORD.'),
            update_allowed=True,
            required=False,
        ),
        EXTERNAL_IPAM: properties.Schema(
            properties.Schema.BOOLEAN,
            _('EXTERNAL_IPAM.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_POLICY_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_POLICY_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTING_POLICY_REFS_DATA_SEQUENCE: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_POLICY_REFS_DATA_SEQUENCE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        SECURITY_LOGGING_OBJECT_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_LOGGING_OBJECT_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NETWORK_POLICY_REFS_DATA_SEQUENCE: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_POLICY_REFS_DATA_SEQUENCE.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    ),
                    NETWORK_POLICY_REFS_DATA_TIMER: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_POLICY_REFS_DATA_TIMER.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_POLICY_REFS_DATA_TIMER_START_TIME: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_START_TIME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_END_TIME: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_END_TIME.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    ),
                }
            )
        ),
        QOS_CONFIG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('QOS_CONFIG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TABLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TABLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        BGPVPN_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGPVPN_REFS.'),
            update_allowed=True,
            required=False,
        ),
        MULTICAST_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('MULTICAST_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_IPAM_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_IPAM_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_IPAM_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_IPAM_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS: properties.Schema(
                        properties.Schema.LIST,
                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS.'),
                        update_allowed=True,
                        required=False,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                    }
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP: properties.Schema(
                                    properties.Schema.BOOLEAN,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS.'),
                                    update_allowed=True,
                                    required=False,
                                    schema=properties.Schema(
                                        properties.Schema.MAP,
                                        schema={
                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                        }
                                    )
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START: properties.Schema(
                                    properties.Schema.BOOLEAN,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            )
                                        ),
                                    }
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        constraints=[
                                                            constraints.AllowedValues([u'service-instance', u'ip-address']),
                                                        ],
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                }
                                            )
                                        ),
                                    }
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        )
                    ),
                    NETWORK_IPAM_REFS_DATA_HOST_ROUTES: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.AllowedValues([u'service-instance', u'ip-address']),
                                            ],
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                            properties.Schema.MAP,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                            update_allowed=True,
                                            required=False,
                                            schema={
                                                NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                    properties.Schema.LIST,
                                                    _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                            }
                                        ),
                                    }
                                )
                            ),
                        }
                    ),
                }
            )
        ),
        INTENT_MAP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('INTENT_MAP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        VIRTUAL_NETWORK_NETWORK_ID: attributes.Schema(
            _('VIRTUAL_NETWORK_NETWORK_ID.'),
        ),
        ADDRESS_ALLOCATION_MODE: attributes.Schema(
            _('ADDRESS_ALLOCATION_MODE.'),
        ),
        IGMP_ENABLE: attributes.Schema(
            _('IGMP_ENABLE.'),
        ),
        VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS: attributes.Schema(
            _('VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS.'),
        ),
        ROUTE_TARGET_LIST: attributes.Schema(
            _('ROUTE_TARGET_LIST.'),
        ),
        MAC_LEARNING_ENABLED: attributes.Schema(
            _('MAC_LEARNING_ENABLED.'),
        ),
        PORT_SECURITY_ENABLED: attributes.Schema(
            _('PORT_SECURITY_ENABLED.'),
        ),
        FABRIC_SNAT: attributes.Schema(
            _('FABRIC_SNAT.'),
        ),
        PBB_ETREE_ENABLE: attributes.Schema(
            _('PBB_ETREE_ENABLE.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        VIRTUAL_NETWORK_ROUTED_PROPERTIES: attributes.Schema(
            _('VIRTUAL_NETWORK_ROUTED_PROPERTIES.'),
        ),
        MAC_AGING_TIME: attributes.Schema(
            _('MAC_AGING_TIME.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        MULTI_POLICY_SERVICE_CHAINS_ENABLED: attributes.Schema(
            _('MULTI_POLICY_SERVICE_CHAINS_ENABLED.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        MAC_LIMIT_CONTROL: attributes.Schema(
            _('MAC_LIMIT_CONTROL.'),
        ),
        VIRTUAL_NETWORK_PROPERTIES: attributes.Schema(
            _('VIRTUAL_NETWORK_PROPERTIES.'),
        ),
        ECMP_HASHING_INCLUDE_FIELDS: attributes.Schema(
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
        ),
        PROVIDER_PROPERTIES: attributes.Schema(
            _('PROVIDER_PROPERTIES.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        IS_SHARED: attributes.Schema(
            _('IS_SHARED.'),
        ),
        VIRTUAL_NETWORK_CATEGORY: attributes.Schema(
            _('VIRTUAL_NETWORK_CATEGORY.'),
        ),
        IMPORT_ROUTE_TARGET_LIST: attributes.Schema(
            _('IMPORT_ROUTE_TARGET_LIST.'),
        ),
        MAC_MOVE_CONTROL: attributes.Schema(
            _('MAC_MOVE_CONTROL.'),
        ),
        ROUTER_EXTERNAL: attributes.Schema(
            _('ROUTER_EXTERNAL.'),
        ),
        IS_PROVIDER_NETWORK: attributes.Schema(
            _('IS_PROVIDER_NETWORK.'),
        ),
        PBB_EVPN_ENABLE: attributes.Schema(
            _('PBB_EVPN_ENABLE.'),
        ),
        EXPORT_ROUTE_TARGET_LIST: attributes.Schema(
            _('EXPORT_ROUTE_TARGET_LIST.'),
        ),
        FLOOD_UNKNOWN_UNICAST: attributes.Schema(
            _('FLOOD_UNKNOWN_UNICAST.'),
        ),
        LAYER2_CONTROL_WORD: attributes.Schema(
            _('LAYER2_CONTROL_WORD.'),
        ),
        EXTERNAL_IPAM: attributes.Schema(
            _('EXTERNAL_IPAM.'),
        ),
        ROUTING_POLICY_REFS: attributes.Schema(
            _('ROUTING_POLICY_REFS.'),
        ),
        ROUTING_POLICY_REFS_DATA: attributes.Schema(
            _('ROUTING_POLICY_REFS_DATA.'),
        ),
        SECURITY_LOGGING_OBJECT_REFS: attributes.Schema(
            _('SECURITY_LOGGING_OBJECT_REFS.'),
        ),
        NETWORK_POLICY_REFS: attributes.Schema(
            _('NETWORK_POLICY_REFS.'),
        ),
        NETWORK_POLICY_REFS_DATA: attributes.Schema(
            _('NETWORK_POLICY_REFS_DATA.'),
        ),
        QOS_CONFIG_REFS: attributes.Schema(
            _('QOS_CONFIG_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        ROUTE_TABLE_REFS: attributes.Schema(
            _('ROUTE_TABLE_REFS.'),
        ),
        BGPVPN_REFS: attributes.Schema(
            _('BGPVPN_REFS.'),
        ),
        MULTICAST_POLICY_REFS: attributes.Schema(
            _('MULTICAST_POLICY_REFS.'),
        ),
        NETWORK_IPAM_REFS: attributes.Schema(
            _('NETWORK_IPAM_REFS.'),
        ),
        NETWORK_IPAM_REFS_DATA: attributes.Schema(
            _('NETWORK_IPAM_REFS_DATA.'),
        ),
        INTENT_MAP_REFS: attributes.Schema(
            _('INTENT_MAP_REFS.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.VirtualNetwork(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.VIRTUAL_NETWORK_NETWORK_ID) is not None:
            obj_0.set_virtual_network_network_id(self.properties.get(self.VIRTUAL_NETWORK_NETWORK_ID))
        if self.properties.get(self.ADDRESS_ALLOCATION_MODE) is not None:
            obj_0.set_address_allocation_mode(self.properties.get(self.ADDRESS_ALLOCATION_MODE))
        if self.properties.get(self.IGMP_ENABLE) is not None:
            obj_0.set_igmp_enable(self.properties.get(self.IGMP_ENABLE))
        if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS) is not None:
            obj_1 = vnc_api.FatFlowProtocols()
            if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL))):
                    obj_2 = vnc_api.ProtocolType()
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL))
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT) is not None:
                        obj_2.set_port(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT))
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS) is not None:
                        obj_2.set_ignore_address(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS))
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX))
                        if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_source_prefix(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH) is not None:
                        obj_2.set_source_aggregate_prefix_length(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH))
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX))
                        if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_destination_prefix(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH) is not None:
                        obj_2.set_destination_aggregate_prefix_length(self.properties.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH))
                    obj_1.add_fat_flow_protocol(obj_2)
            obj_0.set_virtual_network_fat_flow_protocols(obj_1)
        if self.properties.get(self.ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_route_target_list(obj_1)
        if self.properties.get(self.MAC_LEARNING_ENABLED) is not None:
            obj_0.set_mac_learning_enabled(self.properties.get(self.MAC_LEARNING_ENABLED))
        if self.properties.get(self.PORT_SECURITY_ENABLED) is not None:
            obj_0.set_port_security_enabled(self.properties.get(self.PORT_SECURITY_ENABLED))
        if self.properties.get(self.FABRIC_SNAT) is not None:
            obj_0.set_fabric_snat(self.properties.get(self.FABRIC_SNAT))
        if self.properties.get(self.PBB_ETREE_ENABLE) is not None:
            obj_0.set_pbb_etree_enable(self.properties.get(self.PBB_ETREE_ENABLE))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkRoutedPropertiesType()
            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES))):
                    obj_2 = vnc_api.RoutedProperties()
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID) is not None:
                        obj_2.set_physical_router_uuid(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID))
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID) is not None:
                        obj_2.set_logical_router_uuid(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID))
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS) is not None:
                        obj_2.set_routed_interface_ip_address(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS))
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS) is not None:
                        obj_2.set_loopback_ip_address(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS))
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL) is not None:
                        obj_2.set_routing_protocol(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL))
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS) is not None:
                        obj_3 = vnc_api.BgpParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM) is not None:
                            obj_3.set_peer_autonomous_system(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS) is not None:
                            obj_3.set_peer_ip_address(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST))):
                                obj_3.add_peer_ip_address_list(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST)[index_3])
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME) is not None:
                            obj_3.set_hold_time(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA) is not None:
                            obj_4 = vnc_api.AuthenticationData()
                            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE) is not None:
                                obj_4.set_key_type(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE))
                            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS) is not None:
                                for index_4 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS))):
                                    obj_5 = vnc_api.AuthenticationKeyItem()
                                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                        obj_5.set_key_id(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                        obj_5.set_key(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY))
                                    obj_4.add_key_items(obj_5)
                            obj_3.set_auth_data(obj_4)
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                            obj_3.set_local_autonomous_system(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL) is not None:
                            obj_3.set_multihop_ttl(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL))
                        obj_2.set_bgp_params(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS) is not None:
                        obj_3 = vnc_api.OspfParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA) is not None:
                            obj_4 = vnc_api.AuthenticationData()
                            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE) is not None:
                                obj_4.set_key_type(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE))
                            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS) is not None:
                                for index_4 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS))):
                                    obj_5 = vnc_api.AuthenticationKeyItem()
                                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                        obj_5.set_key_id(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                        obj_5.set_key(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY))
                                    obj_4.add_key_items(obj_5)
                            obj_3.set_auth_data(obj_4)
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL) is not None:
                            obj_3.set_hello_interval(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL) is not None:
                            obj_3.set_dead_interval(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID) is not None:
                            obj_3.set_area_id(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE) is not None:
                            obj_3.set_area_type(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK) is not None:
                            obj_3.set_advertise_loopback(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA) is not None:
                            obj_3.set_orignate_summary_lsa(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA))
                        obj_2.set_ospf_params(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS) is not None:
                        obj_3 = vnc_api.PimParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS))):
                                obj_3.add_rp_ip_address(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS)[index_3])
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE) is not None:
                            obj_3.set_mode(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES) is not None:
                            obj_3.set_enable_all_interfaces(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES))
                        obj_2.set_pim_params(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS) is not None:
                        obj_3 = vnc_api.StaticRouteParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID))):
                                obj_3.add_interface_route_table_uuid(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID)[index_3])
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS))):
                                obj_3.add_next_hop_ip_address(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS)[index_3])
                        obj_2.set_static_route_params(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS) is not None:
                        obj_3 = vnc_api.BfdParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL) is not None:
                            obj_3.set_time_interval(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL))
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER) is not None:
                            obj_3.set_detection_time_multiplier(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER))
                        obj_2.set_bfd_params(obj_3)
                    if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS) is not None:
                        obj_3 = vnc_api.RoutingPolicyParameters()
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID))):
                                obj_3.add_import_routing_policy_uuid(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID)[index_3])
                        if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID))):
                                obj_3.add_export_routing_policy_uuid(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID)[index_3])
                        obj_2.set_routing_policy_params(obj_3)
                    obj_1.add_routed_properties(obj_2)
            if self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS) is not None:
                obj_1.set_shared_across_all_lrs(self.properties.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS))
            obj_0.set_virtual_network_routed_properties(obj_1)
        if self.properties.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(self.properties.get(self.MAC_AGING_TIME))
        if self.properties.get(self.ID_PERMS) is not None:
            obj_1 = vnc_api.IdPermsType()
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS) is not None:
                obj_2 = vnc_api.PermType()
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OWNER) is not None:
                    obj_2.set_owner(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OWNER))
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OWNER_ACCESS) is not None:
                    obj_2.set_owner_access(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OWNER_ACCESS))
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_GROUP) is not None:
                    obj_2.set_group(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_GROUP))
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_GROUP_ACCESS) is not None:
                    obj_2.set_group_access(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_GROUP_ACCESS))
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OTHER_ACCESS) is not None:
                    obj_2.set_other_access(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_PERMISSIONS, {}).get(self.ID_PERMS_PERMISSIONS_OTHER_ACCESS))
                obj_1.set_permissions(obj_2)
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_UUID) is not None:
                obj_2 = vnc_api.UuidType()
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_UUID, {}).get(self.ID_PERMS_UUID_UUID_MSLONG) is not None:
                    obj_2.set_uuid_mslong(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_UUID, {}).get(self.ID_PERMS_UUID_UUID_MSLONG))
                if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_UUID, {}).get(self.ID_PERMS_UUID_UUID_LSLONG) is not None:
                    obj_2.set_uuid_lslong(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_UUID, {}).get(self.ID_PERMS_UUID_UUID_LSLONG))
                obj_1.set_uuid(obj_2)
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_ENABLE) is not None:
                obj_1.set_enable(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_ENABLE))
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_CREATED) is not None:
                obj_1.set_created(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_CREATED))
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_LAST_MODIFIED) is not None:
                obj_1.set_last_modified(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_LAST_MODIFIED))
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_DESCRIPTION) is not None:
                obj_1.set_description(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_DESCRIPTION))
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_USER_VISIBLE) is not None:
                obj_1.set_user_visible(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_USER_VISIBLE))
            if self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_CREATOR) is not None:
                obj_1.set_creator(self.properties.get(self.ID_PERMS, {}).get(self.ID_PERMS_CREATOR))
            obj_0.set_id_perms(obj_1)
        if self.properties.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED) is not None:
            obj_0.set_multi_policy_service_chains_enabled(self.properties.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED))
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if self.properties.get(self.MAC_LIMIT_CONTROL) is not None:
            obj_1 = vnc_api.MACLimitControlType()
            if self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT) is not None:
                obj_1.set_mac_limit(self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT))
            if self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION) is not None:
                obj_1.set_mac_limit_action(self.properties.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION))
            obj_0.set_mac_limit_control(obj_1)
        if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkType()
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT) is not None:
                obj_1.set_allow_transit(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID) is not None:
                obj_1.set_network_id(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER) is not None:
                obj_1.set_vxlan_network_identifier(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE) is not None:
                obj_1.set_forwarding_mode(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF) is not None:
                obj_1.set_rpf(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION) is not None:
                obj_1.set_mirror_destination(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS) is not None:
                obj_1.set_max_flows(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS))
            obj_0.set_virtual_network_properties(obj_1)
        if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS) is not None:
            obj_1 = vnc_api.EcmpHashingIncludeFields()
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED) is not None:
                obj_1.set_hashing_configured(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP) is not None:
                obj_1.set_source_ip(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP) is not None:
                obj_1.set_destination_ip(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL) is not None:
                obj_1.set_ip_protocol(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT) is not None:
                obj_1.set_source_port(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT) is not None:
                obj_1.set_destination_port(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT))
            obj_0.set_ecmp_hashing_include_fields(obj_1)
        if self.properties.get(self.PROVIDER_PROPERTIES) is not None:
            obj_1 = vnc_api.ProviderDetails()
            if self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID) is not None:
                obj_1.set_segmentation_id(self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID))
            if self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK) is not None:
                obj_1.set_physical_network(self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK))
            obj_0.set_provider_properties(obj_1)
        if self.properties.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)
        if self.properties.get(self.IS_SHARED) is not None:
            obj_0.set_is_shared(self.properties.get(self.IS_SHARED))
        if self.properties.get(self.VIRTUAL_NETWORK_CATEGORY) is not None:
            obj_0.set_virtual_network_category(self.properties.get(self.VIRTUAL_NETWORK_CATEGORY))
        if self.properties.get(self.IMPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_import_route_target_list(obj_1)
        if self.properties.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if self.properties.get(self.ROUTER_EXTERNAL) is not None:
            obj_0.set_router_external(self.properties.get(self.ROUTER_EXTERNAL))
        if self.properties.get(self.IS_PROVIDER_NETWORK) is not None:
            obj_0.set_is_provider_network(self.properties.get(self.IS_PROVIDER_NETWORK))
        if self.properties.get(self.PBB_EVPN_ENABLE) is not None:
            obj_0.set_pbb_evpn_enable(self.properties.get(self.PBB_EVPN_ENABLE))
        if self.properties.get(self.EXPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_export_route_target_list(obj_1)
        if self.properties.get(self.FLOOD_UNKNOWN_UNICAST) is not None:
            obj_0.set_flood_unknown_unicast(self.properties.get(self.FLOOD_UNKNOWN_UNICAST))
        if self.properties.get(self.LAYER2_CONTROL_WORD) is not None:
            obj_0.set_layer2_control_word(self.properties.get(self.LAYER2_CONTROL_WORD))
        if self.properties.get(self.EXTERNAL_IPAM) is not None:
            obj_0.set_external_ipam(self.properties.get(self.EXTERNAL_IPAM))

        # reference to routing_policy_refs
        if len(self.properties.get(self.ROUTING_POLICY_REFS) or []) != len(self.properties.get(self.ROUTING_POLICY_REFS_DATA) or []):
            raise Exception(_('virtual-network: specify routing_policy_refs for each routing_policy_refs_data.'))
        obj_1 = None
        if self.properties.get(self.ROUTING_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTING_POLICY_REFS_DATA))):
                obj_1 = vnc_api.RoutingPolicyType()
                if self.properties.get(self.ROUTING_POLICY_REFS_DATA, {})[index_0].get(self.ROUTING_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_1.set_sequence(self.properties.get(self.ROUTING_POLICY_REFS_DATA, {})[index_0].get(self.ROUTING_POLICY_REFS_DATA_SEQUENCE))

                if self.properties.get(self.ROUTING_POLICY_REFS):
                    try:
                        ref_obj = self.vnc_lib().routing_policy_read(
                            id=self.properties.get(self.ROUTING_POLICY_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().routing_policy_read(
                            fq_name_str=self.properties.get(self.ROUTING_POLICY_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_routing_policy(ref_obj, obj_1)

        # reference to security_logging_object_refs
        if self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS):
            for index_0 in range(len(self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS))):
                try:
                    ref_obj = self.vnc_lib().security_logging_object_read(
                        id=self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().security_logging_object_read(
                        fq_name_str=self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_security_logging_object(ref_obj)

        # reference to network_policy_refs
        if len(self.properties.get(self.NETWORK_POLICY_REFS) or []) != len(self.properties.get(self.NETWORK_POLICY_REFS_DATA) or []):
            raise Exception(_('virtual-network: specify network_policy_refs for each network_policy_refs_data.'))
        obj_1 = None
        if self.properties.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.VirtualNetworkPolicyType()
                if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_2 = vnc_api.SequenceType()
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR) is not None:
                        obj_2.set_major(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR) is not None:
                        obj_2.set_minor(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR))
                    obj_1.set_sequence(obj_2)
                if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER) is not None:
                    obj_2 = vnc_api.TimerType()
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME) is not None:
                        obj_2.set_start_time(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL) is not None:
                        obj_2.set_on_interval(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL) is not None:
                        obj_2.set_off_interval(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME) is not None:
                        obj_2.set_end_time(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME))
                    obj_1.set_timer(obj_2)

                if self.properties.get(self.NETWORK_POLICY_REFS):
                    try:
                        ref_obj = self.vnc_lib().network_policy_read(
                            id=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().network_policy_read(
                            fq_name_str=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_network_policy(ref_obj, obj_1)

        # reference to qos_config_refs
        if self.properties.get(self.QOS_CONFIG_REFS):
            for index_0 in range(len(self.properties.get(self.QOS_CONFIG_REFS))):
                try:
                    ref_obj = self.vnc_lib().qos_config_read(
                        id=self.properties.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().qos_config_read(
                        fq_name_str=self.properties.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_qos_config(ref_obj)

        # reference to virtual_network_refs
        if self.properties.get(self.VIRTUAL_NETWORK_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_NETWORK_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_virtual_network(ref_obj)

        # reference to tag_refs
        if self.properties.get(self.TAG_REFS):
            for index_0 in range(len(self.properties.get(self.TAG_REFS))):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_tag(ref_obj)

        # reference to route_table_refs
        if self.properties.get(self.ROUTE_TABLE_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTE_TABLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_route_table(ref_obj)

        # reference to bgpvpn_refs
        if self.properties.get(self.BGPVPN_REFS):
            for index_0 in range(len(self.properties.get(self.BGPVPN_REFS))):
                try:
                    ref_obj = self.vnc_lib().bgpvpn_read(
                        id=self.properties.get(self.BGPVPN_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().bgpvpn_read(
                        fq_name_str=self.properties.get(self.BGPVPN_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_bgpvpn(ref_obj)

        # reference to multicast_policy_refs
        if self.properties.get(self.MULTICAST_POLICY_REFS):
            for index_0 in range(len(self.properties.get(self.MULTICAST_POLICY_REFS))):
                try:
                    ref_obj = self.vnc_lib().multicast_policy_read(
                        id=self.properties.get(self.MULTICAST_POLICY_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().multicast_policy_read(
                        fq_name_str=self.properties.get(self.MULTICAST_POLICY_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_multicast_policy(ref_obj)

        # reference to network_ipam_refs
        if len(self.properties.get(self.NETWORK_IPAM_REFS) or []) != len(self.properties.get(self.NETWORK_IPAM_REFS_DATA) or []):
            raise Exception(_('virtual-network: specify network_ipam_refs for each network_ipam_refs_data.'))
        obj_1 = None
        if self.properties.get(self.NETWORK_IPAM_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA))):
                obj_1 = vnc_api.VnSubnetsType()
                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS) is not None:
                    for index_1 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS))):
                        obj_2 = vnc_api.IpamSubnetType()
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET) is not None:
                            obj_3 = vnc_api.SubnetType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX) is not None:
                                obj_3.set_ip_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                                obj_3.set_ip_prefix_len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN))
                            obj_2.set_subnet(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY) is not None:
                            obj_2.set_default_gateway(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                            obj_2.set_dns_server_address(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID) is not None:
                            obj_2.set_subnet_uuid(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP) is not None:
                            obj_2.set_enable_dhcp(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS) is not None:
                            for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS))):
                                obj_2.add_dns_nameservers(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS)[index_2])
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS) is not None:
                            for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS))):
                                obj_3 = vnc_api.AllocationPoolType()
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                    obj_3.set_start(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START))
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                    obj_3.set_end(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END))
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL) is not None:
                                    obj_3.set_vrouter_specific_pool(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL))
                                obj_2.add_allocation_pools(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START) is not None:
                            obj_2.set_addr_from_start(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST) is not None:
                            obj_3 = vnc_api.DhcpOptionsListType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                    obj_4 = vnc_api.DhcpOptionType()
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                        obj_4.set_dhcp_option_name(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                        obj_4.set_dhcp_option_value(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                        obj_4.set_dhcp_option_value_bytes(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                    obj_3.add_dhcp_option(obj_4)
                            obj_2.set_dhcp_option_list(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES) is not None:
                            obj_3 = vnc_api.RouteTableType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE))):
                                    obj_4 = vnc_api.RouteType()
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                        obj_4.set_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                        obj_4.set_next_hop(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                        obj_4.set_next_hop_type(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                        obj_5 = vnc_api.CommunityAttributes()
                                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                            for index_5 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                                obj_5.add_community_attribute(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                        obj_4.set_community_attributes(obj_5)
                                    obj_3.add_route(obj_4)
                            obj_2.set_host_routes(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME) is not None:
                            obj_2.set_subnet_name(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT) is not None:
                            obj_2.set_alloc_unit(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED) is not None:
                            obj_2.set_created(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED) is not None:
                            obj_2.set_last_modified(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG) is not None:
                            obj_2.set_subscriber_tag(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG) is not None:
                            obj_2.set_vlan_tag(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER) is not None:
                            for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER))):
                                obj_2.add_dhcp_relay_server(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER)[index_2])
                        obj_1.add_ipam_subnets(obj_2)
                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES) is not None:
                    obj_2 = vnc_api.RouteTableType()
                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE))):
                            obj_3 = vnc_api.RouteType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                obj_3.set_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                obj_3.set_next_hop(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                obj_3.set_next_hop_type(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                obj_4 = vnc_api.CommunityAttributes()
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                    for index_4 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                        obj_4.add_community_attribute(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                                obj_3.set_community_attributes(obj_4)
                            obj_2.add_route(obj_3)
                    obj_1.set_host_routes(obj_2)

                if self.properties.get(self.NETWORK_IPAM_REFS):
                    try:
                        ref_obj = self.vnc_lib().network_ipam_read(
                            id=self.properties.get(self.NETWORK_IPAM_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().network_ipam_read(
                            fq_name_str=self.properties.get(self.NETWORK_IPAM_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_network_ipam(ref_obj, obj_1)

        # reference to intent_map_refs
        if self.properties.get(self.INTENT_MAP_REFS):
            for index_0 in range(len(self.properties.get(self.INTENT_MAP_REFS))):
                try:
                    ref_obj = self.vnc_lib().intent_map_read(
                        id=self.properties.get(self.INTENT_MAP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().intent_map_read(
                        fq_name_str=self.properties.get(self.INTENT_MAP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_intent_map(ref_obj)

        try:
            obj_uuid = super(ContrailVirtualNetwork, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_network_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.ADDRESS_ALLOCATION_MODE) is not None:
            obj_0.set_address_allocation_mode(prop_diff.get(self.ADDRESS_ALLOCATION_MODE))
        if prop_diff.get(self.IGMP_ENABLE) is not None:
            obj_0.set_igmp_enable(prop_diff.get(self.IGMP_ENABLE))
        if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS) is not None:
            obj_1 = vnc_api.FatFlowProtocols()
            if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL))):
                    obj_2 = vnc_api.ProtocolType()
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL))
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT) is not None:
                        obj_2.set_port(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT))
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS) is not None:
                        obj_2.set_ignore_address(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_IGNORE_ADDRESS))
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX))
                        if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_source_prefix(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH) is not None:
                        obj_2.set_source_aggregate_prefix_length(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_SOURCE_AGGREGATE_PREFIX_LENGTH))
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX))
                        if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_destination_prefix(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH) is not None:
                        obj_2.set_destination_aggregate_prefix_length(prop_diff.get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_NETWORK_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_DESTINATION_AGGREGATE_PREFIX_LENGTH))
                    obj_1.add_fat_flow_protocol(obj_2)
            obj_0.set_virtual_network_fat_flow_protocols(obj_1)
        if prop_diff.get(self.ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_route_target_list(obj_1)
        if prop_diff.get(self.MAC_LEARNING_ENABLED) is not None:
            obj_0.set_mac_learning_enabled(prop_diff.get(self.MAC_LEARNING_ENABLED))
        if prop_diff.get(self.PORT_SECURITY_ENABLED) is not None:
            obj_0.set_port_security_enabled(prop_diff.get(self.PORT_SECURITY_ENABLED))
        if prop_diff.get(self.FABRIC_SNAT) is not None:
            obj_0.set_fabric_snat(prop_diff.get(self.FABRIC_SNAT))
        if prop_diff.get(self.PBB_ETREE_ENABLE) is not None:
            obj_0.set_pbb_etree_enable(prop_diff.get(self.PBB_ETREE_ENABLE))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkRoutedPropertiesType()
            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES))):
                    obj_2 = vnc_api.RoutedProperties()
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID) is not None:
                        obj_2.set_physical_router_uuid(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PHYSICAL_ROUTER_UUID))
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID) is not None:
                        obj_2.set_logical_router_uuid(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOGICAL_ROUTER_UUID))
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS) is not None:
                        obj_2.set_routed_interface_ip_address(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTED_INTERFACE_IP_ADDRESS))
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS) is not None:
                        obj_2.set_loopback_ip_address(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_LOOPBACK_IP_ADDRESS))
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL) is not None:
                        obj_2.set_routing_protocol(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_PROTOCOL))
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS) is not None:
                        obj_3 = vnc_api.BgpParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM) is not None:
                            obj_3.set_peer_autonomous_system(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_AUTONOMOUS_SYSTEM))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS) is not None:
                            obj_3.set_peer_ip_address(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST))):
                                obj_3.add_peer_ip_address_list(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_PEER_IP_ADDRESS_LIST)[index_3])
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME) is not None:
                            obj_3.set_hold_time(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_HOLD_TIME))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA) is not None:
                            obj_4 = vnc_api.AuthenticationData()
                            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE) is not None:
                                obj_4.set_key_type(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_TYPE))
                            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS) is not None:
                                for index_4 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS))):
                                    obj_5 = vnc_api.AuthenticationKeyItem()
                                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                        obj_5.set_key_id(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                        obj_5.set_key(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_AUTH_DATA_KEY_ITEMS_KEY))
                                    obj_4.add_key_items(obj_5)
                            obj_3.set_auth_data(obj_4)
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                            obj_3.set_local_autonomous_system(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_LOCAL_AUTONOMOUS_SYSTEM))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL) is not None:
                            obj_3.set_multihop_ttl(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BGP_PARAMS_MULTIHOP_TTL))
                        obj_2.set_bgp_params(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS) is not None:
                        obj_3 = vnc_api.OspfParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA) is not None:
                            obj_4 = vnc_api.AuthenticationData()
                            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE) is not None:
                                obj_4.set_key_type(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_TYPE))
                            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS) is not None:
                                for index_4 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS))):
                                    obj_5 = vnc_api.AuthenticationKeyItem()
                                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                        obj_5.set_key_id(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                        obj_5.set_key(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AUTH_DATA_KEY_ITEMS_KEY))
                                    obj_4.add_key_items(obj_5)
                            obj_3.set_auth_data(obj_4)
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL) is not None:
                            obj_3.set_hello_interval(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_HELLO_INTERVAL))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL) is not None:
                            obj_3.set_dead_interval(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_DEAD_INTERVAL))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID) is not None:
                            obj_3.set_area_id(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_ID))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE) is not None:
                            obj_3.set_area_type(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_AREA_TYPE))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK) is not None:
                            obj_3.set_advertise_loopback(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ADVERTISE_LOOPBACK))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA) is not None:
                            obj_3.set_orignate_summary_lsa(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_OSPF_PARAMS_ORIGNATE_SUMMARY_LSA))
                        obj_2.set_ospf_params(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS) is not None:
                        obj_3 = vnc_api.PimParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS))):
                                obj_3.add_rp_ip_address(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_RP_IP_ADDRESS)[index_3])
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE) is not None:
                            obj_3.set_mode(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_MODE))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES) is not None:
                            obj_3.set_enable_all_interfaces(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_PIM_PARAMS_ENABLE_ALL_INTERFACES))
                        obj_2.set_pim_params(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS) is not None:
                        obj_3 = vnc_api.StaticRouteParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID))):
                                obj_3.add_interface_route_table_uuid(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_INTERFACE_ROUTE_TABLE_UUID)[index_3])
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS))):
                                obj_3.add_next_hop_ip_address(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_STATIC_ROUTE_PARAMS_NEXT_HOP_IP_ADDRESS)[index_3])
                        obj_2.set_static_route_params(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS) is not None:
                        obj_3 = vnc_api.BfdParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL) is not None:
                            obj_3.set_time_interval(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_TIME_INTERVAL))
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER) is not None:
                            obj_3.set_detection_time_multiplier(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_BFD_PARAMS_DETECTION_TIME_MULTIPLIER))
                        obj_2.set_bfd_params(obj_3)
                    if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS) is not None:
                        obj_3 = vnc_api.RoutingPolicyParameters()
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID))):
                                obj_3.add_import_routing_policy_uuid(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_IMPORT_ROUTING_POLICY_UUID)[index_3])
                        if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID))):
                                obj_3.add_export_routing_policy_uuid(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES, {})[index_1].get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_ROUTED_PROPERTIES_ROUTING_POLICY_PARAMS_EXPORT_ROUTING_POLICY_UUID)[index_3])
                        obj_2.set_routing_policy_params(obj_3)
                    obj_1.add_routed_properties(obj_2)
            if prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS) is not None:
                obj_1.set_shared_across_all_lrs(prop_diff.get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_ROUTED_PROPERTIES_SHARED_ACROSS_ALL_LRS))
            obj_0.set_virtual_network_routed_properties(obj_1)
        if prop_diff.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(prop_diff.get(self.MAC_AGING_TIME))
        if prop_diff.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED) is not None:
            obj_0.set_multi_policy_service_chains_enabled(prop_diff.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED))
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if prop_diff.get(self.MAC_LIMIT_CONTROL) is not None:
            obj_1 = vnc_api.MACLimitControlType()
            if prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT) is not None:
                obj_1.set_mac_limit(prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT))
            if prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION) is not None:
                obj_1.set_mac_limit_action(prop_diff.get(self.MAC_LIMIT_CONTROL, {}).get(self.MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION))
            obj_0.set_mac_limit_control(obj_1)
        if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkType()
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT) is not None:
                obj_1.set_allow_transit(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID) is not None:
                obj_1.set_network_id(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER) is not None:
                obj_1.set_vxlan_network_identifier(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE) is not None:
                obj_1.set_forwarding_mode(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF) is not None:
                obj_1.set_rpf(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION) is not None:
                obj_1.set_mirror_destination(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MIRROR_DESTINATION))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS) is not None:
                obj_1.set_max_flows(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_MAX_FLOWS))
            obj_0.set_virtual_network_properties(obj_1)
        if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS) is not None:
            obj_1 = vnc_api.EcmpHashingIncludeFields()
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED) is not None:
                obj_1.set_hashing_configured(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP) is not None:
                obj_1.set_source_ip(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP) is not None:
                obj_1.set_destination_ip(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL) is not None:
                obj_1.set_ip_protocol(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT) is not None:
                obj_1.set_source_port(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT) is not None:
                obj_1.set_destination_port(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT))
            obj_0.set_ecmp_hashing_include_fields(obj_1)
        if prop_diff.get(self.IS_SHARED) is not None:
            obj_0.set_is_shared(prop_diff.get(self.IS_SHARED))
        if prop_diff.get(self.VIRTUAL_NETWORK_CATEGORY) is not None:
            obj_0.set_virtual_network_category(prop_diff.get(self.VIRTUAL_NETWORK_CATEGORY))
        if prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_import_route_target_list(obj_1)
        if prop_diff.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if prop_diff.get(self.ROUTER_EXTERNAL) is not None:
            obj_0.set_router_external(prop_diff.get(self.ROUTER_EXTERNAL))
        if prop_diff.get(self.PBB_EVPN_ENABLE) is not None:
            obj_0.set_pbb_evpn_enable(prop_diff.get(self.PBB_EVPN_ENABLE))
        if prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_export_route_target_list(obj_1)
        if prop_diff.get(self.FLOOD_UNKNOWN_UNICAST) is not None:
            obj_0.set_flood_unknown_unicast(prop_diff.get(self.FLOOD_UNKNOWN_UNICAST))
        if prop_diff.get(self.LAYER2_CONTROL_WORD) is not None:
            obj_0.set_layer2_control_word(prop_diff.get(self.LAYER2_CONTROL_WORD))
        if prop_diff.get(self.EXTERNAL_IPAM) is not None:
            obj_0.set_external_ipam(prop_diff.get(self.EXTERNAL_IPAM))

        # reference to routing_policy
        update = 0
        if not self.ROUTING_POLICY_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_routing_policy_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.ROUTING_POLICY_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_routing_policy_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.ROUTING_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTING_POLICY_REFS_DATA))):
                obj_1 = vnc_api.RoutingPolicyType()
                if prop_diff.get(self.ROUTING_POLICY_REFS_DATA, {})[index_0].get(self.ROUTING_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_1.set_sequence(prop_diff.get(self.ROUTING_POLICY_REFS_DATA, {})[index_0].get(self.ROUTING_POLICY_REFS_DATA_SEQUENCE))
                ref_data_list.append(obj_1)
        if self.ROUTING_POLICY_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTING_POLICY_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().routing_policy_read(
                        id=prop_diff.get(self.ROUTING_POLICY_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().routing_policy_read(
                        fq_name_str=prop_diff.get(self.ROUTING_POLICY_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('virtual-network: specify routing_policy_refs_data for each routing_policy_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_routing_policy_list(ref_obj_list, ref_data_list)
        # End: reference to routing_policy_refs

        # reference to security_logging_object_refs
        ref_obj_list = []
        if self.SECURITY_LOGGING_OBJECT_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().security_logging_object_read(
                        id=prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().security_logging_object_read(
                        fq_name_str=prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_security_logging_object_list(ref_obj_list)
            # End: reference to security_logging_object_refs

        # reference to network_policy
        update = 0
        if not self.NETWORK_POLICY_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_network_policy_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.NETWORK_POLICY_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_network_policy_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.VirtualNetworkPolicyType()
                if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_2 = vnc_api.SequenceType()
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR) is not None:
                        obj_2.set_major(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR) is not None:
                        obj_2.set_minor(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR))
                    obj_1.set_sequence(obj_2)
                if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER) is not None:
                    obj_2 = vnc_api.TimerType()
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME) is not None:
                        obj_2.set_start_time(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL) is not None:
                        obj_2.set_on_interval(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL) is not None:
                        obj_2.set_off_interval(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME) is not None:
                        obj_2.set_end_time(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME))
                    obj_1.set_timer(obj_2)
                ref_data_list.append(obj_1)
        if self.NETWORK_POLICY_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().network_policy_read(
                        id=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().network_policy_read(
                        fq_name_str=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('virtual-network: specify network_policy_refs_data for each network_policy_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_network_policy_list(ref_obj_list, ref_data_list)
        # End: reference to network_policy_refs

        # reference to qos_config_refs
        ref_obj_list = []
        if self.QOS_CONFIG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.QOS_CONFIG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().qos_config_read(
                        id=prop_diff.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().qos_config_read(
                        fq_name_str=prop_diff.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_qos_config_list(ref_obj_list)
            # End: reference to qos_config_refs

        # reference to virtual_network_refs
        ref_obj_list = []
        if self.VIRTUAL_NETWORK_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_network_list(ref_obj_list)
            # End: reference to virtual_network_refs

        # reference to tag_refs
        ref_obj_list = []
        if self.TAG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TAG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_tag_list(ref_obj_list)
            # End: reference to tag_refs

        # reference to route_table_refs
        ref_obj_list = []
        if self.ROUTE_TABLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TABLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_route_table_list(ref_obj_list)
            # End: reference to route_table_refs

        # reference to bgpvpn_refs
        ref_obj_list = []
        if self.BGPVPN_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.BGPVPN_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().bgpvpn_read(
                        id=prop_diff.get(self.BGPVPN_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().bgpvpn_read(
                        fq_name_str=prop_diff.get(self.BGPVPN_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_bgpvpn_list(ref_obj_list)
            # End: reference to bgpvpn_refs

        # reference to multicast_policy_refs
        ref_obj_list = []
        if self.MULTICAST_POLICY_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.MULTICAST_POLICY_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().multicast_policy_read(
                        id=prop_diff.get(self.MULTICAST_POLICY_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().multicast_policy_read(
                        fq_name_str=prop_diff.get(self.MULTICAST_POLICY_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_multicast_policy_list(ref_obj_list)
            # End: reference to multicast_policy_refs

        # reference to network_ipam
        update = 0
        if not self.NETWORK_IPAM_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_network_ipam_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.NETWORK_IPAM_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_network_ipam_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA))):
                obj_1 = vnc_api.VnSubnetsType()
                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS) is not None:
                    for index_1 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS))):
                        obj_2 = vnc_api.IpamSubnetType()
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET) is not None:
                            obj_3 = vnc_api.SubnetType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX) is not None:
                                obj_3.set_ip_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                                obj_3.set_ip_prefix_len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN))
                            obj_2.set_subnet(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY) is not None:
                            obj_2.set_default_gateway(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                            obj_2.set_dns_server_address(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID) is not None:
                            obj_2.set_subnet_uuid(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP) is not None:
                            obj_2.set_enable_dhcp(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS) is not None:
                            for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS))):
                                obj_2.add_dns_nameservers(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS)[index_2])
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS) is not None:
                            for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS))):
                                obj_3 = vnc_api.AllocationPoolType()
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                    obj_3.set_start(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START))
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                    obj_3.set_end(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END))
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL) is not None:
                                    obj_3.set_vrouter_specific_pool(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_VROUTER_SPECIFIC_POOL))
                                obj_2.add_allocation_pools(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START) is not None:
                            obj_2.set_addr_from_start(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST) is not None:
                            obj_3 = vnc_api.DhcpOptionsListType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                    obj_4 = vnc_api.DhcpOptionType()
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                        obj_4.set_dhcp_option_name(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                        obj_4.set_dhcp_option_value(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                        obj_4.set_dhcp_option_value_bytes(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                    obj_3.add_dhcp_option(obj_4)
                            obj_2.set_dhcp_option_list(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES) is not None:
                            obj_3 = vnc_api.RouteTableType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE))):
                                    obj_4 = vnc_api.RouteType()
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                        obj_4.set_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                        obj_4.set_next_hop(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                        obj_4.set_next_hop_type(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                        obj_5 = vnc_api.CommunityAttributes()
                                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                            for index_5 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                                obj_5.add_community_attribute(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                        obj_4.set_community_attributes(obj_5)
                                    obj_3.add_route(obj_4)
                            obj_2.set_host_routes(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME) is not None:
                            obj_2.set_subnet_name(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT) is not None:
                            obj_2.set_alloc_unit(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOC_UNIT))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED) is not None:
                            obj_2.set_created(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_CREATED))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED) is not None:
                            obj_2.set_last_modified(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_LAST_MODIFIED))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG) is not None:
                            obj_2.set_subscriber_tag(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBSCRIBER_TAG))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG) is not None:
                            obj_2.set_vlan_tag(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_VLAN_TAG))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER) is not None:
                            for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER))):
                                obj_2.add_dhcp_relay_server(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_RELAY_SERVER)[index_2])
                        obj_1.add_ipam_subnets(obj_2)
                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES) is not None:
                    obj_2 = vnc_api.RouteTableType()
                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE))):
                            obj_3 = vnc_api.RouteType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                obj_3.set_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                obj_3.set_next_hop(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                obj_3.set_next_hop_type(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                obj_4 = vnc_api.CommunityAttributes()
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                    for index_4 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                        obj_4.add_community_attribute(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                                obj_3.set_community_attributes(obj_4)
                            obj_2.add_route(obj_3)
                    obj_1.set_host_routes(obj_2)
                ref_data_list.append(obj_1)
        if self.NETWORK_IPAM_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().network_ipam_read(
                        id=prop_diff.get(self.NETWORK_IPAM_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().network_ipam_read(
                        fq_name_str=prop_diff.get(self.NETWORK_IPAM_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('virtual-network: specify network_ipam_refs_data for each network_ipam_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_network_ipam_list(ref_obj_list, ref_data_list)
        # End: reference to network_ipam_refs

        # reference to intent_map_refs
        ref_obj_list = []
        if self.INTENT_MAP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.INTENT_MAP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().intent_map_read(
                        id=prop_diff.get(self.INTENT_MAP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().intent_map_read(
                        fq_name_str=prop_diff.get(self.INTENT_MAP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_intent_map_list(ref_obj_list)
            # End: reference to intent_map_refs

        try:
            self.vnc_lib().virtual_network_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_network_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_network %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualNetwork': ContrailVirtualNetwork,
    }
