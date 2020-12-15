
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

import fixtures
import testtools

from vnc_api.gen.resource_test import *

class VncApiTestGen(testtools.TestCase, fixtures.TestWithFixtures):
    def test_service_endpoint_crud(self):
        self.useFixture(ServiceEndpointTestFixtureGen(self._vnc_lib))
    # end test_service_endpoint_crud

    def test_instance_ip_crud(self):
        self.useFixture(InstanceIpTestFixtureGen(self._vnc_lib))
    # end test_instance_ip_crud

    def test_service_appliance_set_crud(self):
        self.useFixture(ServiceApplianceSetTestFixtureGen(self._vnc_lib))
    # end test_service_appliance_set_crud

    def test_route_target_crud(self):
        self.useFixture(RouteTargetTestFixtureGen(self._vnc_lib))
    # end test_route_target_crud

    def test_loadbalancer_listener_crud(self):
        self.useFixture(LoadbalancerListenerTestFixtureGen(self._vnc_lib))
    # end test_loadbalancer_listener_crud

    def test_floating_ip_pool_crud(self):
        self.useFixture(FloatingIpPoolTestFixtureGen(self._vnc_lib))
    # end test_floating_ip_pool_crud

    def test_physical_router_crud(self):
        self.useFixture(PhysicalRouterTestFixtureGen(self._vnc_lib))
    # end test_physical_router_crud

    def test_service_template_crud(self):
        self.useFixture(ServiceTemplateTestFixtureGen(self._vnc_lib))
    # end test_service_template_crud

    def test_hardware_inventory_crud(self):
        self.useFixture(HardwareInventoryTestFixtureGen(self._vnc_lib))
    # end test_hardware_inventory_crud

    def test_firewall_policy_crud(self):
        self.useFixture(FirewallPolicyTestFixtureGen(self._vnc_lib))
    # end test_firewall_policy_crud

    def test_route_table_crud(self):
        self.useFixture(RouteTableTestFixtureGen(self._vnc_lib))
    # end test_route_table_crud

    def test_provider_attachment_crud(self):
        self.useFixture(ProviderAttachmentTestFixtureGen(self._vnc_lib))
    # end test_provider_attachment_crud

    def test_overlay_role_crud(self):
        self.useFixture(OverlayRoleTestFixtureGen(self._vnc_lib))
    # end test_overlay_role_crud

    def test_multicast_policy_crud(self):
        self.useFixture(MulticastPolicyTestFixtureGen(self._vnc_lib))
    # end test_multicast_policy_crud

    def test_network_device_config_crud(self):
        self.useFixture(NetworkDeviceConfigTestFixtureGen(self._vnc_lib))
    # end test_network_device_config_crud

    def test_virtual_DNS_record_crud(self):
        self.useFixture(VirtualDnsRecordTestFixtureGen(self._vnc_lib))
    # end test_virtual_DNS_record_crud

    def test_control_node_zone_crud(self):
        self.useFixture(ControlNodeZoneTestFixtureGen(self._vnc_lib))
    # end test_control_node_zone_crud

    def test_dsa_rule_crud(self):
        self.useFixture(DsaRuleTestFixtureGen(self._vnc_lib))
    # end test_dsa_rule_crud

    def test_structured_syslog_config_crud(self):
        self.useFixture(StructuredSyslogConfigTestFixtureGen(self._vnc_lib))
    # end test_structured_syslog_config_crud

    def test_discovery_service_assignment_crud(self):
        self.useFixture(DiscoveryServiceAssignmentTestFixtureGen(self._vnc_lib))
    # end test_discovery_service_assignment_crud

    def test_logical_interface_crud(self):
        self.useFixture(LogicalInterfaceTestFixtureGen(self._vnc_lib))
    # end test_logical_interface_crud

    def test_flow_node_crud(self):
        self.useFixture(FlowNodeTestFixtureGen(self._vnc_lib))
    # end test_flow_node_crud

    def test_port_group_crud(self):
        self.useFixture(PortGroupTestFixtureGen(self._vnc_lib))
    # end test_port_group_crud

    def test_route_aggregate_crud(self):
        self.useFixture(RouteAggregateTestFixtureGen(self._vnc_lib))
    # end test_route_aggregate_crud

    def test_logical_router_crud(self):
        self.useFixture(LogicalRouterTestFixtureGen(self._vnc_lib))
    # end test_logical_router_crud

    def test_domain_crud(self):
        self.useFixture(DomainTestFixtureGen(self._vnc_lib))
    # end test_domain_crud

    def test_structured_syslog_hostname_record_crud(self):
        self.useFixture(StructuredSyslogHostnameRecordTestFixtureGen(self._vnc_lib))
    # end test_structured_syslog_hostname_record_crud

    def test_service_instance_crud(self):
        self.useFixture(ServiceInstanceTestFixtureGen(self._vnc_lib))
    # end test_service_instance_crud

    def test_node_profile_crud(self):
        self.useFixture(NodeProfileTestFixtureGen(self._vnc_lib))
    # end test_node_profile_crud

    def test_bridge_domain_crud(self):
        self.useFixture(BridgeDomainTestFixtureGen(self._vnc_lib))
    # end test_bridge_domain_crud

    def test_alias_ip_crud(self):
        self.useFixture(AliasIpTestFixtureGen(self._vnc_lib))
    # end test_alias_ip_crud

    def test_webui_node_crud(self):
        self.useFixture(WebuiNodeTestFixtureGen(self._vnc_lib))
    # end test_webui_node_crud

    def test_port_crud(self):
        self.useFixture(PortTestFixtureGen(self._vnc_lib))
    # end test_port_crud

    def test_bgp_as_a_service_crud(self):
        self.useFixture(BgpAsAServiceTestFixtureGen(self._vnc_lib))
    # end test_bgp_as_a_service_crud

    def test_subnet_crud(self):
        self.useFixture(SubnetTestFixtureGen(self._vnc_lib))
    # end test_subnet_crud

    def test_global_system_config_crud(self):
        self.useFixture(GlobalSystemConfigTestFixtureGen(self._vnc_lib))
    # end test_global_system_config_crud

    def test_sub_cluster_crud(self):
        self.useFixture(SubClusterTestFixtureGen(self._vnc_lib))
    # end test_sub_cluster_crud

    def test_forwarding_class_crud(self):
        self.useFixture(ForwardingClassTestFixtureGen(self._vnc_lib))
    # end test_forwarding_class_crud

    def test_service_group_crud(self):
        self.useFixture(ServiceGroupTestFixtureGen(self._vnc_lib))
    # end test_service_group_crud

    def test_global_analytics_config_crud(self):
        self.useFixture(GlobalAnalyticsConfigTestFixtureGen(self._vnc_lib))
    # end test_global_analytics_config_crud

    def test_address_group_crud(self):
        self.useFixture(AddressGroupTestFixtureGen(self._vnc_lib))
    # end test_address_group_crud

    def test_application_policy_set_crud(self):
        self.useFixture(ApplicationPolicySetTestFixtureGen(self._vnc_lib))
    # end test_application_policy_set_crud

    def test_virtual_ip_crud(self):
        self.useFixture(VirtualIpTestFixtureGen(self._vnc_lib))
    # end test_virtual_ip_crud

    def test_intent_map_crud(self):
        self.useFixture(IntentMapTestFixtureGen(self._vnc_lib))
    # end test_intent_map_crud

    def test_port_tuple_crud(self):
        self.useFixture(PortTupleTestFixtureGen(self._vnc_lib))
    # end test_port_tuple_crud

    def test_analytics_alarm_node_crud(self):
        self.useFixture(AnalyticsAlarmNodeTestFixtureGen(self._vnc_lib))
    # end test_analytics_alarm_node_crud

    def test_qos_queue_crud(self):
        self.useFixture(QosQueueTestFixtureGen(self._vnc_lib))
    # end test_qos_queue_crud

    def test_physical_role_crud(self):
        self.useFixture(PhysicalRoleTestFixtureGen(self._vnc_lib))
    # end test_physical_role_crud

    def test_card_crud(self):
        self.useFixture(CardTestFixtureGen(self._vnc_lib))
    # end test_card_crud

    def test_security_logging_object_crud(self):
        self.useFixture(SecurityLoggingObjectTestFixtureGen(self._vnc_lib))
    # end test_security_logging_object_crud

    def test_qos_config_crud(self):
        self.useFixture(QosConfigTestFixtureGen(self._vnc_lib))
    # end test_qos_config_crud

    def test_analytics_snmp_node_crud(self):
        self.useFixture(AnalyticsSnmpNodeTestFixtureGen(self._vnc_lib))
    # end test_analytics_snmp_node_crud

    def test_virtual_machine_interface_crud(self):
        self.useFixture(VirtualMachineInterfaceTestFixtureGen(self._vnc_lib))
    # end test_virtual_machine_interface_crud

    def test_cli_config_crud(self):
        self.useFixture(CliConfigTestFixtureGen(self._vnc_lib))
    # end test_cli_config_crud

    def test_service_object_crud(self):
        self.useFixture(ServiceObjectTestFixtureGen(self._vnc_lib))
    # end test_service_object_crud

    def test_feature_flag_crud(self):
        self.useFixture(FeatureFlagTestFixtureGen(self._vnc_lib))
    # end test_feature_flag_crud

    def test_loadbalancer_crud(self):
        self.useFixture(LoadbalancerTestFixtureGen(self._vnc_lib))
    # end test_loadbalancer_crud

    def test_peering_policy_crud(self):
        self.useFixture(PeeringPolicyTestFixtureGen(self._vnc_lib))
    # end test_peering_policy_crud

    def test_structured_syslog_application_record_crud(self):
        self.useFixture(StructuredSyslogApplicationRecordTestFixtureGen(self._vnc_lib))
    # end test_structured_syslog_application_record_crud

    def test_global_vrouter_config_crud(self):
        self.useFixture(GlobalVrouterConfigTestFixtureGen(self._vnc_lib))
    # end test_global_vrouter_config_crud

    def test_floating_ip_crud(self):
        self.useFixture(FloatingIpTestFixtureGen(self._vnc_lib))
    # end test_floating_ip_crud

    def test_link_aggregation_group_crud(self):
        self.useFixture(LinkAggregationGroupTestFixtureGen(self._vnc_lib))
    # end test_link_aggregation_group_crud

    def test_virtual_router_crud(self):
        self.useFixture(VirtualRouterTestFixtureGen(self._vnc_lib))
    # end test_virtual_router_crud

    def test_port_profile_crud(self):
        self.useFixture(PortProfileTestFixtureGen(self._vnc_lib))
    # end test_port_profile_crud

    def test_policy_management_crud(self):
        self.useFixture(PolicyManagementTestFixtureGen(self._vnc_lib))
    # end test_policy_management_crud

    def test_e2_service_provider_crud(self):
        self.useFixture(E2ServiceProviderTestFixtureGen(self._vnc_lib))
    # end test_e2_service_provider_crud

    def test_fabric_crud(self):
        self.useFixture(FabricTestFixtureGen(self._vnc_lib))
    # end test_fabric_crud

    def test_job_template_crud(self):
        self.useFixture(JobTemplateTestFixtureGen(self._vnc_lib))
    # end test_job_template_crud

    def test_routing_policy_crud(self):
        self.useFixture(RoutingPolicyTestFixtureGen(self._vnc_lib))
    # end test_routing_policy_crud

    def test_role_config_crud(self):
        self.useFixture(RoleConfigTestFixtureGen(self._vnc_lib))
    # end test_role_config_crud

    def test_tag_type_crud(self):
        self.useFixture(TagTypeTestFixtureGen(self._vnc_lib))
    # end test_tag_type_crud

    def test_structured_syslog_message_crud(self):
        self.useFixture(StructuredSyslogMessageTestFixtureGen(self._vnc_lib))
    # end test_structured_syslog_message_crud

    def test_loadbalancer_pool_crud(self):
        self.useFixture(LoadbalancerPoolTestFixtureGen(self._vnc_lib))
    # end test_loadbalancer_pool_crud

    def test_device_chassis_crud(self):
        self.useFixture(DeviceChassisTestFixtureGen(self._vnc_lib))
    # end test_device_chassis_crud

    def test_global_qos_config_crud(self):
        self.useFixture(GlobalQosConfigTestFixtureGen(self._vnc_lib))
    # end test_global_qos_config_crud

    def test_analytics_node_crud(self):
        self.useFixture(AnalyticsNodeTestFixtureGen(self._vnc_lib))
    # end test_analytics_node_crud

    def test_virtual_DNS_crud(self):
        self.useFixture(VirtualDnsTestFixtureGen(self._vnc_lib))
    # end test_virtual_DNS_crud

    def test_config_database_node_crud(self):
        self.useFixture(ConfigDatabaseNodeTestFixtureGen(self._vnc_lib))
    # end test_config_database_node_crud

    def test_config_node_crud(self):
        self.useFixture(ConfigNodeTestFixtureGen(self._vnc_lib))
    # end test_config_node_crud

    def test_device_functional_group_crud(self):
        self.useFixture(DeviceFunctionalGroupTestFixtureGen(self._vnc_lib))
    # end test_device_functional_group_crud

    def test_firewall_rule_crud(self):
        self.useFixture(FirewallRuleTestFixtureGen(self._vnc_lib))
    # end test_firewall_rule_crud

    def test_bgpvpn_crud(self):
        self.useFixture(BgpvpnTestFixtureGen(self._vnc_lib))
    # end test_bgpvpn_crud

    def test_role_definition_crud(self):
        self.useFixture(RoleDefinitionTestFixtureGen(self._vnc_lib))
    # end test_role_definition_crud

    def test_service_connection_module_crud(self):
        self.useFixture(ServiceConnectionModuleTestFixtureGen(self._vnc_lib))
    # end test_service_connection_module_crud

    def test_security_group_crud(self):
        self.useFixture(SecurityGroupTestFixtureGen(self._vnc_lib))
    # end test_security_group_crud

    def test_database_node_crud(self):
        self.useFixture(DatabaseNodeTestFixtureGen(self._vnc_lib))
    # end test_database_node_crud

    def test_loadbalancer_healthmonitor_crud(self):
        self.useFixture(LoadbalancerHealthmonitorTestFixtureGen(self._vnc_lib))
    # end test_loadbalancer_healthmonitor_crud

    def test_devicemgr_node_crud(self):
        self.useFixture(DevicemgrNodeTestFixtureGen(self._vnc_lib))
    # end test_devicemgr_node_crud

    def test_project_crud(self):
        self.useFixture(ProjectTestFixtureGen(self._vnc_lib))
    # end test_project_crud

    def test_fabric_namespace_crud(self):
        self.useFixture(FabricNamespaceTestFixtureGen(self._vnc_lib))
    # end test_fabric_namespace_crud

    def test_network_ipam_crud(self):
        self.useFixture(NetworkIpamTestFixtureGen(self._vnc_lib))
    # end test_network_ipam_crud

    def test_network_policy_crud(self):
        self.useFixture(NetworkPolicyTestFixtureGen(self._vnc_lib))
    # end test_network_policy_crud

    def test_sflow_profile_crud(self):
        self.useFixture(SflowProfileTestFixtureGen(self._vnc_lib))
    # end test_sflow_profile_crud

    def test_hardware_crud(self):
        self.useFixture(HardwareTestFixtureGen(self._vnc_lib))
    # end test_hardware_crud

    def test_tag_crud(self):
        self.useFixture(TagTestFixtureGen(self._vnc_lib))
    # end test_tag_crud

    def test_feature_config_crud(self):
        self.useFixture(FeatureConfigTestFixtureGen(self._vnc_lib))
    # end test_feature_config_crud

    def test_telemetry_profile_crud(self):
        self.useFixture(TelemetryProfileTestFixtureGen(self._vnc_lib))
    # end test_telemetry_profile_crud

    def test_bgp_router_crud(self):
        self.useFixture(BgpRouterTestFixtureGen(self._vnc_lib))
    # end test_bgp_router_crud

    def test_virtual_network_crud(self):
        self.useFixture(VirtualNetworkTestFixtureGen(self._vnc_lib))
    # end test_virtual_network_crud

    def test_virtual_port_group_crud(self):
        self.useFixture(VirtualPortGroupTestFixtureGen(self._vnc_lib))
    # end test_virtual_port_group_crud

    def test_service_appliance_crud(self):
        self.useFixture(ServiceApplianceTestFixtureGen(self._vnc_lib))
    # end test_service_appliance_crud

    def test_namespace_crud(self):
        self.useFixture(NamespaceTestFixtureGen(self._vnc_lib))
    # end test_namespace_crud

    def test_feature_crud(self):
        self.useFixture(FeatureTestFixtureGen(self._vnc_lib))
    # end test_feature_crud

    def test_storm_control_profile_crud(self):
        self.useFixture(StormControlProfileTestFixtureGen(self._vnc_lib))
    # end test_storm_control_profile_crud

    def test_device_image_crud(self):
        self.useFixture(DeviceImageTestFixtureGen(self._vnc_lib))
    # end test_device_image_crud

    def test_physical_interface_crud(self):
        self.useFixture(PhysicalInterfaceTestFixtureGen(self._vnc_lib))
    # end test_physical_interface_crud

    def test_access_control_list_crud(self):
        self.useFixture(AccessControlListTestFixtureGen(self._vnc_lib))
    # end test_access_control_list_crud

    def test_node_crud(self):
        self.useFixture(NodeTestFixtureGen(self._vnc_lib))
    # end test_node_crud

    def test_customer_attachment_crud(self):
        self.useFixture(CustomerAttachmentTestFixtureGen(self._vnc_lib))
    # end test_customer_attachment_crud

    def test_structured_syslog_sla_profile_crud(self):
        self.useFixture(StructuredSyslogSlaProfileTestFixtureGen(self._vnc_lib))
    # end test_structured_syslog_sla_profile_crud

    def test_host_based_service_crud(self):
        self.useFixture(HostBasedServiceTestFixtureGen(self._vnc_lib))
    # end test_host_based_service_crud

    def test_virtual_machine_crud(self):
        self.useFixture(VirtualMachineTestFixtureGen(self._vnc_lib))
    # end test_virtual_machine_crud

    def test_interface_route_table_crud(self):
        self.useFixture(InterfaceRouteTableTestFixtureGen(self._vnc_lib))
    # end test_interface_route_table_crud

    def test_loadbalancer_member_crud(self):
        self.useFixture(LoadbalancerMemberTestFixtureGen(self._vnc_lib))
    # end test_loadbalancer_member_crud

    def test_service_health_check_crud(self):
        self.useFixture(ServiceHealthCheckTestFixtureGen(self._vnc_lib))
    # end test_service_health_check_crud

    def test_alarm_crud(self):
        self.useFixture(AlarmTestFixtureGen(self._vnc_lib))
    # end test_alarm_crud

    def test_api_access_list_crud(self):
        self.useFixture(ApiAccessListTestFixtureGen(self._vnc_lib))
    # end test_api_access_list_crud

    def test_routing_instance_crud(self):
        self.useFixture(RoutingInstanceTestFixtureGen(self._vnc_lib))
    # end test_routing_instance_crud

    def test_alias_ip_pool_crud(self):
        self.useFixture(AliasIpPoolTestFixtureGen(self._vnc_lib))
    # end test_alias_ip_pool_crud

    def test_data_center_interconnect_crud(self):
        self.useFixture(DataCenterInterconnectTestFixtureGen(self._vnc_lib))
    # end test_data_center_interconnect_crud

# end class VncApiTestGen
