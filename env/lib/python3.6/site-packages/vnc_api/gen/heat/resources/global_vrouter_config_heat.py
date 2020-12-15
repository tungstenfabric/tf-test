
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


class ContrailGlobalVrouterConfig(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ECMP_HASHING_INCLUDE_FIELDS, ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP, ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT, FLOW_AGING_TIMEOUT_LIST, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS, DISPLAY_NAME, PORT_TRANSLATION_POOLS, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT, PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT, FORWARDING_MODE, ENCRYPTION_MODE, FLOW_EXPORT_RATE, LINKLOCAL_SERVICES, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ENCAPSULATION_PRIORITIES, ENCAPSULATION_PRIORITIES_ENCAPSULATION, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, ENCRYPTION_TUNNEL_ENDPOINTS, ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT, ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS, VXLAN_NETWORK_IDENTIFIER_MODE, ENABLE_SECURITY_LOGGING, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'ecmp_hashing_include_fields', 'ecmp_hashing_include_fields_hashing_configured', 'ecmp_hashing_include_fields_source_ip', 'ecmp_hashing_include_fields_destination_ip', 'ecmp_hashing_include_fields_ip_protocol', 'ecmp_hashing_include_fields_source_port', 'ecmp_hashing_include_fields_destination_port', 'flow_aging_timeout_list', 'flow_aging_timeout_list_flow_aging_timeout', 'flow_aging_timeout_list_flow_aging_timeout_protocol', 'flow_aging_timeout_list_flow_aging_timeout_port', 'flow_aging_timeout_list_flow_aging_timeout_timeout_in_seconds', 'display_name', 'port_translation_pools', 'port_translation_pools_port_translation_pool', 'port_translation_pools_port_translation_pool_protocol', 'port_translation_pools_port_translation_pool_port_range', 'port_translation_pools_port_translation_pool_port_range_start_port', 'port_translation_pools_port_translation_pool_port_range_end_port', 'port_translation_pools_port_translation_pool_port_count', 'forwarding_mode', 'encryption_mode', 'flow_export_rate', 'linklocal_services', 'linklocal_services_linklocal_service_entry', 'linklocal_services_linklocal_service_entry_linklocal_service_name', 'linklocal_services_linklocal_service_entry_linklocal_service_ip', 'linklocal_services_linklocal_service_entry_linklocal_service_port', 'linklocal_services_linklocal_service_entry_ip_fabric_DNS_service_name', 'linklocal_services_linklocal_service_entry_ip_fabric_service_port', 'linklocal_services_linklocal_service_entry_ip_fabric_service_ip', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'encapsulation_priorities', 'encapsulation_priorities_encapsulation', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'encryption_tunnel_endpoints', 'encryption_tunnel_endpoints_endpoint', 'encryption_tunnel_endpoints_endpoint_tunnel_remote_ip_address', 'vxlan_network_identifier_mode', 'enable_security_logging', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'global_system_config'
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
        FLOW_AGING_TIMEOUT_LIST: properties.Schema(
            properties.Schema.MAP,
            _('FLOW_AGING_TIMEOUT_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT: properties.Schema(
                    properties.Schema.LIST,
                    _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PORT_TRANSLATION_POOLS: properties.Schema(
            properties.Schema.MAP,
            _('PORT_TRANSLATION_POOLS.'),
            update_allowed=True,
            required=False,
            schema={
                PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL: properties.Schema(
                    properties.Schema.LIST,
                    _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE: properties.Schema(
                                properties.Schema.MAP,
                                _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(-1, 65535),
                                        ],
                                    ),
                                    PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(-1, 65535),
                                        ],
                                    ),
                                }
                            ),
                            PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT: properties.Schema(
                                properties.Schema.STRING,
                                _('PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        FORWARDING_MODE: properties.Schema(
            properties.Schema.STRING,
            _('FORWARDING_MODE.'),
            update_allowed=True,
            required=False,
        ),
        ENCRYPTION_MODE: properties.Schema(
            properties.Schema.STRING,
            _('ENCRYPTION_MODE.'),
            update_allowed=True,
            required=False,
        ),
        FLOW_EXPORT_RATE: properties.Schema(
            properties.Schema.INTEGER,
            _('FLOW_EXPORT_RATE.'),
            update_allowed=True,
            required=False,
        ),
        LINKLOCAL_SERVICES: properties.Schema(
            properties.Schema.MAP,
            _('LINKLOCAL_SERVICES.'),
            update_allowed=True,
            required=False,
            schema={
                LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY: properties.Schema(
                    properties.Schema.LIST,
                    _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP: properties.Schema(
                                properties.Schema.LIST,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP.'),
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
        ENCAPSULATION_PRIORITIES: properties.Schema(
            properties.Schema.MAP,
            _('ENCAPSULATION_PRIORITIES.'),
            update_allowed=True,
            required=False,
            schema={
                ENCAPSULATION_PRIORITIES_ENCAPSULATION: properties.Schema(
                    properties.Schema.LIST,
                    _('ENCAPSULATION_PRIORITIES_ENCAPSULATION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'MPLSoGRE', u'MPLSoUDP', u'VXLAN']),
                    ],
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
        ENCRYPTION_TUNNEL_ENDPOINTS: properties.Schema(
            properties.Schema.MAP,
            _('ENCRYPTION_TUNNEL_ENDPOINTS.'),
            update_allowed=True,
            required=False,
            schema={
                ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT: properties.Schema(
                    properties.Schema.LIST,
                    _('ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VXLAN_NETWORK_IDENTIFIER_MODE: properties.Schema(
            properties.Schema.STRING,
            _('VXLAN_NETWORK_IDENTIFIER_MODE.'),
            update_allowed=True,
            required=False,
        ),
        ENABLE_SECURITY_LOGGING: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ENABLE_SECURITY_LOGGING.'),
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
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
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
        ECMP_HASHING_INCLUDE_FIELDS: attributes.Schema(
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
        ),
        FLOW_AGING_TIMEOUT_LIST: attributes.Schema(
            _('FLOW_AGING_TIMEOUT_LIST.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PORT_TRANSLATION_POOLS: attributes.Schema(
            _('PORT_TRANSLATION_POOLS.'),
        ),
        FORWARDING_MODE: attributes.Schema(
            _('FORWARDING_MODE.'),
        ),
        ENCRYPTION_MODE: attributes.Schema(
            _('ENCRYPTION_MODE.'),
        ),
        FLOW_EXPORT_RATE: attributes.Schema(
            _('FLOW_EXPORT_RATE.'),
        ),
        LINKLOCAL_SERVICES: attributes.Schema(
            _('LINKLOCAL_SERVICES.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ENCAPSULATION_PRIORITIES: attributes.Schema(
            _('ENCAPSULATION_PRIORITIES.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        ENCRYPTION_TUNNEL_ENDPOINTS: attributes.Schema(
            _('ENCRYPTION_TUNNEL_ENDPOINTS.'),
        ),
        VXLAN_NETWORK_IDENTIFIER_MODE: attributes.Schema(
            _('VXLAN_NETWORK_IDENTIFIER_MODE.'),
        ),
        ENABLE_SECURITY_LOGGING: attributes.Schema(
            _('ENABLE_SECURITY_LOGGING.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
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

        obj_0 = vnc_api.GlobalVrouterConfig(name=self.properties[self.NAME],
            parent_obj=parent_obj)

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
        if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST) is not None:
            obj_1 = vnc_api.FlowAgingTimeoutList()
            if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT) is not None:
                for index_1 in range(len(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT))):
                    obj_2 = vnc_api.FlowAgingTimeout()
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL))
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT) is not None:
                        obj_2.set_port(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT))
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS) is not None:
                        obj_2.set_timeout_in_seconds(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS))
                    obj_1.add_flow_aging_timeout(obj_2)
            obj_0.set_flow_aging_timeout_list(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PORT_TRANSLATION_POOLS) is not None:
            obj_1 = vnc_api.PortTranslationPools()
            if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL) is not None:
                for index_1 in range(len(self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL))):
                    obj_2 = vnc_api.PortTranslationPool()
                    if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL))
                    if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE) is not None:
                        obj_3 = vnc_api.PortType()
                        if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT) is not None:
                            obj_3.set_start_port(self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT))
                        if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT) is not None:
                            obj_3.set_end_port(self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT))
                        obj_2.set_port_range(obj_3)
                    if self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT) is not None:
                        obj_2.set_port_count(self.properties.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT))
                    obj_1.add_port_translation_pool(obj_2)
            obj_0.set_port_translation_pools(obj_1)
        if self.properties.get(self.FORWARDING_MODE) is not None:
            obj_0.set_forwarding_mode(self.properties.get(self.FORWARDING_MODE))
        if self.properties.get(self.ENCRYPTION_MODE) is not None:
            obj_0.set_encryption_mode(self.properties.get(self.ENCRYPTION_MODE))
        if self.properties.get(self.FLOW_EXPORT_RATE) is not None:
            obj_0.set_flow_export_rate(self.properties.get(self.FLOW_EXPORT_RATE))
        if self.properties.get(self.LINKLOCAL_SERVICES) is not None:
            obj_1 = vnc_api.LinklocalServicesTypes()
            if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY) is not None:
                for index_1 in range(len(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY))):
                    obj_2 = vnc_api.LinklocalServiceEntryType()
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME) is not None:
                        obj_2.set_linklocal_service_name(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP) is not None:
                        obj_2.set_linklocal_service_ip(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT) is not None:
                        obj_2.set_linklocal_service_port(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME) is not None:
                        obj_2.set_ip_fabric_DNS_service_name(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT) is not None:
                        obj_2.set_ip_fabric_service_port(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP) is not None:
                        for index_2 in range(len(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP))):
                            obj_2.add_ip_fabric_service_ip(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP)[index_2])
                    obj_1.add_linklocal_service_entry(obj_2)
            obj_0.set_linklocal_services(obj_1)
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
        if self.properties.get(self.ENCAPSULATION_PRIORITIES) is not None:
            obj_1 = vnc_api.EncapsulationPrioritiesType()
            if self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION) is not None:
                for index_1 in range(len(self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION))):
                    obj_1.add_encapsulation(self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION)[index_1])
            obj_0.set_encapsulation_priorities(obj_1)
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
        if self.properties.get(self.ENCRYPTION_TUNNEL_ENDPOINTS) is not None:
            obj_1 = vnc_api.EncryptionTunnelEndpointList()
            if self.properties.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT) is not None:
                for index_1 in range(len(self.properties.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT))):
                    obj_2 = vnc_api.EncryptionTunnelEndpoint()
                    if self.properties.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT, {})[index_1].get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS) is not None:
                        obj_2.set_tunnel_remote_ip_address(self.properties.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT, {})[index_1].get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS))
                    obj_1.add_endpoint(obj_2)
            obj_0.set_encryption_tunnel_endpoints(obj_1)
        if self.properties.get(self.VXLAN_NETWORK_IDENTIFIER_MODE) is not None:
            obj_0.set_vxlan_network_identifier_mode(self.properties.get(self.VXLAN_NETWORK_IDENTIFIER_MODE))
        if self.properties.get(self.ENABLE_SECURITY_LOGGING) is not None:
            obj_0.set_enable_security_logging(self.properties.get(self.ENABLE_SECURITY_LOGGING))
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
            obj_uuid = super(ContrailGlobalVrouterConfig, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().global_vrouter_config_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

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
        if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST) is not None:
            obj_1 = vnc_api.FlowAgingTimeoutList()
            if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT) is not None:
                for index_1 in range(len(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT))):
                    obj_2 = vnc_api.FlowAgingTimeout()
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL))
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT) is not None:
                        obj_2.set_port(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT))
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS) is not None:
                        obj_2.set_timeout_in_seconds(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS))
                    obj_1.add_flow_aging_timeout(obj_2)
            obj_0.set_flow_aging_timeout_list(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.PORT_TRANSLATION_POOLS) is not None:
            obj_1 = vnc_api.PortTranslationPools()
            if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL) is not None:
                for index_1 in range(len(prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL))):
                    obj_2 = vnc_api.PortTranslationPool()
                    if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PROTOCOL))
                    if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE) is not None:
                        obj_3 = vnc_api.PortType()
                        if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT) is not None:
                            obj_3.set_start_port(prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_START_PORT))
                        if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT) is not None:
                            obj_3.set_end_port(prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_RANGE_END_PORT))
                        obj_2.set_port_range(obj_3)
                    if prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT) is not None:
                        obj_2.set_port_count(prop_diff.get(self.PORT_TRANSLATION_POOLS, {}).get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL, {})[index_1].get(self.PORT_TRANSLATION_POOLS_PORT_TRANSLATION_POOL_PORT_COUNT))
                    obj_1.add_port_translation_pool(obj_2)
            obj_0.set_port_translation_pools(obj_1)
        if prop_diff.get(self.FORWARDING_MODE) is not None:
            obj_0.set_forwarding_mode(prop_diff.get(self.FORWARDING_MODE))
        if prop_diff.get(self.ENCRYPTION_MODE) is not None:
            obj_0.set_encryption_mode(prop_diff.get(self.ENCRYPTION_MODE))
        if prop_diff.get(self.FLOW_EXPORT_RATE) is not None:
            obj_0.set_flow_export_rate(prop_diff.get(self.FLOW_EXPORT_RATE))
        if prop_diff.get(self.LINKLOCAL_SERVICES) is not None:
            obj_1 = vnc_api.LinklocalServicesTypes()
            if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY) is not None:
                for index_1 in range(len(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY))):
                    obj_2 = vnc_api.LinklocalServiceEntryType()
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME) is not None:
                        obj_2.set_linklocal_service_name(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP) is not None:
                        obj_2.set_linklocal_service_ip(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT) is not None:
                        obj_2.set_linklocal_service_port(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME) is not None:
                        obj_2.set_ip_fabric_DNS_service_name(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT) is not None:
                        obj_2.set_ip_fabric_service_port(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP) is not None:
                        for index_2 in range(len(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP))):
                            obj_2.add_ip_fabric_service_ip(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP)[index_2])
                    obj_1.add_linklocal_service_entry(obj_2)
            obj_0.set_linklocal_services(obj_1)
        if prop_diff.get(self.ENCAPSULATION_PRIORITIES) is not None:
            obj_1 = vnc_api.EncapsulationPrioritiesType()
            if prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION) is not None:
                for index_1 in range(len(prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION))):
                    obj_1.add_encapsulation(prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION)[index_1])
            obj_0.set_encapsulation_priorities(obj_1)
        if prop_diff.get(self.ENCRYPTION_TUNNEL_ENDPOINTS) is not None:
            obj_1 = vnc_api.EncryptionTunnelEndpointList()
            if prop_diff.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT) is not None:
                for index_1 in range(len(prop_diff.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT))):
                    obj_2 = vnc_api.EncryptionTunnelEndpoint()
                    if prop_diff.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT, {})[index_1].get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS) is not None:
                        obj_2.set_tunnel_remote_ip_address(prop_diff.get(self.ENCRYPTION_TUNNEL_ENDPOINTS, {}).get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT, {})[index_1].get(self.ENCRYPTION_TUNNEL_ENDPOINTS_ENDPOINT_TUNNEL_REMOTE_IP_ADDRESS))
                    obj_1.add_endpoint(obj_2)
            obj_0.set_encryption_tunnel_endpoints(obj_1)
        if prop_diff.get(self.VXLAN_NETWORK_IDENTIFIER_MODE) is not None:
            obj_0.set_vxlan_network_identifier_mode(prop_diff.get(self.VXLAN_NETWORK_IDENTIFIER_MODE))
        if prop_diff.get(self.ENABLE_SECURITY_LOGGING) is not None:
            obj_0.set_enable_security_logging(prop_diff.get(self.ENABLE_SECURITY_LOGGING))
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
            self.vnc_lib().global_vrouter_config_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().global_vrouter_config_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('global_vrouter_config %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().global_vrouter_config_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::GlobalVrouterConfig': ContrailGlobalVrouterConfig,
    }
