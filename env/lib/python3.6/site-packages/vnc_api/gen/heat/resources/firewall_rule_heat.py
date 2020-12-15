
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


class ContrailFirewallRule(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ENDPOINT_1, ENDPOINT_1_SUBNET, ENDPOINT_1_SUBNET_IP_PREFIX, ENDPOINT_1_SUBNET_IP_PREFIX_LEN, ENDPOINT_1_VIRTUAL_NETWORK, ENDPOINT_1_ADDRESS_GROUP, ENDPOINT_1_TAGS, ENDPOINT_1_TAG_IDS, ENDPOINT_1_ANY, ENDPOINT_2, ENDPOINT_2_SUBNET, ENDPOINT_2_SUBNET_IP_PREFIX, ENDPOINT_2_SUBNET_IP_PREFIX_LEN, ENDPOINT_2_VIRTUAL_NETWORK, ENDPOINT_2_ADDRESS_GROUP, ENDPOINT_2_TAGS, ENDPOINT_2_TAG_IDS, ENDPOINT_2_ANY, DISPLAY_NAME, ACTION_LIST, ACTION_LIST_SIMPLE_ACTION, ACTION_LIST_GATEWAY_NAME, ACTION_LIST_APPLY_SERVICE, ACTION_LIST_MIRROR_TO, ACTION_LIST_MIRROR_TO_ANALYZER_NAME, ACTION_LIST_MIRROR_TO_ENCAPSULATION, ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS, ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS, ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE, ACTION_LIST_MIRROR_TO_UDP_PORT, ACTION_LIST_MIRROR_TO_JUNIPER_HEADER, ACTION_LIST_MIRROR_TO_NH_MODE, ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS, ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS, ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI, ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING, ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN, ACTION_LIST_ASSIGN_ROUTING_INSTANCE, ACTION_LIST_LOG, ACTION_LIST_ALERT, ACTION_LIST_QOS_ACTION, ACTION_LIST_HOST_BASED_SERVICE, SERVICE, SERVICE_PROTOCOL, SERVICE_PROTOCOL_ID, SERVICE_SRC_PORTS, SERVICE_SRC_PORTS_START_PORT, SERVICE_SRC_PORTS_END_PORT, SERVICE_DST_PORTS, SERVICE_DST_PORTS_START_PORT, SERVICE_DST_PORTS_END_PORT, DIRECTION, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, DRAFT_MODE_STATE, MATCH_TAG_TYPES, MATCH_TAG_TYPES_TAG_TYPE, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, MATCH_TAGS, MATCH_TAGS_TAG_LIST, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, SECURITY_LOGGING_OBJECT_REFS, SECURITY_LOGGING_OBJECT_REFS_DATA, SECURITY_LOGGING_OBJECT_REFS_DATA_RATE, TAG_REFS, VIRTUAL_NETWORK_REFS, SERVICE_GROUP_REFS, ADDRESS_GROUP_REFS, POLICY_MANAGEMENT, PROJECT
    ) = (
        'name', 'fq_name', 'endpoint_1', 'endpoint_1_subnet', 'endpoint_1_subnet_ip_prefix', 'endpoint_1_subnet_ip_prefix_len', 'endpoint_1_virtual_network', 'endpoint_1_address_group', 'endpoint_1_tags', 'endpoint_1_tag_ids', 'endpoint_1_any', 'endpoint_2', 'endpoint_2_subnet', 'endpoint_2_subnet_ip_prefix', 'endpoint_2_subnet_ip_prefix_len', 'endpoint_2_virtual_network', 'endpoint_2_address_group', 'endpoint_2_tags', 'endpoint_2_tag_ids', 'endpoint_2_any', 'display_name', 'action_list', 'action_list_simple_action', 'action_list_gateway_name', 'action_list_apply_service', 'action_list_mirror_to', 'action_list_mirror_to_analyzer_name', 'action_list_mirror_to_encapsulation', 'action_list_mirror_to_analyzer_ip_address', 'action_list_mirror_to_analyzer_mac_address', 'action_list_mirror_to_routing_instance', 'action_list_mirror_to_udp_port', 'action_list_mirror_to_juniper_header', 'action_list_mirror_to_nh_mode', 'action_list_mirror_to_static_nh_header', 'action_list_mirror_to_static_nh_header_vtep_dst_ip_address', 'action_list_mirror_to_static_nh_header_vtep_dst_mac_address', 'action_list_mirror_to_static_nh_header_vni', 'action_list_mirror_to_nic_assisted_mirroring', 'action_list_mirror_to_nic_assisted_mirroring_vlan', 'action_list_assign_routing_instance', 'action_list_log', 'action_list_alert', 'action_list_qos_action', 'action_list_host_based_service', 'service', 'service_protocol', 'service_protocol_id', 'service_src_ports', 'service_src_ports_start_port', 'service_src_ports_end_port', 'service_dst_ports', 'service_dst_ports_start_port', 'service_dst_ports_end_port', 'direction', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'draft_mode_state', 'match_tag_types', 'match_tag_types_tag_type', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'match_tags', 'match_tags_tag_list', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'security_logging_object_refs', 'security_logging_object_refs_data', 'security_logging_object_refs_data_rate', 'tag_refs', 'virtual_network_refs', 'service_group_refs', 'address_group_refs', 'policy_management', 'project'
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
        ENDPOINT_1: properties.Schema(
            properties.Schema.MAP,
            _('ENDPOINT_1.'),
            update_allowed=True,
            required=False,
            schema={
                ENDPOINT_1_SUBNET: properties.Schema(
                    properties.Schema.MAP,
                    _('ENDPOINT_1_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        ENDPOINT_1_SUBNET_IP_PREFIX: properties.Schema(
                            properties.Schema.STRING,
                            _('ENDPOINT_1_SUBNET_IP_PREFIX.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ENDPOINT_1_SUBNET_IP_PREFIX_LEN: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ENDPOINT_1_SUBNET_IP_PREFIX_LEN.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                ENDPOINT_1_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('ENDPOINT_1_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_1_ADDRESS_GROUP: properties.Schema(
                    properties.Schema.STRING,
                    _('ENDPOINT_1_ADDRESS_GROUP.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_1_TAGS: properties.Schema(
                    properties.Schema.LIST,
                    _('ENDPOINT_1_TAGS.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_1_TAG_IDS: properties.Schema(
                    properties.Schema.LIST,
                    _('ENDPOINT_1_TAG_IDS.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_1_ANY: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ENDPOINT_1_ANY.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        ENDPOINT_2: properties.Schema(
            properties.Schema.MAP,
            _('ENDPOINT_2.'),
            update_allowed=True,
            required=False,
            schema={
                ENDPOINT_2_SUBNET: properties.Schema(
                    properties.Schema.MAP,
                    _('ENDPOINT_2_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        ENDPOINT_2_SUBNET_IP_PREFIX: properties.Schema(
                            properties.Schema.STRING,
                            _('ENDPOINT_2_SUBNET_IP_PREFIX.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ENDPOINT_2_SUBNET_IP_PREFIX_LEN: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ENDPOINT_2_SUBNET_IP_PREFIX_LEN.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                ENDPOINT_2_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('ENDPOINT_2_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_2_ADDRESS_GROUP: properties.Schema(
                    properties.Schema.STRING,
                    _('ENDPOINT_2_ADDRESS_GROUP.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_2_TAGS: properties.Schema(
                    properties.Schema.LIST,
                    _('ENDPOINT_2_TAGS.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_2_TAG_IDS: properties.Schema(
                    properties.Schema.LIST,
                    _('ENDPOINT_2_TAG_IDS.'),
                    update_allowed=True,
                    required=False,
                ),
                ENDPOINT_2_ANY: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ENDPOINT_2_ANY.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        ACTION_LIST: properties.Schema(
            properties.Schema.MAP,
            _('ACTION_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                ACTION_LIST_SIMPLE_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('ACTION_LIST_SIMPLE_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'deny', u'pass']),
                    ],
                ),
                ACTION_LIST_GATEWAY_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('ACTION_LIST_GATEWAY_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_APPLY_SERVICE: properties.Schema(
                    properties.Schema.LIST,
                    _('ACTION_LIST_APPLY_SERVICE.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_MIRROR_TO: properties.Schema(
                    properties.Schema.MAP,
                    _('ACTION_LIST_MIRROR_TO.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        ACTION_LIST_MIRROR_TO_ANALYZER_NAME: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_ANALYZER_NAME.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_ENCAPSULATION: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_ENCAPSULATION.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_UDP_PORT: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ACTION_LIST_MIRROR_TO_UDP_PORT.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_JUNIPER_HEADER: properties.Schema(
                            properties.Schema.BOOLEAN,
                            _('ACTION_LIST_MIRROR_TO_JUNIPER_HEADER.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_NH_MODE: properties.Schema(
                            properties.Schema.STRING,
                            _('ACTION_LIST_MIRROR_TO_NH_MODE.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'dynamic', u'static']),
                            ],
                        ),
                        ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER: properties.Schema(
                            properties.Schema.MAP,
                            _('ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER.'),
                            update_allowed=True,
                            required=False,
                            schema={
                                ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS: properties.Schema(
                                    properties.Schema.STRING,
                                    _('ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS: properties.Schema(
                                    properties.Schema.STRING,
                                    _('ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI.'),
                                    update_allowed=True,
                                    required=False,
                                    constraints=[
                                        constraints.Range(1, 16777215),
                                    ],
                                ),
                            }
                        ),
                        ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING: properties.Schema(
                            properties.Schema.BOOLEAN,
                            _('ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING.'),
                            update_allowed=True,
                            required=False,
                        ),
                        ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN: properties.Schema(
                            properties.Schema.INTEGER,
                            _('ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(0, 4094),
                            ],
                        ),
                    }
                ),
                ACTION_LIST_ASSIGN_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('ACTION_LIST_ASSIGN_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_LOG: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ACTION_LIST_LOG.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_ALERT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ACTION_LIST_ALERT.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_QOS_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('ACTION_LIST_QOS_ACTION.'),
                    update_allowed=True,
                    required=False,
                ),
                ACTION_LIST_HOST_BASED_SERVICE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ACTION_LIST_HOST_BASED_SERVICE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        SERVICE: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_PROTOCOL_ID: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SERVICE_PROTOCOL_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_SRC_PORTS: properties.Schema(
                    properties.Schema.MAP,
                    _('SERVICE_SRC_PORTS.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        SERVICE_SRC_PORTS_START_PORT: properties.Schema(
                            properties.Schema.INTEGER,
                            _('SERVICE_SRC_PORTS_START_PORT.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(-1, 65535),
                            ],
                        ),
                        SERVICE_SRC_PORTS_END_PORT: properties.Schema(
                            properties.Schema.INTEGER,
                            _('SERVICE_SRC_PORTS_END_PORT.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(-1, 65535),
                            ],
                        ),
                    }
                ),
                SERVICE_DST_PORTS: properties.Schema(
                    properties.Schema.MAP,
                    _('SERVICE_DST_PORTS.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        SERVICE_DST_PORTS_START_PORT: properties.Schema(
                            properties.Schema.INTEGER,
                            _('SERVICE_DST_PORTS_START_PORT.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(-1, 65535),
                            ],
                        ),
                        SERVICE_DST_PORTS_END_PORT: properties.Schema(
                            properties.Schema.INTEGER,
                            _('SERVICE_DST_PORTS_END_PORT.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.Range(-1, 65535),
                            ],
                        ),
                    }
                ),
            }
        ),
        DIRECTION: properties.Schema(
            properties.Schema.STRING,
            _('DIRECTION.'),
            update_allowed=True,
            required=False,
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
        DRAFT_MODE_STATE: properties.Schema(
            properties.Schema.STRING,
            _('DRAFT_MODE_STATE.'),
            update_allowed=True,
            required=False,
        ),
        MATCH_TAG_TYPES: properties.Schema(
            properties.Schema.MAP,
            _('MATCH_TAG_TYPES.'),
            update_allowed=True,
            required=False,
            schema={
                MATCH_TAG_TYPES_TAG_TYPE: properties.Schema(
                    properties.Schema.LIST,
                    _('MATCH_TAG_TYPES_TAG_TYPE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
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
        MATCH_TAGS: properties.Schema(
            properties.Schema.MAP,
            _('MATCH_TAGS.'),
            update_allowed=True,
            required=False,
            schema={
                MATCH_TAGS_TAG_LIST: properties.Schema(
                    properties.Schema.LIST,
                    _('MATCH_TAGS_TAG_LIST.'),
                    update_allowed=True,
                    required=False,
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
        SECURITY_LOGGING_OBJECT_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_LOGGING_OBJECT_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SECURITY_LOGGING_OBJECT_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_LOGGING_OBJECT_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    SECURITY_LOGGING_OBJECT_REFS_DATA_RATE: properties.Schema(
                        properties.Schema.INTEGER,
                        _('SECURITY_LOGGING_OBJECT_REFS_DATA_RATE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_GROUP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_GROUP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ADDRESS_GROUP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ADDRESS_GROUP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        POLICY_MANAGEMENT: properties.Schema(
            properties.Schema.STRING,
            _('POLICY_MANAGEMENT.'),
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
        ENDPOINT_1: attributes.Schema(
            _('ENDPOINT_1.'),
        ),
        ENDPOINT_2: attributes.Schema(
            _('ENDPOINT_2.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ACTION_LIST: attributes.Schema(
            _('ACTION_LIST.'),
        ),
        SERVICE: attributes.Schema(
            _('SERVICE.'),
        ),
        DIRECTION: attributes.Schema(
            _('DIRECTION.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        DRAFT_MODE_STATE: attributes.Schema(
            _('DRAFT_MODE_STATE.'),
        ),
        MATCH_TAG_TYPES: attributes.Schema(
            _('MATCH_TAG_TYPES.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        MATCH_TAGS: attributes.Schema(
            _('MATCH_TAGS.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        SECURITY_LOGGING_OBJECT_REFS: attributes.Schema(
            _('SECURITY_LOGGING_OBJECT_REFS.'),
        ),
        SECURITY_LOGGING_OBJECT_REFS_DATA: attributes.Schema(
            _('SECURITY_LOGGING_OBJECT_REFS_DATA.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        SERVICE_GROUP_REFS: attributes.Schema(
            _('SERVICE_GROUP_REFS.'),
        ),
        ADDRESS_GROUP_REFS: attributes.Schema(
            _('ADDRESS_GROUP_REFS.'),
        ),
        POLICY_MANAGEMENT: attributes.Schema(
            _('POLICY_MANAGEMENT.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.POLICY_MANAGEMENT) and self.properties.get(self.POLICY_MANAGEMENT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().policy_management_read(fq_name_str=self.properties.get(self.POLICY_MANAGEMENT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().policy_management_read(id=str(uuid.UUID(self.properties.get(self.POLICY_MANAGEMENT))))
            except:
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

        obj_0 = vnc_api.FirewallRule(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.ENDPOINT_1) is not None:
            obj_1 = vnc_api.FirewallRuleEndpointType()
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET) is not None:
                obj_2 = vnc_api.SubnetType()
                if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX))
                if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX_LEN))
                obj_1.set_subnet(obj_2)
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_VIRTUAL_NETWORK))
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ADDRESS_GROUP) is not None:
                obj_1.set_address_group(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ADDRESS_GROUP))
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS) is not None:
                for index_1 in range(len(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS))):
                    obj_1.add_tags(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS)[index_1])
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS) is not None:
                for index_1 in range(len(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS))):
                    obj_1.add_tag_ids(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS)[index_1])
            if self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ANY) is not None:
                obj_1.set_any(self.properties.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ANY))
            obj_0.set_endpoint_1(obj_1)
        if self.properties.get(self.ENDPOINT_2) is not None:
            obj_1 = vnc_api.FirewallRuleEndpointType()
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET) is not None:
                obj_2 = vnc_api.SubnetType()
                if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX))
                if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX_LEN))
                obj_1.set_subnet(obj_2)
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_VIRTUAL_NETWORK))
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ADDRESS_GROUP) is not None:
                obj_1.set_address_group(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ADDRESS_GROUP))
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS) is not None:
                for index_1 in range(len(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS))):
                    obj_1.add_tags(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS)[index_1])
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS) is not None:
                for index_1 in range(len(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS))):
                    obj_1.add_tag_ids(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS)[index_1])
            if self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ANY) is not None:
                obj_1.set_any(self.properties.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ANY))
            obj_0.set_endpoint_2(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ACTION_LIST) is not None:
            obj_1 = vnc_api.ActionListType()
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_SIMPLE_ACTION) is not None:
                obj_1.set_simple_action(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_SIMPLE_ACTION))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_GATEWAY_NAME) is not None:
                obj_1.set_gateway_name(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_GATEWAY_NAME))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE) is not None:
                for index_1 in range(len(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE))):
                    obj_1.add_apply_service(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE)[index_1])
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO) is not None:
                obj_2 = vnc_api.MirrorActionType()
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                    obj_2.set_analyzer_name(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                    obj_2.set_encapsulation(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                    obj_2.set_analyzer_ip_address(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS) is not None:
                    obj_2.set_analyzer_mac_address(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                    obj_2.set_routing_instance(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                    obj_2.set_udp_port(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_UDP_PORT))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_JUNIPER_HEADER) is not None:
                    obj_2.set_juniper_header(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_JUNIPER_HEADER))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NH_MODE) is not None:
                    obj_2.set_nh_mode(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NH_MODE))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER) is not None:
                    obj_3 = vnc_api.StaticMirrorNhType()
                    if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS) is not None:
                        obj_3.set_vtep_dst_ip_address(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS))
                    if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS) is not None:
                        obj_3.set_vtep_dst_mac_address(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS))
                    if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI) is not None:
                        obj_3.set_vni(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI))
                    obj_2.set_static_nh_header(obj_3)
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING) is not None:
                    obj_2.set_nic_assisted_mirroring(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING))
                if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN) is not None:
                    obj_2.set_nic_assisted_mirroring_vlan(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN))
                obj_1.set_mirror_to(obj_2)
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                obj_1.set_assign_routing_instance(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_LOG) is not None:
                obj_1.set_log(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_LOG))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ALERT) is not None:
                obj_1.set_alert(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ALERT))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_QOS_ACTION) is not None:
                obj_1.set_qos_action(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_QOS_ACTION))
            if self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_HOST_BASED_SERVICE) is not None:
                obj_1.set_host_based_service(self.properties.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_HOST_BASED_SERVICE))
            obj_0.set_action_list(obj_1)
        if self.properties.get(self.SERVICE) is not None:
            obj_1 = vnc_api.FirewallServiceType()
            if self.properties.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL) is not None:
                obj_1.set_protocol(self.properties.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL))
            if self.properties.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL_ID) is not None:
                obj_1.set_protocol_id(self.properties.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL_ID))
            if self.properties.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS) is not None:
                obj_2 = vnc_api.PortType()
                if self.properties.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_START_PORT) is not None:
                    obj_2.set_start_port(self.properties.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_START_PORT))
                if self.properties.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_END_PORT) is not None:
                    obj_2.set_end_port(self.properties.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_END_PORT))
                obj_1.set_src_ports(obj_2)
            if self.properties.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS) is not None:
                obj_2 = vnc_api.PortType()
                if self.properties.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_START_PORT) is not None:
                    obj_2.set_start_port(self.properties.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_START_PORT))
                if self.properties.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_END_PORT) is not None:
                    obj_2.set_end_port(self.properties.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_END_PORT))
                obj_1.set_dst_ports(obj_2)
            obj_0.set_service(obj_1)
        if self.properties.get(self.DIRECTION) is not None:
            obj_0.set_direction(self.properties.get(self.DIRECTION))
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
        if self.properties.get(self.DRAFT_MODE_STATE) is not None:
            obj_0.set_draft_mode_state(self.properties.get(self.DRAFT_MODE_STATE))
        if self.properties.get(self.MATCH_TAG_TYPES) is not None:
            obj_1 = vnc_api.FirewallRuleMatchTagsTypeIdList()
            if self.properties.get(self.MATCH_TAG_TYPES, {}).get(self.MATCH_TAG_TYPES_TAG_TYPE) is not None:
                for index_1 in range(len(self.properties.get(self.MATCH_TAG_TYPES, {}).get(self.MATCH_TAG_TYPES_TAG_TYPE))):
                    obj_1.add_tag_type(self.properties.get(self.MATCH_TAG_TYPES, {}).get(self.MATCH_TAG_TYPES_TAG_TYPE)[index_1])
            obj_0.set_match_tag_types(obj_1)
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
        if self.properties.get(self.MATCH_TAGS) is not None:
            obj_1 = vnc_api.FirewallRuleMatchTagsType()
            if self.properties.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST) is not None:
                for index_1 in range(len(self.properties.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST))):
                    obj_1.add_tag_list(self.properties.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST)[index_1])
            obj_0.set_match_tags(obj_1)
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

        # reference to security_logging_object_refs
        if len(self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS) or []) != len(self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA) or []):
            raise Exception(_('firewall-rule: specify security_logging_object_refs for each security_logging_object_refs_data.'))
        obj_1 = None
        if self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA))):
                obj_1 = vnc_api.SloRateType()
                if self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA, {})[index_0].get(self.SECURITY_LOGGING_OBJECT_REFS_DATA_RATE) is not None:
                    obj_1.set_rate(self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA, {})[index_0].get(self.SECURITY_LOGGING_OBJECT_REFS_DATA_RATE))

                if self.properties.get(self.SECURITY_LOGGING_OBJECT_REFS):
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
                    obj_0.add_security_logging_object(ref_obj, obj_1)

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

        # reference to service_group_refs
        if self.properties.get(self.SERVICE_GROUP_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_GROUP_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_group_read(
                        id=self.properties.get(self.SERVICE_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_group_read(
                        fq_name_str=self.properties.get(self.SERVICE_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_service_group(ref_obj)

        # reference to address_group_refs
        if self.properties.get(self.ADDRESS_GROUP_REFS):
            for index_0 in range(len(self.properties.get(self.ADDRESS_GROUP_REFS))):
                try:
                    ref_obj = self.vnc_lib().address_group_read(
                        id=self.properties.get(self.ADDRESS_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().address_group_read(
                        fq_name_str=self.properties.get(self.ADDRESS_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_address_group(ref_obj)

        try:
            obj_uuid = super(ContrailFirewallRule, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().firewall_rule_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.ENDPOINT_1) is not None:
            obj_1 = vnc_api.FirewallRuleEndpointType()
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET) is not None:
                obj_2 = vnc_api.SubnetType()
                if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX))
                if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_SUBNET, {}).get(self.ENDPOINT_1_SUBNET_IP_PREFIX_LEN))
                obj_1.set_subnet(obj_2)
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_VIRTUAL_NETWORK))
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ADDRESS_GROUP) is not None:
                obj_1.set_address_group(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ADDRESS_GROUP))
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS) is not None:
                for index_1 in range(len(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS))):
                    obj_1.add_tags(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAGS)[index_1])
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS) is not None:
                for index_1 in range(len(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS))):
                    obj_1.add_tag_ids(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_TAG_IDS)[index_1])
            if prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ANY) is not None:
                obj_1.set_any(prop_diff.get(self.ENDPOINT_1, {}).get(self.ENDPOINT_1_ANY))
            obj_0.set_endpoint_1(obj_1)
        if prop_diff.get(self.ENDPOINT_2) is not None:
            obj_1 = vnc_api.FirewallRuleEndpointType()
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET) is not None:
                obj_2 = vnc_api.SubnetType()
                if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX))
                if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_SUBNET, {}).get(self.ENDPOINT_2_SUBNET_IP_PREFIX_LEN))
                obj_1.set_subnet(obj_2)
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_VIRTUAL_NETWORK))
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ADDRESS_GROUP) is not None:
                obj_1.set_address_group(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ADDRESS_GROUP))
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS) is not None:
                for index_1 in range(len(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS))):
                    obj_1.add_tags(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAGS)[index_1])
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS) is not None:
                for index_1 in range(len(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS))):
                    obj_1.add_tag_ids(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_TAG_IDS)[index_1])
            if prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ANY) is not None:
                obj_1.set_any(prop_diff.get(self.ENDPOINT_2, {}).get(self.ENDPOINT_2_ANY))
            obj_0.set_endpoint_2(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ACTION_LIST) is not None:
            obj_1 = vnc_api.ActionListType()
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_SIMPLE_ACTION) is not None:
                obj_1.set_simple_action(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_SIMPLE_ACTION))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_GATEWAY_NAME) is not None:
                obj_1.set_gateway_name(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_GATEWAY_NAME))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE) is not None:
                for index_1 in range(len(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE))):
                    obj_1.add_apply_service(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_APPLY_SERVICE)[index_1])
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO) is not None:
                obj_2 = vnc_api.MirrorActionType()
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                    obj_2.set_analyzer_name(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                    obj_2.set_encapsulation(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                    obj_2.set_analyzer_ip_address(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS) is not None:
                    obj_2.set_analyzer_mac_address(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ANALYZER_MAC_ADDRESS))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                    obj_2.set_routing_instance(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                    obj_2.set_udp_port(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_UDP_PORT))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_JUNIPER_HEADER) is not None:
                    obj_2.set_juniper_header(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_JUNIPER_HEADER))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NH_MODE) is not None:
                    obj_2.set_nh_mode(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NH_MODE))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER) is not None:
                    obj_3 = vnc_api.StaticMirrorNhType()
                    if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS) is not None:
                        obj_3.set_vtep_dst_ip_address(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_IP_ADDRESS))
                    if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS) is not None:
                        obj_3.set_vtep_dst_mac_address(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VTEP_DST_MAC_ADDRESS))
                    if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI) is not None:
                        obj_3.set_vni(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER, {}).get(self.ACTION_LIST_MIRROR_TO_STATIC_NH_HEADER_VNI))
                    obj_2.set_static_nh_header(obj_3)
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING) is not None:
                    obj_2.set_nic_assisted_mirroring(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING))
                if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN) is not None:
                    obj_2.set_nic_assisted_mirroring_vlan(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_MIRROR_TO, {}).get(self.ACTION_LIST_MIRROR_TO_NIC_ASSISTED_MIRRORING_VLAN))
                obj_1.set_mirror_to(obj_2)
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                obj_1.set_assign_routing_instance(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_LOG) is not None:
                obj_1.set_log(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_LOG))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ALERT) is not None:
                obj_1.set_alert(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_ALERT))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_QOS_ACTION) is not None:
                obj_1.set_qos_action(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_QOS_ACTION))
            if prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_HOST_BASED_SERVICE) is not None:
                obj_1.set_host_based_service(prop_diff.get(self.ACTION_LIST, {}).get(self.ACTION_LIST_HOST_BASED_SERVICE))
            obj_0.set_action_list(obj_1)
        if prop_diff.get(self.SERVICE) is not None:
            obj_1 = vnc_api.FirewallServiceType()
            if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL) is not None:
                obj_1.set_protocol(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL))
            if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL_ID) is not None:
                obj_1.set_protocol_id(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_PROTOCOL_ID))
            if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS) is not None:
                obj_2 = vnc_api.PortType()
                if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_START_PORT) is not None:
                    obj_2.set_start_port(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_START_PORT))
                if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_END_PORT) is not None:
                    obj_2.set_end_port(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_SRC_PORTS, {}).get(self.SERVICE_SRC_PORTS_END_PORT))
                obj_1.set_src_ports(obj_2)
            if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS) is not None:
                obj_2 = vnc_api.PortType()
                if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_START_PORT) is not None:
                    obj_2.set_start_port(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_START_PORT))
                if prop_diff.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_END_PORT) is not None:
                    obj_2.set_end_port(prop_diff.get(self.SERVICE, {}).get(self.SERVICE_DST_PORTS, {}).get(self.SERVICE_DST_PORTS_END_PORT))
                obj_1.set_dst_ports(obj_2)
            obj_0.set_service(obj_1)
        if prop_diff.get(self.DIRECTION) is not None:
            obj_0.set_direction(prop_diff.get(self.DIRECTION))
        if prop_diff.get(self.MATCH_TAGS) is not None:
            obj_1 = vnc_api.FirewallRuleMatchTagsType()
            if prop_diff.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST) is not None:
                for index_1 in range(len(prop_diff.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST))):
                    obj_1.add_tag_list(prop_diff.get(self.MATCH_TAGS, {}).get(self.MATCH_TAGS_TAG_LIST)[index_1])
            obj_0.set_match_tags(obj_1)
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

        # reference to security_logging_object
        update = 0
        if not self.SECURITY_LOGGING_OBJECT_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_security_logging_object_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.SECURITY_LOGGING_OBJECT_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_security_logging_object_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA))):
                obj_1 = vnc_api.SloRateType()
                if prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA, {})[index_0].get(self.SECURITY_LOGGING_OBJECT_REFS_DATA_RATE) is not None:
                    obj_1.set_rate(prop_diff.get(self.SECURITY_LOGGING_OBJECT_REFS_DATA, {})[index_0].get(self.SECURITY_LOGGING_OBJECT_REFS_DATA_RATE))
                ref_data_list.append(obj_1)
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
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('firewall-rule: specify security_logging_object_refs_data for each security_logging_object_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_security_logging_object_list(ref_obj_list, ref_data_list)
        # End: reference to security_logging_object_refs

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

        # reference to service_group_refs
        ref_obj_list = []
        if self.SERVICE_GROUP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_GROUP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_group_read(
                        id=prop_diff.get(self.SERVICE_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_group_read(
                        fq_name_str=prop_diff.get(self.SERVICE_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_service_group_list(ref_obj_list)
            # End: reference to service_group_refs

        # reference to address_group_refs
        ref_obj_list = []
        if self.ADDRESS_GROUP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ADDRESS_GROUP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().address_group_read(
                        id=prop_diff.get(self.ADDRESS_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().address_group_read(
                        fq_name_str=prop_diff.get(self.ADDRESS_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_address_group_list(ref_obj_list)
            # End: reference to address_group_refs

        try:
            self.vnc_lib().firewall_rule_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().firewall_rule_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('firewall_rule %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().firewall_rule_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::FirewallRule': ContrailFirewallRule,
    }
