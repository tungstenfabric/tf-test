
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


class ContrailFabric(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, FABRIC_OS_VERSION, FABRIC_ENTERPRISE_STYLE, DISPLAY_NAME, FABRIC_CREDENTIALS, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR, FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, FABRIC_ZTP, DISABLE_VLAN_VN_UNIQUENESS_CHECK, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, NODE_PROFILE_REFS, NODE_PROFILE_REFS_DATA, NODE_PROFILE_REFS_DATA_SERIAL_NUM, INTENT_MAP_REFS, VIRTUAL_NETWORK_REFS, VIRTUAL_NETWORK_REFS_DATA, VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'fabric_os_version', 'fabric_enterprise_style', 'display_name', 'fabric_credentials', 'fabric_credentials_device_credential', 'fabric_credentials_device_credential_credential', 'fabric_credentials_device_credential_credential_username', 'fabric_credentials_device_credential_credential_password', 'fabric_credentials_device_credential_vendor', 'fabric_credentials_device_credential_device_family', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'fabric_ztp', 'disable_vlan_vn_uniqueness_check', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'node_profile_refs', 'node_profile_refs_data', 'node_profile_refs_data_serial_num', 'intent_map_refs', 'virtual_network_refs', 'virtual_network_refs_data', 'virtual_network_refs_data_network_type', 'global_system_config'
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
        FABRIC_OS_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('FABRIC_OS_VERSION.'),
            update_allowed=True,
            required=False,
        ),
        FABRIC_ENTERPRISE_STYLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FABRIC_ENTERPRISE_STYLE.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        FABRIC_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('FABRIC_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                FABRIC_CREDENTIALS_DEVICE_CREDENTIAL: properties.Schema(
                    properties.Schema.LIST,
                    _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL: properties.Schema(
                                properties.Schema.MAP,
                                _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME: properties.Schema(
                                        properties.Schema.STRING,
                                        _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD: properties.Schema(
                                        properties.Schema.STRING,
                                        _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR: properties.Schema(
                                properties.Schema.STRING,
                                _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY: properties.Schema(
                                properties.Schema.STRING,
                                _('FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY.'),
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
        FABRIC_ZTP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FABRIC_ZTP.'),
            update_allowed=True,
            required=False,
        ),
        DISABLE_VLAN_VN_UNIQUENESS_CHECK: properties.Schema(
            properties.Schema.BOOLEAN,
            _('DISABLE_VLAN_VN_UNIQUENESS_CHECK.'),
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
        NODE_PROFILE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NODE_PROFILE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NODE_PROFILE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NODE_PROFILE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NODE_PROFILE_REFS_DATA_SERIAL_NUM: properties.Schema(
                        properties.Schema.LIST,
                        _('NODE_PROFILE_REFS_DATA_SERIAL_NUM.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        INTENT_MAP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('INTENT_MAP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE.'),
                        update_allowed=True,
                        required=False,
                        constraints=[
                            constraints.AllowedValues([u'management', u'loopback', u'ip-fabric', u'pnf-servicechain', u'overlay-loopback']),
                        ],
                    ),
                }
            )
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
        FABRIC_OS_VERSION: attributes.Schema(
            _('FABRIC_OS_VERSION.'),
        ),
        FABRIC_ENTERPRISE_STYLE: attributes.Schema(
            _('FABRIC_ENTERPRISE_STYLE.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        FABRIC_CREDENTIALS: attributes.Schema(
            _('FABRIC_CREDENTIALS.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        FABRIC_ZTP: attributes.Schema(
            _('FABRIC_ZTP.'),
        ),
        DISABLE_VLAN_VN_UNIQUENESS_CHECK: attributes.Schema(
            _('DISABLE_VLAN_VN_UNIQUENESS_CHECK.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        NODE_PROFILE_REFS: attributes.Schema(
            _('NODE_PROFILE_REFS.'),
        ),
        NODE_PROFILE_REFS_DATA: attributes.Schema(
            _('NODE_PROFILE_REFS_DATA.'),
        ),
        INTENT_MAP_REFS: attributes.Schema(
            _('INTENT_MAP_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS_DATA: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS_DATA.'),
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

        obj_0 = vnc_api.Fabric(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.FABRIC_OS_VERSION) is not None:
            obj_0.set_fabric_os_version(self.properties.get(self.FABRIC_OS_VERSION))
        if self.properties.get(self.FABRIC_ENTERPRISE_STYLE) is not None:
            obj_0.set_fabric_enterprise_style(self.properties.get(self.FABRIC_ENTERPRISE_STYLE))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.FABRIC_CREDENTIALS) is not None:
            obj_1 = vnc_api.DeviceCredentialList()
            if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL) is not None:
                for index_1 in range(len(self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL))):
                    obj_2 = vnc_api.DeviceCredential()
                    if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL) is not None:
                        obj_3 = vnc_api.UserCredentials()
                        if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME) is not None:
                            obj_3.set_username(self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME))
                        if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD) is not None:
                            obj_3.set_password(self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD))
                        obj_2.set_credential(obj_3)
                    if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR) is not None:
                        obj_2.set_vendor(self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR))
                    if self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY) is not None:
                        obj_2.set_device_family(self.properties.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY))
                    obj_1.add_device_credential(obj_2)
            obj_0.set_fabric_credentials(obj_1)
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
        if self.properties.get(self.FABRIC_ZTP) is not None:
            obj_0.set_fabric_ztp(self.properties.get(self.FABRIC_ZTP))
        if self.properties.get(self.DISABLE_VLAN_VN_UNIQUENESS_CHECK) is not None:
            obj_0.set_disable_vlan_vn_uniqueness_check(self.properties.get(self.DISABLE_VLAN_VN_UNIQUENESS_CHECK))
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

        # reference to node_profile_refs
        if len(self.properties.get(self.NODE_PROFILE_REFS) or []) != len(self.properties.get(self.NODE_PROFILE_REFS_DATA) or []):
            raise Exception(_('fabric: specify node_profile_refs for each node_profile_refs_data.'))
        obj_1 = None
        if self.properties.get(self.NODE_PROFILE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NODE_PROFILE_REFS_DATA))):
                obj_1 = vnc_api.SerialNumListType()
                if self.properties.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM) is not None:
                    for index_1 in range(len(self.properties.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM))):
                        obj_1.add_serial_num(self.properties.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM)[index_1])

                if self.properties.get(self.NODE_PROFILE_REFS):
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
                    obj_0.add_node_profile(ref_obj, obj_1)

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

        # reference to virtual_network_refs
        if len(self.properties.get(self.VIRTUAL_NETWORK_REFS) or []) != len(self.properties.get(self.VIRTUAL_NETWORK_REFS_DATA) or []):
            raise Exception(_('fabric: specify virtual_network_refs for each virtual_network_refs_data.'))
        obj_1 = None
        if self.properties.get(self.VIRTUAL_NETWORK_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.VIRTUAL_NETWORK_REFS_DATA))):
                obj_1 = vnc_api.FabricNetworkTag()
                if self.properties.get(self.VIRTUAL_NETWORK_REFS_DATA, {})[index_0].get(self.VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE) is not None:
                    obj_1.set_network_type(self.properties.get(self.VIRTUAL_NETWORK_REFS_DATA, {})[index_0].get(self.VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE))

                if self.properties.get(self.VIRTUAL_NETWORK_REFS):
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
                    obj_0.add_virtual_network(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailFabric, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().fabric_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.FABRIC_OS_VERSION) is not None:
            obj_0.set_fabric_os_version(prop_diff.get(self.FABRIC_OS_VERSION))
        if prop_diff.get(self.FABRIC_ENTERPRISE_STYLE) is not None:
            obj_0.set_fabric_enterprise_style(prop_diff.get(self.FABRIC_ENTERPRISE_STYLE))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.FABRIC_CREDENTIALS) is not None:
            obj_1 = vnc_api.DeviceCredentialList()
            if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL) is not None:
                for index_1 in range(len(prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL))):
                    obj_2 = vnc_api.DeviceCredential()
                    if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL) is not None:
                        obj_3 = vnc_api.UserCredentials()
                        if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME) is not None:
                            obj_3.set_username(prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_USERNAME))
                        if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD) is not None:
                            obj_3.set_password(prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_CREDENTIAL_PASSWORD))
                        obj_2.set_credential(obj_3)
                    if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR) is not None:
                        obj_2.set_vendor(prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_VENDOR))
                    if prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY) is not None:
                        obj_2.set_device_family(prop_diff.get(self.FABRIC_CREDENTIALS, {}).get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL, {})[index_1].get(self.FABRIC_CREDENTIALS_DEVICE_CREDENTIAL_DEVICE_FAMILY))
                    obj_1.add_device_credential(obj_2)
            obj_0.set_fabric_credentials(obj_1)
        if prop_diff.get(self.FABRIC_ZTP) is not None:
            obj_0.set_fabric_ztp(prop_diff.get(self.FABRIC_ZTP))
        if prop_diff.get(self.DISABLE_VLAN_VN_UNIQUENESS_CHECK) is not None:
            obj_0.set_disable_vlan_vn_uniqueness_check(prop_diff.get(self.DISABLE_VLAN_VN_UNIQUENESS_CHECK))
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

        # reference to node_profile
        update = 0
        if not self.NODE_PROFILE_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_node_profile_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.NODE_PROFILE_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_node_profile_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.NODE_PROFILE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NODE_PROFILE_REFS_DATA))):
                obj_1 = vnc_api.SerialNumListType()
                if prop_diff.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM) is not None:
                    for index_1 in range(len(prop_diff.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM))):
                        obj_1.add_serial_num(prop_diff.get(self.NODE_PROFILE_REFS_DATA, {})[index_0].get(self.NODE_PROFILE_REFS_DATA_SERIAL_NUM)[index_1])
                ref_data_list.append(obj_1)
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
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('fabric: specify node_profile_refs_data for each node_profile_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_node_profile_list(ref_obj_list, ref_data_list)
        # End: reference to node_profile_refs

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

        # reference to virtual_network
        update = 0
        if not self.VIRTUAL_NETWORK_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_virtual_network_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.VIRTUAL_NETWORK_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_virtual_network_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.VIRTUAL_NETWORK_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_REFS_DATA))):
                obj_1 = vnc_api.FabricNetworkTag()
                if prop_diff.get(self.VIRTUAL_NETWORK_REFS_DATA, {})[index_0].get(self.VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE) is not None:
                    obj_1.set_network_type(prop_diff.get(self.VIRTUAL_NETWORK_REFS_DATA, {})[index_0].get(self.VIRTUAL_NETWORK_REFS_DATA_NETWORK_TYPE))
                ref_data_list.append(obj_1)
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
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('fabric: specify virtual_network_refs_data for each virtual_network_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_virtual_network_list(ref_obj_list, ref_data_list)
        # End: reference to virtual_network_refs

        try:
            self.vnc_lib().fabric_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().fabric_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('fabric %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().fabric_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Fabric': ContrailFabric,
    }
