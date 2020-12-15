
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


class ContrailPort(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ESXI_PORT_INFO, ESXI_PORT_INFO_DVS_NAME, ESXI_PORT_INFO_DVS_ID, BMS_PORT_INFO, BMS_PORT_INFO_PXE_ENABLED, BMS_PORT_INFO_LOCAL_LINK_CONNECTION, BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO, BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX, BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID, BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID, BMS_PORT_INFO_NODE_UUID, BMS_PORT_INFO_ADDRESS, LABEL, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PORT_GROUP_UUID, TAG_REFS, NODE
    ) = (
        'name', 'fq_name', 'display_name', 'esxi_port_info', 'esxi_port_info_dvs_name', 'esxi_port_info_dvs_id', 'bms_port_info', 'bms_port_info_pxe_enabled', 'bms_port_info_local_link_connection', 'bms_port_info_local_link_connection_switch_info', 'bms_port_info_local_link_connection_port_index', 'bms_port_info_local_link_connection_port_id', 'bms_port_info_local_link_connection_switch_id', 'bms_port_info_node_uuid', 'bms_port_info_address', 'label', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'port_group_uuid', 'tag_refs', 'node'
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
        ESXI_PORT_INFO: properties.Schema(
            properties.Schema.MAP,
            _('ESXI_PORT_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                ESXI_PORT_INFO_DVS_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_PORT_INFO_DVS_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_PORT_INFO_DVS_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_PORT_INFO_DVS_ID.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        BMS_PORT_INFO: properties.Schema(
            properties.Schema.MAP,
            _('BMS_PORT_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                BMS_PORT_INFO_PXE_ENABLED: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BMS_PORT_INFO_PXE_ENABLED.'),
                    update_allowed=True,
                    required=False,
                ),
                BMS_PORT_INFO_LOCAL_LINK_CONNECTION: properties.Schema(
                    properties.Schema.MAP,
                    _('BMS_PORT_INFO_LOCAL_LINK_CONNECTION.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                BMS_PORT_INFO_NODE_UUID: properties.Schema(
                    properties.Schema.STRING,
                    _('BMS_PORT_INFO_NODE_UUID.'),
                    update_allowed=True,
                    required=False,
                ),
                BMS_PORT_INFO_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('BMS_PORT_INFO_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        LABEL: properties.Schema(
            properties.Schema.STRING,
            _('LABEL.'),
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
        PORT_GROUP_UUID: properties.Schema(
            properties.Schema.STRING,
            _('PORT_GROUP_UUID.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NODE: properties.Schema(
            properties.Schema.STRING,
            _('NODE.'),
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
        ESXI_PORT_INFO: attributes.Schema(
            _('ESXI_PORT_INFO.'),
        ),
        BMS_PORT_INFO: attributes.Schema(
            _('BMS_PORT_INFO.'),
        ),
        LABEL: attributes.Schema(
            _('LABEL.'),
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
        PORT_GROUP_UUID: attributes.Schema(
            _('PORT_GROUP_UUID.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        NODE: attributes.Schema(
            _('NODE.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.NODE) and self.properties.get(self.NODE) != 'config-root':
            try:
                parent_obj = self.vnc_lib().node_read(fq_name_str=self.properties.get(self.NODE))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().node_read(id=str(uuid.UUID(self.properties.get(self.NODE))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.NODE) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.Port(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ESXI_PORT_INFO) is not None:
            obj_1 = vnc_api.ESXIProperties()
            if self.properties.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_NAME) is not None:
                obj_1.set_dvs_name(self.properties.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_NAME))
            if self.properties.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_ID) is not None:
                obj_1.set_dvs_id(self.properties.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_ID))
            obj_0.set_esxi_port_info(obj_1)
        if self.properties.get(self.BMS_PORT_INFO) is not None:
            obj_1 = vnc_api.BaremetalPortInfo()
            if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_PXE_ENABLED) is not None:
                obj_1.set_pxe_enabled(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_PXE_ENABLED))
            if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION) is not None:
                obj_2 = vnc_api.LocalLinkConnection()
                if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO) is not None:
                    obj_2.set_switch_info(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO))
                if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX) is not None:
                    obj_2.set_port_index(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX))
                if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID) is not None:
                    obj_2.set_port_id(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID))
                if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID) is not None:
                    obj_2.set_switch_id(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID))
                obj_1.set_local_link_connection(obj_2)
            if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_NODE_UUID) is not None:
                obj_1.set_node_uuid(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_NODE_UUID))
            if self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_ADDRESS) is not None:
                obj_1.set_address(self.properties.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_ADDRESS))
            obj_0.set_bms_port_info(obj_1)
        if self.properties.get(self.LABEL) is not None:
            obj_0.set_label(self.properties.get(self.LABEL))
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
        if self.properties.get(self.PORT_GROUP_UUID) is not None:
            obj_0.set_port_group_uuid(self.properties.get(self.PORT_GROUP_UUID))

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
            obj_uuid = super(ContrailPort, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().port_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ESXI_PORT_INFO) is not None:
            obj_1 = vnc_api.ESXIProperties()
            if prop_diff.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_NAME) is not None:
                obj_1.set_dvs_name(prop_diff.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_NAME))
            if prop_diff.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_ID) is not None:
                obj_1.set_dvs_id(prop_diff.get(self.ESXI_PORT_INFO, {}).get(self.ESXI_PORT_INFO_DVS_ID))
            obj_0.set_esxi_port_info(obj_1)
        if prop_diff.get(self.BMS_PORT_INFO) is not None:
            obj_1 = vnc_api.BaremetalPortInfo()
            if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_PXE_ENABLED) is not None:
                obj_1.set_pxe_enabled(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_PXE_ENABLED))
            if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION) is not None:
                obj_2 = vnc_api.LocalLinkConnection()
                if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO) is not None:
                    obj_2.set_switch_info(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_INFO))
                if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX) is not None:
                    obj_2.set_port_index(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_INDEX))
                if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID) is not None:
                    obj_2.set_port_id(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_PORT_ID))
                if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID) is not None:
                    obj_2.set_switch_id(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION, {}).get(self.BMS_PORT_INFO_LOCAL_LINK_CONNECTION_SWITCH_ID))
                obj_1.set_local_link_connection(obj_2)
            if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_NODE_UUID) is not None:
                obj_1.set_node_uuid(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_NODE_UUID))
            if prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_ADDRESS) is not None:
                obj_1.set_address(prop_diff.get(self.BMS_PORT_INFO, {}).get(self.BMS_PORT_INFO_ADDRESS))
            obj_0.set_bms_port_info(obj_1)
        if prop_diff.get(self.LABEL) is not None:
            obj_0.set_label(prop_diff.get(self.LABEL))
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
        if prop_diff.get(self.PORT_GROUP_UUID) is not None:
            obj_0.set_port_group_uuid(prop_diff.get(self.PORT_GROUP_UUID))

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
            self.vnc_lib().port_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().port_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('port %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().port_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Port': ContrailPort,
    }
