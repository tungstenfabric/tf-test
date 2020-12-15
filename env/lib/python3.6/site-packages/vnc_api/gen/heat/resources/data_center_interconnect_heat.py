
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


class ContrailDataCenterInterconnect(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY, DISPLAY_NAME, DATA_CENTER_INTERCONNECT_TYPE, DATA_CENTER_INTERCONNECT_MODE, DESTINATION_PHYSICAL_ROUTER_LIST, DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID, DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, LOGICAL_ROUTER_REFS, ROUTING_POLICY_REFS, VIRTUAL_NETWORK_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'data_center_interconnect_bgp_address_families', 'data_center_interconnect_bgp_address_families_family', 'display_name', 'data_center_interconnect_type', 'data_center_interconnect_mode', 'destination_physical_router_list', 'destination_physical_router_list_logical_router_list', 'destination_physical_router_list_logical_router_list_logical_router_uuid', 'destination_physical_router_list_logical_router_list_physical_router_uuid_list', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'data_center_interconnect_bgp_hold_time', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'data_center_interconnect_configured_route_target_list', 'data_center_interconnect_configured_route_target_list_route_target', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'logical_router_refs', 'routing_policy_refs', 'virtual_network_refs', 'global_system_config'
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
        DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES: properties.Schema(
            properties.Schema.MAP,
            _('DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES.'),
            update_allowed=True,
            required=False,
            schema={
                DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY: properties.Schema(
                    properties.Schema.LIST,
                    _('DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'inet', u'inet-labeled', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet-mvpn', u'inet6-vpn']),
                    ],
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DATA_CENTER_INTERCONNECT_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('DATA_CENTER_INTERCONNECT_TYPE.'),
            update_allowed=True,
            required=False,
        ),
        DATA_CENTER_INTERCONNECT_MODE: properties.Schema(
            properties.Schema.STRING,
            _('DATA_CENTER_INTERCONNECT_MODE.'),
            update_allowed=True,
            required=False,
        ),
        DESTINATION_PHYSICAL_ROUTER_LIST: properties.Schema(
            properties.Schema.MAP,
            _('DESTINATION_PHYSICAL_ROUTER_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST: properties.Schema(
                    properties.Schema.LIST,
                    _('DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST: properties.Schema(
                                properties.Schema.LIST,
                                _('DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST.'),
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
        DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME: properties.Schema(
            properties.Schema.INTEGER,
            _('DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME.'),
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
        DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
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
        LOGICAL_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOGICAL_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
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
        DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        DATA_CENTER_INTERCONNECT_TYPE: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_TYPE.'),
        ),
        DATA_CENTER_INTERCONNECT_MODE: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_MODE.'),
        ),
        DESTINATION_PHYSICAL_ROUTER_LIST: attributes.Schema(
            _('DESTINATION_PHYSICAL_ROUTER_LIST.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST: attributes.Schema(
            _('DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        LOGICAL_ROUTER_REFS: attributes.Schema(
            _('LOGICAL_ROUTER_REFS.'),
        ),
        ROUTING_POLICY_REFS: attributes.Schema(
            _('ROUTING_POLICY_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
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

        obj_0 = vnc_api.DataCenterInterconnect(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES) is not None:
            obj_1 = vnc_api.AddressFamilies()
            if self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY) is not None:
                for index_1 in range(len(self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY))):
                    obj_1.add_family(self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY)[index_1])
            obj_0.set_data_center_interconnect_bgp_address_families(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_TYPE) is not None:
            obj_0.set_data_center_interconnect_type(self.properties.get(self.DATA_CENTER_INTERCONNECT_TYPE))
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_MODE) is not None:
            obj_0.set_data_center_interconnect_mode(self.properties.get(self.DATA_CENTER_INTERCONNECT_MODE))
        if self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST) is not None:
            obj_1 = vnc_api.LogicalRouterPRListType()
            if self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST) is not None:
                for index_1 in range(len(self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST))):
                    obj_2 = vnc_api.LogicalRouterPRListParams()
                    if self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID) is not None:
                        obj_2.set_logical_router_uuid(self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID))
                    if self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST) is not None:
                        for index_2 in range(len(self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST))):
                            obj_2.add_physical_router_uuid_list(self.properties.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST)[index_2])
                    obj_1.add_logical_router_list(obj_2)
            obj_0.set_destination_physical_router_list(obj_1)
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
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME) is not None:
            obj_0.set_data_center_interconnect_bgp_hold_time(self.properties.get(self.DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME))
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
        if self.properties.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_data_center_interconnect_configured_route_target_list(obj_1)
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

        # reference to logical_router_refs
        if self.properties.get(self.LOGICAL_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.LOGICAL_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().logical_router_read(
                        id=self.properties.get(self.LOGICAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().logical_router_read(
                        fq_name_str=self.properties.get(self.LOGICAL_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_logical_router(ref_obj)

        # reference to routing_policy_refs
        if self.properties.get(self.ROUTING_POLICY_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTING_POLICY_REFS))):
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
                obj_0.add_routing_policy(ref_obj)

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

        try:
            obj_uuid = super(ContrailDataCenterInterconnect, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().data_center_interconnect_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES) is not None:
            obj_1 = vnc_api.AddressFamilies()
            if prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY) is not None:
                for index_1 in range(len(prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY))):
                    obj_1.add_family(prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES, {}).get(self.DATA_CENTER_INTERCONNECT_BGP_ADDRESS_FAMILIES_FAMILY)[index_1])
            obj_0.set_data_center_interconnect_bgp_address_families(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_TYPE) is not None:
            obj_0.set_data_center_interconnect_type(prop_diff.get(self.DATA_CENTER_INTERCONNECT_TYPE))
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_MODE) is not None:
            obj_0.set_data_center_interconnect_mode(prop_diff.get(self.DATA_CENTER_INTERCONNECT_MODE))
        if prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST) is not None:
            obj_1 = vnc_api.LogicalRouterPRListType()
            if prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST) is not None:
                for index_1 in range(len(prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST))):
                    obj_2 = vnc_api.LogicalRouterPRListParams()
                    if prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID) is not None:
                        obj_2.set_logical_router_uuid(prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_LOGICAL_ROUTER_UUID))
                    if prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST) is not None:
                        for index_2 in range(len(prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST))):
                            obj_2.add_physical_router_uuid_list(prop_diff.get(self.DESTINATION_PHYSICAL_ROUTER_LIST, {}).get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST, {})[index_1].get(self.DESTINATION_PHYSICAL_ROUTER_LIST_LOGICAL_ROUTER_LIST_PHYSICAL_ROUTER_UUID_LIST)[index_2])
                    obj_1.add_logical_router_list(obj_2)
            obj_0.set_destination_physical_router_list(obj_1)
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME) is not None:
            obj_0.set_data_center_interconnect_bgp_hold_time(prop_diff.get(self.DATA_CENTER_INTERCONNECT_BGP_HOLD_TIME))
        if prop_diff.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.DATA_CENTER_INTERCONNECT_CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_data_center_interconnect_configured_route_target_list(obj_1)
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

        # reference to logical_router_refs
        ref_obj_list = []
        if self.LOGICAL_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOGICAL_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().logical_router_read(
                        id=prop_diff.get(self.LOGICAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().logical_router_read(
                        fq_name_str=prop_diff.get(self.LOGICAL_ROUTER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_logical_router_list(ref_obj_list)
            # End: reference to logical_router_refs

        # reference to routing_policy_refs
        ref_obj_list = []
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
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_routing_policy_list(ref_obj_list)
            # End: reference to routing_policy_refs

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

        try:
            self.vnc_lib().data_center_interconnect_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().data_center_interconnect_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('data_center_interconnect %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().data_center_interconnect_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::DataCenterInterconnect': ContrailDataCenterInterconnect,
    }
