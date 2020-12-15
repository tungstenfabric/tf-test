'''
This module defines the fixture classes for all config elements
'''

# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from __future__ import absolute_import
from . import cfixture
from vnc_api import vnc_api
try:
    from cfgm_common.exceptions import *
except ImportError:
    from vnc_api.exceptions import *

from .generatedssuper import GeneratedsSuper

class ServiceEndpointTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceEndpoint`
    """
    def __init__(self, conn_drv, service_endpoint_name=None, auto_prop_val=False, service_connection_module_refs = None, physical_router_refs = None, service_object_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceEndpointTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            service_connection_module (list): list of :class:`ServiceConnectionModule` type
            physical_router (list): list of :class:`PhysicalRouter` type
            service_object (list): list of :class:`ServiceObject` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceEndpointTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_endpoint_name:
            self._name = 'default-service-endpoint'
        else:
            self._name = service_endpoint_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if service_connection_module_refs:
            for ln in service_connection_module_refs:
                self.add_service_connection_module (ln)
        if physical_router_refs:
            for ln in physical_router_refs:
                self.add_physical_router (ln)
        if service_object_refs:
            for ln in service_object_refs:
                self.add_service_object (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_connection_modules ():
            self.add_service_connection_module (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_routers ():
            self.add_physical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_objects ():
            self.add_service_object (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_connection_module (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceConnectionModule` link to :class:`ServiceEndpoint`
        Args:
            lo (:class:`ServiceConnectionModule`): obj to link
        '''
        if self._obj:
            self._obj.add_service_connection_module (lo)
            if update_server:
                self._conn_drv.service_endpoint_update (self._obj)

        if add_link:
            self.add_link('service_connection_module', cfixture.ConrtailLink('service_connection_module', 'service_endpoint', 'service_connection_module', ['ref'], lo))
    # end add_service_connection_module_link

    def get_service_connection_modules (self):
        return self.get_links ('service_connection_module')
    # end get_service_connection_modules
    def add_physical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRouter` link to :class:`ServiceEndpoint`
        Args:
            lo (:class:`PhysicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_router (lo)
            if update_server:
                self._conn_drv.service_endpoint_update (self._obj)

        if add_link:
            self.add_link('physical_router', cfixture.ConrtailLink('physical_router', 'service_endpoint', 'physical_router', ['ref'], lo))
    # end add_physical_router_link

    def get_physical_routers (self):
        return self.get_links ('physical_router')
    # end get_physical_routers
    def add_service_object (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceObject` link to :class:`ServiceEndpoint`
        Args:
            lo (:class:`ServiceObject`): obj to link
        '''
        if self._obj:
            self._obj.add_service_object (lo)
            if update_server:
                self._conn_drv.service_endpoint_update (self._obj)

        if add_link:
            self.add_link('service_object', cfixture.ConrtailLink('service_object', 'service_endpoint', 'service_object', ['ref'], lo))
    # end add_service_object_link

    def get_service_objects (self):
        return self.get_links ('service_object')
    # end get_service_objects
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceEndpoint`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_endpoint_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_endpoint', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceEndpointTestFixtureGen, self).setUp()
        self._obj = vnc_api.ServiceEndpoint(self._name)
        try:
            self._obj = self._conn_drv.service_endpoint_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_endpoint_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_endpoint_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_endpoint_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceEndpointTestFixtureGen

class InstanceIpTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.InstanceIp`
    """
    def __init__(self, conn_drv, instance_ip_name=None, auto_prop_val=False, virtual_network_refs = None, network_ipam_refs = None, virtual_machine_interface_refs = None, physical_router_refs = None, virtual_router_refs = None, logical_interface_refs = None, flow_node_refs = None, tag_refs = None, instance_ip_address=None, instance_ip_family=None, instance_ip_mode=None, secondary_ip_tracking_ip=None, subnet_uuid=None, instance_ip_subscriber_tag=None, instance_ip_secondary=None, instance_ip_local_ip=None, service_instance_ip=None, service_health_check_ip=None, instance_ip_subnet=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create InstanceIpTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            virtual_network (list): list of :class:`VirtualNetwork` type
            network_ipam (list): list of :class:`NetworkIpam` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            physical_router (list): list of :class:`PhysicalRouter` type
            virtual_router (list): list of :class:`VirtualRouter` type
            logical_interface (list): list of :class:`LogicalInterface` type
            flow_node (list): list of :class:`FlowNode` type
            tag (list): list of :class:`Tag` type
            instance_ip_address (instance): instance of :class:`xsd:string`
            instance_ip_family (instance): instance of :class:`xsd:string`
            instance_ip_mode (instance): instance of :class:`xsd:string`
            secondary_ip_tracking_ip (instance): instance of :class:`SubnetType`
            subnet_uuid (instance): instance of :class:`xsd:string`
            instance_ip_subscriber_tag (instance): instance of :class:`xsd:string`
            instance_ip_secondary (instance): instance of :class:`xsd:boolean`
            instance_ip_local_ip (instance): instance of :class:`xsd:boolean`
            service_instance_ip (instance): instance of :class:`xsd:boolean`
            service_health_check_ip (instance): instance of :class:`xsd:boolean`
            instance_ip_subnet (instance): instance of :class:`SubnetType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(InstanceIpTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not instance_ip_name:
            self._name = 'default-instance-ip'
        else:
            self._name = instance_ip_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if network_ipam_refs:
            for ln in network_ipam_refs:
                self.add_network_ipam (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if physical_router_refs:
            for ln in physical_router_refs:
                self.add_physical_router (ln)
        if virtual_router_refs:
            for ln in virtual_router_refs:
                self.add_virtual_router (ln)
        if logical_interface_refs:
            for ln in logical_interface_refs:
                self.add_logical_interface (ln)
        if flow_node_refs:
            for ln in flow_node_refs:
                self.add_flow_node (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.instance_ip_address = instance_ip_address
        self.instance_ip_family = instance_ip_family
        self.instance_ip_mode = instance_ip_mode
        self.secondary_ip_tracking_ip = secondary_ip_tracking_ip
        self.subnet_uuid = subnet_uuid
        self.instance_ip_subscriber_tag = instance_ip_subscriber_tag
        self.instance_ip_secondary = instance_ip_secondary
        self.instance_ip_local_ip = instance_ip_local_ip
        self.service_instance_ip = service_instance_ip
        self.service_health_check_ip = service_health_check_ip
        self.instance_ip_subnet = instance_ip_subnet
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_network_ipams ():
            self.add_network_ipam (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_routers ():
            self.add_physical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_routers ():
            self.add_virtual_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_logical_interfaces ():
            self.add_logical_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_flow_nodes ():
            self.add_flow_node (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`InstanceIp`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'instance_ip', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_network_ipam (self, lo, update_server = True, add_link = True):
        '''
        add :class:`NetworkIpam` link to :class:`InstanceIp`
        Args:
            lo (:class:`NetworkIpam`): obj to link
        '''
        if self._obj:
            self._obj.add_network_ipam (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('network_ipam', cfixture.ConrtailLink('network_ipam', 'instance_ip', 'network_ipam', ['ref'], lo))
    # end add_network_ipam_link

    def get_network_ipams (self):
        return self.get_links ('network_ipam')
    # end get_network_ipams
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`InstanceIp`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'instance_ip', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_physical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRouter` link to :class:`InstanceIp`
        Args:
            lo (:class:`PhysicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_router (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('physical_router', cfixture.ConrtailLink('physical_router', 'instance_ip', 'physical_router', ['ref'], lo))
    # end add_physical_router_link

    def get_physical_routers (self):
        return self.get_links ('physical_router')
    # end get_physical_routers
    def add_virtual_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualRouter` link to :class:`InstanceIp`
        Args:
            lo (:class:`VirtualRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_router (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_router', cfixture.ConrtailLink('virtual_router', 'instance_ip', 'virtual_router', ['ref'], lo))
    # end add_virtual_router_link

    def get_virtual_routers (self):
        return self.get_links ('virtual_router')
    # end get_virtual_routers
    def add_logical_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LogicalInterface` link to :class:`InstanceIp`
        Args:
            lo (:class:`LogicalInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_logical_interface (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('logical_interface', cfixture.ConrtailLink('logical_interface', 'instance_ip', 'logical_interface', ['ref'], lo))
    # end add_logical_interface_link

    def get_logical_interfaces (self):
        return self.get_links ('logical_interface')
    # end get_logical_interfaces
    def add_flow_node (self, lo, update_server = True, add_link = True):
        '''
        add :class:`FlowNode` link to :class:`InstanceIp`
        Args:
            lo (:class:`FlowNode`): obj to link
        '''
        if self._obj:
            self._obj.add_flow_node (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('flow_node', cfixture.ConrtailLink('flow_node', 'instance_ip', 'flow_node', ['ref'], lo))
    # end add_flow_node_link

    def get_flow_nodes (self):
        return self.get_links ('flow_node')
    # end get_flow_nodes
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`InstanceIp`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.instance_ip_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'instance_ip', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_instance_ip_address(self.instance_ip_address or GeneratedsSuper.populate_string("instance_ip_address"))
        self._obj.set_instance_ip_family(self.instance_ip_family or GeneratedsSuper.populate_string("instance_ip_family"))
        self._obj.set_instance_ip_mode(self.instance_ip_mode or GeneratedsSuper.populate_string("instance_ip_mode"))
        self._obj.set_secondary_ip_tracking_ip(self.secondary_ip_tracking_ip or vnc_api.gen.resource_xsd.SubnetType.populate())
        self._obj.set_subnet_uuid(self.subnet_uuid or GeneratedsSuper.populate_string("subnet_uuid"))
        self._obj.set_instance_ip_subscriber_tag(self.instance_ip_subscriber_tag or GeneratedsSuper.populate_string("instance_ip_subscriber_tag"))
        self._obj.set_instance_ip_secondary(self.instance_ip_secondary or GeneratedsSuper.populate_boolean("instance_ip_secondary"))
        self._obj.set_instance_ip_local_ip(self.instance_ip_local_ip or GeneratedsSuper.populate_boolean("instance_ip_local_ip"))
        self._obj.set_service_instance_ip(self.service_instance_ip or GeneratedsSuper.populate_boolean("service_instance_ip"))
        self._obj.set_service_health_check_ip(self.service_health_check_ip or GeneratedsSuper.populate_boolean("service_health_check_ip"))
        self._obj.set_instance_ip_subnet(self.instance_ip_subnet or vnc_api.gen.resource_xsd.SubnetType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(InstanceIpTestFixtureGen, self).setUp()
        self._obj = vnc_api.InstanceIp(self._name)
        try:
            self._obj = self._conn_drv.instance_ip_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.instance_ip_address = self.instance_ip_address
                self._obj.instance_ip_family = self.instance_ip_family
                self._obj.instance_ip_mode = self.instance_ip_mode
                self._obj.secondary_ip_tracking_ip = self.secondary_ip_tracking_ip
                self._obj.subnet_uuid = self.subnet_uuid
                self._obj.instance_ip_subscriber_tag = self.instance_ip_subscriber_tag
                self._obj.instance_ip_secondary = self.instance_ip_secondary
                self._obj.instance_ip_local_ip = self.instance_ip_local_ip
                self._obj.service_instance_ip = self.service_instance_ip
                self._obj.service_health_check_ip = self.service_health_check_ip
                self._obj.instance_ip_subnet = self.instance_ip_subnet
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.instance_ip_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.instance_ip_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.instance_ip_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class InstanceIpTestFixtureGen

class ServiceApplianceSetTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceApplianceSet`
    """
    def __init__(self, conn_drv, service_appliance_set_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, service_appliance_set_virtualization_type=None, service_appliance_set_properties=None, service_appliance_driver=None, service_appliance_ha_mode=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceApplianceSetTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_appliance_set_name (str): Name of service_appliance_set
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            service_appliance_set_virtualization_type (instance): instance of :class:`xsd:string`
            service_appliance_set_properties (instance): instance of :class:`KeyValuePairs`
            service_appliance_driver (instance): instance of :class:`xsd:string`
            service_appliance_ha_mode (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceApplianceSetTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_appliance_set_name:
            self._name = 'default-service-appliance-set'
        else:
            self._name = service_appliance_set_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_appliance_set_virtualization_type = service_appliance_set_virtualization_type
        self.service_appliance_set_properties = service_appliance_set_properties
        self.service_appliance_driver = service_appliance_driver
        self.service_appliance_ha_mode = service_appliance_ha_mode
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceApplianceSet`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_appliance_set_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_appliance_set', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_appliance_set_virtualization_type(self.service_appliance_set_virtualization_type or GeneratedsSuper.populate_string("service_appliance_set_virtualization_type"))
        self._obj.set_service_appliance_set_properties(self.service_appliance_set_properties or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_service_appliance_driver(self.service_appliance_driver or GeneratedsSuper.populate_string("service_appliance_driver"))
        self._obj.set_service_appliance_ha_mode(self.service_appliance_ha_mode or GeneratedsSuper.populate_string("service_appliance_ha_mode"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceApplianceSetTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.ServiceApplianceSet(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_appliance_set_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_appliance_set_virtualization_type = self.service_appliance_set_virtualization_type
                self._obj.service_appliance_set_properties = self.service_appliance_set_properties
                self._obj.service_appliance_driver = self.service_appliance_driver
                self._obj.service_appliance_ha_mode = self.service_appliance_ha_mode
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_appliance_set_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_appliance_set_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_appliance_set_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_appliance_sets() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_appliance_sets.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceApplianceSetTestFixtureGen

class RouteTargetTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RouteTarget`
    """
    def __init__(self, conn_drv, route_target_name=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RouteTargetTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RouteTargetTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not route_target_name:
            self._name = 'default-route-target'
        else:
            self._name = route_target_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RouteTarget`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.route_target_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'route_target', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RouteTargetTestFixtureGen, self).setUp()
        self._obj = vnc_api.RouteTarget(self._name)
        try:
            self._obj = self._conn_drv.route_target_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.route_target_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.route_target_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.route_target_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RouteTargetTestFixtureGen

class LoadbalancerListenerTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LoadbalancerListener`
    """
    def __init__(self, conn_drv, loadbalancer_listener_name=None, parent_fixt=None, auto_prop_val=False, loadbalancer_refs = None, tag_refs = None, loadbalancer_listener_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LoadbalancerListenerTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            loadbalancer_listener_name (str): Name of loadbalancer_listener
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            loadbalancer (list): list of :class:`Loadbalancer` type
            tag (list): list of :class:`Tag` type
            loadbalancer_listener_properties (instance): instance of :class:`LoadbalancerListenerType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LoadbalancerListenerTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not loadbalancer_listener_name:
            self._name = 'default-loadbalancer-listener'
        else:
            self._name = loadbalancer_listener_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if loadbalancer_refs:
            for ln in loadbalancer_refs:
                self.add_loadbalancer (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.loadbalancer_listener_properties = loadbalancer_listener_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_loadbalancers ():
            self.add_loadbalancer (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_loadbalancer (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Loadbalancer` link to :class:`LoadbalancerListener`
        Args:
            lo (:class:`Loadbalancer`): obj to link
        '''
        if self._obj:
            self._obj.add_loadbalancer (lo)
            if update_server:
                self._conn_drv.loadbalancer_listener_update (self._obj)

        if add_link:
            self.add_link('loadbalancer', cfixture.ConrtailLink('loadbalancer', 'loadbalancer_listener', 'loadbalancer', ['ref'], lo))
    # end add_loadbalancer_link

    def get_loadbalancers (self):
        return self.get_links ('loadbalancer')
    # end get_loadbalancers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LoadbalancerListener`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.loadbalancer_listener_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'loadbalancer_listener', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_loadbalancer_listener_properties(self.loadbalancer_listener_properties or vnc_api.gen.resource_xsd.LoadbalancerListenerType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LoadbalancerListenerTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.LoadbalancerListener(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.loadbalancer_listener_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.loadbalancer_listener_properties = self.loadbalancer_listener_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.loadbalancer_listener_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.loadbalancer_listener_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.loadbalancer_listener_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_loadbalancer_listeners() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.loadbalancer_listeners.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LoadbalancerListenerTestFixtureGen

class FloatingIpPoolTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FloatingIpPool`
    """
    def __init__(self, conn_drv, floating_ip_pool_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, floating_ip_pool_subnets=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FloatingIpPoolTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            floating_ip_pool_name (str): Name of floating_ip_pool
            parent_fixt (:class:`.VirtualNetworkTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            floating_ip_pool_subnets (instance): instance of :class:`FloatingIpPoolSubnetType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FloatingIpPoolTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not floating_ip_pool_name:
            self._name = 'default-floating-ip-pool'
        else:
            self._name = floating_ip_pool_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.floating_ip_pool_subnets = floating_ip_pool_subnets
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FloatingIpPool`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.floating_ip_pool_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'floating_ip_pool', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_floating_ip_pool_subnets(self.floating_ip_pool_subnets or vnc_api.gen.resource_xsd.FloatingIpPoolSubnetType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FloatingIpPoolTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(VirtualNetworkTestFixtureGen(self._conn_drv, 'default-virtual-network'))

        self._obj = vnc_api.FloatingIpPool(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.floating_ip_pool_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.floating_ip_pool_subnets = self.floating_ip_pool_subnets
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.floating_ip_pool_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.floating_ip_pool_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.floating_ip_pool_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_floating_ip_pools() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.floating_ip_pools.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FloatingIpPoolTestFixtureGen

class PhysicalRouterTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PhysicalRouter`
    """
    def __init__(self, conn_drv, physical_router_name=None, parent_fixt=None, auto_prop_val=False, virtual_router_refs = None, bgp_router_refs = None, virtual_network_refs = None, intent_map_refs = None, fabric_refs = None, node_profile_refs = None, device_functional_group_refs = None, device_chassis_refs = None, device_image_refs = None, physical_role_refs = None, overlay_role_refs = None, telemetry_profile_refs = None, tag_refs = None, physical_router_junos_service_ports=None, telemetry_info=None, physical_router_device_family=None, physical_router_os_version=None, physical_router_hostname=None, physical_router_management_ip=None, physical_router_management_mac=None, physical_router_dataplane_ip=None, physical_router_loopback_ip=None, physical_router_replicator_loopback_ip=None, physical_router_vendor_name=None, physical_router_product_name=None, physical_router_serial_number=None, physical_router_vnc_managed=None, physical_router_underlay_managed=None, physical_router_role=None, routing_bridging_roles=None, physical_router_snmp=None, physical_router_lldp=None, physical_router_user_credentials=None, physical_router_encryption_type=None, physical_router_snmp_credentials=None, physical_router_dhcp_parameters=None, physical_router_cli_commit_state=None, physical_router_managed_state=None, physical_router_underlay_config=None, physical_router_supplemental_config=None, physical_router_autonomous_system=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PhysicalRouterTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            physical_router_name (str): Name of physical_router
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            virtual_router (list): list of :class:`VirtualRouter` type
            bgp_router (list): list of :class:`BgpRouter` type
            virtual_network (list): list of :class:`VirtualNetwork` type
            intent_map (list): list of :class:`IntentMap` type
            fabric (list): list of :class:`Fabric` type
            node_profile (list): list of :class:`NodeProfile` type
            device_functional_group (list): list of :class:`DeviceFunctionalGroup` type
            device_chassis (list): list of :class:`DeviceChassis` type
            device_image (list): list of :class:`DeviceImage` type
            physical_role (list): list of :class:`PhysicalRole` type
            overlay_role (list): list of :class:`OverlayRole` type
            telemetry_profile (list): list of :class:`TelemetryProfile` type
            tag (list): list of :class:`Tag` type
            physical_router_junos_service_ports (instance): instance of :class:`JunosServicePorts`
            telemetry_info (instance): instance of :class:`TelemetryStateInfo`
            physical_router_device_family (instance): instance of :class:`xsd:string`
            physical_router_os_version (instance): instance of :class:`xsd:string`
            physical_router_hostname (instance): instance of :class:`xsd:string`
            physical_router_management_ip (instance): instance of :class:`xsd:string`
            physical_router_management_mac (instance): instance of :class:`xsd:string`
            physical_router_dataplane_ip (instance): instance of :class:`xsd:string`
            physical_router_loopback_ip (instance): instance of :class:`xsd:string`
            physical_router_replicator_loopback_ip (instance): instance of :class:`xsd:string`
            physical_router_vendor_name (instance): instance of :class:`xsd:string`
            physical_router_product_name (instance): instance of :class:`xsd:string`
            physical_router_serial_number (instance): instance of :class:`xsd:string`
            physical_router_vnc_managed (instance): instance of :class:`xsd:boolean`
            physical_router_underlay_managed (instance): instance of :class:`xsd:boolean`
            physical_router_role (instance): instance of :class:`xsd:string`
            routing_bridging_roles (instance): instance of :class:`RoutingBridgingRolesType`
            physical_router_snmp (instance): instance of :class:`xsd:boolean`
            physical_router_lldp (instance): instance of :class:`xsd:boolean`
            physical_router_user_credentials (instance): instance of :class:`UserCredentials`
            physical_router_encryption_type (instance): instance of :class:`xsd:string`
            physical_router_snmp_credentials (instance): instance of :class:`SNMPCredentials`
            physical_router_dhcp_parameters (instance): instance of :class:`DnsmasqLeaseParameters`
            physical_router_cli_commit_state (instance): instance of :class:`xsd:string`
            physical_router_managed_state (instance): instance of :class:`xsd:string`
            physical_router_underlay_config (instance): instance of :class:`xsd:string`
            physical_router_supplemental_config (instance): instance of :class:`xsd:string`
            physical_router_autonomous_system (instance): instance of :class:`AutonomousSystemsType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PhysicalRouterTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not physical_router_name:
            self._name = 'default-physical-router'
        else:
            self._name = physical_router_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_router_refs:
            for ln in virtual_router_refs:
                self.add_virtual_router (ln)
        if bgp_router_refs:
            for ln in bgp_router_refs:
                self.add_bgp_router (ln)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if intent_map_refs:
            for ln in intent_map_refs:
                self.add_intent_map (ln)
        if fabric_refs:
            for ln in fabric_refs:
                self.add_fabric (ln)
        if node_profile_refs:
            for ln in node_profile_refs:
                self.add_node_profile (ln)
        if device_functional_group_refs:
            for ln in device_functional_group_refs:
                self.add_device_functional_group (ln)
        if device_chassis_refs:
            for ln in device_chassis_refs:
                self.add_device_chassis (ln)
        if device_image_refs:
            for ln in device_image_refs:
                self.add_device_image (ln)
        if physical_role_refs:
            for ln in physical_role_refs:
                self.add_physical_role (ln)
        if overlay_role_refs:
            for ln in overlay_role_refs:
                self.add_overlay_role (ln)
        if telemetry_profile_refs:
            for ln in telemetry_profile_refs:
                self.add_telemetry_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.physical_router_junos_service_ports = physical_router_junos_service_ports
        self.telemetry_info = telemetry_info
        self.physical_router_device_family = physical_router_device_family
        self.physical_router_os_version = physical_router_os_version
        self.physical_router_hostname = physical_router_hostname
        self.physical_router_management_ip = physical_router_management_ip
        self.physical_router_management_mac = physical_router_management_mac
        self.physical_router_dataplane_ip = physical_router_dataplane_ip
        self.physical_router_loopback_ip = physical_router_loopback_ip
        self.physical_router_replicator_loopback_ip = physical_router_replicator_loopback_ip
        self.physical_router_vendor_name = physical_router_vendor_name
        self.physical_router_product_name = physical_router_product_name
        self.physical_router_serial_number = physical_router_serial_number
        self.physical_router_vnc_managed = physical_router_vnc_managed
        self.physical_router_underlay_managed = physical_router_underlay_managed
        self.physical_router_role = physical_router_role
        self.routing_bridging_roles = routing_bridging_roles
        self.physical_router_snmp = physical_router_snmp
        self.physical_router_lldp = physical_router_lldp
        self.physical_router_user_credentials = physical_router_user_credentials
        self.physical_router_encryption_type = physical_router_encryption_type
        self.physical_router_snmp_credentials = physical_router_snmp_credentials
        self.physical_router_dhcp_parameters = physical_router_dhcp_parameters
        self.physical_router_cli_commit_state = physical_router_cli_commit_state
        self.physical_router_managed_state = physical_router_managed_state
        self.physical_router_underlay_config = physical_router_underlay_config
        self.physical_router_supplemental_config = physical_router_supplemental_config
        self.physical_router_autonomous_system = physical_router_autonomous_system
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_routers ():
            self.add_virtual_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgp_routers ():
            self.add_bgp_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_intent_maps ():
            self.add_intent_map (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_fabrics ():
            self.add_fabric (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_node_profiles ():
            self.add_node_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_device_functional_groups ():
            self.add_device_functional_group (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_device_chassiss ():
            self.add_device_chassis (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_device_images ():
            self.add_device_image (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_roles ():
            self.add_physical_role (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_overlay_roles ():
            self.add_overlay_role (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_telemetry_profiles ():
            self.add_telemetry_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualRouter` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`VirtualRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_router (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('virtual_router', cfixture.ConrtailLink('virtual_router', 'physical_router', 'virtual_router', ['ref'], lo))
    # end add_virtual_router_link

    def get_virtual_routers (self):
        return self.get_links ('virtual_router')
    # end get_virtual_routers
    def add_bgp_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`BgpRouter` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`BgpRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_bgp_router (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('bgp_router', cfixture.ConrtailLink('bgp_router', 'physical_router', 'bgp_router', ['ref'], lo))
    # end add_bgp_router_link

    def get_bgp_routers (self):
        return self.get_links ('bgp_router')
    # end get_bgp_routers
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'physical_router', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_intent_map (self, lo, update_server = True, add_link = True):
        '''
        add :class:`IntentMap` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`IntentMap`): obj to link
        '''
        if self._obj:
            self._obj.add_intent_map (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('intent_map', cfixture.ConrtailLink('intent_map', 'physical_router', 'intent_map', ['ref'], lo))
    # end add_intent_map_link

    def get_intent_maps (self):
        return self.get_links ('intent_map')
    # end get_intent_maps
    def add_fabric (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Fabric` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`Fabric`): obj to link
        '''
        if self._obj:
            self._obj.add_fabric (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('fabric', cfixture.ConrtailLink('fabric', 'physical_router', 'fabric', ['ref'], lo))
    # end add_fabric_link

    def get_fabrics (self):
        return self.get_links ('fabric')
    # end get_fabrics
    def add_node_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`NodeProfile` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`NodeProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_node_profile (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('node_profile', cfixture.ConrtailLink('node_profile', 'physical_router', 'node_profile', ['ref'], lo))
    # end add_node_profile_link

    def get_node_profiles (self):
        return self.get_links ('node_profile')
    # end get_node_profiles
    def add_device_functional_group (self, lo, update_server = True, add_link = True):
        '''
        add :class:`DeviceFunctionalGroup` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`DeviceFunctionalGroup`): obj to link
        '''
        if self._obj:
            self._obj.add_device_functional_group (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('device_functional_group', cfixture.ConrtailLink('device_functional_group', 'physical_router', 'device_functional_group', ['ref'], lo))
    # end add_device_functional_group_link

    def get_device_functional_groups (self):
        return self.get_links ('device_functional_group')
    # end get_device_functional_groups
    def add_device_chassis (self, lo, update_server = True, add_link = True):
        '''
        add :class:`DeviceChassis` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`DeviceChassis`): obj to link
        '''
        if self._obj:
            self._obj.add_device_chassis (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('device_chassis', cfixture.ConrtailLink('device_chassis', 'physical_router', 'device_chassis', ['ref'], lo))
    # end add_device_chassis_link

    def get_device_chassiss (self):
        return self.get_links ('device_chassis')
    # end get_device_chassiss
    def add_device_image (self, lo, update_server = True, add_link = True):
        '''
        add :class:`DeviceImage` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`DeviceImage`): obj to link
        '''
        if self._obj:
            self._obj.add_device_image (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('device_image', cfixture.ConrtailLink('device_image', 'physical_router', 'device_image', ['ref'], lo))
    # end add_device_image_link

    def get_device_images (self):
        return self.get_links ('device_image')
    # end get_device_images
    def add_physical_role (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRole` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`PhysicalRole`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_role (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('physical_role', cfixture.ConrtailLink('physical_role', 'physical_router', 'physical_role', ['ref'], lo))
    # end add_physical_role_link

    def get_physical_roles (self):
        return self.get_links ('physical_role')
    # end get_physical_roles
    def add_overlay_role (self, lo, update_server = True, add_link = True):
        '''
        add :class:`OverlayRole` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`OverlayRole`): obj to link
        '''
        if self._obj:
            self._obj.add_overlay_role (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('overlay_role', cfixture.ConrtailLink('overlay_role', 'physical_router', 'overlay_role', ['ref'], lo))
    # end add_overlay_role_link

    def get_overlay_roles (self):
        return self.get_links ('overlay_role')
    # end get_overlay_roles
    def add_telemetry_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`TelemetryProfile` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`TelemetryProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_telemetry_profile (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('telemetry_profile', cfixture.ConrtailLink('telemetry_profile', 'physical_router', 'telemetry_profile', ['ref'], lo))
    # end add_telemetry_profile_link

    def get_telemetry_profiles (self):
        return self.get_links ('telemetry_profile')
    # end get_telemetry_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PhysicalRouter`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.physical_router_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'physical_router', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_physical_router_junos_service_ports(self.physical_router_junos_service_ports or vnc_api.gen.resource_xsd.JunosServicePorts.populate())
        self._obj.set_telemetry_info(self.telemetry_info or vnc_api.gen.resource_xsd.TelemetryStateInfo.populate())
        self._obj.set_physical_router_device_family(self.physical_router_device_family or GeneratedsSuper.populate_string("physical_router_device_family"))
        self._obj.set_physical_router_os_version(self.physical_router_os_version or GeneratedsSuper.populate_string("physical_router_os_version"))
        self._obj.set_physical_router_hostname(self.physical_router_hostname or GeneratedsSuper.populate_string("physical_router_hostname"))
        self._obj.set_physical_router_management_ip(self.physical_router_management_ip or GeneratedsSuper.populate_string("physical_router_management_ip"))
        self._obj.set_physical_router_management_mac(self.physical_router_management_mac or GeneratedsSuper.populate_string("physical_router_management_mac"))
        self._obj.set_physical_router_dataplane_ip(self.physical_router_dataplane_ip or GeneratedsSuper.populate_string("physical_router_dataplane_ip"))
        self._obj.set_physical_router_loopback_ip(self.physical_router_loopback_ip or GeneratedsSuper.populate_string("physical_router_loopback_ip"))
        self._obj.set_physical_router_replicator_loopback_ip(self.physical_router_replicator_loopback_ip or GeneratedsSuper.populate_string("physical_router_replicator_loopback_ip"))
        self._obj.set_physical_router_vendor_name(self.physical_router_vendor_name or GeneratedsSuper.populate_string("physical_router_vendor_name"))
        self._obj.set_physical_router_product_name(self.physical_router_product_name or GeneratedsSuper.populate_string("physical_router_product_name"))
        self._obj.set_physical_router_serial_number(self.physical_router_serial_number or GeneratedsSuper.populate_string("physical_router_serial_number"))
        self._obj.set_physical_router_vnc_managed(self.physical_router_vnc_managed or GeneratedsSuper.populate_boolean("physical_router_vnc_managed"))
        self._obj.set_physical_router_underlay_managed(self.physical_router_underlay_managed or GeneratedsSuper.populate_boolean("physical_router_underlay_managed"))
        self._obj.set_physical_router_role(self.physical_router_role or GeneratedsSuper.populate_string("physical_router_role"))
        self._obj.set_routing_bridging_roles(self.routing_bridging_roles or vnc_api.gen.resource_xsd.RoutingBridgingRolesType.populate())
        self._obj.set_physical_router_snmp(self.physical_router_snmp or GeneratedsSuper.populate_boolean("physical_router_snmp"))
        self._obj.set_physical_router_lldp(self.physical_router_lldp or GeneratedsSuper.populate_boolean("physical_router_lldp"))
        self._obj.set_physical_router_user_credentials(self.physical_router_user_credentials or vnc_api.gen.resource_xsd.UserCredentials.populate())
        self._obj.set_physical_router_encryption_type(self.physical_router_encryption_type or GeneratedsSuper.populate_string("physical_router_encryption_type"))
        self._obj.set_physical_router_snmp_credentials(self.physical_router_snmp_credentials or vnc_api.gen.resource_xsd.SNMPCredentials.populate())
        self._obj.set_physical_router_dhcp_parameters(self.physical_router_dhcp_parameters or vnc_api.gen.resource_xsd.DnsmasqLeaseParameters.populate())
        self._obj.set_physical_router_cli_commit_state(self.physical_router_cli_commit_state or GeneratedsSuper.populate_string("physical_router_cli_commit_state"))
        self._obj.set_physical_router_managed_state(self.physical_router_managed_state or GeneratedsSuper.populate_string("physical_router_managed_state"))
        self._obj.set_physical_router_underlay_config(self.physical_router_underlay_config or GeneratedsSuper.populate_string("physical_router_underlay_config"))
        self._obj.set_physical_router_supplemental_config(self.physical_router_supplemental_config or GeneratedsSuper.populate_string("physical_router_supplemental_config"))
        self._obj.set_physical_router_autonomous_system(self.physical_router_autonomous_system or vnc_api.gen.resource_xsd.AutonomousSystemsType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PhysicalRouterTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.PhysicalRouter(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.physical_router_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.physical_router_junos_service_ports = self.physical_router_junos_service_ports
                self._obj.telemetry_info = self.telemetry_info
                self._obj.physical_router_device_family = self.physical_router_device_family
                self._obj.physical_router_os_version = self.physical_router_os_version
                self._obj.physical_router_hostname = self.physical_router_hostname
                self._obj.physical_router_management_ip = self.physical_router_management_ip
                self._obj.physical_router_management_mac = self.physical_router_management_mac
                self._obj.physical_router_dataplane_ip = self.physical_router_dataplane_ip
                self._obj.physical_router_loopback_ip = self.physical_router_loopback_ip
                self._obj.physical_router_replicator_loopback_ip = self.physical_router_replicator_loopback_ip
                self._obj.physical_router_vendor_name = self.physical_router_vendor_name
                self._obj.physical_router_product_name = self.physical_router_product_name
                self._obj.physical_router_serial_number = self.physical_router_serial_number
                self._obj.physical_router_vnc_managed = self.physical_router_vnc_managed
                self._obj.physical_router_underlay_managed = self.physical_router_underlay_managed
                self._obj.physical_router_role = self.physical_router_role
                self._obj.routing_bridging_roles = self.routing_bridging_roles
                self._obj.physical_router_snmp = self.physical_router_snmp
                self._obj.physical_router_lldp = self.physical_router_lldp
                self._obj.physical_router_user_credentials = self.physical_router_user_credentials
                self._obj.physical_router_encryption_type = self.physical_router_encryption_type
                self._obj.physical_router_snmp_credentials = self.physical_router_snmp_credentials
                self._obj.physical_router_dhcp_parameters = self.physical_router_dhcp_parameters
                self._obj.physical_router_cli_commit_state = self.physical_router_cli_commit_state
                self._obj.physical_router_managed_state = self.physical_router_managed_state
                self._obj.physical_router_underlay_config = self.physical_router_underlay_config
                self._obj.physical_router_supplemental_config = self.physical_router_supplemental_config
                self._obj.physical_router_autonomous_system = self.physical_router_autonomous_system
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.physical_router_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.physical_router_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.physical_router_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_physical_routers() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.physical_routers.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PhysicalRouterTestFixtureGen

class ServiceTemplateTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceTemplate`
    """
    def __init__(self, conn_drv, service_template_name=None, parent_fixt=None, auto_prop_val=False, service_appliance_set_refs = None, tag_refs = None, service_template_properties=None, service_config_managed=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceTemplateTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_template_name (str): Name of service_template
            parent_fixt (:class:`.DomainTestFixtureGen`): Parent fixture
            service_appliance_set (list): list of :class:`ServiceApplianceSet` type
            tag (list): list of :class:`Tag` type
            service_template_properties (instance): instance of :class:`ServiceTemplateType`
            service_config_managed (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceTemplateTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_template_name:
            self._name = 'default-service-template'
        else:
            self._name = service_template_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_appliance_set_refs:
            for ln in service_appliance_set_refs:
                self.add_service_appliance_set (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_template_properties = service_template_properties
        self.service_config_managed = service_config_managed
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_appliance_sets ():
            self.add_service_appliance_set (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_appliance_set (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceApplianceSet` link to :class:`ServiceTemplate`
        Args:
            lo (:class:`ServiceApplianceSet`): obj to link
        '''
        if self._obj:
            self._obj.add_service_appliance_set (lo)
            if update_server:
                self._conn_drv.service_template_update (self._obj)

        if add_link:
            self.add_link('service_appliance_set', cfixture.ConrtailLink('service_appliance_set', 'service_template', 'service_appliance_set', ['ref'], lo))
    # end add_service_appliance_set_link

    def get_service_appliance_sets (self):
        return self.get_links ('service_appliance_set')
    # end get_service_appliance_sets
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceTemplate`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_template_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_template', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_template_properties(self.service_template_properties or vnc_api.gen.resource_xsd.ServiceTemplateType.populate())
        self._obj.set_service_config_managed(self.service_config_managed or GeneratedsSuper.populate_boolean("service_config_managed"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceTemplateTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(DomainTestFixtureGen(self._conn_drv, 'default-domain'))

        self._obj = vnc_api.ServiceTemplate(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_template_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_template_properties = self.service_template_properties
                self._obj.service_config_managed = self.service_config_managed
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_template_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_template_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_template_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_templates() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_templates.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceTemplateTestFixtureGen

class HardwareInventoryTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.HardwareInventory`
    """
    def __init__(self, conn_drv, hardware_inventory_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, hardware_inventory_inventory_info=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create HardwareInventoryTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            hardware_inventory_name (str): Name of hardware_inventory
            parent_fixt (:class:`.PhysicalRouterTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            hardware_inventory_inventory_info (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(HardwareInventoryTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not hardware_inventory_name:
            self._name = 'default-hardware-inventory'
        else:
            self._name = hardware_inventory_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.hardware_inventory_inventory_info = hardware_inventory_inventory_info
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`HardwareInventory`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.hardware_inventory_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'hardware_inventory', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_hardware_inventory_inventory_info(self.hardware_inventory_inventory_info or GeneratedsSuper.populate_string("hardware_inventory_inventory_info"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(HardwareInventoryTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(PhysicalRouterTestFixtureGen(self._conn_drv, 'default-physical-router'))

        self._obj = vnc_api.HardwareInventory(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.hardware_inventory_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.hardware_inventory_inventory_info = self.hardware_inventory_inventory_info
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.hardware_inventory_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.hardware_inventory_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.hardware_inventory_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_hardware_inventorys() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.hardware_inventorys.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class HardwareInventoryTestFixtureGen

class FirewallPolicyTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FirewallPolicy`
    """
    def __init__(self, conn_drv, firewall_policy_name=None, parent_fixt=None, auto_prop_val=False, firewall_rule_ref_infos = None, security_logging_object_ref_infos = None, tag_refs = None, draft_mode_state=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FirewallPolicyTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            firewall_policy_name (str): Name of firewall_policy
            parent_fixt (:class:`.PolicyManagementTestFixtureGen`): Parent fixture
            firewall_rule (list): list of tuple (:class:`FirewallRule`, :class: `FirewallSequence`) type
            security_logging_object (list): list of tuple (:class:`SecurityLoggingObject`, :class: `SloRateType`) type
            tag (list): list of :class:`Tag` type
            draft_mode_state (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FirewallPolicyTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not firewall_policy_name:
            self._name = 'default-firewall-policy'
        else:
            self._name = firewall_policy_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if firewall_rule_ref_infos:
            for ln, ref in firewall_rule_ref_infos:
                self.add_firewall_rule (ln, ref)
        if security_logging_object_ref_infos:
            for ln, ref in security_logging_object_ref_infos:
                self.add_security_logging_object (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.draft_mode_state = draft_mode_state
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_firewall_rules ():
            self.add_firewall_rule (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_security_logging_objects ():
            self.add_security_logging_object (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_firewall_rule (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`FirewallRule` link to :class:`FirewallPolicy`
        Args:
            lo (:class:`FirewallRule`): obj to link
            ref (:class:`FirewallSequence`): property of the link object
        '''
        if self._obj:
            self._obj.add_firewall_rule (lo, ref)
            if update_server:
                self._conn_drv.firewall_policy_update (self._obj)

        if add_link:
            self.add_link('firewall_rule', cfixture.ConrtailLink('firewall_rule', 'firewall_policy', 'firewall_rule', ['ref'], (lo, ref)))
    # end add_firewall_rule_link

    def get_firewall_rules (self):
        return self.get_links ('firewall_rule')
    # end get_firewall_rules
    def add_security_logging_object (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`SecurityLoggingObject` link to :class:`FirewallPolicy`
        Args:
            lo (:class:`SecurityLoggingObject`): obj to link
            ref (:class:`SloRateType`): property of the link object
        '''
        if self._obj:
            self._obj.add_security_logging_object (lo, ref)
            if update_server:
                self._conn_drv.firewall_policy_update (self._obj)

        if add_link:
            self.add_link('security_logging_object', cfixture.ConrtailLink('security_logging_object', 'firewall_policy', 'security_logging_object', ['ref'], (lo, ref)))
    # end add_security_logging_object_link

    def get_security_logging_objects (self):
        return self.get_links ('security_logging_object')
    # end get_security_logging_objects
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FirewallPolicy`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.firewall_policy_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'firewall_policy', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_draft_mode_state(self.draft_mode_state or GeneratedsSuper.populate_string("draft_mode_state"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FirewallPolicyTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'policy-management', 'project']")

        self._obj = vnc_api.FirewallPolicy(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.firewall_policy_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.draft_mode_state = self.draft_mode_state
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.firewall_policy_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.firewall_policy_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.firewall_policy_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_firewall_policys() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.firewall_policys.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FirewallPolicyTestFixtureGen

class RouteTableTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RouteTable`
    """
    def __init__(self, conn_drv, route_table_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, routes=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RouteTableTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            route_table_name (str): Name of route_table
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            routes (instance): instance of :class:`RouteTableType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RouteTableTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not route_table_name:
            self._name = 'default-route-table'
        else:
            self._name = route_table_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.routes = routes
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RouteTable`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.route_table_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'route_table', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_routes(self.routes or vnc_api.gen.resource_xsd.RouteTableType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RouteTableTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.RouteTable(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.route_table_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.routes = self.routes
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.route_table_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.route_table_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.route_table_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_route_tables() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.route_tables.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RouteTableTestFixtureGen

class ProviderAttachmentTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ProviderAttachment`
    """
    def __init__(self, conn_drv, provider_attachment_name=None, auto_prop_val=False, virtual_router_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ProviderAttachmentTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            virtual_router (list): list of :class:`VirtualRouter` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ProviderAttachmentTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not provider_attachment_name:
            self._name = 'default-provider-attachment'
        else:
            self._name = provider_attachment_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if virtual_router_refs:
            for ln in virtual_router_refs:
                self.add_virtual_router (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_routers ():
            self.add_virtual_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualRouter` link to :class:`ProviderAttachment`
        Args:
            lo (:class:`VirtualRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_router (lo)
            if update_server:
                self._conn_drv.provider_attachment_update (self._obj)

        if add_link:
            self.add_link('virtual_router', cfixture.ConrtailLink('virtual_router', 'provider_attachment', 'virtual_router', ['ref'], lo))
    # end add_virtual_router_link

    def get_virtual_routers (self):
        return self.get_links ('virtual_router')
    # end get_virtual_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ProviderAttachment`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.provider_attachment_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'provider_attachment', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ProviderAttachmentTestFixtureGen, self).setUp()
        self._obj = vnc_api.ProviderAttachment(self._name)
        try:
            self._obj = self._conn_drv.provider_attachment_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.provider_attachment_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.provider_attachment_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.provider_attachment_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ProviderAttachmentTestFixtureGen

class OverlayRoleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.OverlayRole`
    """
    def __init__(self, conn_drv, overlay_role_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create OverlayRoleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            overlay_role_name (str): Name of overlay_role
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(OverlayRoleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not overlay_role_name:
            self._name = 'default-overlay-role'
        else:
            self._name = overlay_role_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`OverlayRole`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.overlay_role_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'overlay_role', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(OverlayRoleTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.OverlayRole(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.overlay_role_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.overlay_role_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.overlay_role_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.overlay_role_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_overlay_roles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.overlay_roles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class OverlayRoleTestFixtureGen

class MulticastPolicyTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.MulticastPolicy`
    """
    def __init__(self, conn_drv, multicast_policy_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, multicast_source_groups=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create MulticastPolicyTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            multicast_policy_name (str): Name of multicast_policy
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            multicast_source_groups (instance): instance of :class:`MulticastSourceGroups`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(MulticastPolicyTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not multicast_policy_name:
            self._name = 'default-multicast-policy'
        else:
            self._name = multicast_policy_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.multicast_source_groups = multicast_source_groups
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`MulticastPolicy`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.multicast_policy_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'multicast_policy', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_multicast_source_groups(self.multicast_source_groups or vnc_api.gen.resource_xsd.MulticastSourceGroups.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(MulticastPolicyTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.MulticastPolicy(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.multicast_policy_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.multicast_source_groups = self.multicast_source_groups
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.multicast_policy_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.multicast_policy_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.multicast_policy_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_multicast_policys() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.multicast_policys.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class MulticastPolicyTestFixtureGen

class NetworkDeviceConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.NetworkDeviceConfig`
    """
    def __init__(self, conn_drv, network_device_config_name=None, auto_prop_val=False, physical_router_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NetworkDeviceConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            physical_router (list): list of :class:`PhysicalRouter` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NetworkDeviceConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not network_device_config_name:
            self._name = 'default-network-device-config'
        else:
            self._name = network_device_config_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if physical_router_refs:
            for ln in physical_router_refs:
                self.add_physical_router (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_routers ():
            self.add_physical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRouter` link to :class:`NetworkDeviceConfig`
        Args:
            lo (:class:`PhysicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_router (lo)
            if update_server:
                self._conn_drv.network_device_config_update (self._obj)

        if add_link:
            self.add_link('physical_router', cfixture.ConrtailLink('physical_router', 'network_device_config', 'physical_router', ['ref'], lo))
    # end add_physical_router_link

    def get_physical_routers (self):
        return self.get_links ('physical_router')
    # end get_physical_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`NetworkDeviceConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.network_device_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'network_device_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NetworkDeviceConfigTestFixtureGen, self).setUp()
        self._obj = vnc_api.NetworkDeviceConfig(self._name)
        try:
            self._obj = self._conn_drv.network_device_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.network_device_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.network_device_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.network_device_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NetworkDeviceConfigTestFixtureGen

class VirtualDnsRecordTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualDnsRecord`
    """
    def __init__(self, conn_drv, virtual_DNS_record_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, virtual_DNS_record_data=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualDnsRecordTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_DNS_record_name (str): Name of virtual_DNS_record
            parent_fixt (:class:`.VirtualDnsTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            virtual_DNS_record_data (instance): instance of :class:`VirtualDnsRecordType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualDnsRecordTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_DNS_record_name:
            self._name = 'default-virtual-DNS-record'
        else:
            self._name = virtual_DNS_record_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.virtual_DNS_record_data = virtual_DNS_record_data
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualDnsRecord`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_DNS_record_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_DNS_record', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_virtual_DNS_record_data(self.virtual_DNS_record_data or vnc_api.gen.resource_xsd.VirtualDnsRecordType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualDnsRecordTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(VirtualDnsTestFixtureGen(self._conn_drv, 'default-virtual-DNS'))

        self._obj = vnc_api.VirtualDnsRecord(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_DNS_record_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.virtual_DNS_record_data = self.virtual_DNS_record_data
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_DNS_record_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_DNS_record_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_DNS_record_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_DNS_records() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_DNS_records.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualDnsRecordTestFixtureGen

class ControlNodeZoneTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ControlNodeZone`
    """
    def __init__(self, conn_drv, control_node_zone_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ControlNodeZoneTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            control_node_zone_name (str): Name of control_node_zone
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ControlNodeZoneTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not control_node_zone_name:
            self._name = 'default-control-node-zone'
        else:
            self._name = control_node_zone_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ControlNodeZone`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.control_node_zone_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'control_node_zone', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ControlNodeZoneTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.ControlNodeZone(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.control_node_zone_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.control_node_zone_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.control_node_zone_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.control_node_zone_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_control_node_zones() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.control_node_zones.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ControlNodeZoneTestFixtureGen

class DsaRuleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DsaRule`
    """
    def __init__(self, conn_drv, dsa_rule_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, dsa_rule_entry=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DsaRuleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            dsa_rule_name (str): Name of dsa_rule
            parent_fixt (:class:`.DiscoveryServiceAssignmentTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            dsa_rule_entry (instance): instance of :class:`DiscoveryServiceAssignmentType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DsaRuleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not dsa_rule_name:
            self._name = 'default-dsa-rule'
        else:
            self._name = dsa_rule_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.dsa_rule_entry = dsa_rule_entry
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DsaRule`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.dsa_rule_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'dsa_rule', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_dsa_rule_entry(self.dsa_rule_entry or vnc_api.gen.resource_xsd.DiscoveryServiceAssignmentType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DsaRuleTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(DiscoveryServiceAssignmentTestFixtureGen(self._conn_drv, 'default-discovery-service-assignment'))

        self._obj = vnc_api.DsaRule(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.dsa_rule_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.dsa_rule_entry = self.dsa_rule_entry
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.dsa_rule_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.dsa_rule_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.dsa_rule_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_dsa_rules() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.dsa_rules.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DsaRuleTestFixtureGen

class StructuredSyslogConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StructuredSyslogConfig`
    """
    def __init__(self, conn_drv, structured_syslog_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StructuredSyslogConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            structured_syslog_config_name (str): Name of structured_syslog_config
            parent_fixt (:class:`.GlobalAnalyticsConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StructuredSyslogConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not structured_syslog_config_name:
            self._name = 'default-structured-syslog-config'
        else:
            self._name = structured_syslog_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StructuredSyslogConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.structured_syslog_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'structured_syslog_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StructuredSyslogConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'global-analytics-config', 'project']")

        self._obj = vnc_api.StructuredSyslogConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.structured_syslog_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.structured_syslog_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.structured_syslog_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.structured_syslog_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_structured_syslog_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.structured_syslog_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StructuredSyslogConfigTestFixtureGen

class DiscoveryServiceAssignmentTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DiscoveryServiceAssignment`
    """
    def __init__(self, conn_drv, discovery_service_assignment_name=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DiscoveryServiceAssignmentTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DiscoveryServiceAssignmentTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not discovery_service_assignment_name:
            self._name = 'default-discovery-service-assignment'
        else:
            self._name = discovery_service_assignment_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DiscoveryServiceAssignment`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.discovery_service_assignment_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'discovery_service_assignment', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DiscoveryServiceAssignmentTestFixtureGen, self).setUp()
        self._obj = vnc_api.DiscoveryServiceAssignment(self._name)
        try:
            self._obj = self._conn_drv.discovery_service_assignment_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.discovery_service_assignment_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.discovery_service_assignment_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.discovery_service_assignment_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DiscoveryServiceAssignmentTestFixtureGen

class LogicalInterfaceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LogicalInterface`
    """
    def __init__(self, conn_drv, logical_interface_name=None, parent_fixt=None, auto_prop_val=False, virtual_machine_interface_refs = None, tag_refs = None, logical_interface_vlan_tag=None, logical_interface_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LogicalInterfaceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            logical_interface_name (str): Name of logical_interface
            parent_fixt (:class:`.PhysicalRouterTestFixtureGen`): Parent fixture
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            logical_interface_vlan_tag (instance): instance of :class:`xsd:integer`
            logical_interface_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LogicalInterfaceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not logical_interface_name:
            self._name = 'default-logical-interface'
        else:
            self._name = logical_interface_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.logical_interface_vlan_tag = logical_interface_vlan_tag
        self.logical_interface_type = logical_interface_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`LogicalInterface`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.logical_interface_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'logical_interface', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LogicalInterface`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.logical_interface_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'logical_interface', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_logical_interface_vlan_tag(self.logical_interface_vlan_tag or GeneratedsSuper.populate_integer("logical_interface_vlan_tag"))
        self._obj.set_logical_interface_type(self.logical_interface_type or GeneratedsSuper.populate_string("logical_interface_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LogicalInterfaceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("['physical-router', 'physical-interface']")

        self._obj = vnc_api.LogicalInterface(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.logical_interface_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.logical_interface_vlan_tag = self.logical_interface_vlan_tag
                self._obj.logical_interface_type = self.logical_interface_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.logical_interface_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.logical_interface_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.logical_interface_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_logical_interfaces() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.logical_interfaces.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LogicalInterfaceTestFixtureGen

class FlowNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FlowNode`
    """
    def __init__(self, conn_drv, flow_node_name=None, parent_fixt=None, auto_prop_val=False, virtual_network_refs = None, tag_refs = None, flow_node_ip_address=None, flow_node_load_balancer_ip=None, flow_node_inband_interface=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FlowNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            flow_node_name (str): Name of flow_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            virtual_network (list): list of :class:`VirtualNetwork` type
            tag (list): list of :class:`Tag` type
            flow_node_ip_address (instance): instance of :class:`xsd:string`
            flow_node_load_balancer_ip (instance): instance of :class:`xsd:string`
            flow_node_inband_interface (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FlowNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not flow_node_name:
            self._name = 'default-flow-node'
        else:
            self._name = flow_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.flow_node_ip_address = flow_node_ip_address
        self.flow_node_load_balancer_ip = flow_node_load_balancer_ip
        self.flow_node_inband_interface = flow_node_inband_interface
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`FlowNode`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.flow_node_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'flow_node', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FlowNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.flow_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'flow_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_flow_node_ip_address(self.flow_node_ip_address or GeneratedsSuper.populate_string("flow_node_ip_address"))
        self._obj.set_flow_node_load_balancer_ip(self.flow_node_load_balancer_ip or GeneratedsSuper.populate_string("flow_node_load_balancer_ip"))
        self._obj.set_flow_node_inband_interface(self.flow_node_inband_interface or GeneratedsSuper.populate_string("flow_node_inband_interface"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FlowNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.FlowNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.flow_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.flow_node_ip_address = self.flow_node_ip_address
                self._obj.flow_node_load_balancer_ip = self.flow_node_load_balancer_ip
                self._obj.flow_node_inband_interface = self.flow_node_inband_interface
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.flow_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.flow_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.flow_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_flow_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.flow_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FlowNodeTestFixtureGen

class PortGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PortGroup`
    """
    def __init__(self, conn_drv, port_group_name=None, parent_fixt=None, auto_prop_val=False, port_refs = None, tag_refs = None, bms_port_group_info=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PortGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            port_group_name (str): Name of port_group
            parent_fixt (:class:`.NodeTestFixtureGen`): Parent fixture
            port (list): list of :class:`Port` type
            tag (list): list of :class:`Tag` type
            bms_port_group_info (instance): instance of :class:`BaremetalPortGroupInfo`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PortGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not port_group_name:
            self._name = 'default-port-group'
        else:
            self._name = port_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if port_refs:
            for ln in port_refs:
                self.add_port (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.bms_port_group_info = bms_port_group_info
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_ports ():
            self.add_port (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_port (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Port` link to :class:`PortGroup`
        Args:
            lo (:class:`Port`): obj to link
        '''
        if self._obj:
            self._obj.add_port (lo)
            if update_server:
                self._conn_drv.port_group_update (self._obj)

        if add_link:
            self.add_link('port', cfixture.ConrtailLink('port', 'port_group', 'port', ['ref'], lo))
    # end add_port_link

    def get_ports (self):
        return self.get_links ('port')
    # end get_ports
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PortGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.port_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'port_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_bms_port_group_info(self.bms_port_group_info or vnc_api.gen.resource_xsd.BaremetalPortGroupInfo.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PortGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(NodeTestFixtureGen(self._conn_drv, 'default-node'))

        self._obj = vnc_api.PortGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.port_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.bms_port_group_info = self.bms_port_group_info
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.port_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.port_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.port_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_port_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.port_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PortGroupTestFixtureGen

class RouteAggregateTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RouteAggregate`
    """
    def __init__(self, conn_drv, route_aggregate_name=None, parent_fixt=None, auto_prop_val=False, service_instance_ref_infos = None, routing_instance_refs = None, tag_refs = None, aggregate_route_entries=None, aggregate_route_nexthop=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RouteAggregateTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            route_aggregate_name (str): Name of route_aggregate
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_instance (list): list of tuple (:class:`ServiceInstance`, :class: `ServiceInterfaceTag`) type
            routing_instance (list): list of :class:`RoutingInstance` type
            tag (list): list of :class:`Tag` type
            aggregate_route_entries (instance): instance of :class:`RouteListType`
            aggregate_route_nexthop (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RouteAggregateTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not route_aggregate_name:
            self._name = 'default-route-aggregate'
        else:
            self._name = route_aggregate_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_instance_ref_infos:
            for ln, ref in service_instance_ref_infos:
                self.add_service_instance (ln, ref)
        if routing_instance_refs:
            for ln in routing_instance_refs:
                self.add_routing_instance (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.aggregate_route_entries = aggregate_route_entries
        self.aggregate_route_nexthop = aggregate_route_nexthop
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_routing_instances ():
            self.add_routing_instance (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`RouteAggregate`
        Args:
            lo (:class:`ServiceInstance`): obj to link
            ref (:class:`ServiceInterfaceTag`): property of the link object
        '''
        if self._obj:
            self._obj.add_service_instance (lo, ref)
            if update_server:
                self._conn_drv.route_aggregate_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'route_aggregate', 'service_instance', ['ref'], (lo, ref)))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_routing_instance (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RoutingInstance` link to :class:`RouteAggregate`
        Args:
            lo (:class:`RoutingInstance`): obj to link
        '''
        if self._obj:
            self._obj.add_routing_instance (lo)
            if update_server:
                self._conn_drv.route_aggregate_update (self._obj)

        if add_link:
            self.add_link('routing_instance', cfixture.ConrtailLink('routing_instance', 'route_aggregate', 'routing_instance', ['ref'], lo))
    # end add_routing_instance_link

    def get_routing_instances (self):
        return self.get_links ('routing_instance')
    # end get_routing_instances
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RouteAggregate`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.route_aggregate_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'route_aggregate', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_aggregate_route_entries(self.aggregate_route_entries or vnc_api.gen.resource_xsd.RouteListType.populate())
        self._obj.set_aggregate_route_nexthop(self.aggregate_route_nexthop or GeneratedsSuper.populate_string("aggregate_route_nexthop"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RouteAggregateTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.RouteAggregate(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.route_aggregate_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.aggregate_route_entries = self.aggregate_route_entries
                self._obj.aggregate_route_nexthop = self.aggregate_route_nexthop
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.route_aggregate_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.route_aggregate_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.route_aggregate_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_route_aggregates() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.route_aggregates.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RouteAggregateTestFixtureGen

class LogicalRouterTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LogicalRouter`
    """
    def __init__(self, conn_drv, logical_router_name=None, parent_fixt=None, auto_prop_val=False, virtual_machine_interface_refs = None, route_target_refs = None, route_table_refs = None, virtual_network_ref_infos = None, service_instance_refs = None, physical_router_refs = None, bgpvpn_refs = None, tag_refs = None, configured_route_target_list=None, vxlan_network_identifier=None, logical_router_dhcp_relay_server=None, logical_router_gateway_external=None, logical_router_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LogicalRouterTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            logical_router_name (str): Name of logical_router
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            route_target (list): list of :class:`RouteTarget` type
            route_table (list): list of :class:`RouteTable` type
            virtual_network (list): list of tuple (:class:`VirtualNetwork`, :class: `LogicalRouterVirtualNetworkType`) type
            service_instance (list): list of :class:`ServiceInstance` type
            physical_router (list): list of :class:`PhysicalRouter` type
            bgpvpn (list): list of :class:`Bgpvpn` type
            tag (list): list of :class:`Tag` type
            configured_route_target_list (instance): instance of :class:`RouteTargetList`
            vxlan_network_identifier (instance): instance of :class:`xsd:string`
            logical_router_dhcp_relay_server (instance): instance of :class:`IpAddressesType`
            logical_router_gateway_external (instance): instance of :class:`xsd:boolean`
            logical_router_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LogicalRouterTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not logical_router_name:
            self._name = 'default-logical-router'
        else:
            self._name = logical_router_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if route_target_refs:
            for ln in route_target_refs:
                self.add_route_target (ln)
        if route_table_refs:
            for ln in route_table_refs:
                self.add_route_table (ln)
        if virtual_network_ref_infos:
            for ln, ref in virtual_network_ref_infos:
                self.add_virtual_network (ln, ref)
        if service_instance_refs:
            for ln in service_instance_refs:
                self.add_service_instance (ln)
        if physical_router_refs:
            for ln in physical_router_refs:
                self.add_physical_router (ln)
        if bgpvpn_refs:
            for ln in bgpvpn_refs:
                self.add_bgpvpn (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.configured_route_target_list = configured_route_target_list
        self.vxlan_network_identifier = vxlan_network_identifier
        self.logical_router_dhcp_relay_server = logical_router_dhcp_relay_server
        self.logical_router_gateway_external = logical_router_gateway_external
        self.logical_router_type = logical_router_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_route_targets ():
            self.add_route_target (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_route_tables ():
            self.add_route_table (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_instances ():
            self.add_service_instance (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_routers ():
            self.add_physical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgpvpns ():
            self.add_bgpvpn (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`LogicalRouter`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'logical_router', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_route_target (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RouteTarget` link to :class:`LogicalRouter`
        Args:
            lo (:class:`RouteTarget`): obj to link
        '''
        if self._obj:
            self._obj.add_route_target (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('route_target', cfixture.ConrtailLink('route_target', 'logical_router', 'route_target', ['ref'], lo))
    # end add_route_target_link

    def get_route_targets (self):
        return self.get_links ('route_target')
    # end get_route_targets
    def add_route_table (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RouteTable` link to :class:`LogicalRouter`
        Args:
            lo (:class:`RouteTable`): obj to link
        '''
        if self._obj:
            self._obj.add_route_table (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('route_table', cfixture.ConrtailLink('route_table', 'logical_router', 'route_table', ['ref'], lo))
    # end add_route_table_link

    def get_route_tables (self):
        return self.get_links ('route_table')
    # end get_route_tables
    def add_virtual_network (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`LogicalRouter`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
            ref (:class:`LogicalRouterVirtualNetworkType`): property of the link object
        '''
        if self._obj:
            self._obj.add_virtual_network (lo, ref)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'logical_router', 'virtual_network', ['ref'], (lo, ref)))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_service_instance (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`LogicalRouter`
        Args:
            lo (:class:`ServiceInstance`): obj to link
        '''
        if self._obj:
            self._obj.add_service_instance (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'logical_router', 'service_instance', ['ref'], lo))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_physical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRouter` link to :class:`LogicalRouter`
        Args:
            lo (:class:`PhysicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_router (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('physical_router', cfixture.ConrtailLink('physical_router', 'logical_router', 'physical_router', ['ref'], lo))
    # end add_physical_router_link

    def get_physical_routers (self):
        return self.get_links ('physical_router')
    # end get_physical_routers
    def add_bgpvpn (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Bgpvpn` link to :class:`LogicalRouter`
        Args:
            lo (:class:`Bgpvpn`): obj to link
        '''
        if self._obj:
            self._obj.add_bgpvpn (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('bgpvpn', cfixture.ConrtailLink('bgpvpn', 'logical_router', 'bgpvpn', ['ref'], lo))
    # end add_bgpvpn_link

    def get_bgpvpns (self):
        return self.get_links ('bgpvpn')
    # end get_bgpvpns
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LogicalRouter`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.logical_router_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'logical_router', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_configured_route_target_list(self.configured_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_vxlan_network_identifier(self.vxlan_network_identifier or GeneratedsSuper.populate_string("vxlan_network_identifier"))
        self._obj.set_logical_router_dhcp_relay_server(self.logical_router_dhcp_relay_server or vnc_api.gen.resource_xsd.IpAddressesType.populate())
        self._obj.set_logical_router_gateway_external(self.logical_router_gateway_external or GeneratedsSuper.populate_boolean("logical_router_gateway_external"))
        self._obj.set_logical_router_type(self.logical_router_type or GeneratedsSuper.populate_string("logical_router_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LogicalRouterTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.LogicalRouter(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.logical_router_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.configured_route_target_list = self.configured_route_target_list
                self._obj.vxlan_network_identifier = self.vxlan_network_identifier
                self._obj.logical_router_dhcp_relay_server = self.logical_router_dhcp_relay_server
                self._obj.logical_router_gateway_external = self.logical_router_gateway_external
                self._obj.logical_router_type = self.logical_router_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.logical_router_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.logical_router_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.logical_router_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_logical_routers() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.logical_routers.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LogicalRouterTestFixtureGen

class DomainTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Domain`
    """
    def __init__(self, conn_drv, domain_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, domain_limits=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DomainTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            domain_name (str): Name of domain
            parent_fixt (:class:`.ConfigRootTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            domain_limits (instance): instance of :class:`DomainLimitsType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DomainTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not domain_name:
            self._name = 'default-domain'
        else:
            self._name = domain_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.domain_limits = domain_limits
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Domain`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.domain_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'domain', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_domain_limits(self.domain_limits or vnc_api.gen.resource_xsd.DomainLimitsType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DomainTestFixtureGen, self).setUp()
        # child of config-root
        self._obj = vnc_api.Domain(self._name)
        try:
            self._obj = self._conn_drv.domain_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.domain_limits = self.domain_limits
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.domain_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.domain_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.domain_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_domains() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.domains.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DomainTestFixtureGen

class StructuredSyslogHostnameRecordTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StructuredSyslogHostnameRecord`
    """
    def __init__(self, conn_drv, structured_syslog_hostname_record_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, structured_syslog_hostaddr=None, structured_syslog_tenant=None, structured_syslog_location=None, structured_syslog_device=None, structured_syslog_hostname_tags=None, structured_syslog_linkmap=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StructuredSyslogHostnameRecordTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            structured_syslog_hostname_record_name (str): Name of structured_syslog_hostname_record
            parent_fixt (:class:`.StructuredSyslogConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            structured_syslog_hostaddr (instance): instance of :class:`xsd:string`
            structured_syslog_tenant (instance): instance of :class:`xsd:string`
            structured_syslog_location (instance): instance of :class:`xsd:string`
            structured_syslog_device (instance): instance of :class:`xsd:string`
            structured_syslog_hostname_tags (instance): instance of :class:`xsd:string`
            structured_syslog_linkmap (instance): instance of :class:`StructuredSyslogLinkmap`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StructuredSyslogHostnameRecordTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not structured_syslog_hostname_record_name:
            self._name = 'default-structured-syslog-hostname-record'
        else:
            self._name = structured_syslog_hostname_record_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.structured_syslog_hostaddr = structured_syslog_hostaddr
        self.structured_syslog_tenant = structured_syslog_tenant
        self.structured_syslog_location = structured_syslog_location
        self.structured_syslog_device = structured_syslog_device
        self.structured_syslog_hostname_tags = structured_syslog_hostname_tags
        self.structured_syslog_linkmap = structured_syslog_linkmap
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StructuredSyslogHostnameRecord`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.structured_syslog_hostname_record_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'structured_syslog_hostname_record', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_structured_syslog_hostaddr(self.structured_syslog_hostaddr or GeneratedsSuper.populate_string("structured_syslog_hostaddr"))
        self._obj.set_structured_syslog_tenant(self.structured_syslog_tenant or GeneratedsSuper.populate_string("structured_syslog_tenant"))
        self._obj.set_structured_syslog_location(self.structured_syslog_location or GeneratedsSuper.populate_string("structured_syslog_location"))
        self._obj.set_structured_syslog_device(self.structured_syslog_device or GeneratedsSuper.populate_string("structured_syslog_device"))
        self._obj.set_structured_syslog_hostname_tags(self.structured_syslog_hostname_tags or GeneratedsSuper.populate_string("structured_syslog_hostname_tags"))
        self._obj.set_structured_syslog_linkmap(self.structured_syslog_linkmap or vnc_api.gen.resource_xsd.StructuredSyslogLinkmap.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StructuredSyslogHostnameRecordTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(StructuredSyslogConfigTestFixtureGen(self._conn_drv, 'default-structured-syslog-config'))

        self._obj = vnc_api.StructuredSyslogHostnameRecord(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.structured_syslog_hostname_record_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.structured_syslog_hostaddr = self.structured_syslog_hostaddr
                self._obj.structured_syslog_tenant = self.structured_syslog_tenant
                self._obj.structured_syslog_location = self.structured_syslog_location
                self._obj.structured_syslog_device = self.structured_syslog_device
                self._obj.structured_syslog_hostname_tags = self.structured_syslog_hostname_tags
                self._obj.structured_syslog_linkmap = self.structured_syslog_linkmap
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.structured_syslog_hostname_record_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.structured_syslog_hostname_record_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.structured_syslog_hostname_record_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_structured_syslog_hostname_records() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.structured_syslog_hostname_records.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StructuredSyslogHostnameRecordTestFixtureGen

class ServiceInstanceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceInstance`
    """
    def __init__(self, conn_drv, service_instance_name=None, parent_fixt=None, auto_prop_val=False, service_template_refs = None, instance_ip_ref_infos = None, tag_refs = None, service_instance_properties=None, service_instance_bindings=None, service_instance_bgp_enabled=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceInstanceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_instance_name (str): Name of service_instance
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_template (list): list of :class:`ServiceTemplate` type
            instance_ip (list): list of tuple (:class:`InstanceIp`, :class: `ServiceInterfaceTag`) type
            tag (list): list of :class:`Tag` type
            service_instance_properties (instance): instance of :class:`ServiceInstanceType`
            service_instance_bindings (instance): instance of :class:`KeyValuePairs`
            service_instance_bgp_enabled (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceInstanceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_instance_name:
            self._name = 'default-service-instance'
        else:
            self._name = service_instance_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_template_refs:
            for ln in service_template_refs:
                self.add_service_template (ln)
        if instance_ip_ref_infos:
            for ln, ref in instance_ip_ref_infos:
                self.add_instance_ip (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_instance_properties = service_instance_properties
        self.service_instance_bindings = service_instance_bindings
        self.service_instance_bgp_enabled = service_instance_bgp_enabled
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_templates ():
            self.add_service_template (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_instance_ips ():
            self.add_instance_ip (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_template (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceTemplate` link to :class:`ServiceInstance`
        Args:
            lo (:class:`ServiceTemplate`): obj to link
        '''
        if self._obj:
            self._obj.add_service_template (lo)
            if update_server:
                self._conn_drv.service_instance_update (self._obj)

        if add_link:
            self.add_link('service_template', cfixture.ConrtailLink('service_template', 'service_instance', 'service_template', ['ref'], lo))
    # end add_service_template_link

    def get_service_templates (self):
        return self.get_links ('service_template')
    # end get_service_templates
    def add_instance_ip (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`InstanceIp` link to :class:`ServiceInstance`
        Args:
            lo (:class:`InstanceIp`): obj to link
            ref (:class:`ServiceInterfaceTag`): property of the link object
        '''
        if self._obj:
            self._obj.add_instance_ip (lo, ref)
            if update_server:
                self._conn_drv.service_instance_update (self._obj)

        if add_link:
            self.add_link('instance_ip', cfixture.ConrtailLink('instance_ip', 'service_instance', 'instance_ip', ['ref'], (lo, ref)))
    # end add_instance_ip_link

    def get_instance_ips (self):
        return self.get_links ('instance_ip')
    # end get_instance_ips
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceInstance`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_instance_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_instance', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_instance_properties(self.service_instance_properties or vnc_api.gen.resource_xsd.ServiceInstanceType.populate())
        self._obj.set_service_instance_bindings(self.service_instance_bindings or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_service_instance_bgp_enabled(self.service_instance_bgp_enabled or GeneratedsSuper.populate_boolean("service_instance_bgp_enabled"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceInstanceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.ServiceInstance(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_instance_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_instance_properties = self.service_instance_properties
                self._obj.service_instance_bindings = self.service_instance_bindings
                self._obj.service_instance_bgp_enabled = self.service_instance_bgp_enabled
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_instance_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_instance_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_instance_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_instances() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_instances.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceInstanceTestFixtureGen

class NodeProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.NodeProfile`
    """
    def __init__(self, conn_drv, node_profile_name=None, parent_fixt=None, auto_prop_val=False, job_template_refs = None, hardware_refs = None, role_definition_refs = None, tag_refs = None, node_profile_type=None, node_profile_vendor=None, node_profile_device_family=None, node_profile_hitless_upgrade=None, node_profile_roles=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NodeProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            node_profile_name (str): Name of node_profile
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            job_template (list): list of :class:`JobTemplate` type
            hardware (list): list of :class:`Hardware` type
            role_definition (list): list of :class:`RoleDefinition` type
            tag (list): list of :class:`Tag` type
            node_profile_type (instance): instance of :class:`xsd:string`
            node_profile_vendor (instance): instance of :class:`xsd:string`
            node_profile_device_family (instance): instance of :class:`xsd:string`
            node_profile_hitless_upgrade (instance): instance of :class:`xsd:boolean`
            node_profile_roles (instance): instance of :class:`NodeProfileRolesType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NodeProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not node_profile_name:
            self._name = 'default-node-profile'
        else:
            self._name = node_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if job_template_refs:
            for ln in job_template_refs:
                self.add_job_template (ln)
        if hardware_refs:
            for ln in hardware_refs:
                self.add_hardware (ln)
        if role_definition_refs:
            for ln in role_definition_refs:
                self.add_role_definition (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.node_profile_type = node_profile_type
        self.node_profile_vendor = node_profile_vendor
        self.node_profile_device_family = node_profile_device_family
        self.node_profile_hitless_upgrade = node_profile_hitless_upgrade
        self.node_profile_roles = node_profile_roles
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_job_templates ():
            self.add_job_template (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_hardwares ():
            self.add_hardware (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_role_definitions ():
            self.add_role_definition (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_job_template (self, lo, update_server = True, add_link = True):
        '''
        add :class:`JobTemplate` link to :class:`NodeProfile`
        Args:
            lo (:class:`JobTemplate`): obj to link
        '''
        if self._obj:
            self._obj.add_job_template (lo)
            if update_server:
                self._conn_drv.node_profile_update (self._obj)

        if add_link:
            self.add_link('job_template', cfixture.ConrtailLink('job_template', 'node_profile', 'job_template', ['ref'], lo))
    # end add_job_template_link

    def get_job_templates (self):
        return self.get_links ('job_template')
    # end get_job_templates
    def add_hardware (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Hardware` link to :class:`NodeProfile`
        Args:
            lo (:class:`Hardware`): obj to link
        '''
        if self._obj:
            self._obj.add_hardware (lo)
            if update_server:
                self._conn_drv.node_profile_update (self._obj)

        if add_link:
            self.add_link('hardware', cfixture.ConrtailLink('hardware', 'node_profile', 'hardware', ['ref'], lo))
    # end add_hardware_link

    def get_hardwares (self):
        return self.get_links ('hardware')
    # end get_hardwares
    def add_role_definition (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RoleDefinition` link to :class:`NodeProfile`
        Args:
            lo (:class:`RoleDefinition`): obj to link
        '''
        if self._obj:
            self._obj.add_role_definition (lo)
            if update_server:
                self._conn_drv.node_profile_update (self._obj)

        if add_link:
            self.add_link('role_definition', cfixture.ConrtailLink('role_definition', 'node_profile', 'role_definition', ['ref'], lo))
    # end add_role_definition_link

    def get_role_definitions (self):
        return self.get_links ('role_definition')
    # end get_role_definitions
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`NodeProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.node_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'node_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_node_profile_type(self.node_profile_type or GeneratedsSuper.populate_string("node_profile_type"))
        self._obj.set_node_profile_vendor(self.node_profile_vendor or GeneratedsSuper.populate_string("node_profile_vendor"))
        self._obj.set_node_profile_device_family(self.node_profile_device_family or GeneratedsSuper.populate_string("node_profile_device_family"))
        self._obj.set_node_profile_hitless_upgrade(self.node_profile_hitless_upgrade or GeneratedsSuper.populate_boolean("node_profile_hitless_upgrade"))
        self._obj.set_node_profile_roles(self.node_profile_roles or vnc_api.gen.resource_xsd.NodeProfileRolesType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NodeProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.NodeProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.node_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.node_profile_type = self.node_profile_type
                self._obj.node_profile_vendor = self.node_profile_vendor
                self._obj.node_profile_device_family = self.node_profile_device_family
                self._obj.node_profile_hitless_upgrade = self.node_profile_hitless_upgrade
                self._obj.node_profile_roles = self.node_profile_roles
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.node_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.node_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.node_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_node_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.node_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NodeProfileTestFixtureGen

class BridgeDomainTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.BridgeDomain`
    """
    def __init__(self, conn_drv, bridge_domain_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, mac_learning_enabled=None, mac_limit_control=None, mac_move_control=None, mac_aging_time=None, isid=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create BridgeDomainTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            bridge_domain_name (str): Name of bridge_domain
            parent_fixt (:class:`.VirtualNetworkTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            mac_learning_enabled (instance): instance of :class:`xsd:boolean`
            mac_limit_control (instance): instance of :class:`MACLimitControlType`
            mac_move_control (instance): instance of :class:`MACMoveLimitControlType`
            mac_aging_time (instance): instance of :class:`xsd:integer`
            isid (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(BridgeDomainTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not bridge_domain_name:
            self._name = 'default-bridge-domain'
        else:
            self._name = bridge_domain_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.mac_learning_enabled = mac_learning_enabled
        self.mac_limit_control = mac_limit_control
        self.mac_move_control = mac_move_control
        self.mac_aging_time = mac_aging_time
        self.isid = isid
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`BridgeDomain`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.bridge_domain_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'bridge_domain', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_mac_learning_enabled(self.mac_learning_enabled or GeneratedsSuper.populate_boolean("mac_learning_enabled"))
        self._obj.set_mac_limit_control(self.mac_limit_control or vnc_api.gen.resource_xsd.MACLimitControlType.populate())
        self._obj.set_mac_move_control(self.mac_move_control or vnc_api.gen.resource_xsd.MACMoveLimitControlType.populate())
        self._obj.set_mac_aging_time(self.mac_aging_time or GeneratedsSuper.populate_integer("mac_aging_time"))
        self._obj.set_isid(self.isid or GeneratedsSuper.populate_integer("isid"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(BridgeDomainTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(VirtualNetworkTestFixtureGen(self._conn_drv, 'default-virtual-network'))

        self._obj = vnc_api.BridgeDomain(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.bridge_domain_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.mac_learning_enabled = self.mac_learning_enabled
                self._obj.mac_limit_control = self.mac_limit_control
                self._obj.mac_move_control = self.mac_move_control
                self._obj.mac_aging_time = self.mac_aging_time
                self._obj.isid = self.isid
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.bridge_domain_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.bridge_domain_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.bridge_domain_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_bridge_domains() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.bridge_domains.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class BridgeDomainTestFixtureGen

class AliasIpTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AliasIp`
    """
    def __init__(self, conn_drv, alias_ip_name=None, parent_fixt=None, auto_prop_val=False, project_refs = None, virtual_machine_interface_refs = None, tag_refs = None, alias_ip_address=None, alias_ip_address_family=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AliasIpTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            alias_ip_name (str): Name of alias_ip
            parent_fixt (:class:`.AliasIpPoolTestFixtureGen`): Parent fixture
            project (list): list of :class:`Project` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            alias_ip_address (instance): instance of :class:`xsd:string`
            alias_ip_address_family (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AliasIpTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not alias_ip_name:
            self._name = 'default-alias-ip'
        else:
            self._name = alias_ip_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if project_refs:
            for ln in project_refs:
                self.add_project (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.alias_ip_address = alias_ip_address
        self.alias_ip_address_family = alias_ip_address_family
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_projects ():
            self.add_project (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_project (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Project` link to :class:`AliasIp`
        Args:
            lo (:class:`Project`): obj to link
        '''
        if self._obj:
            self._obj.add_project (lo)
            if update_server:
                self._conn_drv.alias_ip_update (self._obj)

        if add_link:
            self.add_link('project', cfixture.ConrtailLink('project', 'alias_ip', 'project', ['ref'], lo))
    # end add_project_link

    def get_projects (self):
        return self.get_links ('project')
    # end get_projects
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`AliasIp`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.alias_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'alias_ip', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AliasIp`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.alias_ip_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'alias_ip', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_alias_ip_address(self.alias_ip_address or GeneratedsSuper.populate_string("alias_ip_address"))
        self._obj.set_alias_ip_address_family(self.alias_ip_address_family or GeneratedsSuper.populate_string("alias_ip_address_family"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AliasIpTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(AliasIpPoolTestFixtureGen(self._conn_drv, 'default-alias-ip-pool'))

        self._obj = vnc_api.AliasIp(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.alias_ip_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.alias_ip_address = self.alias_ip_address
                self._obj.alias_ip_address_family = self.alias_ip_address_family
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.alias_ip_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.alias_ip_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.alias_ip_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_alias_ips() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.alias_ips.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AliasIpTestFixtureGen

class WebuiNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.WebuiNode`
    """
    def __init__(self, conn_drv, webui_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, webui_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create WebuiNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            webui_node_name (str): Name of webui_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            webui_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(WebuiNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not webui_node_name:
            self._name = 'default-webui-node'
        else:
            self._name = webui_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.webui_node_ip_address = webui_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`WebuiNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.webui_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'webui_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_webui_node_ip_address(self.webui_node_ip_address or GeneratedsSuper.populate_string("webui_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(WebuiNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.WebuiNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.webui_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.webui_node_ip_address = self.webui_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.webui_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.webui_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.webui_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_webui_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.webui_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class WebuiNodeTestFixtureGen

class PortTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Port`
    """
    def __init__(self, conn_drv, port_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, port_group_uuid=None, bms_port_info=None, esxi_port_info=None, label=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PortTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            port_name (str): Name of port
            parent_fixt (:class:`.NodeTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            port_group_uuid (instance): instance of :class:`xsd:string`
            bms_port_info (instance): instance of :class:`BaremetalPortInfo`
            esxi_port_info (instance): instance of :class:`ESXIProperties`
            label (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PortTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not port_name:
            self._name = 'default-port'
        else:
            self._name = port_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.port_group_uuid = port_group_uuid
        self.bms_port_info = bms_port_info
        self.esxi_port_info = esxi_port_info
        self.label = label
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Port`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.port_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'port', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_port_group_uuid(self.port_group_uuid or GeneratedsSuper.populate_string("port_group_uuid"))
        self._obj.set_bms_port_info(self.bms_port_info or vnc_api.gen.resource_xsd.BaremetalPortInfo.populate())
        self._obj.set_esxi_port_info(self.esxi_port_info or vnc_api.gen.resource_xsd.ESXIProperties.populate())
        self._obj.set_label(self.label or GeneratedsSuper.populate_string("label"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PortTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(NodeTestFixtureGen(self._conn_drv, 'default-node'))

        self._obj = vnc_api.Port(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.port_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.port_group_uuid = self.port_group_uuid
                self._obj.bms_port_info = self.bms_port_info
                self._obj.esxi_port_info = self.esxi_port_info
                self._obj.label = self.label
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.port_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.port_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.port_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_ports() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.ports.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PortTestFixtureGen

class BgpAsAServiceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.BgpAsAService`
    """
    def __init__(self, conn_drv, bgp_as_a_service_name=None, parent_fixt=None, auto_prop_val=False, control_node_zone_ref_infos = None, virtual_machine_interface_refs = None, service_health_check_refs = None, bgp_router_refs = None, tag_refs = None, autonomous_system=None, bgpaas_shared=None, bgpaas_ip_address=None, bgpaas_session_attributes=None, bgpaas_ipv4_mapped_ipv6_nexthop=None, bgpaas_suppress_route_advertisement=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create BgpAsAServiceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            bgp_as_a_service_name (str): Name of bgp_as_a_service
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            control_node_zone (list): list of tuple (:class:`ControlNodeZone`, :class: `BGPaaSControlNodeZoneAttributes`) type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            service_health_check (list): list of :class:`ServiceHealthCheck` type
            bgp_router (list): list of :class:`BgpRouter` type
            tag (list): list of :class:`Tag` type
            autonomous_system (instance): instance of :class:`xsd:integer`
            bgpaas_shared (instance): instance of :class:`xsd:boolean`
            bgpaas_ip_address (instance): instance of :class:`xsd:string`
            bgpaas_session_attributes (instance): instance of :class:`BgpSessionAttributes`
            bgpaas_ipv4_mapped_ipv6_nexthop (instance): instance of :class:`xsd:boolean`
            bgpaas_suppress_route_advertisement (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(BgpAsAServiceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not bgp_as_a_service_name:
            self._name = 'default-bgp-as-a-service'
        else:
            self._name = bgp_as_a_service_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if control_node_zone_ref_infos:
            for ln, ref in control_node_zone_ref_infos:
                self.add_control_node_zone (ln, ref)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if service_health_check_refs:
            for ln in service_health_check_refs:
                self.add_service_health_check (ln)
        if bgp_router_refs:
            for ln in bgp_router_refs:
                self.add_bgp_router (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.autonomous_system = autonomous_system
        self.bgpaas_shared = bgpaas_shared
        self.bgpaas_ip_address = bgpaas_ip_address
        self.bgpaas_session_attributes = bgpaas_session_attributes
        self.bgpaas_ipv4_mapped_ipv6_nexthop = bgpaas_ipv4_mapped_ipv6_nexthop
        self.bgpaas_suppress_route_advertisement = bgpaas_suppress_route_advertisement
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_control_node_zones ():
            self.add_control_node_zone (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_health_checks ():
            self.add_service_health_check (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgp_routers ():
            self.add_bgp_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_control_node_zone (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`ControlNodeZone` link to :class:`BgpAsAService`
        Args:
            lo (:class:`ControlNodeZone`): obj to link
            ref (:class:`BGPaaSControlNodeZoneAttributes`): property of the link object
        '''
        if self._obj:
            self._obj.add_control_node_zone (lo, ref)
            if update_server:
                self._conn_drv.bgp_as_a_service_update (self._obj)

        if add_link:
            self.add_link('control_node_zone', cfixture.ConrtailLink('control_node_zone', 'bgp_as_a_service', 'control_node_zone', ['ref'], (lo, ref)))
    # end add_control_node_zone_link

    def get_control_node_zones (self):
        return self.get_links ('control_node_zone')
    # end get_control_node_zones
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`BgpAsAService`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.bgp_as_a_service_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'bgp_as_a_service', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_service_health_check (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceHealthCheck` link to :class:`BgpAsAService`
        Args:
            lo (:class:`ServiceHealthCheck`): obj to link
        '''
        if self._obj:
            self._obj.add_service_health_check (lo)
            if update_server:
                self._conn_drv.bgp_as_a_service_update (self._obj)

        if add_link:
            self.add_link('service_health_check', cfixture.ConrtailLink('service_health_check', 'bgp_as_a_service', 'service_health_check', ['ref'], lo))
    # end add_service_health_check_link

    def get_service_health_checks (self):
        return self.get_links ('service_health_check')
    # end get_service_health_checks
    def add_bgp_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`BgpRouter` link to :class:`BgpAsAService`
        Args:
            lo (:class:`BgpRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_bgp_router (lo)
            if update_server:
                self._conn_drv.bgp_as_a_service_update (self._obj)

        if add_link:
            self.add_link('bgp_router', cfixture.ConrtailLink('bgp_router', 'bgp_as_a_service', 'bgp_router', ['ref'], lo))
    # end add_bgp_router_link

    def get_bgp_routers (self):
        return self.get_links ('bgp_router')
    # end get_bgp_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`BgpAsAService`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.bgp_as_a_service_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'bgp_as_a_service', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_autonomous_system(self.autonomous_system or GeneratedsSuper.populate_integer("autonomous_system"))
        self._obj.set_bgpaas_shared(self.bgpaas_shared or GeneratedsSuper.populate_boolean("bgpaas_shared"))
        self._obj.set_bgpaas_ip_address(self.bgpaas_ip_address or GeneratedsSuper.populate_string("bgpaas_ip_address"))
        self._obj.set_bgpaas_session_attributes(self.bgpaas_session_attributes or vnc_api.gen.resource_xsd.BgpSessionAttributes.populate())
        self._obj.set_bgpaas_ipv4_mapped_ipv6_nexthop(self.bgpaas_ipv4_mapped_ipv6_nexthop or GeneratedsSuper.populate_boolean("bgpaas_ipv4_mapped_ipv6_nexthop"))
        self._obj.set_bgpaas_suppress_route_advertisement(self.bgpaas_suppress_route_advertisement or GeneratedsSuper.populate_boolean("bgpaas_suppress_route_advertisement"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(BgpAsAServiceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.BgpAsAService(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.bgp_as_a_service_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.autonomous_system = self.autonomous_system
                self._obj.bgpaas_shared = self.bgpaas_shared
                self._obj.bgpaas_ip_address = self.bgpaas_ip_address
                self._obj.bgpaas_session_attributes = self.bgpaas_session_attributes
                self._obj.bgpaas_ipv4_mapped_ipv6_nexthop = self.bgpaas_ipv4_mapped_ipv6_nexthop
                self._obj.bgpaas_suppress_route_advertisement = self.bgpaas_suppress_route_advertisement
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.bgp_as_a_service_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.bgp_as_a_service_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.bgp_as_a_service_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_bgp_as_a_services() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.bgp_as_a_services.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class BgpAsAServiceTestFixtureGen

class SubnetTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Subnet`
    """
    def __init__(self, conn_drv, subnet_name=None, auto_prop_val=False, virtual_machine_interface_refs = None, tag_refs = None, subnet_ip_prefix=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create SubnetTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            subnet_ip_prefix (instance): instance of :class:`SubnetType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(SubnetTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not subnet_name:
            self._name = 'default-subnet'
        else:
            self._name = subnet_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.subnet_ip_prefix = subnet_ip_prefix
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`Subnet`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.subnet_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'subnet', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Subnet`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.subnet_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'subnet', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_subnet_ip_prefix(self.subnet_ip_prefix or vnc_api.gen.resource_xsd.SubnetType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(SubnetTestFixtureGen, self).setUp()
        self._obj = vnc_api.Subnet(self._name)
        try:
            self._obj = self._conn_drv.subnet_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.subnet_ip_prefix = self.subnet_ip_prefix
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.subnet_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.subnet_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.subnet_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class SubnetTestFixtureGen

class GlobalSystemConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.GlobalSystemConfig`
    """
    def __init__(self, conn_drv, global_system_config_name=None, parent_fixt=None, auto_prop_val=False, bgp_router_refs = None, tag_refs = None, autonomous_system=None, enable_4byte_as=None, config_version=None, graceful_restart_parameters=None, plugin_tuning=None, data_center_interconnect_loopback_namespace=None, data_center_interconnect_asn_namespace=None, ibgp_auto_mesh=None, bgp_always_compare_med=None, rd_cluster_seed=None, ip_fabric_subnets=None, supported_device_families=None, supported_vendor_hardwares=None, bgpaas_parameters=None, mac_limit_control=None, mac_move_control=None, mac_aging_time=None, igmp_enable=None, alarm_enable=None, user_defined_log_statistics=None, enable_security_policy_draft=None, supported_fabric_annotations=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create GlobalSystemConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            global_system_config_name (str): Name of global_system_config
            parent_fixt (:class:`.ConfigRootTestFixtureGen`): Parent fixture
            bgp_router (list): list of :class:`BgpRouter` type
            tag (list): list of :class:`Tag` type
            autonomous_system (instance): instance of :class:`xsd:integer`
            enable_4byte_as (instance): instance of :class:`xsd:boolean`
            config_version (instance): instance of :class:`xsd:string`
            graceful_restart_parameters (instance): instance of :class:`GracefulRestartParametersType`
            plugin_tuning (instance): instance of :class:`PluginProperties`
            data_center_interconnect_loopback_namespace (instance): instance of :class:`SubnetListType`
            data_center_interconnect_asn_namespace (instance): instance of :class:`AsnRangeType`
            ibgp_auto_mesh (instance): instance of :class:`xsd:boolean`
            bgp_always_compare_med (instance): instance of :class:`xsd:boolean`
            rd_cluster_seed (instance): instance of :class:`xsd:integer`
            ip_fabric_subnets (instance): instance of :class:`SubnetListType`
            supported_device_families (instance): instance of :class:`DeviceFamilyListType`
            supported_vendor_hardwares (instance): instance of :class:`VendorHardwaresType`
            bgpaas_parameters (instance): instance of :class:`BGPaaServiceParametersType`
            mac_limit_control (instance): instance of :class:`MACLimitControlType`
            mac_move_control (instance): instance of :class:`MACMoveLimitControlType`
            mac_aging_time (instance): instance of :class:`xsd:integer`
            igmp_enable (instance): instance of :class:`xsd:boolean`
            alarm_enable (instance): instance of :class:`xsd:boolean`
            user_defined_log_statistics (instance): instance of :class:`UserDefinedLogStatList`
            enable_security_policy_draft (instance): instance of :class:`xsd:boolean`
            supported_fabric_annotations (instance): instance of :class:`KeyValuePairs`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(GlobalSystemConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not global_system_config_name:
            self._name = 'default-global-system-config'
        else:
            self._name = global_system_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if bgp_router_refs:
            for ln in bgp_router_refs:
                self.add_bgp_router (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.autonomous_system = autonomous_system
        self.enable_4byte_as = enable_4byte_as
        self.config_version = config_version
        self.graceful_restart_parameters = graceful_restart_parameters
        self.plugin_tuning = plugin_tuning
        self.data_center_interconnect_loopback_namespace = data_center_interconnect_loopback_namespace
        self.data_center_interconnect_asn_namespace = data_center_interconnect_asn_namespace
        self.ibgp_auto_mesh = ibgp_auto_mesh
        self.bgp_always_compare_med = bgp_always_compare_med
        self.rd_cluster_seed = rd_cluster_seed
        self.ip_fabric_subnets = ip_fabric_subnets
        self.supported_device_families = supported_device_families
        self.supported_vendor_hardwares = supported_vendor_hardwares
        self.bgpaas_parameters = bgpaas_parameters
        self.mac_limit_control = mac_limit_control
        self.mac_move_control = mac_move_control
        self.mac_aging_time = mac_aging_time
        self.igmp_enable = igmp_enable
        self.alarm_enable = alarm_enable
        self.user_defined_log_statistics = user_defined_log_statistics
        self.enable_security_policy_draft = enable_security_policy_draft
        self.supported_fabric_annotations = supported_fabric_annotations
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_bgp_routers ():
            self.add_bgp_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_bgp_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`BgpRouter` link to :class:`GlobalSystemConfig`
        Args:
            lo (:class:`BgpRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_bgp_router (lo)
            if update_server:
                self._conn_drv.global_system_config_update (self._obj)

        if add_link:
            self.add_link('bgp_router', cfixture.ConrtailLink('bgp_router', 'global_system_config', 'bgp_router', ['ref'], lo))
    # end add_bgp_router_link

    def get_bgp_routers (self):
        return self.get_links ('bgp_router')
    # end get_bgp_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`GlobalSystemConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.global_system_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'global_system_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_autonomous_system(self.autonomous_system or GeneratedsSuper.populate_integer("autonomous_system"))
        self._obj.set_enable_4byte_as(self.enable_4byte_as or GeneratedsSuper.populate_boolean("enable_4byte_as"))
        self._obj.set_config_version(self.config_version or GeneratedsSuper.populate_string("config_version"))
        self._obj.set_graceful_restart_parameters(self.graceful_restart_parameters or vnc_api.gen.resource_xsd.GracefulRestartParametersType.populate())
        self._obj.set_plugin_tuning(self.plugin_tuning or vnc_api.gen.resource_xsd.PluginProperties.populate())
        self._obj.set_data_center_interconnect_loopback_namespace(self.data_center_interconnect_loopback_namespace or vnc_api.gen.resource_xsd.SubnetListType.populate())
        self._obj.set_data_center_interconnect_asn_namespace(self.data_center_interconnect_asn_namespace or vnc_api.gen.resource_xsd.AsnRangeType.populate())
        self._obj.set_ibgp_auto_mesh(self.ibgp_auto_mesh or GeneratedsSuper.populate_boolean("ibgp_auto_mesh"))
        self._obj.set_bgp_always_compare_med(self.bgp_always_compare_med or GeneratedsSuper.populate_boolean("bgp_always_compare_med"))
        self._obj.set_rd_cluster_seed(self.rd_cluster_seed or GeneratedsSuper.populate_integer("rd_cluster_seed"))
        self._obj.set_ip_fabric_subnets(self.ip_fabric_subnets or vnc_api.gen.resource_xsd.SubnetListType.populate())
        self._obj.set_supported_device_families(self.supported_device_families or vnc_api.gen.resource_xsd.DeviceFamilyListType.populate())
        self._obj.set_supported_vendor_hardwares(self.supported_vendor_hardwares or vnc_api.gen.resource_xsd.VendorHardwaresType.populate())
        self._obj.set_bgpaas_parameters(self.bgpaas_parameters or vnc_api.gen.resource_xsd.BGPaaServiceParametersType.populate())
        self._obj.set_mac_limit_control(self.mac_limit_control or vnc_api.gen.resource_xsd.MACLimitControlType.populate())
        self._obj.set_mac_move_control(self.mac_move_control or vnc_api.gen.resource_xsd.MACMoveLimitControlType.populate())
        self._obj.set_mac_aging_time(self.mac_aging_time or GeneratedsSuper.populate_integer("mac_aging_time"))
        self._obj.set_igmp_enable(self.igmp_enable or GeneratedsSuper.populate_boolean("igmp_enable"))
        self._obj.set_alarm_enable(self.alarm_enable or GeneratedsSuper.populate_boolean("alarm_enable"))
        self._obj.set_user_defined_log_statistics(self.user_defined_log_statistics or vnc_api.gen.resource_xsd.UserDefinedLogStatList.populate())
        self._obj.set_enable_security_policy_draft(self.enable_security_policy_draft or GeneratedsSuper.populate_boolean("enable_security_policy_draft"))
        self._obj.set_supported_fabric_annotations(self.supported_fabric_annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(GlobalSystemConfigTestFixtureGen, self).setUp()
        # child of config-root
        self._obj = vnc_api.GlobalSystemConfig(self._name)
        try:
            self._obj = self._conn_drv.global_system_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.autonomous_system = self.autonomous_system
                self._obj.enable_4byte_as = self.enable_4byte_as
                self._obj.config_version = self.config_version
                self._obj.graceful_restart_parameters = self.graceful_restart_parameters
                self._obj.plugin_tuning = self.plugin_tuning
                self._obj.data_center_interconnect_loopback_namespace = self.data_center_interconnect_loopback_namespace
                self._obj.data_center_interconnect_asn_namespace = self.data_center_interconnect_asn_namespace
                self._obj.ibgp_auto_mesh = self.ibgp_auto_mesh
                self._obj.bgp_always_compare_med = self.bgp_always_compare_med
                self._obj.rd_cluster_seed = self.rd_cluster_seed
                self._obj.ip_fabric_subnets = self.ip_fabric_subnets
                self._obj.supported_device_families = self.supported_device_families
                self._obj.supported_vendor_hardwares = self.supported_vendor_hardwares
                self._obj.bgpaas_parameters = self.bgpaas_parameters
                self._obj.mac_limit_control = self.mac_limit_control
                self._obj.mac_move_control = self.mac_move_control
                self._obj.mac_aging_time = self.mac_aging_time
                self._obj.igmp_enable = self.igmp_enable
                self._obj.alarm_enable = self.alarm_enable
                self._obj.user_defined_log_statistics = self.user_defined_log_statistics
                self._obj.enable_security_policy_draft = self.enable_security_policy_draft
                self._obj.supported_fabric_annotations = self.supported_fabric_annotations
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.global_system_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.global_system_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.global_system_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_global_system_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.global_system_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class GlobalSystemConfigTestFixtureGen

class SubClusterTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.SubCluster`
    """
    def __init__(self, conn_drv, sub_cluster_name=None, auto_prop_val=False, tag_refs = None, sub_cluster_asn=None, sub_cluster_id=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create SubClusterTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            sub_cluster_asn (instance): instance of :class:`xsd:integer`
            sub_cluster_id (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(SubClusterTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not sub_cluster_name:
            self._name = 'default-sub-cluster'
        else:
            self._name = sub_cluster_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.sub_cluster_asn = sub_cluster_asn
        self.sub_cluster_id = sub_cluster_id
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`SubCluster`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.sub_cluster_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'sub_cluster', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_sub_cluster_asn(self.sub_cluster_asn or GeneratedsSuper.populate_integer("sub_cluster_asn"))
        self._obj.set_sub_cluster_id(self.sub_cluster_id or GeneratedsSuper.populate_integer("sub_cluster_id"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(SubClusterTestFixtureGen, self).setUp()
        self._obj = vnc_api.SubCluster(self._name)
        try:
            self._obj = self._conn_drv.sub_cluster_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.sub_cluster_asn = self.sub_cluster_asn
                self._obj.sub_cluster_id = self.sub_cluster_id
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.sub_cluster_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.sub_cluster_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.sub_cluster_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class SubClusterTestFixtureGen

class ForwardingClassTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ForwardingClass`
    """
    def __init__(self, conn_drv, forwarding_class_name=None, parent_fixt=None, auto_prop_val=False, qos_queue_refs = None, tag_refs = None, forwarding_class_id=None, forwarding_class_dscp=None, forwarding_class_vlan_priority=None, forwarding_class_mpls_exp=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ForwardingClassTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            forwarding_class_name (str): Name of forwarding_class
            parent_fixt (:class:`.GlobalQosConfigTestFixtureGen`): Parent fixture
            qos_queue (list): list of :class:`QosQueue` type
            tag (list): list of :class:`Tag` type
            forwarding_class_id (instance): instance of :class:`xsd:integer`
            forwarding_class_dscp (instance): instance of :class:`xsd:integer`
            forwarding_class_vlan_priority (instance): instance of :class:`xsd:integer`
            forwarding_class_mpls_exp (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ForwardingClassTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not forwarding_class_name:
            self._name = 'default-forwarding-class'
        else:
            self._name = forwarding_class_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if qos_queue_refs:
            for ln in qos_queue_refs:
                self.add_qos_queue (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.forwarding_class_id = forwarding_class_id
        self.forwarding_class_dscp = forwarding_class_dscp
        self.forwarding_class_vlan_priority = forwarding_class_vlan_priority
        self.forwarding_class_mpls_exp = forwarding_class_mpls_exp
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_qos_queues ():
            self.add_qos_queue (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_qos_queue (self, lo, update_server = True, add_link = True):
        '''
        add :class:`QosQueue` link to :class:`ForwardingClass`
        Args:
            lo (:class:`QosQueue`): obj to link
        '''
        if self._obj:
            self._obj.add_qos_queue (lo)
            if update_server:
                self._conn_drv.forwarding_class_update (self._obj)

        if add_link:
            self.add_link('qos_queue', cfixture.ConrtailLink('qos_queue', 'forwarding_class', 'qos_queue', ['ref'], lo))
    # end add_qos_queue_link

    def get_qos_queues (self):
        return self.get_links ('qos_queue')
    # end get_qos_queues
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ForwardingClass`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.forwarding_class_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'forwarding_class', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_forwarding_class_id(self.forwarding_class_id or GeneratedsSuper.populate_integer("forwarding_class_id"))
        self._obj.set_forwarding_class_dscp(self.forwarding_class_dscp or GeneratedsSuper.populate_integer("forwarding_class_dscp"))
        self._obj.set_forwarding_class_vlan_priority(self.forwarding_class_vlan_priority or GeneratedsSuper.populate_integer("forwarding_class_vlan_priority"))
        self._obj.set_forwarding_class_mpls_exp(self.forwarding_class_mpls_exp or GeneratedsSuper.populate_integer("forwarding_class_mpls_exp"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ForwardingClassTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalQosConfigTestFixtureGen(self._conn_drv, 'default-global-qos-config'))

        self._obj = vnc_api.ForwardingClass(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.forwarding_class_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.forwarding_class_id = self.forwarding_class_id
                self._obj.forwarding_class_dscp = self.forwarding_class_dscp
                self._obj.forwarding_class_vlan_priority = self.forwarding_class_vlan_priority
                self._obj.forwarding_class_mpls_exp = self.forwarding_class_mpls_exp
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.forwarding_class_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.forwarding_class_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.forwarding_class_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_forwarding_classs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.forwarding_classs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ForwardingClassTestFixtureGen

class ServiceGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceGroup`
    """
    def __init__(self, conn_drv, service_group_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, draft_mode_state=None, service_group_firewall_service_list=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_group_name (str): Name of service_group
            parent_fixt (:class:`.PolicyManagementTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            draft_mode_state (instance): instance of :class:`xsd:string`
            service_group_firewall_service_list (instance): instance of :class:`FirewallServiceGroupType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_group_name:
            self._name = 'default-service-group'
        else:
            self._name = service_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.draft_mode_state = draft_mode_state
        self.service_group_firewall_service_list = service_group_firewall_service_list
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_draft_mode_state(self.draft_mode_state or GeneratedsSuper.populate_string("draft_mode_state"))
        self._obj.set_service_group_firewall_service_list(self.service_group_firewall_service_list or vnc_api.gen.resource_xsd.FirewallServiceGroupType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'policy-management', 'project']")

        self._obj = vnc_api.ServiceGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.draft_mode_state = self.draft_mode_state
                self._obj.service_group_firewall_service_list = self.service_group_firewall_service_list
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceGroupTestFixtureGen

class GlobalAnalyticsConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.GlobalAnalyticsConfig`
    """
    def __init__(self, conn_drv, global_analytics_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create GlobalAnalyticsConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            global_analytics_config_name (str): Name of global_analytics_config
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(GlobalAnalyticsConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not global_analytics_config_name:
            self._name = 'default-global-analytics-config'
        else:
            self._name = global_analytics_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`GlobalAnalyticsConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.global_analytics_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'global_analytics_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(GlobalAnalyticsConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.GlobalAnalyticsConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.global_analytics_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.global_analytics_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.global_analytics_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.global_analytics_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_global_analytics_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.global_analytics_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class GlobalAnalyticsConfigTestFixtureGen

class AddressGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AddressGroup`
    """
    def __init__(self, conn_drv, address_group_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, draft_mode_state=None, address_group_prefix=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AddressGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            address_group_name (str): Name of address_group
            parent_fixt (:class:`.PolicyManagementTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            draft_mode_state (instance): instance of :class:`xsd:string`
            address_group_prefix (instance): instance of :class:`SubnetListType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AddressGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not address_group_name:
            self._name = 'default-address-group'
        else:
            self._name = address_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.draft_mode_state = draft_mode_state
        self.address_group_prefix = address_group_prefix
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AddressGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.address_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'address_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_draft_mode_state(self.draft_mode_state or GeneratedsSuper.populate_string("draft_mode_state"))
        self._obj.set_address_group_prefix(self.address_group_prefix or vnc_api.gen.resource_xsd.SubnetListType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AddressGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'policy-management', 'project']")

        self._obj = vnc_api.AddressGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.address_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.draft_mode_state = self.draft_mode_state
                self._obj.address_group_prefix = self.address_group_prefix
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.address_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.address_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.address_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_address_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.address_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AddressGroupTestFixtureGen

class ApplicationPolicySetTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ApplicationPolicySet`
    """
    def __init__(self, conn_drv, application_policy_set_name=None, parent_fixt=None, auto_prop_val=False, firewall_policy_ref_infos = None, global_vrouter_config_refs = None, tag_refs = None, draft_mode_state=None, all_applications=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ApplicationPolicySetTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            application_policy_set_name (str): Name of application_policy_set
            parent_fixt (:class:`.PolicyManagementTestFixtureGen`): Parent fixture
            firewall_policy (list): list of tuple (:class:`FirewallPolicy`, :class: `FirewallSequence`) type
            global_vrouter_config (list): list of :class:`GlobalVrouterConfig` type
            tag (list): list of :class:`Tag` type
            draft_mode_state (instance): instance of :class:`xsd:string`
            all_applications (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ApplicationPolicySetTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not application_policy_set_name:
            self._name = 'default-application-policy-set'
        else:
            self._name = application_policy_set_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if firewall_policy_ref_infos:
            for ln, ref in firewall_policy_ref_infos:
                self.add_firewall_policy (ln, ref)
        if global_vrouter_config_refs:
            for ln in global_vrouter_config_refs:
                self.add_global_vrouter_config (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.draft_mode_state = draft_mode_state
        self.all_applications = all_applications
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_firewall_policys ():
            self.add_firewall_policy (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_global_vrouter_configs ():
            self.add_global_vrouter_config (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_firewall_policy (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`FirewallPolicy` link to :class:`ApplicationPolicySet`
        Args:
            lo (:class:`FirewallPolicy`): obj to link
            ref (:class:`FirewallSequence`): property of the link object
        '''
        if self._obj:
            self._obj.add_firewall_policy (lo, ref)
            if update_server:
                self._conn_drv.application_policy_set_update (self._obj)

        if add_link:
            self.add_link('firewall_policy', cfixture.ConrtailLink('firewall_policy', 'application_policy_set', 'firewall_policy', ['ref'], (lo, ref)))
    # end add_firewall_policy_link

    def get_firewall_policys (self):
        return self.get_links ('firewall_policy')
    # end get_firewall_policys
    def add_global_vrouter_config (self, lo, update_server = True, add_link = True):
        '''
        add :class:`GlobalVrouterConfig` link to :class:`ApplicationPolicySet`
        Args:
            lo (:class:`GlobalVrouterConfig`): obj to link
        '''
        if self._obj:
            self._obj.add_global_vrouter_config (lo)
            if update_server:
                self._conn_drv.application_policy_set_update (self._obj)

        if add_link:
            self.add_link('global_vrouter_config', cfixture.ConrtailLink('global_vrouter_config', 'application_policy_set', 'global_vrouter_config', ['ref'], lo))
    # end add_global_vrouter_config_link

    def get_global_vrouter_configs (self):
        return self.get_links ('global_vrouter_config')
    # end get_global_vrouter_configs
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ApplicationPolicySet`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.application_policy_set_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'application_policy_set', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_draft_mode_state(self.draft_mode_state or GeneratedsSuper.populate_string("draft_mode_state"))
        self._obj.set_all_applications(self.all_applications or GeneratedsSuper.populate_boolean("all_applications"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ApplicationPolicySetTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'policy-management', 'project']")

        self._obj = vnc_api.ApplicationPolicySet(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.application_policy_set_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.draft_mode_state = self.draft_mode_state
                self._obj.all_applications = self.all_applications
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.application_policy_set_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.application_policy_set_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.application_policy_set_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_application_policy_sets() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.application_policy_sets.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ApplicationPolicySetTestFixtureGen

class VirtualIpTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualIp`
    """
    def __init__(self, conn_drv, virtual_ip_name=None, parent_fixt=None, auto_prop_val=False, loadbalancer_pool_refs = None, virtual_machine_interface_refs = None, tag_refs = None, virtual_ip_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualIpTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_ip_name (str): Name of virtual_ip
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            loadbalancer_pool (list): list of :class:`LoadbalancerPool` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            virtual_ip_properties (instance): instance of :class:`VirtualIpType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualIpTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_ip_name:
            self._name = 'default-virtual-ip'
        else:
            self._name = virtual_ip_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if loadbalancer_pool_refs:
            for ln in loadbalancer_pool_refs:
                self.add_loadbalancer_pool (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.virtual_ip_properties = virtual_ip_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_loadbalancer_pools ():
            self.add_loadbalancer_pool (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_loadbalancer_pool (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LoadbalancerPool` link to :class:`VirtualIp`
        Args:
            lo (:class:`LoadbalancerPool`): obj to link
        '''
        if self._obj:
            self._obj.add_loadbalancer_pool (lo)
            if update_server:
                self._conn_drv.virtual_ip_update (self._obj)

        if add_link:
            self.add_link('loadbalancer_pool', cfixture.ConrtailLink('loadbalancer_pool', 'virtual_ip', 'loadbalancer_pool', ['ref'], lo))
    # end add_loadbalancer_pool_link

    def get_loadbalancer_pools (self):
        return self.get_links ('loadbalancer_pool')
    # end get_loadbalancer_pools
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`VirtualIp`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.virtual_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'virtual_ip', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualIp`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_ip_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_ip', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_virtual_ip_properties(self.virtual_ip_properties or vnc_api.gen.resource_xsd.VirtualIpType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualIpTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.VirtualIp(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_ip_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.virtual_ip_properties = self.virtual_ip_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_ip_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_ip_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_ip_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_ips() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_ips.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualIpTestFixtureGen

class IntentMapTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.IntentMap`
    """
    def __init__(self, conn_drv, intent_map_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, intent_map_intent_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create IntentMapTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            intent_map_name (str): Name of intent_map
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            intent_map_intent_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(IntentMapTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not intent_map_name:
            self._name = 'default-intent-map'
        else:
            self._name = intent_map_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.intent_map_intent_type = intent_map_intent_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`IntentMap`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.intent_map_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'intent_map', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_intent_map_intent_type(self.intent_map_intent_type or GeneratedsSuper.populate_string("intent_map_intent_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(IntentMapTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.IntentMap(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.intent_map_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.intent_map_intent_type = self.intent_map_intent_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.intent_map_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.intent_map_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.intent_map_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_intent_maps() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.intent_maps.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class IntentMapTestFixtureGen

class PortTupleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PortTuple`
    """
    def __init__(self, conn_drv, port_tuple_name=None, parent_fixt=None, auto_prop_val=False, logical_router_refs = None, virtual_network_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PortTupleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            port_tuple_name (str): Name of port_tuple
            parent_fixt (:class:`.ServiceInstanceTestFixtureGen`): Parent fixture
            logical_router (list): list of :class:`LogicalRouter` type
            virtual_network (list): list of :class:`VirtualNetwork` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PortTupleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not port_tuple_name:
            self._name = 'default-port-tuple'
        else:
            self._name = port_tuple_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if logical_router_refs:
            for ln in logical_router_refs:
                self.add_logical_router (ln)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_logical_routers ():
            self.add_logical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_logical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LogicalRouter` link to :class:`PortTuple`
        Args:
            lo (:class:`LogicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_logical_router (lo)
            if update_server:
                self._conn_drv.port_tuple_update (self._obj)

        if add_link:
            self.add_link('logical_router', cfixture.ConrtailLink('logical_router', 'port_tuple', 'logical_router', ['ref'], lo))
    # end add_logical_router_link

    def get_logical_routers (self):
        return self.get_links ('logical_router')
    # end get_logical_routers
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`PortTuple`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.port_tuple_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'port_tuple', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PortTuple`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.port_tuple_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'port_tuple', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PortTupleTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ServiceInstanceTestFixtureGen(self._conn_drv, 'default-service-instance'))

        self._obj = vnc_api.PortTuple(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.port_tuple_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.port_tuple_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.port_tuple_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.port_tuple_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_port_tuples() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.port_tuples.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PortTupleTestFixtureGen

class AnalyticsAlarmNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AnalyticsAlarmNode`
    """
    def __init__(self, conn_drv, analytics_alarm_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, analytics_alarm_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AnalyticsAlarmNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            analytics_alarm_node_name (str): Name of analytics_alarm_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            analytics_alarm_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AnalyticsAlarmNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not analytics_alarm_node_name:
            self._name = 'default-analytics-alarm-node'
        else:
            self._name = analytics_alarm_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.analytics_alarm_node_ip_address = analytics_alarm_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AnalyticsAlarmNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.analytics_alarm_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'analytics_alarm_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_analytics_alarm_node_ip_address(self.analytics_alarm_node_ip_address or GeneratedsSuper.populate_string("analytics_alarm_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AnalyticsAlarmNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.AnalyticsAlarmNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.analytics_alarm_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.analytics_alarm_node_ip_address = self.analytics_alarm_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.analytics_alarm_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.analytics_alarm_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.analytics_alarm_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_analytics_alarm_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.analytics_alarm_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AnalyticsAlarmNodeTestFixtureGen

class QosQueueTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.QosQueue`
    """
    def __init__(self, conn_drv, qos_queue_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, min_bandwidth=None, max_bandwidth=None, qos_queue_identifier=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create QosQueueTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            qos_queue_name (str): Name of qos_queue
            parent_fixt (:class:`.GlobalQosConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            min_bandwidth (instance): instance of :class:`xsd:integer`
            max_bandwidth (instance): instance of :class:`xsd:integer`
            qos_queue_identifier (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(QosQueueTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not qos_queue_name:
            self._name = 'default-qos-queue'
        else:
            self._name = qos_queue_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.min_bandwidth = min_bandwidth
        self.max_bandwidth = max_bandwidth
        self.qos_queue_identifier = qos_queue_identifier
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`QosQueue`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.qos_queue_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'qos_queue', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_min_bandwidth(self.min_bandwidth or GeneratedsSuper.populate_integer("min_bandwidth"))
        self._obj.set_max_bandwidth(self.max_bandwidth or GeneratedsSuper.populate_integer("max_bandwidth"))
        self._obj.set_qos_queue_identifier(self.qos_queue_identifier or GeneratedsSuper.populate_integer("qos_queue_identifier"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(QosQueueTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalQosConfigTestFixtureGen(self._conn_drv, 'default-global-qos-config'))

        self._obj = vnc_api.QosQueue(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.qos_queue_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.min_bandwidth = self.min_bandwidth
                self._obj.max_bandwidth = self.max_bandwidth
                self._obj.qos_queue_identifier = self.qos_queue_identifier
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.qos_queue_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.qos_queue_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.qos_queue_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_qos_queues() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.qos_queues.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class QosQueueTestFixtureGen

class PhysicalRoleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PhysicalRole`
    """
    def __init__(self, conn_drv, physical_role_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PhysicalRoleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            physical_role_name (str): Name of physical_role
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PhysicalRoleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not physical_role_name:
            self._name = 'default-physical-role'
        else:
            self._name = physical_role_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PhysicalRole`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.physical_role_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'physical_role', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PhysicalRoleTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.PhysicalRole(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.physical_role_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.physical_role_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.physical_role_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.physical_role_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_physical_roles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.physical_roles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PhysicalRoleTestFixtureGen

class CardTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Card`
    """
    def __init__(self, conn_drv, card_name=None, auto_prop_val=False, tag_refs = None, interface_map=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create CardTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            interface_map (instance): instance of :class:`InterfaceMapType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(CardTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not card_name:
            self._name = 'default-card'
        else:
            self._name = card_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.interface_map = interface_map
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Card`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.card_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'card', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_interface_map(self.interface_map or vnc_api.gen.resource_xsd.InterfaceMapType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(CardTestFixtureGen, self).setUp()
        self._obj = vnc_api.Card(self._name)
        try:
            self._obj = self._conn_drv.card_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.interface_map = self.interface_map
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.card_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.card_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.card_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class CardTestFixtureGen

class SecurityLoggingObjectTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.SecurityLoggingObject`
    """
    def __init__(self, conn_drv, security_logging_object_name=None, parent_fixt=None, auto_prop_val=False, network_policy_ref_infos = None, security_group_ref_infos = None, tag_refs = None, security_logging_object_rules=None, security_logging_object_rate=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create SecurityLoggingObjectTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            security_logging_object_name (str): Name of security_logging_object
            parent_fixt (:class:`.GlobalVrouterConfigTestFixtureGen`): Parent fixture
            network_policy (list): list of tuple (:class:`NetworkPolicy`, :class: `SecurityLoggingObjectRuleListType`) type
            security_group (list): list of tuple (:class:`SecurityGroup`, :class: `SecurityLoggingObjectRuleListType`) type
            tag (list): list of :class:`Tag` type
            security_logging_object_rules (instance): instance of :class:`SecurityLoggingObjectRuleListType`
            security_logging_object_rate (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(SecurityLoggingObjectTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not security_logging_object_name:
            self._name = 'default-security-logging-object'
        else:
            self._name = security_logging_object_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if network_policy_ref_infos:
            for ln, ref in network_policy_ref_infos:
                self.add_network_policy (ln, ref)
        if security_group_ref_infos:
            for ln, ref in security_group_ref_infos:
                self.add_security_group (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.security_logging_object_rules = security_logging_object_rules
        self.security_logging_object_rate = security_logging_object_rate
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_network_policys ():
            self.add_network_policy (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_security_groups ():
            self.add_security_group (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_network_policy (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`NetworkPolicy` link to :class:`SecurityLoggingObject`
        Args:
            lo (:class:`NetworkPolicy`): obj to link
            ref (:class:`SecurityLoggingObjectRuleListType`): property of the link object
        '''
        if self._obj:
            self._obj.add_network_policy (lo, ref)
            if update_server:
                self._conn_drv.security_logging_object_update (self._obj)

        if add_link:
            self.add_link('network_policy', cfixture.ConrtailLink('network_policy', 'security_logging_object', 'network_policy', ['ref'], (lo, ref)))
    # end add_network_policy_link

    def get_network_policys (self):
        return self.get_links ('network_policy')
    # end get_network_policys
    def add_security_group (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`SecurityGroup` link to :class:`SecurityLoggingObject`
        Args:
            lo (:class:`SecurityGroup`): obj to link
            ref (:class:`SecurityLoggingObjectRuleListType`): property of the link object
        '''
        if self._obj:
            self._obj.add_security_group (lo, ref)
            if update_server:
                self._conn_drv.security_logging_object_update (self._obj)

        if add_link:
            self.add_link('security_group', cfixture.ConrtailLink('security_group', 'security_logging_object', 'security_group', ['ref'], (lo, ref)))
    # end add_security_group_link

    def get_security_groups (self):
        return self.get_links ('security_group')
    # end get_security_groups
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`SecurityLoggingObject`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.security_logging_object_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'security_logging_object', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_security_logging_object_rules(self.security_logging_object_rules or vnc_api.gen.resource_xsd.SecurityLoggingObjectRuleListType.populate())
        self._obj.set_security_logging_object_rate(self.security_logging_object_rate or GeneratedsSuper.populate_integer("security_logging_object_rate"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(SecurityLoggingObjectTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("['global-vrouter-config', 'project']")

        self._obj = vnc_api.SecurityLoggingObject(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.security_logging_object_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.security_logging_object_rules = self.security_logging_object_rules
                self._obj.security_logging_object_rate = self.security_logging_object_rate
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.security_logging_object_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.security_logging_object_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.security_logging_object_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_security_logging_objects() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.security_logging_objects.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class SecurityLoggingObjectTestFixtureGen

class QosConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.QosConfig`
    """
    def __init__(self, conn_drv, qos_config_name=None, parent_fixt=None, auto_prop_val=False, global_system_config_refs = None, tag_refs = None, qos_config_type=None, dscp_entries=None, vlan_priority_entries=None, mpls_exp_entries=None, default_forwarding_class_id=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create QosConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            qos_config_name (str): Name of qos_config
            parent_fixt (:class:`.GlobalQosConfigTestFixtureGen`): Parent fixture
            global_system_config (list): list of :class:`GlobalSystemConfig` type
            tag (list): list of :class:`Tag` type
            qos_config_type (instance): instance of :class:`xsd:string`
            dscp_entries (instance): instance of :class:`QosIdForwardingClassPairs`
            vlan_priority_entries (instance): instance of :class:`QosIdForwardingClassPairs`
            mpls_exp_entries (instance): instance of :class:`QosIdForwardingClassPairs`
            default_forwarding_class_id (instance): instance of :class:`xsd:integer`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(QosConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not qos_config_name:
            self._name = 'default-qos-config'
        else:
            self._name = qos_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if global_system_config_refs:
            for ln in global_system_config_refs:
                self.add_global_system_config (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.qos_config_type = qos_config_type
        self.dscp_entries = dscp_entries
        self.vlan_priority_entries = vlan_priority_entries
        self.mpls_exp_entries = mpls_exp_entries
        self.default_forwarding_class_id = default_forwarding_class_id
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_global_system_configs ():
            self.add_global_system_config (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_global_system_config (self, lo, update_server = True, add_link = True):
        '''
        add :class:`GlobalSystemConfig` link to :class:`QosConfig`
        Args:
            lo (:class:`GlobalSystemConfig`): obj to link
        '''
        if self._obj:
            self._obj.add_global_system_config (lo)
            if update_server:
                self._conn_drv.qos_config_update (self._obj)

        if add_link:
            self.add_link('global_system_config', cfixture.ConrtailLink('global_system_config', 'qos_config', 'global_system_config', ['ref'], lo))
    # end add_global_system_config_link

    def get_global_system_configs (self):
        return self.get_links ('global_system_config')
    # end get_global_system_configs
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`QosConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.qos_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'qos_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_qos_config_type(self.qos_config_type or GeneratedsSuper.populate_string("qos_config_type"))
        self._obj.set_dscp_entries(self.dscp_entries or vnc_api.gen.resource_xsd.QosIdForwardingClassPairs.populate())
        self._obj.set_vlan_priority_entries(self.vlan_priority_entries or vnc_api.gen.resource_xsd.QosIdForwardingClassPairs.populate())
        self._obj.set_mpls_exp_entries(self.mpls_exp_entries or vnc_api.gen.resource_xsd.QosIdForwardingClassPairs.populate())
        self._obj.set_default_forwarding_class_id(self.default_forwarding_class_id or GeneratedsSuper.populate_integer("default_forwarding_class_id"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(QosConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'global-qos-config', 'project']")

        self._obj = vnc_api.QosConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.qos_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.qos_config_type = self.qos_config_type
                self._obj.dscp_entries = self.dscp_entries
                self._obj.vlan_priority_entries = self.vlan_priority_entries
                self._obj.mpls_exp_entries = self.mpls_exp_entries
                self._obj.default_forwarding_class_id = self.default_forwarding_class_id
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.qos_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.qos_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.qos_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_qos_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.qos_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class QosConfigTestFixtureGen

class AnalyticsSnmpNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AnalyticsSnmpNode`
    """
    def __init__(self, conn_drv, analytics_snmp_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, analytics_snmp_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AnalyticsSnmpNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            analytics_snmp_node_name (str): Name of analytics_snmp_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            analytics_snmp_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AnalyticsSnmpNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not analytics_snmp_node_name:
            self._name = 'default-analytics-snmp-node'
        else:
            self._name = analytics_snmp_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.analytics_snmp_node_ip_address = analytics_snmp_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AnalyticsSnmpNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.analytics_snmp_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'analytics_snmp_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_analytics_snmp_node_ip_address(self.analytics_snmp_node_ip_address or GeneratedsSuper.populate_string("analytics_snmp_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AnalyticsSnmpNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.AnalyticsSnmpNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.analytics_snmp_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.analytics_snmp_node_ip_address = self.analytics_snmp_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.analytics_snmp_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.analytics_snmp_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.analytics_snmp_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_analytics_snmp_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.analytics_snmp_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AnalyticsSnmpNodeTestFixtureGen

class VirtualMachineInterfaceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualMachineInterface`
    """
    def __init__(self, conn_drv, virtual_machine_interface_name=None, parent_fixt=None, auto_prop_val=False, security_logging_object_refs = None, qos_config_refs = None, security_group_refs = None, virtual_machine_interface_refs = None, virtual_machine_refs = None, virtual_network_refs = None, routing_instance_ref_infos = None, bgp_router_refs = None, port_tuple_refs = None, service_health_check_refs = None, interface_route_table_refs = None, physical_interface_refs = None, bridge_domain_ref_infos = None, service_endpoint_refs = None, port_profile_refs = None, tag_refs = None, ecmp_hashing_include_fields=None, port_security_enabled=None, virtual_machine_interface_mac_addresses=None, virtual_machine_interface_dhcp_option_list=None, virtual_machine_interface_host_routes=None, virtual_machine_interface_allowed_address_pairs=None, vrf_assign_table=None, virtual_machine_interface_device_owner=None, virtual_machine_interface_disable_policy=None, virtual_machine_interface_properties=None, virtual_machine_interface_bindings=None, virtual_machine_interface_fat_flow_protocols=None, vlan_tag_based_bridge_domain=None, igmp_enable=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualMachineInterfaceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_machine_interface_name (str): Name of virtual_machine_interface
            parent_fixt (:class:`.VirtualMachineTestFixtureGen`): Parent fixture
            security_logging_object (list): list of :class:`SecurityLoggingObject` type
            qos_config (list): list of :class:`QosConfig` type
            security_group (list): list of :class:`SecurityGroup` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            virtual_machine (list): list of :class:`VirtualMachine` type
            virtual_network (list): list of :class:`VirtualNetwork` type
            routing_instance (list): list of tuple (:class:`RoutingInstance`, :class: `PolicyBasedForwardingRuleType`) type
            bgp_router (list): list of :class:`BgpRouter` type
            port_tuple (list): list of :class:`PortTuple` type
            service_health_check (list): list of :class:`ServiceHealthCheck` type
            interface_route_table (list): list of :class:`InterfaceRouteTable` type
            physical_interface (list): list of :class:`PhysicalInterface` type
            bridge_domain (list): list of tuple (:class:`BridgeDomain`, :class: `BridgeDomainMembershipType`) type
            service_endpoint (list): list of :class:`ServiceEndpoint` type
            port_profile (list): list of :class:`PortProfile` type
            tag (list): list of :class:`Tag` type
            ecmp_hashing_include_fields (instance): instance of :class:`EcmpHashingIncludeFields`
            port_security_enabled (instance): instance of :class:`xsd:boolean`
            virtual_machine_interface_mac_addresses (instance): instance of :class:`MacAddressesType`
            virtual_machine_interface_dhcp_option_list (instance): instance of :class:`DhcpOptionsListType`
            virtual_machine_interface_host_routes (instance): instance of :class:`RouteTableType`
            virtual_machine_interface_allowed_address_pairs (instance): instance of :class:`AllowedAddressPairs`
            vrf_assign_table (instance): instance of :class:`VrfAssignTableType`
            virtual_machine_interface_device_owner (instance): instance of :class:`xsd:string`
            virtual_machine_interface_disable_policy (instance): instance of :class:`xsd:boolean`
            virtual_machine_interface_properties (instance): instance of :class:`VirtualMachineInterfacePropertiesType`
            virtual_machine_interface_bindings (instance): instance of :class:`KeyValuePairs`
            virtual_machine_interface_fat_flow_protocols (instance): instance of :class:`FatFlowProtocols`
            vlan_tag_based_bridge_domain (instance): instance of :class:`xsd:boolean`
            igmp_enable (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualMachineInterfaceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_machine_interface_name:
            self._name = 'default-virtual-machine-interface'
        else:
            self._name = virtual_machine_interface_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if security_logging_object_refs:
            for ln in security_logging_object_refs:
                self.add_security_logging_object (ln)
        if qos_config_refs:
            for ln in qos_config_refs:
                self.add_qos_config (ln)
        if security_group_refs:
            for ln in security_group_refs:
                self.add_security_group (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if virtual_machine_refs:
            for ln in virtual_machine_refs:
                self.add_virtual_machine (ln)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if routing_instance_ref_infos:
            for ln, ref in routing_instance_ref_infos:
                self.add_routing_instance (ln, ref)
        if bgp_router_refs:
            for ln in bgp_router_refs:
                self.add_bgp_router (ln)
        if port_tuple_refs:
            for ln in port_tuple_refs:
                self.add_port_tuple (ln)
        if service_health_check_refs:
            for ln in service_health_check_refs:
                self.add_service_health_check (ln)
        if interface_route_table_refs:
            for ln in interface_route_table_refs:
                self.add_interface_route_table (ln)
        if physical_interface_refs:
            for ln in physical_interface_refs:
                self.add_physical_interface (ln)
        if bridge_domain_ref_infos:
            for ln, ref in bridge_domain_ref_infos:
                self.add_bridge_domain (ln, ref)
        if service_endpoint_refs:
            for ln in service_endpoint_refs:
                self.add_service_endpoint (ln)
        if port_profile_refs:
            for ln in port_profile_refs:
                self.add_port_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.ecmp_hashing_include_fields = ecmp_hashing_include_fields
        self.port_security_enabled = port_security_enabled
        self.virtual_machine_interface_mac_addresses = virtual_machine_interface_mac_addresses
        self.virtual_machine_interface_dhcp_option_list = virtual_machine_interface_dhcp_option_list
        self.virtual_machine_interface_host_routes = virtual_machine_interface_host_routes
        self.virtual_machine_interface_allowed_address_pairs = virtual_machine_interface_allowed_address_pairs
        self.vrf_assign_table = vrf_assign_table
        self.virtual_machine_interface_device_owner = virtual_machine_interface_device_owner
        self.virtual_machine_interface_disable_policy = virtual_machine_interface_disable_policy
        self.virtual_machine_interface_properties = virtual_machine_interface_properties
        self.virtual_machine_interface_bindings = virtual_machine_interface_bindings
        self.virtual_machine_interface_fat_flow_protocols = virtual_machine_interface_fat_flow_protocols
        self.vlan_tag_based_bridge_domain = vlan_tag_based_bridge_domain
        self.igmp_enable = igmp_enable
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_security_logging_objects ():
            self.add_security_logging_object (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_qos_configs ():
            self.add_qos_config (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_security_groups ():
            self.add_security_group (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machines ():
            self.add_virtual_machine (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_routing_instances ():
            self.add_routing_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgp_routers ():
            self.add_bgp_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_port_tuples ():
            self.add_port_tuple (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_health_checks ():
            self.add_service_health_check (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_interface_route_tables ():
            self.add_interface_route_table (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_interfaces ():
            self.add_physical_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bridge_domains ():
            self.add_bridge_domain (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_endpoints ():
            self.add_service_endpoint (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_port_profiles ():
            self.add_port_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_security_logging_object (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SecurityLoggingObject` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`SecurityLoggingObject`): obj to link
        '''
        if self._obj:
            self._obj.add_security_logging_object (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('security_logging_object', cfixture.ConrtailLink('security_logging_object', 'virtual_machine_interface', 'security_logging_object', ['ref'], lo))
    # end add_security_logging_object_link

    def get_security_logging_objects (self):
        return self.get_links ('security_logging_object')
    # end get_security_logging_objects
    def add_qos_config (self, lo, update_server = True, add_link = True):
        '''
        add :class:`QosConfig` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`QosConfig`): obj to link
        '''
        if self._obj:
            self._obj.add_qos_config (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('qos_config', cfixture.ConrtailLink('qos_config', 'virtual_machine_interface', 'qos_config', ['ref'], lo))
    # end add_qos_config_link

    def get_qos_configs (self):
        return self.get_links ('qos_config')
    # end get_qos_configs
    def add_security_group (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SecurityGroup` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`SecurityGroup`): obj to link
        '''
        if self._obj:
            self._obj.add_security_group (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('security_group', cfixture.ConrtailLink('security_group', 'virtual_machine_interface', 'security_group', ['ref'], lo))
    # end add_security_group_link

    def get_security_groups (self):
        return self.get_links ('security_group')
    # end get_security_groups
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'virtual_machine_interface', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_virtual_machine (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachine` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`VirtualMachine`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('virtual_machine', cfixture.ConrtailLink('virtual_machine', 'virtual_machine_interface', 'virtual_machine', ['ref'], lo))
    # end add_virtual_machine_link

    def get_virtual_machines (self):
        return self.get_links ('virtual_machine')
    # end get_virtual_machines
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'virtual_machine_interface', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_routing_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`RoutingInstance` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`RoutingInstance`): obj to link
            ref (:class:`PolicyBasedForwardingRuleType`): property of the link object
        '''
        if self._obj:
            self._obj.add_routing_instance (lo, ref)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('routing_instance', cfixture.ConrtailLink('routing_instance', 'virtual_machine_interface', 'routing_instance', ['ref'], (lo, ref)))
    # end add_routing_instance_link

    def get_routing_instances (self):
        return self.get_links ('routing_instance')
    # end get_routing_instances
    def add_bgp_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`BgpRouter` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`BgpRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_bgp_router (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('bgp_router', cfixture.ConrtailLink('bgp_router', 'virtual_machine_interface', 'bgp_router', ['ref'], lo))
    # end add_bgp_router_link

    def get_bgp_routers (self):
        return self.get_links ('bgp_router')
    # end get_bgp_routers
    def add_port_tuple (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PortTuple` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`PortTuple`): obj to link
        '''
        if self._obj:
            self._obj.add_port_tuple (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('port_tuple', cfixture.ConrtailLink('port_tuple', 'virtual_machine_interface', 'port_tuple', ['ref'], lo))
    # end add_port_tuple_link

    def get_port_tuples (self):
        return self.get_links ('port_tuple')
    # end get_port_tuples
    def add_service_health_check (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceHealthCheck` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`ServiceHealthCheck`): obj to link
        '''
        if self._obj:
            self._obj.add_service_health_check (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('service_health_check', cfixture.ConrtailLink('service_health_check', 'virtual_machine_interface', 'service_health_check', ['ref'], lo))
    # end add_service_health_check_link

    def get_service_health_checks (self):
        return self.get_links ('service_health_check')
    # end get_service_health_checks
    def add_interface_route_table (self, lo, update_server = True, add_link = True):
        '''
        add :class:`InterfaceRouteTable` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`InterfaceRouteTable`): obj to link
        '''
        if self._obj:
            self._obj.add_interface_route_table (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('interface_route_table', cfixture.ConrtailLink('interface_route_table', 'virtual_machine_interface', 'interface_route_table', ['ref'], lo))
    # end add_interface_route_table_link

    def get_interface_route_tables (self):
        return self.get_links ('interface_route_table')
    # end get_interface_route_tables
    def add_physical_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalInterface` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`PhysicalInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_interface (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('physical_interface', cfixture.ConrtailLink('physical_interface', 'virtual_machine_interface', 'physical_interface', ['ref'], lo))
    # end add_physical_interface_link

    def get_physical_interfaces (self):
        return self.get_links ('physical_interface')
    # end get_physical_interfaces
    def add_bridge_domain (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`BridgeDomain` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`BridgeDomain`): obj to link
            ref (:class:`BridgeDomainMembershipType`): property of the link object
        '''
        if self._obj:
            self._obj.add_bridge_domain (lo, ref)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('bridge_domain', cfixture.ConrtailLink('bridge_domain', 'virtual_machine_interface', 'bridge_domain', ['ref'], (lo, ref)))
    # end add_bridge_domain_link

    def get_bridge_domains (self):
        return self.get_links ('bridge_domain')
    # end get_bridge_domains
    def add_service_endpoint (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceEndpoint` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`ServiceEndpoint`): obj to link
        '''
        if self._obj:
            self._obj.add_service_endpoint (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('service_endpoint', cfixture.ConrtailLink('service_endpoint', 'virtual_machine_interface', 'service_endpoint', ['ref'], lo))
    # end add_service_endpoint_link

    def get_service_endpoints (self):
        return self.get_links ('service_endpoint')
    # end get_service_endpoints
    def add_port_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PortProfile` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`PortProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_port_profile (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('port_profile', cfixture.ConrtailLink('port_profile', 'virtual_machine_interface', 'port_profile', ['ref'], lo))
    # end add_port_profile_link

    def get_port_profiles (self):
        return self.get_links ('port_profile')
    # end get_port_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualMachineInterface`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_machine_interface_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_machine_interface', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_ecmp_hashing_include_fields(self.ecmp_hashing_include_fields or vnc_api.gen.resource_xsd.EcmpHashingIncludeFields.populate())
        self._obj.set_port_security_enabled(self.port_security_enabled or GeneratedsSuper.populate_boolean("port_security_enabled"))
        self._obj.set_virtual_machine_interface_mac_addresses(self.virtual_machine_interface_mac_addresses or vnc_api.gen.resource_xsd.MacAddressesType.populate())
        self._obj.set_virtual_machine_interface_dhcp_option_list(self.virtual_machine_interface_dhcp_option_list or vnc_api.gen.resource_xsd.DhcpOptionsListType.populate())
        self._obj.set_virtual_machine_interface_host_routes(self.virtual_machine_interface_host_routes or vnc_api.gen.resource_xsd.RouteTableType.populate())
        self._obj.set_virtual_machine_interface_allowed_address_pairs(self.virtual_machine_interface_allowed_address_pairs or vnc_api.gen.resource_xsd.AllowedAddressPairs.populate())
        self._obj.set_vrf_assign_table(self.vrf_assign_table or vnc_api.gen.resource_xsd.VrfAssignTableType.populate())
        self._obj.set_virtual_machine_interface_device_owner(self.virtual_machine_interface_device_owner or GeneratedsSuper.populate_string("virtual_machine_interface_device_owner"))
        self._obj.set_virtual_machine_interface_disable_policy(self.virtual_machine_interface_disable_policy or GeneratedsSuper.populate_boolean("virtual_machine_interface_disable_policy"))
        self._obj.set_virtual_machine_interface_properties(self.virtual_machine_interface_properties or vnc_api.gen.resource_xsd.VirtualMachineInterfacePropertiesType.populate())
        self._obj.set_virtual_machine_interface_bindings(self.virtual_machine_interface_bindings or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_virtual_machine_interface_fat_flow_protocols(self.virtual_machine_interface_fat_flow_protocols or vnc_api.gen.resource_xsd.FatFlowProtocols.populate())
        self._obj.set_vlan_tag_based_bridge_domain(self.vlan_tag_based_bridge_domain or GeneratedsSuper.populate_boolean("vlan_tag_based_bridge_domain"))
        self._obj.set_igmp_enable(self.igmp_enable or GeneratedsSuper.populate_boolean("igmp_enable"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualMachineInterfaceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'virtual-machine', 'project', 'virtual-router']")

        self._obj = vnc_api.VirtualMachineInterface(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_machine_interface_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.ecmp_hashing_include_fields = self.ecmp_hashing_include_fields
                self._obj.port_security_enabled = self.port_security_enabled
                self._obj.virtual_machine_interface_mac_addresses = self.virtual_machine_interface_mac_addresses
                self._obj.virtual_machine_interface_dhcp_option_list = self.virtual_machine_interface_dhcp_option_list
                self._obj.virtual_machine_interface_host_routes = self.virtual_machine_interface_host_routes
                self._obj.virtual_machine_interface_allowed_address_pairs = self.virtual_machine_interface_allowed_address_pairs
                self._obj.vrf_assign_table = self.vrf_assign_table
                self._obj.virtual_machine_interface_device_owner = self.virtual_machine_interface_device_owner
                self._obj.virtual_machine_interface_disable_policy = self.virtual_machine_interface_disable_policy
                self._obj.virtual_machine_interface_properties = self.virtual_machine_interface_properties
                self._obj.virtual_machine_interface_bindings = self.virtual_machine_interface_bindings
                self._obj.virtual_machine_interface_fat_flow_protocols = self.virtual_machine_interface_fat_flow_protocols
                self._obj.vlan_tag_based_bridge_domain = self.vlan_tag_based_bridge_domain
                self._obj.igmp_enable = self.igmp_enable
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_machine_interface_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_machine_interface_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_machine_interface_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_machine_interfaces() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_machine_interfaces.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualMachineInterfaceTestFixtureGen

class CliConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.CliConfig`
    """
    def __init__(self, conn_drv, cli_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, accepted_cli_config=None, commit_diff_list=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create CliConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            cli_config_name (str): Name of cli_config
            parent_fixt (:class:`.PhysicalRouterTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            accepted_cli_config (instance): instance of :class:`xsd:string`
            commit_diff_list (instance): instance of :class:`CliDiffListType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(CliConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not cli_config_name:
            self._name = 'default-cli-config'
        else:
            self._name = cli_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.accepted_cli_config = accepted_cli_config
        self.commit_diff_list = commit_diff_list
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`CliConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.cli_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'cli_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_accepted_cli_config(self.accepted_cli_config or GeneratedsSuper.populate_string("accepted_cli_config"))
        self._obj.set_commit_diff_list(self.commit_diff_list or vnc_api.gen.resource_xsd.CliDiffListType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(CliConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(PhysicalRouterTestFixtureGen(self._conn_drv, 'default-physical-router'))

        self._obj = vnc_api.CliConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.cli_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.accepted_cli_config = self.accepted_cli_config
                self._obj.commit_diff_list = self.commit_diff_list
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.cli_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.cli_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.cli_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_cli_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.cli_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class CliConfigTestFixtureGen

class ServiceObjectTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceObject`
    """
    def __init__(self, conn_drv, service_object_name=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceObjectTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceObjectTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_object_name:
            self._name = 'default-service-object'
        else:
            self._name = service_object_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceObject`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_object_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_object', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceObjectTestFixtureGen, self).setUp()
        self._obj = vnc_api.ServiceObject(self._name)
        try:
            self._obj = self._conn_drv.service_object_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_object_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_object_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_object_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceObjectTestFixtureGen

class FeatureFlagTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FeatureFlag`
    """
    def __init__(self, conn_drv, feature_flag_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, feature_description=None, feature_id=None, feature_flag_version=None, feature_release=None, enable_feature=None, feature_state=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FeatureFlagTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            feature_flag_name (str): Name of feature_flag
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            feature_description (instance): instance of :class:`xsd:string`
            feature_id (instance): instance of :class:`xsd:string`
            feature_flag_version (instance): instance of :class:`xsd:string`
            feature_release (instance): instance of :class:`xsd:string`
            enable_feature (instance): instance of :class:`xsd:boolean`
            feature_state (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FeatureFlagTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not feature_flag_name:
            self._name = 'default-feature-flag'
        else:
            self._name = feature_flag_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.feature_description = feature_description
        self.feature_id = feature_id
        self.feature_flag_version = feature_flag_version
        self.feature_release = feature_release
        self.enable_feature = enable_feature
        self.feature_state = feature_state
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FeatureFlag`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.feature_flag_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'feature_flag', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_feature_description(self.feature_description or GeneratedsSuper.populate_string("feature_description"))
        self._obj.set_feature_id(self.feature_id or GeneratedsSuper.populate_string("feature_id"))
        self._obj.set_feature_flag_version(self.feature_flag_version or GeneratedsSuper.populate_string("feature_flag_version"))
        self._obj.set_feature_release(self.feature_release or GeneratedsSuper.populate_string("feature_release"))
        self._obj.set_enable_feature(self.enable_feature or GeneratedsSuper.populate_boolean("enable_feature"))
        self._obj.set_feature_state(self.feature_state or GeneratedsSuper.populate_string("feature_state"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FeatureFlagTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.FeatureFlag(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.feature_flag_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.feature_description = self.feature_description
                self._obj.feature_id = self.feature_id
                self._obj.feature_flag_version = self.feature_flag_version
                self._obj.feature_release = self.feature_release
                self._obj.enable_feature = self.enable_feature
                self._obj.feature_state = self.feature_state
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.feature_flag_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.feature_flag_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.feature_flag_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_feature_flags() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.feature_flags.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FeatureFlagTestFixtureGen

class LoadbalancerTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Loadbalancer`
    """
    def __init__(self, conn_drv, loadbalancer_name=None, parent_fixt=None, auto_prop_val=False, service_appliance_set_refs = None, service_instance_refs = None, virtual_machine_interface_refs = None, tag_refs = None, loadbalancer_properties=None, loadbalancer_provider=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LoadbalancerTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            loadbalancer_name (str): Name of loadbalancer
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_appliance_set (list): list of :class:`ServiceApplianceSet` type
            service_instance (list): list of :class:`ServiceInstance` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            loadbalancer_properties (instance): instance of :class:`LoadbalancerType`
            loadbalancer_provider (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LoadbalancerTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not loadbalancer_name:
            self._name = 'default-loadbalancer'
        else:
            self._name = loadbalancer_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_appliance_set_refs:
            for ln in service_appliance_set_refs:
                self.add_service_appliance_set (ln)
        if service_instance_refs:
            for ln in service_instance_refs:
                self.add_service_instance (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.loadbalancer_properties = loadbalancer_properties
        self.loadbalancer_provider = loadbalancer_provider
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_appliance_sets ():
            self.add_service_appliance_set (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_instances ():
            self.add_service_instance (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_appliance_set (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceApplianceSet` link to :class:`Loadbalancer`
        Args:
            lo (:class:`ServiceApplianceSet`): obj to link
        '''
        if self._obj:
            self._obj.add_service_appliance_set (lo)
            if update_server:
                self._conn_drv.loadbalancer_update (self._obj)

        if add_link:
            self.add_link('service_appliance_set', cfixture.ConrtailLink('service_appliance_set', 'loadbalancer', 'service_appliance_set', ['ref'], lo))
    # end add_service_appliance_set_link

    def get_service_appliance_sets (self):
        return self.get_links ('service_appliance_set')
    # end get_service_appliance_sets
    def add_service_instance (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`Loadbalancer`
        Args:
            lo (:class:`ServiceInstance`): obj to link
        '''
        if self._obj:
            self._obj.add_service_instance (lo)
            if update_server:
                self._conn_drv.loadbalancer_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'loadbalancer', 'service_instance', ['ref'], lo))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`Loadbalancer`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.loadbalancer_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'loadbalancer', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Loadbalancer`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.loadbalancer_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'loadbalancer', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_loadbalancer_properties(self.loadbalancer_properties or vnc_api.gen.resource_xsd.LoadbalancerType.populate())
        self._obj.set_loadbalancer_provider(self.loadbalancer_provider or GeneratedsSuper.populate_string("loadbalancer_provider"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LoadbalancerTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.Loadbalancer(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.loadbalancer_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.loadbalancer_properties = self.loadbalancer_properties
                self._obj.loadbalancer_provider = self.loadbalancer_provider
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.loadbalancer_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.loadbalancer_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.loadbalancer_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_loadbalancers() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.loadbalancers.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LoadbalancerTestFixtureGen

class PeeringPolicyTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PeeringPolicy`
    """
    def __init__(self, conn_drv, peering_policy_name=None, auto_prop_val=False, tag_refs = None, peering_service=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PeeringPolicyTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            peering_service (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PeeringPolicyTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not peering_policy_name:
            self._name = 'default-peering-policy'
        else:
            self._name = peering_policy_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.peering_service = peering_service
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PeeringPolicy`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.peering_policy_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'peering_policy', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_peering_service(self.peering_service or GeneratedsSuper.populate_string("peering_service"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PeeringPolicyTestFixtureGen, self).setUp()
        self._obj = vnc_api.PeeringPolicy(self._name)
        try:
            self._obj = self._conn_drv.peering_policy_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.peering_service = self.peering_service
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.peering_policy_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.peering_policy_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.peering_policy_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PeeringPolicyTestFixtureGen

class StructuredSyslogApplicationRecordTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StructuredSyslogApplicationRecord`
    """
    def __init__(self, conn_drv, structured_syslog_application_record_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, structured_syslog_app_category=None, structured_syslog_app_subcategory=None, structured_syslog_app_groups=None, structured_syslog_app_risk=None, structured_syslog_app_service_tags=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StructuredSyslogApplicationRecordTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            structured_syslog_application_record_name (str): Name of structured_syslog_application_record
            parent_fixt (:class:`.StructuredSyslogConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            structured_syslog_app_category (instance): instance of :class:`xsd:string`
            structured_syslog_app_subcategory (instance): instance of :class:`xsd:string`
            structured_syslog_app_groups (instance): instance of :class:`xsd:string`
            structured_syslog_app_risk (instance): instance of :class:`xsd:string`
            structured_syslog_app_service_tags (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StructuredSyslogApplicationRecordTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not structured_syslog_application_record_name:
            self._name = 'default-structured-syslog-application-record'
        else:
            self._name = structured_syslog_application_record_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.structured_syslog_app_category = structured_syslog_app_category
        self.structured_syslog_app_subcategory = structured_syslog_app_subcategory
        self.structured_syslog_app_groups = structured_syslog_app_groups
        self.structured_syslog_app_risk = structured_syslog_app_risk
        self.structured_syslog_app_service_tags = structured_syslog_app_service_tags
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StructuredSyslogApplicationRecord`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.structured_syslog_application_record_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'structured_syslog_application_record', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_structured_syslog_app_category(self.structured_syslog_app_category or GeneratedsSuper.populate_string("structured_syslog_app_category"))
        self._obj.set_structured_syslog_app_subcategory(self.structured_syslog_app_subcategory or GeneratedsSuper.populate_string("structured_syslog_app_subcategory"))
        self._obj.set_structured_syslog_app_groups(self.structured_syslog_app_groups or GeneratedsSuper.populate_string("structured_syslog_app_groups"))
        self._obj.set_structured_syslog_app_risk(self.structured_syslog_app_risk or GeneratedsSuper.populate_string("structured_syslog_app_risk"))
        self._obj.set_structured_syslog_app_service_tags(self.structured_syslog_app_service_tags or GeneratedsSuper.populate_string("structured_syslog_app_service_tags"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StructuredSyslogApplicationRecordTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(StructuredSyslogConfigTestFixtureGen(self._conn_drv, 'default-structured-syslog-config'))

        self._obj = vnc_api.StructuredSyslogApplicationRecord(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.structured_syslog_application_record_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.structured_syslog_app_category = self.structured_syslog_app_category
                self._obj.structured_syslog_app_subcategory = self.structured_syslog_app_subcategory
                self._obj.structured_syslog_app_groups = self.structured_syslog_app_groups
                self._obj.structured_syslog_app_risk = self.structured_syslog_app_risk
                self._obj.structured_syslog_app_service_tags = self.structured_syslog_app_service_tags
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.structured_syslog_application_record_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.structured_syslog_application_record_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.structured_syslog_application_record_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_structured_syslog_application_records() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.structured_syslog_application_records.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StructuredSyslogApplicationRecordTestFixtureGen

class GlobalVrouterConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.GlobalVrouterConfig`
    """
    def __init__(self, conn_drv, global_vrouter_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, ecmp_hashing_include_fields=None, linklocal_services=None, encapsulation_priorities=None, vxlan_network_identifier_mode=None, flow_export_rate=None, flow_aging_timeout_list=None, enable_security_logging=None, encryption_mode=None, encryption_tunnel_endpoints=None, forwarding_mode=None, port_translation_pools=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create GlobalVrouterConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            global_vrouter_config_name (str): Name of global_vrouter_config
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            ecmp_hashing_include_fields (instance): instance of :class:`EcmpHashingIncludeFields`
            linklocal_services (instance): instance of :class:`LinklocalServicesTypes`
            encapsulation_priorities (instance): instance of :class:`EncapsulationPrioritiesType`
            vxlan_network_identifier_mode (instance): instance of :class:`xsd:string`
            flow_export_rate (instance): instance of :class:`xsd:integer`
            flow_aging_timeout_list (instance): instance of :class:`FlowAgingTimeoutList`
            enable_security_logging (instance): instance of :class:`xsd:boolean`
            encryption_mode (instance): instance of :class:`xsd:string`
            encryption_tunnel_endpoints (instance): instance of :class:`EncryptionTunnelEndpointList`
            forwarding_mode (instance): instance of :class:`xsd:string`
            port_translation_pools (instance): instance of :class:`PortTranslationPools`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(GlobalVrouterConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not global_vrouter_config_name:
            self._name = 'default-global-vrouter-config'
        else:
            self._name = global_vrouter_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.ecmp_hashing_include_fields = ecmp_hashing_include_fields
        self.linklocal_services = linklocal_services
        self.encapsulation_priorities = encapsulation_priorities
        self.vxlan_network_identifier_mode = vxlan_network_identifier_mode
        self.flow_export_rate = flow_export_rate
        self.flow_aging_timeout_list = flow_aging_timeout_list
        self.enable_security_logging = enable_security_logging
        self.encryption_mode = encryption_mode
        self.encryption_tunnel_endpoints = encryption_tunnel_endpoints
        self.forwarding_mode = forwarding_mode
        self.port_translation_pools = port_translation_pools
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`GlobalVrouterConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.global_vrouter_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'global_vrouter_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_ecmp_hashing_include_fields(self.ecmp_hashing_include_fields or vnc_api.gen.resource_xsd.EcmpHashingIncludeFields.populate())
        self._obj.set_linklocal_services(self.linklocal_services or vnc_api.gen.resource_xsd.LinklocalServicesTypes.populate())
        self._obj.set_encapsulation_priorities(self.encapsulation_priorities or vnc_api.gen.resource_xsd.EncapsulationPrioritiesType.populate())
        self._obj.set_vxlan_network_identifier_mode(self.vxlan_network_identifier_mode or GeneratedsSuper.populate_string("vxlan_network_identifier_mode"))
        self._obj.set_flow_export_rate(self.flow_export_rate or GeneratedsSuper.populate_integer("flow_export_rate"))
        self._obj.set_flow_aging_timeout_list(self.flow_aging_timeout_list or vnc_api.gen.resource_xsd.FlowAgingTimeoutList.populate())
        self._obj.set_enable_security_logging(self.enable_security_logging or GeneratedsSuper.populate_boolean("enable_security_logging"))
        self._obj.set_encryption_mode(self.encryption_mode or GeneratedsSuper.populate_string("encryption_mode"))
        self._obj.set_encryption_tunnel_endpoints(self.encryption_tunnel_endpoints or vnc_api.gen.resource_xsd.EncryptionTunnelEndpointList.populate())
        self._obj.set_forwarding_mode(self.forwarding_mode or GeneratedsSuper.populate_string("forwarding_mode"))
        self._obj.set_port_translation_pools(self.port_translation_pools or vnc_api.gen.resource_xsd.PortTranslationPools.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(GlobalVrouterConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.GlobalVrouterConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.global_vrouter_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.ecmp_hashing_include_fields = self.ecmp_hashing_include_fields
                self._obj.linklocal_services = self.linklocal_services
                self._obj.encapsulation_priorities = self.encapsulation_priorities
                self._obj.vxlan_network_identifier_mode = self.vxlan_network_identifier_mode
                self._obj.flow_export_rate = self.flow_export_rate
                self._obj.flow_aging_timeout_list = self.flow_aging_timeout_list
                self._obj.enable_security_logging = self.enable_security_logging
                self._obj.encryption_mode = self.encryption_mode
                self._obj.encryption_tunnel_endpoints = self.encryption_tunnel_endpoints
                self._obj.forwarding_mode = self.forwarding_mode
                self._obj.port_translation_pools = self.port_translation_pools
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.global_vrouter_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.global_vrouter_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.global_vrouter_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_global_vrouter_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.global_vrouter_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class GlobalVrouterConfigTestFixtureGen

class FloatingIpTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FloatingIp`
    """
    def __init__(self, conn_drv, floating_ip_name=None, parent_fixt=None, auto_prop_val=False, project_refs = None, virtual_machine_interface_refs = None, tag_refs = None, floating_ip_address=None, floating_ip_is_virtual_ip=None, floating_ip_fixed_ip_address=None, floating_ip_address_family=None, floating_ip_port_mappings_enable=None, floating_ip_port_mappings=None, floating_ip_traffic_direction=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FloatingIpTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            floating_ip_name (str): Name of floating_ip
            parent_fixt (:class:`.FloatingIpPoolTestFixtureGen`): Parent fixture
            project (list): list of :class:`Project` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            floating_ip_address (instance): instance of :class:`xsd:string`
            floating_ip_is_virtual_ip (instance): instance of :class:`xsd:boolean`
            floating_ip_fixed_ip_address (instance): instance of :class:`xsd:string`
            floating_ip_address_family (instance): instance of :class:`xsd:string`
            floating_ip_port_mappings_enable (instance): instance of :class:`xsd:boolean`
            floating_ip_port_mappings (instance): instance of :class:`PortMappings`
            floating_ip_traffic_direction (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FloatingIpTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not floating_ip_name:
            self._name = 'default-floating-ip'
        else:
            self._name = floating_ip_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if project_refs:
            for ln in project_refs:
                self.add_project (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.floating_ip_address = floating_ip_address
        self.floating_ip_is_virtual_ip = floating_ip_is_virtual_ip
        self.floating_ip_fixed_ip_address = floating_ip_fixed_ip_address
        self.floating_ip_address_family = floating_ip_address_family
        self.floating_ip_port_mappings_enable = floating_ip_port_mappings_enable
        self.floating_ip_port_mappings = floating_ip_port_mappings
        self.floating_ip_traffic_direction = floating_ip_traffic_direction
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_projects ():
            self.add_project (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_project (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Project` link to :class:`FloatingIp`
        Args:
            lo (:class:`Project`): obj to link
        '''
        if self._obj:
            self._obj.add_project (lo)
            if update_server:
                self._conn_drv.floating_ip_update (self._obj)

        if add_link:
            self.add_link('project', cfixture.ConrtailLink('project', 'floating_ip', 'project', ['ref'], lo))
    # end add_project_link

    def get_projects (self):
        return self.get_links ('project')
    # end get_projects
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`FloatingIp`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.floating_ip_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'floating_ip', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FloatingIp`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.floating_ip_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'floating_ip', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_floating_ip_address(self.floating_ip_address or GeneratedsSuper.populate_string("floating_ip_address"))
        self._obj.set_floating_ip_is_virtual_ip(self.floating_ip_is_virtual_ip or GeneratedsSuper.populate_boolean("floating_ip_is_virtual_ip"))
        self._obj.set_floating_ip_fixed_ip_address(self.floating_ip_fixed_ip_address or GeneratedsSuper.populate_string("floating_ip_fixed_ip_address"))
        self._obj.set_floating_ip_address_family(self.floating_ip_address_family or GeneratedsSuper.populate_string("floating_ip_address_family"))
        self._obj.set_floating_ip_port_mappings_enable(self.floating_ip_port_mappings_enable or GeneratedsSuper.populate_boolean("floating_ip_port_mappings_enable"))
        self._obj.set_floating_ip_port_mappings(self.floating_ip_port_mappings or vnc_api.gen.resource_xsd.PortMappings.populate())
        self._obj.set_floating_ip_traffic_direction(self.floating_ip_traffic_direction or GeneratedsSuper.populate_string("floating_ip_traffic_direction"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FloatingIpTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'floating-ip-pool', u'instance-ip']")

        self._obj = vnc_api.FloatingIp(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.floating_ip_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.floating_ip_address = self.floating_ip_address
                self._obj.floating_ip_is_virtual_ip = self.floating_ip_is_virtual_ip
                self._obj.floating_ip_fixed_ip_address = self.floating_ip_fixed_ip_address
                self._obj.floating_ip_address_family = self.floating_ip_address_family
                self._obj.floating_ip_port_mappings_enable = self.floating_ip_port_mappings_enable
                self._obj.floating_ip_port_mappings = self.floating_ip_port_mappings
                self._obj.floating_ip_traffic_direction = self.floating_ip_traffic_direction
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.floating_ip_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.floating_ip_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.floating_ip_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_floating_ips() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.floating_ips.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FloatingIpTestFixtureGen

class LinkAggregationGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LinkAggregationGroup`
    """
    def __init__(self, conn_drv, link_aggregation_group_name=None, parent_fixt=None, auto_prop_val=False, physical_interface_refs = None, virtual_machine_interface_refs = None, tag_refs = None, link_aggregation_group_lacp_enabled=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LinkAggregationGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            link_aggregation_group_name (str): Name of link_aggregation_group
            parent_fixt (:class:`.PhysicalRouterTestFixtureGen`): Parent fixture
            physical_interface (list): list of :class:`PhysicalInterface` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            tag (list): list of :class:`Tag` type
            link_aggregation_group_lacp_enabled (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LinkAggregationGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not link_aggregation_group_name:
            self._name = 'default-link-aggregation-group'
        else:
            self._name = link_aggregation_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if physical_interface_refs:
            for ln in physical_interface_refs:
                self.add_physical_interface (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.link_aggregation_group_lacp_enabled = link_aggregation_group_lacp_enabled
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_interfaces ():
            self.add_physical_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalInterface` link to :class:`LinkAggregationGroup`
        Args:
            lo (:class:`PhysicalInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_interface (lo)
            if update_server:
                self._conn_drv.link_aggregation_group_update (self._obj)

        if add_link:
            self.add_link('physical_interface', cfixture.ConrtailLink('physical_interface', 'link_aggregation_group', 'physical_interface', ['ref'], lo))
    # end add_physical_interface_link

    def get_physical_interfaces (self):
        return self.get_links ('physical_interface')
    # end get_physical_interfaces
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`LinkAggregationGroup`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.link_aggregation_group_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'link_aggregation_group', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LinkAggregationGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.link_aggregation_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'link_aggregation_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_link_aggregation_group_lacp_enabled(self.link_aggregation_group_lacp_enabled or GeneratedsSuper.populate_boolean("link_aggregation_group_lacp_enabled"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LinkAggregationGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(PhysicalRouterTestFixtureGen(self._conn_drv, 'default-physical-router'))

        self._obj = vnc_api.LinkAggregationGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.link_aggregation_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.link_aggregation_group_lacp_enabled = self.link_aggregation_group_lacp_enabled
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.link_aggregation_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.link_aggregation_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.link_aggregation_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_link_aggregation_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.link_aggregation_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LinkAggregationGroupTestFixtureGen

class VirtualRouterTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualRouter`
    """
    def __init__(self, conn_drv, virtual_router_name=None, parent_fixt=None, auto_prop_val=False, network_ipam_ref_infos = None, sub_cluster_refs = None, virtual_machine_refs = None, tag_refs = None, virtual_router_type=None, virtual_router_dpdk_enabled=None, virtual_router_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualRouterTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_router_name (str): Name of virtual_router
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            network_ipam (list): list of tuple (:class:`NetworkIpam`, :class: `VirtualRouterNetworkIpamType`) type
            sub_cluster (list): list of :class:`SubCluster` type
            virtual_machine (list): list of :class:`VirtualMachine` type
            tag (list): list of :class:`Tag` type
            virtual_router_type (instance): instance of :class:`xsd:string`
            virtual_router_dpdk_enabled (instance): instance of :class:`xsd:boolean`
            virtual_router_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualRouterTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_router_name:
            self._name = 'default-virtual-router'
        else:
            self._name = virtual_router_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if network_ipam_ref_infos:
            for ln, ref in network_ipam_ref_infos:
                self.add_network_ipam (ln, ref)
        if sub_cluster_refs:
            for ln in sub_cluster_refs:
                self.add_sub_cluster (ln)
        if virtual_machine_refs:
            for ln in virtual_machine_refs:
                self.add_virtual_machine (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.virtual_router_type = virtual_router_type
        self.virtual_router_dpdk_enabled = virtual_router_dpdk_enabled
        self.virtual_router_ip_address = virtual_router_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_network_ipams ():
            self.add_network_ipam (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_sub_clusters ():
            self.add_sub_cluster (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machines ():
            self.add_virtual_machine (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_network_ipam (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`NetworkIpam` link to :class:`VirtualRouter`
        Args:
            lo (:class:`NetworkIpam`): obj to link
            ref (:class:`VirtualRouterNetworkIpamType`): property of the link object
        '''
        if self._obj:
            self._obj.add_network_ipam (lo, ref)
            if update_server:
                self._conn_drv.virtual_router_update (self._obj)

        if add_link:
            self.add_link('network_ipam', cfixture.ConrtailLink('network_ipam', 'virtual_router', 'network_ipam', ['ref'], (lo, ref)))
    # end add_network_ipam_link

    def get_network_ipams (self):
        return self.get_links ('network_ipam')
    # end get_network_ipams
    def add_sub_cluster (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SubCluster` link to :class:`VirtualRouter`
        Args:
            lo (:class:`SubCluster`): obj to link
        '''
        if self._obj:
            self._obj.add_sub_cluster (lo)
            if update_server:
                self._conn_drv.virtual_router_update (self._obj)

        if add_link:
            self.add_link('sub_cluster', cfixture.ConrtailLink('sub_cluster', 'virtual_router', 'sub_cluster', ['ref'], lo))
    # end add_sub_cluster_link

    def get_sub_clusters (self):
        return self.get_links ('sub_cluster')
    # end get_sub_clusters
    def add_virtual_machine (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachine` link to :class:`VirtualRouter`
        Args:
            lo (:class:`VirtualMachine`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine (lo)
            if update_server:
                self._conn_drv.virtual_router_update (self._obj)

        if add_link:
            self.add_link('virtual_machine', cfixture.ConrtailLink('virtual_machine', 'virtual_router', 'virtual_machine', ['ref'], lo))
    # end add_virtual_machine_link

    def get_virtual_machines (self):
        return self.get_links ('virtual_machine')
    # end get_virtual_machines
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualRouter`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_router_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_router', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_virtual_router_type(self.virtual_router_type or GeneratedsSuper.populate_string("virtual_router_type"))
        self._obj.set_virtual_router_dpdk_enabled(self.virtual_router_dpdk_enabled or GeneratedsSuper.populate_boolean("virtual_router_dpdk_enabled"))
        self._obj.set_virtual_router_ip_address(self.virtual_router_ip_address or GeneratedsSuper.populate_string("virtual_router_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualRouterTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.VirtualRouter(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_router_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.virtual_router_type = self.virtual_router_type
                self._obj.virtual_router_dpdk_enabled = self.virtual_router_dpdk_enabled
                self._obj.virtual_router_ip_address = self.virtual_router_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_router_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_router_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_router_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_routers() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_routers.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualRouterTestFixtureGen

class PortProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PortProfile`
    """
    def __init__(self, conn_drv, port_profile_name=None, parent_fixt=None, auto_prop_val=False, storm_control_profile_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PortProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            port_profile_name (str): Name of port_profile
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            storm_control_profile (list): list of :class:`StormControlProfile` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PortProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not port_profile_name:
            self._name = 'default-port-profile'
        else:
            self._name = port_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if storm_control_profile_refs:
            for ln in storm_control_profile_refs:
                self.add_storm_control_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_storm_control_profiles ():
            self.add_storm_control_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_storm_control_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`StormControlProfile` link to :class:`PortProfile`
        Args:
            lo (:class:`StormControlProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_storm_control_profile (lo)
            if update_server:
                self._conn_drv.port_profile_update (self._obj)

        if add_link:
            self.add_link('storm_control_profile', cfixture.ConrtailLink('storm_control_profile', 'port_profile', 'storm_control_profile', ['ref'], lo))
    # end add_storm_control_profile_link

    def get_storm_control_profiles (self):
        return self.get_links ('storm_control_profile')
    # end get_storm_control_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PortProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.port_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'port_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PortProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.PortProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.port_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.port_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.port_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.port_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_port_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.port_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PortProfileTestFixtureGen

class PolicyManagementTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PolicyManagement`
    """
    def __init__(self, conn_drv, policy_management_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PolicyManagementTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            policy_management_name (str): Name of policy_management
            parent_fixt (:class:`.ConfigRootTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PolicyManagementTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not policy_management_name:
            self._name = 'default-policy-management'
        else:
            self._name = policy_management_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PolicyManagement`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.policy_management_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'policy_management', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PolicyManagementTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'config-root', 'project']")

        self._obj = vnc_api.PolicyManagement(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.policy_management_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.policy_management_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.policy_management_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.policy_management_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_policy_managements() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.policy_managements.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PolicyManagementTestFixtureGen

class E2ServiceProviderTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.E2ServiceProvider`
    """
    def __init__(self, conn_drv, e2_service_provider_name=None, auto_prop_val=False, peering_policy_refs = None, physical_router_refs = None, tag_refs = None, e2_service_provider_promiscuous=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create E2ServiceProviderTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            peering_policy (list): list of :class:`PeeringPolicy` type
            physical_router (list): list of :class:`PhysicalRouter` type
            tag (list): list of :class:`Tag` type
            e2_service_provider_promiscuous (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(E2ServiceProviderTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not e2_service_provider_name:
            self._name = 'default-e2-service-provider'
        else:
            self._name = e2_service_provider_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if peering_policy_refs:
            for ln in peering_policy_refs:
                self.add_peering_policy (ln)
        if physical_router_refs:
            for ln in physical_router_refs:
                self.add_physical_router (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.e2_service_provider_promiscuous = e2_service_provider_promiscuous
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_peering_policys ():
            self.add_peering_policy (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_routers ():
            self.add_physical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_peering_policy (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PeeringPolicy` link to :class:`E2ServiceProvider`
        Args:
            lo (:class:`PeeringPolicy`): obj to link
        '''
        if self._obj:
            self._obj.add_peering_policy (lo)
            if update_server:
                self._conn_drv.e2_service_provider_update (self._obj)

        if add_link:
            self.add_link('peering_policy', cfixture.ConrtailLink('peering_policy', 'e2_service_provider', 'peering_policy', ['ref'], lo))
    # end add_peering_policy_link

    def get_peering_policys (self):
        return self.get_links ('peering_policy')
    # end get_peering_policys
    def add_physical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRouter` link to :class:`E2ServiceProvider`
        Args:
            lo (:class:`PhysicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_router (lo)
            if update_server:
                self._conn_drv.e2_service_provider_update (self._obj)

        if add_link:
            self.add_link('physical_router', cfixture.ConrtailLink('physical_router', 'e2_service_provider', 'physical_router', ['ref'], lo))
    # end add_physical_router_link

    def get_physical_routers (self):
        return self.get_links ('physical_router')
    # end get_physical_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`E2ServiceProvider`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.e2_service_provider_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'e2_service_provider', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_e2_service_provider_promiscuous(self.e2_service_provider_promiscuous or GeneratedsSuper.populate_boolean("e2_service_provider_promiscuous"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(E2ServiceProviderTestFixtureGen, self).setUp()
        self._obj = vnc_api.E2ServiceProvider(self._name)
        try:
            self._obj = self._conn_drv.e2_service_provider_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.e2_service_provider_promiscuous = self.e2_service_provider_promiscuous
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.e2_service_provider_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.e2_service_provider_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.e2_service_provider_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class E2ServiceProviderTestFixtureGen

class FabricTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Fabric`
    """
    def __init__(self, conn_drv, fabric_name=None, parent_fixt=None, auto_prop_val=False, intent_map_refs = None, virtual_network_ref_infos = None, node_profile_ref_infos = None, tag_refs = None, fabric_ztp=None, fabric_os_version=None, fabric_credentials=None, fabric_enterprise_style=None, disable_vlan_vn_uniqueness_check=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FabricTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            fabric_name (str): Name of fabric
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            intent_map (list): list of :class:`IntentMap` type
            virtual_network (list): list of tuple (:class:`VirtualNetwork`, :class: `FabricNetworkTag`) type
            node_profile (list): list of tuple (:class:`NodeProfile`, :class: `SerialNumListType`) type
            tag (list): list of :class:`Tag` type
            fabric_ztp (instance): instance of :class:`xsd:boolean`
            fabric_os_version (instance): instance of :class:`xsd:string`
            fabric_credentials (instance): instance of :class:`DeviceCredentialList`
            fabric_enterprise_style (instance): instance of :class:`xsd:boolean`
            disable_vlan_vn_uniqueness_check (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FabricTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not fabric_name:
            self._name = 'default-fabric'
        else:
            self._name = fabric_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if intent_map_refs:
            for ln in intent_map_refs:
                self.add_intent_map (ln)
        if virtual_network_ref_infos:
            for ln, ref in virtual_network_ref_infos:
                self.add_virtual_network (ln, ref)
        if node_profile_ref_infos:
            for ln, ref in node_profile_ref_infos:
                self.add_node_profile (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.fabric_ztp = fabric_ztp
        self.fabric_os_version = fabric_os_version
        self.fabric_credentials = fabric_credentials
        self.fabric_enterprise_style = fabric_enterprise_style
        self.disable_vlan_vn_uniqueness_check = disable_vlan_vn_uniqueness_check
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_intent_maps ():
            self.add_intent_map (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_node_profiles ():
            self.add_node_profile (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_intent_map (self, lo, update_server = True, add_link = True):
        '''
        add :class:`IntentMap` link to :class:`Fabric`
        Args:
            lo (:class:`IntentMap`): obj to link
        '''
        if self._obj:
            self._obj.add_intent_map (lo)
            if update_server:
                self._conn_drv.fabric_update (self._obj)

        if add_link:
            self.add_link('intent_map', cfixture.ConrtailLink('intent_map', 'fabric', 'intent_map', ['ref'], lo))
    # end add_intent_map_link

    def get_intent_maps (self):
        return self.get_links ('intent_map')
    # end get_intent_maps
    def add_virtual_network (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`Fabric`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
            ref (:class:`FabricNetworkTag`): property of the link object
        '''
        if self._obj:
            self._obj.add_virtual_network (lo, ref)
            if update_server:
                self._conn_drv.fabric_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'fabric', 'virtual_network', ['ref'], (lo, ref)))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_node_profile (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`NodeProfile` link to :class:`Fabric`
        Args:
            lo (:class:`NodeProfile`): obj to link
            ref (:class:`SerialNumListType`): property of the link object
        '''
        if self._obj:
            self._obj.add_node_profile (lo, ref)
            if update_server:
                self._conn_drv.fabric_update (self._obj)

        if add_link:
            self.add_link('node_profile', cfixture.ConrtailLink('node_profile', 'fabric', 'node_profile', ['ref'], (lo, ref)))
    # end add_node_profile_link

    def get_node_profiles (self):
        return self.get_links ('node_profile')
    # end get_node_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Fabric`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.fabric_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'fabric', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_fabric_ztp(self.fabric_ztp or GeneratedsSuper.populate_boolean("fabric_ztp"))
        self._obj.set_fabric_os_version(self.fabric_os_version or GeneratedsSuper.populate_string("fabric_os_version"))
        self._obj.set_fabric_credentials(self.fabric_credentials or vnc_api.gen.resource_xsd.DeviceCredentialList.populate())
        self._obj.set_fabric_enterprise_style(self.fabric_enterprise_style or GeneratedsSuper.populate_boolean("fabric_enterprise_style"))
        self._obj.set_disable_vlan_vn_uniqueness_check(self.disable_vlan_vn_uniqueness_check or GeneratedsSuper.populate_boolean("disable_vlan_vn_uniqueness_check"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FabricTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.Fabric(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.fabric_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.fabric_ztp = self.fabric_ztp
                self._obj.fabric_os_version = self.fabric_os_version
                self._obj.fabric_credentials = self.fabric_credentials
                self._obj.fabric_enterprise_style = self.fabric_enterprise_style
                self._obj.disable_vlan_vn_uniqueness_check = self.disable_vlan_vn_uniqueness_check
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.fabric_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.fabric_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.fabric_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_fabrics() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.fabrics.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FabricTestFixtureGen

class JobTemplateTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.JobTemplate`
    """
    def __init__(self, conn_drv, job_template_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, job_template_synchronous_job=None, job_template_type=None, job_template_concurrency_level=None, job_template_playbooks=None, job_template_executables=None, job_template_input_schema=None, job_template_output_schema=None, job_template_input_ui_schema=None, job_template_output_ui_schema=None, job_template_description=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create JobTemplateTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            job_template_name (str): Name of job_template
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            job_template_synchronous_job (instance): instance of :class:`xsd:boolean`
            job_template_type (instance): instance of :class:`xsd:string`
            job_template_concurrency_level (instance): instance of :class:`xsd:string`
            job_template_playbooks (instance): instance of :class:`PlaybookInfoListType`
            job_template_executables (instance): instance of :class:`ExecutableInfoListType`
            job_template_input_schema (instance): instance of :class:`xsd:string`
            job_template_output_schema (instance): instance of :class:`xsd:string`
            job_template_input_ui_schema (instance): instance of :class:`xsd:string`
            job_template_output_ui_schema (instance): instance of :class:`xsd:string`
            job_template_description (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(JobTemplateTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not job_template_name:
            self._name = 'default-job-template'
        else:
            self._name = job_template_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.job_template_synchronous_job = job_template_synchronous_job
        self.job_template_type = job_template_type
        self.job_template_concurrency_level = job_template_concurrency_level
        self.job_template_playbooks = job_template_playbooks
        self.job_template_executables = job_template_executables
        self.job_template_input_schema = job_template_input_schema
        self.job_template_output_schema = job_template_output_schema
        self.job_template_input_ui_schema = job_template_input_ui_schema
        self.job_template_output_ui_schema = job_template_output_ui_schema
        self.job_template_description = job_template_description
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`JobTemplate`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.job_template_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'job_template', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_job_template_synchronous_job(self.job_template_synchronous_job or GeneratedsSuper.populate_boolean("job_template_synchronous_job"))
        self._obj.set_job_template_type(self.job_template_type or GeneratedsSuper.populate_string("job_template_type"))
        self._obj.set_job_template_concurrency_level(self.job_template_concurrency_level or GeneratedsSuper.populate_string("job_template_concurrency_level"))
        self._obj.set_job_template_playbooks(self.job_template_playbooks or vnc_api.gen.resource_xsd.PlaybookInfoListType.populate())
        self._obj.set_job_template_executables(self.job_template_executables or vnc_api.gen.resource_xsd.ExecutableInfoListType.populate())
        self._obj.set_job_template_input_schema(self.job_template_input_schema or GeneratedsSuper.populate_string("job_template_input_schema"))
        self._obj.set_job_template_output_schema(self.job_template_output_schema or GeneratedsSuper.populate_string("job_template_output_schema"))
        self._obj.set_job_template_input_ui_schema(self.job_template_input_ui_schema or GeneratedsSuper.populate_string("job_template_input_ui_schema"))
        self._obj.set_job_template_output_ui_schema(self.job_template_output_ui_schema or GeneratedsSuper.populate_string("job_template_output_ui_schema"))
        self._obj.set_job_template_description(self.job_template_description or GeneratedsSuper.populate_string("job_template_description"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(JobTemplateTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.JobTemplate(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.job_template_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.job_template_synchronous_job = self.job_template_synchronous_job
                self._obj.job_template_type = self.job_template_type
                self._obj.job_template_concurrency_level = self.job_template_concurrency_level
                self._obj.job_template_playbooks = self.job_template_playbooks
                self._obj.job_template_executables = self.job_template_executables
                self._obj.job_template_input_schema = self.job_template_input_schema
                self._obj.job_template_output_schema = self.job_template_output_schema
                self._obj.job_template_input_ui_schema = self.job_template_input_ui_schema
                self._obj.job_template_output_ui_schema = self.job_template_output_ui_schema
                self._obj.job_template_description = self.job_template_description
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.job_template_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.job_template_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.job_template_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_job_templates() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.job_templates.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class JobTemplateTestFixtureGen

class RoutingPolicyTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RoutingPolicy`
    """
    def __init__(self, conn_drv, routing_policy_name=None, parent_fixt=None, auto_prop_val=False, service_instance_ref_infos = None, routing_instance_ref_infos = None, tag_refs = None, routing_policy_entries=None, term_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RoutingPolicyTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            routing_policy_name (str): Name of routing_policy
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_instance (list): list of tuple (:class:`ServiceInstance`, :class: `RoutingPolicyServiceInstanceType`) type
            routing_instance (list): list of tuple (:class:`RoutingInstance`, :class: `RoutingPolicyType`) type
            tag (list): list of :class:`Tag` type
            routing_policy_entries (instance): instance of :class:`PolicyStatementType`
            term_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RoutingPolicyTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not routing_policy_name:
            self._name = 'default-routing-policy'
        else:
            self._name = routing_policy_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_instance_ref_infos:
            for ln, ref in service_instance_ref_infos:
                self.add_service_instance (ln, ref)
        if routing_instance_ref_infos:
            for ln, ref in routing_instance_ref_infos:
                self.add_routing_instance (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.routing_policy_entries = routing_policy_entries
        self.term_type = term_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_routing_instances ():
            self.add_routing_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`RoutingPolicy`
        Args:
            lo (:class:`ServiceInstance`): obj to link
            ref (:class:`RoutingPolicyServiceInstanceType`): property of the link object
        '''
        if self._obj:
            self._obj.add_service_instance (lo, ref)
            if update_server:
                self._conn_drv.routing_policy_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'routing_policy', 'service_instance', ['ref'], (lo, ref)))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_routing_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`RoutingInstance` link to :class:`RoutingPolicy`
        Args:
            lo (:class:`RoutingInstance`): obj to link
            ref (:class:`RoutingPolicyType`): property of the link object
        '''
        if self._obj:
            self._obj.add_routing_instance (lo, ref)
            if update_server:
                self._conn_drv.routing_policy_update (self._obj)

        if add_link:
            self.add_link('routing_instance', cfixture.ConrtailLink('routing_instance', 'routing_policy', 'routing_instance', ['ref'], (lo, ref)))
    # end add_routing_instance_link

    def get_routing_instances (self):
        return self.get_links ('routing_instance')
    # end get_routing_instances
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RoutingPolicy`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.routing_policy_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'routing_policy', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_routing_policy_entries(self.routing_policy_entries or vnc_api.gen.resource_xsd.PolicyStatementType.populate())
        self._obj.set_term_type(self.term_type or GeneratedsSuper.populate_string("term_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RoutingPolicyTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.RoutingPolicy(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.routing_policy_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.routing_policy_entries = self.routing_policy_entries
                self._obj.term_type = self.term_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.routing_policy_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.routing_policy_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.routing_policy_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_routing_policys() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.routing_policys.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RoutingPolicyTestFixtureGen

class RoleConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RoleConfig`
    """
    def __init__(self, conn_drv, role_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, role_config_config=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RoleConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            role_config_name (str): Name of role_config
            parent_fixt (:class:`.NodeProfileTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            role_config_config (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RoleConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not role_config_name:
            self._name = 'default-role-config'
        else:
            self._name = role_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.role_config_config = role_config_config
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RoleConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.role_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'role_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_role_config_config(self.role_config_config or GeneratedsSuper.populate_string("role_config_config"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RoleConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(NodeProfileTestFixtureGen(self._conn_drv, 'default-node-profile'))

        self._obj = vnc_api.RoleConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.role_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.role_config_config = self.role_config_config
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.role_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.role_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.role_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_role_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.role_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RoleConfigTestFixtureGen

class TagTypeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.TagType`
    """
    def __init__(self, conn_drv, tag_type_name=None, auto_prop_val=False, tag_refs = None, tag_type_id=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create TagTypeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            tag_type_id (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(TagTypeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not tag_type_name:
            self._name = 'default-tag-type'
        else:
            self._name = tag_type_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.tag_type_id = tag_type_id
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`TagType`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.tag_type_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'tag_type', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_tag_type_id(self.tag_type_id or GeneratedsSuper.populate_string("tag_type_id"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(TagTypeTestFixtureGen, self).setUp()
        self._obj = vnc_api.TagType(self._name)
        try:
            self._obj = self._conn_drv.tag_type_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.tag_type_id = self.tag_type_id
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.tag_type_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.tag_type_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.tag_type_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class TagTypeTestFixtureGen

class StructuredSyslogMessageTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StructuredSyslogMessage`
    """
    def __init__(self, conn_drv, structured_syslog_message_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, structured_syslog_message_tagged_fields=None, structured_syslog_message_integer_fields=None, structured_syslog_message_process_and_store=None, structured_syslog_message_process_and_summarize=None, structured_syslog_message_process_and_summarize_user=None, structured_syslog_message_forward=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StructuredSyslogMessageTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            structured_syslog_message_name (str): Name of structured_syslog_message
            parent_fixt (:class:`.StructuredSyslogConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            structured_syslog_message_tagged_fields (instance): instance of :class:`FieldNamesList`
            structured_syslog_message_integer_fields (instance): instance of :class:`FieldNamesList`
            structured_syslog_message_process_and_store (instance): instance of :class:`xsd:boolean`
            structured_syslog_message_process_and_summarize (instance): instance of :class:`xsd:boolean`
            structured_syslog_message_process_and_summarize_user (instance): instance of :class:`xsd:boolean`
            structured_syslog_message_forward (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StructuredSyslogMessageTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not structured_syslog_message_name:
            self._name = 'default-structured-syslog-message'
        else:
            self._name = structured_syslog_message_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.structured_syslog_message_tagged_fields = structured_syslog_message_tagged_fields
        self.structured_syslog_message_integer_fields = structured_syslog_message_integer_fields
        self.structured_syslog_message_process_and_store = structured_syslog_message_process_and_store
        self.structured_syslog_message_process_and_summarize = structured_syslog_message_process_and_summarize
        self.structured_syslog_message_process_and_summarize_user = structured_syslog_message_process_and_summarize_user
        self.structured_syslog_message_forward = structured_syslog_message_forward
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StructuredSyslogMessage`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.structured_syslog_message_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'structured_syslog_message', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_structured_syslog_message_tagged_fields(self.structured_syslog_message_tagged_fields or vnc_api.gen.resource_xsd.FieldNamesList.populate())
        self._obj.set_structured_syslog_message_integer_fields(self.structured_syslog_message_integer_fields or vnc_api.gen.resource_xsd.FieldNamesList.populate())
        self._obj.set_structured_syslog_message_process_and_store(self.structured_syslog_message_process_and_store or GeneratedsSuper.populate_boolean("structured_syslog_message_process_and_store"))
        self._obj.set_structured_syslog_message_process_and_summarize(self.structured_syslog_message_process_and_summarize or GeneratedsSuper.populate_boolean("structured_syslog_message_process_and_summarize"))
        self._obj.set_structured_syslog_message_process_and_summarize_user(self.structured_syslog_message_process_and_summarize_user or GeneratedsSuper.populate_boolean("structured_syslog_message_process_and_summarize_user"))
        self._obj.set_structured_syslog_message_forward(self.structured_syslog_message_forward or GeneratedsSuper.populate_string("structured_syslog_message_forward"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StructuredSyslogMessageTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(StructuredSyslogConfigTestFixtureGen(self._conn_drv, 'default-structured-syslog-config'))

        self._obj = vnc_api.StructuredSyslogMessage(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.structured_syslog_message_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.structured_syslog_message_tagged_fields = self.structured_syslog_message_tagged_fields
                self._obj.structured_syslog_message_integer_fields = self.structured_syslog_message_integer_fields
                self._obj.structured_syslog_message_process_and_store = self.structured_syslog_message_process_and_store
                self._obj.structured_syslog_message_process_and_summarize = self.structured_syslog_message_process_and_summarize
                self._obj.structured_syslog_message_process_and_summarize_user = self.structured_syslog_message_process_and_summarize_user
                self._obj.structured_syslog_message_forward = self.structured_syslog_message_forward
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.structured_syslog_message_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.structured_syslog_message_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.structured_syslog_message_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_structured_syslog_messages() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.structured_syslog_messages.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StructuredSyslogMessageTestFixtureGen

class LoadbalancerPoolTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LoadbalancerPool`
    """
    def __init__(self, conn_drv, loadbalancer_pool_name=None, parent_fixt=None, auto_prop_val=False, service_instance_refs = None, virtual_machine_interface_refs = None, loadbalancer_listener_refs = None, service_appliance_set_refs = None, loadbalancer_healthmonitor_refs = None, tag_refs = None, loadbalancer_pool_properties=None, loadbalancer_pool_provider=None, loadbalancer_pool_custom_attributes=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LoadbalancerPoolTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            loadbalancer_pool_name (str): Name of loadbalancer_pool
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_instance (list): list of :class:`ServiceInstance` type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            loadbalancer_listener (list): list of :class:`LoadbalancerListener` type
            service_appliance_set (list): list of :class:`ServiceApplianceSet` type
            loadbalancer_healthmonitor (list): list of :class:`LoadbalancerHealthmonitor` type
            tag (list): list of :class:`Tag` type
            loadbalancer_pool_properties (instance): instance of :class:`LoadbalancerPoolType`
            loadbalancer_pool_provider (instance): instance of :class:`xsd:string`
            loadbalancer_pool_custom_attributes (instance): instance of :class:`KeyValuePairs`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LoadbalancerPoolTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not loadbalancer_pool_name:
            self._name = 'default-loadbalancer-pool'
        else:
            self._name = loadbalancer_pool_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_instance_refs:
            for ln in service_instance_refs:
                self.add_service_instance (ln)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if loadbalancer_listener_refs:
            for ln in loadbalancer_listener_refs:
                self.add_loadbalancer_listener (ln)
        if service_appliance_set_refs:
            for ln in service_appliance_set_refs:
                self.add_service_appliance_set (ln)
        if loadbalancer_healthmonitor_refs:
            for ln in loadbalancer_healthmonitor_refs:
                self.add_loadbalancer_healthmonitor (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.loadbalancer_pool_properties = loadbalancer_pool_properties
        self.loadbalancer_pool_provider = loadbalancer_pool_provider
        self.loadbalancer_pool_custom_attributes = loadbalancer_pool_custom_attributes
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_loadbalancer_listeners ():
            self.add_loadbalancer_listener (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_service_appliance_sets ():
            self.add_service_appliance_set (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_loadbalancer_healthmonitors ():
            self.add_loadbalancer_healthmonitor (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`ServiceInstance`): obj to link
        '''
        if self._obj:
            self._obj.add_service_instance (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'loadbalancer_pool', 'service_instance', ['ref'], lo))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'loadbalancer_pool', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_loadbalancer_listener (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LoadbalancerListener` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`LoadbalancerListener`): obj to link
        '''
        if self._obj:
            self._obj.add_loadbalancer_listener (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('loadbalancer_listener', cfixture.ConrtailLink('loadbalancer_listener', 'loadbalancer_pool', 'loadbalancer_listener', ['ref'], lo))
    # end add_loadbalancer_listener_link

    def get_loadbalancer_listeners (self):
        return self.get_links ('loadbalancer_listener')
    # end get_loadbalancer_listeners
    def add_service_appliance_set (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceApplianceSet` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`ServiceApplianceSet`): obj to link
        '''
        if self._obj:
            self._obj.add_service_appliance_set (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('service_appliance_set', cfixture.ConrtailLink('service_appliance_set', 'loadbalancer_pool', 'service_appliance_set', ['ref'], lo))
    # end add_service_appliance_set_link

    def get_service_appliance_sets (self):
        return self.get_links ('service_appliance_set')
    # end get_service_appliance_sets
    def add_loadbalancer_healthmonitor (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LoadbalancerHealthmonitor` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`LoadbalancerHealthmonitor`): obj to link
        '''
        if self._obj:
            self._obj.add_loadbalancer_healthmonitor (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('loadbalancer_healthmonitor', cfixture.ConrtailLink('loadbalancer_healthmonitor', 'loadbalancer_pool', 'loadbalancer_healthmonitor', ['ref'], lo))
    # end add_loadbalancer_healthmonitor_link

    def get_loadbalancer_healthmonitors (self):
        return self.get_links ('loadbalancer_healthmonitor')
    # end get_loadbalancer_healthmonitors
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LoadbalancerPool`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.loadbalancer_pool_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'loadbalancer_pool', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_loadbalancer_pool_properties(self.loadbalancer_pool_properties or vnc_api.gen.resource_xsd.LoadbalancerPoolType.populate())
        self._obj.set_loadbalancer_pool_provider(self.loadbalancer_pool_provider or GeneratedsSuper.populate_string("loadbalancer_pool_provider"))
        self._obj.set_loadbalancer_pool_custom_attributes(self.loadbalancer_pool_custom_attributes or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LoadbalancerPoolTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.LoadbalancerPool(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.loadbalancer_pool_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.loadbalancer_pool_properties = self.loadbalancer_pool_properties
                self._obj.loadbalancer_pool_provider = self.loadbalancer_pool_provider
                self._obj.loadbalancer_pool_custom_attributes = self.loadbalancer_pool_custom_attributes
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.loadbalancer_pool_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.loadbalancer_pool_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.loadbalancer_pool_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_loadbalancer_pools() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.loadbalancer_pools.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LoadbalancerPoolTestFixtureGen

class DeviceChassisTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DeviceChassis`
    """
    def __init__(self, conn_drv, device_chassis_name=None, auto_prop_val=False, tag_refs = None, device_chassis_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DeviceChassisTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            tag (list): list of :class:`Tag` type
            device_chassis_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DeviceChassisTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not device_chassis_name:
            self._name = 'default-device-chassis'
        else:
            self._name = device_chassis_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.device_chassis_type = device_chassis_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DeviceChassis`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.device_chassis_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'device_chassis', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_device_chassis_type(self.device_chassis_type or GeneratedsSuper.populate_string("device_chassis_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DeviceChassisTestFixtureGen, self).setUp()
        self._obj = vnc_api.DeviceChassis(self._name)
        try:
            self._obj = self._conn_drv.device_chassis_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.device_chassis_type = self.device_chassis_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.device_chassis_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.device_chassis_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.device_chassis_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DeviceChassisTestFixtureGen

class GlobalQosConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.GlobalQosConfig`
    """
    def __init__(self, conn_drv, global_qos_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, control_traffic_dscp=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create GlobalQosConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            global_qos_config_name (str): Name of global_qos_config
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            control_traffic_dscp (instance): instance of :class:`ControlTrafficDscpType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(GlobalQosConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not global_qos_config_name:
            self._name = 'default-global-qos-config'
        else:
            self._name = global_qos_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.control_traffic_dscp = control_traffic_dscp
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`GlobalQosConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.global_qos_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'global_qos_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_control_traffic_dscp(self.control_traffic_dscp or vnc_api.gen.resource_xsd.ControlTrafficDscpType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(GlobalQosConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.GlobalQosConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.global_qos_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.control_traffic_dscp = self.control_traffic_dscp
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.global_qos_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.global_qos_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.global_qos_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_global_qos_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.global_qos_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class GlobalQosConfigTestFixtureGen

class AnalyticsNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AnalyticsNode`
    """
    def __init__(self, conn_drv, analytics_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, analytics_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AnalyticsNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            analytics_node_name (str): Name of analytics_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            analytics_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AnalyticsNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not analytics_node_name:
            self._name = 'default-analytics-node'
        else:
            self._name = analytics_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.analytics_node_ip_address = analytics_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AnalyticsNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.analytics_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'analytics_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_analytics_node_ip_address(self.analytics_node_ip_address or GeneratedsSuper.populate_string("analytics_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AnalyticsNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.AnalyticsNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.analytics_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.analytics_node_ip_address = self.analytics_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.analytics_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.analytics_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.analytics_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_analytics_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.analytics_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AnalyticsNodeTestFixtureGen

class VirtualDnsTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualDns`
    """
    def __init__(self, conn_drv, virtual_DNS_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, virtual_DNS_data=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualDnsTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_DNS_name (str): Name of virtual_DNS
            parent_fixt (:class:`.DomainTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            virtual_DNS_data (instance): instance of :class:`VirtualDnsType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualDnsTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_DNS_name:
            self._name = 'default-virtual-DNS'
        else:
            self._name = virtual_DNS_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.virtual_DNS_data = virtual_DNS_data
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualDns`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_DNS_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_DNS', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_virtual_DNS_data(self.virtual_DNS_data or vnc_api.gen.resource_xsd.VirtualDnsType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualDnsTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(DomainTestFixtureGen(self._conn_drv, 'default-domain'))

        self._obj = vnc_api.VirtualDns(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_DNS_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.virtual_DNS_data = self.virtual_DNS_data
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_DNS_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_DNS_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_DNS_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_DNSs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_DNSs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualDnsTestFixtureGen

class ConfigDatabaseNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ConfigDatabaseNode`
    """
    def __init__(self, conn_drv, config_database_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, config_database_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ConfigDatabaseNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            config_database_node_name (str): Name of config_database_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            config_database_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ConfigDatabaseNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not config_database_node_name:
            self._name = 'default-config-database-node'
        else:
            self._name = config_database_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.config_database_node_ip_address = config_database_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ConfigDatabaseNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.config_database_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'config_database_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_config_database_node_ip_address(self.config_database_node_ip_address or GeneratedsSuper.populate_string("config_database_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ConfigDatabaseNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.ConfigDatabaseNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.config_database_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.config_database_node_ip_address = self.config_database_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.config_database_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.config_database_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.config_database_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_config_database_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.config_database_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ConfigDatabaseNodeTestFixtureGen

class ConfigNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ConfigNode`
    """
    def __init__(self, conn_drv, config_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, config_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ConfigNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            config_node_name (str): Name of config_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            config_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ConfigNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not config_node_name:
            self._name = 'default-config-node'
        else:
            self._name = config_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.config_node_ip_address = config_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ConfigNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.config_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'config_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_config_node_ip_address(self.config_node_ip_address or GeneratedsSuper.populate_string("config_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ConfigNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.ConfigNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.config_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.config_node_ip_address = self.config_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.config_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.config_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.config_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_config_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.config_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ConfigNodeTestFixtureGen

class DeviceFunctionalGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DeviceFunctionalGroup`
    """
    def __init__(self, conn_drv, device_functional_group_name=None, parent_fixt=None, auto_prop_val=False, physical_role_refs = None, tag_refs = None, device_functional_group_description=None, device_functional_group_os_version=None, device_functional_group_routing_bridging_roles=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DeviceFunctionalGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            device_functional_group_name (str): Name of device_functional_group
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            physical_role (list): list of :class:`PhysicalRole` type
            tag (list): list of :class:`Tag` type
            device_functional_group_description (instance): instance of :class:`xsd:string`
            device_functional_group_os_version (instance): instance of :class:`xsd:string`
            device_functional_group_routing_bridging_roles (instance): instance of :class:`RoutingBridgingRolesType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DeviceFunctionalGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not device_functional_group_name:
            self._name = 'default-device-functional-group'
        else:
            self._name = device_functional_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if physical_role_refs:
            for ln in physical_role_refs:
                self.add_physical_role (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.device_functional_group_description = device_functional_group_description
        self.device_functional_group_os_version = device_functional_group_os_version
        self.device_functional_group_routing_bridging_roles = device_functional_group_routing_bridging_roles
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_roles ():
            self.add_physical_role (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_role (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRole` link to :class:`DeviceFunctionalGroup`
        Args:
            lo (:class:`PhysicalRole`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_role (lo)
            if update_server:
                self._conn_drv.device_functional_group_update (self._obj)

        if add_link:
            self.add_link('physical_role', cfixture.ConrtailLink('physical_role', 'device_functional_group', 'physical_role', ['ref'], lo))
    # end add_physical_role_link

    def get_physical_roles (self):
        return self.get_links ('physical_role')
    # end get_physical_roles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DeviceFunctionalGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.device_functional_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'device_functional_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_device_functional_group_description(self.device_functional_group_description or GeneratedsSuper.populate_string("device_functional_group_description"))
        self._obj.set_device_functional_group_os_version(self.device_functional_group_os_version or GeneratedsSuper.populate_string("device_functional_group_os_version"))
        self._obj.set_device_functional_group_routing_bridging_roles(self.device_functional_group_routing_bridging_roles or vnc_api.gen.resource_xsd.RoutingBridgingRolesType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DeviceFunctionalGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.DeviceFunctionalGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.device_functional_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.device_functional_group_description = self.device_functional_group_description
                self._obj.device_functional_group_os_version = self.device_functional_group_os_version
                self._obj.device_functional_group_routing_bridging_roles = self.device_functional_group_routing_bridging_roles
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.device_functional_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.device_functional_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.device_functional_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_device_functional_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.device_functional_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DeviceFunctionalGroupTestFixtureGen

class FirewallRuleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FirewallRule`
    """
    def __init__(self, conn_drv, firewall_rule_name=None, parent_fixt=None, auto_prop_val=False, service_group_refs = None, address_group_refs = None, virtual_network_refs = None, security_logging_object_ref_infos = None, tag_refs = None, draft_mode_state=None, action_list=None, service=None, endpoint_1=None, endpoint_2=None, match_tags=None, match_tag_types=None, direction=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FirewallRuleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            firewall_rule_name (str): Name of firewall_rule
            parent_fixt (:class:`.PolicyManagementTestFixtureGen`): Parent fixture
            service_group (list): list of :class:`ServiceGroup` type
            address_group (list): list of :class:`AddressGroup` type
            virtual_network (list): list of :class:`VirtualNetwork` type
            security_logging_object (list): list of tuple (:class:`SecurityLoggingObject`, :class: `SloRateType`) type
            tag (list): list of :class:`Tag` type
            draft_mode_state (instance): instance of :class:`xsd:string`
            action_list (instance): instance of :class:`ActionListType`
            service (instance): instance of :class:`FirewallServiceType`
            endpoint_1 (instance): instance of :class:`FirewallRuleEndpointType`
            endpoint_2 (instance): instance of :class:`FirewallRuleEndpointType`
            match_tags (instance): instance of :class:`FirewallRuleMatchTagsType`
            match_tag_types (instance): instance of :class:`FirewallRuleMatchTagsTypeIdList`
            direction (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FirewallRuleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not firewall_rule_name:
            self._name = 'default-firewall-rule'
        else:
            self._name = firewall_rule_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_group_refs:
            for ln in service_group_refs:
                self.add_service_group (ln)
        if address_group_refs:
            for ln in address_group_refs:
                self.add_address_group (ln)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if security_logging_object_ref_infos:
            for ln, ref in security_logging_object_ref_infos:
                self.add_security_logging_object (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.draft_mode_state = draft_mode_state
        self.action_list = action_list
        self.service = service
        self.endpoint_1 = endpoint_1
        self.endpoint_2 = endpoint_2
        self.match_tags = match_tags
        self.match_tag_types = match_tag_types
        self.direction = direction
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_groups ():
            self.add_service_group (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_address_groups ():
            self.add_address_group (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_security_logging_objects ():
            self.add_security_logging_object (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_group (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceGroup` link to :class:`FirewallRule`
        Args:
            lo (:class:`ServiceGroup`): obj to link
        '''
        if self._obj:
            self._obj.add_service_group (lo)
            if update_server:
                self._conn_drv.firewall_rule_update (self._obj)

        if add_link:
            self.add_link('service_group', cfixture.ConrtailLink('service_group', 'firewall_rule', 'service_group', ['ref'], lo))
    # end add_service_group_link

    def get_service_groups (self):
        return self.get_links ('service_group')
    # end get_service_groups
    def add_address_group (self, lo, update_server = True, add_link = True):
        '''
        add :class:`AddressGroup` link to :class:`FirewallRule`
        Args:
            lo (:class:`AddressGroup`): obj to link
        '''
        if self._obj:
            self._obj.add_address_group (lo)
            if update_server:
                self._conn_drv.firewall_rule_update (self._obj)

        if add_link:
            self.add_link('address_group', cfixture.ConrtailLink('address_group', 'firewall_rule', 'address_group', ['ref'], lo))
    # end add_address_group_link

    def get_address_groups (self):
        return self.get_links ('address_group')
    # end get_address_groups
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`FirewallRule`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.firewall_rule_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'firewall_rule', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_security_logging_object (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`SecurityLoggingObject` link to :class:`FirewallRule`
        Args:
            lo (:class:`SecurityLoggingObject`): obj to link
            ref (:class:`SloRateType`): property of the link object
        '''
        if self._obj:
            self._obj.add_security_logging_object (lo, ref)
            if update_server:
                self._conn_drv.firewall_rule_update (self._obj)

        if add_link:
            self.add_link('security_logging_object', cfixture.ConrtailLink('security_logging_object', 'firewall_rule', 'security_logging_object', ['ref'], (lo, ref)))
    # end add_security_logging_object_link

    def get_security_logging_objects (self):
        return self.get_links ('security_logging_object')
    # end get_security_logging_objects
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FirewallRule`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.firewall_rule_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'firewall_rule', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_draft_mode_state(self.draft_mode_state or GeneratedsSuper.populate_string("draft_mode_state"))
        self._obj.set_action_list(self.action_list or vnc_api.gen.resource_xsd.ActionListType.populate())
        self._obj.set_service(self.service or vnc_api.gen.resource_xsd.FirewallServiceType.populate())
        self._obj.set_endpoint_1(self.endpoint_1 or vnc_api.gen.resource_xsd.FirewallRuleEndpointType.populate())
        self._obj.set_endpoint_2(self.endpoint_2 or vnc_api.gen.resource_xsd.FirewallRuleEndpointType.populate())
        self._obj.set_match_tags(self.match_tags or vnc_api.gen.resource_xsd.FirewallRuleMatchTagsType.populate())
        self._obj.set_match_tag_types(self.match_tag_types or vnc_api.gen.resource_xsd.FirewallRuleMatchTagsTypeIdList.populate())
        self._obj.set_direction(self.direction or GeneratedsSuper.populate_string("direction"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FirewallRuleTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'policy-management', 'project']")

        self._obj = vnc_api.FirewallRule(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.firewall_rule_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.draft_mode_state = self.draft_mode_state
                self._obj.action_list = self.action_list
                self._obj.service = self.service
                self._obj.endpoint_1 = self.endpoint_1
                self._obj.endpoint_2 = self.endpoint_2
                self._obj.match_tags = self.match_tags
                self._obj.match_tag_types = self.match_tag_types
                self._obj.direction = self.direction
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.firewall_rule_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.firewall_rule_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.firewall_rule_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_firewall_rules() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.firewall_rules.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FirewallRuleTestFixtureGen

class BgpvpnTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Bgpvpn`
    """
    def __init__(self, conn_drv, bgpvpn_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, route_target_list=None, import_route_target_list=None, export_route_target_list=None, bgpvpn_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create BgpvpnTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            bgpvpn_name (str): Name of bgpvpn
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            route_target_list (instance): instance of :class:`RouteTargetList`
            import_route_target_list (instance): instance of :class:`RouteTargetList`
            export_route_target_list (instance): instance of :class:`RouteTargetList`
            bgpvpn_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(BgpvpnTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not bgpvpn_name:
            self._name = 'default-bgpvpn'
        else:
            self._name = bgpvpn_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.route_target_list = route_target_list
        self.import_route_target_list = import_route_target_list
        self.export_route_target_list = export_route_target_list
        self.bgpvpn_type = bgpvpn_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Bgpvpn`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.bgpvpn_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'bgpvpn', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_route_target_list(self.route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_import_route_target_list(self.import_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_export_route_target_list(self.export_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_bgpvpn_type(self.bgpvpn_type or GeneratedsSuper.populate_string("bgpvpn_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(BgpvpnTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.Bgpvpn(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.bgpvpn_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.route_target_list = self.route_target_list
                self._obj.import_route_target_list = self.import_route_target_list
                self._obj.export_route_target_list = self.export_route_target_list
                self._obj.bgpvpn_type = self.bgpvpn_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.bgpvpn_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.bgpvpn_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.bgpvpn_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_bgpvpns() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.bgpvpns.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class BgpvpnTestFixtureGen

class RoleDefinitionTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RoleDefinition`
    """
    def __init__(self, conn_drv, role_definition_name=None, parent_fixt=None, auto_prop_val=False, feature_refs = None, physical_role_refs = None, overlay_role_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RoleDefinitionTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            role_definition_name (str): Name of role_definition
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            feature (list): list of :class:`Feature` type
            physical_role (list): list of :class:`PhysicalRole` type
            overlay_role (list): list of :class:`OverlayRole` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RoleDefinitionTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not role_definition_name:
            self._name = 'default-role-definition'
        else:
            self._name = role_definition_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if feature_refs:
            for ln in feature_refs:
                self.add_feature (ln)
        if physical_role_refs:
            for ln in physical_role_refs:
                self.add_physical_role (ln)
        if overlay_role_refs:
            for ln in overlay_role_refs:
                self.add_overlay_role (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_features ():
            self.add_feature (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_physical_roles ():
            self.add_physical_role (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_overlay_roles ():
            self.add_overlay_role (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_feature (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Feature` link to :class:`RoleDefinition`
        Args:
            lo (:class:`Feature`): obj to link
        '''
        if self._obj:
            self._obj.add_feature (lo)
            if update_server:
                self._conn_drv.role_definition_update (self._obj)

        if add_link:
            self.add_link('feature', cfixture.ConrtailLink('feature', 'role_definition', 'feature', ['ref'], lo))
    # end add_feature_link

    def get_features (self):
        return self.get_links ('feature')
    # end get_features
    def add_physical_role (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalRole` link to :class:`RoleDefinition`
        Args:
            lo (:class:`PhysicalRole`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_role (lo)
            if update_server:
                self._conn_drv.role_definition_update (self._obj)

        if add_link:
            self.add_link('physical_role', cfixture.ConrtailLink('physical_role', 'role_definition', 'physical_role', ['ref'], lo))
    # end add_physical_role_link

    def get_physical_roles (self):
        return self.get_links ('physical_role')
    # end get_physical_roles
    def add_overlay_role (self, lo, update_server = True, add_link = True):
        '''
        add :class:`OverlayRole` link to :class:`RoleDefinition`
        Args:
            lo (:class:`OverlayRole`): obj to link
        '''
        if self._obj:
            self._obj.add_overlay_role (lo)
            if update_server:
                self._conn_drv.role_definition_update (self._obj)

        if add_link:
            self.add_link('overlay_role', cfixture.ConrtailLink('overlay_role', 'role_definition', 'overlay_role', ['ref'], lo))
    # end add_overlay_role_link

    def get_overlay_roles (self):
        return self.get_links ('overlay_role')
    # end get_overlay_roles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RoleDefinition`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.role_definition_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'role_definition', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RoleDefinitionTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.RoleDefinition(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.role_definition_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.role_definition_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.role_definition_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.role_definition_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_role_definitions() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.role_definitions.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RoleDefinitionTestFixtureGen

class ServiceConnectionModuleTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceConnectionModule`
    """
    def __init__(self, conn_drv, service_connection_module_name=None, auto_prop_val=False, service_object_refs = None, tag_refs = None, e2_service=None, service_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceConnectionModuleTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            service_object (list): list of :class:`ServiceObject` type
            tag (list): list of :class:`Tag` type
            e2_service (instance): instance of :class:`xsd:string`
            service_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceConnectionModuleTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_connection_module_name:
            self._name = 'default-service-connection-module'
        else:
            self._name = service_connection_module_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if service_object_refs:
            for ln in service_object_refs:
                self.add_service_object (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.e2_service = e2_service
        self.service_type = service_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_objects ():
            self.add_service_object (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_object (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceObject` link to :class:`ServiceConnectionModule`
        Args:
            lo (:class:`ServiceObject`): obj to link
        '''
        if self._obj:
            self._obj.add_service_object (lo)
            if update_server:
                self._conn_drv.service_connection_module_update (self._obj)

        if add_link:
            self.add_link('service_object', cfixture.ConrtailLink('service_object', 'service_connection_module', 'service_object', ['ref'], lo))
    # end add_service_object_link

    def get_service_objects (self):
        return self.get_links ('service_object')
    # end get_service_objects
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceConnectionModule`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_connection_module_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_connection_module', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_e2_service(self.e2_service or GeneratedsSuper.populate_string("e2_service"))
        self._obj.set_service_type(self.service_type or GeneratedsSuper.populate_string("service_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceConnectionModuleTestFixtureGen, self).setUp()
        self._obj = vnc_api.ServiceConnectionModule(self._name)
        try:
            self._obj = self._conn_drv.service_connection_module_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.e2_service = self.e2_service
                self._obj.service_type = self.service_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_connection_module_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_connection_module_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_connection_module_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceConnectionModuleTestFixtureGen

class SecurityGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.SecurityGroup`
    """
    def __init__(self, conn_drv, security_group_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, security_group_id=None, configured_security_group_id=None, security_group_entries=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create SecurityGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            security_group_name (str): Name of security_group
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            security_group_id (instance): instance of :class:`xsd:integer`
            configured_security_group_id (instance): instance of :class:`xsd:integer`
            security_group_entries (instance): instance of :class:`PolicyEntriesType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(SecurityGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not security_group_name:
            self._name = 'default-security-group'
        else:
            self._name = security_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.security_group_id = security_group_id
        self.configured_security_group_id = configured_security_group_id
        self.security_group_entries = security_group_entries
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`SecurityGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.security_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'security_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_security_group_id(self.security_group_id or GeneratedsSuper.populate_integer("security_group_id"))
        self._obj.set_configured_security_group_id(self.configured_security_group_id or GeneratedsSuper.populate_integer("configured_security_group_id"))
        self._obj.set_security_group_entries(self.security_group_entries or vnc_api.gen.resource_xsd.PolicyEntriesType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(SecurityGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.SecurityGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.security_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.security_group_id = self.security_group_id
                self._obj.configured_security_group_id = self.configured_security_group_id
                self._obj.security_group_entries = self.security_group_entries
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.security_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.security_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.security_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_security_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.security_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class SecurityGroupTestFixtureGen

class DatabaseNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DatabaseNode`
    """
    def __init__(self, conn_drv, database_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, database_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DatabaseNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            database_node_name (str): Name of database_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            database_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DatabaseNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not database_node_name:
            self._name = 'default-database-node'
        else:
            self._name = database_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.database_node_ip_address = database_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DatabaseNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.database_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'database_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_database_node_ip_address(self.database_node_ip_address or GeneratedsSuper.populate_string("database_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DatabaseNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.DatabaseNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.database_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.database_node_ip_address = self.database_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.database_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.database_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.database_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_database_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.database_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DatabaseNodeTestFixtureGen

class LoadbalancerHealthmonitorTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LoadbalancerHealthmonitor`
    """
    def __init__(self, conn_drv, loadbalancer_healthmonitor_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, loadbalancer_healthmonitor_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LoadbalancerHealthmonitorTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            loadbalancer_healthmonitor_name (str): Name of loadbalancer_healthmonitor
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            loadbalancer_healthmonitor_properties (instance): instance of :class:`LoadbalancerHealthmonitorType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LoadbalancerHealthmonitorTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not loadbalancer_healthmonitor_name:
            self._name = 'default-loadbalancer-healthmonitor'
        else:
            self._name = loadbalancer_healthmonitor_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.loadbalancer_healthmonitor_properties = loadbalancer_healthmonitor_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LoadbalancerHealthmonitor`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.loadbalancer_healthmonitor_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'loadbalancer_healthmonitor', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_loadbalancer_healthmonitor_properties(self.loadbalancer_healthmonitor_properties or vnc_api.gen.resource_xsd.LoadbalancerHealthmonitorType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LoadbalancerHealthmonitorTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.LoadbalancerHealthmonitor(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.loadbalancer_healthmonitor_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.loadbalancer_healthmonitor_properties = self.loadbalancer_healthmonitor_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.loadbalancer_healthmonitor_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.loadbalancer_healthmonitor_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.loadbalancer_healthmonitor_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_loadbalancer_healthmonitors() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.loadbalancer_healthmonitors.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LoadbalancerHealthmonitorTestFixtureGen

class DevicemgrNodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DevicemgrNode`
    """
    def __init__(self, conn_drv, devicemgr_node_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, devicemgr_node_ip_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DevicemgrNodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            devicemgr_node_name (str): Name of devicemgr_node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            devicemgr_node_ip_address (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DevicemgrNodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not devicemgr_node_name:
            self._name = 'default-devicemgr-node'
        else:
            self._name = devicemgr_node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.devicemgr_node_ip_address = devicemgr_node_ip_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DevicemgrNode`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.devicemgr_node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'devicemgr_node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_devicemgr_node_ip_address(self.devicemgr_node_ip_address or GeneratedsSuper.populate_string("devicemgr_node_ip_address"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DevicemgrNodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.DevicemgrNode(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.devicemgr_node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.devicemgr_node_ip_address = self.devicemgr_node_ip_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.devicemgr_node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.devicemgr_node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.devicemgr_node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_devicemgr_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.devicemgr_nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DevicemgrNodeTestFixtureGen

class ProjectTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Project`
    """
    def __init__(self, conn_drv, project_name=None, parent_fixt=None, auto_prop_val=False, namespace_ref_infos = None, floating_ip_pool_refs = None, alias_ip_pool_refs = None, application_policy_set_refs = None, tag_refs = None, quota=None, vxlan_routing=None, alarm_enable=None, enable_security_policy_draft=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ProjectTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            project_name (str): Name of project
            parent_fixt (:class:`.DomainTestFixtureGen`): Parent fixture
            namespace (list): list of tuple (:class:`Namespace`, :class: `SubnetType`) type
            floating_ip_pool (list): list of :class:`FloatingIpPool` type
            alias_ip_pool (list): list of :class:`AliasIpPool` type
            application_policy_set (list): list of :class:`ApplicationPolicySet` type
            tag (list): list of :class:`Tag` type
            quota (instance): instance of :class:`QuotaType`
            vxlan_routing (instance): instance of :class:`xsd:boolean`
            alarm_enable (instance): instance of :class:`xsd:boolean`
            enable_security_policy_draft (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ProjectTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not project_name:
            self._name = 'default-project'
        else:
            self._name = project_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if namespace_ref_infos:
            for ln, ref in namespace_ref_infos:
                self.add_namespace (ln, ref)
        if floating_ip_pool_refs:
            for ln in floating_ip_pool_refs:
                self.add_floating_ip_pool (ln)
        if alias_ip_pool_refs:
            for ln in alias_ip_pool_refs:
                self.add_alias_ip_pool (ln)
        if application_policy_set_refs:
            for ln in application_policy_set_refs:
                self.add_application_policy_set (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.quota = quota
        self.vxlan_routing = vxlan_routing
        self.alarm_enable = alarm_enable
        self.enable_security_policy_draft = enable_security_policy_draft
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_namespaces ():
            self.add_namespace (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_floating_ip_pools ():
            self.add_floating_ip_pool (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_alias_ip_pools ():
            self.add_alias_ip_pool (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_application_policy_sets ():
            self.add_application_policy_set (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_namespace (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`Namespace` link to :class:`Project`
        Args:
            lo (:class:`Namespace`): obj to link
            ref (:class:`SubnetType`): property of the link object
        '''
        if self._obj:
            self._obj.add_namespace (lo, ref)
            if update_server:
                self._conn_drv.project_update (self._obj)

        if add_link:
            self.add_link('namespace', cfixture.ConrtailLink('namespace', 'project', 'namespace', ['ref'], (lo, ref)))
    # end add_namespace_link

    def get_namespaces (self):
        return self.get_links ('namespace')
    # end get_namespaces
    def add_floating_ip_pool (self, lo, update_server = True, add_link = True):
        '''
        add :class:`FloatingIpPool` link to :class:`Project`
        Args:
            lo (:class:`FloatingIpPool`): obj to link
        '''
        if self._obj:
            self._obj.add_floating_ip_pool (lo)
            if update_server:
                self._conn_drv.project_update (self._obj)

        if add_link:
            self.add_link('floating_ip_pool', cfixture.ConrtailLink('floating_ip_pool', 'project', 'floating_ip_pool', ['ref'], lo))
    # end add_floating_ip_pool_link

    def get_floating_ip_pools (self):
        return self.get_links ('floating_ip_pool')
    # end get_floating_ip_pools
    def add_alias_ip_pool (self, lo, update_server = True, add_link = True):
        '''
        add :class:`AliasIpPool` link to :class:`Project`
        Args:
            lo (:class:`AliasIpPool`): obj to link
        '''
        if self._obj:
            self._obj.add_alias_ip_pool (lo)
            if update_server:
                self._conn_drv.project_update (self._obj)

        if add_link:
            self.add_link('alias_ip_pool', cfixture.ConrtailLink('alias_ip_pool', 'project', 'alias_ip_pool', ['ref'], lo))
    # end add_alias_ip_pool_link

    def get_alias_ip_pools (self):
        return self.get_links ('alias_ip_pool')
    # end get_alias_ip_pools
    def add_application_policy_set (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ApplicationPolicySet` link to :class:`Project`
        Args:
            lo (:class:`ApplicationPolicySet`): obj to link
        '''
        if self._obj:
            self._obj.add_application_policy_set (lo)
            if update_server:
                self._conn_drv.project_update (self._obj)

        if add_link:
            self.add_link('application_policy_set', cfixture.ConrtailLink('application_policy_set', 'project', 'application_policy_set', ['ref'], lo))
    # end add_application_policy_set_link

    def get_application_policy_sets (self):
        return self.get_links ('application_policy_set')
    # end get_application_policy_sets
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Project`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.project_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'project', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_quota(self.quota or vnc_api.gen.resource_xsd.QuotaType.populate())
        self._obj.set_vxlan_routing(self.vxlan_routing or GeneratedsSuper.populate_boolean("vxlan_routing"))
        self._obj.set_alarm_enable(self.alarm_enable or GeneratedsSuper.populate_boolean("alarm_enable"))
        self._obj.set_enable_security_policy_draft(self.enable_security_policy_draft or GeneratedsSuper.populate_boolean("enable_security_policy_draft"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ProjectTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(DomainTestFixtureGen(self._conn_drv, 'default-domain'))

        self._obj = vnc_api.Project(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.project_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.quota = self.quota
                self._obj.vxlan_routing = self.vxlan_routing
                self._obj.alarm_enable = self.alarm_enable
                self._obj.enable_security_policy_draft = self.enable_security_policy_draft
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.project_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.project_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.project_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_projects() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.projects.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ProjectTestFixtureGen

class FabricNamespaceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FabricNamespace`
    """
    def __init__(self, conn_drv, fabric_namespace_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, fabric_namespace_type=None, fabric_namespace_value=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FabricNamespaceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            fabric_namespace_name (str): Name of fabric_namespace
            parent_fixt (:class:`.FabricTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            fabric_namespace_type (instance): instance of :class:`xsd:string`
            fabric_namespace_value (instance): instance of :class:`NamespaceValue`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FabricNamespaceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not fabric_namespace_name:
            self._name = 'default-fabric-namespace'
        else:
            self._name = fabric_namespace_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.fabric_namespace_type = fabric_namespace_type
        self.fabric_namespace_value = fabric_namespace_value
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FabricNamespace`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.fabric_namespace_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'fabric_namespace', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_fabric_namespace_type(self.fabric_namespace_type or GeneratedsSuper.populate_string("fabric_namespace_type"))
        self._obj.set_fabric_namespace_value(self.fabric_namespace_value or vnc_api.gen.resource_xsd.NamespaceValue.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FabricNamespaceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(FabricTestFixtureGen(self._conn_drv, 'default-fabric'))

        self._obj = vnc_api.FabricNamespace(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.fabric_namespace_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.fabric_namespace_type = self.fabric_namespace_type
                self._obj.fabric_namespace_value = self.fabric_namespace_value
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.fabric_namespace_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.fabric_namespace_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.fabric_namespace_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_fabric_namespaces() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.fabric_namespaces.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FabricNamespaceTestFixtureGen

class NetworkIpamTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.NetworkIpam`
    """
    def __init__(self, conn_drv, network_ipam_name=None, parent_fixt=None, auto_prop_val=False, virtual_DNS_refs = None, tag_refs = None, network_ipam_mgmt=None, ipam_subnets=None, ipam_subnet_method=None, ipam_subnetting=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NetworkIpamTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            network_ipam_name (str): Name of network_ipam
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            virtual_DNS (list): list of :class:`VirtualDns` type
            tag (list): list of :class:`Tag` type
            network_ipam_mgmt (instance): instance of :class:`IpamType`
            ipam_subnets (instance): instance of :class:`IpamSubnets`
            ipam_subnet_method (instance): instance of :class:`xsd:string`
            ipam_subnetting (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NetworkIpamTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not network_ipam_name:
            self._name = 'default-network-ipam'
        else:
            self._name = network_ipam_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_DNS_refs:
            for ln in virtual_DNS_refs:
                self.add_virtual_DNS (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.network_ipam_mgmt = network_ipam_mgmt
        self.ipam_subnets = ipam_subnets
        self.ipam_subnet_method = ipam_subnet_method
        self.ipam_subnetting = ipam_subnetting
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_DNSs ():
            self.add_virtual_DNS (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_DNS (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualDns` link to :class:`NetworkIpam`
        Args:
            lo (:class:`VirtualDns`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_DNS (lo)
            if update_server:
                self._conn_drv.network_ipam_update (self._obj)

        if add_link:
            self.add_link('virtual_DNS', cfixture.ConrtailLink('virtual_DNS', 'network_ipam', 'virtual_DNS', ['ref'], lo))
    # end add_virtual_DNS_link

    def get_virtual_DNSs (self):
        return self.get_links ('virtual_DNS')
    # end get_virtual_DNSs
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`NetworkIpam`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.network_ipam_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'network_ipam', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_network_ipam_mgmt(self.network_ipam_mgmt or vnc_api.gen.resource_xsd.IpamType.populate())
        self._obj.set_ipam_subnets(self.ipam_subnets or vnc_api.gen.resource_xsd.IpamSubnets.populate())
        self._obj.set_ipam_subnet_method(self.ipam_subnet_method or GeneratedsSuper.populate_string("ipam_subnet_method"))
        self._obj.set_ipam_subnetting(self.ipam_subnetting or GeneratedsSuper.populate_boolean("ipam_subnetting"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NetworkIpamTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.NetworkIpam(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.network_ipam_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.network_ipam_mgmt = self.network_ipam_mgmt
                self._obj.ipam_subnets = self.ipam_subnets
                self._obj.ipam_subnet_method = self.ipam_subnet_method
                self._obj.ipam_subnetting = self.ipam_subnetting
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.network_ipam_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.network_ipam_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.network_ipam_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_network_ipams() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.network_ipams.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NetworkIpamTestFixtureGen

class NetworkPolicyTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.NetworkPolicy`
    """
    def __init__(self, conn_drv, network_policy_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, network_policy_entries=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NetworkPolicyTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            network_policy_name (str): Name of network_policy
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            network_policy_entries (instance): instance of :class:`PolicyEntriesType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NetworkPolicyTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not network_policy_name:
            self._name = 'default-network-policy'
        else:
            self._name = network_policy_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.network_policy_entries = network_policy_entries
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`NetworkPolicy`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.network_policy_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'network_policy', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_network_policy_entries(self.network_policy_entries or vnc_api.gen.resource_xsd.PolicyEntriesType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NetworkPolicyTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.NetworkPolicy(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.network_policy_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.network_policy_entries = self.network_policy_entries
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.network_policy_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.network_policy_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.network_policy_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_network_policys() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.network_policys.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NetworkPolicyTestFixtureGen

class SflowProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.SflowProfile`
    """
    def __init__(self, conn_drv, sflow_profile_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, sflow_profile_is_default=None, sflow_parameters=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create SflowProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            sflow_profile_name (str): Name of sflow_profile
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            sflow_profile_is_default (instance): instance of :class:`xsd:boolean`
            sflow_parameters (instance): instance of :class:`SflowParameters`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(SflowProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not sflow_profile_name:
            self._name = 'default-sflow-profile'
        else:
            self._name = sflow_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.sflow_profile_is_default = sflow_profile_is_default
        self.sflow_parameters = sflow_parameters
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`SflowProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.sflow_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'sflow_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_sflow_profile_is_default(self.sflow_profile_is_default or GeneratedsSuper.populate_boolean("sflow_profile_is_default"))
        self._obj.set_sflow_parameters(self.sflow_parameters or vnc_api.gen.resource_xsd.SflowParameters.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(SflowProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.SflowProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.sflow_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.sflow_profile_is_default = self.sflow_profile_is_default
                self._obj.sflow_parameters = self.sflow_parameters
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.sflow_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.sflow_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.sflow_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_sflow_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.sflow_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class SflowProfileTestFixtureGen

class HardwareTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Hardware`
    """
    def __init__(self, conn_drv, hardware_name=None, auto_prop_val=False, card_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create HardwareTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            card (list): list of :class:`Card` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(HardwareTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not hardware_name:
            self._name = 'default-hardware'
        else:
            self._name = hardware_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if card_refs:
            for ln in card_refs:
                self.add_card (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_cards ():
            self.add_card (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_card (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Card` link to :class:`Hardware`
        Args:
            lo (:class:`Card`): obj to link
        '''
        if self._obj:
            self._obj.add_card (lo)
            if update_server:
                self._conn_drv.hardware_update (self._obj)

        if add_link:
            self.add_link('card', cfixture.ConrtailLink('card', 'hardware', 'card', ['ref'], lo))
    # end add_card_link

    def get_cards (self):
        return self.get_links ('card')
    # end get_cards
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Hardware`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.hardware_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'hardware', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(HardwareTestFixtureGen, self).setUp()
        self._obj = vnc_api.Hardware(self._name)
        try:
            self._obj = self._conn_drv.hardware_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.hardware_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.hardware_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.hardware_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class HardwareTestFixtureGen

class TagTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Tag`
    """
    def __init__(self, conn_drv, tag_name=None, parent_fixt=None, auto_prop_val=False, tag_type_refs = None, tag_refs = None, tag_type_name=None, tag_value=None, tag_predefined=None, tag_id=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create TagTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            tag_name (str): Name of tag
            parent_fixt (:class:`.ConfigRootTestFixtureGen`): Parent fixture
            tag_type (list): list of :class:`TagType` type
            tag (list): list of :class:`Tag` type
            tag_type_name (instance): instance of :class:`xsd:string`
            tag_value (instance): instance of :class:`xsd:string`
            tag_predefined (instance): instance of :class:`xsd:boolean`
            tag_id (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(TagTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not tag_name:
            self._name = 'default-tag'
        else:
            self._name = tag_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_type_refs:
            for ln in tag_type_refs:
                self.add_tag_type (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.tag_type_name = tag_type_name
        self.tag_value = tag_value
        self.tag_predefined = tag_predefined
        self.tag_id = tag_id
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tag_types ():
            self.add_tag_type (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag_type (self, lo, update_server = True, add_link = True):
        '''
        add :class:`TagType` link to :class:`Tag`
        Args:
            lo (:class:`TagType`): obj to link
        '''
        if self._obj:
            self._obj.add_tag_type (lo)
            if update_server:
                self._conn_drv.tag_update (self._obj)

        if add_link:
            self.add_link('tag_type', cfixture.ConrtailLink('tag_type', 'tag', 'tag_type', ['ref'], lo))
    # end add_tag_type_link

    def get_tag_types (self):
        return self.get_links ('tag_type')
    # end get_tag_types
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Tag`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.tag_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'tag', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_tag_type_name(self.tag_type_name or GeneratedsSuper.populate_string("tag_type_name"))
        self._obj.set_tag_value(self.tag_value or GeneratedsSuper.populate_string("tag_value"))
        self._obj.set_tag_predefined(self.tag_predefined or GeneratedsSuper.populate_boolean("tag_predefined"))
        self._obj.set_tag_id(self.tag_id or GeneratedsSuper.populate_string("tag_id"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(TagTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'config-root', 'project']")

        self._obj = vnc_api.Tag(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.tag_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.tag_type_name = self.tag_type_name
                self._obj.tag_value = self.tag_value
                self._obj.tag_predefined = self.tag_predefined
                self._obj.tag_id = self.tag_id
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.tag_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.tag_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.tag_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_tags() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.tags.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class TagTestFixtureGen

class FeatureConfigTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.FeatureConfig`
    """
    def __init__(self, conn_drv, feature_config_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, feature_config_additional_params=None, feature_config_vendor_config=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FeatureConfigTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            feature_config_name (str): Name of feature_config
            parent_fixt (:class:`.RoleDefinitionTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            feature_config_additional_params (instance): instance of :class:`KeyValuePairs`
            feature_config_vendor_config (instance): instance of :class:`KeyValuePairs`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FeatureConfigTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not feature_config_name:
            self._name = 'default-feature-config'
        else:
            self._name = feature_config_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.feature_config_additional_params = feature_config_additional_params
        self.feature_config_vendor_config = feature_config_vendor_config
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`FeatureConfig`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.feature_config_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'feature_config', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_feature_config_additional_params(self.feature_config_additional_params or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_feature_config_vendor_config(self.feature_config_vendor_config or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FeatureConfigTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(RoleDefinitionTestFixtureGen(self._conn_drv, 'default-role-definition'))

        self._obj = vnc_api.FeatureConfig(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.feature_config_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.feature_config_additional_params = self.feature_config_additional_params
                self._obj.feature_config_vendor_config = self.feature_config_vendor_config
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.feature_config_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.feature_config_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.feature_config_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_feature_configs() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.feature_configs.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FeatureConfigTestFixtureGen

class TelemetryProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.TelemetryProfile`
    """
    def __init__(self, conn_drv, telemetry_profile_name=None, parent_fixt=None, auto_prop_val=False, sflow_profile_refs = None, tag_refs = None, telemetry_profile_is_default=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create TelemetryProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            telemetry_profile_name (str): Name of telemetry_profile
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            sflow_profile (list): list of :class:`SflowProfile` type
            tag (list): list of :class:`Tag` type
            telemetry_profile_is_default (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(TelemetryProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not telemetry_profile_name:
            self._name = 'default-telemetry-profile'
        else:
            self._name = telemetry_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if sflow_profile_refs:
            for ln in sflow_profile_refs:
                self.add_sflow_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.telemetry_profile_is_default = telemetry_profile_is_default
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_sflow_profiles ():
            self.add_sflow_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_sflow_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SflowProfile` link to :class:`TelemetryProfile`
        Args:
            lo (:class:`SflowProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_sflow_profile (lo)
            if update_server:
                self._conn_drv.telemetry_profile_update (self._obj)

        if add_link:
            self.add_link('sflow_profile', cfixture.ConrtailLink('sflow_profile', 'telemetry_profile', 'sflow_profile', ['ref'], lo))
    # end add_sflow_profile_link

    def get_sflow_profiles (self):
        return self.get_links ('sflow_profile')
    # end get_sflow_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`TelemetryProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.telemetry_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'telemetry_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_telemetry_profile_is_default(self.telemetry_profile_is_default or GeneratedsSuper.populate_boolean("telemetry_profile_is_default"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(TelemetryProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.TelemetryProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.telemetry_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.telemetry_profile_is_default = self.telemetry_profile_is_default
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.telemetry_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.telemetry_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.telemetry_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_telemetry_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.telemetry_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class TelemetryProfileTestFixtureGen

class BgpRouterTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.BgpRouter`
    """
    def __init__(self, conn_drv, bgp_router_name=None, parent_fixt=None, auto_prop_val=False, control_node_zone_refs = None, sub_cluster_refs = None, bgp_router_ref_infos = None, tag_refs = None, bgp_router_parameters=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create BgpRouterTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            bgp_router_name (str): Name of bgp_router
            parent_fixt (:class:`.RoutingInstanceTestFixtureGen`): Parent fixture
            control_node_zone (list): list of :class:`ControlNodeZone` type
            sub_cluster (list): list of :class:`SubCluster` type
            bgp_router (list): list of tuple (:class:`BgpRouter`, :class: `BgpPeeringAttributes`) type
            tag (list): list of :class:`Tag` type
            bgp_router_parameters (instance): instance of :class:`BgpRouterParams`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(BgpRouterTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not bgp_router_name:
            self._name = 'default-bgp-router'
        else:
            self._name = bgp_router_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if control_node_zone_refs:
            for ln in control_node_zone_refs:
                self.add_control_node_zone (ln)
        if sub_cluster_refs:
            for ln in sub_cluster_refs:
                self.add_sub_cluster (ln)
        if bgp_router_ref_infos:
            for ln, ref in bgp_router_ref_infos:
                self.add_bgp_router (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.bgp_router_parameters = bgp_router_parameters
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_control_node_zones ():
            self.add_control_node_zone (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_sub_clusters ():
            self.add_sub_cluster (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgp_routers ():
            self.add_bgp_router (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_control_node_zone (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ControlNodeZone` link to :class:`BgpRouter`
        Args:
            lo (:class:`ControlNodeZone`): obj to link
        '''
        if self._obj:
            self._obj.add_control_node_zone (lo)
            if update_server:
                self._conn_drv.bgp_router_update (self._obj)

        if add_link:
            self.add_link('control_node_zone', cfixture.ConrtailLink('control_node_zone', 'bgp_router', 'control_node_zone', ['ref'], lo))
    # end add_control_node_zone_link

    def get_control_node_zones (self):
        return self.get_links ('control_node_zone')
    # end get_control_node_zones
    def add_sub_cluster (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SubCluster` link to :class:`BgpRouter`
        Args:
            lo (:class:`SubCluster`): obj to link
        '''
        if self._obj:
            self._obj.add_sub_cluster (lo)
            if update_server:
                self._conn_drv.bgp_router_update (self._obj)

        if add_link:
            self.add_link('sub_cluster', cfixture.ConrtailLink('sub_cluster', 'bgp_router', 'sub_cluster', ['ref'], lo))
    # end add_sub_cluster_link

    def get_sub_clusters (self):
        return self.get_links ('sub_cluster')
    # end get_sub_clusters
    def add_bgp_router (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`BgpRouter` link to :class:`BgpRouter`
        Args:
            lo (:class:`BgpRouter`): obj to link
            ref (:class:`BgpPeeringAttributes`): property of the link object
        '''
        if self._obj:
            self._obj.add_bgp_router (lo, ref)
            if update_server:
                self._conn_drv.bgp_router_update (self._obj)

        if add_link:
            self.add_link('bgp_router', cfixture.ConrtailLink('bgp_router', 'bgp_router', 'bgp_router', ['ref'], (lo, ref)))
    # end add_bgp_router_link

    def get_bgp_routers (self):
        return self.get_links ('bgp_router')
    # end get_bgp_routers
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`BgpRouter`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.bgp_router_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'bgp_router', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_bgp_router_parameters(self.bgp_router_parameters or vnc_api.gen.resource_xsd.BgpRouterParams.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(BgpRouterTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(RoutingInstanceTestFixtureGen(self._conn_drv, 'default-routing-instance'))

        self._obj = vnc_api.BgpRouter(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.bgp_router_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.bgp_router_parameters = self.bgp_router_parameters
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.bgp_router_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.bgp_router_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.bgp_router_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_bgp_routers() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.bgp_routers.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class BgpRouterTestFixtureGen

class VirtualNetworkTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualNetwork`
    """
    def __init__(self, conn_drv, virtual_network_name=None, parent_fixt=None, auto_prop_val=False, security_logging_object_refs = None, qos_config_refs = None, network_ipam_ref_infos = None, network_policy_ref_infos = None, virtual_network_refs = None, route_table_refs = None, multicast_policy_refs = None, bgpvpn_refs = None, intent_map_refs = None, routing_policy_ref_infos = None, tag_refs = None, ecmp_hashing_include_fields=None, virtual_network_category=None, virtual_network_properties=None, virtual_network_routed_properties=None, provider_properties=None, virtual_network_network_id=None, is_provider_network=None, port_security_enabled=None, fabric_snat=None, route_target_list=None, import_route_target_list=None, export_route_target_list=None, router_external=None, is_shared=None, external_ipam=None, flood_unknown_unicast=None, multi_policy_service_chains_enabled=None, address_allocation_mode=None, virtual_network_fat_flow_protocols=None, mac_learning_enabled=None, mac_limit_control=None, mac_move_control=None, mac_aging_time=None, pbb_evpn_enable=None, pbb_etree_enable=None, layer2_control_word=None, igmp_enable=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualNetworkTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_network_name (str): Name of virtual_network
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            security_logging_object (list): list of :class:`SecurityLoggingObject` type
            qos_config (list): list of :class:`QosConfig` type
            network_ipam (list): list of tuple (:class:`NetworkIpam`, :class: `VnSubnetsType`) type
            network_policy (list): list of tuple (:class:`NetworkPolicy`, :class: `VirtualNetworkPolicyType`) type
            virtual_network (list): list of :class:`VirtualNetwork` type
            route_table (list): list of :class:`RouteTable` type
            multicast_policy (list): list of :class:`MulticastPolicy` type
            bgpvpn (list): list of :class:`Bgpvpn` type
            intent_map (list): list of :class:`IntentMap` type
            routing_policy (list): list of tuple (:class:`RoutingPolicy`, :class: `RoutingPolicyType`) type
            tag (list): list of :class:`Tag` type
            ecmp_hashing_include_fields (instance): instance of :class:`EcmpHashingIncludeFields`
            virtual_network_category (instance): instance of :class:`xsd:string`
            virtual_network_properties (instance): instance of :class:`VirtualNetworkType`
            virtual_network_routed_properties (instance): instance of :class:`VirtualNetworkRoutedPropertiesType`
            provider_properties (instance): instance of :class:`ProviderDetails`
            virtual_network_network_id (instance): instance of :class:`xsd:integer`
            is_provider_network (instance): instance of :class:`xsd:boolean`
            port_security_enabled (instance): instance of :class:`xsd:boolean`
            fabric_snat (instance): instance of :class:`xsd:boolean`
            route_target_list (instance): instance of :class:`RouteTargetList`
            import_route_target_list (instance): instance of :class:`RouteTargetList`
            export_route_target_list (instance): instance of :class:`RouteTargetList`
            router_external (instance): instance of :class:`xsd:boolean`
            is_shared (instance): instance of :class:`xsd:boolean`
            external_ipam (instance): instance of :class:`xsd:boolean`
            flood_unknown_unicast (instance): instance of :class:`xsd:boolean`
            multi_policy_service_chains_enabled (instance): instance of :class:`xsd:boolean`
            address_allocation_mode (instance): instance of :class:`xsd:string`
            virtual_network_fat_flow_protocols (instance): instance of :class:`FatFlowProtocols`
            mac_learning_enabled (instance): instance of :class:`xsd:boolean`
            mac_limit_control (instance): instance of :class:`MACLimitControlType`
            mac_move_control (instance): instance of :class:`MACMoveLimitControlType`
            mac_aging_time (instance): instance of :class:`xsd:integer`
            pbb_evpn_enable (instance): instance of :class:`xsd:boolean`
            pbb_etree_enable (instance): instance of :class:`xsd:boolean`
            layer2_control_word (instance): instance of :class:`xsd:boolean`
            igmp_enable (instance): instance of :class:`xsd:boolean`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualNetworkTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_network_name:
            self._name = 'default-virtual-network'
        else:
            self._name = virtual_network_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if security_logging_object_refs:
            for ln in security_logging_object_refs:
                self.add_security_logging_object (ln)
        if qos_config_refs:
            for ln in qos_config_refs:
                self.add_qos_config (ln)
        if network_ipam_ref_infos:
            for ln, ref in network_ipam_ref_infos:
                self.add_network_ipam (ln, ref)
        if network_policy_ref_infos:
            for ln, ref in network_policy_ref_infos:
                self.add_network_policy (ln, ref)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if route_table_refs:
            for ln in route_table_refs:
                self.add_route_table (ln)
        if multicast_policy_refs:
            for ln in multicast_policy_refs:
                self.add_multicast_policy (ln)
        if bgpvpn_refs:
            for ln in bgpvpn_refs:
                self.add_bgpvpn (ln)
        if intent_map_refs:
            for ln in intent_map_refs:
                self.add_intent_map (ln)
        if routing_policy_ref_infos:
            for ln, ref in routing_policy_ref_infos:
                self.add_routing_policy (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.ecmp_hashing_include_fields = ecmp_hashing_include_fields
        self.virtual_network_category = virtual_network_category
        self.virtual_network_properties = virtual_network_properties
        self.virtual_network_routed_properties = virtual_network_routed_properties
        self.provider_properties = provider_properties
        self.virtual_network_network_id = virtual_network_network_id
        self.is_provider_network = is_provider_network
        self.port_security_enabled = port_security_enabled
        self.fabric_snat = fabric_snat
        self.route_target_list = route_target_list
        self.import_route_target_list = import_route_target_list
        self.export_route_target_list = export_route_target_list
        self.router_external = router_external
        self.is_shared = is_shared
        self.external_ipam = external_ipam
        self.flood_unknown_unicast = flood_unknown_unicast
        self.multi_policy_service_chains_enabled = multi_policy_service_chains_enabled
        self.address_allocation_mode = address_allocation_mode
        self.virtual_network_fat_flow_protocols = virtual_network_fat_flow_protocols
        self.mac_learning_enabled = mac_learning_enabled
        self.mac_limit_control = mac_limit_control
        self.mac_move_control = mac_move_control
        self.mac_aging_time = mac_aging_time
        self.pbb_evpn_enable = pbb_evpn_enable
        self.pbb_etree_enable = pbb_etree_enable
        self.layer2_control_word = layer2_control_word
        self.igmp_enable = igmp_enable
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_security_logging_objects ():
            self.add_security_logging_object (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_qos_configs ():
            self.add_qos_config (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_network_ipams ():
            self.add_network_ipam (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_network_policys ():
            self.add_network_policy (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_route_tables ():
            self.add_route_table (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_multicast_policys ():
            self.add_multicast_policy (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_bgpvpns ():
            self.add_bgpvpn (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_intent_maps ():
            self.add_intent_map (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_routing_policys ():
            self.add_routing_policy (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_security_logging_object (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SecurityLoggingObject` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`SecurityLoggingObject`): obj to link
        '''
        if self._obj:
            self._obj.add_security_logging_object (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('security_logging_object', cfixture.ConrtailLink('security_logging_object', 'virtual_network', 'security_logging_object', ['ref'], lo))
    # end add_security_logging_object_link

    def get_security_logging_objects (self):
        return self.get_links ('security_logging_object')
    # end get_security_logging_objects
    def add_qos_config (self, lo, update_server = True, add_link = True):
        '''
        add :class:`QosConfig` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`QosConfig`): obj to link
        '''
        if self._obj:
            self._obj.add_qos_config (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('qos_config', cfixture.ConrtailLink('qos_config', 'virtual_network', 'qos_config', ['ref'], lo))
    # end add_qos_config_link

    def get_qos_configs (self):
        return self.get_links ('qos_config')
    # end get_qos_configs
    def add_network_ipam (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`NetworkIpam` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`NetworkIpam`): obj to link
            ref (:class:`VnSubnetsType`): property of the link object
        '''
        if self._obj:
            self._obj.add_network_ipam (lo, ref)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('network_ipam', cfixture.ConrtailLink('network_ipam', 'virtual_network', 'network_ipam', ['ref'], (lo, ref)))
    # end add_network_ipam_link

    def get_network_ipams (self):
        return self.get_links ('network_ipam')
    # end get_network_ipams
    def add_network_policy (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`NetworkPolicy` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`NetworkPolicy`): obj to link
            ref (:class:`VirtualNetworkPolicyType`): property of the link object
        '''
        if self._obj:
            self._obj.add_network_policy (lo, ref)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('network_policy', cfixture.ConrtailLink('network_policy', 'virtual_network', 'network_policy', ['ref'], (lo, ref)))
    # end add_network_policy_link

    def get_network_policys (self):
        return self.get_links ('network_policy')
    # end get_network_policys
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'virtual_network', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_route_table (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RouteTable` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`RouteTable`): obj to link
        '''
        if self._obj:
            self._obj.add_route_table (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('route_table', cfixture.ConrtailLink('route_table', 'virtual_network', 'route_table', ['ref'], lo))
    # end add_route_table_link

    def get_route_tables (self):
        return self.get_links ('route_table')
    # end get_route_tables
    def add_multicast_policy (self, lo, update_server = True, add_link = True):
        '''
        add :class:`MulticastPolicy` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`MulticastPolicy`): obj to link
        '''
        if self._obj:
            self._obj.add_multicast_policy (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('multicast_policy', cfixture.ConrtailLink('multicast_policy', 'virtual_network', 'multicast_policy', ['ref'], lo))
    # end add_multicast_policy_link

    def get_multicast_policys (self):
        return self.get_links ('multicast_policy')
    # end get_multicast_policys
    def add_bgpvpn (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Bgpvpn` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`Bgpvpn`): obj to link
        '''
        if self._obj:
            self._obj.add_bgpvpn (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('bgpvpn', cfixture.ConrtailLink('bgpvpn', 'virtual_network', 'bgpvpn', ['ref'], lo))
    # end add_bgpvpn_link

    def get_bgpvpns (self):
        return self.get_links ('bgpvpn')
    # end get_bgpvpns
    def add_intent_map (self, lo, update_server = True, add_link = True):
        '''
        add :class:`IntentMap` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`IntentMap`): obj to link
        '''
        if self._obj:
            self._obj.add_intent_map (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('intent_map', cfixture.ConrtailLink('intent_map', 'virtual_network', 'intent_map', ['ref'], lo))
    # end add_intent_map_link

    def get_intent_maps (self):
        return self.get_links ('intent_map')
    # end get_intent_maps
    def add_routing_policy (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`RoutingPolicy` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`RoutingPolicy`): obj to link
            ref (:class:`RoutingPolicyType`): property of the link object
        '''
        if self._obj:
            self._obj.add_routing_policy (lo, ref)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('routing_policy', cfixture.ConrtailLink('routing_policy', 'virtual_network', 'routing_policy', ['ref'], (lo, ref)))
    # end add_routing_policy_link

    def get_routing_policys (self):
        return self.get_links ('routing_policy')
    # end get_routing_policys
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualNetwork`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_network_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_network', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_ecmp_hashing_include_fields(self.ecmp_hashing_include_fields or vnc_api.gen.resource_xsd.EcmpHashingIncludeFields.populate())
        self._obj.set_virtual_network_category(self.virtual_network_category or GeneratedsSuper.populate_string("virtual_network_category"))
        self._obj.set_virtual_network_properties(self.virtual_network_properties or vnc_api.gen.resource_xsd.VirtualNetworkType.populate())
        self._obj.set_virtual_network_routed_properties(self.virtual_network_routed_properties or vnc_api.gen.resource_xsd.VirtualNetworkRoutedPropertiesType.populate())
        self._obj.set_provider_properties(self.provider_properties or vnc_api.gen.resource_xsd.ProviderDetails.populate())
        self._obj.set_virtual_network_network_id(self.virtual_network_network_id or GeneratedsSuper.populate_integer("virtual_network_network_id"))
        self._obj.set_is_provider_network(self.is_provider_network or GeneratedsSuper.populate_boolean("is_provider_network"))
        self._obj.set_port_security_enabled(self.port_security_enabled or GeneratedsSuper.populate_boolean("port_security_enabled"))
        self._obj.set_fabric_snat(self.fabric_snat or GeneratedsSuper.populate_boolean("fabric_snat"))
        self._obj.set_route_target_list(self.route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_import_route_target_list(self.import_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_export_route_target_list(self.export_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_router_external(self.router_external or GeneratedsSuper.populate_boolean("router_external"))
        self._obj.set_is_shared(self.is_shared or GeneratedsSuper.populate_boolean("is_shared"))
        self._obj.set_external_ipam(self.external_ipam or GeneratedsSuper.populate_boolean("external_ipam"))
        self._obj.set_flood_unknown_unicast(self.flood_unknown_unicast or GeneratedsSuper.populate_boolean("flood_unknown_unicast"))
        self._obj.set_multi_policy_service_chains_enabled(self.multi_policy_service_chains_enabled or GeneratedsSuper.populate_boolean("multi_policy_service_chains_enabled"))
        self._obj.set_address_allocation_mode(self.address_allocation_mode or GeneratedsSuper.populate_string("address_allocation_mode"))
        self._obj.set_virtual_network_fat_flow_protocols(self.virtual_network_fat_flow_protocols or vnc_api.gen.resource_xsd.FatFlowProtocols.populate())
        self._obj.set_mac_learning_enabled(self.mac_learning_enabled or GeneratedsSuper.populate_boolean("mac_learning_enabled"))
        self._obj.set_mac_limit_control(self.mac_limit_control or vnc_api.gen.resource_xsd.MACLimitControlType.populate())
        self._obj.set_mac_move_control(self.mac_move_control or vnc_api.gen.resource_xsd.MACMoveLimitControlType.populate())
        self._obj.set_mac_aging_time(self.mac_aging_time or GeneratedsSuper.populate_integer("mac_aging_time"))
        self._obj.set_pbb_evpn_enable(self.pbb_evpn_enable or GeneratedsSuper.populate_boolean("pbb_evpn_enable"))
        self._obj.set_pbb_etree_enable(self.pbb_etree_enable or GeneratedsSuper.populate_boolean("pbb_etree_enable"))
        self._obj.set_layer2_control_word(self.layer2_control_word or GeneratedsSuper.populate_boolean("layer2_control_word"))
        self._obj.set_igmp_enable(self.igmp_enable or GeneratedsSuper.populate_boolean("igmp_enable"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualNetworkTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.VirtualNetwork(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_network_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.ecmp_hashing_include_fields = self.ecmp_hashing_include_fields
                self._obj.virtual_network_category = self.virtual_network_category
                self._obj.virtual_network_properties = self.virtual_network_properties
                self._obj.virtual_network_routed_properties = self.virtual_network_routed_properties
                self._obj.provider_properties = self.provider_properties
                self._obj.virtual_network_network_id = self.virtual_network_network_id
                self._obj.is_provider_network = self.is_provider_network
                self._obj.port_security_enabled = self.port_security_enabled
                self._obj.fabric_snat = self.fabric_snat
                self._obj.route_target_list = self.route_target_list
                self._obj.import_route_target_list = self.import_route_target_list
                self._obj.export_route_target_list = self.export_route_target_list
                self._obj.router_external = self.router_external
                self._obj.is_shared = self.is_shared
                self._obj.external_ipam = self.external_ipam
                self._obj.flood_unknown_unicast = self.flood_unknown_unicast
                self._obj.multi_policy_service_chains_enabled = self.multi_policy_service_chains_enabled
                self._obj.address_allocation_mode = self.address_allocation_mode
                self._obj.virtual_network_fat_flow_protocols = self.virtual_network_fat_flow_protocols
                self._obj.mac_learning_enabled = self.mac_learning_enabled
                self._obj.mac_limit_control = self.mac_limit_control
                self._obj.mac_move_control = self.mac_move_control
                self._obj.mac_aging_time = self.mac_aging_time
                self._obj.pbb_evpn_enable = self.pbb_evpn_enable
                self._obj.pbb_etree_enable = self.pbb_etree_enable
                self._obj.layer2_control_word = self.layer2_control_word
                self._obj.igmp_enable = self.igmp_enable
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_network_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_network_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_network_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_networks() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_networks.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualNetworkTestFixtureGen

class VirtualPortGroupTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualPortGroup`
    """
    def __init__(self, conn_drv, virtual_port_group_name=None, parent_fixt=None, auto_prop_val=False, physical_interface_ref_infos = None, virtual_machine_interface_refs = None, security_group_refs = None, port_profile_refs = None, tag_refs = None, virtual_port_group_lacp_enabled=None, virtual_port_group_trunk_port_id=None, virtual_port_group_user_created=None, virtual_port_group_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualPortGroupTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            virtual_port_group_name (str): Name of virtual_port_group
            parent_fixt (:class:`.FabricTestFixtureGen`): Parent fixture
            physical_interface (list): list of tuple (:class:`PhysicalInterface`, :class: `VpgInterfaceParametersType`) type
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            security_group (list): list of :class:`SecurityGroup` type
            port_profile (list): list of :class:`PortProfile` type
            tag (list): list of :class:`Tag` type
            virtual_port_group_lacp_enabled (instance): instance of :class:`xsd:boolean`
            virtual_port_group_trunk_port_id (instance): instance of :class:`xsd:string`
            virtual_port_group_user_created (instance): instance of :class:`xsd:boolean`
            virtual_port_group_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualPortGroupTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_port_group_name:
            self._name = 'default-virtual-port-group'
        else:
            self._name = virtual_port_group_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if physical_interface_ref_infos:
            for ln, ref in physical_interface_ref_infos:
                self.add_physical_interface (ln, ref)
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if security_group_refs:
            for ln in security_group_refs:
                self.add_security_group (ln)
        if port_profile_refs:
            for ln in port_profile_refs:
                self.add_port_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.virtual_port_group_lacp_enabled = virtual_port_group_lacp_enabled
        self.virtual_port_group_trunk_port_id = virtual_port_group_trunk_port_id
        self.virtual_port_group_user_created = virtual_port_group_user_created
        self.virtual_port_group_type = virtual_port_group_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_interfaces ():
            self.add_physical_interface (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_security_groups ():
            self.add_security_group (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_port_profiles ():
            self.add_port_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_interface (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`PhysicalInterface` link to :class:`VirtualPortGroup`
        Args:
            lo (:class:`PhysicalInterface`): obj to link
            ref (:class:`VpgInterfaceParametersType`): property of the link object
        '''
        if self._obj:
            self._obj.add_physical_interface (lo, ref)
            if update_server:
                self._conn_drv.virtual_port_group_update (self._obj)

        if add_link:
            self.add_link('physical_interface', cfixture.ConrtailLink('physical_interface', 'virtual_port_group', 'physical_interface', ['ref'], (lo, ref)))
    # end add_physical_interface_link

    def get_physical_interfaces (self):
        return self.get_links ('physical_interface')
    # end get_physical_interfaces
    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`VirtualPortGroup`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.virtual_port_group_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'virtual_port_group', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_security_group (self, lo, update_server = True, add_link = True):
        '''
        add :class:`SecurityGroup` link to :class:`VirtualPortGroup`
        Args:
            lo (:class:`SecurityGroup`): obj to link
        '''
        if self._obj:
            self._obj.add_security_group (lo)
            if update_server:
                self._conn_drv.virtual_port_group_update (self._obj)

        if add_link:
            self.add_link('security_group', cfixture.ConrtailLink('security_group', 'virtual_port_group', 'security_group', ['ref'], lo))
    # end add_security_group_link

    def get_security_groups (self):
        return self.get_links ('security_group')
    # end get_security_groups
    def add_port_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PortProfile` link to :class:`VirtualPortGroup`
        Args:
            lo (:class:`PortProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_port_profile (lo)
            if update_server:
                self._conn_drv.virtual_port_group_update (self._obj)

        if add_link:
            self.add_link('port_profile', cfixture.ConrtailLink('port_profile', 'virtual_port_group', 'port_profile', ['ref'], lo))
    # end add_port_profile_link

    def get_port_profiles (self):
        return self.get_links ('port_profile')
    # end get_port_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualPortGroup`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_port_group_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_port_group', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_virtual_port_group_lacp_enabled(self.virtual_port_group_lacp_enabled or GeneratedsSuper.populate_boolean("virtual_port_group_lacp_enabled"))
        self._obj.set_virtual_port_group_trunk_port_id(self.virtual_port_group_trunk_port_id or GeneratedsSuper.populate_string("virtual_port_group_trunk_port_id"))
        self._obj.set_virtual_port_group_user_created(self.virtual_port_group_user_created or GeneratedsSuper.populate_boolean("virtual_port_group_user_created"))
        self._obj.set_virtual_port_group_type(self.virtual_port_group_type or GeneratedsSuper.populate_string("virtual_port_group_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualPortGroupTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("['fabric', 'project']")

        self._obj = vnc_api.VirtualPortGroup(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.virtual_port_group_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.virtual_port_group_lacp_enabled = self.virtual_port_group_lacp_enabled
                self._obj.virtual_port_group_trunk_port_id = self.virtual_port_group_trunk_port_id
                self._obj.virtual_port_group_user_created = self.virtual_port_group_user_created
                self._obj.virtual_port_group_type = self.virtual_port_group_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_port_group_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_port_group_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_port_group_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_virtual_port_groups() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.virtual_port_groups.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualPortGroupTestFixtureGen

class ServiceApplianceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceAppliance`
    """
    def __init__(self, conn_drv, service_appliance_name=None, parent_fixt=None, auto_prop_val=False, physical_interface_ref_infos = None, tag_refs = None, service_appliance_user_credentials=None, service_appliance_ip_address=None, service_appliance_virtualization_type=None, service_appliance_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceApplianceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_appliance_name (str): Name of service_appliance
            parent_fixt (:class:`.ServiceApplianceSetTestFixtureGen`): Parent fixture
            physical_interface (list): list of tuple (:class:`PhysicalInterface`, :class: `ServiceApplianceInterfaceType`) type
            tag (list): list of :class:`Tag` type
            service_appliance_user_credentials (instance): instance of :class:`UserCredentials`
            service_appliance_ip_address (instance): instance of :class:`xsd:string`
            service_appliance_virtualization_type (instance): instance of :class:`xsd:string`
            service_appliance_properties (instance): instance of :class:`KeyValuePairs`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceApplianceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_appliance_name:
            self._name = 'default-service-appliance'
        else:
            self._name = service_appliance_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if physical_interface_ref_infos:
            for ln, ref in physical_interface_ref_infos:
                self.add_physical_interface (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_appliance_user_credentials = service_appliance_user_credentials
        self.service_appliance_ip_address = service_appliance_ip_address
        self.service_appliance_virtualization_type = service_appliance_virtualization_type
        self.service_appliance_properties = service_appliance_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_interfaces ():
            self.add_physical_interface (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_interface (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`PhysicalInterface` link to :class:`ServiceAppliance`
        Args:
            lo (:class:`PhysicalInterface`): obj to link
            ref (:class:`ServiceApplianceInterfaceType`): property of the link object
        '''
        if self._obj:
            self._obj.add_physical_interface (lo, ref)
            if update_server:
                self._conn_drv.service_appliance_update (self._obj)

        if add_link:
            self.add_link('physical_interface', cfixture.ConrtailLink('physical_interface', 'service_appliance', 'physical_interface', ['ref'], (lo, ref)))
    # end add_physical_interface_link

    def get_physical_interfaces (self):
        return self.get_links ('physical_interface')
    # end get_physical_interfaces
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceAppliance`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_appliance_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_appliance', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_appliance_user_credentials(self.service_appliance_user_credentials or vnc_api.gen.resource_xsd.UserCredentials.populate())
        self._obj.set_service_appliance_ip_address(self.service_appliance_ip_address or GeneratedsSuper.populate_string("service_appliance_ip_address"))
        self._obj.set_service_appliance_virtualization_type(self.service_appliance_virtualization_type or GeneratedsSuper.populate_string("service_appliance_virtualization_type"))
        self._obj.set_service_appliance_properties(self.service_appliance_properties or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceApplianceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ServiceApplianceSetTestFixtureGen(self._conn_drv, 'default-service-appliance-set'))

        self._obj = vnc_api.ServiceAppliance(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_appliance_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_appliance_user_credentials = self.service_appliance_user_credentials
                self._obj.service_appliance_ip_address = self.service_appliance_ip_address
                self._obj.service_appliance_virtualization_type = self.service_appliance_virtualization_type
                self._obj.service_appliance_properties = self.service_appliance_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_appliance_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_appliance_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_appliance_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_appliances() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_appliances.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceApplianceTestFixtureGen

class NamespaceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Namespace`
    """
    def __init__(self, conn_drv, namespace_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, namespace_cidr=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NamespaceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            namespace_name (str): Name of namespace
            parent_fixt (:class:`.DomainTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            namespace_cidr (instance): instance of :class:`SubnetType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NamespaceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not namespace_name:
            self._name = 'default-namespace'
        else:
            self._name = namespace_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.namespace_cidr = namespace_cidr
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Namespace`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.namespace_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'namespace', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_namespace_cidr(self.namespace_cidr or vnc_api.gen.resource_xsd.SubnetType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NamespaceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(DomainTestFixtureGen(self._conn_drv, 'default-domain'))

        self._obj = vnc_api.Namespace(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.namespace_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.namespace_cidr = self.namespace_cidr
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.namespace_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.namespace_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.namespace_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_namespaces() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.namespaces.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NamespaceTestFixtureGen

class FeatureTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Feature`
    """
    def __init__(self, conn_drv, feature_name=None, parent_fixt=None, auto_prop_val=False, feature_refs = None, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create FeatureTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            feature_name (str): Name of feature
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            feature (list): list of :class:`Feature` type
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(FeatureTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not feature_name:
            self._name = 'default-feature'
        else:
            self._name = feature_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if feature_refs:
            for ln in feature_refs:
                self.add_feature (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_features ():
            self.add_feature (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_feature (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Feature` link to :class:`Feature`
        Args:
            lo (:class:`Feature`): obj to link
        '''
        if self._obj:
            self._obj.add_feature (lo)
            if update_server:
                self._conn_drv.feature_update (self._obj)

        if add_link:
            self.add_link('feature', cfixture.ConrtailLink('feature', 'feature', 'feature', ['ref'], lo))
    # end add_feature_link

    def get_features (self):
        return self.get_links ('feature')
    # end get_features
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Feature`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.feature_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'feature', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(FeatureTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.Feature(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.feature_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.feature_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.feature_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.feature_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_features() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.features.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class FeatureTestFixtureGen

class StormControlProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StormControlProfile`
    """
    def __init__(self, conn_drv, storm_control_profile_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, storm_control_parameters=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StormControlProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            storm_control_profile_name (str): Name of storm_control_profile
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            storm_control_parameters (instance): instance of :class:`StormControlParameters`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StormControlProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not storm_control_profile_name:
            self._name = 'default-storm-control-profile'
        else:
            self._name = storm_control_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.storm_control_parameters = storm_control_parameters
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StormControlProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.storm_control_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'storm_control_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_storm_control_parameters(self.storm_control_parameters or vnc_api.gen.resource_xsd.StormControlParameters.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StormControlProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.StormControlProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.storm_control_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.storm_control_parameters = self.storm_control_parameters
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.storm_control_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.storm_control_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.storm_control_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_storm_control_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.storm_control_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StormControlProfileTestFixtureGen

class DeviceImageTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DeviceImage`
    """
    def __init__(self, conn_drv, device_image_name=None, parent_fixt=None, auto_prop_val=False, hardware_refs = None, tag_refs = None, device_image_vendor_name=None, device_image_device_family=None, device_image_supported_platforms=None, device_image_os_version=None, device_image_file_uri=None, device_image_size=None, device_image_md5=None, device_image_sha1=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DeviceImageTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            device_image_name (str): Name of device_image
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            hardware (list): list of :class:`Hardware` type
            tag (list): list of :class:`Tag` type
            device_image_vendor_name (instance): instance of :class:`xsd:string`
            device_image_device_family (instance): instance of :class:`xsd:string`
            device_image_supported_platforms (instance): instance of :class:`DevicePlatformListType`
            device_image_os_version (instance): instance of :class:`xsd:string`
            device_image_file_uri (instance): instance of :class:`xsd:string`
            device_image_size (instance): instance of :class:`xsd:integer`
            device_image_md5 (instance): instance of :class:`xsd:string`
            device_image_sha1 (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DeviceImageTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not device_image_name:
            self._name = 'default-device-image'
        else:
            self._name = device_image_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if hardware_refs:
            for ln in hardware_refs:
                self.add_hardware (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.device_image_vendor_name = device_image_vendor_name
        self.device_image_device_family = device_image_device_family
        self.device_image_supported_platforms = device_image_supported_platforms
        self.device_image_os_version = device_image_os_version
        self.device_image_file_uri = device_image_file_uri
        self.device_image_size = device_image_size
        self.device_image_md5 = device_image_md5
        self.device_image_sha1 = device_image_sha1
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_hardwares ():
            self.add_hardware (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_hardware (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Hardware` link to :class:`DeviceImage`
        Args:
            lo (:class:`Hardware`): obj to link
        '''
        if self._obj:
            self._obj.add_hardware (lo)
            if update_server:
                self._conn_drv.device_image_update (self._obj)

        if add_link:
            self.add_link('hardware', cfixture.ConrtailLink('hardware', 'device_image', 'hardware', ['ref'], lo))
    # end add_hardware_link

    def get_hardwares (self):
        return self.get_links ('hardware')
    # end get_hardwares
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DeviceImage`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.device_image_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'device_image', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_device_image_vendor_name(self.device_image_vendor_name or GeneratedsSuper.populate_string("device_image_vendor_name"))
        self._obj.set_device_image_device_family(self.device_image_device_family or GeneratedsSuper.populate_string("device_image_device_family"))
        self._obj.set_device_image_supported_platforms(self.device_image_supported_platforms or vnc_api.gen.resource_xsd.DevicePlatformListType.populate())
        self._obj.set_device_image_os_version(self.device_image_os_version or GeneratedsSuper.populate_string("device_image_os_version"))
        self._obj.set_device_image_file_uri(self.device_image_file_uri or GeneratedsSuper.populate_string("device_image_file_uri"))
        self._obj.set_device_image_size(self.device_image_size or GeneratedsSuper.populate_integer("device_image_size"))
        self._obj.set_device_image_md5(self.device_image_md5 or GeneratedsSuper.populate_string("device_image_md5"))
        self._obj.set_device_image_sha1(self.device_image_sha1 or GeneratedsSuper.populate_string("device_image_sha1"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DeviceImageTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.DeviceImage(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.device_image_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.device_image_vendor_name = self.device_image_vendor_name
                self._obj.device_image_device_family = self.device_image_device_family
                self._obj.device_image_supported_platforms = self.device_image_supported_platforms
                self._obj.device_image_os_version = self.device_image_os_version
                self._obj.device_image_file_uri = self.device_image_file_uri
                self._obj.device_image_size = self.device_image_size
                self._obj.device_image_md5 = self.device_image_md5
                self._obj.device_image_sha1 = self.device_image_sha1
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.device_image_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.device_image_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.device_image_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_device_images() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.device_images.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DeviceImageTestFixtureGen

class PhysicalInterfaceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.PhysicalInterface`
    """
    def __init__(self, conn_drv, physical_interface_name=None, parent_fixt=None, auto_prop_val=False, physical_interface_refs = None, port_refs = None, tag_refs = None, ethernet_segment_identifier=None, physical_interface_type=None, physical_interface_mac_addresses=None, physical_interface_port_id=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create PhysicalInterfaceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            physical_interface_name (str): Name of physical_interface
            parent_fixt (:class:`.PhysicalRouterTestFixtureGen`): Parent fixture
            physical_interface (list): list of :class:`PhysicalInterface` type
            port (list): list of :class:`Port` type
            tag (list): list of :class:`Tag` type
            ethernet_segment_identifier (instance): instance of :class:`xsd:string`
            physical_interface_type (instance): instance of :class:`xsd:string`
            physical_interface_mac_addresses (instance): instance of :class:`MacAddressesType`
            physical_interface_port_id (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(PhysicalInterfaceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not physical_interface_name:
            self._name = 'default-physical-interface'
        else:
            self._name = physical_interface_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if physical_interface_refs:
            for ln in physical_interface_refs:
                self.add_physical_interface (ln)
        if port_refs:
            for ln in port_refs:
                self.add_port (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.ethernet_segment_identifier = ethernet_segment_identifier
        self.physical_interface_type = physical_interface_type
        self.physical_interface_mac_addresses = physical_interface_mac_addresses
        self.physical_interface_port_id = physical_interface_port_id
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_physical_interfaces ():
            self.add_physical_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_ports ():
            self.add_port (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_physical_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`PhysicalInterface` link to :class:`PhysicalInterface`
        Args:
            lo (:class:`PhysicalInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_physical_interface (lo)
            if update_server:
                self._conn_drv.physical_interface_update (self._obj)

        if add_link:
            self.add_link('physical_interface', cfixture.ConrtailLink('physical_interface', 'physical_interface', 'physical_interface', ['ref'], lo))
    # end add_physical_interface_link

    def get_physical_interfaces (self):
        return self.get_links ('physical_interface')
    # end get_physical_interfaces
    def add_port (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Port` link to :class:`PhysicalInterface`
        Args:
            lo (:class:`Port`): obj to link
        '''
        if self._obj:
            self._obj.add_port (lo)
            if update_server:
                self._conn_drv.physical_interface_update (self._obj)

        if add_link:
            self.add_link('port', cfixture.ConrtailLink('port', 'physical_interface', 'port', ['ref'], lo))
    # end add_port_link

    def get_ports (self):
        return self.get_links ('port')
    # end get_ports
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`PhysicalInterface`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.physical_interface_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'physical_interface', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_ethernet_segment_identifier(self.ethernet_segment_identifier or GeneratedsSuper.populate_string("ethernet_segment_identifier"))
        self._obj.set_physical_interface_type(self.physical_interface_type or GeneratedsSuper.populate_string("physical_interface_type"))
        self._obj.set_physical_interface_mac_addresses(self.physical_interface_mac_addresses or vnc_api.gen.resource_xsd.MacAddressesType.populate())
        self._obj.set_physical_interface_port_id(self.physical_interface_port_id or GeneratedsSuper.populate_string("physical_interface_port_id"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(PhysicalInterfaceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(PhysicalRouterTestFixtureGen(self._conn_drv, 'default-physical-router'))

        self._obj = vnc_api.PhysicalInterface(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.physical_interface_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.ethernet_segment_identifier = self.ethernet_segment_identifier
                self._obj.physical_interface_type = self.physical_interface_type
                self._obj.physical_interface_mac_addresses = self.physical_interface_mac_addresses
                self._obj.physical_interface_port_id = self.physical_interface_port_id
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.physical_interface_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.physical_interface_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.physical_interface_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_physical_interfaces() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.physical_interfaces.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class PhysicalInterfaceTestFixtureGen

class AccessControlListTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AccessControlList`
    """
    def __init__(self, conn_drv, access_control_list_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, access_control_list_entries=None, access_control_list_hash=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AccessControlListTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            access_control_list_name (str): Name of access_control_list
            parent_fixt (:class:`.VirtualNetworkTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            access_control_list_entries (instance): instance of :class:`AclEntriesType`
            access_control_list_hash (instance): instance of :class:`xsd:unsignedLong`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AccessControlListTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not access_control_list_name:
            self._name = 'default-access-control-list'
        else:
            self._name = access_control_list_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.access_control_list_entries = access_control_list_entries
        self.access_control_list_hash = access_control_list_hash
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AccessControlList`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.access_control_list_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'access_control_list', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_access_control_list_entries(self.access_control_list_entries or vnc_api.gen.resource_xsd.AclEntriesType.populate())
        self._obj.set_access_control_list_hash(self.access_control_list_hash or GeneratedsSuper.populate_unsignedLong("access_control_list_hash"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AccessControlListTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("['virtual-network', 'security-group']")

        self._obj = vnc_api.AccessControlList(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.access_control_list_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.access_control_list_entries = self.access_control_list_entries
                self._obj.access_control_list_hash = self.access_control_list_hash
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.access_control_list_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.access_control_list_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.access_control_list_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_access_control_lists() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.access_control_lists.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AccessControlListTestFixtureGen

class NodeTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Node`
    """
    def __init__(self, conn_drv, node_name=None, parent_fixt=None, auto_prop_val=False, node_profile_refs = None, tag_refs = None, node_type=None, esxi_info=None, ip_address=None, hostname=None, bms_info=None, mac_address=None, disk_partition=None, interface_name=None, cloud_info=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create NodeTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            node_name (str): Name of node
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            node_profile (list): list of :class:`NodeProfile` type
            tag (list): list of :class:`Tag` type
            node_type (instance): instance of :class:`xsd:string`
            esxi_info (instance): instance of :class:`ESXIHostInfo`
            ip_address (instance): instance of :class:`xsd:string`
            hostname (instance): instance of :class:`xsd:string`
            bms_info (instance): instance of :class:`BaremetalServerInfo`
            mac_address (instance): instance of :class:`xsd:string`
            disk_partition (instance): instance of :class:`xsd:string`
            interface_name (instance): instance of :class:`xsd:string`
            cloud_info (instance): instance of :class:`CloudInstanceInfo`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(NodeTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not node_name:
            self._name = 'default-node'
        else:
            self._name = node_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if node_profile_refs:
            for ln in node_profile_refs:
                self.add_node_profile (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.node_type = node_type
        self.esxi_info = esxi_info
        self.ip_address = ip_address
        self.hostname = hostname
        self.bms_info = bms_info
        self.mac_address = mac_address
        self.disk_partition = disk_partition
        self.interface_name = interface_name
        self.cloud_info = cloud_info
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_node_profiles ():
            self.add_node_profile (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_node_profile (self, lo, update_server = True, add_link = True):
        '''
        add :class:`NodeProfile` link to :class:`Node`
        Args:
            lo (:class:`NodeProfile`): obj to link
        '''
        if self._obj:
            self._obj.add_node_profile (lo)
            if update_server:
                self._conn_drv.node_update (self._obj)

        if add_link:
            self.add_link('node_profile', cfixture.ConrtailLink('node_profile', 'node', 'node_profile', ['ref'], lo))
    # end add_node_profile_link

    def get_node_profiles (self):
        return self.get_links ('node_profile')
    # end get_node_profiles
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Node`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.node_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'node', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_node_type(self.node_type or GeneratedsSuper.populate_string("node_type"))
        self._obj.set_esxi_info(self.esxi_info or vnc_api.gen.resource_xsd.ESXIHostInfo.populate())
        self._obj.set_ip_address(self.ip_address or GeneratedsSuper.populate_string("ip_address"))
        self._obj.set_hostname(self.hostname or GeneratedsSuper.populate_string("hostname"))
        self._obj.set_bms_info(self.bms_info or vnc_api.gen.resource_xsd.BaremetalServerInfo.populate())
        self._obj.set_mac_address(self.mac_address or GeneratedsSuper.populate_string("mac_address"))
        self._obj.set_disk_partition(self.disk_partition or GeneratedsSuper.populate_string("disk_partition"))
        self._obj.set_interface_name(self.interface_name or GeneratedsSuper.populate_string("interface_name"))
        self._obj.set_cloud_info(self.cloud_info or vnc_api.gen.resource_xsd.CloudInstanceInfo.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(NodeTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.Node(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.node_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.node_type = self.node_type
                self._obj.esxi_info = self.esxi_info
                self._obj.ip_address = self.ip_address
                self._obj.hostname = self.hostname
                self._obj.bms_info = self.bms_info
                self._obj.mac_address = self.mac_address
                self._obj.disk_partition = self.disk_partition
                self._obj.interface_name = self.interface_name
                self._obj.cloud_info = self.cloud_info
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.node_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.node_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.node_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_nodes() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.nodes.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class NodeTestFixtureGen

class CustomerAttachmentTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.CustomerAttachment`
    """
    def __init__(self, conn_drv, customer_attachment_name=None, auto_prop_val=False, virtual_machine_interface_refs = None, floating_ip_refs = None, tag_refs = None, attachment_address=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create CustomerAttachmentTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            virtual_machine_interface (list): list of :class:`VirtualMachineInterface` type
            floating_ip (list): list of :class:`FloatingIp` type
            tag (list): list of :class:`Tag` type
            attachment_address (instance): instance of :class:`AttachmentAddressType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(CustomerAttachmentTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not customer_attachment_name:
            self._name = 'default-customer-attachment'
        else:
            self._name = customer_attachment_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if virtual_machine_interface_refs:
            for ln in virtual_machine_interface_refs:
                self.add_virtual_machine_interface (ln)
        if floating_ip_refs:
            for ln in floating_ip_refs:
                self.add_floating_ip (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.attachment_address = attachment_address
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_machine_interfaces ():
            self.add_virtual_machine_interface (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_floating_ips ():
            self.add_floating_ip (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_machine_interface (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualMachineInterface` link to :class:`CustomerAttachment`
        Args:
            lo (:class:`VirtualMachineInterface`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_machine_interface (lo)
            if update_server:
                self._conn_drv.customer_attachment_update (self._obj)

        if add_link:
            self.add_link('virtual_machine_interface', cfixture.ConrtailLink('virtual_machine_interface', 'customer_attachment', 'virtual_machine_interface', ['ref'], lo))
    # end add_virtual_machine_interface_link

    def get_virtual_machine_interfaces (self):
        return self.get_links ('virtual_machine_interface')
    # end get_virtual_machine_interfaces
    def add_floating_ip (self, lo, update_server = True, add_link = True):
        '''
        add :class:`FloatingIp` link to :class:`CustomerAttachment`
        Args:
            lo (:class:`FloatingIp`): obj to link
        '''
        if self._obj:
            self._obj.add_floating_ip (lo)
            if update_server:
                self._conn_drv.customer_attachment_update (self._obj)

        if add_link:
            self.add_link('floating_ip', cfixture.ConrtailLink('floating_ip', 'customer_attachment', 'floating_ip', ['ref'], lo))
    # end add_floating_ip_link

    def get_floating_ips (self):
        return self.get_links ('floating_ip')
    # end get_floating_ips
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`CustomerAttachment`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.customer_attachment_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'customer_attachment', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_attachment_address(self.attachment_address or vnc_api.gen.resource_xsd.AttachmentAddressType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(CustomerAttachmentTestFixtureGen, self).setUp()
        self._obj = vnc_api.CustomerAttachment(self._name)
        try:
            self._obj = self._conn_drv.customer_attachment_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.attachment_address = self.attachment_address
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.customer_attachment_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.customer_attachment_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.customer_attachment_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class CustomerAttachmentTestFixtureGen

class StructuredSyslogSlaProfileTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.StructuredSyslogSlaProfile`
    """
    def __init__(self, conn_drv, structured_syslog_sla_profile_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, structured_syslog_sla_params=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create StructuredSyslogSlaProfileTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            structured_syslog_sla_profile_name (str): Name of structured_syslog_sla_profile
            parent_fixt (:class:`.StructuredSyslogConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            structured_syslog_sla_params (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(StructuredSyslogSlaProfileTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not structured_syslog_sla_profile_name:
            self._name = 'default-structured-syslog-sla-profile'
        else:
            self._name = structured_syslog_sla_profile_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.structured_syslog_sla_params = structured_syslog_sla_params
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`StructuredSyslogSlaProfile`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.structured_syslog_sla_profile_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'structured_syslog_sla_profile', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_structured_syslog_sla_params(self.structured_syslog_sla_params or GeneratedsSuper.populate_string("structured_syslog_sla_params"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(StructuredSyslogSlaProfileTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(StructuredSyslogConfigTestFixtureGen(self._conn_drv, 'default-structured-syslog-config'))

        self._obj = vnc_api.StructuredSyslogSlaProfile(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.structured_syslog_sla_profile_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.structured_syslog_sla_params = self.structured_syslog_sla_params
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.structured_syslog_sla_profile_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.structured_syslog_sla_profile_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.structured_syslog_sla_profile_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_structured_syslog_sla_profiles() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.structured_syslog_sla_profiles.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class StructuredSyslogSlaProfileTestFixtureGen

class HostBasedServiceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.HostBasedService`
    """
    def __init__(self, conn_drv, host_based_service_name=None, parent_fixt=None, auto_prop_val=False, virtual_network_ref_infos = None, tag_refs = None, host_based_service_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create HostBasedServiceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            host_based_service_name (str): Name of host_based_service
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            virtual_network (list): list of tuple (:class:`VirtualNetwork`, :class: `ServiceVirtualNetworkType`) type
            tag (list): list of :class:`Tag` type
            host_based_service_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(HostBasedServiceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not host_based_service_name:
            self._name = 'default-host-based-service'
        else:
            self._name = host_based_service_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if virtual_network_ref_infos:
            for ln, ref in virtual_network_ref_infos:
                self.add_virtual_network (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.host_based_service_type = host_based_service_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_virtual_network (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`HostBasedService`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
            ref (:class:`ServiceVirtualNetworkType`): property of the link object
        '''
        if self._obj:
            self._obj.add_virtual_network (lo, ref)
            if update_server:
                self._conn_drv.host_based_service_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'host_based_service', 'virtual_network', ['ref'], (lo, ref)))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`HostBasedService`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.host_based_service_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'host_based_service', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_host_based_service_type(self.host_based_service_type or GeneratedsSuper.populate_string("host_based_service_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(HostBasedServiceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.HostBasedService(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.host_based_service_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.host_based_service_type = self.host_based_service_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.host_based_service_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.host_based_service_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.host_based_service_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_host_based_services() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.host_based_services.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class HostBasedServiceTestFixtureGen

class VirtualMachineTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.VirtualMachine`
    """
    def __init__(self, conn_drv, virtual_machine_name=None, auto_prop_val=False, service_instance_refs = None, tag_refs = None, server_type=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create VirtualMachineTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            %s_name (str): Name of %s
            service_instance (list): list of :class:`ServiceInstance` type
            tag (list): list of :class:`Tag` type
            server_type (instance): instance of :class:`xsd:string`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(VirtualMachineTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not virtual_machine_name:
            self._name = 'default-virtual-machine'
        else:
            self._name = virtual_machine_name
        self._obj = None
        self._auto_prop_val = auto_prop_val
        if service_instance_refs:
            for ln in service_instance_refs:
                self.add_service_instance (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.server_type = server_type
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`VirtualMachine`
        Args:
            lo (:class:`ServiceInstance`): obj to link
        '''
        if self._obj:
            self._obj.add_service_instance (lo)
            if update_server:
                self._conn_drv.virtual_machine_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'virtual_machine', 'service_instance', ['ref', 'derived'], lo))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`VirtualMachine`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.virtual_machine_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'virtual_machine', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_server_type(self.server_type or GeneratedsSuper.populate_string("server_type"))
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(VirtualMachineTestFixtureGen, self).setUp()
        self._obj = vnc_api.VirtualMachine(self._name)
        try:
            self._obj = self._conn_drv.virtual_machine_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.server_type = self.server_type
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.virtual_machine_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.virtual_machine_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.virtual_machine_delete(id = self._obj.uuid)
        except RefsExistError:
            return
    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class VirtualMachineTestFixtureGen

class InterfaceRouteTableTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.InterfaceRouteTable`
    """
    def __init__(self, conn_drv, interface_route_table_name=None, parent_fixt=None, auto_prop_val=False, service_instance_ref_infos = None, tag_refs = None, interface_route_table_routes=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create InterfaceRouteTableTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            interface_route_table_name (str): Name of interface_route_table
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_instance (list): list of tuple (:class:`ServiceInstance`, :class: `ServiceInterfaceTag`) type
            tag (list): list of :class:`Tag` type
            interface_route_table_routes (instance): instance of :class:`RouteTableType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(InterfaceRouteTableTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not interface_route_table_name:
            self._name = 'default-interface-route-table'
        else:
            self._name = interface_route_table_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_instance_ref_infos:
            for ln, ref in service_instance_ref_infos:
                self.add_service_instance (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.interface_route_table_routes = interface_route_table_routes
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`InterfaceRouteTable`
        Args:
            lo (:class:`ServiceInstance`): obj to link
            ref (:class:`ServiceInterfaceTag`): property of the link object
        '''
        if self._obj:
            self._obj.add_service_instance (lo, ref)
            if update_server:
                self._conn_drv.interface_route_table_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'interface_route_table', 'service_instance', ['ref', 'derived'], (lo, ref)))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`InterfaceRouteTable`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.interface_route_table_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'interface_route_table', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_interface_route_table_routes(self.interface_route_table_routes or vnc_api.gen.resource_xsd.RouteTableType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(InterfaceRouteTableTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.InterfaceRouteTable(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.interface_route_table_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.interface_route_table_routes = self.interface_route_table_routes
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.interface_route_table_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.interface_route_table_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.interface_route_table_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_interface_route_tables() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.interface_route_tables.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class InterfaceRouteTableTestFixtureGen

class LoadbalancerMemberTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.LoadbalancerMember`
    """
    def __init__(self, conn_drv, loadbalancer_member_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, loadbalancer_member_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create LoadbalancerMemberTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            loadbalancer_member_name (str): Name of loadbalancer_member
            parent_fixt (:class:`.LoadbalancerPoolTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            loadbalancer_member_properties (instance): instance of :class:`LoadbalancerMemberType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(LoadbalancerMemberTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not loadbalancer_member_name:
            self._name = 'default-loadbalancer-member'
        else:
            self._name = loadbalancer_member_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.loadbalancer_member_properties = loadbalancer_member_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`LoadbalancerMember`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.loadbalancer_member_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'loadbalancer_member', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_loadbalancer_member_properties(self.loadbalancer_member_properties or vnc_api.gen.resource_xsd.LoadbalancerMemberType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(LoadbalancerMemberTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(LoadbalancerPoolTestFixtureGen(self._conn_drv, 'default-loadbalancer-pool'))

        self._obj = vnc_api.LoadbalancerMember(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.loadbalancer_member_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.loadbalancer_member_properties = self.loadbalancer_member_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.loadbalancer_member_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.loadbalancer_member_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.loadbalancer_member_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_loadbalancer_members() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.loadbalancer_members.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class LoadbalancerMemberTestFixtureGen

class ServiceHealthCheckTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ServiceHealthCheck`
    """
    def __init__(self, conn_drv, service_health_check_name=None, parent_fixt=None, auto_prop_val=False, service_instance_ref_infos = None, tag_refs = None, service_health_check_properties=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ServiceHealthCheckTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            service_health_check_name (str): Name of service_health_check
            parent_fixt (:class:`.ProjectTestFixtureGen`): Parent fixture
            service_instance (list): list of tuple (:class:`ServiceInstance`, :class: `ServiceInterfaceTag`) type
            tag (list): list of :class:`Tag` type
            service_health_check_properties (instance): instance of :class:`ServiceHealthCheckType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ServiceHealthCheckTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not service_health_check_name:
            self._name = 'default-service-health-check'
        else:
            self._name = service_health_check_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if service_instance_ref_infos:
            for ln, ref in service_instance_ref_infos:
                self.add_service_instance (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_health_check_properties = service_health_check_properties
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_service_instances ():
            self.add_service_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_service_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`ServiceInstance` link to :class:`ServiceHealthCheck`
        Args:
            lo (:class:`ServiceInstance`): obj to link
            ref (:class:`ServiceInterfaceTag`): property of the link object
        '''
        if self._obj:
            self._obj.add_service_instance (lo, ref)
            if update_server:
                self._conn_drv.service_health_check_update (self._obj)

        if add_link:
            self.add_link('service_instance', cfixture.ConrtailLink('service_instance', 'service_health_check', 'service_instance', ['ref', 'derived'], (lo, ref)))
    # end add_service_instance_link

    def get_service_instances (self):
        return self.get_links ('service_instance')
    # end get_service_instances
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ServiceHealthCheck`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.service_health_check_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'service_health_check', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_health_check_properties(self.service_health_check_properties or vnc_api.gen.resource_xsd.ServiceHealthCheckType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ServiceHealthCheckTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(ProjectTestFixtureGen(self._conn_drv, 'default-project'))

        self._obj = vnc_api.ServiceHealthCheck(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.service_health_check_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_health_check_properties = self.service_health_check_properties
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.service_health_check_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.service_health_check_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.service_health_check_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_service_health_checks() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.service_health_checks.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ServiceHealthCheckTestFixtureGen

class AlarmTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.Alarm`
    """
    def __init__(self, conn_drv, alarm_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, uve_keys=None, alarm_severity=None, alarm_rules=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AlarmTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            alarm_name (str): Name of alarm
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            uve_keys (instance): instance of :class:`UveKeysType`
            alarm_severity (instance): instance of :class:`xsd:integer`
            alarm_rules (instance): instance of :class:`AlarmOrList`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AlarmTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not alarm_name:
            self._name = 'default-alarm'
        else:
            self._name = alarm_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.uve_keys = uve_keys
        self.alarm_severity = alarm_severity
        self.alarm_rules = alarm_rules
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`Alarm`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.alarm_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'alarm', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_uve_keys(self.uve_keys or vnc_api.gen.resource_xsd.UveKeysType.populate())
        self._obj.set_alarm_severity(self.alarm_severity or GeneratedsSuper.populate_integer("alarm_severity"))
        self._obj.set_alarm_rules(self.alarm_rules or vnc_api.gen.resource_xsd.AlarmOrList.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AlarmTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("['global-system-config', 'project']")

        self._obj = vnc_api.Alarm(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.alarm_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.uve_keys = self.uve_keys
                self._obj.alarm_severity = self.alarm_severity
                self._obj.alarm_rules = self.alarm_rules
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.alarm_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.alarm_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.alarm_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_alarms() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.alarms.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AlarmTestFixtureGen

class ApiAccessListTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.ApiAccessList`
    """
    def __init__(self, conn_drv, api_access_list_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, api_access_list_entries=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create ApiAccessListTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            api_access_list_name (str): Name of api_access_list
            parent_fixt (:class:`.DomainTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            api_access_list_entries (instance): instance of :class:`RbacRuleEntriesType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(ApiAccessListTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not api_access_list_name:
            self._name = 'default-api-access-list'
        else:
            self._name = api_access_list_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.api_access_list_entries = api_access_list_entries
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`ApiAccessList`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.api_access_list_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'api_access_list', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_api_access_list_entries(self.api_access_list_entries or vnc_api.gen.resource_xsd.RbacRuleEntriesType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(ApiAccessListTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            raise AmbiguousParentError("[u'domain', 'project', 'global-system-config']")

        self._obj = vnc_api.ApiAccessList(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.api_access_list_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.api_access_list_entries = self.api_access_list_entries
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.api_access_list_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.api_access_list_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.api_access_list_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_api_access_lists() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.api_access_lists.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class ApiAccessListTestFixtureGen

class RoutingInstanceTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.RoutingInstance`
    """
    def __init__(self, conn_drv, routing_instance_name=None, parent_fixt=None, auto_prop_val=False, routing_instance_ref_infos = None, route_target_ref_infos = None, tag_refs = None, service_chain_information=None, ipv6_service_chain_information=None, evpn_service_chain_information=None, evpn_ipv6_service_chain_information=None, routing_instance_is_default=None, routing_instance_has_pnf=None, static_route_entries=None, routing_instance_fabric_snat=None, default_ce_protocol=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create RoutingInstanceTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            routing_instance_name (str): Name of routing_instance
            parent_fixt (:class:`.VirtualNetworkTestFixtureGen`): Parent fixture
            routing_instance (list): list of tuple (:class:`RoutingInstance`, :class: `ConnectionType`) type
            route_target (list): list of tuple (:class:`RouteTarget`, :class: `InstanceTargetType`) type
            tag (list): list of :class:`Tag` type
            service_chain_information (instance): instance of :class:`ServiceChainInfo`
            ipv6_service_chain_information (instance): instance of :class:`ServiceChainInfo`
            evpn_service_chain_information (instance): instance of :class:`ServiceChainInfo`
            evpn_ipv6_service_chain_information (instance): instance of :class:`ServiceChainInfo`
            routing_instance_is_default (instance): instance of :class:`xsd:boolean`
            routing_instance_has_pnf (instance): instance of :class:`xsd:boolean`
            static_route_entries (instance): instance of :class:`StaticRouteEntriesType`
            routing_instance_fabric_snat (instance): instance of :class:`xsd:boolean`
            default_ce_protocol (instance): instance of :class:`DefaultProtocolType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(RoutingInstanceTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not routing_instance_name:
            self._name = 'default-routing-instance'
        else:
            self._name = routing_instance_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if routing_instance_ref_infos:
            for ln, ref in routing_instance_ref_infos:
                self.add_routing_instance (ln, ref)
        if route_target_ref_infos:
            for ln, ref in route_target_ref_infos:
                self.add_route_target (ln, ref)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.service_chain_information = service_chain_information
        self.ipv6_service_chain_information = ipv6_service_chain_information
        self.evpn_service_chain_information = evpn_service_chain_information
        self.evpn_ipv6_service_chain_information = evpn_ipv6_service_chain_information
        self.routing_instance_is_default = routing_instance_is_default
        self.routing_instance_has_pnf = routing_instance_has_pnf
        self.static_route_entries = static_route_entries
        self.routing_instance_fabric_snat = routing_instance_fabric_snat
        self.default_ce_protocol = default_ce_protocol
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_routing_instances ():
            self.add_routing_instance (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_route_targets ():
            self.add_route_target (*ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_routing_instance (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`RoutingInstance` link to :class:`RoutingInstance`
        Args:
            lo (:class:`RoutingInstance`): obj to link
            ref (:class:`ConnectionType`): property of the link object
        '''
        if self._obj:
            self._obj.add_routing_instance (lo, ref)
            if update_server:
                self._conn_drv.routing_instance_update (self._obj)

        if add_link:
            self.add_link('routing_instance', cfixture.ConrtailLink('routing_instance', 'routing_instance', 'routing_instance', ['ref'], (lo, ref)))
    # end add_routing_instance_link

    def get_routing_instances (self):
        return self.get_links ('routing_instance')
    # end get_routing_instances
    def add_route_target (self, lo, ref, update_server = True, add_link = True):
        '''
        add :class:`RouteTarget` link to :class:`RoutingInstance`
        Args:
            lo (:class:`RouteTarget`): obj to link
            ref (:class:`InstanceTargetType`): property of the link object
        '''
        if self._obj:
            self._obj.add_route_target (lo, ref)
            if update_server:
                self._conn_drv.routing_instance_update (self._obj)

        if add_link:
            self.add_link('route_target', cfixture.ConrtailLink('route_target', 'routing_instance', 'route_target', ['ref'], (lo, ref)))
    # end add_route_target_link

    def get_route_targets (self):
        return self.get_links ('route_target')
    # end get_route_targets
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`RoutingInstance`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.routing_instance_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'routing_instance', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_service_chain_information(self.service_chain_information or vnc_api.gen.resource_xsd.ServiceChainInfo.populate())
        self._obj.set_ipv6_service_chain_information(self.ipv6_service_chain_information or vnc_api.gen.resource_xsd.ServiceChainInfo.populate())
        self._obj.set_evpn_service_chain_information(self.evpn_service_chain_information or vnc_api.gen.resource_xsd.ServiceChainInfo.populate())
        self._obj.set_evpn_ipv6_service_chain_information(self.evpn_ipv6_service_chain_information or vnc_api.gen.resource_xsd.ServiceChainInfo.populate())
        self._obj.set_routing_instance_is_default(self.routing_instance_is_default or GeneratedsSuper.populate_boolean("routing_instance_is_default"))
        self._obj.set_routing_instance_has_pnf(self.routing_instance_has_pnf or GeneratedsSuper.populate_boolean("routing_instance_has_pnf"))
        self._obj.set_static_route_entries(self.static_route_entries or vnc_api.gen.resource_xsd.StaticRouteEntriesType.populate())
        self._obj.set_routing_instance_fabric_snat(self.routing_instance_fabric_snat or GeneratedsSuper.populate_boolean("routing_instance_fabric_snat"))
        self._obj.set_default_ce_protocol(self.default_ce_protocol or vnc_api.gen.resource_xsd.DefaultProtocolType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(RoutingInstanceTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(VirtualNetworkTestFixtureGen(self._conn_drv, 'default-virtual-network'))

        self._obj = vnc_api.RoutingInstance(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.routing_instance_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.service_chain_information = self.service_chain_information
                self._obj.ipv6_service_chain_information = self.ipv6_service_chain_information
                self._obj.evpn_service_chain_information = self.evpn_service_chain_information
                self._obj.evpn_ipv6_service_chain_information = self.evpn_ipv6_service_chain_information
                self._obj.routing_instance_is_default = self.routing_instance_is_default
                self._obj.routing_instance_has_pnf = self.routing_instance_has_pnf
                self._obj.static_route_entries = self.static_route_entries
                self._obj.routing_instance_fabric_snat = self.routing_instance_fabric_snat
                self._obj.default_ce_protocol = self.default_ce_protocol
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.routing_instance_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.routing_instance_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.routing_instance_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_routing_instances() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.routing_instances.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class RoutingInstanceTestFixtureGen

class AliasIpPoolTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.AliasIpPool`
    """
    def __init__(self, conn_drv, alias_ip_pool_name=None, parent_fixt=None, auto_prop_val=False, tag_refs = None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create AliasIpPoolTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            alias_ip_pool_name (str): Name of alias_ip_pool
            parent_fixt (:class:`.VirtualNetworkTestFixtureGen`): Parent fixture
            tag (list): list of :class:`Tag` type
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(AliasIpPoolTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not alias_ip_pool_name:
            self._name = 'default-alias-ip-pool'
        else:
            self._name = alias_ip_pool_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`AliasIpPool`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.alias_ip_pool_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'alias_ip_pool', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(AliasIpPoolTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(VirtualNetworkTestFixtureGen(self._conn_drv, 'default-virtual-network'))

        self._obj = vnc_api.AliasIpPool(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.alias_ip_pool_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.alias_ip_pool_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.alias_ip_pool_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.alias_ip_pool_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_alias_ip_pools() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.alias_ip_pools.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class AliasIpPoolTestFixtureGen

class DataCenterInterconnectTestFixtureGen(cfixture.ContrailFixture):
    """
    Fixture for :class:`.DataCenterInterconnect`
    """
    def __init__(self, conn_drv, data_center_interconnect_name=None, parent_fixt=None, auto_prop_val=False, logical_router_refs = None, virtual_network_refs = None, routing_policy_refs = None, tag_refs = None, data_center_interconnect_bgp_hold_time=None, data_center_interconnect_mode=None, data_center_interconnect_bgp_address_families=None, data_center_interconnect_configured_route_target_list=None, data_center_interconnect_type=None, destination_physical_router_list=None, id_perms=None, perms2=None, annotations=None, display_name=None):
        '''
        Create DataCenterInterconnectTestFixtureGen object
        
        constructor

        Args:
            conn_drv (:class:`ConnectionDriver`): connection driver (eg. :class:`vnc_api.vnc_api.VncApi`, :class:`novaclient.client.Client`, etc)

        Kwargs:
            data_center_interconnect_name (str): Name of data_center_interconnect
            parent_fixt (:class:`.GlobalSystemConfigTestFixtureGen`): Parent fixture
            logical_router (list): list of :class:`LogicalRouter` type
            virtual_network (list): list of :class:`VirtualNetwork` type
            routing_policy (list): list of :class:`RoutingPolicy` type
            tag (list): list of :class:`Tag` type
            data_center_interconnect_bgp_hold_time (instance): instance of :class:`xsd:integer`
            data_center_interconnect_mode (instance): instance of :class:`xsd:string`
            data_center_interconnect_bgp_address_families (instance): instance of :class:`AddressFamilies`
            data_center_interconnect_configured_route_target_list (instance): instance of :class:`RouteTargetList`
            data_center_interconnect_type (instance): instance of :class:`xsd:string`
            destination_physical_router_list (instance): instance of :class:`LogicalRouterPRListType`
            id_perms (instance): instance of :class:`IdPermsType`
            perms2 (instance): instance of :class:`PermType2`
            annotations (instance): instance of :class:`KeyValuePairs`
            display_name (instance): instance of :class:`xsd:string`

        '''
        super(DataCenterInterconnectTestFixtureGen, self).__init__()
        self._conn_drv = conn_drv
        if not data_center_interconnect_name:
            self._name = 'default-data-center-interconnect'
        else:
            self._name = data_center_interconnect_name
        self._obj = None
        self._parent_fixt = parent_fixt
        self._auto_prop_val = auto_prop_val
        if logical_router_refs:
            for ln in logical_router_refs:
                self.add_logical_router (ln)
        if virtual_network_refs:
            for ln in virtual_network_refs:
                self.add_virtual_network (ln)
        if routing_policy_refs:
            for ln in routing_policy_refs:
                self.add_routing_policy (ln)
        if tag_refs:
            for ln in tag_refs:
                self.add_tag (ln)
        self.data_center_interconnect_bgp_hold_time = data_center_interconnect_bgp_hold_time
        self.data_center_interconnect_mode = data_center_interconnect_mode
        self.data_center_interconnect_bgp_address_families = data_center_interconnect_bgp_address_families
        self.data_center_interconnect_configured_route_target_list = data_center_interconnect_configured_route_target_list
        self.data_center_interconnect_type = data_center_interconnect_type
        self.destination_physical_router_list = destination_physical_router_list
        self.id_perms = id_perms
        self.perms2 = perms2
        self.annotations = annotations
        self.display_name = display_name
    # end __init__

    def _update_links (self, update_server):
        for ln in self.get_logical_routers ():
            self.add_logical_router (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_virtual_networks ():
            self.add_virtual_network (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_routing_policys ():
            self.add_routing_policy (ln.fixture (), update_server = update_server, add_link = False)
        for ln in self.get_tags ():
            self.add_tag (ln.fixture (), update_server = update_server, add_link = False)
        return None
    # end _update_links

    def add_logical_router (self, lo, update_server = True, add_link = True):
        '''
        add :class:`LogicalRouter` link to :class:`DataCenterInterconnect`
        Args:
            lo (:class:`LogicalRouter`): obj to link
        '''
        if self._obj:
            self._obj.add_logical_router (lo)
            if update_server:
                self._conn_drv.data_center_interconnect_update (self._obj)

        if add_link:
            self.add_link('logical_router', cfixture.ConrtailLink('logical_router', 'data_center_interconnect', 'logical_router', ['ref'], lo))
    # end add_logical_router_link

    def get_logical_routers (self):
        return self.get_links ('logical_router')
    # end get_logical_routers
    def add_virtual_network (self, lo, update_server = True, add_link = True):
        '''
        add :class:`VirtualNetwork` link to :class:`DataCenterInterconnect`
        Args:
            lo (:class:`VirtualNetwork`): obj to link
        '''
        if self._obj:
            self._obj.add_virtual_network (lo)
            if update_server:
                self._conn_drv.data_center_interconnect_update (self._obj)

        if add_link:
            self.add_link('virtual_network', cfixture.ConrtailLink('virtual_network', 'data_center_interconnect', 'virtual_network', ['ref'], lo))
    # end add_virtual_network_link

    def get_virtual_networks (self):
        return self.get_links ('virtual_network')
    # end get_virtual_networks
    def add_routing_policy (self, lo, update_server = True, add_link = True):
        '''
        add :class:`RoutingPolicy` link to :class:`DataCenterInterconnect`
        Args:
            lo (:class:`RoutingPolicy`): obj to link
        '''
        if self._obj:
            self._obj.add_routing_policy (lo)
            if update_server:
                self._conn_drv.data_center_interconnect_update (self._obj)

        if add_link:
            self.add_link('routing_policy', cfixture.ConrtailLink('routing_policy', 'data_center_interconnect', 'routing_policy', ['ref'], lo))
    # end add_routing_policy_link

    def get_routing_policys (self):
        return self.get_links ('routing_policy')
    # end get_routing_policys
    def add_tag (self, lo, update_server = True, add_link = True):
        '''
        add :class:`Tag` link to :class:`DataCenterInterconnect`
        Args:
            lo (:class:`Tag`): obj to link
        '''
        if self._obj:
            self._obj.add_tag (lo)
            if update_server:
                self._conn_drv.data_center_interconnect_update (self._obj)

        if add_link:
            self.add_link('tag', cfixture.ConrtailLink('tag', 'data_center_interconnect', 'tag', ['ref'], lo))
    # end add_tag_link

    def get_tags (self):
        return self.get_links ('tag')
    # end get_tags

    def populate (self):
        self._obj.set_data_center_interconnect_bgp_hold_time(self.data_center_interconnect_bgp_hold_time or GeneratedsSuper.populate_integer("data_center_interconnect_bgp_hold_time"))
        self._obj.set_data_center_interconnect_mode(self.data_center_interconnect_mode or GeneratedsSuper.populate_string("data_center_interconnect_mode"))
        self._obj.set_data_center_interconnect_bgp_address_families(self.data_center_interconnect_bgp_address_families or vnc_api.gen.resource_xsd.AddressFamilies.populate())
        self._obj.set_data_center_interconnect_configured_route_target_list(self.data_center_interconnect_configured_route_target_list or vnc_api.gen.resource_xsd.RouteTargetList.populate())
        self._obj.set_data_center_interconnect_type(self.data_center_interconnect_type or GeneratedsSuper.populate_string("data_center_interconnect_type"))
        self._obj.set_destination_physical_router_list(self.destination_physical_router_list or vnc_api.gen.resource_xsd.LogicalRouterPRListType.populate())
        self._obj.set_id_perms(self.id_perms or vnc_api.gen.resource_xsd.IdPermsType.populate())
        self._obj.set_perms2(self.perms2 or vnc_api.gen.resource_xsd.PermType2.populate())
        self._obj.set_annotations(self.annotations or vnc_api.gen.resource_xsd.KeyValuePairs.populate())
        self._obj.set_display_name(self.display_name or GeneratedsSuper.populate_string("display_name"))
    # end populate

    def setUp(self):
        super(DataCenterInterconnectTestFixtureGen, self).setUp()
        if not self._parent_fixt:
            self._parent_fixt = self.useFixture(GlobalSystemConfigTestFixtureGen(self._conn_drv, 'default-global-system-config'))

        self._obj = vnc_api.DataCenterInterconnect(self._name, self._parent_fixt.getObj ())
        try:
            self._obj = self._conn_drv.data_center_interconnect_read (fq_name=self._obj.get_fq_name())
            self._update_links (update_server=True)
        except NoIdError:
            self._update_links (update_server=False)
            if self._auto_prop_val:
                self.populate ()
            else:
                self._obj.data_center_interconnect_bgp_hold_time = self.data_center_interconnect_bgp_hold_time
                self._obj.data_center_interconnect_mode = self.data_center_interconnect_mode
                self._obj.data_center_interconnect_bgp_address_families = self.data_center_interconnect_bgp_address_families
                self._obj.data_center_interconnect_configured_route_target_list = self.data_center_interconnect_configured_route_target_list
                self._obj.data_center_interconnect_type = self.data_center_interconnect_type
                self._obj.destination_physical_router_list = self.destination_physical_router_list
                self._obj.id_perms = self.id_perms
                self._obj.perms2 = self.perms2
                self._obj.annotations = self.annotations
                self._obj.display_name = self.display_name
            self._conn_drv.data_center_interconnect_create(self._obj)
            # read back for server allocated values
            self._obj = self._conn_drv.data_center_interconnect_read(id = self._obj.uuid)
    # end setUp

    def cleanUp(self):
        try:
            self._conn_drv.data_center_interconnect_delete(id = self._obj.uuid)
        except RefsExistError:
            return
        parent_fixt = getattr(self, '_parent_fixt', None)
        if parent_fixt:
            # non config-root child
            parent_obj = self._parent_fixt.getObj()
            # remove child from parent obj
            for child_obj in parent_obj.get_data_center_interconnects() or []:
                if type(child_obj) == dict:
                    child_uuid = child_obj['uuid']
                else:
                    child_uuid = child_obj.uuid
                if child_uuid == self._obj.uuid:
                    parent_obj.data_center_interconnects.remove(child_obj)
                    break

    # end cleanUp

    def getObj(self):
        return self._obj
    # end getObj

# end class DataCenterInterconnectTestFixtureGen

