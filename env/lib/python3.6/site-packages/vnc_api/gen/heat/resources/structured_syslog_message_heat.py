
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


class ContrailStructuredSyslogMessage(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE, DISPLAY_NAME, STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES, STRUCTURED_SYSLOG_MESSAGE_FORWARD, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE, TAG_REFS, STRUCTURED_SYSLOG_CONFIG
    ) = (
        'name', 'fq_name', 'structured_syslog_message_process_and_store', 'display_name', 'structured_syslog_message_process_and_summarize_user', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'structured_syslog_message_integer_fields', 'structured_syslog_message_integer_fields_field_names', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'structured_syslog_message_tagged_fields', 'structured_syslog_message_tagged_fields_field_names', 'structured_syslog_message_forward', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'structured_syslog_message_process_and_summarize', 'tag_refs', 'structured_syslog_config'
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
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER: properties.Schema(
            properties.Schema.BOOLEAN,
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER.'),
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
        STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS: properties.Schema(
            properties.Schema.MAP,
            _('STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS.'),
            update_allowed=True,
            required=False,
            schema={
                STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES: properties.Schema(
                    properties.Schema.LIST,
                    _('STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES.'),
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
        STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS: properties.Schema(
            properties.Schema.MAP,
            _('STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS.'),
            update_allowed=True,
            required=False,
            schema={
                STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES: properties.Schema(
                    properties.Schema.LIST,
                    _('STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        STRUCTURED_SYSLOG_MESSAGE_FORWARD: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_MESSAGE_FORWARD.'),
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
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        STRUCTURED_SYSLOG_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('STRUCTURED_SYSLOG_CONFIG.'),
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
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS.'),
        ),
        STRUCTURED_SYSLOG_MESSAGE_FORWARD: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_FORWARD.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE: attributes.Schema(
            _('STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        STRUCTURED_SYSLOG_CONFIG: attributes.Schema(
            _('STRUCTURED_SYSLOG_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().structured_syslog_config_read(fq_name_str=self.properties.get(self.STRUCTURED_SYSLOG_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().structured_syslog_config_read(id=str(uuid.UUID(self.properties.get(self.STRUCTURED_SYSLOG_CONFIG))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.STRUCTURED_SYSLOG_CONFIG) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.StructuredSyslogMessage(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE) is not None:
            obj_0.set_structured_syslog_message_process_and_store(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER) is not None:
            obj_0.set_structured_syslog_message_process_and_summarize_user(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER))
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
        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS) is not None:
            obj_1 = vnc_api.FieldNamesList()
            if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES) is not None:
                for index_1 in range(len(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES))):
                    obj_1.add_field_names(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES)[index_1])
            obj_0.set_structured_syslog_message_integer_fields(obj_1)
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
        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS) is not None:
            obj_1 = vnc_api.FieldNamesList()
            if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES) is not None:
                for index_1 in range(len(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES))):
                    obj_1.add_field_names(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES)[index_1])
            obj_0.set_structured_syslog_message_tagged_fields(obj_1)
        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_FORWARD) is not None:
            obj_0.set_structured_syslog_message_forward(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_FORWARD))
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
        if self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE) is not None:
            obj_0.set_structured_syslog_message_process_and_summarize(self.properties.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE))

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
            obj_uuid = super(ContrailStructuredSyslogMessage, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().structured_syslog_message_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE) is not None:
            obj_0.set_structured_syslog_message_process_and_store(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_STORE))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER) is not None:
            obj_0.set_structured_syslog_message_process_and_summarize_user(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE_USER))
        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS) is not None:
            obj_1 = vnc_api.FieldNamesList()
            if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES) is not None:
                for index_1 in range(len(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES))):
                    obj_1.add_field_names(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_INTEGER_FIELDS_FIELD_NAMES)[index_1])
            obj_0.set_structured_syslog_message_integer_fields(obj_1)
        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS) is not None:
            obj_1 = vnc_api.FieldNamesList()
            if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES) is not None:
                for index_1 in range(len(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES))):
                    obj_1.add_field_names(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS, {}).get(self.STRUCTURED_SYSLOG_MESSAGE_TAGGED_FIELDS_FIELD_NAMES)[index_1])
            obj_0.set_structured_syslog_message_tagged_fields(obj_1)
        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_FORWARD) is not None:
            obj_0.set_structured_syslog_message_forward(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_FORWARD))
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
        if prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE) is not None:
            obj_0.set_structured_syslog_message_process_and_summarize(prop_diff.get(self.STRUCTURED_SYSLOG_MESSAGE_PROCESS_AND_SUMMARIZE))

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
            self.vnc_lib().structured_syslog_message_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().structured_syslog_message_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('structured_syslog_message %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().structured_syslog_message_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::StructuredSyslogMessage': ContrailStructuredSyslogMessage,
    }
