
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


class ContrailServiceInstance(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, SERVICE_INSTANCE_BGP_ENABLED, SERVICE_INSTANCE_BINDINGS, SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY, SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE, SERVICE_INSTANCE_PROPERTIES, SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY, SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE, SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK, SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK, SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS, SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK, SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC, SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE, SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES, SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE, SERVICE_INSTANCE_PROPERTIES_HA_MODE, SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID, SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, SERVICE_TEMPLATE_REFS, INSTANCE_IP_REFS, INSTANCE_IP_REFS_DATA, INSTANCE_IP_REFS_DATA_INTERFACE_TYPE, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'service_instance_bgp_enabled', 'service_instance_bindings', 'service_instance_bindings_key_value_pair', 'service_instance_bindings_key_value_pair_key', 'service_instance_bindings_key_value_pair_value', 'service_instance_properties', 'service_instance_properties_auto_policy', 'service_instance_properties_availability_zone', 'service_instance_properties_management_virtual_network', 'service_instance_properties_left_virtual_network', 'service_instance_properties_left_ip_address', 'service_instance_properties_right_virtual_network', 'service_instance_properties_right_ip_address', 'service_instance_properties_interface_list', 'service_instance_properties_interface_list_virtual_network', 'service_instance_properties_interface_list_ip_address', 'service_instance_properties_interface_list_static_routes', 'service_instance_properties_interface_list_static_routes_route', 'service_instance_properties_interface_list_static_routes_route_prefix', 'service_instance_properties_interface_list_static_routes_route_next_hop', 'service_instance_properties_interface_list_static_routes_route_next_hop_type', 'service_instance_properties_interface_list_static_routes_route_community_attributes', 'service_instance_properties_interface_list_static_routes_route_community_attributes_community_attribute', 'service_instance_properties_interface_list_allowed_address_pairs', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair_ip', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair_ip_ip_prefix', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair_mac', 'service_instance_properties_interface_list_allowed_address_pairs_allowed_address_pair_address_mode', 'service_instance_properties_scale_out', 'service_instance_properties_scale_out_max_instances', 'service_instance_properties_scale_out_auto_scale', 'service_instance_properties_ha_mode', 'service_instance_properties_virtual_router_id', 'service_instance_properties_service_virtualization_type', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'service_template_refs', 'instance_ip_refs', 'instance_ip_refs_data', 'instance_ip_refs_data_interface_type', 'project'
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
        SERVICE_INSTANCE_BGP_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('SERVICE_INSTANCE_BGP_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_BINDINGS: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_INSTANCE_BINDINGS.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        SERVICE_INSTANCE_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_INSTANCE_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES: properties.Schema(
                                properties.Schema.MAP,
                                _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    constraints=[
                                                        constraints.AllowedValues([u'service-instance', u'ip-address']),
                                                    ],
                                                ),
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                                    properties.Schema.MAP,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    schema={
                                                        SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                            properties.Schema.LIST,
                                                            _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
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
                            SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS: properties.Schema(
                                properties.Schema.MAP,
                                _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR: properties.Schema(
                                        properties.Schema.LIST,
                                        _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP: properties.Schema(
                                                    properties.Schema.MAP,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    schema={
                                                        SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                ),
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    constraints=[
                                                        constraints.AllowedValues([u'active-active', u'active-standby']),
                                                    ],
                                                ),
                                            }
                                        )
                                    ),
                                }
                            ),
                        }
                    )
                ),
                SERVICE_INSTANCE_PROPERTIES_SCALE_OUT: properties.Schema(
                    properties.Schema.MAP,
                    _('SERVICE_INSTANCE_PROPERTIES_SCALE_OUT.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES: properties.Schema(
                            properties.Schema.INTEGER,
                            _('SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES.'),
                            update_allowed=True,
                            required=False,
                        ),
                        SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE: properties.Schema(
                            properties.Schema.BOOLEAN,
                            _('SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                SERVICE_INSTANCE_PROPERTIES_HA_MODE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_HA_MODE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'active-active', u'active-standby']),
                    ],
                ),
                SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'virtual-machine', u'network-namespace', u'vrouter-instance', u'physical-device']),
                    ],
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
        SERVICE_TEMPLATE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_TEMPLATE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        INSTANCE_IP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('INSTANCE_IP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        INSTANCE_IP_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('INSTANCE_IP_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    INSTANCE_IP_REFS_DATA_INTERFACE_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('INSTANCE_IP_REFS_DATA_INTERFACE_TYPE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
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
        SERVICE_INSTANCE_BGP_ENABLED: attributes.Schema(
            _('SERVICE_INSTANCE_BGP_ENABLED.'),
        ),
        SERVICE_INSTANCE_BINDINGS: attributes.Schema(
            _('SERVICE_INSTANCE_BINDINGS.'),
        ),
        SERVICE_INSTANCE_PROPERTIES: attributes.Schema(
            _('SERVICE_INSTANCE_PROPERTIES.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        SERVICE_TEMPLATE_REFS: attributes.Schema(
            _('SERVICE_TEMPLATE_REFS.'),
        ),
        INSTANCE_IP_REFS: attributes.Schema(
            _('INSTANCE_IP_REFS.'),
        ),
        INSTANCE_IP_REFS_DATA: attributes.Schema(
            _('INSTANCE_IP_REFS_DATA.'),
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

        obj_0 = vnc_api.ServiceInstance(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.SERVICE_INSTANCE_BGP_ENABLED) is not None:
            obj_0.set_service_instance_bgp_enabled(self.properties.get(self.SERVICE_INSTANCE_BGP_ENABLED))
        if self.properties.get(self.SERVICE_INSTANCE_BINDINGS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_instance_bindings(obj_1)
        if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceInstanceType()
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY) is not None:
                obj_1.set_auto_policy(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE) is not None:
                obj_1.set_availability_zone(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK) is not None:
                obj_1.set_management_virtual_network(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK) is not None:
                obj_1.set_left_virtual_network(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS) is not None:
                obj_1.set_left_ip_address(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK) is not None:
                obj_1.set_right_virtual_network(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS) is not None:
                obj_1.set_right_ip_address(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST))):
                    obj_2 = vnc_api.ServiceInstanceInterfaceType()
                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK) is not None:
                        obj_2.set_virtual_network(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK))
                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS) is not None:
                        obj_2.set_ip_address(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS))
                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES) is not None:
                        obj_3 = vnc_api.RouteTableType()
                        if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE) is not None:
                            for index_3 in range(len(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE))):
                                obj_4 = vnc_api.RouteType()
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX) is not None:
                                    obj_4.set_prefix(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX))
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP) is not None:
                                    obj_4.set_next_hop(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP))
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                    obj_4.set_next_hop_type(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                    obj_5 = vnc_api.CommunityAttributes()
                                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                        for index_5 in range(len(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                            obj_5.add_community_attribute(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                    obj_4.set_community_attributes(obj_5)
                                obj_3.add_route(obj_4)
                        obj_2.set_static_routes(obj_3)
                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS) is not None:
                        obj_3 = vnc_api.AllowedAddressPairs()
                        if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR) is not None:
                            for index_3 in range(len(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR))):
                                obj_4 = vnc_api.AllowedAddressPair()
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP) is not None:
                                    obj_5 = vnc_api.SubnetType()
                                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX))
                                    if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN))
                                    obj_4.set_ip(obj_5)
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC) is not None:
                                    obj_4.set_mac(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC))
                                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE) is not None:
                                    obj_4.set_address_mode(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE))
                                obj_3.add_allowed_address_pair(obj_4)
                        obj_2.set_allowed_address_pairs(obj_3)
                    obj_1.add_interface_list(obj_2)
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT) is not None:
                obj_2 = vnc_api.ServiceScaleOutType()
                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES) is not None:
                    obj_2.set_max_instances(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES))
                if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE) is not None:
                    obj_2.set_auto_scale(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE))
                obj_1.set_scale_out(obj_2)
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_HA_MODE) is not None:
                obj_1.set_ha_mode(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_HA_MODE))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID) is not None:
                obj_1.set_virtual_router_id(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID))
            if self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE) is not None:
                obj_1.set_service_virtualization_type(self.properties.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE))
            obj_0.set_service_instance_properties(obj_1)
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

        # reference to service_template_refs
        if self.properties.get(self.SERVICE_TEMPLATE_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_TEMPLATE_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_template_read(
                        id=self.properties.get(self.SERVICE_TEMPLATE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_template_read(
                        fq_name_str=self.properties.get(self.SERVICE_TEMPLATE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_service_template(ref_obj)

        # reference to instance_ip_refs
        if len(self.properties.get(self.INSTANCE_IP_REFS) or []) != len(self.properties.get(self.INSTANCE_IP_REFS_DATA) or []):
            raise Exception(_('service-instance: specify instance_ip_refs for each instance_ip_refs_data.'))
        obj_1 = None
        if self.properties.get(self.INSTANCE_IP_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.INSTANCE_IP_REFS_DATA))):
                obj_1 = vnc_api.ServiceInterfaceTag()
                if self.properties.get(self.INSTANCE_IP_REFS_DATA, {})[index_0].get(self.INSTANCE_IP_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(self.properties.get(self.INSTANCE_IP_REFS_DATA, {})[index_0].get(self.INSTANCE_IP_REFS_DATA_INTERFACE_TYPE))

                if self.properties.get(self.INSTANCE_IP_REFS):
                    try:
                        ref_obj = self.vnc_lib().instance_ip_read(
                            id=self.properties.get(self.INSTANCE_IP_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().instance_ip_read(
                            fq_name_str=self.properties.get(self.INSTANCE_IP_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_instance_ip(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailServiceInstance, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().service_instance_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SERVICE_INSTANCE_BGP_ENABLED) is not None:
            obj_0.set_service_instance_bgp_enabled(prop_diff.get(self.SERVICE_INSTANCE_BGP_ENABLED))
        if prop_diff.get(self.SERVICE_INSTANCE_BINDINGS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.SERVICE_INSTANCE_BINDINGS, {}).get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_INSTANCE_BINDINGS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_instance_bindings(obj_1)
        if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceInstanceType()
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY) is not None:
                obj_1.set_auto_policy(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AUTO_POLICY))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE) is not None:
                obj_1.set_availability_zone(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_AVAILABILITY_ZONE))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK) is not None:
                obj_1.set_management_virtual_network(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_MANAGEMENT_VIRTUAL_NETWORK))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK) is not None:
                obj_1.set_left_virtual_network(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_VIRTUAL_NETWORK))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS) is not None:
                obj_1.set_left_ip_address(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_LEFT_IP_ADDRESS))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK) is not None:
                obj_1.set_right_virtual_network(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_VIRTUAL_NETWORK))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS) is not None:
                obj_1.set_right_ip_address(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_RIGHT_IP_ADDRESS))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST))):
                    obj_2 = vnc_api.ServiceInstanceInterfaceType()
                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK) is not None:
                        obj_2.set_virtual_network(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_VIRTUAL_NETWORK))
                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS) is not None:
                        obj_2.set_ip_address(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_IP_ADDRESS))
                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES) is not None:
                        obj_3 = vnc_api.RouteTableType()
                        if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE) is not None:
                            for index_3 in range(len(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE))):
                                obj_4 = vnc_api.RouteType()
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX) is not None:
                                    obj_4.set_prefix(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_PREFIX))
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP) is not None:
                                    obj_4.set_next_hop(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP))
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                    obj_4.set_next_hop_type(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                    obj_5 = vnc_api.CommunityAttributes()
                                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                        for index_5 in range(len(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                            obj_5.add_community_attribute(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_STATIC_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                    obj_4.set_community_attributes(obj_5)
                                obj_3.add_route(obj_4)
                        obj_2.set_static_routes(obj_3)
                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS) is not None:
                        obj_3 = vnc_api.AllowedAddressPairs()
                        if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR) is not None:
                            for index_3 in range(len(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR))):
                                obj_4 = vnc_api.AllowedAddressPair()
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP) is not None:
                                    obj_5 = vnc_api.SubnetType()
                                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX))
                                    if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN))
                                    obj_4.set_ip(obj_5)
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC) is not None:
                                    obj_4.set_mac(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC))
                                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE) is not None:
                                    obj_4.set_address_mode(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST, {})[index_1].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS, {}).get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_3].get(self.SERVICE_INSTANCE_PROPERTIES_INTERFACE_LIST_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE))
                                obj_3.add_allowed_address_pair(obj_4)
                        obj_2.set_allowed_address_pairs(obj_3)
                    obj_1.add_interface_list(obj_2)
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT) is not None:
                obj_2 = vnc_api.ServiceScaleOutType()
                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES) is not None:
                    obj_2.set_max_instances(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_MAX_INSTANCES))
                if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE) is not None:
                    obj_2.set_auto_scale(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SCALE_OUT_AUTO_SCALE))
                obj_1.set_scale_out(obj_2)
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_HA_MODE) is not None:
                obj_1.set_ha_mode(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_HA_MODE))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID) is not None:
                obj_1.set_virtual_router_id(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_VIRTUAL_ROUTER_ID))
            if prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE) is not None:
                obj_1.set_service_virtualization_type(prop_diff.get(self.SERVICE_INSTANCE_PROPERTIES, {}).get(self.SERVICE_INSTANCE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE))
            obj_0.set_service_instance_properties(obj_1)
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

        # reference to service_template_refs
        ref_obj_list = []
        if self.SERVICE_TEMPLATE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_TEMPLATE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_template_read(
                        id=prop_diff.get(self.SERVICE_TEMPLATE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_template_read(
                        fq_name_str=prop_diff.get(self.SERVICE_TEMPLATE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_service_template_list(ref_obj_list)
            # End: reference to service_template_refs

        # reference to instance_ip
        update = 0
        if not self.INSTANCE_IP_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_instance_ip_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.INSTANCE_IP_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_instance_ip_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.INSTANCE_IP_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.INSTANCE_IP_REFS_DATA))):
                obj_1 = vnc_api.ServiceInterfaceTag()
                if prop_diff.get(self.INSTANCE_IP_REFS_DATA, {})[index_0].get(self.INSTANCE_IP_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(prop_diff.get(self.INSTANCE_IP_REFS_DATA, {})[index_0].get(self.INSTANCE_IP_REFS_DATA_INTERFACE_TYPE))
                ref_data_list.append(obj_1)
        if self.INSTANCE_IP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.INSTANCE_IP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().instance_ip_read(
                        id=prop_diff.get(self.INSTANCE_IP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().instance_ip_read(
                        fq_name_str=prop_diff.get(self.INSTANCE_IP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('service-instance: specify instance_ip_refs_data for each instance_ip_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_instance_ip_list(ref_obj_list, ref_data_list)
        # End: reference to instance_ip_refs

        try:
            self.vnc_lib().service_instance_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().service_instance_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('service_instance %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().service_instance_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ServiceInstance': ContrailServiceInstance,
    }
