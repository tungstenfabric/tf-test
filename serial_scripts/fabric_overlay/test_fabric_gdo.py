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
        self.get_chassis_gdo_info(self.inputs.fabrics[0])

    @preposttest_wrapper
    def test_fabric_gdo_alarms(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis alarms")

    @preposttest_wrapper
    def test_fabric_gdo_env(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis environment")

    @preposttest_wrapper
    def test_fabric_gdo_cb(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis environment cb")

    @preposttest_wrapper
    def test_fabric_gdo_env_fpc(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis environment fpc")

    @preposttest_wrapper
    def test_fabric_gdo_env_pem(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis environment pem")

    @preposttest_wrapper
    def test_fabric_gdo_env_re(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis environment routing-engine")

    @preposttest_wrapper
    def test_fabric_gdo_env_fan(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis fan")

    @preposttest_wrapper
    def test_fabric_gdo_env_firmware(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis chassis firmware")

    @preposttest_wrapper
    def test_fabric_gdo_env_power(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis power")

    @preposttest_wrapper
    def test_fabric_gdo_env_clei(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis hardware clei-models")

    @preposttest_wrapper
    def test_fabric_gdo_env_temp(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis chassis temperature-thresholds")

    @preposttest_wrapper
    def test_fabric_gdo_mac_addr(self):
        self.get_chassis_gdo_info(self.inputs.fabrics[0], gdo_type="chassis mac-addresses")
