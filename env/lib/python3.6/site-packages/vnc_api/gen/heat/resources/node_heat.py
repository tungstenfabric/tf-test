
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


class ContrailNode(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ESXI_INFO, ESXI_INFO_USERNAME, ESXI_INFO_DATACENTER, ESXI_INFO_ESXI_NAME, ESXI_INFO_CLUSTER, ESXI_INFO_MAC, ESXI_INFO_DATASTORE, ESXI_INFO_PASSWORD, ESXI_INFO_VCENTER_SERVER, CLOUD_INFO, CLOUD_INFO_OS_VERSION, CLOUD_INFO_OPERATING_SYSTEM, CLOUD_INFO_ROLES, CLOUD_INFO_AVAILABILITY_ZONE, CLOUD_INFO_INSTANCE_TYPE, CLOUD_INFO_MACHINE_ID, CLOUD_INFO_VOLUME_SIZE, HOSTNAME, BMS_INFO, BMS_INFO_NETWORK_INTERFACE, BMS_INFO_DRIVER, BMS_INFO_PROPERTIES, BMS_INFO_PROPERTIES_MEMORY_MB, BMS_INFO_PROPERTIES_CPU_ARCH, BMS_INFO_PROPERTIES_LOCAL_GB, BMS_INFO_PROPERTIES_CPUS, BMS_INFO_PROPERTIES_CAPABILITIES, BMS_INFO_DRIVER_INFO, BMS_INFO_DRIVER_INFO_IPMI_ADDRESS, BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK, BMS_INFO_DRIVER_INFO_IPMI_PASSWORD, BMS_INFO_DRIVER_INFO_IPMI_PORT, BMS_INFO_DRIVER_INFO_IPMI_USERNAME, BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL, BMS_INFO_NAME, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, NODE_TYPE, ID_PERMS, ID_PERMS_PERMISSIONS, ID_PERMS_PERMISSIONS_OWNER, ID_PERMS_PERMISSIONS_OWNER_ACCESS, ID_PERMS_PERMISSIONS_GROUP, ID_PERMS_PERMISSIONS_GROUP_ACCESS, ID_PERMS_PERMISSIONS_OTHER_ACCESS, ID_PERMS_UUID, ID_PERMS_UUID_UUID_MSLONG, ID_PERMS_UUID_UUID_LSLONG, ID_PERMS_ENABLE, ID_PERMS_CREATED, ID_PERMS_LAST_MODIFIED, ID_PERMS_DESCRIPTION, ID_PERMS_USER_VISIBLE, ID_PERMS_CREATOR, MAC_ADDRESS, DISK_PARTITION, INTERFACE_NAME, IP_ADDRESS, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, TAG_REFS, NODE_PROFILE_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'esxi_info', 'esxi_info_username', 'esxi_info_datacenter', 'esxi_info_esxi_name', 'esxi_info_cluster', 'esxi_info_mac', 'esxi_info_datastore', 'esxi_info_password', 'esxi_info_vcenter_server', 'cloud_info', 'cloud_info_os_version', 'cloud_info_operating_system', 'cloud_info_roles', 'cloud_info_availability_zone', 'cloud_info_instance_type', 'cloud_info_machine_id', 'cloud_info_volume_size', 'hostname', 'bms_info', 'bms_info_network_interface', 'bms_info_driver', 'bms_info_properties', 'bms_info_properties_memory_mb', 'bms_info_properties_cpu_arch', 'bms_info_properties_local_gb', 'bms_info_properties_cpus', 'bms_info_properties_capabilities', 'bms_info_driver_info', 'bms_info_driver_info_ipmi_address', 'bms_info_driver_info_deploy_ramdisk', 'bms_info_driver_info_ipmi_password', 'bms_info_driver_info_ipmi_port', 'bms_info_driver_info_ipmi_username', 'bms_info_driver_info_deploy_kernel', 'bms_info_name', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'node_type', 'id_perms', 'id_perms_permissions', 'id_perms_permissions_owner', 'id_perms_permissions_owner_access', 'id_perms_permissions_group', 'id_perms_permissions_group_access', 'id_perms_permissions_other_access', 'id_perms_uuid', 'id_perms_uuid_uuid_mslong', 'id_perms_uuid_uuid_lslong', 'id_perms_enable', 'id_perms_created', 'id_perms_last_modified', 'id_perms_description', 'id_perms_user_visible', 'id_perms_creator', 'mac_address', 'disk_partition', 'interface_name', 'ip_address', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'tag_refs', 'node_profile_refs', 'global_system_config'
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
        ESXI_INFO: properties.Schema(
            properties.Schema.MAP,
            _('ESXI_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                ESXI_INFO_USERNAME: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_USERNAME.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_DATACENTER: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_DATACENTER.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_ESXI_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_ESXI_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_CLUSTER: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_CLUSTER.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_MAC: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_MAC.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_DATASTORE: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_DATASTORE.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
                ESXI_INFO_VCENTER_SERVER: properties.Schema(
                    properties.Schema.STRING,
                    _('ESXI_INFO_VCENTER_SERVER.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        CLOUD_INFO: properties.Schema(
            properties.Schema.MAP,
            _('CLOUD_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                CLOUD_INFO_OS_VERSION: properties.Schema(
                    properties.Schema.STRING,
                    _('CLOUD_INFO_OS_VERSION.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_OPERATING_SYSTEM: properties.Schema(
                    properties.Schema.STRING,
                    _('CLOUD_INFO_OPERATING_SYSTEM.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_ROLES: properties.Schema(
                    properties.Schema.LIST,
                    _('CLOUD_INFO_ROLES.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_AVAILABILITY_ZONE: properties.Schema(
                    properties.Schema.STRING,
                    _('CLOUD_INFO_AVAILABILITY_ZONE.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_INSTANCE_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('CLOUD_INFO_INSTANCE_TYPE.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_MACHINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('CLOUD_INFO_MACHINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                CLOUD_INFO_VOLUME_SIZE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('CLOUD_INFO_VOLUME_SIZE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        HOSTNAME: properties.Schema(
            properties.Schema.STRING,
            _('HOSTNAME.'),
            update_allowed=True,
            required=False,
        ),
        BMS_INFO: properties.Schema(
            properties.Schema.MAP,
            _('BMS_INFO.'),
            update_allowed=True,
            required=False,
            schema={
                BMS_INFO_NETWORK_INTERFACE: properties.Schema(
                    properties.Schema.STRING,
                    _('BMS_INFO_NETWORK_INTERFACE.'),
                    update_allowed=True,
                    required=False,
                ),
                BMS_INFO_DRIVER: properties.Schema(
                    properties.Schema.STRING,
                    _('BMS_INFO_DRIVER.'),
                    update_allowed=True,
                    required=False,
                ),
                BMS_INFO_PROPERTIES: properties.Schema(
                    properties.Schema.MAP,
                    _('BMS_INFO_PROPERTIES.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BMS_INFO_PROPERTIES_MEMORY_MB: properties.Schema(
                            properties.Schema.INTEGER,
                            _('BMS_INFO_PROPERTIES_MEMORY_MB.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_PROPERTIES_CPU_ARCH: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_PROPERTIES_CPU_ARCH.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_PROPERTIES_LOCAL_GB: properties.Schema(
                            properties.Schema.INTEGER,
                            _('BMS_INFO_PROPERTIES_LOCAL_GB.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_PROPERTIES_CPUS: properties.Schema(
                            properties.Schema.INTEGER,
                            _('BMS_INFO_PROPERTIES_CPUS.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_PROPERTIES_CAPABILITIES: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_PROPERTIES_CAPABILITIES.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                BMS_INFO_DRIVER_INFO: properties.Schema(
                    properties.Schema.MAP,
                    _('BMS_INFO_DRIVER_INFO.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BMS_INFO_DRIVER_INFO_IPMI_ADDRESS: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_IPMI_ADDRESS.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_DRIVER_INFO_IPMI_PASSWORD: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_IPMI_PASSWORD.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_DRIVER_INFO_IPMI_PORT: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_IPMI_PORT.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_DRIVER_INFO_IPMI_USERNAME: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_IPMI_USERNAME.'),
                            update_allowed=True,
                            required=False,
                        ),
                        BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL: properties.Schema(
                            properties.Schema.STRING,
                            _('BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                BMS_INFO_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('BMS_INFO_NAME.'),
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
        NODE_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('NODE_TYPE.'),
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
        MAC_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('MAC_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        DISK_PARTITION: properties.Schema(
            properties.Schema.STRING,
            _('DISK_PARTITION.'),
            update_allowed=True,
            required=False,
        ),
        INTERFACE_NAME: properties.Schema(
            properties.Schema.STRING,
            _('INTERFACE_NAME.'),
            update_allowed=True,
            required=False,
        ),
        IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('IP_ADDRESS.'),
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
        ESXI_INFO: attributes.Schema(
            _('ESXI_INFO.'),
        ),
        CLOUD_INFO: attributes.Schema(
            _('CLOUD_INFO.'),
        ),
        HOSTNAME: attributes.Schema(
            _('HOSTNAME.'),
        ),
        BMS_INFO: attributes.Schema(
            _('BMS_INFO.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        NODE_TYPE: attributes.Schema(
            _('NODE_TYPE.'),
        ),
        ID_PERMS: attributes.Schema(
            _('ID_PERMS.'),
        ),
        MAC_ADDRESS: attributes.Schema(
            _('MAC_ADDRESS.'),
        ),
        DISK_PARTITION: attributes.Schema(
            _('DISK_PARTITION.'),
        ),
        INTERFACE_NAME: attributes.Schema(
            _('INTERFACE_NAME.'),
        ),
        IP_ADDRESS: attributes.Schema(
            _('IP_ADDRESS.'),
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

        obj_0 = vnc_api.Node(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ESXI_INFO) is not None:
            obj_1 = vnc_api.ESXIHostInfo()
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_USERNAME) is not None:
                obj_1.set_username(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_USERNAME))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATACENTER) is not None:
                obj_1.set_datacenter(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATACENTER))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_ESXI_NAME) is not None:
                obj_1.set_esxi_name(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_ESXI_NAME))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_CLUSTER) is not None:
                obj_1.set_cluster(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_CLUSTER))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_MAC) is not None:
                obj_1.set_mac(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_MAC))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATASTORE) is not None:
                obj_1.set_datastore(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATASTORE))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_PASSWORD) is not None:
                obj_1.set_password(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_PASSWORD))
            if self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_VCENTER_SERVER) is not None:
                obj_1.set_vcenter_server(self.properties.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_VCENTER_SERVER))
            obj_0.set_esxi_info(obj_1)
        if self.properties.get(self.CLOUD_INFO) is not None:
            obj_1 = vnc_api.CloudInstanceInfo()
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OS_VERSION) is not None:
                obj_1.set_os_version(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OS_VERSION))
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OPERATING_SYSTEM) is not None:
                obj_1.set_operating_system(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OPERATING_SYSTEM))
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES) is not None:
                for index_1 in range(len(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES))):
                    obj_1.add_roles(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES)[index_1])
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_AVAILABILITY_ZONE) is not None:
                obj_1.set_availability_zone(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_AVAILABILITY_ZONE))
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_INSTANCE_TYPE) is not None:
                obj_1.set_instance_type(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_INSTANCE_TYPE))
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_MACHINE_ID) is not None:
                obj_1.set_machine_id(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_MACHINE_ID))
            if self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_VOLUME_SIZE) is not None:
                obj_1.set_volume_size(self.properties.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_VOLUME_SIZE))
            obj_0.set_cloud_info(obj_1)
        if self.properties.get(self.HOSTNAME) is not None:
            obj_0.set_hostname(self.properties.get(self.HOSTNAME))
        if self.properties.get(self.BMS_INFO) is not None:
            obj_1 = vnc_api.BaremetalServerInfo()
            if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_NETWORK_INTERFACE) is not None:
                obj_1.set_network_interface(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_NETWORK_INTERFACE))
            if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER) is not None:
                obj_1.set_driver(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER))
            if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES) is not None:
                obj_2 = vnc_api.BaremetalProperties()
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_MEMORY_MB) is not None:
                    obj_2.set_memory_mb(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_MEMORY_MB))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPU_ARCH) is not None:
                    obj_2.set_cpu_arch(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPU_ARCH))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_LOCAL_GB) is not None:
                    obj_2.set_local_gb(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_LOCAL_GB))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPUS) is not None:
                    obj_2.set_cpus(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPUS))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CAPABILITIES) is not None:
                    obj_2.set_capabilities(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CAPABILITIES))
                obj_1.set_properties(obj_2)
            if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO) is not None:
                obj_2 = vnc_api.DriverInfo()
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_ADDRESS) is not None:
                    obj_2.set_ipmi_address(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_ADDRESS))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK) is not None:
                    obj_2.set_deploy_ramdisk(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PASSWORD) is not None:
                    obj_2.set_ipmi_password(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PASSWORD))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PORT) is not None:
                    obj_2.set_ipmi_port(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PORT))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_USERNAME) is not None:
                    obj_2.set_ipmi_username(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_USERNAME))
                if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL) is not None:
                    obj_2.set_deploy_kernel(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL))
                obj_1.set_driver_info(obj_2)
            if self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_NAME) is not None:
                obj_1.set_name(self.properties.get(self.BMS_INFO, {}).get(self.BMS_INFO_NAME))
            obj_0.set_bms_info(obj_1)
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
        if self.properties.get(self.NODE_TYPE) is not None:
            obj_0.set_node_type(self.properties.get(self.NODE_TYPE))
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
        if self.properties.get(self.MAC_ADDRESS) is not None:
            obj_0.set_mac_address(self.properties.get(self.MAC_ADDRESS))
        if self.properties.get(self.DISK_PARTITION) is not None:
            obj_0.set_disk_partition(self.properties.get(self.DISK_PARTITION))
        if self.properties.get(self.INTERFACE_NAME) is not None:
            obj_0.set_interface_name(self.properties.get(self.INTERFACE_NAME))
        if self.properties.get(self.IP_ADDRESS) is not None:
            obj_0.set_ip_address(self.properties.get(self.IP_ADDRESS))
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
        if self.properties.get(self.NODE_PROFILE_REFS):
            for index_0 in range(len(self.properties.get(self.NODE_PROFILE_REFS))):
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
                obj_0.add_node_profile(ref_obj)

        try:
            obj_uuid = super(ContrailNode, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().node_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ESXI_INFO) is not None:
            obj_1 = vnc_api.ESXIHostInfo()
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_USERNAME) is not None:
                obj_1.set_username(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_USERNAME))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATACENTER) is not None:
                obj_1.set_datacenter(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATACENTER))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_ESXI_NAME) is not None:
                obj_1.set_esxi_name(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_ESXI_NAME))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_CLUSTER) is not None:
                obj_1.set_cluster(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_CLUSTER))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_MAC) is not None:
                obj_1.set_mac(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_MAC))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATASTORE) is not None:
                obj_1.set_datastore(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_DATASTORE))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_PASSWORD) is not None:
                obj_1.set_password(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_PASSWORD))
            if prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_VCENTER_SERVER) is not None:
                obj_1.set_vcenter_server(prop_diff.get(self.ESXI_INFO, {}).get(self.ESXI_INFO_VCENTER_SERVER))
            obj_0.set_esxi_info(obj_1)
        if prop_diff.get(self.CLOUD_INFO) is not None:
            obj_1 = vnc_api.CloudInstanceInfo()
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OS_VERSION) is not None:
                obj_1.set_os_version(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OS_VERSION))
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OPERATING_SYSTEM) is not None:
                obj_1.set_operating_system(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_OPERATING_SYSTEM))
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES) is not None:
                for index_1 in range(len(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES))):
                    obj_1.add_roles(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_ROLES)[index_1])
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_AVAILABILITY_ZONE) is not None:
                obj_1.set_availability_zone(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_AVAILABILITY_ZONE))
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_INSTANCE_TYPE) is not None:
                obj_1.set_instance_type(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_INSTANCE_TYPE))
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_MACHINE_ID) is not None:
                obj_1.set_machine_id(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_MACHINE_ID))
            if prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_VOLUME_SIZE) is not None:
                obj_1.set_volume_size(prop_diff.get(self.CLOUD_INFO, {}).get(self.CLOUD_INFO_VOLUME_SIZE))
            obj_0.set_cloud_info(obj_1)
        if prop_diff.get(self.HOSTNAME) is not None:
            obj_0.set_hostname(prop_diff.get(self.HOSTNAME))
        if prop_diff.get(self.BMS_INFO) is not None:
            obj_1 = vnc_api.BaremetalServerInfo()
            if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_NETWORK_INTERFACE) is not None:
                obj_1.set_network_interface(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_NETWORK_INTERFACE))
            if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER) is not None:
                obj_1.set_driver(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER))
            if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES) is not None:
                obj_2 = vnc_api.BaremetalProperties()
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_MEMORY_MB) is not None:
                    obj_2.set_memory_mb(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_MEMORY_MB))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPU_ARCH) is not None:
                    obj_2.set_cpu_arch(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPU_ARCH))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_LOCAL_GB) is not None:
                    obj_2.set_local_gb(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_LOCAL_GB))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPUS) is not None:
                    obj_2.set_cpus(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CPUS))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CAPABILITIES) is not None:
                    obj_2.set_capabilities(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_PROPERTIES, {}).get(self.BMS_INFO_PROPERTIES_CAPABILITIES))
                obj_1.set_properties(obj_2)
            if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO) is not None:
                obj_2 = vnc_api.DriverInfo()
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_ADDRESS) is not None:
                    obj_2.set_ipmi_address(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_ADDRESS))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK) is not None:
                    obj_2.set_deploy_ramdisk(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_RAMDISK))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PASSWORD) is not None:
                    obj_2.set_ipmi_password(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PASSWORD))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PORT) is not None:
                    obj_2.set_ipmi_port(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_PORT))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_USERNAME) is not None:
                    obj_2.set_ipmi_username(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_IPMI_USERNAME))
                if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL) is not None:
                    obj_2.set_deploy_kernel(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_DRIVER_INFO, {}).get(self.BMS_INFO_DRIVER_INFO_DEPLOY_KERNEL))
                obj_1.set_driver_info(obj_2)
            if prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_NAME) is not None:
                obj_1.set_name(prop_diff.get(self.BMS_INFO, {}).get(self.BMS_INFO_NAME))
            obj_0.set_bms_info(obj_1)
        if prop_diff.get(self.NODE_TYPE) is not None:
            obj_0.set_node_type(prop_diff.get(self.NODE_TYPE))
        if prop_diff.get(self.MAC_ADDRESS) is not None:
            obj_0.set_mac_address(prop_diff.get(self.MAC_ADDRESS))
        if prop_diff.get(self.DISK_PARTITION) is not None:
            obj_0.set_disk_partition(prop_diff.get(self.DISK_PARTITION))
        if prop_diff.get(self.INTERFACE_NAME) is not None:
            obj_0.set_interface_name(prop_diff.get(self.INTERFACE_NAME))
        if prop_diff.get(self.IP_ADDRESS) is not None:
            obj_0.set_ip_address(prop_diff.get(self.IP_ADDRESS))
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

        # reference to node_profile_refs
        ref_obj_list = []
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
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_node_profile_list(ref_obj_list)
            # End: reference to node_profile_refs

        try:
            self.vnc_lib().node_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().node_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('node %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().node_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Node': ContrailNode,
    }
