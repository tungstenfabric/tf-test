
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


class ContrailRoutingPolicy(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, ROUTING_POLICY_ENTRIES, ROUTING_POLICY_ENTRIES_TERM, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE, ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND, ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND, TERM_TYPE, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, SERVICE_INSTANCE_REFS, SERVICE_INSTANCE_REFS_DATA, SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE, SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE, ROUTING_INSTANCE_REFS, ROUTING_INSTANCE_REFS_DATA, ROUTING_INSTANCE_REFS_DATA_SEQUENCE, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'routing_policy_entries', 'routing_policy_entries_term', 'routing_policy_entries_term_term_match_condition', 'routing_policy_entries_term_term_match_condition_protocol', 'routing_policy_entries_term_term_match_condition_prefix', 'routing_policy_entries_term_term_match_condition_prefix_prefix', 'routing_policy_entries_term_term_match_condition_prefix_prefix_type', 'routing_policy_entries_term_term_match_condition_community', 'routing_policy_entries_term_term_match_condition_community_list', 'routing_policy_entries_term_term_match_condition_community_match_all', 'routing_policy_entries_term_term_match_condition_extcommunity_list', 'routing_policy_entries_term_term_match_condition_extcommunity_match_all', 'routing_policy_entries_term_term_match_condition_family', 'routing_policy_entries_term_term_match_condition_as_path', 'routing_policy_entries_term_term_match_condition_external', 'routing_policy_entries_term_term_match_condition_local_pref', 'routing_policy_entries_term_term_match_condition_nlri_route_type', 'routing_policy_entries_term_term_match_condition_prefix_list', 'routing_policy_entries_term_term_match_condition_prefix_list_interface_route_table_uuid', 'routing_policy_entries_term_term_match_condition_prefix_list_prefix_type', 'routing_policy_entries_term_term_match_condition_route_filter', 'routing_policy_entries_term_term_match_condition_route_filter_route_filter_properties', 'routing_policy_entries_term_term_match_condition_route_filter_route_filter_properties_route', 'routing_policy_entries_term_term_match_condition_route_filter_route_filter_properties_route_type', 'routing_policy_entries_term_term_match_condition_route_filter_route_filter_properties_route_type_value', 'routing_policy_entries_term_term_action_list', 'routing_policy_entries_term_term_action_list_update', 'routing_policy_entries_term_term_action_list_update_as_path', 'routing_policy_entries_term_term_action_list_update_as_path_expand', 'routing_policy_entries_term_term_action_list_update_as_path_expand_asn_list', 'routing_policy_entries_term_term_action_list_update_community', 'routing_policy_entries_term_term_action_list_update_community_add', 'routing_policy_entries_term_term_action_list_update_community_add_community', 'routing_policy_entries_term_term_action_list_update_community_remove', 'routing_policy_entries_term_term_action_list_update_community_remove_community', 'routing_policy_entries_term_term_action_list_update_community_set', 'routing_policy_entries_term_term_action_list_update_community_set_community', 'routing_policy_entries_term_term_action_list_update_extcommunity', 'routing_policy_entries_term_term_action_list_update_extcommunity_add', 'routing_policy_entries_term_term_action_list_update_extcommunity_add_community', 'routing_policy_entries_term_term_action_list_update_extcommunity_remove', 'routing_policy_entries_term_term_action_list_update_extcommunity_remove_community', 'routing_policy_entries_term_term_action_list_update_extcommunity_set', 'routing_policy_entries_term_term_action_list_update_extcommunity_set_community', 'routing_policy_entries_term_term_action_list_update_local_pref', 'routing_policy_entries_term_term_action_list_update_med', 'routing_policy_entries_term_term_action_list_action', 'routing_policy_entries_term_term_action_list_external', 'routing_policy_entries_term_term_action_list_as_path_expand', 'routing_policy_entries_term_term_action_list_as_path_prepend', 'term_type', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'service_instance_refs', 'service_instance_refs_data', 'service_instance_refs_data_left_sequence', 'service_instance_refs_data_right_sequence', 'routing_instance_refs', 'routing_instance_refs_data', 'routing_instance_refs_data_sequence', 'project'
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
        ROUTING_POLICY_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('ROUTING_POLICY_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                ROUTING_POLICY_ENTRIES_TERM: properties.Schema(
                    properties.Schema.LIST,
                    _('ROUTING_POLICY_ENTRIES_TERM.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION: properties.Schema(
                                properties.Schema.MAP,
                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'xmpp', u'service-chain', u'interface', u'interface-static', u'service-interface', u'bgpaas', u'bgp', u'static', u'aggregate', u'direct', u'pim', u'evpn', u'ospf', u'ospf3']),
                                        ],
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    constraints=[
                                                        constraints.AllowedValues([u'exact', u'longer', u'orlonger']),
                                                    ],
                                                ),
                                            }
                                        )
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'inet', u'inet-vpn', u'evpn']),
                                        ],
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'ospf-type-1', u'ospf-type-2']),
                                        ],
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID: properties.Schema(
                                                    properties.Schema.LIST,
                                                    _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    constraints=[
                                                        constraints.AllowedValues([u'exact', u'longer', u'orlonger']),
                                                    ],
                                                ),
                                            }
                                        )
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES: properties.Schema(
                                                properties.Schema.LIST,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            constraints=[
                                                                constraints.AllowedValues([u'exact', u'longer', u'orlonger', u'prefix-length-range', u'through', u'upto']),
                                                            ],
                                                        ),
                                                        ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                }
                            ),
                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST: properties.Schema(
                                properties.Schema.MAP,
                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH: properties.Schema(
                                                properties.Schema.MAP,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                }
                                            ),
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY: properties.Schema(
                                                properties.Schema.MAP,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                }
                                            ),
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY: properties.Schema(
                                                properties.Schema.MAP,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY.'),
                                                                update_allowed=True,
                                                                required=False,
                                                            ),
                                                        }
                                                    ),
                                                }
                                            ),
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                        }
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'reject', u'accept', u'next']),
                                        ],
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'ospf-type-1', u'ospf-type-2']),
                                        ],
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND.'),
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
        TERM_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('TERM_TYPE.'),
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
        SERVICE_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE: properties.Schema(
                        properties.Schema.STRING,
                        _('SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE.'),
                        update_allowed=True,
                        required=False,
                    ),
                    SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE: properties.Schema(
                        properties.Schema.STRING,
                        _('SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
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
                    ROUTING_INSTANCE_REFS_DATA_SEQUENCE: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_SEQUENCE.'),
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
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        ROUTING_POLICY_ENTRIES: attributes.Schema(
            _('ROUTING_POLICY_ENTRIES.'),
        ),
        TERM_TYPE: attributes.Schema(
            _('TERM_TYPE.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        SERVICE_INSTANCE_REFS_DATA: attributes.Schema(
            _('SERVICE_INSTANCE_REFS_DATA.'),
        ),
        ROUTING_INSTANCE_REFS: attributes.Schema(
            _('ROUTING_INSTANCE_REFS.'),
        ),
        ROUTING_INSTANCE_REFS_DATA: attributes.Schema(
            _('ROUTING_INSTANCE_REFS_DATA.'),
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

        obj_0 = vnc_api.RoutingPolicy(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
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
        if self.properties.get(self.ROUTING_POLICY_ENTRIES) is not None:
            obj_1 = vnc_api.PolicyStatementType()
            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM) is not None:
                for index_1 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM))):
                    obj_2 = vnc_api.PolicyTermType()
                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.TermMatchConditionType()
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL))):
                                obj_3.add_protocol(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL)[index_3])
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX))):
                                obj_4 = vnc_api.PrefixMatchType()
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX) is not None:
                                    obj_4.set_prefix(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX))
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE) is not None:
                                    obj_4.set_prefix_type(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE))
                                obj_3.add_prefix(obj_4)
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY) is not None:
                            obj_3.set_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST))):
                                obj_3.add_community_list(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST)[index_3])
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL) is not None:
                            obj_3.set_community_match_all(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST))):
                                obj_3.add_extcommunity_list(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST)[index_3])
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL) is not None:
                            obj_3.set_extcommunity_match_all(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY) is not None:
                            obj_3.set_family(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH))):
                                obj_3.add_as_path(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH)[index_3])
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL) is not None:
                            obj_3.set_external(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF) is not None:
                            obj_3.set_local_pref(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE))):
                                obj_3.add_nlri_route_type(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE)[index_3])
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST))):
                                obj_4 = vnc_api.PrefixListMatchType()
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID) is not None:
                                    for index_4 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID))):
                                        obj_4.add_interface_route_table_uuid(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID)[index_4])
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE) is not None:
                                    obj_4.set_prefix_type(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE))
                                obj_3.add_prefix_list(obj_4)
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER) is not None:
                            obj_4 = vnc_api.RouteFilterType()
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES) is not None:
                                for index_4 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES))):
                                    obj_5 = vnc_api.RouteFilterProperties()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE) is not None:
                                        obj_5.set_route(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE))
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE) is not None:
                                        obj_5.set_route_type(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE))
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE) is not None:
                                        obj_5.set_route_type_value(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE))
                                    obj_4.add_route_filter_properties(obj_5)
                            obj_3.set_route_filter(obj_4)
                        obj_2.set_term_match_condition(obj_3)
                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST) is not None:
                        obj_3 = vnc_api.TermActionListType()
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE) is not None:
                            obj_4 = vnc_api.ActionUpdateType()
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH) is not None:
                                obj_5 = vnc_api.ActionAsPathType()
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND) is not None:
                                    obj_6 = vnc_api.AsListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST))):
                                            obj_6.add_asn_list(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST)[index_6])
                                    obj_5.set_expand(obj_6)
                                obj_4.set_as_path(obj_5)
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY) is not None:
                                obj_5 = vnc_api.ActionCommunityType()
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY)[index_6])
                                    obj_5.set_add(obj_6)
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY)[index_6])
                                    obj_5.set_remove(obj_6)
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY)[index_6])
                                    obj_5.set_set(obj_6)
                                obj_4.set_community(obj_5)
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY) is not None:
                                obj_5 = vnc_api.ActionExtCommunityType()
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY)[index_6])
                                    obj_5.set_add(obj_6)
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY)[index_6])
                                    obj_5.set_remove(obj_6)
                                if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY) is not None:
                                        for index_6 in range(len(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY))):
                                            obj_6.add_community(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY)[index_6])
                                    obj_5.set_set(obj_6)
                                obj_4.set_extcommunity(obj_5)
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF) is not None:
                                obj_4.set_local_pref(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF))
                            if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED) is not None:
                                obj_4.set_med(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED))
                            obj_3.set_update(obj_4)
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION) is not None:
                            obj_3.set_action(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL) is not None:
                            obj_3.set_external(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND) is not None:
                            obj_3.set_as_path_expand(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND))
                        if self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND) is not None:
                            obj_3.set_as_path_prepend(self.properties.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND))
                        obj_2.set_term_action_list(obj_3)
                    obj_1.add_term(obj_2)
            obj_0.set_routing_policy_entries(obj_1)
        if self.properties.get(self.TERM_TYPE) is not None:
            obj_0.set_term_type(self.properties.get(self.TERM_TYPE))
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

        # reference to service_instance_refs
        if len(self.properties.get(self.SERVICE_INSTANCE_REFS) or []) != len(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA) or []):
            raise Exception(_('routing-policy: specify service_instance_refs for each service_instance_refs_data.'))
        obj_1 = None
        if self.properties.get(self.SERVICE_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.RoutingPolicyServiceInstanceType()
                if self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE) is not None:
                    obj_1.set_left_sequence(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE))
                if self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE) is not None:
                    obj_1.set_right_sequence(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE))

                if self.properties.get(self.SERVICE_INSTANCE_REFS):
                    try:
                        ref_obj = self.vnc_lib().service_instance_read(
                            id=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().service_instance_read(
                            fq_name_str=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_service_instance(ref_obj, obj_1)

        # reference to routing_instance_refs
        if len(self.properties.get(self.ROUTING_INSTANCE_REFS) or []) != len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) or []):
            raise Exception(_('routing-policy: specify routing_instance_refs for each routing_instance_refs_data.'))
        obj_1 = None
        if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.RoutingPolicyType()
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SEQUENCE) is not None:
                    obj_1.set_sequence(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SEQUENCE))

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

        try:
            obj_uuid = super(ContrailRoutingPolicy, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().routing_policy_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ROUTING_POLICY_ENTRIES) is not None:
            obj_1 = vnc_api.PolicyStatementType()
            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM) is not None:
                for index_1 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM))):
                    obj_2 = vnc_api.PolicyTermType()
                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.TermMatchConditionType()
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL))):
                                obj_3.add_protocol(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PROTOCOL)[index_3])
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX))):
                                obj_4 = vnc_api.PrefixMatchType()
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX) is not None:
                                    obj_4.set_prefix(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX))
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE) is not None:
                                    obj_4.set_prefix_type(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_PREFIX_TYPE))
                                obj_3.add_prefix(obj_4)
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY) is not None:
                            obj_3.set_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST))):
                                obj_3.add_community_list(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_LIST)[index_3])
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL) is not None:
                            obj_3.set_community_match_all(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_COMMUNITY_MATCH_ALL))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST))):
                                obj_3.add_extcommunity_list(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_LIST)[index_3])
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL) is not None:
                            obj_3.set_extcommunity_match_all(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTCOMMUNITY_MATCH_ALL))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY) is not None:
                            obj_3.set_family(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_FAMILY))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH))):
                                obj_3.add_as_path(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_AS_PATH)[index_3])
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL) is not None:
                            obj_3.set_external(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_EXTERNAL))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF) is not None:
                            obj_3.set_local_pref(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_LOCAL_PREF))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE))):
                                obj_3.add_nlri_route_type(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_NLRI_ROUTE_TYPE)[index_3])
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST))):
                                obj_4 = vnc_api.PrefixListMatchType()
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID) is not None:
                                    for index_4 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID))):
                                        obj_4.add_interface_route_table_uuid(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_INTERFACE_ROUTE_TABLE_UUID)[index_4])
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE) is not None:
                                    obj_4.set_prefix_type(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST, {})[index_3].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_PREFIX_LIST_PREFIX_TYPE))
                                obj_3.add_prefix_list(obj_4)
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER) is not None:
                            obj_4 = vnc_api.RouteFilterType()
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES) is not None:
                                for index_4 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES))):
                                    obj_5 = vnc_api.RouteFilterProperties()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE) is not None:
                                        obj_5.set_route(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE))
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE) is not None:
                                        obj_5.set_route_type(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE))
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE) is not None:
                                        obj_5.set_route_type_value(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES, {})[index_4].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_MATCH_CONDITION_ROUTE_FILTER_ROUTE_FILTER_PROPERTIES_ROUTE_TYPE_VALUE))
                                    obj_4.add_route_filter_properties(obj_5)
                            obj_3.set_route_filter(obj_4)
                        obj_2.set_term_match_condition(obj_3)
                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST) is not None:
                        obj_3 = vnc_api.TermActionListType()
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE) is not None:
                            obj_4 = vnc_api.ActionUpdateType()
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH) is not None:
                                obj_5 = vnc_api.ActionAsPathType()
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND) is not None:
                                    obj_6 = vnc_api.AsListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST))):
                                            obj_6.add_asn_list(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_AS_PATH_EXPAND_ASN_LIST)[index_6])
                                    obj_5.set_expand(obj_6)
                                obj_4.set_as_path(obj_5)
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY) is not None:
                                obj_5 = vnc_api.ActionCommunityType()
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_ADD_COMMUNITY)[index_6])
                                    obj_5.set_add(obj_6)
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_REMOVE_COMMUNITY)[index_6])
                                    obj_5.set_remove(obj_6)
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET) is not None:
                                    obj_6 = vnc_api.CommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_COMMUNITY_SET_COMMUNITY)[index_6])
                                    obj_5.set_set(obj_6)
                                obj_4.set_community(obj_5)
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY) is not None:
                                obj_5 = vnc_api.ActionExtCommunityType()
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_ADD_COMMUNITY)[index_6])
                                    obj_5.set_add(obj_6)
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_REMOVE_COMMUNITY)[index_6])
                                    obj_5.set_remove(obj_6)
                                if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET) is not None:
                                    obj_6 = vnc_api.ExtCommunityListType()
                                    if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY) is not None:
                                        for index_6 in range(len(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY))):
                                            obj_6.add_community(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_EXTCOMMUNITY_SET_COMMUNITY)[index_6])
                                    obj_5.set_set(obj_6)
                                obj_4.set_extcommunity(obj_5)
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF) is not None:
                                obj_4.set_local_pref(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_LOCAL_PREF))
                            if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED) is not None:
                                obj_4.set_med(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_UPDATE_MED))
                            obj_3.set_update(obj_4)
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION) is not None:
                            obj_3.set_action(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_ACTION))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL) is not None:
                            obj_3.set_external(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_EXTERNAL))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND) is not None:
                            obj_3.set_as_path_expand(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_EXPAND))
                        if prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND) is not None:
                            obj_3.set_as_path_prepend(prop_diff.get(self.ROUTING_POLICY_ENTRIES, {}).get(self.ROUTING_POLICY_ENTRIES_TERM, {})[index_1].get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST, {}).get(self.ROUTING_POLICY_ENTRIES_TERM_TERM_ACTION_LIST_AS_PATH_PREPEND))
                        obj_2.set_term_action_list(obj_3)
                    obj_1.add_term(obj_2)
            obj_0.set_routing_policy_entries(obj_1)
        if prop_diff.get(self.TERM_TYPE) is not None:
            obj_0.set_term_type(prop_diff.get(self.TERM_TYPE))
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

        # reference to service_instance
        update = 0
        if not self.SERVICE_INSTANCE_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_service_instance_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.SERVICE_INSTANCE_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_service_instance_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.RoutingPolicyServiceInstanceType()
                if prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE) is not None:
                    obj_1.set_left_sequence(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_LEFT_SEQUENCE))
                if prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE) is not None:
                    obj_1.set_right_sequence(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_RIGHT_SEQUENCE))
                ref_data_list.append(obj_1)
        if self.SERVICE_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_INSTANCE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_instance_read(
                        id=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_instance_read(
                        fq_name_str=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('routing-policy: specify service_instance_refs_data for each service_instance_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_service_instance_list(ref_obj_list, ref_data_list)
        # End: reference to service_instance_refs

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
                obj_1 = vnc_api.RoutingPolicyType()
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SEQUENCE) is not None:
                    obj_1.set_sequence(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SEQUENCE))
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
            raise Exception(_('routing-policy: specify routing_instance_refs_data for each routing_instance_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_routing_instance_list(ref_obj_list, ref_data_list)
        # End: reference to routing_instance_refs

        try:
            self.vnc_lib().routing_policy_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().routing_policy_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('routing_policy %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().routing_policy_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::RoutingPolicy': ContrailRoutingPolicy,
    }
