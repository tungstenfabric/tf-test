
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


class ContrailRoutingInstance(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ROUTING_INSTANCE_HAS_PNF, ROUTING_INSTANCE_IS_DEFAULT, EVPN_IPV6_SERVICE_CHAIN_INFORMATION, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID, EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, SERVICE_CHAIN_INFORMATION, SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, SERVICE_CHAIN_INFORMATION_PREFIX, SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID, SERVICE_CHAIN_INFORMATION_SC_HEAD, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, IPV6_SERVICE_CHAIN_INFORMATION, IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION_PREFIX, IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID, IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD, STATIC_ROUTE_ENTRIES, STATIC_ROUTE_ENTRIES_ROUTE, STATIC_ROUTE_ENTRIES_ROUTE_PREFIX, STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP, STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET, STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY, EVPN_SERVICE_CHAIN_INFORMATION, EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, EVPN_SERVICE_CHAIN_INFORMATION_PREFIX, EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID, EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD, ROUTING_INSTANCE_FABRIC_SNAT, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, DEFAULT_CE_PROTOCOL, DEFAULT_CE_PROTOCOL_BGP, DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM, DEFAULT_CE_PROTOCOL_OSPF, DEFAULT_CE_PROTOCOL_OSPF_AREA, TAG_REFS, ROUTING_INSTANCE_REFS, ROUTING_INSTANCE_REFS_DATA, ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE, ROUTE_TARGET_REFS, ROUTE_TARGET_REFS_DATA, ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT, VIRTUAL_NETWORK
    ) = (
        'name', 'fq_name', 'display_name', 'routing_instance_has_pnf', 'routing_instance_is_default', 'evpn_ipv6_service_chain_information', 'evpn_ipv6_service_chain_information_routing_instance', 'evpn_ipv6_service_chain_information_prefix', 'evpn_ipv6_service_chain_information_service_chain_address', 'evpn_ipv6_service_chain_information_service_instance', 'evpn_ipv6_service_chain_information_source_routing_instance', 'evpn_ipv6_service_chain_information_service_chain_id', 'evpn_ipv6_service_chain_information_sc_head', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'service_chain_information', 'service_chain_information_routing_instance', 'service_chain_information_prefix', 'service_chain_information_service_chain_address', 'service_chain_information_service_instance', 'service_chain_information_source_routing_instance', 'service_chain_information_service_chain_id', 'service_chain_information_sc_head', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'ipv6_service_chain_information', 'ipv6_service_chain_information_routing_instance', 'ipv6_service_chain_information_prefix', 'ipv6_service_chain_information_service_chain_address', 'ipv6_service_chain_information_service_instance', 'ipv6_service_chain_information_source_routing_instance', 'ipv6_service_chain_information_service_chain_id', 'ipv6_service_chain_information_sc_head', 'static_route_entries', 'static_route_entries_route', 'static_route_entries_route_prefix', 'static_route_entries_route_next_hop', 'static_route_entries_route_route_target', 'static_route_entries_route_community', 'evpn_service_chain_information', 'evpn_service_chain_information_routing_instance', 'evpn_service_chain_information_prefix', 'evpn_service_chain_information_service_chain_address', 'evpn_service_chain_information_service_instance', 'evpn_service_chain_information_source_routing_instance', 'evpn_service_chain_information_service_chain_id', 'evpn_service_chain_information_sc_head', 'routing_instance_fabric_snat', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'default_ce_protocol', 'default_ce_protocol_bgp', 'default_ce_protocol_bgp_autonomous_system', 'default_ce_protocol_ospf', 'default_ce_protocol_ospf_area', 'tag_refs', 'routing_instance_refs', 'routing_instance_refs_data', 'routing_instance_refs_data_destination_instance', 'route_target_refs', 'route_target_refs_data', 'route_target_refs_data_import_export', 'virtual_network'
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
        ROUTING_INSTANCE_HAS_PNF: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTING_INSTANCE_HAS_PNF.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_IS_DEFAULT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTING_INSTANCE_IS_DEFAULT.'),
            update_allowed=True,
            required=False,
        ),
        EVPN_IPV6_SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD.'),
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
        SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SC_HEAD: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_CHAIN_INFORMATION_SC_HEAD.'),
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
        IPV6_SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('IPV6_SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        STATIC_ROUTE_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('STATIC_ROUTE_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                STATIC_ROUTE_ENTRIES_ROUTE: properties.Schema(
                    properties.Schema.LIST,
                    _('STATIC_ROUTE_ENTRIES_ROUTE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            STATIC_ROUTE_ENTRIES_ROUTE_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP: properties.Schema(
                                properties.Schema.STRING,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET: properties.Schema(
                                properties.Schema.LIST,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY: properties.Schema(
                                properties.Schema.LIST,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        EVPN_SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('EVPN_SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        ROUTING_INSTANCE_FABRIC_SNAT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTING_INSTANCE_FABRIC_SNAT.'),
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
        DEFAULT_CE_PROTOCOL: properties.Schema(
            properties.Schema.MAP,
            _('DEFAULT_CE_PROTOCOL.'),
            update_allowed=True,
            required=False,
            schema={
                DEFAULT_CE_PROTOCOL_BGP: properties.Schema(
                    properties.Schema.MAP,
                    _('DEFAULT_CE_PROTOCOL_BGP.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM: properties.Schema(
                            properties.Schema.INTEGER,
                            _('DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                DEFAULT_CE_PROTOCOL_OSPF: properties.Schema(
                    properties.Schema.MAP,
                    _('DEFAULT_CE_PROTOCOL_OSPF.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        DEFAULT_CE_PROTOCOL_OSPF_AREA: properties.Schema(
                            properties.Schema.INTEGER,
                            _('DEFAULT_CE_PROTOCOL_OSPF_AREA.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
            }
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_INSTANCE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        ROUTE_TARGET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TARGET_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TARGET_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TARGET_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT.'),
                        update_allowed=True,
                        required=False,
                        constraints=[
                            constraints.AllowedValues([u'import', u'export']),
                        ],
                    ),
                }
            )
        ),
        VIRTUAL_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK.'),
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
        ROUTING_INSTANCE_HAS_PNF: attributes.Schema(
            _('ROUTING_INSTANCE_HAS_PNF.'),
        ),
        ROUTING_INSTANCE_IS_DEFAULT: attributes.Schema(
            _('ROUTING_INSTANCE_IS_DEFAULT.'),
        ),
        EVPN_IPV6_SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('EVPN_IPV6_SERVICE_CHAIN_INFORMATION.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('SERVICE_CHAIN_INFORMATION.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        IPV6_SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('IPV6_SERVICE_CHAIN_INFORMATION.'),
        ),
        STATIC_ROUTE_ENTRIES: attributes.Schema(
            _('STATIC_ROUTE_ENTRIES.'),
        ),
        EVPN_SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('EVPN_SERVICE_CHAIN_INFORMATION.'),
        ),
        ROUTING_INSTANCE_FABRIC_SNAT: attributes.Schema(
            _('ROUTING_INSTANCE_FABRIC_SNAT.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        DEFAULT_CE_PROTOCOL: attributes.Schema(
            _('DEFAULT_CE_PROTOCOL.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        ROUTING_INSTANCE_REFS: attributes.Schema(
            _('ROUTING_INSTANCE_REFS.'),
        ),
        ROUTING_INSTANCE_REFS_DATA: attributes.Schema(
            _('ROUTING_INSTANCE_REFS_DATA.'),
        ),
        ROUTE_TARGET_REFS: attributes.Schema(
            _('ROUTE_TARGET_REFS.'),
        ),
        ROUTE_TARGET_REFS_DATA: attributes.Schema(
            _('ROUTE_TARGET_REFS_DATA.'),
        ),
        VIRTUAL_NETWORK: attributes.Schema(
            _('VIRTUAL_NETWORK.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK) and self.properties.get(self.VIRTUAL_NETWORK) != 'config-root':
            try:
                parent_obj = self.vnc_lib().virtual_network_read(fq_name_str=self.properties.get(self.VIRTUAL_NETWORK))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_network_read(id=str(uuid.UUID(self.properties.get(self.VIRTUAL_NETWORK))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.RoutingInstance(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ROUTING_INSTANCE_HAS_PNF) is not None:
            obj_0.set_routing_instance_has_pnf(self.properties.get(self.ROUTING_INSTANCE_HAS_PNF))
        if self.properties.get(self.ROUTING_INSTANCE_IS_DEFAULT) is not None:
            obj_0.set_routing_instance_is_default(self.properties.get(self.ROUTING_INSTANCE_IS_DEFAULT))
        if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(self.properties.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_evpn_ipv6_service_chain_information(obj_1)
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
        if self.properties.get(self.SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_service_chain_information(obj_1)
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
        if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_ipv6_service_chain_information(obj_1)
        if self.properties.get(self.STATIC_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.StaticRouteEntriesType()
            if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE))):
                    obj_2 = vnc_api.StaticRouteType()
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX))
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP))
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET) is not None:
                        for index_2 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET))):
                            obj_2.add_route_target(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET)[index_2])
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY) is not None:
                        for index_2 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY))):
                            obj_2.add_community(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY)[index_2])
                    obj_1.add_route(obj_2)
            obj_0.set_static_route_entries(obj_1)
        if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(self.properties.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_evpn_service_chain_information(obj_1)
        if self.properties.get(self.ROUTING_INSTANCE_FABRIC_SNAT) is not None:
            obj_0.set_routing_instance_fabric_snat(self.properties.get(self.ROUTING_INSTANCE_FABRIC_SNAT))
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
        if self.properties.get(self.DEFAULT_CE_PROTOCOL) is not None:
            obj_1 = vnc_api.DefaultProtocolType()
            if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP) is not None:
                obj_2 = vnc_api.ProtocolBgpType()
                if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP, {}).get(self.DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM) is not None:
                    obj_2.set_autonomous_system(self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP, {}).get(self.DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM))
                obj_1.set_bgp(obj_2)
            if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF) is not None:
                obj_2 = vnc_api.ProtocolOspfType()
                if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA) is not None:
                    obj_2.set_area(self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA))
                obj_1.set_ospf(obj_2)
            obj_0.set_default_ce_protocol(obj_1)

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

        # reference to routing_instance_refs
        if len(self.properties.get(self.ROUTING_INSTANCE_REFS) or []) != len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) or []):
            raise Exception(_('routing-instance: specify routing_instance_refs for each routing_instance_refs_data.'))
        obj_1 = None
        if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ConnectionType()
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE) is not None:
                    obj_1.set_destination_instance(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE))

                if self.properties.get(self.ROUTING_INSTANCE_REFS):
                    try:
                        ref_obj = self.vnc_lib().routing_instance_read(
                            id=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().routing_instance_read(
                            fq_name_str=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_routing_instance(ref_obj, obj_1)

        # reference to route_target_refs
        if len(self.properties.get(self.ROUTE_TARGET_REFS) or []) != len(self.properties.get(self.ROUTE_TARGET_REFS_DATA) or []):
            raise Exception(_('routing-instance: specify route_target_refs for each route_target_refs_data.'))
        obj_1 = None
        if self.properties.get(self.ROUTE_TARGET_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTE_TARGET_REFS_DATA))):
                obj_1 = vnc_api.InstanceTargetType()
                if self.properties.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT) is not None:
                    obj_1.set_import_export(self.properties.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT))

                if self.properties.get(self.ROUTE_TARGET_REFS):
                    try:
                        ref_obj = self.vnc_lib().route_target_read(
                            id=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().route_target_read(
                            fq_name_str=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_route_target(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailRoutingInstance, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().routing_instance_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ROUTING_INSTANCE_HAS_PNF) is not None:
            obj_0.set_routing_instance_has_pnf(prop_diff.get(self.ROUTING_INSTANCE_HAS_PNF))
        if prop_diff.get(self.ROUTING_INSTANCE_IS_DEFAULT) is not None:
            obj_0.set_routing_instance_is_default(prop_diff.get(self.ROUTING_INSTANCE_IS_DEFAULT))
        if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(prop_diff.get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_evpn_ipv6_service_chain_information(obj_1)
        if prop_diff.get(self.SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_service_chain_information(obj_1)
        if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_ipv6_service_chain_information(obj_1)
        if prop_diff.get(self.STATIC_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.StaticRouteEntriesType()
            if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE))):
                    obj_2 = vnc_api.StaticRouteType()
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX))
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP))
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET) is not None:
                        for index_2 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET))):
                            obj_2.add_route_target(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET)[index_2])
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY) is not None:
                        for index_2 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY))):
                            obj_2.add_community(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY)[index_2])
                    obj_1.add_route(obj_2)
            obj_0.set_static_route_entries(obj_1)
        if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID) is not None:
                obj_1.set_service_chain_id(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ID))
            if prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD) is not None:
                obj_1.set_sc_head(prop_diff.get(self.EVPN_SERVICE_CHAIN_INFORMATION, {}).get(self.EVPN_SERVICE_CHAIN_INFORMATION_SC_HEAD))
            obj_0.set_evpn_service_chain_information(obj_1)
        if prop_diff.get(self.ROUTING_INSTANCE_FABRIC_SNAT) is not None:
            obj_0.set_routing_instance_fabric_snat(prop_diff.get(self.ROUTING_INSTANCE_FABRIC_SNAT))
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
        if prop_diff.get(self.DEFAULT_CE_PROTOCOL) is not None:
            obj_1 = vnc_api.DefaultProtocolType()
            if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP) is not None:
                obj_2 = vnc_api.ProtocolBgpType()
                if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP, {}).get(self.DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM) is not None:
                    obj_2.set_autonomous_system(prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP, {}).get(self.DEFAULT_CE_PROTOCOL_BGP_AUTONOMOUS_SYSTEM))
                obj_1.set_bgp(obj_2)
            if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF) is not None:
                obj_2 = vnc_api.ProtocolOspfType()
                if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA) is not None:
                    obj_2.set_area(prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA))
                obj_1.set_ospf(obj_2)
            obj_0.set_default_ce_protocol(obj_1)

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

        # reference to routing_instance
        update = 0
        if not self.ROUTING_INSTANCE_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_routing_instance_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.ROUTING_INSTANCE_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_routing_instance_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ConnectionType()
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE) is not None:
                    obj_1.set_destination_instance(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE))
                ref_data_list.append(obj_1)
        if self.ROUTING_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        id=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        fq_name_str=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('routing-instance: specify routing_instance_refs_data for each routing_instance_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_routing_instance_list(ref_obj_list, ref_data_list)
        # End: reference to routing_instance_refs

        # reference to route_target
        update = 0
        if not self.ROUTE_TARGET_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_route_target_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.ROUTE_TARGET_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_route_target_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.ROUTE_TARGET_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TARGET_REFS_DATA))):
                obj_1 = vnc_api.InstanceTargetType()
                if prop_diff.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT) is not None:
                    obj_1.set_import_export(prop_diff.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT))
                ref_data_list.append(obj_1)
        if self.ROUTE_TARGET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TARGET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().route_target_read(
                        id=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_target_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('routing-instance: specify route_target_refs_data for each route_target_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_route_target_list(ref_obj_list, ref_data_list)
        # End: reference to route_target_refs

        try:
            self.vnc_lib().routing_instance_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().routing_instance_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('routing_instance %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().routing_instance_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::RoutingInstance': ContrailRoutingInstance,
    }
