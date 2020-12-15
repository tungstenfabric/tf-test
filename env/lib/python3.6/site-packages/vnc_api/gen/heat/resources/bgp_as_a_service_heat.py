
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


class ContrailBgpAsAService(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, BGPAAS_SHARED, BGPAAS_SESSION_ATTRIBUTES, BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER, BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN, BGPAAS_SESSION_ATTRIBUTES_PASSIVE, BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE, BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME, BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT, BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM, BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP, BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION, BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE, BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN, DISPLAY_NAME, BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT, BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, BGPAAS_IP_ADDRESS, AUTONOMOUS_SYSTEM, SERVICE_HEALTH_CHECK_REFS, CONTROL_NODE_ZONE_REFS, CONTROL_NODE_ZONE_REFS_DATA, CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE, BGP_ROUTER_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, TAG_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'bgpaas_shared', 'bgpaas_session_attributes', 'bgpaas_session_attributes_bgp_router', 'bgpaas_session_attributes_admin_down', 'bgpaas_session_attributes_passive', 'bgpaas_session_attributes_as_override', 'bgpaas_session_attributes_hold_time', 'bgpaas_session_attributes_loop_count', 'bgpaas_session_attributes_local_autonomous_system', 'bgpaas_session_attributes_address_families', 'bgpaas_session_attributes_address_families_family', 'bgpaas_session_attributes_auth_data', 'bgpaas_session_attributes_auth_data_key_type', 'bgpaas_session_attributes_auth_data_key_items', 'bgpaas_session_attributes_auth_data_key_items_key_id', 'bgpaas_session_attributes_auth_data_key_items_key', 'bgpaas_session_attributes_family_attributes', 'bgpaas_session_attributes_family_attributes_address_family', 'bgpaas_session_attributes_family_attributes_loop_count', 'bgpaas_session_attributes_family_attributes_prefix_limit', 'bgpaas_session_attributes_family_attributes_prefix_limit_maximum', 'bgpaas_session_attributes_family_attributes_prefix_limit_idle_timeout', 'bgpaas_session_attributes_family_attributes_default_tunnel_encap', 'bgpaas_session_attributes_private_as_action', 'bgpaas_session_attributes_route_origin_override', 'bgpaas_session_attributes_route_origin_override_origin_override', 'bgpaas_session_attributes_route_origin_override_origin', 'display_name', 'bgpaas_suppress_route_advertisement', 'bgpaas_ipv4_mapped_ipv6_nexthop', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'bgpaas_ip_address', 'autonomous_system', 'service_health_check_refs', 'control_node_zone_refs', 'control_node_zone_refs_data', 'control_node_zone_refs_data_bgpaas_control_node_zone_type', 'bgp_router_refs', 'virtual_machine_interface_refs', 'tag_refs', 'project'
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
        BGPAAS_SHARED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGPAAS_SHARED.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_SESSION_ATTRIBUTES: properties.Schema(
            properties.Schema.MAP,
            _('BGPAAS_SESSION_ATTRIBUTES.'),
            update_allowed=True,
            required=False,
            schema={
                BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER: properties.Schema(
                    properties.Schema.STRING,
                    _('BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_PASSIVE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_PASSIVE.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 65535),
                    ],
                ),
                BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 16),
                    ],
                ),
                BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES: properties.Schema(
                    properties.Schema.MAP,
                    _('BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY: properties.Schema(
                            properties.Schema.LIST,
                            _('BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'inet', u'inet-labeled', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet-mvpn', u'inet6-vpn']),
                            ],
                        ),
                    }
                ),
                BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA: properties.Schema(
                    properties.Schema.MAP,
                    _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE: properties.Schema(
                            properties.Schema.STRING,
                            _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'md5']),
                            ],
                        ),
                        BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS: properties.Schema(
                            properties.Schema.LIST,
                            _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS.'),
                            update_allowed=True,
                            required=False,
                            schema=properties.Schema(
                                properties.Schema.MAP,
                                schema={
                                    BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(0, 63),
                                        ],
                                    ),
                                    BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                        properties.Schema.STRING,
                                        _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            )
                        ),
                    }
                ),
                BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES: properties.Schema(
                    properties.Schema.LIST,
                    _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY: properties.Schema(
                                properties.Schema.STRING,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'inet', u'inet-labeled', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet-mvpn', u'inet6-vpn']),
                                ],
                            ),
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 16),
                                ],
                            ),
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT: properties.Schema(
                                properties.Schema.MAP,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(0, 86400),
                                        ],
                                    ),
                                }
                            ),
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP: properties.Schema(
                                properties.Schema.LIST,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'gre', u'mpls', u'udp', u'vxlan']),
                                ],
                            ),
                        }
                    )
                ),
                BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION: properties.Schema(
                    properties.Schema.STRING,
                    _('BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'remove', u'remove-all', u'replace-all']),
                    ],
                ),
                BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE: properties.Schema(
                    properties.Schema.MAP,
                    _('BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE: properties.Schema(
                            properties.Schema.BOOLEAN,
                            _('BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN: properties.Schema(
                            properties.Schema.STRING,
                            _('BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'IGP', u'EGP', u'INCOMPLETE']),
                            ],
                        ),
                    }
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP.'),
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
        BGPAAS_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('BGPAAS_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        AUTONOMOUS_SYSTEM: properties.Schema(
            properties.Schema.INTEGER,
            _('AUTONOMOUS_SYSTEM.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_HEALTH_CHECK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_HEALTH_CHECK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        CONTROL_NODE_ZONE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('CONTROL_NODE_ZONE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        CONTROL_NODE_ZONE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('CONTROL_NODE_ZONE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE.'),
                        update_allowed=True,
                        required=False,
                        constraints=[
                            constraints.AllowedValues([u'primary', u'secondary']),
                        ],
                    ),
                }
            )
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
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
        BGPAAS_SHARED: attributes.Schema(
            _('BGPAAS_SHARED.'),
        ),
        BGPAAS_SESSION_ATTRIBUTES: attributes.Schema(
            _('BGPAAS_SESSION_ATTRIBUTES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT: attributes.Schema(
            _('BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT.'),
        ),
        BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP: attributes.Schema(
            _('BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        BGPAAS_IP_ADDRESS: attributes.Schema(
            _('BGPAAS_IP_ADDRESS.'),
        ),
        AUTONOMOUS_SYSTEM: attributes.Schema(
            _('AUTONOMOUS_SYSTEM.'),
        ),
        SERVICE_HEALTH_CHECK_REFS: attributes.Schema(
            _('SERVICE_HEALTH_CHECK_REFS.'),
        ),
        CONTROL_NODE_ZONE_REFS: attributes.Schema(
            _('CONTROL_NODE_ZONE_REFS.'),
        ),
        CONTROL_NODE_ZONE_REFS_DATA: attributes.Schema(
            _('CONTROL_NODE_ZONE_REFS_DATA.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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

        obj_0 = vnc_api.BgpAsAService(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.BGPAAS_SHARED) is not None:
            obj_0.set_bgpaas_shared(self.properties.get(self.BGPAAS_SHARED))
        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES) is not None:
            obj_1 = vnc_api.BgpSessionAttributes()
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE) is not None:
                obj_1.set_passive(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                obj_1.set_as_override(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                obj_1.set_hold_time(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                obj_1.set_loop_count(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_local_autonomous_system(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                for index_1 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                    obj_2 = vnc_api.BgpFamilyAttributes()
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                        obj_2.set_address_family(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                        obj_2.set_loop_count(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                        obj_3 = vnc_api.BgpPrefixLimit()
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                            obj_3.set_maximum(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT) is not None:
                            obj_3.set_idle_timeout(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT))
                        obj_2.set_prefix_limit(obj_3)
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP) is not None:
                        for index_2 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP))):
                            obj_2.add_default_tunnel_encap(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP)[index_2])
                    obj_1.add_family_attributes(obj_2)
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION) is not None:
                obj_1.set_private_as_action(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE) is not None:
                obj_2 = vnc_api.RouteOriginOverride()
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE) is not None:
                    obj_2.set_origin_override(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE))
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN) is not None:
                    obj_2.set_origin(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN))
                obj_1.set_route_origin_override(obj_2)
            obj_0.set_bgpaas_session_attributes(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT) is not None:
            obj_0.set_bgpaas_suppress_route_advertisement(self.properties.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT))
        if self.properties.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP) is not None:
            obj_0.set_bgpaas_ipv4_mapped_ipv6_nexthop(self.properties.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP))
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
        if self.properties.get(self.BGPAAS_IP_ADDRESS) is not None:
            obj_0.set_bgpaas_ip_address(self.properties.get(self.BGPAAS_IP_ADDRESS))
        if self.properties.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(self.properties.get(self.AUTONOMOUS_SYSTEM))

        # reference to service_health_check_refs
        if self.properties.get(self.SERVICE_HEALTH_CHECK_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_HEALTH_CHECK_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        id=self.properties.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        fq_name_str=self.properties.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_service_health_check(ref_obj)

        # reference to control_node_zone_refs
        if len(self.properties.get(self.CONTROL_NODE_ZONE_REFS) or []) != len(self.properties.get(self.CONTROL_NODE_ZONE_REFS_DATA) or []):
            raise Exception(_('bgp-as-a-service: specify control_node_zone_refs for each control_node_zone_refs_data.'))
        obj_1 = None
        if self.properties.get(self.CONTROL_NODE_ZONE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.CONTROL_NODE_ZONE_REFS_DATA))):
                obj_1 = vnc_api.BGPaaSControlNodeZoneAttributes()
                if self.properties.get(self.CONTROL_NODE_ZONE_REFS_DATA, {})[index_0].get(self.CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE) is not None:
                    obj_1.set_bgpaas_control_node_zone_type(self.properties.get(self.CONTROL_NODE_ZONE_REFS_DATA, {})[index_0].get(self.CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE))

                if self.properties.get(self.CONTROL_NODE_ZONE_REFS):
                    try:
                        ref_obj = self.vnc_lib().control_node_zone_read(
                            id=self.properties.get(self.CONTROL_NODE_ZONE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().control_node_zone_read(
                            fq_name_str=self.properties.get(self.CONTROL_NODE_ZONE_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_control_node_zone(ref_obj, obj_1)

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

        # reference to virtual_machine_interface_refs
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_virtual_machine_interface(ref_obj)

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
            obj_uuid = super(ContrailBgpAsAService, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().bgp_as_a_service_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.BGPAAS_SHARED) is not None:
            obj_0.set_bgpaas_shared(prop_diff.get(self.BGPAAS_SHARED))
        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES) is not None:
            obj_1 = vnc_api.BgpSessionAttributes()
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE) is not None:
                obj_1.set_passive(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                obj_1.set_as_override(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                obj_1.set_hold_time(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                obj_1.set_loop_count(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_local_autonomous_system(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOCAL_AUTONOMOUS_SYSTEM))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                for index_1 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                    obj_2 = vnc_api.BgpFamilyAttributes()
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                        obj_2.set_address_family(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                        obj_2.set_loop_count(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                        obj_3 = vnc_api.BgpPrefixLimit()
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                            obj_3.set_maximum(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT) is not None:
                            obj_3.set_idle_timeout(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_IDLE_TIMEOUT))
                        obj_2.set_prefix_limit(obj_3)
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP) is not None:
                        for index_2 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP))):
                            obj_2.add_default_tunnel_encap(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_DEFAULT_TUNNEL_ENCAP)[index_2])
                    obj_1.add_family_attributes(obj_2)
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION) is not None:
                obj_1.set_private_as_action(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PRIVATE_AS_ACTION))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE) is not None:
                obj_2 = vnc_api.RouteOriginOverride()
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE) is not None:
                    obj_2.set_origin_override(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN_OVERRIDE))
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN) is not None:
                    obj_2.set_origin(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ROUTE_ORIGIN_OVERRIDE_ORIGIN))
                obj_1.set_route_origin_override(obj_2)
            obj_0.set_bgpaas_session_attributes(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT) is not None:
            obj_0.set_bgpaas_suppress_route_advertisement(prop_diff.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT))
        if prop_diff.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP) is not None:
            obj_0.set_bgpaas_ipv4_mapped_ipv6_nexthop(prop_diff.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP))
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
        if prop_diff.get(self.BGPAAS_IP_ADDRESS) is not None:
            obj_0.set_bgpaas_ip_address(prop_diff.get(self.BGPAAS_IP_ADDRESS))
        if prop_diff.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(prop_diff.get(self.AUTONOMOUS_SYSTEM))

        # reference to service_health_check_refs
        ref_obj_list = []
        if self.SERVICE_HEALTH_CHECK_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        id=prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        fq_name_str=prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_service_health_check_list(ref_obj_list)
            # End: reference to service_health_check_refs

        # reference to control_node_zone
        update = 0
        if not self.CONTROL_NODE_ZONE_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_control_node_zone_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.CONTROL_NODE_ZONE_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_control_node_zone_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.CONTROL_NODE_ZONE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.CONTROL_NODE_ZONE_REFS_DATA))):
                obj_1 = vnc_api.BGPaaSControlNodeZoneAttributes()
                if prop_diff.get(self.CONTROL_NODE_ZONE_REFS_DATA, {})[index_0].get(self.CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE) is not None:
                    obj_1.set_bgpaas_control_node_zone_type(prop_diff.get(self.CONTROL_NODE_ZONE_REFS_DATA, {})[index_0].get(self.CONTROL_NODE_ZONE_REFS_DATA_BGPAAS_CONTROL_NODE_ZONE_TYPE))
                ref_data_list.append(obj_1)
        if self.CONTROL_NODE_ZONE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.CONTROL_NODE_ZONE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().control_node_zone_read(
                        id=prop_diff.get(self.CONTROL_NODE_ZONE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().control_node_zone_read(
                        fq_name_str=prop_diff.get(self.CONTROL_NODE_ZONE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('bgp-as-a-service: specify control_node_zone_refs_data for each control_node_zone_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_control_node_zone_list(ref_obj_list, ref_data_list)
        # End: reference to control_node_zone_refs

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

        # reference to virtual_machine_interface_refs
        ref_obj_list = []
        if self.VIRTUAL_MACHINE_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_machine_interface_list(ref_obj_list)
            # End: reference to virtual_machine_interface_refs

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
            self.vnc_lib().bgp_as_a_service_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().bgp_as_a_service_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('bgp_as_a_service %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().bgp_as_a_service_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::BgpAsAService': ContrailBgpAsAService,
    }
