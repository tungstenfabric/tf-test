from tcutils.wrappers import preposttest_wrapper
from tcutils.util import get_random_name, get_af_type
from common.contrail_fabric.base import BaseFabricTest


class TestFabricCollapsedSpine(BaseFabricTest):
    def is_test_applicable(self):
        result, msg = super(TestFabricCollapsedSpine, self).is_test_applicable()
        if result is False:
            return False, msg
        c_spines, l2 = 0, 0
        for device_dict in list(self.inputs.physical_routers_data.values()):
            if 'collapsed-spine' in (device_dict.get('rb_roles') or []) and device_dict.get('role') == 'spine':
                c_spines += 1
            if 'l2' in (device_dict.get('role') or []):
                l2 += 1
        if c_spines < 2:
            return False, 'At least two spines with collapsed-spine rb_role are required in fabric topology'
        elif l2 < 2:
            return False, 'At least two devices with role l2 are required in fabric topology'
        return True, msg

    def setUp(self):
        for device, device_dict in list(self.inputs.physical_routers_data.items()):
            if 'collapsed-spine' in (device_dict.get('rb_roles') or []):
                if device_dict['role'] == 'spine':
                    self.rb_roles[device] = ['Collapsed-Spine', 'Route-Reflector', 'CRB-Gateway']
        super(TestFabricCollapsedSpine, self).setUp()

    def configure_fabric_for_collapsed_spine(self):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        vns = [vn1, vn2]
        vlan_ids = [10, 20]
        self.bms_name = self.get_bms_nodes(role='l2')[0]
        devices = list()
        for device in self.devices:
            if 'collapsed-spine' in self.inputs.get_prouter_rb_roles(device.name):
                devices.append(device)
        self.create_logical_router(vns, devices=devices)
        self.vmi_create(vns, vlan_ids)
        self.configure_l2_vlan_link(vns, vlan_ids)
        self.instances = []

    def vmi_create(self, vns, vlan_ids):
        i = 0
        self.l2_devices = dict()
        for device, device_dict in list(self.inputs.physical_routers_data.items()):
            if device_dict['role'] == 'spine':
                link = device_dict['links'][0]
                interface = dict()
                interface['tor'] = device_dict['name']
                interface['tor_port'] = link['from']
                l2_name = link['to']['name']
                l2_port = link['to']['port']
                self.l2_devices[l2_name] = l2_port
                port_fixutre = self.create_vmi(fabric_fixture=self.fabric, interfaces=[interface],
                                               vnid=vns[i].get_uuid(), vlan_id=vlan_ids[i], vlan_tag=vlan_ids[i])
                self.l2_devices[l2_name+'-pf'] = port_fixutre
                i += 1

    def configure_l2_vlan_link(self, vns, vlan_ids):
        i = 0
        for device, device_dict in list(self.inputs.physical_routers_data.items()):
            if device_dict['role'] == 'l2':
                name = device_dict['name']
                up_ifc = self.l2_devices.get(name)
                bms_dict = self.inputs.bms_data[self.bms_name]
                down_ifc, bms_ip = '', ''
                for intfc in bms_dict['interfaces']:
                    if intfc['tor'] == name:
                        down_ifc = intfc['tor_port']
                mgmt_ip = device_dict['mgmt_ip']
                ssh_username = device_dict['ssh_username']
                ssh_password = device_dict['ssh_password']
                port_fixture = self.l2_devices.get(name+'-pf')
                for address in port_fixture.get_ip_addresses():
                    if get_af_type(address) == 'v4':
                        bms_ip = address
                self.configure_l2_vlan(pi_name=up_ifc, vlan_name=get_random_name('cspine-vlan'), vlan_id=vlan_ids[i],
                                       mgmt_ip=mgmt_ip, username=ssh_username, password=ssh_password)
                self.configure_l2_vlan(pi_name=down_ifc, vlan_name=get_random_name('cspine-vlan'), vlan_id=vlan_ids[i],
                                       mgmt_ip=mgmt_ip, username=ssh_username, password=ssh_password)
                bms = self.create_bms(bms_name=self.bms_name, vn_fixture=vns[i], tor_port_vlan_tag=vlan_ids[i],
                                      fabric_fixture=self.fabric, vmi_create=False, bms_ip=bms_ip)
                self.instances.append(bms)
                i += 1

    @preposttest_wrapper
    def test_fabric_collpsed_spine_basic(self):
        self.configure_fabric_for_collapsed_spine()
        self.do_ping_mesh(self.instances)

    @preposttest_wrapper
    def test_fabric_dm_restart(self):
        self.configure_fabric_for_collapsed_spine()
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'device-manager')
        self.do_ping_mesh(self.instances)

    @preposttest_wrapper
    def test_fabric_api_restart(self):
        self.configure_fabric_for_collapsed_spine()
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'api-server')
        self.do_ping_mesh(self.instances)
