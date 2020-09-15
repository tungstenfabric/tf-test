from tcutils.wrappers import preposttest_wrapper
from tcutils.util import get_random_name, get_af_type
from common.contrail_fabric.base import BaseFabricTest


class TestFabricCollapsedSpine(BaseFabricTest):
    def is_test_applicable(self):
        result, msg = super(TestFabricCollapsedSpine, self).is_test_applicable()
        if result is False:
            return False, msg
        self.c_spines, self.l2_devices = [], []
        for device_dict in list(self.inputs.physical_routers_data.values()):
            if 'collapsed-spine' in (device_dict.get('rb_roles', [])) and device_dict.get('role', '') == 'spine':
                self.c_spines.append(device_dict)
                self.rb_roles[device_dict['name']] = ['Collapsed-Spine', 'Route-Reflector']
            if 'l2' == (device_dict.get('role', '')):
                self.l2_devices.append(device_dict)
        if len(self.c_spines) < 2:
            return False, 'At least two spines with collapsed-spine rb_role are required in fabric topology'
        elif len(self.l2_devices) < 2:
            return False, 'At least two devices with role l2 are required in fabric topology'
        return True, msg

    def setUp(self):
        super(TestFabricCollapsedSpine, self).setUp()

    def configure_fabric_for_collapsed_spine(self, intravn=False):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        self.instances, self.vns, self.lr_devices = [], [], []
        index = 0
        vlanid = index + 10
        for device_dict in self.c_spines:
            self.lr_devices.append([device for device in self.devices if device_dict['name'] == device.name][0])
            if intravn:
                if index is 0:
                    vn = self.create_vn()
                    self.vns.append(vn)
            else:
                vn = self.create_vn()
                self.vns.append(vn)
                vlanid = vlanid + index

            link = device_dict['links'][0]
            interface = dict()
            interface['tor'] = device_dict['name']
            interface['tor_port'] = link['from']
            l2_name = link['to']['name']
            l2_port = link['to']['port']
            # create vpg
            vpg = self.create_vpg([interface])
            # create vmi
            port_fixture = self.create_vmi(fabric_fixture=self.fabric, interfaces=[interface], name=vpg.get_name(),
                                           vnid=vn.get_uuid(), vlan_id=vlanid, vlan_tag=vlanid)
            self.addCleanup(self.delete_vmi, port_fixture)

            # configure l2 device up and down interface
            l2_device = [l2 for l2 in self.l2_devices if l2['name'] == l2_name][0]
            up_ifc = l2_port
            bms_list = self.get_bms_nodes(role='l2')
            bms = [bms for bms in bms_list for intfc in self.inputs.bms_data[bms]['interfaces'] if intfc['tor'] == l2_name][0]
            bms_dict = self.inputs.bms_data[bms]
            down_ifc = [intfc['tor_port'] for intfc in bms_dict['interfaces'] if intfc['tor'] == l2_name][0]
            mgmt_ip = l2_device['mgmt_ip']
            ssh_username = l2_device['ssh_username']
            ssh_password = l2_device['ssh_password']
            vlan = get_random_name('vlan')
            self.configure_l2_vlan(pi_name=up_ifc, vlan_name=vlan, vlan_id=vlanid, host=mgmt_ip, up_link=True,
                                   username=ssh_username, password=ssh_password, name=l2_name)
            self.configure_l2_vlan(pi_name=down_ifc, vlan_name=vlan, vlan_id=vlanid, host=mgmt_ip,
                                   username=ssh_username, password=ssh_password, name=l2_name)

            # create namespace on bms
            bms_ip = vn.get_an_ip(index=2+index)
            bms = self.create_bms(bms_name=bms, vn_fixture=vn, tor_port_vlan_tag=vlanid, verify_bms=False,
                                  fabric_fixture=self.fabric, vmi_create=False, bms_ip=bms_ip, vlan_id=vlanid)
            self.instances.append(bms)
            index += 1

    def delete_vmi(self, port_fixture):
        if port_fixture:
            port_fixture.cleanUp(force=True)
            if hasattr(port_fixture, '_cleanups') and \
                    port_fixture._cleanups is None \
                    and hasattr(port_fixture, '_clear_cleanups'):
                port_fixture._clear_cleanups()

    @preposttest_wrapper
    def test_fabric_collapsed_spine_intravn(self):
        self.configure_fabric_for_collapsed_spine(intravn=True)
        self.create_logical_router(self.vns, devices=self.lr_devices)
        self.do_ping_mesh(self.instances)

    @preposttest_wrapper
    def test_fabric_collapsed_spine_dm_stop_start(self):
        self.configure_fabric_for_collapsed_spine()
        self.inputs.stop_container(self.inputs.cfgm_ips, 'device-manager')
        self.create_logical_router(self.vns, devices=self.lr_devices)
        self.inputs.start_container(self.inputs.cfgm_ips, 'device-manager')
        self.sleep(30)
        self.do_ping_mesh(self.instances)

    @preposttest_wrapper
    def test_fabric_collapsed_spine_api_dm_restart(self):
        self.configure_fabric_for_collapsed_spine()
        self.create_logical_router(self.vns, devices=self.lr_devices)
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'api-server')
        self.sleep(30)
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'device-manager')
        self.sleep(30)
        self.do_ping_mesh(self.instances)
