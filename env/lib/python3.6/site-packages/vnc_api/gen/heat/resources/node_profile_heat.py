
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


class ContrailNodeProfile(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, NODE_PROFILE_ROLES, NODE_PROFILE_ROLES_ROLE_MAPPINGS, NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE, NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, NODE_PROFILE_HITLESS_UPGRADE, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, NODE_PROFILE_DEVICE_FAMILY, NODE_PROFILE_VENDOR, NODE_PROFILE_TYPE, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, HARDWARE_REFS, ROLE_DEFINITION_REFS, JOB_TEMPLATE_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'node_profile_roles', 'node_profile_roles_role_mappings', 'node_profile_roles_role_mappings_physical_role', 'node_profile_roles_role_mappings_rb_roles', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'node_profile_hitless_upgrade', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'node_profile_device_family', 'node_profile_vendor', 'node_profile_type', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'hardware_refs', 'role_definition_refs', 'job_template_refs', 'global_system_config'
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
        NODE_PROFILE_ROLES: properties.Schema(
            properties.Schema.MAP,
            _('NODE_PROFILE_ROLES.'),
            update_allowed=True,
            required=False,
            schema={
                NODE_PROFILE_ROLES_ROLE_MAPPINGS: properties.Schema(
                    properties.Schema.LIST,
                    _('NODE_PROFILE_ROLES_ROLE_MAPPINGS.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE: properties.Schema(
                                properties.Schema.STRING,
                                _('NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES: properties.Schema(
                                properties.Schema.LIST,
                                _('NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES.'),
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
        NODE_PROFILE_HITLESS_UPGRADE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('NODE_PROFILE_HITLESS_UPGRADE.'),
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
        NODE_PROFILE_DEVICE_FAMILY: properties.Schema(
            properties.Schema.STRING,
            _('NODE_PROFILE_DEVICE_FAMILY.'),
            update_allowed=True,
            required=False,
        ),
        NODE_PROFILE_VENDOR: properties.Schema(
            properties.Schema.STRING,
            _('NODE_PROFILE_VENDOR.'),
            update_allowed=True,
            required=False,
        ),
        NODE_PROFILE_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('NODE_PROFILE_TYPE.'),
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
        HARDWARE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('HARDWARE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROLE_DEFINITION_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROLE_DEFINITION_REFS.'),
            update_allowed=True,
            required=False,
        ),
        JOB_TEMPLATE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('JOB_TEMPLATE_REFS.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        NODE_PROFILE_ROLES: attributes.Schema(
            _('NODE_PROFILE_ROLES.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        NODE_PROFILE_HITLESS_UPGRADE: attributes.Schema(
            _('NODE_PROFILE_HITLESS_UPGRADE.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        NODE_PROFILE_DEVICE_FAMILY: attributes.Schema(
            _('NODE_PROFILE_DEVICE_FAMILY.'),
        ),
        NODE_PROFILE_VENDOR: attributes.Schema(
            _('NODE_PROFILE_VENDOR.'),
        ),
        NODE_PROFILE_TYPE: attributes.Schema(
            _('NODE_PROFILE_TYPE.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        HARDWARE_REFS: attributes.Schema(
            _('HARDWARE_REFS.'),
        ),
        ROLE_DEFINITION_REFS: attributes.Schema(
            _('ROLE_DEFINITION_REFS.'),
        ),
        JOB_TEMPLATE_REFS: attributes.Schema(
            _('JOB_TEMPLATE_REFS.'),
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

        obj_0 = vnc_api.NodeProfile(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.NODE_PROFILE_ROLES) is not None:
            obj_1 = vnc_api.NodeProfileRolesType()
            if self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS) is not None:
                for index_1 in range(len(self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS))):
                    obj_2 = vnc_api.NodeProfileRoleType()
                    if self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE) is not None:
                        obj_2.set_physical_role(self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE))
                    if self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES) is not None:
                        for index_2 in range(len(self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES))):
                            obj_2.add_rb_roles(self.properties.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES)[index_2])
                    obj_1.add_role_mappings(obj_2)
            obj_0.set_node_profile_roles(obj_1)
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
        if self.properties.get(self.NODE_PROFILE_HITLESS_UPGRADE) is not None:
            obj_0.set_node_profile_hitless_upgrade(self.properties.get(self.NODE_PROFILE_HITLESS_UPGRADE))
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
        if self.properties.get(self.NODE_PROFILE_DEVICE_FAMILY) is not None:
            obj_0.set_node_profile_device_family(self.properties.get(self.NODE_PROFILE_DEVICE_FAMILY))
        if self.properties.get(self.NODE_PROFILE_VENDOR) is not None:
            obj_0.set_node_profile_vendor(self.properties.get(self.NODE_PROFILE_VENDOR))
        if self.properties.get(self.NODE_PROFILE_TYPE) is not None:
            obj_0.set_node_profile_type(self.properties.get(self.NODE_PROFILE_TYPE))
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

        # reference to hardware_refs
        if self.properties.get(self.HARDWARE_REFS):
            for index_0 in range(len(self.properties.get(self.HARDWARE_REFS))):
                try:
                    ref_obj = self.vnc_lib().hardware_read(
                        id=self.properties.get(self.HARDWARE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().hardware_read(
                        fq_name_str=self.properties.get(self.HARDWARE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_hardware(ref_obj)

        # reference to role_definition_refs
        if self.properties.get(self.ROLE_DEFINITION_REFS):
            for index_0 in range(len(self.properties.get(self.ROLE_DEFINITION_REFS))):
                try:
                    ref_obj = self.vnc_lib().role_definition_read(
                        id=self.properties.get(self.ROLE_DEFINITION_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().role_definition_read(
                        fq_name_str=self.properties.get(self.ROLE_DEFINITION_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_role_definition(ref_obj)

        # reference to job_template_refs
        if self.properties.get(self.JOB_TEMPLATE_REFS):
            for index_0 in range(len(self.properties.get(self.JOB_TEMPLATE_REFS))):
                try:
                    ref_obj = self.vnc_lib().job_template_read(
                        id=self.properties.get(self.JOB_TEMPLATE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().job_template_read(
                        fq_name_str=self.properties.get(self.JOB_TEMPLATE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_job_template(ref_obj)

        try:
            obj_uuid = super(ContrailNodeProfile, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().node_profile_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.NODE_PROFILE_ROLES) is not None:
            obj_1 = vnc_api.NodeProfileRolesType()
            if prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS) is not None:
                for index_1 in range(len(prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS))):
                    obj_2 = vnc_api.NodeProfileRoleType()
                    if prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE) is not None:
                        obj_2.set_physical_role(prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_PHYSICAL_ROLE))
                    if prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES) is not None:
                        for index_2 in range(len(prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES))):
                            obj_2.add_rb_roles(prop_diff.get(self.NODE_PROFILE_ROLES, {}).get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS, {})[index_1].get(self.NODE_PROFILE_ROLES_ROLE_MAPPINGS_RB_ROLES)[index_2])
                    obj_1.add_role_mappings(obj_2)
            obj_0.set_node_profile_roles(obj_1)
        if prop_diff.get(self.NODE_PROFILE_HITLESS_UPGRADE) is not None:
            obj_0.set_node_profile_hitless_upgrade(prop_diff.get(self.NODE_PROFILE_HITLESS_UPGRADE))
        if prop_diff.get(self.NODE_PROFILE_DEVICE_FAMILY) is not None:
            obj_0.set_node_profile_device_family(prop_diff.get(self.NODE_PROFILE_DEVICE_FAMILY))
        if prop_diff.get(self.NODE_PROFILE_VENDOR) is not None:
            obj_0.set_node_profile_vendor(prop_diff.get(self.NODE_PROFILE_VENDOR))
        if prop_diff.get(self.NODE_PROFILE_TYPE) is not None:
            obj_0.set_node_profile_type(prop_diff.get(self.NODE_PROFILE_TYPE))
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

        # reference to hardware_refs
        ref_obj_list = []
        if self.HARDWARE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.HARDWARE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().hardware_read(
                        id=prop_diff.get(self.HARDWARE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().hardware_read(
                        fq_name_str=prop_diff.get(self.HARDWARE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_hardware_list(ref_obj_list)
            # End: reference to hardware_refs

        # reference to role_definition_refs
        ref_obj_list = []
        if self.ROLE_DEFINITION_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROLE_DEFINITION_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().role_definition_read(
                        id=prop_diff.get(self.ROLE_DEFINITION_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().role_definition_read(
                        fq_name_str=prop_diff.get(self.ROLE_DEFINITION_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_role_definition_list(ref_obj_list)
            # End: reference to role_definition_refs

        # reference to job_template_refs
        ref_obj_list = []
        if self.JOB_TEMPLATE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.JOB_TEMPLATE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().job_template_read(
                        id=prop_diff.get(self.JOB_TEMPLATE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().job_template_read(
                        fq_name_str=prop_diff.get(self.JOB_TEMPLATE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_job_template_list(ref_obj_list)
            # End: reference to job_template_refs

        try:
            self.vnc_lib().node_profile_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().node_profile_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('node_profile %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().node_profile_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::NodeProfile': ContrailNodeProfile,
    }
