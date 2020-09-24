from __future__ import absolute_import
from builtins import str
from builtins import range
import test
import time
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

class Test_assisted_replication(BaseFabricTest):
    erb = False
    def setUp(self):
        for device, device_dict in self.inputs.physical_routers_data.items():
            if device_dict['role'] == 'leaf':
                self.rb_roles[device] = ['CRB-Access', 'AR-Client']
            elif device_dict['role'] == 'spine':
                self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        super(Test_assisted_replication, self).setUp()

    @classmethod
    def setUpClass(cls):
        super(Test_assisted_replication, cls).setUpClass()
        cls.backup_csn_nodes = cls.inputs.get_csn()
        cls.inputs.set_csn([])

    @classmethod
    def tearDownClass(cls):
        cls.inputs.set_csn(cls.backup_csn_nodes)
        super(Test_assisted_replication, cls).tearDownClass()

    @preposttest_wrapper
    def test_fabric_assisted_replication(self):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        bms_nodes = self.get_bms_nodes()
        bms_fixtures = list()
        vn1 = self.create_vn()
        kwargs = {'rb_role': 'erb_ucast_gw'} if self.erb else {}
        for bms in self.get_bms_nodes(**kwargs):
            bms_fixtures.append(self.create_bms(bms_name=bms,vn_fixture=vn1, vlan_id=10, static_ip=True))
        bms1 = bms_fixtures[0]
        bms2 = bms_fixtures[1]
        pid = bms1.send_broadcast_traffic()
        time.sleep(30)
        prouter_1 = self.get_associated_prouters(bms1.name)[0]
        prouter_2 = self.get_associated_prouters(bms2.name)[0]

        assert prouter_1.validate_AR_role()
        spines= []
        leafs = []
        for spine in self.spines:
            spines.append(str(spine.tunnel_ip))

        for leaf in self.leafs:
            leafs.append(str(leaf.tunnel_ip))

        for spine in self.spines:
            if spine.is_spine_replicator(prouter_ip = str(prouter_1.tunnel_ip)):
                assert spine.validate_vtep_interfaces_output_packets(spines, leafs)
            else:
                assert spine.validate_vtep_interfaces_input_packets(prouter_ip = str(prouter_1.tunnel_ip), spines = spines)

        assert prouter_2.validate_vtep_interfaces_input_packets(prouter_ip = str(prouter_1.tunnel_ip), spines = spines)

        bms1.stop_broadcast_traffic(pid)

class Test_assisted_replication_ERB(Test_assisted_replication):
    erb = True
    def setUp(self):
        for device, device_dict in self.inputs.physical_routers_data.items():
            if device_dict['role'] == 'leaf':
                if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                    self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
            elif device_dict['role'] == 'spine':
                self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        super(Test_assisted_replication_ERB, self).setUp()

