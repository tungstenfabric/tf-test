
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


class ContrailPhysicalRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN, PHYSICAL_ROUTER_USER_CREDENTIALS, PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME, PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD, PHYSICAL_ROUTER_MANAGEMENT_MAC, PHYSICAL_ROUTER_UNDERLAY_MANAGED, PHYSICAL_ROUTER_DEVICE_FAMILY, PHYSICAL_ROUTER_MANAGEMENT_IP, DISPLAY_NAME, PHYSICAL_ROUTER_VENDOR_NAME, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, PHYSICAL_ROUTER_UNDERLAY_CONFIG, PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP, PHYSICAL_ROUTER_MANAGED_STATE, PHYSICAL_ROUTER_CLI_COMMIT_STATE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, TELEMETRY_INFO, TELEMETRY_INFO_RESOURCE, TELEMETRY_INFO_RESOURCE_NAME, TELEMETRY_INFO_RESOURCE_PATH, TELEMETRY_INFO_RESOURCE_RATE, TELEMETRY_INFO_SERVER_IP, TELEMETRY_INFO_SERVER_PORT, PHYSICAL_ROUTER_DHCP_PARAMETERS, PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME, PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID, PHYSICAL_ROUTER_DATAPLANE_IP, PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG, PHYSICAL_ROUTER_OS_VERSION, PHYSICAL_ROUTER_VNC_MANAGED, PHYSICAL_ROUTER_ROLE, PHYSICAL_ROUTER_SERIAL_NUMBER, PHYSICAL_ROUTER_SNMP_CREDENTIALS, PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION, PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES, PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME, PHYSICAL_ROUTER_PRODUCT_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PHYSICAL_ROUTER_LLDP, ROUTING_BRIDGING_ROLES, ROUTING_BRIDGING_ROLES_RB_ROLES, PHYSICAL_ROUTER_LOOPBACK_IP, PHYSICAL_ROUTER_ENCRYPTION_TYPE, PHYSICAL_ROUTER_HOSTNAME, PHYSICAL_ROUTER_SNMP, PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT, DEVICE_FUNCTIONAL_GROUP_REFS, OVERLAY_ROLE_REFS, NODE_PROFILE_REFS, VIRTUAL_ROUTER_REFS, VIRTUAL_NETWORK_REFS, TAG_REFS, FABRIC_REFS, DEVICE_IMAGE_REFS, BGP_ROUTER_REFS, TELEMETRY_PROFILE_REFS, DEVICE_CHASSIS_REFS, INTENT_MAP_REFS, PHYSICAL_ROLE_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'physical_router_autonomous_system', 'physical_router_autonomous_system_asn', 'physical_router_user_credentials', 'physical_router_user_credentials_username', 'physical_router_user_credentials_password', 'physical_router_management_mac', 'physical_router_underlay_managed', 'physical_router_device_family', 'physical_router_management_ip', 'display_name', 'physical_router_vendor_name', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'physical_router_underlay_config', 'physical_router_replicator_loopback_ip', 'physical_router_managed_state', 'physical_router_cli_commit_state', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'telemetry_info', 'telemetry_info_resource', 'telemetry_info_resource_name', 'telemetry_info_resource_path', 'telemetry_info_resource_rate', 'telemetry_info_server_ip', 'telemetry_info_server_port', 'physical_router_dhcp_parameters', 'physical_router_dhcp_parameters_lease_expiry_time', 'physical_router_dhcp_parameters_client_id', 'physical_router_dataplane_ip', 'physical_router_supplemental_config', 'physical_router_os_version', 'physical_router_vnc_managed', 'physical_router_role', 'physical_router_serial_number', 'physical_router_snmp_credentials', 'physical_router_snmp_credentials_version', 'physical_router_snmp_credentials_local_port', 'physical_router_snmp_credentials_retries', 'physical_router_snmp_credentials_timeout', 'physical_router_snmp_credentials_v2_community', 'physical_router_snmp_credentials_v3_security_name', 'physical_router_snmp_credentials_v3_security_level', 'physical_router_snmp_credentials_v3_security_engine_id', 'physical_router_snmp_credentials_v3_context', 'physical_router_snmp_credentials_v3_context_engine_id', 'physical_router_snmp_credentials_v3_authentication_protocol', 'physical_router_snmp_credentials_v3_authentication_password', 'physical_router_snmp_credentials_v3_privacy_protocol', 'physical_router_snmp_credentials_v3_privacy_password', 'physical_router_snmp_credentials_v3_engine_id', 'physical_router_snmp_credentials_v3_engine_boots', 'physical_router_snmp_credentials_v3_engine_time', 'physical_router_product_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'physical_router_lldp', 'routing_bridging_roles', 'routing_bridging_roles_rb_roles', 'physical_router_loopback_ip', 'physical_router_encryption_type', 'physical_router_hostname', 'physical_router_snmp', 'physical_router_junos_service_ports', 'physical_router_junos_service_ports_service_port', 'device_functional_group_refs', 'overlay_role_refs', 'node_profile_refs', 'virtual_router_refs', 'virtual_network_refs', 'tag_refs', 'fabric_refs', 'device_image_refs', 'bgp_router_refs', 'telemetry_profile_refs', 'device_chassis_refs', 'intent_map_refs', 'physical_role_refs', 'global_system_config'
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
        PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN: properties.Schema(
                    properties.Schema.LIST,
                    _('PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([1, 4294967295]),
                    ],
                ),
            }
        ),
        PHYSICAL_ROUTER_USER_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_USER_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_MANAGEMENT_MAC: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_MANAGEMENT_MAC.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_UNDERLAY_MANAGED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PHYSICAL_ROUTER_UNDERLAY_MANAGED.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_DEVICE_FAMILY: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_DEVICE_FAMILY.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_MANAGEMENT_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_MANAGEMENT_IP.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_VENDOR_NAME: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_VENDOR_NAME.'),
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
        PHYSICAL_ROUTER_UNDERLAY_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_UNDERLAY_CONFIG.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_MANAGED_STATE: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_MANAGED_STATE.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_CLI_COMMIT_STATE: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_CLI_COMMIT_STATE.'),
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
        TELEMETRY_INFO: properties.Schema(
            properties.Schema.MAP,
            _('TELEMETRY_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                TELEMETRY_INFO_RESOURCE: properties.Schema(
                    properties.Schema.LIST,
                    _('TELEMETRY_INFO_RESOURCE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            TELEMETRY_INFO_RESOURCE_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('TELEMETRY_INFO_RESOURCE_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            TELEMETRY_INFO_RESOURCE_PATH: properties.Schema(
                                properties.Schema.STRING,
                                _('TELEMETRY_INFO_RESOURCE_PATH.'),
                                update_allowed=True,
                                required=False,
                            ),
                            TELEMETRY_INFO_RESOURCE_RATE: properties.Schema(
                                properties.Schema.STRING,
                                _('TELEMETRY_INFO_RESOURCE_RATE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
                TELEMETRY_INFO_SERVER_IP: properties.Schema(
                    properties.Schema.STRING,
                    _('TELEMETRY_INFO_SERVER_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                TELEMETRY_INFO_SERVER_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('TELEMETRY_INFO_SERVER_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_DHCP_PARAMETERS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_DHCP_PARAMETERS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_DATAPLANE_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_DATAPLANE_IP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_OS_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_OS_VERSION.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_VNC_MANAGED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PHYSICAL_ROUTER_VNC_MANAGED.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_ROLE: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_ROLE.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_SERIAL_NUMBER: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_SERIAL_NUMBER.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_SNMP_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_SNMP_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_PRODUCT_NAME: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_PRODUCT_NAME.'),
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
        PHYSICAL_ROUTER_LLDP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PHYSICAL_ROUTER_LLDP.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_BRIDGING_ROLES: properties.Schema(
            properties.Schema.MAP,
            _('ROUTING_BRIDGING_ROLES.'),
            update_allowed=True,
            required=False,
            schema={
                ROUTING_BRIDGING_ROLES_RB_ROLES: properties.Schema(
                    properties.Schema.LIST,
                    _('ROUTING_BRIDGING_ROLES_RB_ROLES.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_LOOPBACK_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_LOOPBACK_IP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_ENCRYPTION_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_ENCRYPTION_TYPE.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_HOSTNAME: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_HOSTNAME.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_SNMP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PHYSICAL_ROUTER_SNMP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT: properties.Schema(
                    properties.Schema.LIST,
                    _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        DEVICE_FUNCTIONAL_GROUP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('DEVICE_FUNCTIONAL_GROUP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        OVERLAY_ROLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('OVERLAY_ROLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NODE_PROFILE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NODE_PROFILE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_ROUTER_REFS.'),
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
        FABRIC_REFS: properties.Schema(
            properties.Schema.LIST,
            _('FABRIC_REFS.'),
            update_allowed=True,
            required=False,
        ),
        DEVICE_IMAGE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('DEVICE_IMAGE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        TELEMETRY_PROFILE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TELEMETRY_PROFILE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        DEVICE_CHASSIS_REFS: properties.Schema(
            properties.Schema.LIST,
            _('DEVICE_CHASSIS_REFS.'),
            update_allowed=True,
            required=False,
        ),
        INTENT_MAP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('INTENT_MAP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_ROLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
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
        PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM: attributes.Schema(
            _('PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM.'),
        ),
        PHYSICAL_ROUTER_USER_CREDENTIALS: attributes.Schema(
            _('PHYSICAL_ROUTER_USER_CREDENTIALS.'),
        ),
        PHYSICAL_ROUTER_MANAGEMENT_MAC: attributes.Schema(
            _('PHYSICAL_ROUTER_MANAGEMENT_MAC.'),
        ),
        PHYSICAL_ROUTER_UNDERLAY_MANAGED: attributes.Schema(
            _('PHYSICAL_ROUTER_UNDERLAY_MANAGED.'),
        ),
        PHYSICAL_ROUTER_DEVICE_FAMILY: attributes.Schema(
            _('PHYSICAL_ROUTER_DEVICE_FAMILY.'),
        ),
        PHYSICAL_ROUTER_MANAGEMENT_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_MANAGEMENT_IP.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PHYSICAL_ROUTER_VENDOR_NAME: attributes.Schema(
            _('PHYSICAL_ROUTER_VENDOR_NAME.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        PHYSICAL_ROUTER_UNDERLAY_CONFIG: attributes.Schema(
            _('PHYSICAL_ROUTER_UNDERLAY_CONFIG.'),
        ),
        PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP.'),
        ),
        PHYSICAL_ROUTER_MANAGED_STATE: attributes.Schema(
            _('PHYSICAL_ROUTER_MANAGED_STATE.'),
        ),
        PHYSICAL_ROUTER_CLI_COMMIT_STATE: attributes.Schema(
            _('PHYSICAL_ROUTER_CLI_COMMIT_STATE.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        TELEMETRY_INFO: attributes.Schema(
            _('TELEMETRY_INFO.'),
        ),
        PHYSICAL_ROUTER_DHCP_PARAMETERS: attributes.Schema(
            _('PHYSICAL_ROUTER_DHCP_PARAMETERS.'),
        ),
        PHYSICAL_ROUTER_DATAPLANE_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_DATAPLANE_IP.'),
        ),
        PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG: attributes.Schema(
            _('PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG.'),
        ),
        PHYSICAL_ROUTER_OS_VERSION: attributes.Schema(
            _('PHYSICAL_ROUTER_OS_VERSION.'),
        ),
        PHYSICAL_ROUTER_VNC_MANAGED: attributes.Schema(
            _('PHYSICAL_ROUTER_VNC_MANAGED.'),
        ),
        PHYSICAL_ROUTER_ROLE: attributes.Schema(
            _('PHYSICAL_ROUTER_ROLE.'),
        ),
        PHYSICAL_ROUTER_SERIAL_NUMBER: attributes.Schema(
            _('PHYSICAL_ROUTER_SERIAL_NUMBER.'),
        ),
        PHYSICAL_ROUTER_SNMP_CREDENTIALS: attributes.Schema(
            _('PHYSICAL_ROUTER_SNMP_CREDENTIALS.'),
        ),
        PHYSICAL_ROUTER_PRODUCT_NAME: attributes.Schema(
            _('PHYSICAL_ROUTER_PRODUCT_NAME.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PHYSICAL_ROUTER_LLDP: attributes.Schema(
            _('PHYSICAL_ROUTER_LLDP.'),
        ),
        ROUTING_BRIDGING_ROLES: attributes.Schema(
            _('ROUTING_BRIDGING_ROLES.'),
        ),
        PHYSICAL_ROUTER_LOOPBACK_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_LOOPBACK_IP.'),
        ),
        PHYSICAL_ROUTER_ENCRYPTION_TYPE: attributes.Schema(
            _('PHYSICAL_ROUTER_ENCRYPTION_TYPE.'),
        ),
        PHYSICAL_ROUTER_HOSTNAME: attributes.Schema(
            _('PHYSICAL_ROUTER_HOSTNAME.'),
        ),
        PHYSICAL_ROUTER_SNMP: attributes.Schema(
            _('PHYSICAL_ROUTER_SNMP.'),
        ),
        PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS: attributes.Schema(
            _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS.'),
        ),
        DEVICE_FUNCTIONAL_GROUP_REFS: attributes.Schema(
            _('DEVICE_FUNCTIONAL_GROUP_REFS.'),
        ),
        OVERLAY_ROLE_REFS: attributes.Schema(
            _('OVERLAY_ROLE_REFS.'),
        ),
        NODE_PROFILE_REFS: attributes.Schema(
            _('NODE_PROFILE_REFS.'),
        ),
        VIRTUAL_ROUTER_REFS: attributes.Schema(
            _('VIRTUAL_ROUTER_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        FABRIC_REFS: attributes.Schema(
            _('FABRIC_REFS.'),
        ),
        DEVICE_IMAGE_REFS: attributes.Schema(
            _('DEVICE_IMAGE_REFS.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
        TELEMETRY_PROFILE_REFS: attributes.Schema(
            _('TELEMETRY_PROFILE_REFS.'),
        ),
        DEVICE_CHASSIS_REFS: attributes.Schema(
            _('DEVICE_CHASSIS_REFS.'),
        ),
        INTENT_MAP_REFS: attributes.Schema(
            _('INTENT_MAP_REFS.'),
        ),
        PHYSICAL_ROLE_REFS: attributes.Schema(
            _('PHYSICAL_ROLE_REFS.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(id=str(uuid.UUID(self.properties.get(self.GLOBAL_SYSTEM_CONFIG))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.PhysicalRouter(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM) is not None:
            obj_1 = vnc_api.AutonomousSystemsType()
            if self.properties.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN) is not None:
                for index_1 in range(len(self.properties.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN))):
                    obj_1.add_asn(self.properties.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN)[index_1])
            obj_0.set_physical_router_autonomous_system(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME))
            if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD))
            obj_0.set_physical_router_user_credentials(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_MAC) is not None:
            obj_0.set_physical_router_management_mac(self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_MAC))
        if self.properties.get(self.PHYSICAL_ROUTER_UNDERLAY_MANAGED) is not None:
            obj_0.set_physical_router_underlay_managed(self.properties.get(self.PHYSICAL_ROUTER_UNDERLAY_MANAGED))
        if self.properties.get(self.PHYSICAL_ROUTER_DEVICE_FAMILY) is not None:
            obj_0.set_physical_router_device_family(self.properties.get(self.PHYSICAL_ROUTER_DEVICE_FAMILY))
        if self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP) is not None:
            obj_0.set_physical_router_management_ip(self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PHYSICAL_ROUTER_VENDOR_NAME) is not None:
            obj_0.set_physical_router_vendor_name(self.properties.get(self.PHYSICAL_ROUTER_VENDOR_NAME))
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
        if self.properties.get(self.PHYSICAL_ROUTER_UNDERLAY_CONFIG) is not None:
            obj_0.set_physical_router_underlay_config(self.properties.get(self.PHYSICAL_ROUTER_UNDERLAY_CONFIG))
        if self.properties.get(self.PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP) is not None:
            obj_0.set_physical_router_replicator_loopback_ip(self.properties.get(self.PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP))
        if self.properties.get(self.PHYSICAL_ROUTER_MANAGED_STATE) is not None:
            obj_0.set_physical_router_managed_state(self.properties.get(self.PHYSICAL_ROUTER_MANAGED_STATE))
        if self.properties.get(self.PHYSICAL_ROUTER_CLI_COMMIT_STATE) is not None:
            obj_0.set_physical_router_cli_commit_state(self.properties.get(self.PHYSICAL_ROUTER_CLI_COMMIT_STATE))
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
        if self.properties.get(self.TELEMETRY_INFO) is not None:
            obj_1 = vnc_api.TelemetryStateInfo()
            if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE) is not None:
                for index_1 in range(len(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE))):
                    obj_2 = vnc_api.TelemetryResourceInfo()
                    if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_NAME) is not None:
                        obj_2.set_name(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_NAME))
                    if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_PATH) is not None:
                        obj_2.set_path(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_PATH))
                    if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_RATE) is not None:
                        obj_2.set_rate(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_RATE))
                    obj_1.add_resource(obj_2)
            if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_IP) is not None:
                obj_1.set_server_ip(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_IP))
            if self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_PORT) is not None:
                obj_1.set_server_port(self.properties.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_PORT))
            obj_0.set_telemetry_info(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS) is not None:
            obj_1 = vnc_api.DnsmasqLeaseParameters()
            if self.properties.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME) is not None:
                obj_1.set_lease_expiry_time(self.properties.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME))
            if self.properties.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID) is not None:
                obj_1.set_client_id(self.properties.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID))
            obj_0.set_physical_router_dhcp_parameters(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_DATAPLANE_IP) is not None:
            obj_0.set_physical_router_dataplane_ip(self.properties.get(self.PHYSICAL_ROUTER_DATAPLANE_IP))
        if self.properties.get(self.PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG) is not None:
            obj_0.set_physical_router_supplemental_config(self.properties.get(self.PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG))
        if self.properties.get(self.PHYSICAL_ROUTER_OS_VERSION) is not None:
            obj_0.set_physical_router_os_version(self.properties.get(self.PHYSICAL_ROUTER_OS_VERSION))
        if self.properties.get(self.PHYSICAL_ROUTER_VNC_MANAGED) is not None:
            obj_0.set_physical_router_vnc_managed(self.properties.get(self.PHYSICAL_ROUTER_VNC_MANAGED))
        if self.properties.get(self.PHYSICAL_ROUTER_ROLE) is not None:
            obj_0.set_physical_router_role(self.properties.get(self.PHYSICAL_ROUTER_ROLE))
        if self.properties.get(self.PHYSICAL_ROUTER_SERIAL_NUMBER) is not None:
            obj_0.set_physical_router_serial_number(self.properties.get(self.PHYSICAL_ROUTER_SERIAL_NUMBER))
        if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS) is not None:
            obj_1 = vnc_api.SNMPCredentials()
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION) is not None:
                obj_1.set_version(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT) is not None:
                obj_1.set_local_port(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES) is not None:
                obj_1.set_retries(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT) is not None:
                obj_1.set_timeout(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY) is not None:
                obj_1.set_v2_community(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME) is not None:
                obj_1.set_v3_security_name(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL) is not None:
                obj_1.set_v3_security_level(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID) is not None:
                obj_1.set_v3_security_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT) is not None:
                obj_1.set_v3_context(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID) is not None:
                obj_1.set_v3_context_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL) is not None:
                obj_1.set_v3_authentication_protocol(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD) is not None:
                obj_1.set_v3_authentication_password(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL) is not None:
                obj_1.set_v3_privacy_protocol(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD) is not None:
                obj_1.set_v3_privacy_password(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID) is not None:
                obj_1.set_v3_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS) is not None:
                obj_1.set_v3_engine_boots(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME) is not None:
                obj_1.set_v3_engine_time(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME))
            obj_0.set_physical_router_snmp_credentials(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_PRODUCT_NAME) is not None:
            obj_0.set_physical_router_product_name(self.properties.get(self.PHYSICAL_ROUTER_PRODUCT_NAME))
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
        if self.properties.get(self.PHYSICAL_ROUTER_LLDP) is not None:
            obj_0.set_physical_router_lldp(self.properties.get(self.PHYSICAL_ROUTER_LLDP))
        if self.properties.get(self.ROUTING_BRIDGING_ROLES) is not None:
            obj_1 = vnc_api.RoutingBridgingRolesType()
            if self.properties.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES) is not None:
                for index_1 in range(len(self.properties.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES))):
                    obj_1.add_rb_roles(self.properties.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES)[index_1])
            obj_0.set_routing_bridging_roles(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_LOOPBACK_IP) is not None:
            obj_0.set_physical_router_loopback_ip(self.properties.get(self.PHYSICAL_ROUTER_LOOPBACK_IP))
        if self.properties.get(self.PHYSICAL_ROUTER_ENCRYPTION_TYPE) is not None:
            obj_0.set_physical_router_encryption_type(self.properties.get(self.PHYSICAL_ROUTER_ENCRYPTION_TYPE))
        if self.properties.get(self.PHYSICAL_ROUTER_HOSTNAME) is not None:
            obj_0.set_physical_router_hostname(self.properties.get(self.PHYSICAL_ROUTER_HOSTNAME))
        if self.properties.get(self.PHYSICAL_ROUTER_SNMP) is not None:
            obj_0.set_physical_router_snmp(self.properties.get(self.PHYSICAL_ROUTER_SNMP))
        if self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS) is not None:
            obj_1 = vnc_api.JunosServicePorts()
            if self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT) is not None:
                for index_1 in range(len(self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT))):
                    obj_1.add_service_port(self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT)[index_1])
            obj_0.set_physical_router_junos_service_ports(obj_1)

        # reference to device_functional_group_refs
        if self.properties.get(self.DEVICE_FUNCTIONAL_GROUP_REFS):
            for index_0 in range(len(self.properties.get(self.DEVICE_FUNCTIONAL_GROUP_REFS))):
                try:
                    ref_obj = self.vnc_lib().device_functional_group_read(
                        id=self.properties.get(self.DEVICE_FUNCTIONAL_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_functional_group_read(
                        fq_name_str=self.properties.get(self.DEVICE_FUNCTIONAL_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_device_functional_group(ref_obj)

        # reference to overlay_role_refs
        if self.properties.get(self.OVERLAY_ROLE_REFS):
            for index_0 in range(len(self.properties.get(self.OVERLAY_ROLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().overlay_role_read(
                        id=self.properties.get(self.OVERLAY_ROLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().overlay_role_read(
                        fq_name_str=self.properties.get(self.OVERLAY_ROLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_overlay_role(ref_obj)

        # reference to node_profile_refs
        if self.properties.get(self.NODE_PROFILE_REFS):
            for index_0 in range(len(self.properties.get(self.NODE_PROFILE_REFS))):
                try:
                    ref_obj = self.vnc_lib().node_profile_read(
                        id=self.properties.get(self.NODE_PROFILE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().node_profile_read(
                        fq_name_str=self.properties.get(self.NODE_PROFILE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_node_profile(ref_obj)

        # reference to virtual_router_refs
        if self.properties.get(self.VIRTUAL_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        id=self.properties.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_virtual_router(ref_obj)

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

        # reference to fabric_refs
        if self.properties.get(self.FABRIC_REFS):
            for index_0 in range(len(self.properties.get(self.FABRIC_REFS))):
                try:
                    ref_obj = self.vnc_lib().fabric_read(
                        id=self.properties.get(self.FABRIC_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().fabric_read(
                        fq_name_str=self.properties.get(self.FABRIC_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_fabric(ref_obj)

        # reference to device_image_refs
        if self.properties.get(self.DEVICE_IMAGE_REFS):
            for index_0 in range(len(self.properties.get(self.DEVICE_IMAGE_REFS))):
                try:
                    ref_obj = self.vnc_lib().device_image_read(
                        id=self.properties.get(self.DEVICE_IMAGE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_image_read(
                        fq_name_str=self.properties.get(self.DEVICE_IMAGE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_device_image(ref_obj)

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

        # reference to telemetry_profile_refs
        if self.properties.get(self.TELEMETRY_PROFILE_REFS):
            for index_0 in range(len(self.properties.get(self.TELEMETRY_PROFILE_REFS))):
                try:
                    ref_obj = self.vnc_lib().telemetry_profile_read(
                        id=self.properties.get(self.TELEMETRY_PROFILE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().telemetry_profile_read(
                        fq_name_str=self.properties.get(self.TELEMETRY_PROFILE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_telemetry_profile(ref_obj)

        # reference to device_chassis_refs
        if self.properties.get(self.DEVICE_CHASSIS_REFS):
            for index_0 in range(len(self.properties.get(self.DEVICE_CHASSIS_REFS))):
                try:
                    ref_obj = self.vnc_lib().device_chassis_read(
                        id=self.properties.get(self.DEVICE_CHASSIS_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_chassis_read(
                        fq_name_str=self.properties.get(self.DEVICE_CHASSIS_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_device_chassis(ref_obj)

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

        # reference to physical_role_refs
        if self.properties.get(self.PHYSICAL_ROLE_REFS):
            for index_0 in range(len(self.properties.get(self.PHYSICAL_ROLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().physical_role_read(
                        id=self.properties.get(self.PHYSICAL_ROLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().physical_role_read(
                        fq_name_str=self.properties.get(self.PHYSICAL_ROLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_physical_role(ref_obj)

        try:
            obj_uuid = super(ContrailPhysicalRouter, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().physical_router_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM) is not None:
            obj_1 = vnc_api.AutonomousSystemsType()
            if prop_diff.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN) is not None:
                for index_1 in range(len(prop_diff.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN))):
                    obj_1.add_asn(prop_diff.get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM, {}).get(self.PHYSICAL_ROUTER_AUTONOMOUS_SYSTEM_ASN)[index_1])
            obj_0.set_physical_router_autonomous_system(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME))
            if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD))
            obj_0.set_physical_router_user_credentials(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_MAC) is not None:
            obj_0.set_physical_router_management_mac(prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_MAC))
        if prop_diff.get(self.PHYSICAL_ROUTER_UNDERLAY_MANAGED) is not None:
            obj_0.set_physical_router_underlay_managed(prop_diff.get(self.PHYSICAL_ROUTER_UNDERLAY_MANAGED))
        if prop_diff.get(self.PHYSICAL_ROUTER_DEVICE_FAMILY) is not None:
            obj_0.set_physical_router_device_family(prop_diff.get(self.PHYSICAL_ROUTER_DEVICE_FAMILY))
        if prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP) is not None:
            obj_0.set_physical_router_management_ip(prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_VENDOR_NAME) is not None:
            obj_0.set_physical_router_vendor_name(prop_diff.get(self.PHYSICAL_ROUTER_VENDOR_NAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_UNDERLAY_CONFIG) is not None:
            obj_0.set_physical_router_underlay_config(prop_diff.get(self.PHYSICAL_ROUTER_UNDERLAY_CONFIG))
        if prop_diff.get(self.PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP) is not None:
            obj_0.set_physical_router_replicator_loopback_ip(prop_diff.get(self.PHYSICAL_ROUTER_REPLICATOR_LOOPBACK_IP))
        if prop_diff.get(self.PHYSICAL_ROUTER_MANAGED_STATE) is not None:
            obj_0.set_physical_router_managed_state(prop_diff.get(self.PHYSICAL_ROUTER_MANAGED_STATE))
        if prop_diff.get(self.PHYSICAL_ROUTER_CLI_COMMIT_STATE) is not None:
            obj_0.set_physical_router_cli_commit_state(prop_diff.get(self.PHYSICAL_ROUTER_CLI_COMMIT_STATE))
        if prop_diff.get(self.TELEMETRY_INFO) is not None:
            obj_1 = vnc_api.TelemetryStateInfo()
            if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE) is not None:
                for index_1 in range(len(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE))):
                    obj_2 = vnc_api.TelemetryResourceInfo()
                    if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_NAME) is not None:
                        obj_2.set_name(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_NAME))
                    if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_PATH) is not None:
                        obj_2.set_path(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_PATH))
                    if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_RATE) is not None:
                        obj_2.set_rate(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_RESOURCE, {})[index_1].get(self.TELEMETRY_INFO_RESOURCE_RATE))
                    obj_1.add_resource(obj_2)
            if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_IP) is not None:
                obj_1.set_server_ip(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_IP))
            if prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_PORT) is not None:
                obj_1.set_server_port(prop_diff.get(self.TELEMETRY_INFO, {}).get(self.TELEMETRY_INFO_SERVER_PORT))
            obj_0.set_telemetry_info(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS) is not None:
            obj_1 = vnc_api.DnsmasqLeaseParameters()
            if prop_diff.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME) is not None:
                obj_1.set_lease_expiry_time(prop_diff.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_LEASE_EXPIRY_TIME))
            if prop_diff.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID) is not None:
                obj_1.set_client_id(prop_diff.get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS, {}).get(self.PHYSICAL_ROUTER_DHCP_PARAMETERS_CLIENT_ID))
            obj_0.set_physical_router_dhcp_parameters(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_DATAPLANE_IP) is not None:
            obj_0.set_physical_router_dataplane_ip(prop_diff.get(self.PHYSICAL_ROUTER_DATAPLANE_IP))
        if prop_diff.get(self.PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG) is not None:
            obj_0.set_physical_router_supplemental_config(prop_diff.get(self.PHYSICAL_ROUTER_SUPPLEMENTAL_CONFIG))
        if prop_diff.get(self.PHYSICAL_ROUTER_OS_VERSION) is not None:
            obj_0.set_physical_router_os_version(prop_diff.get(self.PHYSICAL_ROUTER_OS_VERSION))
        if prop_diff.get(self.PHYSICAL_ROUTER_VNC_MANAGED) is not None:
            obj_0.set_physical_router_vnc_managed(prop_diff.get(self.PHYSICAL_ROUTER_VNC_MANAGED))
        if prop_diff.get(self.PHYSICAL_ROUTER_ROLE) is not None:
            obj_0.set_physical_router_role(prop_diff.get(self.PHYSICAL_ROUTER_ROLE))
        if prop_diff.get(self.PHYSICAL_ROUTER_SERIAL_NUMBER) is not None:
            obj_0.set_physical_router_serial_number(prop_diff.get(self.PHYSICAL_ROUTER_SERIAL_NUMBER))
        if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS) is not None:
            obj_1 = vnc_api.SNMPCredentials()
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION) is not None:
                obj_1.set_version(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT) is not None:
                obj_1.set_local_port(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES) is not None:
                obj_1.set_retries(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT) is not None:
                obj_1.set_timeout(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY) is not None:
                obj_1.set_v2_community(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME) is not None:
                obj_1.set_v3_security_name(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL) is not None:
                obj_1.set_v3_security_level(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID) is not None:
                obj_1.set_v3_security_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT) is not None:
                obj_1.set_v3_context(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID) is not None:
                obj_1.set_v3_context_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL) is not None:
                obj_1.set_v3_authentication_protocol(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD) is not None:
                obj_1.set_v3_authentication_password(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL) is not None:
                obj_1.set_v3_privacy_protocol(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD) is not None:
                obj_1.set_v3_privacy_password(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID) is not None:
                obj_1.set_v3_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS) is not None:
                obj_1.set_v3_engine_boots(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME) is not None:
                obj_1.set_v3_engine_time(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME))
            obj_0.set_physical_router_snmp_credentials(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_PRODUCT_NAME) is not None:
            obj_0.set_physical_router_product_name(prop_diff.get(self.PHYSICAL_ROUTER_PRODUCT_NAME))
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
        if prop_diff.get(self.PHYSICAL_ROUTER_LLDP) is not None:
            obj_0.set_physical_router_lldp(prop_diff.get(self.PHYSICAL_ROUTER_LLDP))
        if prop_diff.get(self.ROUTING_BRIDGING_ROLES) is not None:
            obj_1 = vnc_api.RoutingBridgingRolesType()
            if prop_diff.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES) is not None:
                for index_1 in range(len(prop_diff.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES))):
                    obj_1.add_rb_roles(prop_diff.get(self.ROUTING_BRIDGING_ROLES, {}).get(self.ROUTING_BRIDGING_ROLES_RB_ROLES)[index_1])
            obj_0.set_routing_bridging_roles(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_LOOPBACK_IP) is not None:
            obj_0.set_physical_router_loopback_ip(prop_diff.get(self.PHYSICAL_ROUTER_LOOPBACK_IP))
        if prop_diff.get(self.PHYSICAL_ROUTER_ENCRYPTION_TYPE) is not None:
            obj_0.set_physical_router_encryption_type(prop_diff.get(self.PHYSICAL_ROUTER_ENCRYPTION_TYPE))
        if prop_diff.get(self.PHYSICAL_ROUTER_HOSTNAME) is not None:
            obj_0.set_physical_router_hostname(prop_diff.get(self.PHYSICAL_ROUTER_HOSTNAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_SNMP) is not None:
            obj_0.set_physical_router_snmp(prop_diff.get(self.PHYSICAL_ROUTER_SNMP))
        if prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS) is not None:
            obj_1 = vnc_api.JunosServicePorts()
            if prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT) is not None:
                for index_1 in range(len(prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT))):
                    obj_1.add_service_port(prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT)[index_1])
            obj_0.set_physical_router_junos_service_ports(obj_1)

        # reference to device_functional_group_refs
        ref_obj_list = []
        if self.DEVICE_FUNCTIONAL_GROUP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.DEVICE_FUNCTIONAL_GROUP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().device_functional_group_read(
                        id=prop_diff.get(self.DEVICE_FUNCTIONAL_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_functional_group_read(
                        fq_name_str=prop_diff.get(self.DEVICE_FUNCTIONAL_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_device_functional_group_list(ref_obj_list)
            # End: reference to device_functional_group_refs

        # reference to overlay_role_refs
        ref_obj_list = []
        if self.OVERLAY_ROLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.OVERLAY_ROLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().overlay_role_read(
                        id=prop_diff.get(self.OVERLAY_ROLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().overlay_role_read(
                        fq_name_str=prop_diff.get(self.OVERLAY_ROLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_overlay_role_list(ref_obj_list)
            # End: reference to overlay_role_refs

        # reference to node_profile_refs
        ref_obj_list = []
        if self.NODE_PROFILE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NODE_PROFILE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().node_profile_read(
                        id=prop_diff.get(self.NODE_PROFILE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().node_profile_read(
                        fq_name_str=prop_diff.get(self.NODE_PROFILE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_node_profile_list(ref_obj_list)
            # End: reference to node_profile_refs

        # reference to virtual_router_refs
        ref_obj_list = []
        if self.VIRTUAL_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        id=prop_diff.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_router_list(ref_obj_list)
            # End: reference to virtual_router_refs

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

        # reference to fabric_refs
        ref_obj_list = []
        if self.FABRIC_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.FABRIC_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().fabric_read(
                        id=prop_diff.get(self.FABRIC_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().fabric_read(
                        fq_name_str=prop_diff.get(self.FABRIC_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_fabric_list(ref_obj_list)
            # End: reference to fabric_refs

        # reference to device_image_refs
        ref_obj_list = []
        if self.DEVICE_IMAGE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.DEVICE_IMAGE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().device_image_read(
                        id=prop_diff.get(self.DEVICE_IMAGE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_image_read(
                        fq_name_str=prop_diff.get(self.DEVICE_IMAGE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_device_image_list(ref_obj_list)
            # End: reference to device_image_refs

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

        # reference to telemetry_profile_refs
        ref_obj_list = []
        if self.TELEMETRY_PROFILE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TELEMETRY_PROFILE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().telemetry_profile_read(
                        id=prop_diff.get(self.TELEMETRY_PROFILE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().telemetry_profile_read(
                        fq_name_str=prop_diff.get(self.TELEMETRY_PROFILE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_telemetry_profile_list(ref_obj_list)
            # End: reference to telemetry_profile_refs

        # reference to device_chassis_refs
        ref_obj_list = []
        if self.DEVICE_CHASSIS_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.DEVICE_CHASSIS_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().device_chassis_read(
                        id=prop_diff.get(self.DEVICE_CHASSIS_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().device_chassis_read(
                        fq_name_str=prop_diff.get(self.DEVICE_CHASSIS_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_device_chassis_list(ref_obj_list)
            # End: reference to device_chassis_refs

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

        # reference to physical_role_refs
        ref_obj_list = []
        if self.PHYSICAL_ROLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_ROLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().physical_role_read(
                        id=prop_diff.get(self.PHYSICAL_ROLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().physical_role_read(
                        fq_name_str=prop_diff.get(self.PHYSICAL_ROLE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_physical_role_list(ref_obj_list)
            # End: reference to physical_role_refs

        try:
            self.vnc_lib().physical_router_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().physical_router_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('physical_router %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().physical_router_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::PhysicalRouter': ContrailPhysicalRouter,
    }
