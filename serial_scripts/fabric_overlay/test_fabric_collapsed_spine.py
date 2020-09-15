from tcutils.wrappers import preposttest_wrapper
from common.contrail_fabric.base import BaseFabricTest


class TestFabricCollapsedSpine(BaseFabricTest):
    def is_test_applicable(self):
        result, msg = super(TestFabricCollapsedSpine, self).is_test_applicable()
        if result is False:
            return False, msg
        self.c_spines = []

        leaf_dicts = [device_dict for device_dict in list(self.inputs.physical_routers_data.values())
                      if device_dict.get('role', '') == 'leaf']
        spines = [device_dict['name'] for device_dict in list(self.inputs.physical_routers_data.values())
                  if device_dict.get('role', '') == 'spine']
        for leaf in leaf_dicts:
            remote_names = [link['remote']['name'] for link in leaf['links']]
            for spine in spines:
                if spine in remote_names:
                    if spine not in self.c_spines:
                        self.c_spines.append(spine)
                        self.rb_roles[spine] = ['Collapsed-Spine', 'Route-Reflector']
                    self.rb_roles[leaf['name']] = []

        if len(self.c_spines) < 2:
            return False, 'At least two spines are required in fabric topology'
        return True, msg

    def setUp(self):
        super(TestFabricCollapsedSpine, self).setUp()

    def configure_fabric_for_collapsed_spine(self, intravn=False):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        self.instances, self.vns, self.lr_devices = [], [], []
        index = 0
        vlanid = index + 10
        for bms in self.get_bms_nodes():
            if intravn:
                if index is 0:
                    vn = self.create_vn()
                    self.vns.append(vn)
            else:
                vn = self.create_vn()
                self.vns.append(vn)
                vlanid = vlanid + index
            bms = self.create_bms(bms_name=bms, vn_fixture=vn, tor_port_vlan_tag=vlanid,
                                  fabric_fixture=self.fabric, is_collapsed_spine=True, vlan_id=vlanid)
            self.instances.append(bms)
            index += 1
        for spine in self.c_spines:
            self.lr_devices.append([device for device in self.devices if spine == device.name][0])

    @preposttest_wrapper
    def test_fabric_collapsed_spine_intravn(self):
        self.configure_fabric_for_collapsed_spine(intravn=True)
        self.sleep(30)
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
        self.sleep(30)
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'api-server')
        self.sleep(30)
        self.do_ping_mesh(self.instances)
        self.inputs.restart_container(self.inputs.cfgm_ips, 'device-manager')
        self.sleep(30)
        self.do_ping_mesh(self.instances)
