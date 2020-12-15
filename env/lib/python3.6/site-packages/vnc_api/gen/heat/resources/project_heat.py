
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


class ContrailProject(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ENABLE_SECURITY_POLICY_DRAFT, DISPLAY_NAME, QUOTA, QUOTA_DEFAULTS, QUOTA_FLOATING_IP, QUOTA_INSTANCE_IP, QUOTA_VIRTUAL_MACHINE_INTERFACE, QUOTA_VIRTUAL_NETWORK, QUOTA_VIRTUAL_ROUTER, QUOTA_VIRTUAL_DNS, QUOTA_VIRTUAL_DNS_RECORD, QUOTA_BGP_ROUTER, QUOTA_NETWORK_IPAM, QUOTA_ACCESS_CONTROL_LIST, QUOTA_NETWORK_POLICY, QUOTA_FLOATING_IP_POOL, QUOTA_SERVICE_TEMPLATE, QUOTA_SERVICE_INSTANCE, QUOTA_LOGICAL_ROUTER, QUOTA_SECURITY_GROUP, QUOTA_SECURITY_GROUP_RULE, QUOTA_SUBNET, QUOTA_GLOBAL_VROUTER_CONFIG, QUOTA_LOADBALANCER_POOL, QUOTA_LOADBALANCER_MEMBER, QUOTA_LOADBALANCER_HEALTHMONITOR, QUOTA_VIRTUAL_IP, QUOTA_SECURITY_LOGGING_OBJECT, QUOTA_ROUTE_TABLE, QUOTA_FIREWALL_GROUP, QUOTA_FIREWALL_POLICY, QUOTA_FIREWALL_RULE, QUOTA_HOST_BASED_SERVICE, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, VXLAN_ROUTING, ALARM_ENABLE, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, NAMESPACE_REFS, NAMESPACE_REFS_DATA, NAMESPACE_REFS_DATA_IP_PREFIX, NAMESPACE_REFS_DATA_IP_PREFIX_LEN, FLOATING_IP_POOL_REFS, APPLICATION_POLICY_SET_REFS, ALIAS_IP_POOL_REFS, TAG_REFS, DOMAIN
    ) = (
        'name', 'fq_name', 'enable_security_policy_draft', 'display_name', 'quota', 'quota_defaults', 'quota_floating_ip', 'quota_instance_ip', 'quota_virtual_machine_interface', 'quota_virtual_network', 'quota_virtual_router', 'quota_virtual_DNS', 'quota_virtual_DNS_record', 'quota_bgp_router', 'quota_network_ipam', 'quota_access_control_list', 'quota_network_policy', 'quota_floating_ip_pool', 'quota_service_template', 'quota_service_instance', 'quota_logical_router', 'quota_security_group', 'quota_security_group_rule', 'quota_subnet', 'quota_global_vrouter_config', 'quota_loadbalancer_pool', 'quota_loadbalancer_member', 'quota_loadbalancer_healthmonitor', 'quota_virtual_ip', 'quota_security_logging_object', 'quota_route_table', 'quota_firewall_group', 'quota_firewall_policy', 'quota_firewall_rule', 'quota_host_based_service', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'vxlan_routing', 'alarm_enable', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'namespace_refs', 'namespace_refs_data', 'namespace_refs_data_ip_prefix', 'namespace_refs_data_ip_prefix_len', 'floating_ip_pool_refs', 'application_policy_set_refs', 'alias_ip_pool_refs', 'tag_refs', 'domain'
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
        ENABLE_SECURITY_POLICY_DRAFT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ENABLE_SECURITY_POLICY_DRAFT.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        QUOTA: properties.Schema(
            properties.Schema.MAP,
            _('QUOTA.'),
            update_allowed=True,
            required=False,
            schema={
                QUOTA_DEFAULTS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_DEFAULTS.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FLOATING_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FLOATING_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_INSTANCE_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_INSTANCE_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_MACHINE_INTERFACE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_MACHINE_INTERFACE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_DNS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_DNS.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_DNS_RECORD: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_DNS_RECORD.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_BGP_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_BGP_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_NETWORK_IPAM: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_NETWORK_IPAM.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_ACCESS_CONTROL_LIST: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_ACCESS_CONTROL_LIST.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_NETWORK_POLICY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_NETWORK_POLICY.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FLOATING_IP_POOL: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FLOATING_IP_POOL.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SERVICE_TEMPLATE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SERVICE_TEMPLATE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOGICAL_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOGICAL_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SECURITY_GROUP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SECURITY_GROUP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SECURITY_GROUP_RULE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SECURITY_GROUP_RULE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SUBNET: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SUBNET.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_GLOBAL_VROUTER_CONFIG: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_GLOBAL_VROUTER_CONFIG.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_POOL: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_POOL.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_MEMBER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_MEMBER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_HEALTHMONITOR: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_HEALTHMONITOR.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SECURITY_LOGGING_OBJECT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SECURITY_LOGGING_OBJECT.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_ROUTE_TABLE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_ROUTE_TABLE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FIREWALL_GROUP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FIREWALL_GROUP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FIREWALL_POLICY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FIREWALL_POLICY.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FIREWALL_RULE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FIREWALL_RULE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_HOST_BASED_SERVICE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_HOST_BASED_SERVICE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 1),
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
        VXLAN_ROUTING: properties.Schema(
            properties.Schema.BOOLEAN,
            _('VXLAN_ROUTING.'),
            update_allowed=True,
            required=False,
        ),
        ALARM_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ALARM_ENABLE.'),
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
        NAMESPACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NAMESPACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NAMESPACE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NAMESPACE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NAMESPACE_REFS_DATA_IP_PREFIX: properties.Schema(
                        properties.Schema.STRING,
                        _('NAMESPACE_REFS_DATA_IP_PREFIX.'),
                        update_allowed=True,
                        required=False,
                    ),
                    NAMESPACE_REFS_DATA_IP_PREFIX_LEN: properties.Schema(
                        properties.Schema.INTEGER,
                        _('NAMESPACE_REFS_DATA_IP_PREFIX_LEN.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        FLOATING_IP_POOL_REFS: properties.Schema(
            properties.Schema.LIST,
            _('FLOATING_IP_POOL_REFS.'),
            update_allowed=True,
            required=False,
        ),
        APPLICATION_POLICY_SET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('APPLICATION_POLICY_SET_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ALIAS_IP_POOL_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ALIAS_IP_POOL_REFS.'),
            update_allowed=True,
            required=False,
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('DOMAIN.'),
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
        ENABLE_SECURITY_POLICY_DRAFT: attributes.Schema(
            _('ENABLE_SECURITY_POLICY_DRAFT.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        QUOTA: attributes.Schema(
            _('QUOTA.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        VXLAN_ROUTING: attributes.Schema(
            _('VXLAN_ROUTING.'),
        ),
        ALARM_ENABLE: attributes.Schema(
            _('ALARM_ENABLE.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        NAMESPACE_REFS: attributes.Schema(
            _('NAMESPACE_REFS.'),
        ),
        NAMESPACE_REFS_DATA: attributes.Schema(
            _('NAMESPACE_REFS_DATA.'),
        ),
        FLOATING_IP_POOL_REFS: attributes.Schema(
            _('FLOATING_IP_POOL_REFS.'),
        ),
        APPLICATION_POLICY_SET_REFS: attributes.Schema(
            _('APPLICATION_POLICY_SET_REFS.'),
        ),
        ALIAS_IP_POOL_REFS: attributes.Schema(
            _('ALIAS_IP_POOL_REFS.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        DOMAIN: attributes.Schema(
            _('DOMAIN.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.DOMAIN) and self.properties.get(self.DOMAIN) != 'config-root':
            try:
                parent_obj = self.vnc_lib().domain_read(fq_name_str=self.properties.get(self.DOMAIN))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().domain_read(id=str(uuid.UUID(self.properties.get(self.DOMAIN))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.DOMAIN) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.Project(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.ENABLE_SECURITY_POLICY_DRAFT) is not None:
            obj_0.set_enable_security_policy_draft(self.properties.get(self.ENABLE_SECURITY_POLICY_DRAFT))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.QUOTA) is not None:
            obj_1 = vnc_api.QuotaType()
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS) is not None:
                obj_1.set_defaults(self.properties.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP) is not None:
                obj_1.set_floating_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP) is not None:
                obj_1.set_instance_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE) is not None:
                obj_1.set_virtual_machine_interface(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER) is not None:
                obj_1.set_virtual_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS) is not None:
                obj_1.set_virtual_DNS(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD) is not None:
                obj_1.set_virtual_DNS_record(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM) is not None:
                obj_1.set_network_ipam(self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST) is not None:
                obj_1.set_access_control_list(self.properties.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY) is not None:
                obj_1.set_network_policy(self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL) is not None:
                obj_1.set_floating_ip_pool(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE) is not None:
                obj_1.set_service_template(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER) is not None:
                obj_1.set_logical_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP) is not None:
                obj_1.set_security_group(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE) is not None:
                obj_1.set_security_group_rule(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SUBNET) is not None:
                obj_1.set_subnet(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SUBNET))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG) is not None:
                obj_1.set_global_vrouter_config(self.properties.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL) is not None:
                obj_1.set_loadbalancer_pool(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER) is not None:
                obj_1.set_loadbalancer_member(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR) is not None:
                obj_1.set_loadbalancer_healthmonitor(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP) is not None:
                obj_1.set_virtual_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_LOGGING_OBJECT) is not None:
                obj_1.set_security_logging_object(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_LOGGING_OBJECT))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_ROUTE_TABLE) is not None:
                obj_1.set_route_table(self.properties.get(self.QUOTA, {}).get(self.QUOTA_ROUTE_TABLE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_GROUP) is not None:
                obj_1.set_firewall_group(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_GROUP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_POLICY) is not None:
                obj_1.set_firewall_policy(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_POLICY))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_RULE) is not None:
                obj_1.set_firewall_rule(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_RULE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_HOST_BASED_SERVICE) is not None:
                obj_1.set_host_based_service(self.properties.get(self.QUOTA, {}).get(self.QUOTA_HOST_BASED_SERVICE))
            obj_0.set_quota(obj_1)
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
        if self.properties.get(self.VXLAN_ROUTING) is not None:
            obj_0.set_vxlan_routing(self.properties.get(self.VXLAN_ROUTING))
        if self.properties.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(self.properties.get(self.ALARM_ENABLE))
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

        # reference to namespace_refs
        if len(self.properties.get(self.NAMESPACE_REFS) or []) != len(self.properties.get(self.NAMESPACE_REFS_DATA) or []):
            raise Exception(_('project: specify namespace_refs for each namespace_refs_data.'))
        obj_1 = None
        if self.properties.get(self.NAMESPACE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NAMESPACE_REFS_DATA))):
                obj_1 = vnc_api.SubnetType()
                if self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX) is not None:
                    obj_1.set_ip_prefix(self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX))
                if self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN) is not None:
                    obj_1.set_ip_prefix_len(self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN))

                if self.properties.get(self.NAMESPACE_REFS):
                    try:
                        ref_obj = self.vnc_lib().namespace_read(
                            id=self.properties.get(self.NAMESPACE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().namespace_read(
                            fq_name_str=self.properties.get(self.NAMESPACE_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_namespace(ref_obj, obj_1)

        # reference to floating_ip_pool_refs
        if self.properties.get(self.FLOATING_IP_POOL_REFS):
            for index_0 in range(len(self.properties.get(self.FLOATING_IP_POOL_REFS))):
                try:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        id=self.properties.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        fq_name_str=self.properties.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_floating_ip_pool(ref_obj)

        # reference to application_policy_set_refs
        if self.properties.get(self.APPLICATION_POLICY_SET_REFS):
            for index_0 in range(len(self.properties.get(self.APPLICATION_POLICY_SET_REFS))):
                try:
                    ref_obj = self.vnc_lib().application_policy_set_read(
                        id=self.properties.get(self.APPLICATION_POLICY_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().application_policy_set_read(
                        fq_name_str=self.properties.get(self.APPLICATION_POLICY_SET_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_application_policy_set(ref_obj)

        # reference to alias_ip_pool_refs
        if self.properties.get(self.ALIAS_IP_POOL_REFS):
            for index_0 in range(len(self.properties.get(self.ALIAS_IP_POOL_REFS))):
                try:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        id=self.properties.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        fq_name_str=self.properties.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_alias_ip_pool(ref_obj)

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
            obj_uuid = super(ContrailProject, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().project_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.ENABLE_SECURITY_POLICY_DRAFT) is not None:
            obj_0.set_enable_security_policy_draft(prop_diff.get(self.ENABLE_SECURITY_POLICY_DRAFT))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.QUOTA) is not None:
            obj_1 = vnc_api.QuotaType()
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS) is not None:
                obj_1.set_defaults(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP) is not None:
                obj_1.set_floating_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP) is not None:
                obj_1.set_instance_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE) is not None:
                obj_1.set_virtual_machine_interface(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER) is not None:
                obj_1.set_virtual_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS) is not None:
                obj_1.set_virtual_DNS(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD) is not None:
                obj_1.set_virtual_DNS_record(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM) is not None:
                obj_1.set_network_ipam(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST) is not None:
                obj_1.set_access_control_list(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY) is not None:
                obj_1.set_network_policy(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL) is not None:
                obj_1.set_floating_ip_pool(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE) is not None:
                obj_1.set_service_template(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER) is not None:
                obj_1.set_logical_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP) is not None:
                obj_1.set_security_group(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE) is not None:
                obj_1.set_security_group_rule(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SUBNET) is not None:
                obj_1.set_subnet(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SUBNET))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG) is not None:
                obj_1.set_global_vrouter_config(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL) is not None:
                obj_1.set_loadbalancer_pool(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER) is not None:
                obj_1.set_loadbalancer_member(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR) is not None:
                obj_1.set_loadbalancer_healthmonitor(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP) is not None:
                obj_1.set_virtual_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_LOGGING_OBJECT) is not None:
                obj_1.set_security_logging_object(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_LOGGING_OBJECT))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ROUTE_TABLE) is not None:
                obj_1.set_route_table(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ROUTE_TABLE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_GROUP) is not None:
                obj_1.set_firewall_group(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_GROUP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_POLICY) is not None:
                obj_1.set_firewall_policy(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_POLICY))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_RULE) is not None:
                obj_1.set_firewall_rule(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FIREWALL_RULE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_HOST_BASED_SERVICE) is not None:
                obj_1.set_host_based_service(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_HOST_BASED_SERVICE))
            obj_0.set_quota(obj_1)
        if prop_diff.get(self.VXLAN_ROUTING) is not None:
            obj_0.set_vxlan_routing(prop_diff.get(self.VXLAN_ROUTING))
        if prop_diff.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(prop_diff.get(self.ALARM_ENABLE))
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

        # reference to namespace
        update = 0
        if not self.NAMESPACE_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_namespace_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.NAMESPACE_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_namespace_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.NAMESPACE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NAMESPACE_REFS_DATA))):
                obj_1 = vnc_api.SubnetType()
                if prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX) is not None:
                    obj_1.set_ip_prefix(prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX))
                if prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN) is not None:
                    obj_1.set_ip_prefix_len(prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN))
                ref_data_list.append(obj_1)
        if self.NAMESPACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NAMESPACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().namespace_read(
                        id=prop_diff.get(self.NAMESPACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().namespace_read(
                        fq_name_str=prop_diff.get(self.NAMESPACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('project: specify namespace_refs_data for each namespace_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_namespace_list(ref_obj_list, ref_data_list)
        # End: reference to namespace_refs

        # reference to floating_ip_pool_refs
        ref_obj_list = []
        if self.FLOATING_IP_POOL_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.FLOATING_IP_POOL_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        id=prop_diff.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        fq_name_str=prop_diff.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_floating_ip_pool_list(ref_obj_list)
            # End: reference to floating_ip_pool_refs

        # reference to application_policy_set_refs
        ref_obj_list = []
        if self.APPLICATION_POLICY_SET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.APPLICATION_POLICY_SET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().application_policy_set_read(
                        id=prop_diff.get(self.APPLICATION_POLICY_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().application_policy_set_read(
                        fq_name_str=prop_diff.get(self.APPLICATION_POLICY_SET_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_application_policy_set_list(ref_obj_list)
            # End: reference to application_policy_set_refs

        # reference to alias_ip_pool_refs
        ref_obj_list = []
        if self.ALIAS_IP_POOL_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ALIAS_IP_POOL_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        id=prop_diff.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        fq_name_str=prop_diff.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_alias_ip_pool_list(ref_obj_list)
            # End: reference to alias_ip_pool_refs

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
            self.vnc_lib().project_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().project_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('project %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().project_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Project': ContrailProject,
    }
