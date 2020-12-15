
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from builtins import str
from builtins import object
import abc
from future.utils import with_metaclass

class ConnectionDriverBase(with_metaclass(abc.ABCMeta, object)):
    """
    This class provides type specific methods to create,
    read, update, delete and list objects from the server
    """

    @abc.abstractmethod
    def __init__(self):
        pass
    # end __init__
    def service_endpoint_create(self, obj):
        """Create new service-endpoint.
        
        :param obj: :class:`.ServiceEndpoint` object
        
        """
        raise NotImplementedError('service_endpoint_create is %s\'s responsibility' % (str(type (self))))
    # end service_endpoint_create

    def service_endpoint_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-endpoint information.
        
        :param fq_name: Fully qualified name of service-endpoint
        :param fq_name_str: Fully qualified name string of service-endpoint
        :param id: UUID of service-endpoint
        :param ifmap_id: IFMAP id of service-endpoint
        :returns: :class:`.ServiceEndpoint` object
        
        """
        raise NotImplementedError('service_endpoint_read is %s\'s responsibility' % (str(type (self))))
    # end service_endpoint_read

    def service_endpoint_update(self, obj):
        """Update service-endpoint.
        
        :param obj: :class:`.ServiceEndpoint` object
        
        """
        raise NotImplementedError('service_endpoint_update is %s\'s responsibility' % (str(type (self))))
    # end service_endpoint_update

    def service_endpoints_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-endpoints."""
        raise NotImplementedError('service_endpoints_list is %s\'s responsibility' % (str(type (self))))
    # end service_endpoints_list

    def service_endpoint_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-endpoint from the system.
        
        :param fq_name: Fully qualified name of service-endpoint
        :param id: UUID of service-endpoint
        :param ifmap_id: IFMAP id of service-endpoint
        
        """
        raise NotImplementedError('service_endpoint_delete is %s\'s responsibility' % (str(type (self))))
    # end service_endpoint_delete

    def get_default_service_endpoint_id(self):
        """Return UUID of default service-endpoint."""
        raise NotImplementedError('get_default_service_endpoint_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_endpoint_delete

    def instance_ip_create(self, obj):
        """Create new instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError('instance_ip_create is %s\'s responsibility' % (str(type (self))))
    # end instance_ip_create

    def instance_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return instance-ip information.
        
        :param fq_name: Fully qualified name of instance-ip
        :param fq_name_str: Fully qualified name string of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        :returns: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError('instance_ip_read is %s\'s responsibility' % (str(type (self))))
    # end instance_ip_read

    def instance_ip_update(self, obj):
        """Update instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError('instance_ip_update is %s\'s responsibility' % (str(type (self))))
    # end instance_ip_update

    def instance_ips_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all instance-ips."""
        raise NotImplementedError('instance_ips_list is %s\'s responsibility' % (str(type (self))))
    # end instance_ips_list

    def instance_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete instance-ip from the system.
        
        :param fq_name: Fully qualified name of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        
        """
        raise NotImplementedError('instance_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end instance_ip_delete

    def get_default_instance_ip_id(self):
        """Return UUID of default instance-ip."""
        raise NotImplementedError('get_default_instance_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_instance_ip_delete

    def service_appliance_set_create(self, obj):
        """Create new service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError('service_appliance_set_create is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_set_create

    def service_appliance_set_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-appliance-set information.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param fq_name_str: Fully qualified name string of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        :returns: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError('service_appliance_set_read is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_set_read

    def service_appliance_set_update(self, obj):
        """Update service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError('service_appliance_set_update is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_set_update

    def service_appliance_sets_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-appliance-sets.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceApplianceSet` objects
        
        """
        raise NotImplementedError('service_appliance_sets_list is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_sets_list

    def service_appliance_set_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance-set from the system.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        
        """
        raise NotImplementedError('service_appliance_set_delete is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_set_delete

    def get_default_service_appliance_set_id(self):
        """Return UUID of default service-appliance-set."""
        raise NotImplementedError('get_default_service_appliance_set_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_appliance_set_delete

    def route_target_create(self, obj):
        """Create new route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError('route_target_create is %s\'s responsibility' % (str(type (self))))
    # end route_target_create

    def route_target_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return route-target information.
        
        :param fq_name: Fully qualified name of route-target
        :param fq_name_str: Fully qualified name string of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        :returns: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError('route_target_read is %s\'s responsibility' % (str(type (self))))
    # end route_target_read

    def route_target_update(self, obj):
        """Update route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError('route_target_update is %s\'s responsibility' % (str(type (self))))
    # end route_target_update

    def route_targets_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all route-targets."""
        raise NotImplementedError('route_targets_list is %s\'s responsibility' % (str(type (self))))
    # end route_targets_list

    def route_target_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-target from the system.
        
        :param fq_name: Fully qualified name of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        
        """
        raise NotImplementedError('route_target_delete is %s\'s responsibility' % (str(type (self))))
    # end route_target_delete

    def get_default_route_target_id(self):
        """Return UUID of default route-target."""
        raise NotImplementedError('get_default_route_target_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_route_target_delete

    def loadbalancer_listener_create(self, obj):
        """Create new loadbalancer-listener.
        
        :param obj: :class:`.LoadbalancerListener` object
        
        """
        raise NotImplementedError('loadbalancer_listener_create is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_listener_create

    def loadbalancer_listener_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-listener information.
        
        :param fq_name: Fully qualified name of loadbalancer-listener
        :param fq_name_str: Fully qualified name string of loadbalancer-listener
        :param id: UUID of loadbalancer-listener
        :param ifmap_id: IFMAP id of loadbalancer-listener
        :returns: :class:`.LoadbalancerListener` object
        
        """
        raise NotImplementedError('loadbalancer_listener_read is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_listener_read

    def loadbalancer_listener_update(self, obj):
        """Update loadbalancer-listener.
        
        :param obj: :class:`.LoadbalancerListener` object
        
        """
        raise NotImplementedError('loadbalancer_listener_update is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_listener_update

    def loadbalancer_listeners_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-listeners.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerListener` objects
        
        """
        raise NotImplementedError('loadbalancer_listeners_list is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_listeners_list

    def loadbalancer_listener_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-listener from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-listener
        :param id: UUID of loadbalancer-listener
        :param ifmap_id: IFMAP id of loadbalancer-listener
        
        """
        raise NotImplementedError('loadbalancer_listener_delete is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_listener_delete

    def get_default_loadbalancer_listener_id(self):
        """Return UUID of default loadbalancer-listener."""
        raise NotImplementedError('get_default_loadbalancer_listener_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_loadbalancer_listener_delete

    def floating_ip_pool_create(self, obj):
        """Create new floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError('floating_ip_pool_create is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_pool_create

    def floating_ip_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return floating-ip-pool information.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param fq_name_str: Fully qualified name string of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        :returns: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError('floating_ip_pool_read is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_pool_read

    def floating_ip_pool_update(self, obj):
        """Update floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError('floating_ip_pool_update is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_pool_update

    def floating_ip_pools_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all floating-ip-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIpPool` objects
        
        """
        raise NotImplementedError('floating_ip_pools_list is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_pools_list

    def floating_ip_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip-pool from the system.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        
        """
        raise NotImplementedError('floating_ip_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_pool_delete

    def get_default_floating_ip_pool_id(self):
        """Return UUID of default floating-ip-pool."""
        raise NotImplementedError('get_default_floating_ip_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_floating_ip_pool_delete

    def physical_router_create(self, obj):
        """Create new physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError('physical_router_create is %s\'s responsibility' % (str(type (self))))
    # end physical_router_create

    def physical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return physical-router information.
        
        :param fq_name: Fully qualified name of physical-router
        :param fq_name_str: Fully qualified name string of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        :returns: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError('physical_router_read is %s\'s responsibility' % (str(type (self))))
    # end physical_router_read

    def physical_router_update(self, obj):
        """Update physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError('physical_router_update is %s\'s responsibility' % (str(type (self))))
    # end physical_router_update

    def physical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all physical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalRouter` objects
        
        """
        raise NotImplementedError('physical_routers_list is %s\'s responsibility' % (str(type (self))))
    # end physical_routers_list

    def physical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-router from the system.
        
        :param fq_name: Fully qualified name of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        
        """
        raise NotImplementedError('physical_router_delete is %s\'s responsibility' % (str(type (self))))
    # end physical_router_delete

    def get_default_physical_router_id(self):
        """Return UUID of default physical-router."""
        raise NotImplementedError('get_default_physical_router_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_physical_router_delete

    def config_root_create(self, obj):
        """Create new config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError('config_root_create is %s\'s responsibility' % (str(type (self))))
    # end config_root_create

    def config_root_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return config-root information.
        
        :param fq_name: Fully qualified name of config-root
        :param fq_name_str: Fully qualified name string of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        :returns: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError('config_root_read is %s\'s responsibility' % (str(type (self))))
    # end config_root_read

    def config_root_update(self, obj):
        """Update config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError('config_root_update is %s\'s responsibility' % (str(type (self))))
    # end config_root_update

    def config_roots_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all config-roots."""
        raise NotImplementedError('config_roots_list is %s\'s responsibility' % (str(type (self))))
    # end config_roots_list

    def config_root_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-root from the system.
        
        :param fq_name: Fully qualified name of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        
        """
        raise NotImplementedError('config_root_delete is %s\'s responsibility' % (str(type (self))))
    # end config_root_delete

    def get_default_config_root_id(self):
        """Return UUID of default config-root."""
        raise NotImplementedError('get_default_config_root_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_config_root_delete

    def service_template_create(self, obj):
        """Create new service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError('service_template_create is %s\'s responsibility' % (str(type (self))))
    # end service_template_create

    def service_template_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-template information.
        
        :param fq_name: Fully qualified name of service-template
        :param fq_name_str: Fully qualified name string of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        :returns: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError('service_template_read is %s\'s responsibility' % (str(type (self))))
    # end service_template_read

    def service_template_update(self, obj):
        """Update service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError('service_template_update is %s\'s responsibility' % (str(type (self))))
    # end service_template_update

    def service_templates_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-templates.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceTemplate` objects
        
        """
        raise NotImplementedError('service_templates_list is %s\'s responsibility' % (str(type (self))))
    # end service_templates_list

    def service_template_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-template from the system.
        
        :param fq_name: Fully qualified name of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        
        """
        raise NotImplementedError('service_template_delete is %s\'s responsibility' % (str(type (self))))
    # end service_template_delete

    def get_default_service_template_id(self):
        """Return UUID of default service-template."""
        raise NotImplementedError('get_default_service_template_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_template_delete

    def hardware_inventory_create(self, obj):
        """Create new hardware-inventory.
        
        :param obj: :class:`.HardwareInventory` object
        
        """
        raise NotImplementedError('hardware_inventory_create is %s\'s responsibility' % (str(type (self))))
    # end hardware_inventory_create

    def hardware_inventory_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return hardware-inventory information.
        
        :param fq_name: Fully qualified name of hardware-inventory
        :param fq_name_str: Fully qualified name string of hardware-inventory
        :param id: UUID of hardware-inventory
        :param ifmap_id: IFMAP id of hardware-inventory
        :returns: :class:`.HardwareInventory` object
        
        """
        raise NotImplementedError('hardware_inventory_read is %s\'s responsibility' % (str(type (self))))
    # end hardware_inventory_read

    def hardware_inventory_update(self, obj):
        """Update hardware-inventory.
        
        :param obj: :class:`.HardwareInventory` object
        
        """
        raise NotImplementedError('hardware_inventory_update is %s\'s responsibility' % (str(type (self))))
    # end hardware_inventory_update

    def hardware_inventorys_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all hardware-inventorys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.HardwareInventory` objects
        
        """
        raise NotImplementedError('hardware_inventorys_list is %s\'s responsibility' % (str(type (self))))
    # end hardware_inventorys_list

    def hardware_inventory_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete hardware-inventory from the system.
        
        :param fq_name: Fully qualified name of hardware-inventory
        :param id: UUID of hardware-inventory
        :param ifmap_id: IFMAP id of hardware-inventory
        
        """
        raise NotImplementedError('hardware_inventory_delete is %s\'s responsibility' % (str(type (self))))
    # end hardware_inventory_delete

    def get_default_hardware_inventory_id(self):
        """Return UUID of default hardware-inventory."""
        raise NotImplementedError('get_default_hardware_inventory_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_hardware_inventory_delete

    def firewall_policy_create(self, obj):
        """Create new firewall-policy.
        
        :param obj: :class:`.FirewallPolicy` object
        
        """
        raise NotImplementedError('firewall_policy_create is %s\'s responsibility' % (str(type (self))))
    # end firewall_policy_create

    def firewall_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return firewall-policy information.
        
        :param fq_name: Fully qualified name of firewall-policy
        :param fq_name_str: Fully qualified name string of firewall-policy
        :param id: UUID of firewall-policy
        :param ifmap_id: IFMAP id of firewall-policy
        :returns: :class:`.FirewallPolicy` object
        
        """
        raise NotImplementedError('firewall_policy_read is %s\'s responsibility' % (str(type (self))))
    # end firewall_policy_read

    def firewall_policy_update(self, obj):
        """Update firewall-policy.
        
        :param obj: :class:`.FirewallPolicy` object
        
        """
        raise NotImplementedError('firewall_policy_update is %s\'s responsibility' % (str(type (self))))
    # end firewall_policy_update

    def firewall_policys_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all firewall-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FirewallPolicy` objects
        
        """
        raise NotImplementedError('firewall_policys_list is %s\'s responsibility' % (str(type (self))))
    # end firewall_policys_list

    def firewall_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete firewall-policy from the system.
        
        :param fq_name: Fully qualified name of firewall-policy
        :param id: UUID of firewall-policy
        :param ifmap_id: IFMAP id of firewall-policy
        
        """
        raise NotImplementedError('firewall_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end firewall_policy_delete

    def get_default_firewall_policy_id(self):
        """Return UUID of default firewall-policy."""
        raise NotImplementedError('get_default_firewall_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_firewall_policy_delete

    def route_table_create(self, obj):
        """Create new route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        raise NotImplementedError('route_table_create is %s\'s responsibility' % (str(type (self))))
    # end route_table_create

    def route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return route-table information.
        
        :param fq_name: Fully qualified name of route-table
        :param fq_name_str: Fully qualified name string of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        :returns: :class:`.RouteTable` object
        
        """
        raise NotImplementedError('route_table_read is %s\'s responsibility' % (str(type (self))))
    # end route_table_read

    def route_table_update(self, obj):
        """Update route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        raise NotImplementedError('route_table_update is %s\'s responsibility' % (str(type (self))))
    # end route_table_update

    def route_tables_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RouteTable` objects
        
        """
        raise NotImplementedError('route_tables_list is %s\'s responsibility' % (str(type (self))))
    # end route_tables_list

    def route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-table from the system.
        
        :param fq_name: Fully qualified name of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        
        """
        raise NotImplementedError('route_table_delete is %s\'s responsibility' % (str(type (self))))
    # end route_table_delete

    def get_default_route_table_id(self):
        """Return UUID of default route-table."""
        raise NotImplementedError('get_default_route_table_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_route_table_delete

    def provider_attachment_create(self, obj):
        """Create new provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError('provider_attachment_create is %s\'s responsibility' % (str(type (self))))
    # end provider_attachment_create

    def provider_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return provider-attachment information.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param fq_name_str: Fully qualified name string of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        :returns: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError('provider_attachment_read is %s\'s responsibility' % (str(type (self))))
    # end provider_attachment_read

    def provider_attachment_update(self, obj):
        """Update provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError('provider_attachment_update is %s\'s responsibility' % (str(type (self))))
    # end provider_attachment_update

    def provider_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all provider-attachments."""
        raise NotImplementedError('provider_attachments_list is %s\'s responsibility' % (str(type (self))))
    # end provider_attachments_list

    def provider_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete provider-attachment from the system.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        
        """
        raise NotImplementedError('provider_attachment_delete is %s\'s responsibility' % (str(type (self))))
    # end provider_attachment_delete

    def get_default_provider_attachment_id(self):
        """Return UUID of default provider-attachment."""
        raise NotImplementedError('get_default_provider_attachment_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_provider_attachment_delete

    def overlay_role_create(self, obj):
        """Create new overlay-role.
        
        :param obj: :class:`.OverlayRole` object
        
        """
        raise NotImplementedError('overlay_role_create is %s\'s responsibility' % (str(type (self))))
    # end overlay_role_create

    def overlay_role_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return overlay-role information.
        
        :param fq_name: Fully qualified name of overlay-role
        :param fq_name_str: Fully qualified name string of overlay-role
        :param id: UUID of overlay-role
        :param ifmap_id: IFMAP id of overlay-role
        :returns: :class:`.OverlayRole` object
        
        """
        raise NotImplementedError('overlay_role_read is %s\'s responsibility' % (str(type (self))))
    # end overlay_role_read

    def overlay_role_update(self, obj):
        """Update overlay-role.
        
        :param obj: :class:`.OverlayRole` object
        
        """
        raise NotImplementedError('overlay_role_update is %s\'s responsibility' % (str(type (self))))
    # end overlay_role_update

    def overlay_roles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all overlay-roles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.OverlayRole` objects
        
        """
        raise NotImplementedError('overlay_roles_list is %s\'s responsibility' % (str(type (self))))
    # end overlay_roles_list

    def overlay_role_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete overlay-role from the system.
        
        :param fq_name: Fully qualified name of overlay-role
        :param id: UUID of overlay-role
        :param ifmap_id: IFMAP id of overlay-role
        
        """
        raise NotImplementedError('overlay_role_delete is %s\'s responsibility' % (str(type (self))))
    # end overlay_role_delete

    def get_default_overlay_role_id(self):
        """Return UUID of default overlay-role."""
        raise NotImplementedError('get_default_overlay_role_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_overlay_role_delete

    def multicast_policy_create(self, obj):
        """Create new multicast-policy.
        
        :param obj: :class:`.MulticastPolicy` object
        
        """
        raise NotImplementedError('multicast_policy_create is %s\'s responsibility' % (str(type (self))))
    # end multicast_policy_create

    def multicast_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return multicast-policy information.
        
        :param fq_name: Fully qualified name of multicast-policy
        :param fq_name_str: Fully qualified name string of multicast-policy
        :param id: UUID of multicast-policy
        :param ifmap_id: IFMAP id of multicast-policy
        :returns: :class:`.MulticastPolicy` object
        
        """
        raise NotImplementedError('multicast_policy_read is %s\'s responsibility' % (str(type (self))))
    # end multicast_policy_read

    def multicast_policy_update(self, obj):
        """Update multicast-policy.
        
        :param obj: :class:`.MulticastPolicy` object
        
        """
        raise NotImplementedError('multicast_policy_update is %s\'s responsibility' % (str(type (self))))
    # end multicast_policy_update

    def multicast_policys_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all multicast-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.MulticastPolicy` objects
        
        """
        raise NotImplementedError('multicast_policys_list is %s\'s responsibility' % (str(type (self))))
    # end multicast_policys_list

    def multicast_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete multicast-policy from the system.
        
        :param fq_name: Fully qualified name of multicast-policy
        :param id: UUID of multicast-policy
        :param ifmap_id: IFMAP id of multicast-policy
        
        """
        raise NotImplementedError('multicast_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end multicast_policy_delete

    def get_default_multicast_policy_id(self):
        """Return UUID of default multicast-policy."""
        raise NotImplementedError('get_default_multicast_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_multicast_policy_delete

    def network_device_config_create(self, obj):
        """Create new network-device-config.
        
        :param obj: :class:`.NetworkDeviceConfig` object
        
        """
        raise NotImplementedError('network_device_config_create is %s\'s responsibility' % (str(type (self))))
    # end network_device_config_create

    def network_device_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return network-device-config information.
        
        :param fq_name: Fully qualified name of network-device-config
        :param fq_name_str: Fully qualified name string of network-device-config
        :param id: UUID of network-device-config
        :param ifmap_id: IFMAP id of network-device-config
        :returns: :class:`.NetworkDeviceConfig` object
        
        """
        raise NotImplementedError('network_device_config_read is %s\'s responsibility' % (str(type (self))))
    # end network_device_config_read

    def network_device_config_update(self, obj):
        """Update network-device-config.
        
        :param obj: :class:`.NetworkDeviceConfig` object
        
        """
        raise NotImplementedError('network_device_config_update is %s\'s responsibility' % (str(type (self))))
    # end network_device_config_update

    def network_device_configs_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all network-device-configs."""
        raise NotImplementedError('network_device_configs_list is %s\'s responsibility' % (str(type (self))))
    # end network_device_configs_list

    def network_device_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-device-config from the system.
        
        :param fq_name: Fully qualified name of network-device-config
        :param id: UUID of network-device-config
        :param ifmap_id: IFMAP id of network-device-config
        
        """
        raise NotImplementedError('network_device_config_delete is %s\'s responsibility' % (str(type (self))))
    # end network_device_config_delete

    def get_default_network_device_config_id(self):
        """Return UUID of default network-device-config."""
        raise NotImplementedError('get_default_network_device_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_network_device_config_delete

    def virtual_DNS_record_create(self, obj):
        """Create new virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError('virtual_DNS_record_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_record_create

    def virtual_DNS_record_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-DNS-record information.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param fq_name_str: Fully qualified name string of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        :returns: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError('virtual_DNS_record_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_record_read

    def virtual_DNS_record_update(self, obj):
        """Update virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError('virtual_DNS_record_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_record_update

    def virtual_DNS_records_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-DNS-records.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDnsRecord` objects
        
        """
        raise NotImplementedError('virtual_DNS_records_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_records_list

    def virtual_DNS_record_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS-record from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        
        """
        raise NotImplementedError('virtual_DNS_record_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_record_delete

    def get_default_virtual_DNS_record_id(self):
        """Return UUID of default virtual-DNS-record."""
        raise NotImplementedError('get_default_virtual_DNS_record_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_DNS_record_delete

    def control_node_zone_create(self, obj):
        """Create new control-node-zone.
        
        :param obj: :class:`.ControlNodeZone` object
        
        """
        raise NotImplementedError('control_node_zone_create is %s\'s responsibility' % (str(type (self))))
    # end control_node_zone_create

    def control_node_zone_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return control-node-zone information.
        
        :param fq_name: Fully qualified name of control-node-zone
        :param fq_name_str: Fully qualified name string of control-node-zone
        :param id: UUID of control-node-zone
        :param ifmap_id: IFMAP id of control-node-zone
        :returns: :class:`.ControlNodeZone` object
        
        """
        raise NotImplementedError('control_node_zone_read is %s\'s responsibility' % (str(type (self))))
    # end control_node_zone_read

    def control_node_zone_update(self, obj):
        """Update control-node-zone.
        
        :param obj: :class:`.ControlNodeZone` object
        
        """
        raise NotImplementedError('control_node_zone_update is %s\'s responsibility' % (str(type (self))))
    # end control_node_zone_update

    def control_node_zones_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all control-node-zones.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ControlNodeZone` objects
        
        """
        raise NotImplementedError('control_node_zones_list is %s\'s responsibility' % (str(type (self))))
    # end control_node_zones_list

    def control_node_zone_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete control-node-zone from the system.
        
        :param fq_name: Fully qualified name of control-node-zone
        :param id: UUID of control-node-zone
        :param ifmap_id: IFMAP id of control-node-zone
        
        """
        raise NotImplementedError('control_node_zone_delete is %s\'s responsibility' % (str(type (self))))
    # end control_node_zone_delete

    def get_default_control_node_zone_id(self):
        """Return UUID of default control-node-zone."""
        raise NotImplementedError('get_default_control_node_zone_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_control_node_zone_delete

    def dsa_rule_create(self, obj):
        """Create new dsa-rule.
        
        :param obj: :class:`.DsaRule` object
        
        """
        raise NotImplementedError('dsa_rule_create is %s\'s responsibility' % (str(type (self))))
    # end dsa_rule_create

    def dsa_rule_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return dsa-rule information.
        
        :param fq_name: Fully qualified name of dsa-rule
        :param fq_name_str: Fully qualified name string of dsa-rule
        :param id: UUID of dsa-rule
        :param ifmap_id: IFMAP id of dsa-rule
        :returns: :class:`.DsaRule` object
        
        """
        raise NotImplementedError('dsa_rule_read is %s\'s responsibility' % (str(type (self))))
    # end dsa_rule_read

    def dsa_rule_update(self, obj):
        """Update dsa-rule.
        
        :param obj: :class:`.DsaRule` object
        
        """
        raise NotImplementedError('dsa_rule_update is %s\'s responsibility' % (str(type (self))))
    # end dsa_rule_update

    def dsa_rules_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all dsa-rules.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DsaRule` objects
        
        """
        raise NotImplementedError('dsa_rules_list is %s\'s responsibility' % (str(type (self))))
    # end dsa_rules_list

    def dsa_rule_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete dsa-rule from the system.
        
        :param fq_name: Fully qualified name of dsa-rule
        :param id: UUID of dsa-rule
        :param ifmap_id: IFMAP id of dsa-rule
        
        """
        raise NotImplementedError('dsa_rule_delete is %s\'s responsibility' % (str(type (self))))
    # end dsa_rule_delete

    def get_default_dsa_rule_id(self):
        """Return UUID of default dsa-rule."""
        raise NotImplementedError('get_default_dsa_rule_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_dsa_rule_delete

    def structured_syslog_config_create(self, obj):
        """Create new structured-syslog-config.
        
        :param obj: :class:`.StructuredSyslogConfig` object
        
        """
        raise NotImplementedError('structured_syslog_config_create is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_config_create

    def structured_syslog_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return structured-syslog-config information.
        
        :param fq_name: Fully qualified name of structured-syslog-config
        :param fq_name_str: Fully qualified name string of structured-syslog-config
        :param id: UUID of structured-syslog-config
        :param ifmap_id: IFMAP id of structured-syslog-config
        :returns: :class:`.StructuredSyslogConfig` object
        
        """
        raise NotImplementedError('structured_syslog_config_read is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_config_read

    def structured_syslog_config_update(self, obj):
        """Update structured-syslog-config.
        
        :param obj: :class:`.StructuredSyslogConfig` object
        
        """
        raise NotImplementedError('structured_syslog_config_update is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_config_update

    def structured_syslog_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all structured-syslog-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StructuredSyslogConfig` objects
        
        """
        raise NotImplementedError('structured_syslog_configs_list is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_configs_list

    def structured_syslog_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete structured-syslog-config from the system.
        
        :param fq_name: Fully qualified name of structured-syslog-config
        :param id: UUID of structured-syslog-config
        :param ifmap_id: IFMAP id of structured-syslog-config
        
        """
        raise NotImplementedError('structured_syslog_config_delete is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_config_delete

    def get_default_structured_syslog_config_id(self):
        """Return UUID of default structured-syslog-config."""
        raise NotImplementedError('get_default_structured_syslog_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_structured_syslog_config_delete

    def discovery_service_assignment_create(self, obj):
        """Create new discovery-service-assignment.
        
        :param obj: :class:`.DiscoveryServiceAssignment` object
        
        """
        raise NotImplementedError('discovery_service_assignment_create is %s\'s responsibility' % (str(type (self))))
    # end discovery_service_assignment_create

    def discovery_service_assignment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return discovery-service-assignment information.
        
        :param fq_name: Fully qualified name of discovery-service-assignment
        :param fq_name_str: Fully qualified name string of discovery-service-assignment
        :param id: UUID of discovery-service-assignment
        :param ifmap_id: IFMAP id of discovery-service-assignment
        :returns: :class:`.DiscoveryServiceAssignment` object
        
        """
        raise NotImplementedError('discovery_service_assignment_read is %s\'s responsibility' % (str(type (self))))
    # end discovery_service_assignment_read

    def discovery_service_assignment_update(self, obj):
        """Update discovery-service-assignment.
        
        :param obj: :class:`.DiscoveryServiceAssignment` object
        
        """
        raise NotImplementedError('discovery_service_assignment_update is %s\'s responsibility' % (str(type (self))))
    # end discovery_service_assignment_update

    def discovery_service_assignments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all discovery-service-assignments."""
        raise NotImplementedError('discovery_service_assignments_list is %s\'s responsibility' % (str(type (self))))
    # end discovery_service_assignments_list

    def discovery_service_assignment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete discovery-service-assignment from the system.
        
        :param fq_name: Fully qualified name of discovery-service-assignment
        :param id: UUID of discovery-service-assignment
        :param ifmap_id: IFMAP id of discovery-service-assignment
        
        """
        raise NotImplementedError('discovery_service_assignment_delete is %s\'s responsibility' % (str(type (self))))
    # end discovery_service_assignment_delete

    def get_default_discovery_service_assignment_id(self):
        """Return UUID of default discovery-service-assignment."""
        raise NotImplementedError('get_default_discovery_service_assignment_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_discovery_service_assignment_delete

    def logical_interface_create(self, obj):
        """Create new logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError('logical_interface_create is %s\'s responsibility' % (str(type (self))))
    # end logical_interface_create

    def logical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return logical-interface information.
        
        :param fq_name: Fully qualified name of logical-interface
        :param fq_name_str: Fully qualified name string of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        :returns: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError('logical_interface_read is %s\'s responsibility' % (str(type (self))))
    # end logical_interface_read

    def logical_interface_update(self, obj):
        """Update logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError('logical_interface_update is %s\'s responsibility' % (str(type (self))))
    # end logical_interface_update

    def logical_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all logical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalInterface` objects
        
        """
        raise NotImplementedError('logical_interfaces_list is %s\'s responsibility' % (str(type (self))))
    # end logical_interfaces_list

    def logical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-interface from the system.
        
        :param fq_name: Fully qualified name of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        
        """
        raise NotImplementedError('logical_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end logical_interface_delete

    def get_default_logical_interface_id(self):
        """Return UUID of default logical-interface."""
        raise NotImplementedError('get_default_logical_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_logical_interface_delete

    def flow_node_create(self, obj):
        """Create new flow-node.
        
        :param obj: :class:`.FlowNode` object
        
        """
        raise NotImplementedError('flow_node_create is %s\'s responsibility' % (str(type (self))))
    # end flow_node_create

    def flow_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return flow-node information.
        
        :param fq_name: Fully qualified name of flow-node
        :param fq_name_str: Fully qualified name string of flow-node
        :param id: UUID of flow-node
        :param ifmap_id: IFMAP id of flow-node
        :returns: :class:`.FlowNode` object
        
        """
        raise NotImplementedError('flow_node_read is %s\'s responsibility' % (str(type (self))))
    # end flow_node_read

    def flow_node_update(self, obj):
        """Update flow-node.
        
        :param obj: :class:`.FlowNode` object
        
        """
        raise NotImplementedError('flow_node_update is %s\'s responsibility' % (str(type (self))))
    # end flow_node_update

    def flow_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all flow-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FlowNode` objects
        
        """
        raise NotImplementedError('flow_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end flow_nodes_list

    def flow_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete flow-node from the system.
        
        :param fq_name: Fully qualified name of flow-node
        :param id: UUID of flow-node
        :param ifmap_id: IFMAP id of flow-node
        
        """
        raise NotImplementedError('flow_node_delete is %s\'s responsibility' % (str(type (self))))
    # end flow_node_delete

    def get_default_flow_node_id(self):
        """Return UUID of default flow-node."""
        raise NotImplementedError('get_default_flow_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_flow_node_delete

    def port_group_create(self, obj):
        """Create new port-group.
        
        :param obj: :class:`.PortGroup` object
        
        """
        raise NotImplementedError('port_group_create is %s\'s responsibility' % (str(type (self))))
    # end port_group_create

    def port_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return port-group information.
        
        :param fq_name: Fully qualified name of port-group
        :param fq_name_str: Fully qualified name string of port-group
        :param id: UUID of port-group
        :param ifmap_id: IFMAP id of port-group
        :returns: :class:`.PortGroup` object
        
        """
        raise NotImplementedError('port_group_read is %s\'s responsibility' % (str(type (self))))
    # end port_group_read

    def port_group_update(self, obj):
        """Update port-group.
        
        :param obj: :class:`.PortGroup` object
        
        """
        raise NotImplementedError('port_group_update is %s\'s responsibility' % (str(type (self))))
    # end port_group_update

    def port_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all port-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PortGroup` objects
        
        """
        raise NotImplementedError('port_groups_list is %s\'s responsibility' % (str(type (self))))
    # end port_groups_list

    def port_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete port-group from the system.
        
        :param fq_name: Fully qualified name of port-group
        :param id: UUID of port-group
        :param ifmap_id: IFMAP id of port-group
        
        """
        raise NotImplementedError('port_group_delete is %s\'s responsibility' % (str(type (self))))
    # end port_group_delete

    def get_default_port_group_id(self):
        """Return UUID of default port-group."""
        raise NotImplementedError('get_default_port_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_port_group_delete

    def route_aggregate_create(self, obj):
        """Create new route-aggregate.
        
        :param obj: :class:`.RouteAggregate` object
        
        """
        raise NotImplementedError('route_aggregate_create is %s\'s responsibility' % (str(type (self))))
    # end route_aggregate_create

    def route_aggregate_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return route-aggregate information.
        
        :param fq_name: Fully qualified name of route-aggregate
        :param fq_name_str: Fully qualified name string of route-aggregate
        :param id: UUID of route-aggregate
        :param ifmap_id: IFMAP id of route-aggregate
        :returns: :class:`.RouteAggregate` object
        
        """
        raise NotImplementedError('route_aggregate_read is %s\'s responsibility' % (str(type (self))))
    # end route_aggregate_read

    def route_aggregate_update(self, obj):
        """Update route-aggregate.
        
        :param obj: :class:`.RouteAggregate` object
        
        """
        raise NotImplementedError('route_aggregate_update is %s\'s responsibility' % (str(type (self))))
    # end route_aggregate_update

    def route_aggregates_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all route-aggregates.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RouteAggregate` objects
        
        """
        raise NotImplementedError('route_aggregates_list is %s\'s responsibility' % (str(type (self))))
    # end route_aggregates_list

    def route_aggregate_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-aggregate from the system.
        
        :param fq_name: Fully qualified name of route-aggregate
        :param id: UUID of route-aggregate
        :param ifmap_id: IFMAP id of route-aggregate
        
        """
        raise NotImplementedError('route_aggregate_delete is %s\'s responsibility' % (str(type (self))))
    # end route_aggregate_delete

    def get_default_route_aggregate_id(self):
        """Return UUID of default route-aggregate."""
        raise NotImplementedError('get_default_route_aggregate_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_route_aggregate_delete

    def logical_router_create(self, obj):
        """Create new logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError('logical_router_create is %s\'s responsibility' % (str(type (self))))
    # end logical_router_create

    def logical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return logical-router information.
        
        :param fq_name: Fully qualified name of logical-router
        :param fq_name_str: Fully qualified name string of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        :returns: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError('logical_router_read is %s\'s responsibility' % (str(type (self))))
    # end logical_router_read

    def logical_router_update(self, obj):
        """Update logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError('logical_router_update is %s\'s responsibility' % (str(type (self))))
    # end logical_router_update

    def logical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all logical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalRouter` objects
        
        """
        raise NotImplementedError('logical_routers_list is %s\'s responsibility' % (str(type (self))))
    # end logical_routers_list

    def logical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-router from the system.
        
        :param fq_name: Fully qualified name of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        
        """
        raise NotImplementedError('logical_router_delete is %s\'s responsibility' % (str(type (self))))
    # end logical_router_delete

    def get_default_logical_router_id(self):
        """Return UUID of default logical-router."""
        raise NotImplementedError('get_default_logical_router_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_logical_router_delete

    def domain_create(self, obj):
        """Create new domain.
        
        :param obj: :class:`.Domain` object
        
        """
        raise NotImplementedError('domain_create is %s\'s responsibility' % (str(type (self))))
    # end domain_create

    def domain_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return domain information.
        
        :param fq_name: Fully qualified name of domain
        :param fq_name_str: Fully qualified name string of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        :returns: :class:`.Domain` object
        
        """
        raise NotImplementedError('domain_read is %s\'s responsibility' % (str(type (self))))
    # end domain_read

    def domain_update(self, obj):
        """Update domain.
        
        :param obj: :class:`.Domain` object
        
        """
        raise NotImplementedError('domain_update is %s\'s responsibility' % (str(type (self))))
    # end domain_update

    def domains_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all domains.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Domain` objects
        
        """
        raise NotImplementedError('domains_list is %s\'s responsibility' % (str(type (self))))
    # end domains_list

    def domain_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete domain from the system.
        
        :param fq_name: Fully qualified name of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        
        """
        raise NotImplementedError('domain_delete is %s\'s responsibility' % (str(type (self))))
    # end domain_delete

    def get_default_domain_id(self):
        """Return UUID of default domain."""
        raise NotImplementedError('get_default_domain_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_domain_delete

    def structured_syslog_hostname_record_create(self, obj):
        """Create new structured-syslog-hostname-record.
        
        :param obj: :class:`.StructuredSyslogHostnameRecord` object
        
        """
        raise NotImplementedError('structured_syslog_hostname_record_create is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_hostname_record_create

    def structured_syslog_hostname_record_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return structured-syslog-hostname-record information.
        
        :param fq_name: Fully qualified name of structured-syslog-hostname-record
        :param fq_name_str: Fully qualified name string of structured-syslog-hostname-record
        :param id: UUID of structured-syslog-hostname-record
        :param ifmap_id: IFMAP id of structured-syslog-hostname-record
        :returns: :class:`.StructuredSyslogHostnameRecord` object
        
        """
        raise NotImplementedError('structured_syslog_hostname_record_read is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_hostname_record_read

    def structured_syslog_hostname_record_update(self, obj):
        """Update structured-syslog-hostname-record.
        
        :param obj: :class:`.StructuredSyslogHostnameRecord` object
        
        """
        raise NotImplementedError('structured_syslog_hostname_record_update is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_hostname_record_update

    def structured_syslog_hostname_records_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all structured-syslog-hostname-records.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StructuredSyslogHostnameRecord` objects
        
        """
        raise NotImplementedError('structured_syslog_hostname_records_list is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_hostname_records_list

    def structured_syslog_hostname_record_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete structured-syslog-hostname-record from the system.
        
        :param fq_name: Fully qualified name of structured-syslog-hostname-record
        :param id: UUID of structured-syslog-hostname-record
        :param ifmap_id: IFMAP id of structured-syslog-hostname-record
        
        """
        raise NotImplementedError('structured_syslog_hostname_record_delete is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_hostname_record_delete

    def get_default_structured_syslog_hostname_record_id(self):
        """Return UUID of default structured-syslog-hostname-record."""
        raise NotImplementedError('get_default_structured_syslog_hostname_record_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_structured_syslog_hostname_record_delete

    def service_instance_create(self, obj):
        """Create new service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError('service_instance_create is %s\'s responsibility' % (str(type (self))))
    # end service_instance_create

    def service_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-instance information.
        
        :param fq_name: Fully qualified name of service-instance
        :param fq_name_str: Fully qualified name string of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        :returns: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError('service_instance_read is %s\'s responsibility' % (str(type (self))))
    # end service_instance_read

    def service_instance_update(self, obj):
        """Update service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError('service_instance_update is %s\'s responsibility' % (str(type (self))))
    # end service_instance_update

    def service_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceInstance` objects
        
        """
        raise NotImplementedError('service_instances_list is %s\'s responsibility' % (str(type (self))))
    # end service_instances_list

    def service_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-instance from the system.
        
        :param fq_name: Fully qualified name of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        
        """
        raise NotImplementedError('service_instance_delete is %s\'s responsibility' % (str(type (self))))
    # end service_instance_delete

    def get_default_service_instance_id(self):
        """Return UUID of default service-instance."""
        raise NotImplementedError('get_default_service_instance_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_instance_delete

    def node_profile_create(self, obj):
        """Create new node-profile.
        
        :param obj: :class:`.NodeProfile` object
        
        """
        raise NotImplementedError('node_profile_create is %s\'s responsibility' % (str(type (self))))
    # end node_profile_create

    def node_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return node-profile information.
        
        :param fq_name: Fully qualified name of node-profile
        :param fq_name_str: Fully qualified name string of node-profile
        :param id: UUID of node-profile
        :param ifmap_id: IFMAP id of node-profile
        :returns: :class:`.NodeProfile` object
        
        """
        raise NotImplementedError('node_profile_read is %s\'s responsibility' % (str(type (self))))
    # end node_profile_read

    def node_profile_update(self, obj):
        """Update node-profile.
        
        :param obj: :class:`.NodeProfile` object
        
        """
        raise NotImplementedError('node_profile_update is %s\'s responsibility' % (str(type (self))))
    # end node_profile_update

    def node_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all node-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NodeProfile` objects
        
        """
        raise NotImplementedError('node_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end node_profiles_list

    def node_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete node-profile from the system.
        
        :param fq_name: Fully qualified name of node-profile
        :param id: UUID of node-profile
        :param ifmap_id: IFMAP id of node-profile
        
        """
        raise NotImplementedError('node_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end node_profile_delete

    def get_default_node_profile_id(self):
        """Return UUID of default node-profile."""
        raise NotImplementedError('get_default_node_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_node_profile_delete

    def bridge_domain_create(self, obj):
        """Create new bridge-domain.
        
        :param obj: :class:`.BridgeDomain` object
        
        """
        raise NotImplementedError('bridge_domain_create is %s\'s responsibility' % (str(type (self))))
    # end bridge_domain_create

    def bridge_domain_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return bridge-domain information.
        
        :param fq_name: Fully qualified name of bridge-domain
        :param fq_name_str: Fully qualified name string of bridge-domain
        :param id: UUID of bridge-domain
        :param ifmap_id: IFMAP id of bridge-domain
        :returns: :class:`.BridgeDomain` object
        
        """
        raise NotImplementedError('bridge_domain_read is %s\'s responsibility' % (str(type (self))))
    # end bridge_domain_read

    def bridge_domain_update(self, obj):
        """Update bridge-domain.
        
        :param obj: :class:`.BridgeDomain` object
        
        """
        raise NotImplementedError('bridge_domain_update is %s\'s responsibility' % (str(type (self))))
    # end bridge_domain_update

    def bridge_domains_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all bridge-domains.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.BridgeDomain` objects
        
        """
        raise NotImplementedError('bridge_domains_list is %s\'s responsibility' % (str(type (self))))
    # end bridge_domains_list

    def bridge_domain_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bridge-domain from the system.
        
        :param fq_name: Fully qualified name of bridge-domain
        :param id: UUID of bridge-domain
        :param ifmap_id: IFMAP id of bridge-domain
        
        """
        raise NotImplementedError('bridge_domain_delete is %s\'s responsibility' % (str(type (self))))
    # end bridge_domain_delete

    def get_default_bridge_domain_id(self):
        """Return UUID of default bridge-domain."""
        raise NotImplementedError('get_default_bridge_domain_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_bridge_domain_delete

    def alias_ip_create(self, obj):
        """Create new alias-ip.
        
        :param obj: :class:`.AliasIp` object
        
        """
        raise NotImplementedError('alias_ip_create is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_create

    def alias_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return alias-ip information.
        
        :param fq_name: Fully qualified name of alias-ip
        :param fq_name_str: Fully qualified name string of alias-ip
        :param id: UUID of alias-ip
        :param ifmap_id: IFMAP id of alias-ip
        :returns: :class:`.AliasIp` object
        
        """
        raise NotImplementedError('alias_ip_read is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_read

    def alias_ip_update(self, obj):
        """Update alias-ip.
        
        :param obj: :class:`.AliasIp` object
        
        """
        raise NotImplementedError('alias_ip_update is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_update

    def alias_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all alias-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AliasIp` objects
        
        """
        raise NotImplementedError('alias_ips_list is %s\'s responsibility' % (str(type (self))))
    # end alias_ips_list

    def alias_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete alias-ip from the system.
        
        :param fq_name: Fully qualified name of alias-ip
        :param id: UUID of alias-ip
        :param ifmap_id: IFMAP id of alias-ip
        
        """
        raise NotImplementedError('alias_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_delete

    def get_default_alias_ip_id(self):
        """Return UUID of default alias-ip."""
        raise NotImplementedError('get_default_alias_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_alias_ip_delete

    def webui_node_create(self, obj):
        """Create new webui-node.
        
        :param obj: :class:`.WebuiNode` object
        
        """
        raise NotImplementedError('webui_node_create is %s\'s responsibility' % (str(type (self))))
    # end webui_node_create

    def webui_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return webui-node information.
        
        :param fq_name: Fully qualified name of webui-node
        :param fq_name_str: Fully qualified name string of webui-node
        :param id: UUID of webui-node
        :param ifmap_id: IFMAP id of webui-node
        :returns: :class:`.WebuiNode` object
        
        """
        raise NotImplementedError('webui_node_read is %s\'s responsibility' % (str(type (self))))
    # end webui_node_read

    def webui_node_update(self, obj):
        """Update webui-node.
        
        :param obj: :class:`.WebuiNode` object
        
        """
        raise NotImplementedError('webui_node_update is %s\'s responsibility' % (str(type (self))))
    # end webui_node_update

    def webui_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all webui-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.WebuiNode` objects
        
        """
        raise NotImplementedError('webui_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end webui_nodes_list

    def webui_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete webui-node from the system.
        
        :param fq_name: Fully qualified name of webui-node
        :param id: UUID of webui-node
        :param ifmap_id: IFMAP id of webui-node
        
        """
        raise NotImplementedError('webui_node_delete is %s\'s responsibility' % (str(type (self))))
    # end webui_node_delete

    def get_default_webui_node_id(self):
        """Return UUID of default webui-node."""
        raise NotImplementedError('get_default_webui_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_webui_node_delete

    def port_create(self, obj):
        """Create new port.
        
        :param obj: :class:`.Port` object
        
        """
        raise NotImplementedError('port_create is %s\'s responsibility' % (str(type (self))))
    # end port_create

    def port_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return port information.
        
        :param fq_name: Fully qualified name of port
        :param fq_name_str: Fully qualified name string of port
        :param id: UUID of port
        :param ifmap_id: IFMAP id of port
        :returns: :class:`.Port` object
        
        """
        raise NotImplementedError('port_read is %s\'s responsibility' % (str(type (self))))
    # end port_read

    def port_update(self, obj):
        """Update port.
        
        :param obj: :class:`.Port` object
        
        """
        raise NotImplementedError('port_update is %s\'s responsibility' % (str(type (self))))
    # end port_update

    def ports_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all ports.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Port` objects
        
        """
        raise NotImplementedError('ports_list is %s\'s responsibility' % (str(type (self))))
    # end ports_list

    def port_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete port from the system.
        
        :param fq_name: Fully qualified name of port
        :param id: UUID of port
        :param ifmap_id: IFMAP id of port
        
        """
        raise NotImplementedError('port_delete is %s\'s responsibility' % (str(type (self))))
    # end port_delete

    def get_default_port_id(self):
        """Return UUID of default port."""
        raise NotImplementedError('get_default_port_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_port_delete

    def bgp_as_a_service_create(self, obj):
        """Create new bgp-as-a-service.
        
        :param obj: :class:`.BgpAsAService` object
        
        """
        raise NotImplementedError('bgp_as_a_service_create is %s\'s responsibility' % (str(type (self))))
    # end bgp_as_a_service_create

    def bgp_as_a_service_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return bgp-as-a-service information.
        
        :param fq_name: Fully qualified name of bgp-as-a-service
        :param fq_name_str: Fully qualified name string of bgp-as-a-service
        :param id: UUID of bgp-as-a-service
        :param ifmap_id: IFMAP id of bgp-as-a-service
        :returns: :class:`.BgpAsAService` object
        
        """
        raise NotImplementedError('bgp_as_a_service_read is %s\'s responsibility' % (str(type (self))))
    # end bgp_as_a_service_read

    def bgp_as_a_service_update(self, obj):
        """Update bgp-as-a-service.
        
        :param obj: :class:`.BgpAsAService` object
        
        """
        raise NotImplementedError('bgp_as_a_service_update is %s\'s responsibility' % (str(type (self))))
    # end bgp_as_a_service_update

    def bgp_as_a_services_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all bgp-as-a-services.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.BgpAsAService` objects
        
        """
        raise NotImplementedError('bgp_as_a_services_list is %s\'s responsibility' % (str(type (self))))
    # end bgp_as_a_services_list

    def bgp_as_a_service_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bgp-as-a-service from the system.
        
        :param fq_name: Fully qualified name of bgp-as-a-service
        :param id: UUID of bgp-as-a-service
        :param ifmap_id: IFMAP id of bgp-as-a-service
        
        """
        raise NotImplementedError('bgp_as_a_service_delete is %s\'s responsibility' % (str(type (self))))
    # end bgp_as_a_service_delete

    def get_default_bgp_as_a_service_id(self):
        """Return UUID of default bgp-as-a-service."""
        raise NotImplementedError('get_default_bgp_as_a_service_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_bgp_as_a_service_delete

    def subnet_create(self, obj):
        """Create new subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        raise NotImplementedError('subnet_create is %s\'s responsibility' % (str(type (self))))
    # end subnet_create

    def subnet_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return subnet information.
        
        :param fq_name: Fully qualified name of subnet
        :param fq_name_str: Fully qualified name string of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        :returns: :class:`.Subnet` object
        
        """
        raise NotImplementedError('subnet_read is %s\'s responsibility' % (str(type (self))))
    # end subnet_read

    def subnet_update(self, obj):
        """Update subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        raise NotImplementedError('subnet_update is %s\'s responsibility' % (str(type (self))))
    # end subnet_update

    def subnets_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all subnets."""
        raise NotImplementedError('subnets_list is %s\'s responsibility' % (str(type (self))))
    # end subnets_list

    def subnet_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete subnet from the system.
        
        :param fq_name: Fully qualified name of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        
        """
        raise NotImplementedError('subnet_delete is %s\'s responsibility' % (str(type (self))))
    # end subnet_delete

    def get_default_subnet_id(self):
        """Return UUID of default subnet."""
        raise NotImplementedError('get_default_subnet_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_subnet_delete

    def global_system_config_create(self, obj):
        """Create new global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError('global_system_config_create is %s\'s responsibility' % (str(type (self))))
    # end global_system_config_create

    def global_system_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-system-config information.
        
        :param fq_name: Fully qualified name of global-system-config
        :param fq_name_str: Fully qualified name string of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        :returns: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError('global_system_config_read is %s\'s responsibility' % (str(type (self))))
    # end global_system_config_read

    def global_system_config_update(self, obj):
        """Update global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError('global_system_config_update is %s\'s responsibility' % (str(type (self))))
    # end global_system_config_update

    def global_system_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-system-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalSystemConfig` objects
        
        """
        raise NotImplementedError('global_system_configs_list is %s\'s responsibility' % (str(type (self))))
    # end global_system_configs_list

    def global_system_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-system-config from the system.
        
        :param fq_name: Fully qualified name of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        
        """
        raise NotImplementedError('global_system_config_delete is %s\'s responsibility' % (str(type (self))))
    # end global_system_config_delete

    def get_default_global_system_config_id(self):
        """Return UUID of default global-system-config."""
        raise NotImplementedError('get_default_global_system_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_global_system_config_delete

    def sub_cluster_create(self, obj):
        """Create new sub-cluster.
        
        :param obj: :class:`.SubCluster` object
        
        """
        raise NotImplementedError('sub_cluster_create is %s\'s responsibility' % (str(type (self))))
    # end sub_cluster_create

    def sub_cluster_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return sub-cluster information.
        
        :param fq_name: Fully qualified name of sub-cluster
        :param fq_name_str: Fully qualified name string of sub-cluster
        :param id: UUID of sub-cluster
        :param ifmap_id: IFMAP id of sub-cluster
        :returns: :class:`.SubCluster` object
        
        """
        raise NotImplementedError('sub_cluster_read is %s\'s responsibility' % (str(type (self))))
    # end sub_cluster_read

    def sub_cluster_update(self, obj):
        """Update sub-cluster.
        
        :param obj: :class:`.SubCluster` object
        
        """
        raise NotImplementedError('sub_cluster_update is %s\'s responsibility' % (str(type (self))))
    # end sub_cluster_update

    def sub_clusters_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all sub-clusters."""
        raise NotImplementedError('sub_clusters_list is %s\'s responsibility' % (str(type (self))))
    # end sub_clusters_list

    def sub_cluster_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete sub-cluster from the system.
        
        :param fq_name: Fully qualified name of sub-cluster
        :param id: UUID of sub-cluster
        :param ifmap_id: IFMAP id of sub-cluster
        
        """
        raise NotImplementedError('sub_cluster_delete is %s\'s responsibility' % (str(type (self))))
    # end sub_cluster_delete

    def get_default_sub_cluster_id(self):
        """Return UUID of default sub-cluster."""
        raise NotImplementedError('get_default_sub_cluster_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_sub_cluster_delete

    def forwarding_class_create(self, obj):
        """Create new forwarding-class.
        
        :param obj: :class:`.ForwardingClass` object
        
        """
        raise NotImplementedError('forwarding_class_create is %s\'s responsibility' % (str(type (self))))
    # end forwarding_class_create

    def forwarding_class_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return forwarding-class information.
        
        :param fq_name: Fully qualified name of forwarding-class
        :param fq_name_str: Fully qualified name string of forwarding-class
        :param id: UUID of forwarding-class
        :param ifmap_id: IFMAP id of forwarding-class
        :returns: :class:`.ForwardingClass` object
        
        """
        raise NotImplementedError('forwarding_class_read is %s\'s responsibility' % (str(type (self))))
    # end forwarding_class_read

    def forwarding_class_update(self, obj):
        """Update forwarding-class.
        
        :param obj: :class:`.ForwardingClass` object
        
        """
        raise NotImplementedError('forwarding_class_update is %s\'s responsibility' % (str(type (self))))
    # end forwarding_class_update

    def forwarding_classs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all forwarding-classs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ForwardingClass` objects
        
        """
        raise NotImplementedError('forwarding_classs_list is %s\'s responsibility' % (str(type (self))))
    # end forwarding_classs_list

    def forwarding_class_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete forwarding-class from the system.
        
        :param fq_name: Fully qualified name of forwarding-class
        :param id: UUID of forwarding-class
        :param ifmap_id: IFMAP id of forwarding-class
        
        """
        raise NotImplementedError('forwarding_class_delete is %s\'s responsibility' % (str(type (self))))
    # end forwarding_class_delete

    def get_default_forwarding_class_id(self):
        """Return UUID of default forwarding-class."""
        raise NotImplementedError('get_default_forwarding_class_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_forwarding_class_delete

    def service_group_create(self, obj):
        """Create new service-group.
        
        :param obj: :class:`.ServiceGroup` object
        
        """
        raise NotImplementedError('service_group_create is %s\'s responsibility' % (str(type (self))))
    # end service_group_create

    def service_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-group information.
        
        :param fq_name: Fully qualified name of service-group
        :param fq_name_str: Fully qualified name string of service-group
        :param id: UUID of service-group
        :param ifmap_id: IFMAP id of service-group
        :returns: :class:`.ServiceGroup` object
        
        """
        raise NotImplementedError('service_group_read is %s\'s responsibility' % (str(type (self))))
    # end service_group_read

    def service_group_update(self, obj):
        """Update service-group.
        
        :param obj: :class:`.ServiceGroup` object
        
        """
        raise NotImplementedError('service_group_update is %s\'s responsibility' % (str(type (self))))
    # end service_group_update

    def service_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceGroup` objects
        
        """
        raise NotImplementedError('service_groups_list is %s\'s responsibility' % (str(type (self))))
    # end service_groups_list

    def service_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-group from the system.
        
        :param fq_name: Fully qualified name of service-group
        :param id: UUID of service-group
        :param ifmap_id: IFMAP id of service-group
        
        """
        raise NotImplementedError('service_group_delete is %s\'s responsibility' % (str(type (self))))
    # end service_group_delete

    def get_default_service_group_id(self):
        """Return UUID of default service-group."""
        raise NotImplementedError('get_default_service_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_group_delete

    def global_analytics_config_create(self, obj):
        """Create new global-analytics-config.
        
        :param obj: :class:`.GlobalAnalyticsConfig` object
        
        """
        raise NotImplementedError('global_analytics_config_create is %s\'s responsibility' % (str(type (self))))
    # end global_analytics_config_create

    def global_analytics_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-analytics-config information.
        
        :param fq_name: Fully qualified name of global-analytics-config
        :param fq_name_str: Fully qualified name string of global-analytics-config
        :param id: UUID of global-analytics-config
        :param ifmap_id: IFMAP id of global-analytics-config
        :returns: :class:`.GlobalAnalyticsConfig` object
        
        """
        raise NotImplementedError('global_analytics_config_read is %s\'s responsibility' % (str(type (self))))
    # end global_analytics_config_read

    def global_analytics_config_update(self, obj):
        """Update global-analytics-config.
        
        :param obj: :class:`.GlobalAnalyticsConfig` object
        
        """
        raise NotImplementedError('global_analytics_config_update is %s\'s responsibility' % (str(type (self))))
    # end global_analytics_config_update

    def global_analytics_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-analytics-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalAnalyticsConfig` objects
        
        """
        raise NotImplementedError('global_analytics_configs_list is %s\'s responsibility' % (str(type (self))))
    # end global_analytics_configs_list

    def global_analytics_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-analytics-config from the system.
        
        :param fq_name: Fully qualified name of global-analytics-config
        :param id: UUID of global-analytics-config
        :param ifmap_id: IFMAP id of global-analytics-config
        
        """
        raise NotImplementedError('global_analytics_config_delete is %s\'s responsibility' % (str(type (self))))
    # end global_analytics_config_delete

    def get_default_global_analytics_config_id(self):
        """Return UUID of default global-analytics-config."""
        raise NotImplementedError('get_default_global_analytics_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_global_analytics_config_delete

    def address_group_create(self, obj):
        """Create new address-group.
        
        :param obj: :class:`.AddressGroup` object
        
        """
        raise NotImplementedError('address_group_create is %s\'s responsibility' % (str(type (self))))
    # end address_group_create

    def address_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return address-group information.
        
        :param fq_name: Fully qualified name of address-group
        :param fq_name_str: Fully qualified name string of address-group
        :param id: UUID of address-group
        :param ifmap_id: IFMAP id of address-group
        :returns: :class:`.AddressGroup` object
        
        """
        raise NotImplementedError('address_group_read is %s\'s responsibility' % (str(type (self))))
    # end address_group_read

    def address_group_update(self, obj):
        """Update address-group.
        
        :param obj: :class:`.AddressGroup` object
        
        """
        raise NotImplementedError('address_group_update is %s\'s responsibility' % (str(type (self))))
    # end address_group_update

    def address_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all address-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AddressGroup` objects
        
        """
        raise NotImplementedError('address_groups_list is %s\'s responsibility' % (str(type (self))))
    # end address_groups_list

    def address_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete address-group from the system.
        
        :param fq_name: Fully qualified name of address-group
        :param id: UUID of address-group
        :param ifmap_id: IFMAP id of address-group
        
        """
        raise NotImplementedError('address_group_delete is %s\'s responsibility' % (str(type (self))))
    # end address_group_delete

    def get_default_address_group_id(self):
        """Return UUID of default address-group."""
        raise NotImplementedError('get_default_address_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_address_group_delete

    def application_policy_set_create(self, obj):
        """Create new application-policy-set.
        
        :param obj: :class:`.ApplicationPolicySet` object
        
        """
        raise NotImplementedError('application_policy_set_create is %s\'s responsibility' % (str(type (self))))
    # end application_policy_set_create

    def application_policy_set_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return application-policy-set information.
        
        :param fq_name: Fully qualified name of application-policy-set
        :param fq_name_str: Fully qualified name string of application-policy-set
        :param id: UUID of application-policy-set
        :param ifmap_id: IFMAP id of application-policy-set
        :returns: :class:`.ApplicationPolicySet` object
        
        """
        raise NotImplementedError('application_policy_set_read is %s\'s responsibility' % (str(type (self))))
    # end application_policy_set_read

    def application_policy_set_update(self, obj):
        """Update application-policy-set.
        
        :param obj: :class:`.ApplicationPolicySet` object
        
        """
        raise NotImplementedError('application_policy_set_update is %s\'s responsibility' % (str(type (self))))
    # end application_policy_set_update

    def application_policy_sets_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all application-policy-sets.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ApplicationPolicySet` objects
        
        """
        raise NotImplementedError('application_policy_sets_list is %s\'s responsibility' % (str(type (self))))
    # end application_policy_sets_list

    def application_policy_set_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete application-policy-set from the system.
        
        :param fq_name: Fully qualified name of application-policy-set
        :param id: UUID of application-policy-set
        :param ifmap_id: IFMAP id of application-policy-set
        
        """
        raise NotImplementedError('application_policy_set_delete is %s\'s responsibility' % (str(type (self))))
    # end application_policy_set_delete

    def get_default_application_policy_set_id(self):
        """Return UUID of default application-policy-set."""
        raise NotImplementedError('get_default_application_policy_set_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_application_policy_set_delete

    def virtual_ip_create(self, obj):
        """Create new virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError('virtual_ip_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_ip_create

    def virtual_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-ip information.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param fq_name_str: Fully qualified name string of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        :returns: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError('virtual_ip_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_ip_read

    def virtual_ip_update(self, obj):
        """Update virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError('virtual_ip_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_ip_update

    def virtual_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualIp` objects
        
        """
        raise NotImplementedError('virtual_ips_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_ips_list

    def virtual_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-ip from the system.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        
        """
        raise NotImplementedError('virtual_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_ip_delete

    def get_default_virtual_ip_id(self):
        """Return UUID of default virtual-ip."""
        raise NotImplementedError('get_default_virtual_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_ip_delete

    def intent_map_create(self, obj):
        """Create new intent-map.
        
        :param obj: :class:`.IntentMap` object
        
        """
        raise NotImplementedError('intent_map_create is %s\'s responsibility' % (str(type (self))))
    # end intent_map_create

    def intent_map_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return intent-map information.
        
        :param fq_name: Fully qualified name of intent-map
        :param fq_name_str: Fully qualified name string of intent-map
        :param id: UUID of intent-map
        :param ifmap_id: IFMAP id of intent-map
        :returns: :class:`.IntentMap` object
        
        """
        raise NotImplementedError('intent_map_read is %s\'s responsibility' % (str(type (self))))
    # end intent_map_read

    def intent_map_update(self, obj):
        """Update intent-map.
        
        :param obj: :class:`.IntentMap` object
        
        """
        raise NotImplementedError('intent_map_update is %s\'s responsibility' % (str(type (self))))
    # end intent_map_update

    def intent_maps_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all intent-maps.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.IntentMap` objects
        
        """
        raise NotImplementedError('intent_maps_list is %s\'s responsibility' % (str(type (self))))
    # end intent_maps_list

    def intent_map_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete intent-map from the system.
        
        :param fq_name: Fully qualified name of intent-map
        :param id: UUID of intent-map
        :param ifmap_id: IFMAP id of intent-map
        
        """
        raise NotImplementedError('intent_map_delete is %s\'s responsibility' % (str(type (self))))
    # end intent_map_delete

    def get_default_intent_map_id(self):
        """Return UUID of default intent-map."""
        raise NotImplementedError('get_default_intent_map_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_intent_map_delete

    def port_tuple_create(self, obj):
        """Create new port-tuple.
        
        :param obj: :class:`.PortTuple` object
        
        """
        raise NotImplementedError('port_tuple_create is %s\'s responsibility' % (str(type (self))))
    # end port_tuple_create

    def port_tuple_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return port-tuple information.
        
        :param fq_name: Fully qualified name of port-tuple
        :param fq_name_str: Fully qualified name string of port-tuple
        :param id: UUID of port-tuple
        :param ifmap_id: IFMAP id of port-tuple
        :returns: :class:`.PortTuple` object
        
        """
        raise NotImplementedError('port_tuple_read is %s\'s responsibility' % (str(type (self))))
    # end port_tuple_read

    def port_tuple_update(self, obj):
        """Update port-tuple.
        
        :param obj: :class:`.PortTuple` object
        
        """
        raise NotImplementedError('port_tuple_update is %s\'s responsibility' % (str(type (self))))
    # end port_tuple_update

    def port_tuples_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all port-tuples.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PortTuple` objects
        
        """
        raise NotImplementedError('port_tuples_list is %s\'s responsibility' % (str(type (self))))
    # end port_tuples_list

    def port_tuple_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete port-tuple from the system.
        
        :param fq_name: Fully qualified name of port-tuple
        :param id: UUID of port-tuple
        :param ifmap_id: IFMAP id of port-tuple
        
        """
        raise NotImplementedError('port_tuple_delete is %s\'s responsibility' % (str(type (self))))
    # end port_tuple_delete

    def get_default_port_tuple_id(self):
        """Return UUID of default port-tuple."""
        raise NotImplementedError('get_default_port_tuple_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_port_tuple_delete

    def analytics_alarm_node_create(self, obj):
        """Create new analytics-alarm-node.
        
        :param obj: :class:`.AnalyticsAlarmNode` object
        
        """
        raise NotImplementedError('analytics_alarm_node_create is %s\'s responsibility' % (str(type (self))))
    # end analytics_alarm_node_create

    def analytics_alarm_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return analytics-alarm-node information.
        
        :param fq_name: Fully qualified name of analytics-alarm-node
        :param fq_name_str: Fully qualified name string of analytics-alarm-node
        :param id: UUID of analytics-alarm-node
        :param ifmap_id: IFMAP id of analytics-alarm-node
        :returns: :class:`.AnalyticsAlarmNode` object
        
        """
        raise NotImplementedError('analytics_alarm_node_read is %s\'s responsibility' % (str(type (self))))
    # end analytics_alarm_node_read

    def analytics_alarm_node_update(self, obj):
        """Update analytics-alarm-node.
        
        :param obj: :class:`.AnalyticsAlarmNode` object
        
        """
        raise NotImplementedError('analytics_alarm_node_update is %s\'s responsibility' % (str(type (self))))
    # end analytics_alarm_node_update

    def analytics_alarm_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all analytics-alarm-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AnalyticsAlarmNode` objects
        
        """
        raise NotImplementedError('analytics_alarm_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end analytics_alarm_nodes_list

    def analytics_alarm_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete analytics-alarm-node from the system.
        
        :param fq_name: Fully qualified name of analytics-alarm-node
        :param id: UUID of analytics-alarm-node
        :param ifmap_id: IFMAP id of analytics-alarm-node
        
        """
        raise NotImplementedError('analytics_alarm_node_delete is %s\'s responsibility' % (str(type (self))))
    # end analytics_alarm_node_delete

    def get_default_analytics_alarm_node_id(self):
        """Return UUID of default analytics-alarm-node."""
        raise NotImplementedError('get_default_analytics_alarm_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_analytics_alarm_node_delete

    def qos_queue_create(self, obj):
        """Create new qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        raise NotImplementedError('qos_queue_create is %s\'s responsibility' % (str(type (self))))
    # end qos_queue_create

    def qos_queue_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return qos-queue information.
        
        :param fq_name: Fully qualified name of qos-queue
        :param fq_name_str: Fully qualified name string of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        :returns: :class:`.QosQueue` object
        
        """
        raise NotImplementedError('qos_queue_read is %s\'s responsibility' % (str(type (self))))
    # end qos_queue_read

    def qos_queue_update(self, obj):
        """Update qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        raise NotImplementedError('qos_queue_update is %s\'s responsibility' % (str(type (self))))
    # end qos_queue_update

    def qos_queues_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all qos-queues.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosQueue` objects
        
        """
        raise NotImplementedError('qos_queues_list is %s\'s responsibility' % (str(type (self))))
    # end qos_queues_list

    def qos_queue_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-queue from the system.
        
        :param fq_name: Fully qualified name of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        
        """
        raise NotImplementedError('qos_queue_delete is %s\'s responsibility' % (str(type (self))))
    # end qos_queue_delete

    def get_default_qos_queue_id(self):
        """Return UUID of default qos-queue."""
        raise NotImplementedError('get_default_qos_queue_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_qos_queue_delete

    def physical_role_create(self, obj):
        """Create new physical-role.
        
        :param obj: :class:`.PhysicalRole` object
        
        """
        raise NotImplementedError('physical_role_create is %s\'s responsibility' % (str(type (self))))
    # end physical_role_create

    def physical_role_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return physical-role information.
        
        :param fq_name: Fully qualified name of physical-role
        :param fq_name_str: Fully qualified name string of physical-role
        :param id: UUID of physical-role
        :param ifmap_id: IFMAP id of physical-role
        :returns: :class:`.PhysicalRole` object
        
        """
        raise NotImplementedError('physical_role_read is %s\'s responsibility' % (str(type (self))))
    # end physical_role_read

    def physical_role_update(self, obj):
        """Update physical-role.
        
        :param obj: :class:`.PhysicalRole` object
        
        """
        raise NotImplementedError('physical_role_update is %s\'s responsibility' % (str(type (self))))
    # end physical_role_update

    def physical_roles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all physical-roles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalRole` objects
        
        """
        raise NotImplementedError('physical_roles_list is %s\'s responsibility' % (str(type (self))))
    # end physical_roles_list

    def physical_role_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-role from the system.
        
        :param fq_name: Fully qualified name of physical-role
        :param id: UUID of physical-role
        :param ifmap_id: IFMAP id of physical-role
        
        """
        raise NotImplementedError('physical_role_delete is %s\'s responsibility' % (str(type (self))))
    # end physical_role_delete

    def get_default_physical_role_id(self):
        """Return UUID of default physical-role."""
        raise NotImplementedError('get_default_physical_role_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_physical_role_delete

    def card_create(self, obj):
        """Create new card.
        
        :param obj: :class:`.Card` object
        
        """
        raise NotImplementedError('card_create is %s\'s responsibility' % (str(type (self))))
    # end card_create

    def card_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return card information.
        
        :param fq_name: Fully qualified name of card
        :param fq_name_str: Fully qualified name string of card
        :param id: UUID of card
        :param ifmap_id: IFMAP id of card
        :returns: :class:`.Card` object
        
        """
        raise NotImplementedError('card_read is %s\'s responsibility' % (str(type (self))))
    # end card_read

    def card_update(self, obj):
        """Update card.
        
        :param obj: :class:`.Card` object
        
        """
        raise NotImplementedError('card_update is %s\'s responsibility' % (str(type (self))))
    # end card_update

    def cards_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all cards."""
        raise NotImplementedError('cards_list is %s\'s responsibility' % (str(type (self))))
    # end cards_list

    def card_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete card from the system.
        
        :param fq_name: Fully qualified name of card
        :param id: UUID of card
        :param ifmap_id: IFMAP id of card
        
        """
        raise NotImplementedError('card_delete is %s\'s responsibility' % (str(type (self))))
    # end card_delete

    def get_default_card_id(self):
        """Return UUID of default card."""
        raise NotImplementedError('get_default_card_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_card_delete

    def security_logging_object_create(self, obj):
        """Create new security-logging-object.
        
        :param obj: :class:`.SecurityLoggingObject` object
        
        """
        raise NotImplementedError('security_logging_object_create is %s\'s responsibility' % (str(type (self))))
    # end security_logging_object_create

    def security_logging_object_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return security-logging-object information.
        
        :param fq_name: Fully qualified name of security-logging-object
        :param fq_name_str: Fully qualified name string of security-logging-object
        :param id: UUID of security-logging-object
        :param ifmap_id: IFMAP id of security-logging-object
        :returns: :class:`.SecurityLoggingObject` object
        
        """
        raise NotImplementedError('security_logging_object_read is %s\'s responsibility' % (str(type (self))))
    # end security_logging_object_read

    def security_logging_object_update(self, obj):
        """Update security-logging-object.
        
        :param obj: :class:`.SecurityLoggingObject` object
        
        """
        raise NotImplementedError('security_logging_object_update is %s\'s responsibility' % (str(type (self))))
    # end security_logging_object_update

    def security_logging_objects_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all security-logging-objects.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.SecurityLoggingObject` objects
        
        """
        raise NotImplementedError('security_logging_objects_list is %s\'s responsibility' % (str(type (self))))
    # end security_logging_objects_list

    def security_logging_object_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete security-logging-object from the system.
        
        :param fq_name: Fully qualified name of security-logging-object
        :param id: UUID of security-logging-object
        :param ifmap_id: IFMAP id of security-logging-object
        
        """
        raise NotImplementedError('security_logging_object_delete is %s\'s responsibility' % (str(type (self))))
    # end security_logging_object_delete

    def get_default_security_logging_object_id(self):
        """Return UUID of default security-logging-object."""
        raise NotImplementedError('get_default_security_logging_object_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_security_logging_object_delete

    def qos_config_create(self, obj):
        """Create new qos-config.
        
        :param obj: :class:`.QosConfig` object
        
        """
        raise NotImplementedError('qos_config_create is %s\'s responsibility' % (str(type (self))))
    # end qos_config_create

    def qos_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return qos-config information.
        
        :param fq_name: Fully qualified name of qos-config
        :param fq_name_str: Fully qualified name string of qos-config
        :param id: UUID of qos-config
        :param ifmap_id: IFMAP id of qos-config
        :returns: :class:`.QosConfig` object
        
        """
        raise NotImplementedError('qos_config_read is %s\'s responsibility' % (str(type (self))))
    # end qos_config_read

    def qos_config_update(self, obj):
        """Update qos-config.
        
        :param obj: :class:`.QosConfig` object
        
        """
        raise NotImplementedError('qos_config_update is %s\'s responsibility' % (str(type (self))))
    # end qos_config_update

    def qos_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all qos-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosConfig` objects
        
        """
        raise NotImplementedError('qos_configs_list is %s\'s responsibility' % (str(type (self))))
    # end qos_configs_list

    def qos_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-config from the system.
        
        :param fq_name: Fully qualified name of qos-config
        :param id: UUID of qos-config
        :param ifmap_id: IFMAP id of qos-config
        
        """
        raise NotImplementedError('qos_config_delete is %s\'s responsibility' % (str(type (self))))
    # end qos_config_delete

    def get_default_qos_config_id(self):
        """Return UUID of default qos-config."""
        raise NotImplementedError('get_default_qos_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_qos_config_delete

    def analytics_snmp_node_create(self, obj):
        """Create new analytics-snmp-node.
        
        :param obj: :class:`.AnalyticsSnmpNode` object
        
        """
        raise NotImplementedError('analytics_snmp_node_create is %s\'s responsibility' % (str(type (self))))
    # end analytics_snmp_node_create

    def analytics_snmp_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return analytics-snmp-node information.
        
        :param fq_name: Fully qualified name of analytics-snmp-node
        :param fq_name_str: Fully qualified name string of analytics-snmp-node
        :param id: UUID of analytics-snmp-node
        :param ifmap_id: IFMAP id of analytics-snmp-node
        :returns: :class:`.AnalyticsSnmpNode` object
        
        """
        raise NotImplementedError('analytics_snmp_node_read is %s\'s responsibility' % (str(type (self))))
    # end analytics_snmp_node_read

    def analytics_snmp_node_update(self, obj):
        """Update analytics-snmp-node.
        
        :param obj: :class:`.AnalyticsSnmpNode` object
        
        """
        raise NotImplementedError('analytics_snmp_node_update is %s\'s responsibility' % (str(type (self))))
    # end analytics_snmp_node_update

    def analytics_snmp_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all analytics-snmp-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AnalyticsSnmpNode` objects
        
        """
        raise NotImplementedError('analytics_snmp_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end analytics_snmp_nodes_list

    def analytics_snmp_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete analytics-snmp-node from the system.
        
        :param fq_name: Fully qualified name of analytics-snmp-node
        :param id: UUID of analytics-snmp-node
        :param ifmap_id: IFMAP id of analytics-snmp-node
        
        """
        raise NotImplementedError('analytics_snmp_node_delete is %s\'s responsibility' % (str(type (self))))
    # end analytics_snmp_node_delete

    def get_default_analytics_snmp_node_id(self):
        """Return UUID of default analytics-snmp-node."""
        raise NotImplementedError('get_default_analytics_snmp_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_analytics_snmp_node_delete

    def virtual_machine_interface_create(self, obj):
        """Create new virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError('virtual_machine_interface_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_interface_create

    def virtual_machine_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-machine-interface information.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param fq_name_str: Fully qualified name string of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        :returns: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError('virtual_machine_interface_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_interface_read

    def virtual_machine_interface_update(self, obj):
        """Update virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError('virtual_machine_interface_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_interface_update

    def virtual_machine_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-machine-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualMachineInterface` objects
        
        """
        raise NotImplementedError('virtual_machine_interfaces_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_interfaces_list

    def virtual_machine_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine-interface from the system.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        
        """
        raise NotImplementedError('virtual_machine_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_interface_delete

    def get_default_virtual_machine_interface_id(self):
        """Return UUID of default virtual-machine-interface."""
        raise NotImplementedError('get_default_virtual_machine_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_machine_interface_delete

    def cli_config_create(self, obj):
        """Create new cli-config.
        
        :param obj: :class:`.CliConfig` object
        
        """
        raise NotImplementedError('cli_config_create is %s\'s responsibility' % (str(type (self))))
    # end cli_config_create

    def cli_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return cli-config information.
        
        :param fq_name: Fully qualified name of cli-config
        :param fq_name_str: Fully qualified name string of cli-config
        :param id: UUID of cli-config
        :param ifmap_id: IFMAP id of cli-config
        :returns: :class:`.CliConfig` object
        
        """
        raise NotImplementedError('cli_config_read is %s\'s responsibility' % (str(type (self))))
    # end cli_config_read

    def cli_config_update(self, obj):
        """Update cli-config.
        
        :param obj: :class:`.CliConfig` object
        
        """
        raise NotImplementedError('cli_config_update is %s\'s responsibility' % (str(type (self))))
    # end cli_config_update

    def cli_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all cli-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.CliConfig` objects
        
        """
        raise NotImplementedError('cli_configs_list is %s\'s responsibility' % (str(type (self))))
    # end cli_configs_list

    def cli_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete cli-config from the system.
        
        :param fq_name: Fully qualified name of cli-config
        :param id: UUID of cli-config
        :param ifmap_id: IFMAP id of cli-config
        
        """
        raise NotImplementedError('cli_config_delete is %s\'s responsibility' % (str(type (self))))
    # end cli_config_delete

    def get_default_cli_config_id(self):
        """Return UUID of default cli-config."""
        raise NotImplementedError('get_default_cli_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_cli_config_delete

    def service_object_create(self, obj):
        """Create new service-object.
        
        :param obj: :class:`.ServiceObject` object
        
        """
        raise NotImplementedError('service_object_create is %s\'s responsibility' % (str(type (self))))
    # end service_object_create

    def service_object_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-object information.
        
        :param fq_name: Fully qualified name of service-object
        :param fq_name_str: Fully qualified name string of service-object
        :param id: UUID of service-object
        :param ifmap_id: IFMAP id of service-object
        :returns: :class:`.ServiceObject` object
        
        """
        raise NotImplementedError('service_object_read is %s\'s responsibility' % (str(type (self))))
    # end service_object_read

    def service_object_update(self, obj):
        """Update service-object.
        
        :param obj: :class:`.ServiceObject` object
        
        """
        raise NotImplementedError('service_object_update is %s\'s responsibility' % (str(type (self))))
    # end service_object_update

    def service_objects_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-objects."""
        raise NotImplementedError('service_objects_list is %s\'s responsibility' % (str(type (self))))
    # end service_objects_list

    def service_object_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-object from the system.
        
        :param fq_name: Fully qualified name of service-object
        :param id: UUID of service-object
        :param ifmap_id: IFMAP id of service-object
        
        """
        raise NotImplementedError('service_object_delete is %s\'s responsibility' % (str(type (self))))
    # end service_object_delete

    def get_default_service_object_id(self):
        """Return UUID of default service-object."""
        raise NotImplementedError('get_default_service_object_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_object_delete

    def feature_flag_create(self, obj):
        """Create new feature-flag.
        
        :param obj: :class:`.FeatureFlag` object
        
        """
        raise NotImplementedError('feature_flag_create is %s\'s responsibility' % (str(type (self))))
    # end feature_flag_create

    def feature_flag_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return feature-flag information.
        
        :param fq_name: Fully qualified name of feature-flag
        :param fq_name_str: Fully qualified name string of feature-flag
        :param id: UUID of feature-flag
        :param ifmap_id: IFMAP id of feature-flag
        :returns: :class:`.FeatureFlag` object
        
        """
        raise NotImplementedError('feature_flag_read is %s\'s responsibility' % (str(type (self))))
    # end feature_flag_read

    def feature_flag_update(self, obj):
        """Update feature-flag.
        
        :param obj: :class:`.FeatureFlag` object
        
        """
        raise NotImplementedError('feature_flag_update is %s\'s responsibility' % (str(type (self))))
    # end feature_flag_update

    def feature_flags_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all feature-flags.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FeatureFlag` objects
        
        """
        raise NotImplementedError('feature_flags_list is %s\'s responsibility' % (str(type (self))))
    # end feature_flags_list

    def feature_flag_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete feature-flag from the system.
        
        :param fq_name: Fully qualified name of feature-flag
        :param id: UUID of feature-flag
        :param ifmap_id: IFMAP id of feature-flag
        
        """
        raise NotImplementedError('feature_flag_delete is %s\'s responsibility' % (str(type (self))))
    # end feature_flag_delete

    def get_default_feature_flag_id(self):
        """Return UUID of default feature-flag."""
        raise NotImplementedError('get_default_feature_flag_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_feature_flag_delete

    def loadbalancer_create(self, obj):
        """Create new loadbalancer.
        
        :param obj: :class:`.Loadbalancer` object
        
        """
        raise NotImplementedError('loadbalancer_create is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_create

    def loadbalancer_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer information.
        
        :param fq_name: Fully qualified name of loadbalancer
        :param fq_name_str: Fully qualified name string of loadbalancer
        :param id: UUID of loadbalancer
        :param ifmap_id: IFMAP id of loadbalancer
        :returns: :class:`.Loadbalancer` object
        
        """
        raise NotImplementedError('loadbalancer_read is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_read

    def loadbalancer_update(self, obj):
        """Update loadbalancer.
        
        :param obj: :class:`.Loadbalancer` object
        
        """
        raise NotImplementedError('loadbalancer_update is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_update

    def loadbalancers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Loadbalancer` objects
        
        """
        raise NotImplementedError('loadbalancers_list is %s\'s responsibility' % (str(type (self))))
    # end loadbalancers_list

    def loadbalancer_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer from the system.
        
        :param fq_name: Fully qualified name of loadbalancer
        :param id: UUID of loadbalancer
        :param ifmap_id: IFMAP id of loadbalancer
        
        """
        raise NotImplementedError('loadbalancer_delete is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_delete

    def get_default_loadbalancer_id(self):
        """Return UUID of default loadbalancer."""
        raise NotImplementedError('get_default_loadbalancer_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_loadbalancer_delete

    def peering_policy_create(self, obj):
        """Create new peering-policy.
        
        :param obj: :class:`.PeeringPolicy` object
        
        """
        raise NotImplementedError('peering_policy_create is %s\'s responsibility' % (str(type (self))))
    # end peering_policy_create

    def peering_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return peering-policy information.
        
        :param fq_name: Fully qualified name of peering-policy
        :param fq_name_str: Fully qualified name string of peering-policy
        :param id: UUID of peering-policy
        :param ifmap_id: IFMAP id of peering-policy
        :returns: :class:`.PeeringPolicy` object
        
        """
        raise NotImplementedError('peering_policy_read is %s\'s responsibility' % (str(type (self))))
    # end peering_policy_read

    def peering_policy_update(self, obj):
        """Update peering-policy.
        
        :param obj: :class:`.PeeringPolicy` object
        
        """
        raise NotImplementedError('peering_policy_update is %s\'s responsibility' % (str(type (self))))
    # end peering_policy_update

    def peering_policys_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all peering-policys."""
        raise NotImplementedError('peering_policys_list is %s\'s responsibility' % (str(type (self))))
    # end peering_policys_list

    def peering_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete peering-policy from the system.
        
        :param fq_name: Fully qualified name of peering-policy
        :param id: UUID of peering-policy
        :param ifmap_id: IFMAP id of peering-policy
        
        """
        raise NotImplementedError('peering_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end peering_policy_delete

    def get_default_peering_policy_id(self):
        """Return UUID of default peering-policy."""
        raise NotImplementedError('get_default_peering_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_peering_policy_delete

    def structured_syslog_application_record_create(self, obj):
        """Create new structured-syslog-application-record.
        
        :param obj: :class:`.StructuredSyslogApplicationRecord` object
        
        """
        raise NotImplementedError('structured_syslog_application_record_create is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_application_record_create

    def structured_syslog_application_record_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return structured-syslog-application-record information.
        
        :param fq_name: Fully qualified name of structured-syslog-application-record
        :param fq_name_str: Fully qualified name string of structured-syslog-application-record
        :param id: UUID of structured-syslog-application-record
        :param ifmap_id: IFMAP id of structured-syslog-application-record
        :returns: :class:`.StructuredSyslogApplicationRecord` object
        
        """
        raise NotImplementedError('structured_syslog_application_record_read is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_application_record_read

    def structured_syslog_application_record_update(self, obj):
        """Update structured-syslog-application-record.
        
        :param obj: :class:`.StructuredSyslogApplicationRecord` object
        
        """
        raise NotImplementedError('structured_syslog_application_record_update is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_application_record_update

    def structured_syslog_application_records_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all structured-syslog-application-records.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StructuredSyslogApplicationRecord` objects
        
        """
        raise NotImplementedError('structured_syslog_application_records_list is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_application_records_list

    def structured_syslog_application_record_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete structured-syslog-application-record from the system.
        
        :param fq_name: Fully qualified name of structured-syslog-application-record
        :param id: UUID of structured-syslog-application-record
        :param ifmap_id: IFMAP id of structured-syslog-application-record
        
        """
        raise NotImplementedError('structured_syslog_application_record_delete is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_application_record_delete

    def get_default_structured_syslog_application_record_id(self):
        """Return UUID of default structured-syslog-application-record."""
        raise NotImplementedError('get_default_structured_syslog_application_record_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_structured_syslog_application_record_delete

    def global_vrouter_config_create(self, obj):
        """Create new global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError('global_vrouter_config_create is %s\'s responsibility' % (str(type (self))))
    # end global_vrouter_config_create

    def global_vrouter_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-vrouter-config information.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param fq_name_str: Fully qualified name string of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        :returns: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError('global_vrouter_config_read is %s\'s responsibility' % (str(type (self))))
    # end global_vrouter_config_read

    def global_vrouter_config_update(self, obj):
        """Update global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError('global_vrouter_config_update is %s\'s responsibility' % (str(type (self))))
    # end global_vrouter_config_update

    def global_vrouter_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-vrouter-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalVrouterConfig` objects
        
        """
        raise NotImplementedError('global_vrouter_configs_list is %s\'s responsibility' % (str(type (self))))
    # end global_vrouter_configs_list

    def global_vrouter_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-vrouter-config from the system.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        
        """
        raise NotImplementedError('global_vrouter_config_delete is %s\'s responsibility' % (str(type (self))))
    # end global_vrouter_config_delete

    def get_default_global_vrouter_config_id(self):
        """Return UUID of default global-vrouter-config."""
        raise NotImplementedError('get_default_global_vrouter_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_global_vrouter_config_delete

    def floating_ip_create(self, obj):
        """Create new floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError('floating_ip_create is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_create

    def floating_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return floating-ip information.
        
        :param fq_name: Fully qualified name of floating-ip
        :param fq_name_str: Fully qualified name string of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        :returns: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError('floating_ip_read is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_read

    def floating_ip_update(self, obj):
        """Update floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError('floating_ip_update is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_update

    def floating_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all floating-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIp` objects
        
        """
        raise NotImplementedError('floating_ips_list is %s\'s responsibility' % (str(type (self))))
    # end floating_ips_list

    def floating_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip from the system.
        
        :param fq_name: Fully qualified name of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        
        """
        raise NotImplementedError('floating_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end floating_ip_delete

    def get_default_floating_ip_id(self):
        """Return UUID of default floating-ip."""
        raise NotImplementedError('get_default_floating_ip_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_floating_ip_delete

    def link_aggregation_group_create(self, obj):
        """Create new link-aggregation-group.
        
        :param obj: :class:`.LinkAggregationGroup` object
        
        """
        raise NotImplementedError('link_aggregation_group_create is %s\'s responsibility' % (str(type (self))))
    # end link_aggregation_group_create

    def link_aggregation_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return link-aggregation-group information.
        
        :param fq_name: Fully qualified name of link-aggregation-group
        :param fq_name_str: Fully qualified name string of link-aggregation-group
        :param id: UUID of link-aggregation-group
        :param ifmap_id: IFMAP id of link-aggregation-group
        :returns: :class:`.LinkAggregationGroup` object
        
        """
        raise NotImplementedError('link_aggregation_group_read is %s\'s responsibility' % (str(type (self))))
    # end link_aggregation_group_read

    def link_aggregation_group_update(self, obj):
        """Update link-aggregation-group.
        
        :param obj: :class:`.LinkAggregationGroup` object
        
        """
        raise NotImplementedError('link_aggregation_group_update is %s\'s responsibility' % (str(type (self))))
    # end link_aggregation_group_update

    def link_aggregation_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all link-aggregation-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LinkAggregationGroup` objects
        
        """
        raise NotImplementedError('link_aggregation_groups_list is %s\'s responsibility' % (str(type (self))))
    # end link_aggregation_groups_list

    def link_aggregation_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete link-aggregation-group from the system.
        
        :param fq_name: Fully qualified name of link-aggregation-group
        :param id: UUID of link-aggregation-group
        :param ifmap_id: IFMAP id of link-aggregation-group
        
        """
        raise NotImplementedError('link_aggregation_group_delete is %s\'s responsibility' % (str(type (self))))
    # end link_aggregation_group_delete

    def get_default_link_aggregation_group_id(self):
        """Return UUID of default link-aggregation-group."""
        raise NotImplementedError('get_default_link_aggregation_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_link_aggregation_group_delete

    def virtual_router_create(self, obj):
        """Create new virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError('virtual_router_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_router_create

    def virtual_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-router information.
        
        :param fq_name: Fully qualified name of virtual-router
        :param fq_name_str: Fully qualified name string of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        :returns: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError('virtual_router_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_router_read

    def virtual_router_update(self, obj):
        """Update virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError('virtual_router_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_router_update

    def virtual_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualRouter` objects
        
        """
        raise NotImplementedError('virtual_routers_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_routers_list

    def virtual_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-router from the system.
        
        :param fq_name: Fully qualified name of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        
        """
        raise NotImplementedError('virtual_router_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_router_delete

    def get_default_virtual_router_id(self):
        """Return UUID of default virtual-router."""
        raise NotImplementedError('get_default_virtual_router_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_router_delete

    def port_profile_create(self, obj):
        """Create new port-profile.
        
        :param obj: :class:`.PortProfile` object
        
        """
        raise NotImplementedError('port_profile_create is %s\'s responsibility' % (str(type (self))))
    # end port_profile_create

    def port_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return port-profile information.
        
        :param fq_name: Fully qualified name of port-profile
        :param fq_name_str: Fully qualified name string of port-profile
        :param id: UUID of port-profile
        :param ifmap_id: IFMAP id of port-profile
        :returns: :class:`.PortProfile` object
        
        """
        raise NotImplementedError('port_profile_read is %s\'s responsibility' % (str(type (self))))
    # end port_profile_read

    def port_profile_update(self, obj):
        """Update port-profile.
        
        :param obj: :class:`.PortProfile` object
        
        """
        raise NotImplementedError('port_profile_update is %s\'s responsibility' % (str(type (self))))
    # end port_profile_update

    def port_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all port-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PortProfile` objects
        
        """
        raise NotImplementedError('port_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end port_profiles_list

    def port_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete port-profile from the system.
        
        :param fq_name: Fully qualified name of port-profile
        :param id: UUID of port-profile
        :param ifmap_id: IFMAP id of port-profile
        
        """
        raise NotImplementedError('port_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end port_profile_delete

    def get_default_port_profile_id(self):
        """Return UUID of default port-profile."""
        raise NotImplementedError('get_default_port_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_port_profile_delete

    def policy_management_create(self, obj):
        """Create new policy-management.
        
        :param obj: :class:`.PolicyManagement` object
        
        """
        raise NotImplementedError('policy_management_create is %s\'s responsibility' % (str(type (self))))
    # end policy_management_create

    def policy_management_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return policy-management information.
        
        :param fq_name: Fully qualified name of policy-management
        :param fq_name_str: Fully qualified name string of policy-management
        :param id: UUID of policy-management
        :param ifmap_id: IFMAP id of policy-management
        :returns: :class:`.PolicyManagement` object
        
        """
        raise NotImplementedError('policy_management_read is %s\'s responsibility' % (str(type (self))))
    # end policy_management_read

    def policy_management_update(self, obj):
        """Update policy-management.
        
        :param obj: :class:`.PolicyManagement` object
        
        """
        raise NotImplementedError('policy_management_update is %s\'s responsibility' % (str(type (self))))
    # end policy_management_update

    def policy_managements_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all policy-managements.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PolicyManagement` objects
        
        """
        raise NotImplementedError('policy_managements_list is %s\'s responsibility' % (str(type (self))))
    # end policy_managements_list

    def policy_management_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete policy-management from the system.
        
        :param fq_name: Fully qualified name of policy-management
        :param id: UUID of policy-management
        :param ifmap_id: IFMAP id of policy-management
        
        """
        raise NotImplementedError('policy_management_delete is %s\'s responsibility' % (str(type (self))))
    # end policy_management_delete

    def get_default_policy_management_id(self):
        """Return UUID of default policy-management."""
        raise NotImplementedError('get_default_policy_management_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_policy_management_delete

    def e2_service_provider_create(self, obj):
        """Create new e2-service-provider.
        
        :param obj: :class:`.E2ServiceProvider` object
        
        """
        raise NotImplementedError('e2_service_provider_create is %s\'s responsibility' % (str(type (self))))
    # end e2_service_provider_create

    def e2_service_provider_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return e2-service-provider information.
        
        :param fq_name: Fully qualified name of e2-service-provider
        :param fq_name_str: Fully qualified name string of e2-service-provider
        :param id: UUID of e2-service-provider
        :param ifmap_id: IFMAP id of e2-service-provider
        :returns: :class:`.E2ServiceProvider` object
        
        """
        raise NotImplementedError('e2_service_provider_read is %s\'s responsibility' % (str(type (self))))
    # end e2_service_provider_read

    def e2_service_provider_update(self, obj):
        """Update e2-service-provider.
        
        :param obj: :class:`.E2ServiceProvider` object
        
        """
        raise NotImplementedError('e2_service_provider_update is %s\'s responsibility' % (str(type (self))))
    # end e2_service_provider_update

    def e2_service_providers_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all e2-service-providers."""
        raise NotImplementedError('e2_service_providers_list is %s\'s responsibility' % (str(type (self))))
    # end e2_service_providers_list

    def e2_service_provider_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete e2-service-provider from the system.
        
        :param fq_name: Fully qualified name of e2-service-provider
        :param id: UUID of e2-service-provider
        :param ifmap_id: IFMAP id of e2-service-provider
        
        """
        raise NotImplementedError('e2_service_provider_delete is %s\'s responsibility' % (str(type (self))))
    # end e2_service_provider_delete

    def get_default_e2_service_provider_id(self):
        """Return UUID of default e2-service-provider."""
        raise NotImplementedError('get_default_e2_service_provider_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_e2_service_provider_delete

    def fabric_create(self, obj):
        """Create new fabric.
        
        :param obj: :class:`.Fabric` object
        
        """
        raise NotImplementedError('fabric_create is %s\'s responsibility' % (str(type (self))))
    # end fabric_create

    def fabric_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return fabric information.
        
        :param fq_name: Fully qualified name of fabric
        :param fq_name_str: Fully qualified name string of fabric
        :param id: UUID of fabric
        :param ifmap_id: IFMAP id of fabric
        :returns: :class:`.Fabric` object
        
        """
        raise NotImplementedError('fabric_read is %s\'s responsibility' % (str(type (self))))
    # end fabric_read

    def fabric_update(self, obj):
        """Update fabric.
        
        :param obj: :class:`.Fabric` object
        
        """
        raise NotImplementedError('fabric_update is %s\'s responsibility' % (str(type (self))))
    # end fabric_update

    def fabrics_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all fabrics.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Fabric` objects
        
        """
        raise NotImplementedError('fabrics_list is %s\'s responsibility' % (str(type (self))))
    # end fabrics_list

    def fabric_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete fabric from the system.
        
        :param fq_name: Fully qualified name of fabric
        :param id: UUID of fabric
        :param ifmap_id: IFMAP id of fabric
        
        """
        raise NotImplementedError('fabric_delete is %s\'s responsibility' % (str(type (self))))
    # end fabric_delete

    def get_default_fabric_id(self):
        """Return UUID of default fabric."""
        raise NotImplementedError('get_default_fabric_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_fabric_delete

    def job_template_create(self, obj):
        """Create new job-template.
        
        :param obj: :class:`.JobTemplate` object
        
        """
        raise NotImplementedError('job_template_create is %s\'s responsibility' % (str(type (self))))
    # end job_template_create

    def job_template_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return job-template information.
        
        :param fq_name: Fully qualified name of job-template
        :param fq_name_str: Fully qualified name string of job-template
        :param id: UUID of job-template
        :param ifmap_id: IFMAP id of job-template
        :returns: :class:`.JobTemplate` object
        
        """
        raise NotImplementedError('job_template_read is %s\'s responsibility' % (str(type (self))))
    # end job_template_read

    def job_template_update(self, obj):
        """Update job-template.
        
        :param obj: :class:`.JobTemplate` object
        
        """
        raise NotImplementedError('job_template_update is %s\'s responsibility' % (str(type (self))))
    # end job_template_update

    def job_templates_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all job-templates.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.JobTemplate` objects
        
        """
        raise NotImplementedError('job_templates_list is %s\'s responsibility' % (str(type (self))))
    # end job_templates_list

    def job_template_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete job-template from the system.
        
        :param fq_name: Fully qualified name of job-template
        :param id: UUID of job-template
        :param ifmap_id: IFMAP id of job-template
        
        """
        raise NotImplementedError('job_template_delete is %s\'s responsibility' % (str(type (self))))
    # end job_template_delete

    def get_default_job_template_id(self):
        """Return UUID of default job-template."""
        raise NotImplementedError('get_default_job_template_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_job_template_delete

    def routing_policy_create(self, obj):
        """Create new routing-policy.
        
        :param obj: :class:`.RoutingPolicy` object
        
        """
        raise NotImplementedError('routing_policy_create is %s\'s responsibility' % (str(type (self))))
    # end routing_policy_create

    def routing_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return routing-policy information.
        
        :param fq_name: Fully qualified name of routing-policy
        :param fq_name_str: Fully qualified name string of routing-policy
        :param id: UUID of routing-policy
        :param ifmap_id: IFMAP id of routing-policy
        :returns: :class:`.RoutingPolicy` object
        
        """
        raise NotImplementedError('routing_policy_read is %s\'s responsibility' % (str(type (self))))
    # end routing_policy_read

    def routing_policy_update(self, obj):
        """Update routing-policy.
        
        :param obj: :class:`.RoutingPolicy` object
        
        """
        raise NotImplementedError('routing_policy_update is %s\'s responsibility' % (str(type (self))))
    # end routing_policy_update

    def routing_policys_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all routing-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoutingPolicy` objects
        
        """
        raise NotImplementedError('routing_policys_list is %s\'s responsibility' % (str(type (self))))
    # end routing_policys_list

    def routing_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete routing-policy from the system.
        
        :param fq_name: Fully qualified name of routing-policy
        :param id: UUID of routing-policy
        :param ifmap_id: IFMAP id of routing-policy
        
        """
        raise NotImplementedError('routing_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end routing_policy_delete

    def get_default_routing_policy_id(self):
        """Return UUID of default routing-policy."""
        raise NotImplementedError('get_default_routing_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_routing_policy_delete

    def role_config_create(self, obj):
        """Create new role-config.
        
        :param obj: :class:`.RoleConfig` object
        
        """
        raise NotImplementedError('role_config_create is %s\'s responsibility' % (str(type (self))))
    # end role_config_create

    def role_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return role-config information.
        
        :param fq_name: Fully qualified name of role-config
        :param fq_name_str: Fully qualified name string of role-config
        :param id: UUID of role-config
        :param ifmap_id: IFMAP id of role-config
        :returns: :class:`.RoleConfig` object
        
        """
        raise NotImplementedError('role_config_read is %s\'s responsibility' % (str(type (self))))
    # end role_config_read

    def role_config_update(self, obj):
        """Update role-config.
        
        :param obj: :class:`.RoleConfig` object
        
        """
        raise NotImplementedError('role_config_update is %s\'s responsibility' % (str(type (self))))
    # end role_config_update

    def role_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all role-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoleConfig` objects
        
        """
        raise NotImplementedError('role_configs_list is %s\'s responsibility' % (str(type (self))))
    # end role_configs_list

    def role_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete role-config from the system.
        
        :param fq_name: Fully qualified name of role-config
        :param id: UUID of role-config
        :param ifmap_id: IFMAP id of role-config
        
        """
        raise NotImplementedError('role_config_delete is %s\'s responsibility' % (str(type (self))))
    # end role_config_delete

    def get_default_role_config_id(self):
        """Return UUID of default role-config."""
        raise NotImplementedError('get_default_role_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_role_config_delete

    def tag_type_create(self, obj):
        """Create new tag-type.
        
        :param obj: :class:`.TagType` object
        
        """
        raise NotImplementedError('tag_type_create is %s\'s responsibility' % (str(type (self))))
    # end tag_type_create

    def tag_type_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return tag-type information.
        
        :param fq_name: Fully qualified name of tag-type
        :param fq_name_str: Fully qualified name string of tag-type
        :param id: UUID of tag-type
        :param ifmap_id: IFMAP id of tag-type
        :returns: :class:`.TagType` object
        
        """
        raise NotImplementedError('tag_type_read is %s\'s responsibility' % (str(type (self))))
    # end tag_type_read

    def tag_type_update(self, obj):
        """Update tag-type.
        
        :param obj: :class:`.TagType` object
        
        """
        raise NotImplementedError('tag_type_update is %s\'s responsibility' % (str(type (self))))
    # end tag_type_update

    def tag_types_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all tag-types."""
        raise NotImplementedError('tag_types_list is %s\'s responsibility' % (str(type (self))))
    # end tag_types_list

    def tag_type_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete tag-type from the system.
        
        :param fq_name: Fully qualified name of tag-type
        :param id: UUID of tag-type
        :param ifmap_id: IFMAP id of tag-type
        
        """
        raise NotImplementedError('tag_type_delete is %s\'s responsibility' % (str(type (self))))
    # end tag_type_delete

    def get_default_tag_type_id(self):
        """Return UUID of default tag-type."""
        raise NotImplementedError('get_default_tag_type_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_tag_type_delete

    def structured_syslog_message_create(self, obj):
        """Create new structured-syslog-message.
        
        :param obj: :class:`.StructuredSyslogMessage` object
        
        """
        raise NotImplementedError('structured_syslog_message_create is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_message_create

    def structured_syslog_message_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return structured-syslog-message information.
        
        :param fq_name: Fully qualified name of structured-syslog-message
        :param fq_name_str: Fully qualified name string of structured-syslog-message
        :param id: UUID of structured-syslog-message
        :param ifmap_id: IFMAP id of structured-syslog-message
        :returns: :class:`.StructuredSyslogMessage` object
        
        """
        raise NotImplementedError('structured_syslog_message_read is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_message_read

    def structured_syslog_message_update(self, obj):
        """Update structured-syslog-message.
        
        :param obj: :class:`.StructuredSyslogMessage` object
        
        """
        raise NotImplementedError('structured_syslog_message_update is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_message_update

    def structured_syslog_messages_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all structured-syslog-messages.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StructuredSyslogMessage` objects
        
        """
        raise NotImplementedError('structured_syslog_messages_list is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_messages_list

    def structured_syslog_message_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete structured-syslog-message from the system.
        
        :param fq_name: Fully qualified name of structured-syslog-message
        :param id: UUID of structured-syslog-message
        :param ifmap_id: IFMAP id of structured-syslog-message
        
        """
        raise NotImplementedError('structured_syslog_message_delete is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_message_delete

    def get_default_structured_syslog_message_id(self):
        """Return UUID of default structured-syslog-message."""
        raise NotImplementedError('get_default_structured_syslog_message_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_structured_syslog_message_delete

    def loadbalancer_pool_create(self, obj):
        """Create new loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError('loadbalancer_pool_create is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_pool_create

    def loadbalancer_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-pool information.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param fq_name_str: Fully qualified name string of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        :returns: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError('loadbalancer_pool_read is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_pool_read

    def loadbalancer_pool_update(self, obj):
        """Update loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError('loadbalancer_pool_update is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_pool_update

    def loadbalancer_pools_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerPool` objects
        
        """
        raise NotImplementedError('loadbalancer_pools_list is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_pools_list

    def loadbalancer_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-pool from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        
        """
        raise NotImplementedError('loadbalancer_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_pool_delete

    def get_default_loadbalancer_pool_id(self):
        """Return UUID of default loadbalancer-pool."""
        raise NotImplementedError('get_default_loadbalancer_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_loadbalancer_pool_delete

    def device_chassis_create(self, obj):
        """Create new device-chassis.
        
        :param obj: :class:`.DeviceChassis` object
        
        """
        raise NotImplementedError('device_chassis_create is %s\'s responsibility' % (str(type (self))))
    # end device_chassis_create

    def device_chassis_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return device-chassis information.
        
        :param fq_name: Fully qualified name of device-chassis
        :param fq_name_str: Fully qualified name string of device-chassis
        :param id: UUID of device-chassis
        :param ifmap_id: IFMAP id of device-chassis
        :returns: :class:`.DeviceChassis` object
        
        """
        raise NotImplementedError('device_chassis_read is %s\'s responsibility' % (str(type (self))))
    # end device_chassis_read

    def device_chassis_update(self, obj):
        """Update device-chassis.
        
        :param obj: :class:`.DeviceChassis` object
        
        """
        raise NotImplementedError('device_chassis_update is %s\'s responsibility' % (str(type (self))))
    # end device_chassis_update

    def device_chassiss_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all device-chassiss."""
        raise NotImplementedError('device_chassiss_list is %s\'s responsibility' % (str(type (self))))
    # end device_chassiss_list

    def device_chassis_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete device-chassis from the system.
        
        :param fq_name: Fully qualified name of device-chassis
        :param id: UUID of device-chassis
        :param ifmap_id: IFMAP id of device-chassis
        
        """
        raise NotImplementedError('device_chassis_delete is %s\'s responsibility' % (str(type (self))))
    # end device_chassis_delete

    def get_default_device_chassis_id(self):
        """Return UUID of default device-chassis."""
        raise NotImplementedError('get_default_device_chassis_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_device_chassis_delete

    def global_qos_config_create(self, obj):
        """Create new global-qos-config.
        
        :param obj: :class:`.GlobalQosConfig` object
        
        """
        raise NotImplementedError('global_qos_config_create is %s\'s responsibility' % (str(type (self))))
    # end global_qos_config_create

    def global_qos_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-qos-config information.
        
        :param fq_name: Fully qualified name of global-qos-config
        :param fq_name_str: Fully qualified name string of global-qos-config
        :param id: UUID of global-qos-config
        :param ifmap_id: IFMAP id of global-qos-config
        :returns: :class:`.GlobalQosConfig` object
        
        """
        raise NotImplementedError('global_qos_config_read is %s\'s responsibility' % (str(type (self))))
    # end global_qos_config_read

    def global_qos_config_update(self, obj):
        """Update global-qos-config.
        
        :param obj: :class:`.GlobalQosConfig` object
        
        """
        raise NotImplementedError('global_qos_config_update is %s\'s responsibility' % (str(type (self))))
    # end global_qos_config_update

    def global_qos_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-qos-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalQosConfig` objects
        
        """
        raise NotImplementedError('global_qos_configs_list is %s\'s responsibility' % (str(type (self))))
    # end global_qos_configs_list

    def global_qos_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-qos-config from the system.
        
        :param fq_name: Fully qualified name of global-qos-config
        :param id: UUID of global-qos-config
        :param ifmap_id: IFMAP id of global-qos-config
        
        """
        raise NotImplementedError('global_qos_config_delete is %s\'s responsibility' % (str(type (self))))
    # end global_qos_config_delete

    def get_default_global_qos_config_id(self):
        """Return UUID of default global-qos-config."""
        raise NotImplementedError('get_default_global_qos_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_global_qos_config_delete

    def analytics_node_create(self, obj):
        """Create new analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError('analytics_node_create is %s\'s responsibility' % (str(type (self))))
    # end analytics_node_create

    def analytics_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return analytics-node information.
        
        :param fq_name: Fully qualified name of analytics-node
        :param fq_name_str: Fully qualified name string of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        :returns: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError('analytics_node_read is %s\'s responsibility' % (str(type (self))))
    # end analytics_node_read

    def analytics_node_update(self, obj):
        """Update analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError('analytics_node_update is %s\'s responsibility' % (str(type (self))))
    # end analytics_node_update

    def analytics_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all analytics-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AnalyticsNode` objects
        
        """
        raise NotImplementedError('analytics_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end analytics_nodes_list

    def analytics_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete analytics-node from the system.
        
        :param fq_name: Fully qualified name of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        
        """
        raise NotImplementedError('analytics_node_delete is %s\'s responsibility' % (str(type (self))))
    # end analytics_node_delete

    def get_default_analytics_node_id(self):
        """Return UUID of default analytics-node."""
        raise NotImplementedError('get_default_analytics_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_analytics_node_delete

    def virtual_DNS_create(self, obj):
        """Create new virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError('virtual_DNS_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_create

    def virtual_DNS_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-DNS information.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param fq_name_str: Fully qualified name string of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        :returns: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError('virtual_DNS_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_read

    def virtual_DNS_update(self, obj):
        """Update virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError('virtual_DNS_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_update

    def virtual_DNSs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-DNSs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDns` objects
        
        """
        raise NotImplementedError('virtual_DNSs_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNSs_list

    def virtual_DNS_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        
        """
        raise NotImplementedError('virtual_DNS_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_DNS_delete

    def get_default_virtual_DNS_id(self):
        """Return UUID of default virtual-DNS."""
        raise NotImplementedError('get_default_virtual_DNS_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_DNS_delete

    def config_database_node_create(self, obj):
        """Create new config-database-node.
        
        :param obj: :class:`.ConfigDatabaseNode` object
        
        """
        raise NotImplementedError('config_database_node_create is %s\'s responsibility' % (str(type (self))))
    # end config_database_node_create

    def config_database_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return config-database-node information.
        
        :param fq_name: Fully qualified name of config-database-node
        :param fq_name_str: Fully qualified name string of config-database-node
        :param id: UUID of config-database-node
        :param ifmap_id: IFMAP id of config-database-node
        :returns: :class:`.ConfigDatabaseNode` object
        
        """
        raise NotImplementedError('config_database_node_read is %s\'s responsibility' % (str(type (self))))
    # end config_database_node_read

    def config_database_node_update(self, obj):
        """Update config-database-node.
        
        :param obj: :class:`.ConfigDatabaseNode` object
        
        """
        raise NotImplementedError('config_database_node_update is %s\'s responsibility' % (str(type (self))))
    # end config_database_node_update

    def config_database_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all config-database-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ConfigDatabaseNode` objects
        
        """
        raise NotImplementedError('config_database_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end config_database_nodes_list

    def config_database_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-database-node from the system.
        
        :param fq_name: Fully qualified name of config-database-node
        :param id: UUID of config-database-node
        :param ifmap_id: IFMAP id of config-database-node
        
        """
        raise NotImplementedError('config_database_node_delete is %s\'s responsibility' % (str(type (self))))
    # end config_database_node_delete

    def get_default_config_database_node_id(self):
        """Return UUID of default config-database-node."""
        raise NotImplementedError('get_default_config_database_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_config_database_node_delete

    def config_node_create(self, obj):
        """Create new config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError('config_node_create is %s\'s responsibility' % (str(type (self))))
    # end config_node_create

    def config_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return config-node information.
        
        :param fq_name: Fully qualified name of config-node
        :param fq_name_str: Fully qualified name string of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        :returns: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError('config_node_read is %s\'s responsibility' % (str(type (self))))
    # end config_node_read

    def config_node_update(self, obj):
        """Update config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError('config_node_update is %s\'s responsibility' % (str(type (self))))
    # end config_node_update

    def config_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all config-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ConfigNode` objects
        
        """
        raise NotImplementedError('config_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end config_nodes_list

    def config_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-node from the system.
        
        :param fq_name: Fully qualified name of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        
        """
        raise NotImplementedError('config_node_delete is %s\'s responsibility' % (str(type (self))))
    # end config_node_delete

    def get_default_config_node_id(self):
        """Return UUID of default config-node."""
        raise NotImplementedError('get_default_config_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_config_node_delete

    def device_functional_group_create(self, obj):
        """Create new device-functional-group.
        
        :param obj: :class:`.DeviceFunctionalGroup` object
        
        """
        raise NotImplementedError('device_functional_group_create is %s\'s responsibility' % (str(type (self))))
    # end device_functional_group_create

    def device_functional_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return device-functional-group information.
        
        :param fq_name: Fully qualified name of device-functional-group
        :param fq_name_str: Fully qualified name string of device-functional-group
        :param id: UUID of device-functional-group
        :param ifmap_id: IFMAP id of device-functional-group
        :returns: :class:`.DeviceFunctionalGroup` object
        
        """
        raise NotImplementedError('device_functional_group_read is %s\'s responsibility' % (str(type (self))))
    # end device_functional_group_read

    def device_functional_group_update(self, obj):
        """Update device-functional-group.
        
        :param obj: :class:`.DeviceFunctionalGroup` object
        
        """
        raise NotImplementedError('device_functional_group_update is %s\'s responsibility' % (str(type (self))))
    # end device_functional_group_update

    def device_functional_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all device-functional-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DeviceFunctionalGroup` objects
        
        """
        raise NotImplementedError('device_functional_groups_list is %s\'s responsibility' % (str(type (self))))
    # end device_functional_groups_list

    def device_functional_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete device-functional-group from the system.
        
        :param fq_name: Fully qualified name of device-functional-group
        :param id: UUID of device-functional-group
        :param ifmap_id: IFMAP id of device-functional-group
        
        """
        raise NotImplementedError('device_functional_group_delete is %s\'s responsibility' % (str(type (self))))
    # end device_functional_group_delete

    def get_default_device_functional_group_id(self):
        """Return UUID of default device-functional-group."""
        raise NotImplementedError('get_default_device_functional_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_device_functional_group_delete

    def firewall_rule_create(self, obj):
        """Create new firewall-rule.
        
        :param obj: :class:`.FirewallRule` object
        
        """
        raise NotImplementedError('firewall_rule_create is %s\'s responsibility' % (str(type (self))))
    # end firewall_rule_create

    def firewall_rule_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return firewall-rule information.
        
        :param fq_name: Fully qualified name of firewall-rule
        :param fq_name_str: Fully qualified name string of firewall-rule
        :param id: UUID of firewall-rule
        :param ifmap_id: IFMAP id of firewall-rule
        :returns: :class:`.FirewallRule` object
        
        """
        raise NotImplementedError('firewall_rule_read is %s\'s responsibility' % (str(type (self))))
    # end firewall_rule_read

    def firewall_rule_update(self, obj):
        """Update firewall-rule.
        
        :param obj: :class:`.FirewallRule` object
        
        """
        raise NotImplementedError('firewall_rule_update is %s\'s responsibility' % (str(type (self))))
    # end firewall_rule_update

    def firewall_rules_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all firewall-rules.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FirewallRule` objects
        
        """
        raise NotImplementedError('firewall_rules_list is %s\'s responsibility' % (str(type (self))))
    # end firewall_rules_list

    def firewall_rule_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete firewall-rule from the system.
        
        :param fq_name: Fully qualified name of firewall-rule
        :param id: UUID of firewall-rule
        :param ifmap_id: IFMAP id of firewall-rule
        
        """
        raise NotImplementedError('firewall_rule_delete is %s\'s responsibility' % (str(type (self))))
    # end firewall_rule_delete

    def get_default_firewall_rule_id(self):
        """Return UUID of default firewall-rule."""
        raise NotImplementedError('get_default_firewall_rule_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_firewall_rule_delete

    def bgpvpn_create(self, obj):
        """Create new bgpvpn.
        
        :param obj: :class:`.Bgpvpn` object
        
        """
        raise NotImplementedError('bgpvpn_create is %s\'s responsibility' % (str(type (self))))
    # end bgpvpn_create

    def bgpvpn_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return bgpvpn information.
        
        :param fq_name: Fully qualified name of bgpvpn
        :param fq_name_str: Fully qualified name string of bgpvpn
        :param id: UUID of bgpvpn
        :param ifmap_id: IFMAP id of bgpvpn
        :returns: :class:`.Bgpvpn` object
        
        """
        raise NotImplementedError('bgpvpn_read is %s\'s responsibility' % (str(type (self))))
    # end bgpvpn_read

    def bgpvpn_update(self, obj):
        """Update bgpvpn.
        
        :param obj: :class:`.Bgpvpn` object
        
        """
        raise NotImplementedError('bgpvpn_update is %s\'s responsibility' % (str(type (self))))
    # end bgpvpn_update

    def bgpvpns_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all bgpvpns.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Bgpvpn` objects
        
        """
        raise NotImplementedError('bgpvpns_list is %s\'s responsibility' % (str(type (self))))
    # end bgpvpns_list

    def bgpvpn_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bgpvpn from the system.
        
        :param fq_name: Fully qualified name of bgpvpn
        :param id: UUID of bgpvpn
        :param ifmap_id: IFMAP id of bgpvpn
        
        """
        raise NotImplementedError('bgpvpn_delete is %s\'s responsibility' % (str(type (self))))
    # end bgpvpn_delete

    def get_default_bgpvpn_id(self):
        """Return UUID of default bgpvpn."""
        raise NotImplementedError('get_default_bgpvpn_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_bgpvpn_delete

    def role_definition_create(self, obj):
        """Create new role-definition.
        
        :param obj: :class:`.RoleDefinition` object
        
        """
        raise NotImplementedError('role_definition_create is %s\'s responsibility' % (str(type (self))))
    # end role_definition_create

    def role_definition_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return role-definition information.
        
        :param fq_name: Fully qualified name of role-definition
        :param fq_name_str: Fully qualified name string of role-definition
        :param id: UUID of role-definition
        :param ifmap_id: IFMAP id of role-definition
        :returns: :class:`.RoleDefinition` object
        
        """
        raise NotImplementedError('role_definition_read is %s\'s responsibility' % (str(type (self))))
    # end role_definition_read

    def role_definition_update(self, obj):
        """Update role-definition.
        
        :param obj: :class:`.RoleDefinition` object
        
        """
        raise NotImplementedError('role_definition_update is %s\'s responsibility' % (str(type (self))))
    # end role_definition_update

    def role_definitions_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all role-definitions.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoleDefinition` objects
        
        """
        raise NotImplementedError('role_definitions_list is %s\'s responsibility' % (str(type (self))))
    # end role_definitions_list

    def role_definition_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete role-definition from the system.
        
        :param fq_name: Fully qualified name of role-definition
        :param id: UUID of role-definition
        :param ifmap_id: IFMAP id of role-definition
        
        """
        raise NotImplementedError('role_definition_delete is %s\'s responsibility' % (str(type (self))))
    # end role_definition_delete

    def get_default_role_definition_id(self):
        """Return UUID of default role-definition."""
        raise NotImplementedError('get_default_role_definition_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_role_definition_delete

    def service_connection_module_create(self, obj):
        """Create new service-connection-module.
        
        :param obj: :class:`.ServiceConnectionModule` object
        
        """
        raise NotImplementedError('service_connection_module_create is %s\'s responsibility' % (str(type (self))))
    # end service_connection_module_create

    def service_connection_module_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-connection-module information.
        
        :param fq_name: Fully qualified name of service-connection-module
        :param fq_name_str: Fully qualified name string of service-connection-module
        :param id: UUID of service-connection-module
        :param ifmap_id: IFMAP id of service-connection-module
        :returns: :class:`.ServiceConnectionModule` object
        
        """
        raise NotImplementedError('service_connection_module_read is %s\'s responsibility' % (str(type (self))))
    # end service_connection_module_read

    def service_connection_module_update(self, obj):
        """Update service-connection-module.
        
        :param obj: :class:`.ServiceConnectionModule` object
        
        """
        raise NotImplementedError('service_connection_module_update is %s\'s responsibility' % (str(type (self))))
    # end service_connection_module_update

    def service_connection_modules_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-connection-modules."""
        raise NotImplementedError('service_connection_modules_list is %s\'s responsibility' % (str(type (self))))
    # end service_connection_modules_list

    def service_connection_module_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-connection-module from the system.
        
        :param fq_name: Fully qualified name of service-connection-module
        :param id: UUID of service-connection-module
        :param ifmap_id: IFMAP id of service-connection-module
        
        """
        raise NotImplementedError('service_connection_module_delete is %s\'s responsibility' % (str(type (self))))
    # end service_connection_module_delete

    def get_default_service_connection_module_id(self):
        """Return UUID of default service-connection-module."""
        raise NotImplementedError('get_default_service_connection_module_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_connection_module_delete

    def security_group_create(self, obj):
        """Create new security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError('security_group_create is %s\'s responsibility' % (str(type (self))))
    # end security_group_create

    def security_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return security-group information.
        
        :param fq_name: Fully qualified name of security-group
        :param fq_name_str: Fully qualified name string of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        :returns: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError('security_group_read is %s\'s responsibility' % (str(type (self))))
    # end security_group_read

    def security_group_update(self, obj):
        """Update security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError('security_group_update is %s\'s responsibility' % (str(type (self))))
    # end security_group_update

    def security_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all security-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.SecurityGroup` objects
        
        """
        raise NotImplementedError('security_groups_list is %s\'s responsibility' % (str(type (self))))
    # end security_groups_list

    def security_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete security-group from the system.
        
        :param fq_name: Fully qualified name of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        
        """
        raise NotImplementedError('security_group_delete is %s\'s responsibility' % (str(type (self))))
    # end security_group_delete

    def get_default_security_group_id(self):
        """Return UUID of default security-group."""
        raise NotImplementedError('get_default_security_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_security_group_delete

    def database_node_create(self, obj):
        """Create new database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError('database_node_create is %s\'s responsibility' % (str(type (self))))
    # end database_node_create

    def database_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return database-node information.
        
        :param fq_name: Fully qualified name of database-node
        :param fq_name_str: Fully qualified name string of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        :returns: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError('database_node_read is %s\'s responsibility' % (str(type (self))))
    # end database_node_read

    def database_node_update(self, obj):
        """Update database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError('database_node_update is %s\'s responsibility' % (str(type (self))))
    # end database_node_update

    def database_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all database-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DatabaseNode` objects
        
        """
        raise NotImplementedError('database_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end database_nodes_list

    def database_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete database-node from the system.
        
        :param fq_name: Fully qualified name of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        
        """
        raise NotImplementedError('database_node_delete is %s\'s responsibility' % (str(type (self))))
    # end database_node_delete

    def get_default_database_node_id(self):
        """Return UUID of default database-node."""
        raise NotImplementedError('get_default_database_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_database_node_delete

    def loadbalancer_healthmonitor_create(self, obj):
        """Create new loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError('loadbalancer_healthmonitor_create is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_healthmonitor_create

    def loadbalancer_healthmonitor_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-healthmonitor information.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param fq_name_str: Fully qualified name string of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        :returns: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError('loadbalancer_healthmonitor_read is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_healthmonitor_read

    def loadbalancer_healthmonitor_update(self, obj):
        """Update loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError('loadbalancer_healthmonitor_update is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_healthmonitor_update

    def loadbalancer_healthmonitors_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-healthmonitors.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerHealthmonitor` objects
        
        """
        raise NotImplementedError('loadbalancer_healthmonitors_list is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_healthmonitors_list

    def loadbalancer_healthmonitor_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-healthmonitor from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        
        """
        raise NotImplementedError('loadbalancer_healthmonitor_delete is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_healthmonitor_delete

    def get_default_loadbalancer_healthmonitor_id(self):
        """Return UUID of default loadbalancer-healthmonitor."""
        raise NotImplementedError('get_default_loadbalancer_healthmonitor_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_loadbalancer_healthmonitor_delete

    def devicemgr_node_create(self, obj):
        """Create new devicemgr-node.
        
        :param obj: :class:`.DevicemgrNode` object
        
        """
        raise NotImplementedError('devicemgr_node_create is %s\'s responsibility' % (str(type (self))))
    # end devicemgr_node_create

    def devicemgr_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return devicemgr-node information.
        
        :param fq_name: Fully qualified name of devicemgr-node
        :param fq_name_str: Fully qualified name string of devicemgr-node
        :param id: UUID of devicemgr-node
        :param ifmap_id: IFMAP id of devicemgr-node
        :returns: :class:`.DevicemgrNode` object
        
        """
        raise NotImplementedError('devicemgr_node_read is %s\'s responsibility' % (str(type (self))))
    # end devicemgr_node_read

    def devicemgr_node_update(self, obj):
        """Update devicemgr-node.
        
        :param obj: :class:`.DevicemgrNode` object
        
        """
        raise NotImplementedError('devicemgr_node_update is %s\'s responsibility' % (str(type (self))))
    # end devicemgr_node_update

    def devicemgr_nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all devicemgr-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DevicemgrNode` objects
        
        """
        raise NotImplementedError('devicemgr_nodes_list is %s\'s responsibility' % (str(type (self))))
    # end devicemgr_nodes_list

    def devicemgr_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete devicemgr-node from the system.
        
        :param fq_name: Fully qualified name of devicemgr-node
        :param id: UUID of devicemgr-node
        :param ifmap_id: IFMAP id of devicemgr-node
        
        """
        raise NotImplementedError('devicemgr_node_delete is %s\'s responsibility' % (str(type (self))))
    # end devicemgr_node_delete

    def get_default_devicemgr_node_id(self):
        """Return UUID of default devicemgr-node."""
        raise NotImplementedError('get_default_devicemgr_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_devicemgr_node_delete

    def project_create(self, obj):
        """Create new project.
        
        :param obj: :class:`.Project` object
        
        """
        raise NotImplementedError('project_create is %s\'s responsibility' % (str(type (self))))
    # end project_create

    def project_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return project information.
        
        :param fq_name: Fully qualified name of project
        :param fq_name_str: Fully qualified name string of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        :returns: :class:`.Project` object
        
        """
        raise NotImplementedError('project_read is %s\'s responsibility' % (str(type (self))))
    # end project_read

    def project_update(self, obj):
        """Update project.
        
        :param obj: :class:`.Project` object
        
        """
        raise NotImplementedError('project_update is %s\'s responsibility' % (str(type (self))))
    # end project_update

    def projects_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all projects.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Project` objects
        
        """
        raise NotImplementedError('projects_list is %s\'s responsibility' % (str(type (self))))
    # end projects_list

    def project_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete project from the system.
        
        :param fq_name: Fully qualified name of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        
        """
        raise NotImplementedError('project_delete is %s\'s responsibility' % (str(type (self))))
    # end project_delete

    def get_default_project_id(self):
        """Return UUID of default project."""
        raise NotImplementedError('get_default_project_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_project_delete

    def fabric_namespace_create(self, obj):
        """Create new fabric-namespace.
        
        :param obj: :class:`.FabricNamespace` object
        
        """
        raise NotImplementedError('fabric_namespace_create is %s\'s responsibility' % (str(type (self))))
    # end fabric_namespace_create

    def fabric_namespace_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return fabric-namespace information.
        
        :param fq_name: Fully qualified name of fabric-namespace
        :param fq_name_str: Fully qualified name string of fabric-namespace
        :param id: UUID of fabric-namespace
        :param ifmap_id: IFMAP id of fabric-namespace
        :returns: :class:`.FabricNamespace` object
        
        """
        raise NotImplementedError('fabric_namespace_read is %s\'s responsibility' % (str(type (self))))
    # end fabric_namespace_read

    def fabric_namespace_update(self, obj):
        """Update fabric-namespace.
        
        :param obj: :class:`.FabricNamespace` object
        
        """
        raise NotImplementedError('fabric_namespace_update is %s\'s responsibility' % (str(type (self))))
    # end fabric_namespace_update

    def fabric_namespaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all fabric-namespaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FabricNamespace` objects
        
        """
        raise NotImplementedError('fabric_namespaces_list is %s\'s responsibility' % (str(type (self))))
    # end fabric_namespaces_list

    def fabric_namespace_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete fabric-namespace from the system.
        
        :param fq_name: Fully qualified name of fabric-namespace
        :param id: UUID of fabric-namespace
        :param ifmap_id: IFMAP id of fabric-namespace
        
        """
        raise NotImplementedError('fabric_namespace_delete is %s\'s responsibility' % (str(type (self))))
    # end fabric_namespace_delete

    def get_default_fabric_namespace_id(self):
        """Return UUID of default fabric-namespace."""
        raise NotImplementedError('get_default_fabric_namespace_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_fabric_namespace_delete

    def network_ipam_create(self, obj):
        """Create new network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError('network_ipam_create is %s\'s responsibility' % (str(type (self))))
    # end network_ipam_create

    def network_ipam_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return network-ipam information.
        
        :param fq_name: Fully qualified name of network-ipam
        :param fq_name_str: Fully qualified name string of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        :returns: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError('network_ipam_read is %s\'s responsibility' % (str(type (self))))
    # end network_ipam_read

    def network_ipam_update(self, obj):
        """Update network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError('network_ipam_update is %s\'s responsibility' % (str(type (self))))
    # end network_ipam_update

    def network_ipams_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all network-ipams.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkIpam` objects
        
        """
        raise NotImplementedError('network_ipams_list is %s\'s responsibility' % (str(type (self))))
    # end network_ipams_list

    def network_ipam_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-ipam from the system.
        
        :param fq_name: Fully qualified name of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        
        """
        raise NotImplementedError('network_ipam_delete is %s\'s responsibility' % (str(type (self))))
    # end network_ipam_delete

    def get_default_network_ipam_id(self):
        """Return UUID of default network-ipam."""
        raise NotImplementedError('get_default_network_ipam_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_network_ipam_delete

    def network_policy_create(self, obj):
        """Create new network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError('network_policy_create is %s\'s responsibility' % (str(type (self))))
    # end network_policy_create

    def network_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return network-policy information.
        
        :param fq_name: Fully qualified name of network-policy
        :param fq_name_str: Fully qualified name string of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        :returns: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError('network_policy_read is %s\'s responsibility' % (str(type (self))))
    # end network_policy_read

    def network_policy_update(self, obj):
        """Update network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError('network_policy_update is %s\'s responsibility' % (str(type (self))))
    # end network_policy_update

    def network_policys_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all network-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkPolicy` objects
        
        """
        raise NotImplementedError('network_policys_list is %s\'s responsibility' % (str(type (self))))
    # end network_policys_list

    def network_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-policy from the system.
        
        :param fq_name: Fully qualified name of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        
        """
        raise NotImplementedError('network_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end network_policy_delete

    def get_default_network_policy_id(self):
        """Return UUID of default network-policy."""
        raise NotImplementedError('get_default_network_policy_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_network_policy_delete

    def sflow_profile_create(self, obj):
        """Create new sflow-profile.
        
        :param obj: :class:`.SflowProfile` object
        
        """
        raise NotImplementedError('sflow_profile_create is %s\'s responsibility' % (str(type (self))))
    # end sflow_profile_create

    def sflow_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return sflow-profile information.
        
        :param fq_name: Fully qualified name of sflow-profile
        :param fq_name_str: Fully qualified name string of sflow-profile
        :param id: UUID of sflow-profile
        :param ifmap_id: IFMAP id of sflow-profile
        :returns: :class:`.SflowProfile` object
        
        """
        raise NotImplementedError('sflow_profile_read is %s\'s responsibility' % (str(type (self))))
    # end sflow_profile_read

    def sflow_profile_update(self, obj):
        """Update sflow-profile.
        
        :param obj: :class:`.SflowProfile` object
        
        """
        raise NotImplementedError('sflow_profile_update is %s\'s responsibility' % (str(type (self))))
    # end sflow_profile_update

    def sflow_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all sflow-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.SflowProfile` objects
        
        """
        raise NotImplementedError('sflow_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end sflow_profiles_list

    def sflow_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete sflow-profile from the system.
        
        :param fq_name: Fully qualified name of sflow-profile
        :param id: UUID of sflow-profile
        :param ifmap_id: IFMAP id of sflow-profile
        
        """
        raise NotImplementedError('sflow_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end sflow_profile_delete

    def get_default_sflow_profile_id(self):
        """Return UUID of default sflow-profile."""
        raise NotImplementedError('get_default_sflow_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_sflow_profile_delete

    def hardware_create(self, obj):
        """Create new hardware.
        
        :param obj: :class:`.Hardware` object
        
        """
        raise NotImplementedError('hardware_create is %s\'s responsibility' % (str(type (self))))
    # end hardware_create

    def hardware_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return hardware information.
        
        :param fq_name: Fully qualified name of hardware
        :param fq_name_str: Fully qualified name string of hardware
        :param id: UUID of hardware
        :param ifmap_id: IFMAP id of hardware
        :returns: :class:`.Hardware` object
        
        """
        raise NotImplementedError('hardware_read is %s\'s responsibility' % (str(type (self))))
    # end hardware_read

    def hardware_update(self, obj):
        """Update hardware.
        
        :param obj: :class:`.Hardware` object
        
        """
        raise NotImplementedError('hardware_update is %s\'s responsibility' % (str(type (self))))
    # end hardware_update

    def hardwares_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all hardwares."""
        raise NotImplementedError('hardwares_list is %s\'s responsibility' % (str(type (self))))
    # end hardwares_list

    def hardware_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete hardware from the system.
        
        :param fq_name: Fully qualified name of hardware
        :param id: UUID of hardware
        :param ifmap_id: IFMAP id of hardware
        
        """
        raise NotImplementedError('hardware_delete is %s\'s responsibility' % (str(type (self))))
    # end hardware_delete

    def get_default_hardware_id(self):
        """Return UUID of default hardware."""
        raise NotImplementedError('get_default_hardware_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_hardware_delete

    def tag_create(self, obj):
        """Create new tag.
        
        :param obj: :class:`.Tag` object
        
        """
        raise NotImplementedError('tag_create is %s\'s responsibility' % (str(type (self))))
    # end tag_create

    def tag_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return tag information.
        
        :param fq_name: Fully qualified name of tag
        :param fq_name_str: Fully qualified name string of tag
        :param id: UUID of tag
        :param ifmap_id: IFMAP id of tag
        :returns: :class:`.Tag` object
        
        """
        raise NotImplementedError('tag_read is %s\'s responsibility' % (str(type (self))))
    # end tag_read

    def tag_update(self, obj):
        """Update tag.
        
        :param obj: :class:`.Tag` object
        
        """
        raise NotImplementedError('tag_update is %s\'s responsibility' % (str(type (self))))
    # end tag_update

    def tags_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all tags.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Tag` objects
        
        """
        raise NotImplementedError('tags_list is %s\'s responsibility' % (str(type (self))))
    # end tags_list

    def tag_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete tag from the system.
        
        :param fq_name: Fully qualified name of tag
        :param id: UUID of tag
        :param ifmap_id: IFMAP id of tag
        
        """
        raise NotImplementedError('tag_delete is %s\'s responsibility' % (str(type (self))))
    # end tag_delete

    def get_default_tag_id(self):
        """Return UUID of default tag."""
        raise NotImplementedError('get_default_tag_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_tag_delete

    def feature_config_create(self, obj):
        """Create new feature-config.
        
        :param obj: :class:`.FeatureConfig` object
        
        """
        raise NotImplementedError('feature_config_create is %s\'s responsibility' % (str(type (self))))
    # end feature_config_create

    def feature_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return feature-config information.
        
        :param fq_name: Fully qualified name of feature-config
        :param fq_name_str: Fully qualified name string of feature-config
        :param id: UUID of feature-config
        :param ifmap_id: IFMAP id of feature-config
        :returns: :class:`.FeatureConfig` object
        
        """
        raise NotImplementedError('feature_config_read is %s\'s responsibility' % (str(type (self))))
    # end feature_config_read

    def feature_config_update(self, obj):
        """Update feature-config.
        
        :param obj: :class:`.FeatureConfig` object
        
        """
        raise NotImplementedError('feature_config_update is %s\'s responsibility' % (str(type (self))))
    # end feature_config_update

    def feature_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all feature-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FeatureConfig` objects
        
        """
        raise NotImplementedError('feature_configs_list is %s\'s responsibility' % (str(type (self))))
    # end feature_configs_list

    def feature_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete feature-config from the system.
        
        :param fq_name: Fully qualified name of feature-config
        :param id: UUID of feature-config
        :param ifmap_id: IFMAP id of feature-config
        
        """
        raise NotImplementedError('feature_config_delete is %s\'s responsibility' % (str(type (self))))
    # end feature_config_delete

    def get_default_feature_config_id(self):
        """Return UUID of default feature-config."""
        raise NotImplementedError('get_default_feature_config_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_feature_config_delete

    def telemetry_profile_create(self, obj):
        """Create new telemetry-profile.
        
        :param obj: :class:`.TelemetryProfile` object
        
        """
        raise NotImplementedError('telemetry_profile_create is %s\'s responsibility' % (str(type (self))))
    # end telemetry_profile_create

    def telemetry_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return telemetry-profile information.
        
        :param fq_name: Fully qualified name of telemetry-profile
        :param fq_name_str: Fully qualified name string of telemetry-profile
        :param id: UUID of telemetry-profile
        :param ifmap_id: IFMAP id of telemetry-profile
        :returns: :class:`.TelemetryProfile` object
        
        """
        raise NotImplementedError('telemetry_profile_read is %s\'s responsibility' % (str(type (self))))
    # end telemetry_profile_read

    def telemetry_profile_update(self, obj):
        """Update telemetry-profile.
        
        :param obj: :class:`.TelemetryProfile` object
        
        """
        raise NotImplementedError('telemetry_profile_update is %s\'s responsibility' % (str(type (self))))
    # end telemetry_profile_update

    def telemetry_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all telemetry-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.TelemetryProfile` objects
        
        """
        raise NotImplementedError('telemetry_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end telemetry_profiles_list

    def telemetry_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete telemetry-profile from the system.
        
        :param fq_name: Fully qualified name of telemetry-profile
        :param id: UUID of telemetry-profile
        :param ifmap_id: IFMAP id of telemetry-profile
        
        """
        raise NotImplementedError('telemetry_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end telemetry_profile_delete

    def get_default_telemetry_profile_id(self):
        """Return UUID of default telemetry-profile."""
        raise NotImplementedError('get_default_telemetry_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_telemetry_profile_delete

    def bgp_router_create(self, obj):
        """Create new bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError('bgp_router_create is %s\'s responsibility' % (str(type (self))))
    # end bgp_router_create

    def bgp_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return bgp-router information.
        
        :param fq_name: Fully qualified name of bgp-router
        :param fq_name_str: Fully qualified name string of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        :returns: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError('bgp_router_read is %s\'s responsibility' % (str(type (self))))
    # end bgp_router_read

    def bgp_router_update(self, obj):
        """Update bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError('bgp_router_update is %s\'s responsibility' % (str(type (self))))
    # end bgp_router_update

    def bgp_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all bgp-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.BgpRouter` objects
        
        """
        raise NotImplementedError('bgp_routers_list is %s\'s responsibility' % (str(type (self))))
    # end bgp_routers_list

    def bgp_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bgp-router from the system.
        
        :param fq_name: Fully qualified name of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        
        """
        raise NotImplementedError('bgp_router_delete is %s\'s responsibility' % (str(type (self))))
    # end bgp_router_delete

    def get_default_bgp_router_id(self):
        """Return UUID of default bgp-router."""
        raise NotImplementedError('get_default_bgp_router_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_bgp_router_delete

    def virtual_network_create(self, obj):
        """Create new virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError('virtual_network_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_network_create

    def virtual_network_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-network information.
        
        :param fq_name: Fully qualified name of virtual-network
        :param fq_name_str: Fully qualified name string of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        :returns: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError('virtual_network_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_network_read

    def virtual_network_update(self, obj):
        """Update virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError('virtual_network_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_network_update

    def virtual_networks_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-networks.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualNetwork` objects
        
        """
        raise NotImplementedError('virtual_networks_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_networks_list

    def virtual_network_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-network from the system.
        
        :param fq_name: Fully qualified name of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        
        """
        raise NotImplementedError('virtual_network_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_network_delete

    def get_default_virtual_network_id(self):
        """Return UUID of default virtual-network."""
        raise NotImplementedError('get_default_virtual_network_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_network_delete

    def virtual_port_group_create(self, obj):
        """Create new virtual-port-group.
        
        :param obj: :class:`.VirtualPortGroup` object
        
        """
        raise NotImplementedError('virtual_port_group_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_port_group_create

    def virtual_port_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-port-group information.
        
        :param fq_name: Fully qualified name of virtual-port-group
        :param fq_name_str: Fully qualified name string of virtual-port-group
        :param id: UUID of virtual-port-group
        :param ifmap_id: IFMAP id of virtual-port-group
        :returns: :class:`.VirtualPortGroup` object
        
        """
        raise NotImplementedError('virtual_port_group_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_port_group_read

    def virtual_port_group_update(self, obj):
        """Update virtual-port-group.
        
        :param obj: :class:`.VirtualPortGroup` object
        
        """
        raise NotImplementedError('virtual_port_group_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_port_group_update

    def virtual_port_groups_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-port-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualPortGroup` objects
        
        """
        raise NotImplementedError('virtual_port_groups_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_port_groups_list

    def virtual_port_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-port-group from the system.
        
        :param fq_name: Fully qualified name of virtual-port-group
        :param id: UUID of virtual-port-group
        :param ifmap_id: IFMAP id of virtual-port-group
        
        """
        raise NotImplementedError('virtual_port_group_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_port_group_delete

    def get_default_virtual_port_group_id(self):
        """Return UUID of default virtual-port-group."""
        raise NotImplementedError('get_default_virtual_port_group_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_port_group_delete

    def service_appliance_create(self, obj):
        """Create new service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError('service_appliance_create is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_create

    def service_appliance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-appliance information.
        
        :param fq_name: Fully qualified name of service-appliance
        :param fq_name_str: Fully qualified name string of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        :returns: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError('service_appliance_read is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_read

    def service_appliance_update(self, obj):
        """Update service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError('service_appliance_update is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_update

    def service_appliances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-appliances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceAppliance` objects
        
        """
        raise NotImplementedError('service_appliances_list is %s\'s responsibility' % (str(type (self))))
    # end service_appliances_list

    def service_appliance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance from the system.
        
        :param fq_name: Fully qualified name of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        
        """
        raise NotImplementedError('service_appliance_delete is %s\'s responsibility' % (str(type (self))))
    # end service_appliance_delete

    def get_default_service_appliance_id(self):
        """Return UUID of default service-appliance."""
        raise NotImplementedError('get_default_service_appliance_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_appliance_delete

    def namespace_create(self, obj):
        """Create new namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        raise NotImplementedError('namespace_create is %s\'s responsibility' % (str(type (self))))
    # end namespace_create

    def namespace_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return namespace information.
        
        :param fq_name: Fully qualified name of namespace
        :param fq_name_str: Fully qualified name string of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        :returns: :class:`.Namespace` object
        
        """
        raise NotImplementedError('namespace_read is %s\'s responsibility' % (str(type (self))))
    # end namespace_read

    def namespace_update(self, obj):
        """Update namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        raise NotImplementedError('namespace_update is %s\'s responsibility' % (str(type (self))))
    # end namespace_update

    def namespaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all namespaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Namespace` objects
        
        """
        raise NotImplementedError('namespaces_list is %s\'s responsibility' % (str(type (self))))
    # end namespaces_list

    def namespace_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete namespace from the system.
        
        :param fq_name: Fully qualified name of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        
        """
        raise NotImplementedError('namespace_delete is %s\'s responsibility' % (str(type (self))))
    # end namespace_delete

    def get_default_namespace_id(self):
        """Return UUID of default namespace."""
        raise NotImplementedError('get_default_namespace_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_namespace_delete

    def feature_create(self, obj):
        """Create new feature.
        
        :param obj: :class:`.Feature` object
        
        """
        raise NotImplementedError('feature_create is %s\'s responsibility' % (str(type (self))))
    # end feature_create

    def feature_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return feature information.
        
        :param fq_name: Fully qualified name of feature
        :param fq_name_str: Fully qualified name string of feature
        :param id: UUID of feature
        :param ifmap_id: IFMAP id of feature
        :returns: :class:`.Feature` object
        
        """
        raise NotImplementedError('feature_read is %s\'s responsibility' % (str(type (self))))
    # end feature_read

    def feature_update(self, obj):
        """Update feature.
        
        :param obj: :class:`.Feature` object
        
        """
        raise NotImplementedError('feature_update is %s\'s responsibility' % (str(type (self))))
    # end feature_update

    def features_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all features.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Feature` objects
        
        """
        raise NotImplementedError('features_list is %s\'s responsibility' % (str(type (self))))
    # end features_list

    def feature_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete feature from the system.
        
        :param fq_name: Fully qualified name of feature
        :param id: UUID of feature
        :param ifmap_id: IFMAP id of feature
        
        """
        raise NotImplementedError('feature_delete is %s\'s responsibility' % (str(type (self))))
    # end feature_delete

    def get_default_feature_id(self):
        """Return UUID of default feature."""
        raise NotImplementedError('get_default_feature_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_feature_delete

    def storm_control_profile_create(self, obj):
        """Create new storm-control-profile.
        
        :param obj: :class:`.StormControlProfile` object
        
        """
        raise NotImplementedError('storm_control_profile_create is %s\'s responsibility' % (str(type (self))))
    # end storm_control_profile_create

    def storm_control_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return storm-control-profile information.
        
        :param fq_name: Fully qualified name of storm-control-profile
        :param fq_name_str: Fully qualified name string of storm-control-profile
        :param id: UUID of storm-control-profile
        :param ifmap_id: IFMAP id of storm-control-profile
        :returns: :class:`.StormControlProfile` object
        
        """
        raise NotImplementedError('storm_control_profile_read is %s\'s responsibility' % (str(type (self))))
    # end storm_control_profile_read

    def storm_control_profile_update(self, obj):
        """Update storm-control-profile.
        
        :param obj: :class:`.StormControlProfile` object
        
        """
        raise NotImplementedError('storm_control_profile_update is %s\'s responsibility' % (str(type (self))))
    # end storm_control_profile_update

    def storm_control_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all storm-control-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StormControlProfile` objects
        
        """
        raise NotImplementedError('storm_control_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end storm_control_profiles_list

    def storm_control_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete storm-control-profile from the system.
        
        :param fq_name: Fully qualified name of storm-control-profile
        :param id: UUID of storm-control-profile
        :param ifmap_id: IFMAP id of storm-control-profile
        
        """
        raise NotImplementedError('storm_control_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end storm_control_profile_delete

    def get_default_storm_control_profile_id(self):
        """Return UUID of default storm-control-profile."""
        raise NotImplementedError('get_default_storm_control_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_storm_control_profile_delete

    def device_image_create(self, obj):
        """Create new device-image.
        
        :param obj: :class:`.DeviceImage` object
        
        """
        raise NotImplementedError('device_image_create is %s\'s responsibility' % (str(type (self))))
    # end device_image_create

    def device_image_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return device-image information.
        
        :param fq_name: Fully qualified name of device-image
        :param fq_name_str: Fully qualified name string of device-image
        :param id: UUID of device-image
        :param ifmap_id: IFMAP id of device-image
        :returns: :class:`.DeviceImage` object
        
        """
        raise NotImplementedError('device_image_read is %s\'s responsibility' % (str(type (self))))
    # end device_image_read

    def device_image_update(self, obj):
        """Update device-image.
        
        :param obj: :class:`.DeviceImage` object
        
        """
        raise NotImplementedError('device_image_update is %s\'s responsibility' % (str(type (self))))
    # end device_image_update

    def device_images_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all device-images.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DeviceImage` objects
        
        """
        raise NotImplementedError('device_images_list is %s\'s responsibility' % (str(type (self))))
    # end device_images_list

    def device_image_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete device-image from the system.
        
        :param fq_name: Fully qualified name of device-image
        :param id: UUID of device-image
        :param ifmap_id: IFMAP id of device-image
        
        """
        raise NotImplementedError('device_image_delete is %s\'s responsibility' % (str(type (self))))
    # end device_image_delete

    def get_default_device_image_id(self):
        """Return UUID of default device-image."""
        raise NotImplementedError('get_default_device_image_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_device_image_delete

    def physical_interface_create(self, obj):
        """Create new physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError('physical_interface_create is %s\'s responsibility' % (str(type (self))))
    # end physical_interface_create

    def physical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return physical-interface information.
        
        :param fq_name: Fully qualified name of physical-interface
        :param fq_name_str: Fully qualified name string of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        :returns: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError('physical_interface_read is %s\'s responsibility' % (str(type (self))))
    # end physical_interface_read

    def physical_interface_update(self, obj):
        """Update physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError('physical_interface_update is %s\'s responsibility' % (str(type (self))))
    # end physical_interface_update

    def physical_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all physical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalInterface` objects
        
        """
        raise NotImplementedError('physical_interfaces_list is %s\'s responsibility' % (str(type (self))))
    # end physical_interfaces_list

    def physical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-interface from the system.
        
        :param fq_name: Fully qualified name of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        
        """
        raise NotImplementedError('physical_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end physical_interface_delete

    def get_default_physical_interface_id(self):
        """Return UUID of default physical-interface."""
        raise NotImplementedError('get_default_physical_interface_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_physical_interface_delete

    def access_control_list_create(self, obj):
        """Create new access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError('access_control_list_create is %s\'s responsibility' % (str(type (self))))
    # end access_control_list_create

    def access_control_list_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return access-control-list information.
        
        :param fq_name: Fully qualified name of access-control-list
        :param fq_name_str: Fully qualified name string of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        :returns: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError('access_control_list_read is %s\'s responsibility' % (str(type (self))))
    # end access_control_list_read

    def access_control_list_update(self, obj):
        """Update access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError('access_control_list_update is %s\'s responsibility' % (str(type (self))))
    # end access_control_list_update

    def access_control_lists_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all access-control-lists.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AccessControlList` objects
        
        """
        raise NotImplementedError('access_control_lists_list is %s\'s responsibility' % (str(type (self))))
    # end access_control_lists_list

    def access_control_list_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete access-control-list from the system.
        
        :param fq_name: Fully qualified name of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        
        """
        raise NotImplementedError('access_control_list_delete is %s\'s responsibility' % (str(type (self))))
    # end access_control_list_delete

    def get_default_access_control_list_id(self):
        """Return UUID of default access-control-list."""
        raise NotImplementedError('get_default_access_control_list_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_access_control_list_delete

    def node_create(self, obj):
        """Create new node.
        
        :param obj: :class:`.Node` object
        
        """
        raise NotImplementedError('node_create is %s\'s responsibility' % (str(type (self))))
    # end node_create

    def node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return node information.
        
        :param fq_name: Fully qualified name of node
        :param fq_name_str: Fully qualified name string of node
        :param id: UUID of node
        :param ifmap_id: IFMAP id of node
        :returns: :class:`.Node` object
        
        """
        raise NotImplementedError('node_read is %s\'s responsibility' % (str(type (self))))
    # end node_read

    def node_update(self, obj):
        """Update node.
        
        :param obj: :class:`.Node` object
        
        """
        raise NotImplementedError('node_update is %s\'s responsibility' % (str(type (self))))
    # end node_update

    def nodes_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Node` objects
        
        """
        raise NotImplementedError('nodes_list is %s\'s responsibility' % (str(type (self))))
    # end nodes_list

    def node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete node from the system.
        
        :param fq_name: Fully qualified name of node
        :param id: UUID of node
        :param ifmap_id: IFMAP id of node
        
        """
        raise NotImplementedError('node_delete is %s\'s responsibility' % (str(type (self))))
    # end node_delete

    def get_default_node_id(self):
        """Return UUID of default node."""
        raise NotImplementedError('get_default_node_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_node_delete

    def customer_attachment_create(self, obj):
        """Create new customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError('customer_attachment_create is %s\'s responsibility' % (str(type (self))))
    # end customer_attachment_create

    def customer_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return customer-attachment information.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param fq_name_str: Fully qualified name string of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        :returns: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError('customer_attachment_read is %s\'s responsibility' % (str(type (self))))
    # end customer_attachment_read

    def customer_attachment_update(self, obj):
        """Update customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError('customer_attachment_update is %s\'s responsibility' % (str(type (self))))
    # end customer_attachment_update

    def customer_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all customer-attachments."""
        raise NotImplementedError('customer_attachments_list is %s\'s responsibility' % (str(type (self))))
    # end customer_attachments_list

    def customer_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete customer-attachment from the system.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        
        """
        raise NotImplementedError('customer_attachment_delete is %s\'s responsibility' % (str(type (self))))
    # end customer_attachment_delete

    def get_default_customer_attachment_id(self):
        """Return UUID of default customer-attachment."""
        raise NotImplementedError('get_default_customer_attachment_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_customer_attachment_delete

    def structured_syslog_sla_profile_create(self, obj):
        """Create new structured-syslog-sla-profile.
        
        :param obj: :class:`.StructuredSyslogSlaProfile` object
        
        """
        raise NotImplementedError('structured_syslog_sla_profile_create is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_sla_profile_create

    def structured_syslog_sla_profile_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return structured-syslog-sla-profile information.
        
        :param fq_name: Fully qualified name of structured-syslog-sla-profile
        :param fq_name_str: Fully qualified name string of structured-syslog-sla-profile
        :param id: UUID of structured-syslog-sla-profile
        :param ifmap_id: IFMAP id of structured-syslog-sla-profile
        :returns: :class:`.StructuredSyslogSlaProfile` object
        
        """
        raise NotImplementedError('structured_syslog_sla_profile_read is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_sla_profile_read

    def structured_syslog_sla_profile_update(self, obj):
        """Update structured-syslog-sla-profile.
        
        :param obj: :class:`.StructuredSyslogSlaProfile` object
        
        """
        raise NotImplementedError('structured_syslog_sla_profile_update is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_sla_profile_update

    def structured_syslog_sla_profiles_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all structured-syslog-sla-profiles.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.StructuredSyslogSlaProfile` objects
        
        """
        raise NotImplementedError('structured_syslog_sla_profiles_list is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_sla_profiles_list

    def structured_syslog_sla_profile_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete structured-syslog-sla-profile from the system.
        
        :param fq_name: Fully qualified name of structured-syslog-sla-profile
        :param id: UUID of structured-syslog-sla-profile
        :param ifmap_id: IFMAP id of structured-syslog-sla-profile
        
        """
        raise NotImplementedError('structured_syslog_sla_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end structured_syslog_sla_profile_delete

    def get_default_structured_syslog_sla_profile_id(self):
        """Return UUID of default structured-syslog-sla-profile."""
        raise NotImplementedError('get_default_structured_syslog_sla_profile_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_structured_syslog_sla_profile_delete

    def host_based_service_create(self, obj):
        """Create new host-based-service.
        
        :param obj: :class:`.HostBasedService` object
        
        """
        raise NotImplementedError('host_based_service_create is %s\'s responsibility' % (str(type (self))))
    # end host_based_service_create

    def host_based_service_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return host-based-service information.
        
        :param fq_name: Fully qualified name of host-based-service
        :param fq_name_str: Fully qualified name string of host-based-service
        :param id: UUID of host-based-service
        :param ifmap_id: IFMAP id of host-based-service
        :returns: :class:`.HostBasedService` object
        
        """
        raise NotImplementedError('host_based_service_read is %s\'s responsibility' % (str(type (self))))
    # end host_based_service_read

    def host_based_service_update(self, obj):
        """Update host-based-service.
        
        :param obj: :class:`.HostBasedService` object
        
        """
        raise NotImplementedError('host_based_service_update is %s\'s responsibility' % (str(type (self))))
    # end host_based_service_update

    def host_based_services_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all host-based-services.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.HostBasedService` objects
        
        """
        raise NotImplementedError('host_based_services_list is %s\'s responsibility' % (str(type (self))))
    # end host_based_services_list

    def host_based_service_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete host-based-service from the system.
        
        :param fq_name: Fully qualified name of host-based-service
        :param id: UUID of host-based-service
        :param ifmap_id: IFMAP id of host-based-service
        
        """
        raise NotImplementedError('host_based_service_delete is %s\'s responsibility' % (str(type (self))))
    # end host_based_service_delete

    def get_default_host_based_service_id(self):
        """Return UUID of default host-based-service."""
        raise NotImplementedError('get_default_host_based_service_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_host_based_service_delete

    def virtual_machine_create(self, obj):
        """Create new virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError('virtual_machine_create is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_create

    def virtual_machine_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-machine information.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param fq_name_str: Fully qualified name string of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        :returns: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError('virtual_machine_read is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_read

    def virtual_machine_update(self, obj):
        """Update virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError('virtual_machine_update is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_update

    def virtual_machines_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-machines."""
        raise NotImplementedError('virtual_machines_list is %s\'s responsibility' % (str(type (self))))
    # end virtual_machines_list

    def virtual_machine_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine from the system.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        
        """
        raise NotImplementedError('virtual_machine_delete is %s\'s responsibility' % (str(type (self))))
    # end virtual_machine_delete

    def get_default_virtual_machine_id(self):
        """Return UUID of default virtual-machine."""
        raise NotImplementedError('get_default_virtual_machine_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_virtual_machine_delete

    def interface_route_table_create(self, obj):
        """Create new interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError('interface_route_table_create is %s\'s responsibility' % (str(type (self))))
    # end interface_route_table_create

    def interface_route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return interface-route-table information.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param fq_name_str: Fully qualified name string of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        :returns: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError('interface_route_table_read is %s\'s responsibility' % (str(type (self))))
    # end interface_route_table_read

    def interface_route_table_update(self, obj):
        """Update interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError('interface_route_table_update is %s\'s responsibility' % (str(type (self))))
    # end interface_route_table_update

    def interface_route_tables_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all interface-route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.InterfaceRouteTable` objects
        
        """
        raise NotImplementedError('interface_route_tables_list is %s\'s responsibility' % (str(type (self))))
    # end interface_route_tables_list

    def interface_route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete interface-route-table from the system.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        
        """
        raise NotImplementedError('interface_route_table_delete is %s\'s responsibility' % (str(type (self))))
    # end interface_route_table_delete

    def get_default_interface_route_table_id(self):
        """Return UUID of default interface-route-table."""
        raise NotImplementedError('get_default_interface_route_table_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_interface_route_table_delete

    def loadbalancer_member_create(self, obj):
        """Create new loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError('loadbalancer_member_create is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_member_create

    def loadbalancer_member_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-member information.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param fq_name_str: Fully qualified name string of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        :returns: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError('loadbalancer_member_read is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_member_read

    def loadbalancer_member_update(self, obj):
        """Update loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError('loadbalancer_member_update is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_member_update

    def loadbalancer_members_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-members.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerMember` objects
        
        """
        raise NotImplementedError('loadbalancer_members_list is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_members_list

    def loadbalancer_member_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-member from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        
        """
        raise NotImplementedError('loadbalancer_member_delete is %s\'s responsibility' % (str(type (self))))
    # end loadbalancer_member_delete

    def get_default_loadbalancer_member_id(self):
        """Return UUID of default loadbalancer-member."""
        raise NotImplementedError('get_default_loadbalancer_member_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_loadbalancer_member_delete

    def service_health_check_create(self, obj):
        """Create new service-health-check.
        
        :param obj: :class:`.ServiceHealthCheck` object
        
        """
        raise NotImplementedError('service_health_check_create is %s\'s responsibility' % (str(type (self))))
    # end service_health_check_create

    def service_health_check_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-health-check information.
        
        :param fq_name: Fully qualified name of service-health-check
        :param fq_name_str: Fully qualified name string of service-health-check
        :param id: UUID of service-health-check
        :param ifmap_id: IFMAP id of service-health-check
        :returns: :class:`.ServiceHealthCheck` object
        
        """
        raise NotImplementedError('service_health_check_read is %s\'s responsibility' % (str(type (self))))
    # end service_health_check_read

    def service_health_check_update(self, obj):
        """Update service-health-check.
        
        :param obj: :class:`.ServiceHealthCheck` object
        
        """
        raise NotImplementedError('service_health_check_update is %s\'s responsibility' % (str(type (self))))
    # end service_health_check_update

    def service_health_checks_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-health-checks.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceHealthCheck` objects
        
        """
        raise NotImplementedError('service_health_checks_list is %s\'s responsibility' % (str(type (self))))
    # end service_health_checks_list

    def service_health_check_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-health-check from the system.
        
        :param fq_name: Fully qualified name of service-health-check
        :param id: UUID of service-health-check
        :param ifmap_id: IFMAP id of service-health-check
        
        """
        raise NotImplementedError('service_health_check_delete is %s\'s responsibility' % (str(type (self))))
    # end service_health_check_delete

    def get_default_service_health_check_id(self):
        """Return UUID of default service-health-check."""
        raise NotImplementedError('get_default_service_health_check_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_service_health_check_delete

    def alarm_create(self, obj):
        """Create new alarm.
        
        :param obj: :class:`.Alarm` object
        
        """
        raise NotImplementedError('alarm_create is %s\'s responsibility' % (str(type (self))))
    # end alarm_create

    def alarm_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return alarm information.
        
        :param fq_name: Fully qualified name of alarm
        :param fq_name_str: Fully qualified name string of alarm
        :param id: UUID of alarm
        :param ifmap_id: IFMAP id of alarm
        :returns: :class:`.Alarm` object
        
        """
        raise NotImplementedError('alarm_read is %s\'s responsibility' % (str(type (self))))
    # end alarm_read

    def alarm_update(self, obj):
        """Update alarm.
        
        :param obj: :class:`.Alarm` object
        
        """
        raise NotImplementedError('alarm_update is %s\'s responsibility' % (str(type (self))))
    # end alarm_update

    def alarms_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all alarms.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Alarm` objects
        
        """
        raise NotImplementedError('alarms_list is %s\'s responsibility' % (str(type (self))))
    # end alarms_list

    def alarm_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete alarm from the system.
        
        :param fq_name: Fully qualified name of alarm
        :param id: UUID of alarm
        :param ifmap_id: IFMAP id of alarm
        
        """
        raise NotImplementedError('alarm_delete is %s\'s responsibility' % (str(type (self))))
    # end alarm_delete

    def get_default_alarm_id(self):
        """Return UUID of default alarm."""
        raise NotImplementedError('get_default_alarm_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_alarm_delete

    def api_access_list_create(self, obj):
        """Create new api-access-list.
        
        :param obj: :class:`.ApiAccessList` object
        
        """
        raise NotImplementedError('api_access_list_create is %s\'s responsibility' % (str(type (self))))
    # end api_access_list_create

    def api_access_list_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return api-access-list information.
        
        :param fq_name: Fully qualified name of api-access-list
        :param fq_name_str: Fully qualified name string of api-access-list
        :param id: UUID of api-access-list
        :param ifmap_id: IFMAP id of api-access-list
        :returns: :class:`.ApiAccessList` object
        
        """
        raise NotImplementedError('api_access_list_read is %s\'s responsibility' % (str(type (self))))
    # end api_access_list_read

    def api_access_list_update(self, obj):
        """Update api-access-list.
        
        :param obj: :class:`.ApiAccessList` object
        
        """
        raise NotImplementedError('api_access_list_update is %s\'s responsibility' % (str(type (self))))
    # end api_access_list_update

    def api_access_lists_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all api-access-lists.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ApiAccessList` objects
        
        """
        raise NotImplementedError('api_access_lists_list is %s\'s responsibility' % (str(type (self))))
    # end api_access_lists_list

    def api_access_list_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete api-access-list from the system.
        
        :param fq_name: Fully qualified name of api-access-list
        :param id: UUID of api-access-list
        :param ifmap_id: IFMAP id of api-access-list
        
        """
        raise NotImplementedError('api_access_list_delete is %s\'s responsibility' % (str(type (self))))
    # end api_access_list_delete

    def get_default_api_access_list_id(self):
        """Return UUID of default api-access-list."""
        raise NotImplementedError('get_default_api_access_list_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_api_access_list_delete

    def routing_instance_create(self, obj):
        """Create new routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError('routing_instance_create is %s\'s responsibility' % (str(type (self))))
    # end routing_instance_create

    def routing_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return routing-instance information.
        
        :param fq_name: Fully qualified name of routing-instance
        :param fq_name_str: Fully qualified name string of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        :returns: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError('routing_instance_read is %s\'s responsibility' % (str(type (self))))
    # end routing_instance_read

    def routing_instance_update(self, obj):
        """Update routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError('routing_instance_update is %s\'s responsibility' % (str(type (self))))
    # end routing_instance_update

    def routing_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all routing-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoutingInstance` objects
        
        """
        raise NotImplementedError('routing_instances_list is %s\'s responsibility' % (str(type (self))))
    # end routing_instances_list

    def routing_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete routing-instance from the system.
        
        :param fq_name: Fully qualified name of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        
        """
        raise NotImplementedError('routing_instance_delete is %s\'s responsibility' % (str(type (self))))
    # end routing_instance_delete

    def get_default_routing_instance_id(self):
        """Return UUID of default routing-instance."""
        raise NotImplementedError('get_default_routing_instance_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_routing_instance_delete

    def alias_ip_pool_create(self, obj):
        """Create new alias-ip-pool.
        
        :param obj: :class:`.AliasIpPool` object
        
        """
        raise NotImplementedError('alias_ip_pool_create is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_pool_create

    def alias_ip_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return alias-ip-pool information.
        
        :param fq_name: Fully qualified name of alias-ip-pool
        :param fq_name_str: Fully qualified name string of alias-ip-pool
        :param id: UUID of alias-ip-pool
        :param ifmap_id: IFMAP id of alias-ip-pool
        :returns: :class:`.AliasIpPool` object
        
        """
        raise NotImplementedError('alias_ip_pool_read is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_pool_read

    def alias_ip_pool_update(self, obj):
        """Update alias-ip-pool.
        
        :param obj: :class:`.AliasIpPool` object
        
        """
        raise NotImplementedError('alias_ip_pool_update is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_pool_update

    def alias_ip_pools_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all alias-ip-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AliasIpPool` objects
        
        """
        raise NotImplementedError('alias_ip_pools_list is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_pools_list

    def alias_ip_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete alias-ip-pool from the system.
        
        :param fq_name: Fully qualified name of alias-ip-pool
        :param id: UUID of alias-ip-pool
        :param ifmap_id: IFMAP id of alias-ip-pool
        
        """
        raise NotImplementedError('alias_ip_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end alias_ip_pool_delete

    def get_default_alias_ip_pool_id(self):
        """Return UUID of default alias-ip-pool."""
        raise NotImplementedError('get_default_alias_ip_pool_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_alias_ip_pool_delete

    def data_center_interconnect_create(self, obj):
        """Create new data-center-interconnect.
        
        :param obj: :class:`.DataCenterInterconnect` object
        
        """
        raise NotImplementedError('data_center_interconnect_create is %s\'s responsibility' % (str(type (self))))
    # end data_center_interconnect_create

    def data_center_interconnect_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return data-center-interconnect information.
        
        :param fq_name: Fully qualified name of data-center-interconnect
        :param fq_name_str: Fully qualified name string of data-center-interconnect
        :param id: UUID of data-center-interconnect
        :param ifmap_id: IFMAP id of data-center-interconnect
        :returns: :class:`.DataCenterInterconnect` object
        
        """
        raise NotImplementedError('data_center_interconnect_read is %s\'s responsibility' % (str(type (self))))
    # end data_center_interconnect_read

    def data_center_interconnect_update(self, obj):
        """Update data-center-interconnect.
        
        :param obj: :class:`.DataCenterInterconnect` object
        
        """
        raise NotImplementedError('data_center_interconnect_update is %s\'s responsibility' % (str(type (self))))
    # end data_center_interconnect_update

    def data_center_interconnects_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all data-center-interconnects.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DataCenterInterconnect` objects
        
        """
        raise NotImplementedError('data_center_interconnects_list is %s\'s responsibility' % (str(type (self))))
    # end data_center_interconnects_list

    def data_center_interconnect_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete data-center-interconnect from the system.
        
        :param fq_name: Fully qualified name of data-center-interconnect
        :param id: UUID of data-center-interconnect
        :param ifmap_id: IFMAP id of data-center-interconnect
        
        """
        raise NotImplementedError('data_center_interconnect_delete is %s\'s responsibility' % (str(type (self))))
    # end data_center_interconnect_delete

    def get_default_data_center_interconnect_id(self):
        """Return UUID of default data-center-interconnect."""
        raise NotImplementedError('get_default_data_center_interconnect_delete is %s\'s responsibility' % (str(type (self))))
    # end get_default_data_center_interconnect_delete

# end class ConnectionDriverBase

