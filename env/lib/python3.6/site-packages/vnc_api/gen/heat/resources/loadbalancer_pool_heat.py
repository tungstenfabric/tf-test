
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


class ContrailLoadbalancerPool(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, LOADBALANCER_POOL_PROVIDER, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, LOADBALANCER_POOL_PROPERTIES, LOADBALANCER_POOL_PROPERTIES_STATUS, LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION, LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE, LOADBALANCER_POOL_PROPERTIES_PROTOCOL, LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD, LOADBALANCER_POOL_PROPERTIES_SUBNET_ID, LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE, LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE, SERVICE_APPLIANCE_SET_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, LOADBALANCER_LISTENER_REFS, TAG_REFS, SERVICE_INSTANCE_REFS, LOADBALANCER_HEALTHMONITOR_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'loadbalancer_pool_provider', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'loadbalancer_pool_properties', 'loadbalancer_pool_properties_status', 'loadbalancer_pool_properties_status_description', 'loadbalancer_pool_properties_admin_state', 'loadbalancer_pool_properties_protocol', 'loadbalancer_pool_properties_loadbalancer_method', 'loadbalancer_pool_properties_subnet_id', 'loadbalancer_pool_properties_session_persistence', 'loadbalancer_pool_properties_persistence_cookie_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'loadbalancer_pool_custom_attributes', 'loadbalancer_pool_custom_attributes_key_value_pair', 'loadbalancer_pool_custom_attributes_key_value_pair_key', 'loadbalancer_pool_custom_attributes_key_value_pair_value', 'service_appliance_set_refs', 'virtual_machine_interface_refs', 'loadbalancer_listener_refs', 'tag_refs', 'service_instance_refs', 'loadbalancer_healthmonitor_refs', 'project'
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
        LOADBALANCER_POOL_PROVIDER: properties.Schema(
            properties.Schema.STRING,
            _('LOADBALANCER_POOL_PROVIDER.'),
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
        LOADBALANCER_POOL_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_POOL_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_POOL_PROPERTIES_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'HTTP', u'HTTPS', u'TCP', u'UDP', u'TERMINATED_HTTPS']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'ROUND_ROBIN', u'LEAST_CONNECTIONS', u'SOURCE_IP']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_SUBNET_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_SUBNET_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME.'),
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
        LOADBALANCER_POOL_CUSTOM_ATTRIBUTES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        SERVICE_APPLIANCE_SET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_APPLIANCE_SET_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        LOADBALANCER_LISTENER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_LISTENER_REFS.'),
            update_allowed=True,
            required=False,
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
        LOADBALANCER_HEALTHMONITOR_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_HEALTHMONITOR_REFS.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        LOADBALANCER_POOL_PROVIDER: attributes.Schema(
            _('LOADBALANCER_POOL_PROVIDER.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        LOADBALANCER_POOL_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_POOL_PROPERTIES.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        LOADBALANCER_POOL_CUSTOM_ATTRIBUTES: attributes.Schema(
            _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES.'),
        ),
        SERVICE_APPLIANCE_SET_REFS: attributes.Schema(
            _('SERVICE_APPLIANCE_SET_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        LOADBALANCER_LISTENER_REFS: attributes.Schema(
            _('LOADBALANCER_LISTENER_REFS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        LOADBALANCER_HEALTHMONITOR_REFS: attributes.Schema(
            _('LOADBALANCER_HEALTHMONITOR_REFS.'),
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

        obj_0 = vnc_api.LoadbalancerPool(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.LOADBALANCER_POOL_PROVIDER) is not None:
            obj_0.set_loadbalancer_pool_provider(self.properties.get(self.LOADBALANCER_POOL_PROVIDER))
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
        if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerPoolType()
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS) is not None:
                obj_1.set_status(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD) is not None:
                obj_1.set_loadbalancer_method(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE) is not None:
                obj_1.set_session_persistence(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            obj_0.set_loadbalancer_pool_properties(obj_1)
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
        if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_loadbalancer_pool_custom_attributes(obj_1)

        # reference to service_appliance_set_refs
        if self.properties.get(self.SERVICE_APPLIANCE_SET_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_APPLIANCE_SET_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_service_appliance_set(ref_obj)

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

        # reference to loadbalancer_listener_refs
        if self.properties.get(self.LOADBALANCER_LISTENER_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_LISTENER_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        id=self.properties.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_loadbalancer_listener(ref_obj)

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
        if self.properties.get(self.SERVICE_INSTANCE_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_INSTANCE_REFS))):
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
                obj_0.add_service_instance(ref_obj)

        # reference to loadbalancer_healthmonitor_refs
        if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        id=self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_loadbalancer_healthmonitor(ref_obj)

        try:
            obj_uuid = super(ContrailLoadbalancerPool, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_pool_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerPoolType()
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS) is not None:
                obj_1.set_status(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD) is not None:
                obj_1.set_loadbalancer_method(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE) is not None:
                obj_1.set_session_persistence(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            obj_0.set_loadbalancer_pool_properties(obj_1)
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
        if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_loadbalancer_pool_custom_attributes(obj_1)

        # reference to service_appliance_set_refs
        ref_obj_list = []
        if self.SERVICE_APPLIANCE_SET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_service_appliance_set_list(ref_obj_list)
            # End: reference to service_appliance_set_refs

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

        # reference to loadbalancer_listener_refs
        ref_obj_list = []
        if self.LOADBALANCER_LISTENER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_LISTENER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        id=prop_diff.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_loadbalancer_listener_list(ref_obj_list)
            # End: reference to loadbalancer_listener_refs

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

        # reference to service_instance_refs
        ref_obj_list = []
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
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_service_instance_list(ref_obj_list)
            # End: reference to service_instance_refs

        # reference to loadbalancer_healthmonitor_refs
        ref_obj_list = []
        if self.LOADBALANCER_HEALTHMONITOR_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        id=prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_loadbalancer_healthmonitor_list(ref_obj_list)
            # End: reference to loadbalancer_healthmonitor_refs

        try:
            self.vnc_lib().loadbalancer_pool_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_pool_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_pool %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_pool_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerPool': ContrailLoadbalancerPool,
    }
