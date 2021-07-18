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

    def verify_fabric_assisted_replication(self):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        bms_nodes = self.get_bms_nodes()
        bms_fixtures = list()
        vn1 = self.create_vn()
        kwargs = {'rb_role': 'erb_ucast_gw'} if self.erb else {}
        for bms in self.get_bms_nodes(**kwargs):
            bms_fixtures.append(self.create_bms(bms_name=bms,vn_fixture=vn1, vlan_id=10, static_ip=True))
        self.bms1 = bms_fixtures[0]
        bms2 = bms_fixtures[1]
        pid = self.bms1.send_broadcast_traffic()
        time.sleep(30)
        self.prouter_1 = self.get_associated_prouters(self.bms1.name)[0]
        self.prouter_2 = self.get_associated_prouters(bms2.name)[0]
        assert self.prouter_1.validate_AR_role()
        self.spines1= []
        self.leafs1 = []
        for spine in self.spines:
            self.spines1.append(str(spine.tunnel_ip))

        for leaf in self.leafs:
            self.leafs1.append(str(leaf.tunnel_ip))

        for spine in self.spines:
            if spine.is_spine_replicator(prouter_ip = str(self.prouter_1.tunnel_ip)):
                assert spine.validate_vtep_interfaces_output_packets(self.spines1, self.leafs1)
            else:
                assert spine.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1)

        assert self.prouter_2.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1)
        self.bms1.stop_broadcast_traffic(pid)

    def ar_func_check(self, updown):
        pid = self.bms1.send_broadcast_traffic()
        time.sleep(30)
        result = True
        if updown == 0:
            result = result and not(self.prouter_1.validate_AR_role())
        else:
            result = result and self.prouter_1.validate_AR_role()
        for spine in self.spines:
            if spine.is_spine_replicator(prouter_ip = str(self.prouter_1.tunnel_ip)):
                if updown == 0:
                    result = result and not(spine.validate_vtep_interfaces_output_packets(self.spines1, self.leafs1))
                else:
                    result = result and spine.validate_vtep_interfaces_output_packets(self.spines1, self.leafs1)
            else:
                if updown == 0:
                    result = result and not(spine.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1))
                else:
                    result = result and spine.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1)

        if updown == 0:
            result = result and not(self.prouter_2.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1))
        else:
            result = result and self.prouter_2.validate_vtep_interfaces_input_packets(prouter_ip = str(self.prouter_1.tunnel_ip), spines = self.spines1)
        self.bms1.stop_broadcast_traffic(pid)
        assert result

    @preposttest_wrapper
    def test_fabric_assisted_replication(self):
        self.verify_fabric_assisted_replication()

    @preposttest_wrapper
    def test_add_delete_ar_spine(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector']
        #unconfigure AR for spine
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

    @preposttest_wrapper
    def test_add_delete_ar_leaf(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        #unconfigure AR for leaf
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

    @preposttest_wrapper
    def test_add_ar_leaf_to_spine(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Client']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Client']
        #assign ar-client to spine
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

    @preposttest_wrapper
    def test_add_ar_spine_to_leaf(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Replicator']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Replicator']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        #assign ar-replicator to leaf
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

    @preposttest_wrapper
    def test_add_ar_spine_no_leaf(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        #assign no leaf with ar-client
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

    @preposttest_wrapper
    def test_add_ar_leaf_no_spine(self):
        #lets make sure AR functionality is fine before we begin
        self.verify_fabric_assisted_replication()
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector']
        #assign no spine with ar-replicator
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        self.ar_func_check(updown=0)
        if self.erb:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    if 'erb_ucast_gw' in (device_dict.get('rb_roles') or []):
                        self.rb_roles[device] = ['ERB-UCAST-Gateway', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['lean', 'Route-Reflector', 'AR-Replicator']
        else:
            for device, device_dict in self.inputs.physical_routers_data.items():
                if device_dict['role'] == 'leaf':
                    self.rb_roles[device] = ['CRB-Access', 'AR-Client']
                elif device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['CRB-Gateway', 'Route-Reflector', 'AR-Replicator']
        self.assign_roles(self.fabric, self.devices, rb_roles=self.rb_roles)
        #lets make sure AR functionality is restored
        self.ar_func_check(updown=1)

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

