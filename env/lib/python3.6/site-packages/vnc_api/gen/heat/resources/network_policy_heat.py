
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


class ContrailNetworkPolicy(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, NETWORK_POLICY_ENTRIES, NETWORK_POLICY_ENTRIES_POLICY_RULE, NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR, NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR, NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID, NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION, NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT, NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT, NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT, NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION, NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE, NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE, NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED, NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TAG_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'network_policy_entries', 'network_policy_entries_policy_rule', 'network_policy_entries_policy_rule_rule_sequence', 'network_policy_entries_policy_rule_rule_sequence_major', 'network_policy_entries_policy_rule_rule_sequence_minor', 'network_policy_entries_policy_rule_rule_uuid', 'network_policy_entries_policy_rule_direction', 'network_policy_entries_policy_rule_protocol', 'network_policy_entries_policy_rule_src_addresses', 'network_policy_entries_policy_rule_src_addresses_subnet', 'network_policy_entries_policy_rule_src_addresses_subnet_ip_prefix', 'network_policy_entries_policy_rule_src_addresses_subnet_ip_prefix_len', 'network_policy_entries_policy_rule_src_addresses_virtual_network', 'network_policy_entries_policy_rule_src_addresses_security_group', 'network_policy_entries_policy_rule_src_addresses_network_policy', 'network_policy_entries_policy_rule_src_addresses_subnet_list', 'network_policy_entries_policy_rule_src_addresses_subnet_list_ip_prefix', 'network_policy_entries_policy_rule_src_addresses_subnet_list_ip_prefix_len', 'network_policy_entries_policy_rule_src_ports', 'network_policy_entries_policy_rule_src_ports_start_port', 'network_policy_entries_policy_rule_src_ports_end_port', 'network_policy_entries_policy_rule_application', 'network_policy_entries_policy_rule_dst_addresses', 'network_policy_entries_policy_rule_dst_addresses_subnet', 'network_policy_entries_policy_rule_dst_addresses_subnet_ip_prefix', 'network_policy_entries_policy_rule_dst_addresses_subnet_ip_prefix_len', 'network_policy_entries_policy_rule_dst_addresses_virtual_network', 'network_policy_entries_policy_rule_dst_addresses_security_group', 'network_policy_entries_policy_rule_dst_addresses_network_policy', 'network_policy_entries_policy_rule_dst_addresses_subnet_list', 'network_policy_entries_policy_rule_dst_addresses_subnet_list_ip_prefix', 'network_policy_entries_policy_rule_dst_addresses_subnet_list_ip_prefix_len', 'network_policy_entries_policy_rule_dst_ports', 'network_policy_entries_policy_rule_dst_ports_start_port', 'network_policy_entries_policy_rule_dst_ports_end_port', 'network_policy_entries_policy_rule_action_list', 'network_policy_entries_policy_rule_action_list_simple_action', 'network_policy_entries_policy_rule_action_list_gateway_name', 'network_policy_entries_policy_rule_action_list_apply_service', 'network_policy_entries_policy_rule_action_list_mirror_to', 'network_policy_entries_policy_rule_action_list_mirror_to_analyzer_name', 'network_policy_entries_policy_rule_action_list_mirror_to_encapsulation', 'network_policy_entries_policy_rule_action_list_mirror_to_analyzer_ip_address', 'network_policy_entries_policy_rule_action_list_mirror_to_analyzer_mac_address', 'network_policy_entries_policy_rule_action_list_mirror_to_routing_instance', 'network_policy_entries_policy_rule_action_list_mirror_to_udp_port', 'network_policy_entries_policy_rule_action_list_mirror_to_juniper_header', 'network_policy_entries_policy_rule_action_list_mirror_to_nh_mode', 'network_policy_entries_policy_rule_action_list_mirror_to_static_nh_header', 'network_policy_entries_policy_rule_action_list_mirror_to_static_nh_header_vtep_dst_ip_address', 'network_policy_entries_policy_rule_action_list_mirror_to_static_nh_header_vtep_dst_mac_address', 'network_policy_entries_policy_rule_action_list_mirror_to_static_nh_header_vni', 'network_policy_entries_policy_rule_action_list_mirror_to_nic_assisted_mirroring', 'network_policy_entries_policy_rule_action_list_mirror_to_nic_assisted_mirroring_vlan', 'network_policy_entries_policy_rule_action_list_assign_routing_instance', 'network_policy_entries_policy_rule_action_list_log', 'network_policy_entries_policy_rule_action_list_alert', 'network_policy_entries_policy_rule_action_list_qos_action', 'network_policy_entries_policy_rule_action_list_host_based_service', 'network_policy_entries_policy_rule_ethertype', 'network_policy_entries_policy_rule_created', 'network_policy_entries_policy_rule_last_modified', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'tag_refs', 'project'
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
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
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
        NETWORK_POLICY_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('NETWORK_POLICY_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                NETWORK_POLICY_ENTRIES_POLICY_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('NETWORK_POLICY_ENTRIES_POLICY_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE: properties.Schema(
                                properties.Schema.MAP,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION: properties.Schema(
                                properties.Schema.STRING,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'>', u'<>']),
                                ],
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET: properties.Schema(
                                            properties.Schema.MAP,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET.'),
                                            update_allowed=True,
                                            required=False,
                                            schema={
                                                NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                    properties.Schema.INTEGER,
                                                    _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                            }
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            )
                                        ),
                                    }
                                )
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.Range(-1, 65535),
                                            ],
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.Range(-1, 65535),
                                            ],
                                        ),
                                    }
                                )
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET: properties.Schema(
                                            properties.Schema.MAP,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET.'),
                                            update_allowed=True,
                                            required=False,
                                            schema={
                                                NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                    properties.Schema.INTEGER,
                                                    _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                            }
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            )
                                        ),
                                    }
                                )
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.Range(-1, 65535),
                                            ],
                                        ),
                                        NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.Range(-1, 65535),
                                            ],
                                        ),
                                    }
                                )
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST: properties.Schema(
                                properties.Schema.MAP,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'deny', u'pass']),
                                        ],
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO: properties.Schema(
                                        properties.Schema.MAP,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.AllowedValues([u'dynamic', u'static']),
                                                ],
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER: properties.Schema(
                                                properties.Schema.MAP,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        constraints=[
                                                            constraints.Range(1, 16777215),
                                                        ],
                                                    ),
                                                }
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(0, 4094),
                                                ],
                                            ),
                                        }
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE: properties.Schema(
                                properties.Schema.STRING,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'IPv4', u'IPv6']),
                                ],
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
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
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        NETWORK_POLICY_ENTRIES: attributes.Schema(
            _('NETWORK_POLICY_ENTRIES.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
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

        obj_0 = vnc_api.NetworkPolicy(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
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
        if self.properties.get(self.NETWORK_POLICY_ENTRIES) is not None:
            obj_1 = vnc_api.PolicyEntriesType()
            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE))):
                    obj_2 = vnc_api.PolicyRuleType()
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE) is not None:
                        obj_3 = vnc_api.SequenceType()
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR) is not None:
                            obj_3.set_major(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR) is not None:
                            obj_3.set_minor(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR))
                        obj_2.set_rule_sequence(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID))
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION) is not None:
                        obj_2.set_direction(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION))
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL))
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES))):
                            obj_3 = vnc_api.AddressType()
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET) is not None:
                                obj_4 = vnc_api.SubnetType()
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX) is not None:
                                    obj_4.set_ip_prefix(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX))
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_4.set_ip_prefix_len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN))
                                obj_3.set_subnet(obj_4)
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK) is not None:
                                obj_3.set_virtual_network(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP) is not None:
                                obj_3.set_security_group(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY) is not None:
                                obj_3.set_network_policy(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST))):
                                    obj_4 = vnc_api.SubnetType()
                                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_4.set_ip_prefix(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_4.set_ip_prefix_len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_3.add_subnet_list(obj_4)
                            obj_2.add_src_addresses(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS))):
                            obj_3 = vnc_api.PortType()
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT) is not None:
                                obj_3.set_start_port(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT) is not None:
                                obj_3.set_end_port(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT))
                            obj_2.add_src_ports(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION))):
                            obj_2.add_application(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION)[index_2])
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES))):
                            obj_3 = vnc_api.AddressType()
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET) is not None:
                                obj_4 = vnc_api.SubnetType()
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX) is not None:
                                    obj_4.set_ip_prefix(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX))
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_4.set_ip_prefix_len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN))
                                obj_3.set_subnet(obj_4)
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK) is not None:
                                obj_3.set_virtual_network(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP) is not None:
                                obj_3.set_security_group(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY) is not None:
                                obj_3.set_network_policy(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST))):
                                    obj_4 = vnc_api.SubnetType()
                                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_4.set_ip_prefix(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_4.set_ip_prefix_len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_3.add_subnet_list(obj_4)
                            obj_2.add_dst_addresses(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS))):
                            obj_3 = vnc_api.PortType()
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT) is not None:
                                obj_3.set_start_port(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT) is not None:
                                obj_3.set_end_port(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT))
                            obj_2.add_dst_ports(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST) is not None:
                        obj_3 = vnc_api.ActionListType()
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION) is not None:
                            obj_3.set_simple_action(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME) is not None:
                            obj_3.set_gateway_name(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE) is not None:
                            for index_3 in range(len(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE))):
                                obj_3.add_apply_service(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE)[index_3])
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO) is not None:
                            obj_4 = vnc_api.MirrorActionType()
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                                obj_4.set_analyzer_name(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                                obj_4.set_encapsulation(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                                obj_4.set_analyzer_ip_address(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS) is not None:
                                obj_4.set_analyzer_mac_address(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                                obj_4.set_routing_instance(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                                obj_4.set_udp_port(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER) is not None:
                                obj_4.set_juniper_header(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE) is not None:
                                obj_4.set_nh_mode(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER) is not None:
                                obj_5 = vnc_api.StaticMirrorNhType()
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS) is not None:
                                    obj_5.set_vtep_dst_ip_address(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS))
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS) is not None:
                                    obj_5.set_vtep_dst_mac_address(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS))
                                if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI) is not None:
                                    obj_5.set_vni(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI))
                                obj_4.set_static_nh_header(obj_5)
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING) is not None:
                                obj_4.set_nic_assisted_mirroring(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING))
                            if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN) is not None:
                                obj_4.set_nic_assisted_mirroring_vlan(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN))
                            obj_3.set_mirror_to(obj_4)
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                            obj_3.set_assign_routing_instance(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG) is not None:
                            obj_3.set_log(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT) is not None:
                            obj_3.set_alert(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION) is not None:
                            obj_3.set_qos_action(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION))
                        if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE) is not None:
                            obj_3.set_host_based_service(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE))
                        obj_2.set_action_list(obj_3)
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE) is not None:
                        obj_2.set_ethertype(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE))
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED) is not None:
                        obj_2.set_created(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED))
                    if self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED) is not None:
                        obj_2.set_last_modified(self.properties.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED))
                    obj_1.add_policy_rule(obj_2)
            obj_0.set_network_policy_entries(obj_1)
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

        try:
            obj_uuid = super(ContrailNetworkPolicy, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().network_policy_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.NETWORK_POLICY_ENTRIES) is not None:
            obj_1 = vnc_api.PolicyEntriesType()
            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE))):
                    obj_2 = vnc_api.PolicyRuleType()
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE) is not None:
                        obj_3 = vnc_api.SequenceType()
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR) is not None:
                            obj_3.set_major(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MAJOR))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR) is not None:
                            obj_3.set_minor(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_SEQUENCE_MINOR))
                        obj_2.set_rule_sequence(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_RULE_UUID))
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION) is not None:
                        obj_2.set_direction(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DIRECTION))
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_PROTOCOL))
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES))):
                            obj_3 = vnc_api.AddressType()
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET) is not None:
                                obj_4 = vnc_api.SubnetType()
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX) is not None:
                                    obj_4.set_ip_prefix(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_4.set_ip_prefix_len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_IP_PREFIX_LEN))
                                obj_3.set_subnet(obj_4)
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK) is not None:
                                obj_3.set_virtual_network(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_VIRTUAL_NETWORK))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP) is not None:
                                obj_3.set_security_group(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SECURITY_GROUP))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY) is not None:
                                obj_3.set_network_policy(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_NETWORK_POLICY))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST))):
                                    obj_4 = vnc_api.SubnetType()
                                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_4.set_ip_prefix(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_4.set_ip_prefix_len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_3.add_subnet_list(obj_4)
                            obj_2.add_src_addresses(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS))):
                            obj_3 = vnc_api.PortType()
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT) is not None:
                                obj_3.set_start_port(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_START_PORT))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT) is not None:
                                obj_3.set_end_port(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_SRC_PORTS_END_PORT))
                            obj_2.add_src_ports(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION))):
                            obj_2.add_application(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_APPLICATION)[index_2])
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES))):
                            obj_3 = vnc_api.AddressType()
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET) is not None:
                                obj_4 = vnc_api.SubnetType()
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX) is not None:
                                    obj_4.set_ip_prefix(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_4.set_ip_prefix_len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_IP_PREFIX_LEN))
                                obj_3.set_subnet(obj_4)
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK) is not None:
                                obj_3.set_virtual_network(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_VIRTUAL_NETWORK))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP) is not None:
                                obj_3.set_security_group(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SECURITY_GROUP))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY) is not None:
                                obj_3.set_network_policy(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_NETWORK_POLICY))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST))):
                                    obj_4 = vnc_api.SubnetType()
                                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_4.set_ip_prefix(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_4.set_ip_prefix_len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST, {})[index_3].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_ADDRESSES_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_3.add_subnet_list(obj_4)
                            obj_2.add_dst_addresses(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS))):
                            obj_3 = vnc_api.PortType()
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT) is not None:
                                obj_3.set_start_port(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_START_PORT))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT) is not None:
                                obj_3.set_end_port(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS, {})[index_2].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_DST_PORTS_END_PORT))
                            obj_2.add_dst_ports(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST) is not None:
                        obj_3 = vnc_api.ActionListType()
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION) is not None:
                            obj_3.set_simple_action(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_SIMPLE_ACTION))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME) is not None:
                            obj_3.set_gateway_name(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_GATEWAY_NAME))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE) is not None:
                            for index_3 in range(len(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE))):
                                obj_3.add_apply_service(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_APPLY_SERVICE)[index_3])
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO) is not None:
                            obj_4 = vnc_api.MirrorActionType()
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                                obj_4.set_analyzer_name(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                                obj_4.set_encapsulation(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                                obj_4.set_analyzer_ip_address(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS) is not None:
                                obj_4.set_analyzer_mac_address(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                                obj_4.set_routing_instance(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                                obj_4.set_udp_port(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER) is not None:
                                obj_4.set_juniper_header(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_JUNIPER_HEADER))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE) is not None:
                                obj_4.set_nh_mode(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NH_MODE))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER) is not None:
                                obj_5 = vnc_api.StaticMirrorNhType()
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS) is not None:
                                    obj_5.set_vtep_dst_ip_address(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS))
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS) is not None:
                                    obj_5.set_vtep_dst_mac_address(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS))
                                if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI) is not None:
                                    obj_5.set_vni(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI))
                                obj_4.set_static_nh_header(obj_5)
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING) is not None:
                                obj_4.set_nic_assisted_mirroring(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING))
                            if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN) is not None:
                                obj_4.set_nic_assisted_mirroring_vlan(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN))
                            obj_3.set_mirror_to(obj_4)
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                            obj_3.set_assign_routing_instance(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG) is not None:
                            obj_3.set_log(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_LOG))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT) is not None:
                            obj_3.set_alert(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_ALERT))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION) is not None:
                            obj_3.set_qos_action(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_QOS_ACTION))
                        if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE) is not None:
                            obj_3.set_host_based_service(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ACTION_LIST_HOST_BASED_SERVICE))
                        obj_2.set_action_list(obj_3)
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE) is not None:
                        obj_2.set_ethertype(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_ETHERTYPE))
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED) is not None:
                        obj_2.set_created(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_CREATED))
                    if prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED) is not None:
                        obj_2.set_last_modified(prop_diff.get(self.NETWORK_POLICY_ENTRIES, {}).get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE, {})[index_1].get(self.NETWORK_POLICY_ENTRIES_POLICY_RULE_LAST_MODIFIED))
                    obj_1.add_policy_rule(obj_2)
            obj_0.set_network_policy_entries(obj_1)
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

        try:
            self.vnc_lib().network_policy_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().network_policy_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('network_policy %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().network_policy_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::NetworkPolicy': ContrailNetworkPolicy,
    }
