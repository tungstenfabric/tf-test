from __future__ import absolute_import
from tcutils.wrappers import preposttest_wrapper
from common.contrail_fabric.base import BaseFabricTest
from common.fabric_utils import DEFAULT_UPGRADE_PARAMS
import test
import copy
from tcutils.util import skip_because

class TestHitlessUpgrade(BaseFabricTest):

    @classmethod
    def setUpClass(cls):
        super(TestHitlessUpgrade, cls).setUpClass()
        cls.swift_h = cls.connections.swift_h

    @classmethod
    def tearDownClass(cls):
        super(TestHitlessUpgrade, cls).tearDownClass()

    @skip_because(function='filter_bms_nodes', bms_type='multi_homing')
    @preposttest_wrapper
    def test_hitless_upgrade(self):
        self.inputs.set_af('dual')
        self.addCleanup(self.inputs.set_af, 'v4')
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        self.create_logical_router([vn1, vn2])
        instances = list()
        bms_nodes = self.get_bms_nodes(bms_type='multi_homing')
        prouter = self.get_associated_prouters(bms_nodes[0])[0]
        device_images = self.check_and_create_image_for_device([prouter])
        instances.append(self.create_bms(bms_name=bms_nodes[0],
                                         tor_port_vlan_tag=11,
                                         vn_fixture=vn1))
        self.hitless_upgrade_strategy(device_images, self.fabric,
                                      upgrade_mode='test_run')
        other_bms_node = None
        if len(bms_nodes) > 1:
            other_bms_node = bms_nodes[1]
        else:
            other_nodes = set(self.get_bms_nodes()) - set(bms_nodes)
            for node in other_nodes:
                if prouter.name not in self.get_associated_prouters(node):
                    other_bms_node = node
                    break
        if other_bms_node:
            instances.append(self.create_bms(bms_name=other_bms_node,
                                             vlan_id=21,
                                             vn_fixture=vn2))
        instances.append(self.create_vm(vn_fixture=vn1, image_name='cirros-traffic'))
        self.do_ping_mesh(instances)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=11000)
        traffic = self.start_traffic(instances[0], instances[1], 'udp',
                                     dport=11001, slow=True)
        self.hitless_upgrade_strategy(device_images, self.fabric)
        self.stop_traffic(traffic)
        self.do_ping_mesh(instances)

    @preposttest_wrapper
    def test_upgrade_w_healthcheck_disabled(self):
        instances = list()
        advanced_params = copy.deepcopy(DEFAULT_UPGRADE_PARAMS)
        advanced_params['health_check_abort'] = False

        vn1 = self.create_vn()
        bms_nodes = self.get_bms_nodes()
        interfaces = self.inputs.bms_data[bms_nodes[0]]['interfaces'][:1]
        prouter = self.get_associated_prouters(bms_nodes[0], interfaces)[0]
        device_images = self.check_and_create_image_for_device([prouter])
        try:
            msg = "when there is no bms instances in the device"
            self.hitless_upgrade_strategy(device_images, self.fabric,
                                      upgrade_mode='test_run')
            assert False, 'Hitless upgrade should have failed ' + msg
        except AssertionError:
            self.logger.info('Hitless upgrade failed as expected ' + msg)
        self.hitless_upgrade_strategy(device_images, self.fabric,
           advanced_params=advanced_params, upgrade_mode='test_run')
        instances.append(self.create_bms(bms_name=bms_nodes[0],
                                         vlan_id=40,
                                         interfaces=interfaces,
                                         vn_fixture=vn1))
        try:
            msg = "when there is no multihomed bms instances in the device"
            self.hitless_upgrade_strategy(device_images, self.fabric,
                                      upgrade_mode='test_run')
            assert False, 'Hitless upgrade should have failed ' + msg
        except AssertionError:
            self.logger.info('Hitless upgrade failed as expected ' + msg)
        self.hitless_upgrade_strategy(device_images, self.fabric,
           advanced_params=advanced_params, upgrade_mode='test_run')
        if len(bms_nodes) > 1:
            instances.append(self.create_bms(bms_name=bms_nodes[1],
                                             vlan_id=40,
                                             vn_fixture=vn1))
        instances.append(self.create_vm(vn_fixture=vn1, image_name='cirros-traffic'))
        self.do_ping_mesh(instances)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=9000)
        traffic = self.start_traffic(instances[0], instances[1],
                                     'udp', dport=1001, slow=True)
        self.hitless_upgrade_strategy(device_images, self.fabric,
            advanced_params=advanced_params)
        self.sleep(60) # Waiting for chassis/fpc cards to be up
        self.stop_traffic(traffic, partial=True)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=9001)

    @skip_because(function='filter_bms_nodes', bms_type='multi_homing')
    @preposttest_wrapper
    def test_upgrade_multiple_devices_multiple_times(self):
        instances = list()
        advanced_params = copy.deepcopy(DEFAULT_UPGRADE_PARAMS)
        advanced_params['health_check_abort'] = False
        vn1 = self.create_vn()
        bms_node = self.get_bms_nodes(bms_type='multi_homing')[0]
        interfaces = self.inputs.bms_data[bms_node]['interfaces']

        #Upgrade multiple devices
        bms1_interfaces = interfaces[:1]
        bms2_interfaces = interfaces[1:2]
        prouter1 = self.get_associated_prouters(bms_node, bms1_interfaces)[0]
        prouter2 = self.get_associated_prouters(bms_node, bms2_interfaces)[0]
        prouters = [prouter1, prouter2]
        device_images = self.check_and_create_image_for_device(prouters)
        self.hitless_upgrade_strategy(device_images, self.fabric,
           advanced_params=advanced_params, upgrade_mode='test_run')
        instances.append(self.create_bms(bms_name=bms_node,
                                         vlan_id=50,
                                         interfaces=bms1_interfaces,
                                         vn_fixture=vn1))
        instances.append(self.create_bms(bms_name=bms_node,
                                         interfaces=bms2_interfaces,
                                         vlan_id=50,
                                         vn_fixture=vn1))
        self.do_ping_mesh(instances)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=9100)
        traffic = self.start_traffic(instances[0], instances[1], 'udp',
                                     dport=1002, slow=True)
        self.hitless_upgrade_strategy(device_images, self.fabric,
            advanced_params=advanced_params)
        self.sleep(60) # Waiting for chassis/fpc cards to be up
        self.stop_traffic(traffic, partial=True)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=9102)

        #Upgrade multiple times
        device_images = self.check_and_create_image_for_device(prouters)
        self.hitless_upgrade_strategy(device_images, self.fabric,
           advanced_params=advanced_params, upgrade_mode='test_run')
        traffic = self.start_traffic(instances[0], instances[1], 'udp',
                                     slow=True, dport=1001)
        self.hitless_upgrade_strategy(device_images, self.fabric,
            advanced_params=advanced_params)
        self.sleep(60) # Waiting for chassis/fpc cards to be up
        self.stop_traffic(traffic, partial=True)
        self.verify_traffic(instances[0], instances[1], 'udp', dport=9102)

    @preposttest_wrapper
    def test_upgrade_spine(self):
        advanced_params = copy.deepcopy(DEFAULT_UPGRADE_PARAMS)
        vn1 = self.create_vn()
        vn2 = self.create_vn()
        self.create_logical_router([vn1, vn2])
        bms_nodes = self.get_bms_nodes()
        device_images = self.check_and_create_image_for_device(self.spines)
        try:
            msg = 'when all the spines are upgraded at the same time'
            self.hitless_upgrade_strategy(device_images, self.fabric,
                                      upgrade_mode='test_run')
            assert False, 'Hitless upgrade should have failed ' + msg
        except AssertionError:
            self.logger.info('Hitless upgrade failed as expected ' + msg)
        device_images = self.check_and_create_image_for_device(self.spines[:1])
        self.hitless_upgrade_strategy(device_images, self.fabric,
                                      upgrade_mode='test_run')
        bms1 = self.create_bms(bms_name=bms_nodes[0],
                               vlan_id=14,
                               vn_fixture=vn1)
        bms1_2 = self.create_bms(bms_name=bms_nodes[0],
                                 vlan_id=24,
                                 bond_name=bms1.bond_name,
                                 port_group_name=bms1.port_group_name,
                                 vn_fixture=vn2)
        bms2 = self.create_bms(bms_name=bms_nodes[1],
                               vlan_id=24,
                               vn_fixture=vn2)
        vm1 = self.create_vm(vn_fixture=vn1, image_name='cirros-traffic')
        instances = [bms1, bms2, bms1_2, vm1]
        self.do_ping_mesh(instances)
        flows = list()
        for i in range(1, 10):
           flows.append(self.start_traffic(bms1, bms2, 'udp', dport=11001, slow=True))
           flows.append(self.start_traffic(bms1_2, bms2, 'udp', dport=11001, slow=True))
        self.hitless_upgrade_strategy(device_images, self.fabric)
        for flow in flows:
            self.stop_traffic(flow)
        self.do_ping_mesh(instances)
