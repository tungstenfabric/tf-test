
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


class ContrailGlobalSystemConfig(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, BGPAAS_PARAMETERS, BGPAAS_PARAMETERS_PORT_START, BGPAAS_PARAMETERS_PORT_END, IGMP_ENABLE, IBGP_AUTO_MESH, RD_CLUSTER_SEED, AUTONOMOUS_SYSTEM, ENABLE_4BYTE_AS, DISPLAY_NAME, PLUGIN_TUNING, PLUGIN_TUNING_PLUGIN_PROPERTY, PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY, PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, IP_FABRIC_SUBNETS, IP_FABRIC_SUBNETS_SUBNET, IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX, IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN, ENABLE_SECURITY_POLICY_DRAFT, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, MAC_LIMIT_CONTROL, MAC_LIMIT_CONTROL_MAC_LIMIT, MAC_LIMIT_CONTROL_MAC_LIMIT_ACTION, USER_DEFINED_LOG_STATISTICS, USER_DEFINED_LOG_STATISTICS_STATLIST, USER_DEFINED_LOG_STATISTICS_STATLIST_NAME, USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN, CONFIG_VERSION, SUPPORTED_VENDOR_HARDWARES, SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, SUPPORTED_FABRIC_ANNOTATIONS, SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY, SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE, ALARM_ENABLE, MAC_MOVE_CONTROL, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT, MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW, MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION, DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX, DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN, BGP_ALWAYS_COMPARE_MED, DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN, DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX, GRACEFUL_RESTART_PARAMETERS, GRACEFUL_RESTART_PARAMETERS_ENABLE, GRACEFUL_RESTART_PARAMETERS_RESTART_TIME, GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME, GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT, GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE, GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE, SUPPORTED_DEVICE_FAMILIES, SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY, MAC_AGING_TIME, TAG_REFS, BGP_ROUTER_REFS
    ) = (
        'name', 'fq_name', 'bgpaas_parameters', 'bgpaas_parameters_port_start', 'bgpaas_parameters_port_end', 'igmp_enable', 'ibgp_auto_mesh', 'rd_cluster_seed', 'autonomous_system', 'enable_4byte_as', 'display_name', 'plugin_tuning', 'plugin_tuning_plugin_property', 'plugin_tuning_plugin_property_property', 'plugin_tuning_plugin_property_value', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'ip_fabric_subnets', 'ip_fabric_subnets_subnet', 'ip_fabric_subnets_subnet_ip_prefix', 'ip_fabric_subnets_subnet_ip_prefix_len', 'enable_security_policy_draft', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'mac_limit_control', 'mac_limit_control_mac_limit', 'mac_limit_control_mac_limit_action', 'user_defined_log_statistics', 'user_defined_log_statistics_statlist', 'user_defined_log_statistics_statlist_name', 'user_defined_log_statistics_statlist_pattern', 'config_version', 'supported_vendor_hardwares', 'supported_vendor_hardwares_vendor_hardware', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'supported_fabric_annotations', 'supported_fabric_annotations_key_value_pair', 'supported_fabric_annotations_key_value_pair_key', 'supported_fabric_annotations_key_value_pair_value', 'alarm_enable', 'mac_move_control', 'mac_move_control_mac_move_limit', 'mac_move_control_mac_move_time_window', 'mac_move_control_mac_move_limit_action', 'data_center_interconnect_loopback_namespace', 'data_center_interconnect_loopback_namespace_subnet', 'data_center_interconnect_loopback_namespace_subnet_ip_prefix', 'data_center_interconnect_loopback_namespace_subnet_ip_prefix_len', 'bgp_always_compare_med', 'data_center_interconnect_asn_namespace', 'data_center_interconnect_asn_namespace_asn_min', 'data_center_interconnect_asn_namespace_asn_max', 'graceful_restart_parameters', 'graceful_restart_parameters_enable', 'graceful_restart_parameters_restart_time', 'graceful_restart_parameters_long_lived_restart_time', 'graceful_restart_parameters_end_of_rib_timeout', 'graceful_restart_parameters_bgp_helper_enable', 'graceful_restart_parameters_xmpp_helper_enable', 'supported_device_families', 'supported_device_families_device_family', 'mac_aging_time', 'tag_refs', 'bgp_router_refs'
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
        BGPAAS_PARAMETERS: properties.Schema(
            properties.Schema.MAP,
            _('BGPAAS_PARAMETERS.'),
            update_allowed=True,
            required=False,
            schema={
                BGPAAS_PARAMETERS_PORT_START: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_PARAMETERS_PORT_START.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(-1, 65535),
                    ],
                ),
                BGPAAS_PARAMETERS_PORT_END: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_PARAMETERS_PORT_END.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(-1, 65535),
                    ],
                ),
            }
        ),
        IGMP_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IGMP_ENABLE.'),
            update_allowed=True,
            required=False,
        ),
        IBGP_AUTO_MESH: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IBGP_AUTO_MESH.'),
            update_allowed=True,
            required=False,
        ),
        RD_CLUSTER_SEED: properties.Schema(
            properties.Schema.INTEGER,
            _('RD_CLUSTER_SEED.'),
            update_allowed=True,
            required=False,
        ),
        AUTONOMOUS_SYSTEM: properties.Schema(
            properties.Schema.INTEGER,
            _('AUTONOMOUS_SYSTEM.'),
            update_allowed=True,
            required=False,
        ),
        ENABLE_4BYTE_AS: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ENABLE_4BYTE_AS.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PLUGIN_TUNING: properties.Schema(
            properties.Schema.MAP,
            _('PLUGIN_TUNING.'),
            update_allowed=True,
            required=False,
            schema={
                PLUGIN_TUNING_PLUGIN_PROPERTY: properties.Schema(
                    properties.Schema.LIST,
                    _('PLUGIN_TUNING_PLUGIN_PROPERTY.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY: properties.Schema(
                                properties.Schema.STRING,
                                _('PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
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
        IP_FABRIC_SUBNETS: properties.Schema(
            properties.Schema.MAP,
            _('IP_FABRIC_SUBNETS.'),
            update_allowed=True,
            required=False,
            schema={
                IP_FABRIC_SUBNETS_SUBNET: properties.Schema(
                    properties.Schema.LIST,
                    _('IP_FABRIC_SUBNETS_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                properties.Schema.INTEGER,
                                _('IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        ENABLE_SECURITY_POLICY_DRAFT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ENABLE_SECURITY_POLICY_DRAFT.'),
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
        USER_DEFINED_LOG_STATISTICS: properties.Schema(
            properties.Schema.MAP,
            _('USER_DEFINED_LOG_STATISTICS.'),
            update_allowed=True,
            required=False,
            schema={
                USER_DEFINED_LOG_STATISTICS_STATLIST: properties.Schema(
                    properties.Schema.LIST,
                    _('USER_DEFINED_LOG_STATISTICS_STATLIST.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            USER_DEFINED_LOG_STATISTICS_STATLIST_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('USER_DEFINED_LOG_STATISTICS_STATLIST_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN: properties.Schema(
                                properties.Schema.STRING,
                                _('USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        CONFIG_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('CONFIG_VERSION.'),
            update_allowed=True,
            required=False,
        ),
        SUPPORTED_VENDOR_HARDWARES: properties.Schema(
            properties.Schema.MAP,
            _('SUPPORTED_VENDOR_HARDWARES.'),
            update_allowed=True,
            required=False,
            schema={
                SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE: properties.Schema(
                    properties.Schema.LIST,
                    _('SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE.'),
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
        SUPPORTED_FABRIC_ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('SUPPORTED_FABRIC_ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        ALARM_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ALARM_ENABLE.'),
            update_allowed=True,
            required=False,
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
        DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE: properties.Schema(
            properties.Schema.MAP,
            _('DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE.'),
            update_allowed=True,
            required=False,
            schema={
                DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET: properties.Schema(
                    properties.Schema.LIST,
                    _('DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                properties.Schema.INTEGER,
                                _('DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        BGP_ALWAYS_COMPARE_MED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGP_ALWAYS_COMPARE_MED.'),
            update_allowed=True,
            required=False,
        ),
        DATA_CENTER_INTERCONNECT_ASN_NAMESPACE: properties.Schema(
            properties.Schema.MAP,
            _('DATA_CENTER_INTERCONNECT_ASN_NAMESPACE.'),
            update_allowed=True,
            required=False,
            schema={
                DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN: properties.Schema(
                    properties.Schema.INTEGER,
                    _('DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN.'),
                    update_allowed=True,
                    required=False,
                ),
                DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX: properties.Schema(
                    properties.Schema.INTEGER,
                    _('DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        GRACEFUL_RESTART_PARAMETERS: properties.Schema(
            properties.Schema.MAP,
            _('GRACEFUL_RESTART_PARAMETERS.'),
            update_allowed=True,
            required=False,
            schema={
                GRACEFUL_RESTART_PARAMETERS_ENABLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('GRACEFUL_RESTART_PARAMETERS_ENABLE.'),
                    update_allowed=True,
                    required=False,
                ),
                GRACEFUL_RESTART_PARAMETERS_RESTART_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('GRACEFUL_RESTART_PARAMETERS_RESTART_TIME.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 4095),
                    ],
                ),
                GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 16777215),
                    ],
                ),
                GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 4095),
                    ],
                ),
                GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE.'),
                    update_allowed=True,
                    required=False,
                ),
                GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        SUPPORTED_DEVICE_FAMILIES: properties.Schema(
            properties.Schema.MAP,
            _('SUPPORTED_DEVICE_FAMILIES.'),
            update_allowed=True,
            required=False,
            schema={
                SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY: properties.Schema(
                    properties.Schema.LIST,
                    _('SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY.'),
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
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
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
        BGPAAS_PARAMETERS: attributes.Schema(
            _('BGPAAS_PARAMETERS.'),
        ),
        IGMP_ENABLE: attributes.Schema(
            _('IGMP_ENABLE.'),
        ),
        IBGP_AUTO_MESH: attributes.Schema(
            _('IBGP_AUTO_MESH.'),
        ),
        RD_CLUSTER_SEED: attributes.Schema(
            _('RD_CLUSTER_SEED.'),
        ),
        AUTONOMOUS_SYSTEM: attributes.Schema(
            _('AUTONOMOUS_SYSTEM.'),
        ),
        ENABLE_4BYTE_AS: attributes.Schema(
            _('ENABLE_4BYTE_AS.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PLUGIN_TUNING: attributes.Schema(
            _('PLUGIN_TUNING.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        IP_FABRIC_SUBNETS: attributes.Schema(
            _('IP_FABRIC_SUBNETS.'),
        ),
        ENABLE_SECURITY_POLICY_DRAFT: attributes.Schema(
            _('ENABLE_SECURITY_POLICY_DRAFT.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        MAC_LIMIT_CONTROL: attributes.Schema(
            _('MAC_LIMIT_CONTROL.'),
        ),
        USER_DEFINED_LOG_STATISTICS: attributes.Schema(
            _('USER_DEFINED_LOG_STATISTICS.'),
        ),
        CONFIG_VERSION: attributes.Schema(
            _('CONFIG_VERSION.'),
        ),
        SUPPORTED_VENDOR_HARDWARES: attributes.Schema(
            _('SUPPORTED_VENDOR_HARDWARES.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        SUPPORTED_FABRIC_ANNOTATIONS: attributes.Schema(
            _('SUPPORTED_FABRIC_ANNOTATIONS.'),
        ),
        ALARM_ENABLE: attributes.Schema(
            _('ALARM_ENABLE.'),
        ),
        MAC_MOVE_CONTROL: attributes.Schema(
            _('MAC_MOVE_CONTROL.'),
        ),
        DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE.'),
        ),
        BGP_ALWAYS_COMPARE_MED: attributes.Schema(
            _('BGP_ALWAYS_COMPARE_MED.'),
        ),
        DATA_CENTER_INTERCONNECT_ASN_NAMESPACE: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_ASN_NAMESPACE.'),
        ),
        GRACEFUL_RESTART_PARAMETERS: attributes.Schema(
            _('GRACEFUL_RESTART_PARAMETERS.'),
        ),
        SUPPORTED_DEVICE_FAMILIES: attributes.Schema(
            _('SUPPORTED_DEVICE_FAMILIES.'),
        ),
        MAC_AGING_TIME: attributes.Schema(
            _('MAC_AGING_TIME.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        obj_0 = vnc_api.GlobalSystemConfig(name=self.properties[self.NAME])

        if self.properties.get(self.BGPAAS_PARAMETERS) is not None:
            obj_1 = vnc_api.BGPaaServiceParametersType()
            if self.properties.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_START) is not None:
                obj_1.set_port_start(self.properties.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_START))
            if self.properties.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_END) is not None:
                obj_1.set_port_end(self.properties.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_END))
            obj_0.set_bgpaas_parameters(obj_1)
        if self.properties.get(self.IGMP_ENABLE) is not None:
            obj_0.set_igmp_enable(self.properties.get(self.IGMP_ENABLE))
        if self.properties.get(self.IBGP_AUTO_MESH) is not None:
            obj_0.set_ibgp_auto_mesh(self.properties.get(self.IBGP_AUTO_MESH))
        if self.properties.get(self.RD_CLUSTER_SEED) is not None:
            obj_0.set_rd_cluster_seed(self.properties.get(self.RD_CLUSTER_SEED))
        if self.properties.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(self.properties.get(self.AUTONOMOUS_SYSTEM))
        if self.properties.get(self.ENABLE_4BYTE_AS) is not None:
            obj_0.set_enable_4byte_as(self.properties.get(self.ENABLE_4BYTE_AS))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PLUGIN_TUNING) is not None:
            obj_1 = vnc_api.PluginProperties()
            if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY) is not None:
                for index_1 in range(len(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY))):
                    obj_2 = vnc_api.PluginProperty()
                    if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY) is not None:
                        obj_2.set_property(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY))
                    if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE))
                    obj_1.add_plugin_property(obj_2)
            obj_0.set_plugin_tuning(obj_1)
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
        if self.properties.get(self.IP_FABRIC_SUBNETS) is not None:
            obj_1 = vnc_api.SubnetListType()
            if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET) is not None:
                for index_1 in range(len(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX))
                    if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_ip_fabric_subnets(obj_1)
        if self.properties.get(self.ENABLE_SECURITY_POLICY_DRAFT) is not None:
            obj_0.set_enable_security_policy_draft(self.properties.get(self.ENABLE_SECURITY_POLICY_DRAFT))
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
        if self.properties.get(self.USER_DEFINED_LOG_STATISTICS) is not None:
            obj_1 = vnc_api.UserDefinedLogStatList()
            if self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST) is not None:
                for index_1 in range(len(self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST))):
                    obj_2 = vnc_api.UserDefinedLogStat()
                    if self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_NAME) is not None:
                        obj_2.set_name(self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_NAME))
                    if self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN) is not None:
                        obj_2.set_pattern(self.properties.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN))
                    obj_1.add_statlist(obj_2)
            obj_0.set_user_defined_log_statistics(obj_1)
        if self.properties.get(self.CONFIG_VERSION) is not None:
            obj_0.set_config_version(self.properties.get(self.CONFIG_VERSION))
        if self.properties.get(self.SUPPORTED_VENDOR_HARDWARES) is not None:
            obj_1 = vnc_api.VendorHardwaresType()
            if self.properties.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE) is not None:
                for index_1 in range(len(self.properties.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE))):
                    obj_1.add_vendor_hardware(self.properties.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE)[index_1])
            obj_0.set_supported_vendor_hardwares(obj_1)
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
        if self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_supported_fabric_annotations(obj_1)
        if self.properties.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(self.properties.get(self.ALARM_ENABLE))
        if self.properties.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(self.properties.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE) is not None:
            obj_1 = vnc_api.SubnetListType()
            if self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET) is not None:
                for index_1 in range(len(self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX))
                    if self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(self.properties.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_data_center_interconnect_loopback_namespace(obj_1)
        if self.properties.get(self.BGP_ALWAYS_COMPARE_MED) is not None:
            obj_0.set_bgp_always_compare_med(self.properties.get(self.BGP_ALWAYS_COMPARE_MED))
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE) is not None:
            obj_1 = vnc_api.AsnRangeType()
            if self.properties.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN) is not None:
                obj_1.set_asn_min(self.properties.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN))
            if self.properties.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX) is not None:
                obj_1.set_asn_max(self.properties.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX))
            obj_0.set_data_center_interconnect_asn_namespace(obj_1)
        if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS) is not None:
            obj_1 = vnc_api.GracefulRestartParametersType()
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_ENABLE) is not None:
                obj_1.set_enable(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_ENABLE))
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_RESTART_TIME) is not None:
                obj_1.set_restart_time(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_RESTART_TIME))
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME) is not None:
                obj_1.set_long_lived_restart_time(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME))
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT) is not None:
                obj_1.set_end_of_rib_timeout(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT))
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE) is not None:
                obj_1.set_bgp_helper_enable(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE))
            if self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE) is not None:
                obj_1.set_xmpp_helper_enable(self.properties.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE))
            obj_0.set_graceful_restart_parameters(obj_1)
        if self.properties.get(self.SUPPORTED_DEVICE_FAMILIES) is not None:
            obj_1 = vnc_api.DeviceFamilyListType()
            if self.properties.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY) is not None:
                for index_1 in range(len(self.properties.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY))):
                    obj_1.add_device_family(self.properties.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY)[index_1])
            obj_0.set_supported_device_families(obj_1)
        if self.properties.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(self.properties.get(self.MAC_AGING_TIME))

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

        # reference to bgp_router_refs
        if self.properties.get(self.BGP_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.BGP_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        id=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        fq_name_str=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_bgp_router(ref_obj)

        try:
            obj_uuid = super(ContrailGlobalSystemConfig, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().global_system_config_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.BGPAAS_PARAMETERS) is not None:
            obj_1 = vnc_api.BGPaaServiceParametersType()
            if prop_diff.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_START) is not None:
                obj_1.set_port_start(prop_diff.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_START))
            if prop_diff.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_END) is not None:
                obj_1.set_port_end(prop_diff.get(self.BGPAAS_PARAMETERS, {}).get(self.BGPAAS_PARAMETERS_PORT_END))
            obj_0.set_bgpaas_parameters(obj_1)
        if prop_diff.get(self.IGMP_ENABLE) is not None:
            obj_0.set_igmp_enable(prop_diff.get(self.IGMP_ENABLE))
        if prop_diff.get(self.IBGP_AUTO_MESH) is not None:
            obj_0.set_ibgp_auto_mesh(prop_diff.get(self.IBGP_AUTO_MESH))
        if prop_diff.get(self.RD_CLUSTER_SEED) is not None:
            obj_0.set_rd_cluster_seed(prop_diff.get(self.RD_CLUSTER_SEED))
        if prop_diff.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(prop_diff.get(self.AUTONOMOUS_SYSTEM))
        if prop_diff.get(self.ENABLE_4BYTE_AS) is not None:
            obj_0.set_enable_4byte_as(prop_diff.get(self.ENABLE_4BYTE_AS))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.PLUGIN_TUNING) is not None:
            obj_1 = vnc_api.PluginProperties()
            if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY) is not None:
                for index_1 in range(len(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY))):
                    obj_2 = vnc_api.PluginProperty()
                    if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY) is not None:
                        obj_2.set_property(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY))
                    if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE))
                    obj_1.add_plugin_property(obj_2)
            obj_0.set_plugin_tuning(obj_1)
        if prop_diff.get(self.IP_FABRIC_SUBNETS) is not None:
            obj_1 = vnc_api.SubnetListType()
            if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET) is not None:
                for index_1 in range(len(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX))
                    if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_ip_fabric_subnets(obj_1)
        if prop_diff.get(self.ENABLE_SECURITY_POLICY_DRAFT) is not None:
            obj_0.set_enable_security_policy_draft(prop_diff.get(self.ENABLE_SECURITY_POLICY_DRAFT))
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
        if prop_diff.get(self.USER_DEFINED_LOG_STATISTICS) is not None:
            obj_1 = vnc_api.UserDefinedLogStatList()
            if prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST) is not None:
                for index_1 in range(len(prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST))):
                    obj_2 = vnc_api.UserDefinedLogStat()
                    if prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_NAME) is not None:
                        obj_2.set_name(prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_NAME))
                    if prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN) is not None:
                        obj_2.set_pattern(prop_diff.get(self.USER_DEFINED_LOG_STATISTICS, {}).get(self.USER_DEFINED_LOG_STATISTICS_STATLIST, {})[index_1].get(self.USER_DEFINED_LOG_STATISTICS_STATLIST_PATTERN))
                    obj_1.add_statlist(obj_2)
            obj_0.set_user_defined_log_statistics(obj_1)
        if prop_diff.get(self.SUPPORTED_VENDOR_HARDWARES) is not None:
            obj_1 = vnc_api.VendorHardwaresType()
            if prop_diff.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE) is not None:
                for index_1 in range(len(prop_diff.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE))):
                    obj_1.add_vendor_hardware(prop_diff.get(self.SUPPORTED_VENDOR_HARDWARES, {}).get(self.SUPPORTED_VENDOR_HARDWARES_VENDOR_HARDWARE)[index_1])
            obj_0.set_supported_vendor_hardwares(obj_1)
        if prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.SUPPORTED_FABRIC_ANNOTATIONS, {}).get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.SUPPORTED_FABRIC_ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_supported_fabric_annotations(obj_1)
        if prop_diff.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(prop_diff.get(self.ALARM_ENABLE))
        if prop_diff.get(self.MAC_MOVE_CONTROL) is not None:
            obj_1 = vnc_api.MACMoveLimitControlType()
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT) is not None:
                obj_1.set_mac_move_limit(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW) is not None:
                obj_1.set_mac_move_time_window(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_TIME_WINDOW))
            if prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION) is not None:
                obj_1.set_mac_move_limit_action(prop_diff.get(self.MAC_MOVE_CONTROL, {}).get(self.MAC_MOVE_CONTROL_MAC_MOVE_LIMIT_ACTION))
            obj_0.set_mac_move_control(obj_1)
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE) is not None:
            obj_1 = vnc_api.SubnetListType()
            if prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET) is not None:
                for index_1 in range(len(prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX))
                    if prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(prop_diff.get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET, {})[index_1].get(self.DATA_CENTER_INTERCONNECT_LOOPBACK_NAMESPACE_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_data_center_interconnect_loopback_namespace(obj_1)
        if prop_diff.get(self.BGP_ALWAYS_COMPARE_MED) is not None:
            obj_0.set_bgp_always_compare_med(prop_diff.get(self.BGP_ALWAYS_COMPARE_MED))
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE) is not None:
            obj_1 = vnc_api.AsnRangeType()
            if prop_diff.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN) is not None:
                obj_1.set_asn_min(prop_diff.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MIN))
            if prop_diff.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX) is not None:
                obj_1.set_asn_max(prop_diff.get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE, {}).get(self.DATA_CENTER_INTERCONNECT_ASN_NAMESPACE_ASN_MAX))
            obj_0.set_data_center_interconnect_asn_namespace(obj_1)
        if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS) is not None:
            obj_1 = vnc_api.GracefulRestartParametersType()
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_ENABLE) is not None:
                obj_1.set_enable(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_ENABLE))
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_RESTART_TIME) is not None:
                obj_1.set_restart_time(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_RESTART_TIME))
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME) is not None:
                obj_1.set_long_lived_restart_time(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_LONG_LIVED_RESTART_TIME))
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT) is not None:
                obj_1.set_end_of_rib_timeout(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_END_OF_RIB_TIMEOUT))
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE) is not None:
                obj_1.set_bgp_helper_enable(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_BGP_HELPER_ENABLE))
            if prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE) is not None:
                obj_1.set_xmpp_helper_enable(prop_diff.get(self.GRACEFUL_RESTART_PARAMETERS, {}).get(self.GRACEFUL_RESTART_PARAMETERS_XMPP_HELPER_ENABLE))
            obj_0.set_graceful_restart_parameters(obj_1)
        if prop_diff.get(self.SUPPORTED_DEVICE_FAMILIES) is not None:
            obj_1 = vnc_api.DeviceFamilyListType()
            if prop_diff.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY) is not None:
                for index_1 in range(len(prop_diff.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY))):
                    obj_1.add_device_family(prop_diff.get(self.SUPPORTED_DEVICE_FAMILIES, {}).get(self.SUPPORTED_DEVICE_FAMILIES_DEVICE_FAMILY)[index_1])
            obj_0.set_supported_device_families(obj_1)
        if prop_diff.get(self.MAC_AGING_TIME) is not None:
            obj_0.set_mac_aging_time(prop_diff.get(self.MAC_AGING_TIME))

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

        # reference to bgp_router_refs
        ref_obj_list = []
        if self.BGP_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.BGP_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        id=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        fq_name_str=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_bgp_router_list(ref_obj_list)
            # End: reference to bgp_router_refs

        try:
            self.vnc_lib().global_system_config_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().global_system_config_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('global_system_config %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().global_system_config_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::GlobalSystemConfig': ContrailGlobalSystemConfig,
    }
