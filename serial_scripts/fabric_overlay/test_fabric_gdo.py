from builtins import str
from builtins import range
import test
import uuid
import copy
import random
from netaddr import *
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because, get_random_cidr, get_random_name
from common.contrail_fabric.base import BaseFabricTest
from common.base import GenericTestBase
from netaddr import IPNetwork, IPAddress
from vnc_api.vnc_api import *

class TestFabricGDO(BaseFabricTest):
    enterprise_style = False
    @preposttest_wrapper
    def test_fabric_gdo_hardware(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis hardware")

    @preposttest_wrapper
    def test_fabric_gdo_hardware_detail(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis hardware detail")

    @preposttest_wrapper
    def test_fabric_gdo_hardware_clei_models(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis hardware clei-models")

    @preposttest_wrapper
    def test_fabric_gdo_alarms(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis alarms")

    @preposttest_wrapper
    def test_fabric_gdo_env(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis environment")

    @preposttest_wrapper
    def test_fabric_gdo_cb(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis environment cb")

    @preposttest_wrapper
    def test_fabric_gdo_env_fpc(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis environment fpc")

    @preposttest_wrapper
    def test_fabric_gdo_env_pem(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis environment pem")

    @preposttest_wrapper
    def test_fabric_gdo_env_re(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis environment routing-engine")

    @preposttest_wrapper
    def test_fabric_gdo_env_fan(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis fan")

    @preposttest_wrapper
    def test_fabric_gdo_env_firmware(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis firmware")

    @preposttest_wrapper
    def test_fabric_gdo_env_power(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis power")

    @preposttest_wrapper
    def test_fabric_gdo_env_clei(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis hardware clei-models")

    @preposttest_wrapper
    def test_fabric_gdo_env_temp(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis temperature-thresholds")

    @preposttest_wrapper
    def test_fabric_gdo_mac_addr(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_chassis_info_template', 'chassis_detail', gdo_type="chassis mac-addresses")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_1(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "all")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_2(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "system")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_3(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_4(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "chassis")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_5(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "services")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_6(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "snmp")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_7(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "forwarding-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_8(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "event-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_9(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "policy-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_10(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "class-of-service")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_11(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "firewall")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_12(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "protocols")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_13(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "routing-instances")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_14(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "routing-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_15(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "switch-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_16(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "current", payload2= 'config_filter', value2= "vlans")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_17(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "all")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_18(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "system")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_19(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_20(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "chassis")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_21(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "services")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_22(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "snmp")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_23(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "forwarding-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_24(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "event-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_25(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "policy-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_26(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "class-of-service")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_27(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "firewall")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_28(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "protocols")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_29(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "routing-instances")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_30(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "routing-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_31(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "switch-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_32(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 1", payload2= 'config_filter', value2= "vlans")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_33(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "all")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_34(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "system")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_35(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_36(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "chassis")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_37(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "services")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_38(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "snmp")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_39(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "forwarding-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_40(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "event-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_41(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "policy-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_42(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "class-of-service")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_43(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "firewall")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_44(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "protocols")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_45(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "routing-instances")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_46(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "routing-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_47(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "switch-options")

    @preposttest_wrapper
    def test_fabric_gdo_config_type_48(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_config_template', payload1 = 'config_type', value1= "rollback 2", payload2= 'config_filter', value2= "vlans")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_1(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "physical", payload2= 'sub_operation', value2= "Show runtime interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_2(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "physical", payload2= 'sub_operation', value2= "Show configured interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_3(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "physical", payload2= 'sub_operation', value2= "Show interfaces by names")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_4(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "logical", payload2= 'sub_operation', value2= "Show runtime interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_5(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "logical", payload2= 'sub_operation', value2= "Show configured interfaces")

    @preposttest_wrapper
    def test_fabric_gdo_interface_type_6(self):
        self.get_chassis_gdo_info_multiple(self.inputs.fabrics[0], 'show_interface_details_template', payload1 = 'interface_type', value1= "logical", payload2= 'sub_operation', value2= "Show interfaces by names")

    @preposttest_wrapper
    def test_fabric_ops_1(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show chassis info")

    @preposttest_wrapper
    def test_fabric_ops_2(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show route info")

    @preposttest_wrapper
    def test_fabric_ops_3(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show bgp info")

    @preposttest_wrapper
    def test_fabric_ops_4(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show evpn info")

    @preposttest_wrapper
    def test_fabric_ops_5(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show lldp info")

    @preposttest_wrapper
    def test_fabric_ops_6(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show lacp info")

    @preposttest_wrapper
    def test_fabric_ops_7(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], 'show_ops_info_template', 'sub_operation', gdo_type="show vlan info")
