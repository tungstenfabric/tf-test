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

class TestFabricNTPSNMPDNS(BaseFabricTest):
    enterprise_style = False
    @preposttest_wrapper
    def test_fabric_ntp_snmp_dns_basic(self):
        self.change_role_config_params()
        assert self.check_role_config_params(), 'JUNOS config does not match the config contrail has'

