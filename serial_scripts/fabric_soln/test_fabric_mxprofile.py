from tcutils.wrappers import preposttest_wrapper
from common.contrail_fabric.base import BaseFabricTest
from tcutils.util import skip_because
import test
import time
import random
from tcutils.wrappers import preposttest_wrapper
from common.contrail_fabric.mcast_base import *


class TestFabricCRBprofile(Evpnt6TopologyBase):
    def is_test_applicable(self):
        result, msg = super(TestFabricCRBprofile, self).is_test_applicable()

        roles = []
        if result:
            for device_dict in list(self.inputs.physical_routers_data.values()):
                if device_dict.get('rb_roles'):
                    for ele in device_dict.get('rb_roles'):
                        roles.append(ele)

            msg = 'No device with roles route-reflector,dc_gw,crb_mcast_gw,crb_gw roles in the provided fabric topology'
            reqRoles = ['route-reflector','dc_gw','crb_mcast_gw','crb_gw' ]
            for ele in reqRoles:
                if ele not in roles:
                    return False, msg
             
            msg = 'No public subnets or public host specified in test inputs yaml'
            if self.inputs.public_subnets and self.inputs.public_host:
                return (True, None)
            else:
                return False, msg
        return (True, None)
    
    def setUp(self):
        
        for device, device_dict in list(self.inputs.physical_routers_data.items()):
            self.rb_roles[device] = []
            if device_dict['role'] == 'spine':

                if 'route-reflector' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device] = ['Route-Reflector']
                if 'dc_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('DC-Gateway')

                if 'crb_mcast_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-MCAST-Gateway')
                if 'crb_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-Gateway')
            elif device_dict['role'] == 'leaf':
                if 'erb_ucast_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('ERB-UCAST-Gateway')
                if 'crb-access' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-Access')
        super(TestFabricCRBprofile, self).setUp()

    def cleanup_cli(self,spines):
        cmd = []
        cmd.append('delete groups mcastgw')
        cmd.append('delete apply-groups mcastgw')
        for prouter in spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

    @skip_because(function='filter_bms_nodes',min_bms_count=3)
    @preposttest_wrapper
    def test_crb_profile(self):

        self.logger.info('Validate external networks are reachable.')

        dcgw_bms_fixtures = list()
        public_vn = self.create_vn(vn_subnets=self.inputs.public_subnets[:1],
                                   router_external=True)
        private_vn = self.create_vn()
        fip_pool = self.create_fip_pool(public_vn.uuid)
        bms = list(self.inputs.bms_data.keys())[2]
        bms_fixture = self.create_bms(bms_name=bms, vn_fixture=public_vn)
        dcgw_bms_fixtures.append(bms_fixture)
        for spine in self.spines:
            prouter_details = self.inputs.physical_routers_data[spine.name]
            if prouter_details.get('model', '').startswith('mx'):
                spine.add_virtual_network(public_vn.uuid)
                self.addCleanup(spine.delete_virtual_network, public_vn.uuid)
        dcgw_vm = self.create_vm(vn_fixture=private_vn, image_name='cirros-0.4.0')
        self.check_vms_booted([dcgw_vm])
        self.create_and_assoc_fip(fip_pool, dcgw_vm)
        for fixture in dcgw_bms_fixtures + [dcgw_vm]:
            msg = 'ping from %s to %s failed'%(fixture.name,
                                               self.inputs.public_host)
            assert fixture.ping_with_certainty(self.inputs.public_host),msg

        time.sleep(40)

        self.logger.info('Validate inter vn unicast and multicast.')

        vxlan1 = random.randrange(400, 405)
        bms = self.get_bms_nodes()
        
        vn1_fixture = self.create_vn(vxlan_id=vxlan1,
                                          forwarding_mode='l2_l3')
        vn1_fixture.set_igmp_config()
        vxlan2 = random.randrange(406, 410)
        vn2_fixture = self.create_vn(vxlan_id=vxlan2,
                                          forwarding_mode='l2_l3')
        vn2_fixture.set_igmp_config()

        erb_devices = list()
        erb_devices.extend(self.spines)

        self.create_logical_router([vn1_fixture ,vn2_fixture] , devices=set(erb_devices))

        time.sleep(60)

        # WA till CEM-15484 is fixed.
        cmd = []
        cmd.append('set groups mcastgw routing-instances <__contrail_ctest-Router*> protocols pim passive')
        cmd.append('set apply-groups mcastgw')
        for prouter in self.spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

        self.addCleanup(self.cleanup_cli,self.spines)


        bms_fixture1 = self.create_bms(bms_name=bms[0],
            vn_fixture=vn1_fixture,
            vlan_id=vxlan1)
        interface = bms_fixture1.get_mvi_interface()
        bms_fixture1.config_mroute(interface,'225.1.1.1','255.255.255.255')


        igmp = {'type': 22,                # IGMPv3 Report
                'numgrp': 1,               # Number of group records
                'gaddr': '225.1.1.1'       # Multicast group address
               }

        bms_fixture2 = self.create_bms(bms_name=bms[1],
            vn_fixture=vn2_fixture,
            vlan_id=vxlan2)
        interface = bms_fixture2.get_mvi_interface()
        bms_fixture2.config_mroute(interface,'225.1.1.1','255.255.255.255')


        
        vm2_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu', vm_name="vm2")

        # Wait till vm is up
        assert vm2_fixture.wait_till_vm_is_up()


        vm_fixtures = {'bms1':bms_fixture1,'bms2':bms_fixture2, 'vn1':vn1_fixture ,'vn2':vn2_fixture, 'vm2':vm2_fixture,}

        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])

        time.sleep(20)


        self.logger.info('Make sure bms/vm in different VN is getting multicast packet on sending igmp join.')
 
        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': ['bms2','vm2'],     # Multicast receivers
                             'non_rcvrs': [],        # Non Multicast receivers
                             'maddr': '225.1.1.1',          # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of groups
                               }
                  }

        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)


        self.logger.info('Send igmp leave , VMs should not get multicast traffic.')

        igmp = {'type': 23,                   # IGMPv3 Report
              'numgrp': 1,                    # Number of group records
              'gaddr': '225.1.1.1'       # Multicast group address
               }

        interface = bms_fixture2.get_mvi_interface()
        self.send_igmp_reportv2(vm_fixtures['bms2'], igmp,interface)
        self.send_igmp_reportv2(vm_fixtures['vm2'], igmp,"eth0")

        time.sleep(10)

        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': [],     # Multicast receivers
                             'non_rcvrs': ['bms2','vm2'],        # Non Multicast receivers
                             'maddr': '225.1.1.1',        # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of packets
                               }
                  }


        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)

        msg = "Inter VN ping is failing"
        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])


        self.inputs.restart_container(self.inputs.cfgm_ips, 'device-manager')
        self.sleep(90) #Wait to make sure if any config push happens to complete

        # WA till CEM-15484 is fixed.
        cmd = []
        cmd.append('set groups mcastgw routing-instances <__contrail_ctest-Router*> protocols pim passive')
        cmd.append('set apply-groups mcastgw')
        for prouter in self.spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])

        self.logger.info('Make sure bms/vm in different VN is getting multicast packet on sending igmp join.')

        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': ['bms2','vm2'],     # Multicast receivers
                             'non_rcvrs': [],        # Non Multicast receivers
                             'maddr': '225.1.1.1',          # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of groups
                               }
                  }
        igmp = {'type': 22,                # IGMPv3 Report
                'numgrp': 1,               # Number of group records
                'gaddr': '225.1.1.1'       # Multicast group address
               }

        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)


        for fixture in dcgw_bms_fixtures + [dcgw_vm]:
            msg = 'ping from %s to %s failed'%(fixture.name,
                                               self.inputs.public_host)
            assert fixture.ping_with_certainty(self.inputs.public_host),msg




class TestFabricERBProfile(Evpnt6TopologyBase):
    def is_test_applicable(self):
        result, msg = super(TestFabricERBProfile, self).is_test_applicable()

        roles = []
        if result:
            for device_dict in list(self.inputs.physical_routers_data.values()):
                #if device_dict.get('rb_roles'):
                #    roles.append(device_dict.get('rb_roles'))
                if device_dict.get('rb_roles'):
                    for ele in device_dict.get('rb_roles'):
                        roles.append(ele)

            msg = 'No device with roles route-reflector,dc_gw,crb_mcast_gw,crb_gw roles in the provided fabric topology'
            reqRoles = ['route-reflector','dc_gw','crb_mcast_gw','erb_ucast_gw' ]
            for ele in reqRoles:
                if ele not in roles:
                    return False, msg

            msg = 'No public subnets or public host specified in test inputs yaml'
            if self.inputs.public_subnets and self.inputs.public_host:
                return (True, None)
            else:
                return False, msg
        return (True, None)

    
    def setUp(self):
        
        for device, device_dict in list(self.inputs.physical_routers_data.items()):
            self.rb_roles[device] = []
            if device_dict['role'] == 'spine':

                if 'route-reflector' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device] = ['Route-Reflector']
                if 'dc_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('DC-Gateway')

                if 'crb_mcast_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-MCAST-Gateway')
                if 'crb_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-Gateway')
            elif device_dict['role'] == 'leaf':
                if 'erb_ucast_gw' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('ERB-UCAST-Gateway')
                if 'crb-access' in (device_dict.get('rb_roles') ):
                    self.rb_roles[device].append('CRB-Access')
        super(TestFabricERBProfile, self).setUp()


    def cleanup_cli(self,spines):
        cmd = []
        cmd.append('delete groups mcastgw')
        cmd.append('delete apply-groups mcastgw')
        for prouter in spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

    @skip_because(function='filter_bms_nodes', min_bms_count=3)
    @preposttest_wrapper
    def test_erb_profile(self):


        time.sleep(60)
        self.logger.info('Validate external networks are reachable.')
        dcgw_bms_fixtures = list()
        public_vn = self.create_vn(vn_subnets=self.inputs.public_subnets[:1],
                                   router_external=True)
        private_vn = self.create_vn()
        fip_pool = self.create_fip_pool(public_vn.uuid)
        bms = self.get_bms_nodes(rb_role='crb-access')
        bms_dcgw = bms[0]
        bms_fixture = self.create_bms(bms_name=bms_dcgw, vn_fixture=public_vn)
        dcgw_bms_fixtures.append(bms_fixture)
        for spine in self.spines:
            prouter_details = self.inputs.physical_routers_data[spine.name]
            if prouter_details.get('model', '').startswith('mx'):
                spine.add_virtual_network(public_vn.uuid)
                self.addCleanup(spine.delete_virtual_network, public_vn.uuid)
        dcgw_vm = self.create_vm(vn_fixture=private_vn, image_name='cirros-0.4.0')
        self.check_vms_booted([dcgw_vm])
        self.create_and_assoc_fip(fip_pool, dcgw_vm)
        for fixture in dcgw_bms_fixtures + [dcgw_vm]:
            msg = 'ping from %s to %s failed'%(fixture.name,
                                               self.inputs.public_host)
            assert fixture.ping_with_certainty(self.inputs.public_host),msg

        self.logger.info('Validate inter vn unicast and multicast.')

        vxlan1 = random.randrange(400, 405)
        vn1_fixture = self.create_vn(vxlan_id=vxlan1,
                                          forwarding_mode='l2_l3')
        vn1_fixture.set_igmp_config()
        vxlan2 = random.randrange(406, 410)
        vn2_fixture = self.create_vn(vxlan_id=vxlan2,
                                          forwarding_mode='l2_l3')
        vn2_fixture.set_igmp_config()
        erb_devices = list()
        bms = self.get_bms_nodes(rb_role='erb_ucast_gw')
        for bmsN in bms:
            erb_devices.extend(self.get_associated_prouters(bmsN))
        erb_devices.extend(self.spines)

        self.create_logical_router([vn1_fixture ,vn2_fixture] , devices=set(erb_devices))

        time.sleep(60)

        # WA till CEM-15484 is fixed.
        cmd = []
        cmd.append('set groups mcastgw routing-instances <__contrail_ctest-Router*> protocols pim passive')
        cmd.append('set apply-groups mcastgw')
        for prouter in self.spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

        self.addCleanup(self.cleanup_cli,self.spines)


        bms_fixture1 = self.create_bms(bms_name=bms[0],
            vn_fixture=vn1_fixture,
            vlan_id=vxlan1)
        interface = bms_fixture1.get_mvi_interface()
        bms_fixture1.config_mroute(interface,'225.1.1.1','255.255.255.255')


        igmp = {'type': 22,                # IGMPv3 Report
                'numgrp': 1,               # Number of group records
                'gaddr': '225.1.1.1'       # Multicast group address
               }

        bms_fixture2 = self.create_bms(bms_name=bms[1],
            vn_fixture=vn2_fixture,
            vlan_id=vxlan2)
        interface = bms_fixture2.get_mvi_interface()
        bms_fixture2.config_mroute(interface,'225.1.1.1','255.255.255.255')


        
        vm2_fixture = self.create_vm(vn_fixture=vn2_fixture,
            image_name='ubuntu', vm_name="vm2")

        # Wait till vm is up
        assert vm2_fixture.wait_till_vm_is_up()


        vm_fixtures = {'bms1':bms_fixture1,'bms2':bms_fixture2, 'vn1':vn1_fixture ,'vn2':vn2_fixture, 'vm2':vm2_fixture,}

        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])


        time.sleep(20)


        self.logger.info('Make sure bms/vm in different VN is getting multicast packet on sending igmp join.')
 
        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': ['bms2','vm2'],     # Multicast receivers
                             'non_rcvrs': [],        # Non Multicast receivers
                             'maddr': '225.1.1.1',          # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of groups
                               }
                  }

        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)


        self.logger.info('Send igmp leave , VMs should not get multicast traffic.')

        igmp = {'type': 23,                   # IGMPv3 Report
              'numgrp': 1,                    # Number of group records
              'gaddr': '225.1.1.1'       # Multicast group address
               }

        interface = bms_fixture2.get_mvi_interface()
        self.send_igmp_reportv2(vm_fixtures['bms2'], igmp,interface)
        self.send_igmp_reportv2(vm_fixtures['vm2'], igmp,"eth0")

        time.sleep(10)

        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': [],     # Multicast receivers
                             'non_rcvrs': ['bms2','vm2'],        # Non Multicast receivers
                             'maddr': '225.1.1.1',        # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of packets
                               }
                  }


        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)

        msg = "Inter VN ping is failing"
        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])

        for fixture in dcgw_bms_fixtures + [dcgw_vm]:
            msg = 'ping from %s to %s failed'%(fixture.name,
                                               self.inputs.public_host)
            assert fixture.ping_with_certainty(self.inputs.public_host),msg

        self.logger.info('Validate features after DM restart.')

        self.inputs.restart_container(self.inputs.cfgm_ips, 'device-manager')
        self.sleep(90) #Wait to make sure if any config push happens to complete

        # WA till CEM-15484 is fixed.
        cmd = []
        cmd.append('set groups mcastgw routing-instances <__contrail_ctest-Router*> protocols pim passive')
        cmd.append('set apply-groups mcastgw')
        for prouter in self.spines:
            prouter.netconf.config(stmts=cmd, timeout=120)

        self.do_ping_mesh([bms_fixture1 ,bms_fixture2 ,vm2_fixture])

        self.logger.info('Make sure bms/vm in different VN is getting multicast packet on sending igmp join.')

        traffic = {'stream1': {'src':['bms1'],                 # Multicast source
                             'rcvrs': ['bms2','vm2'],     # Multicast receivers
                             'non_rcvrs': [],        # Non Multicast receivers
                             'maddr': '225.1.1.1',          # Multicast group address
                             'mnet': '225.1.1.1/32',        # Multicast group address
                             'source': bms_fixture1.bms_ip,  # Multicast group address
                             'pcount':10,                 # Num of packets
                             'count':1                   # Num of groups
                               }
                  }

        igmp = {'type': 22,                # IGMPv3 Report
                'numgrp': 1,               # Number of group records
                'gaddr': '225.1.1.1'       # Multicast group address
               }
        assert self.send_verify_intervn_mcast(vm_fixtures, traffic, igmp,vxlan1)

        self.logger.info('Validate Security groups.')

        vn2_subnet = vn2_fixture.get_cidrs()[0]
        sg_rule = self._get_secgrp_rule(cidr=vn2_subnet, direction='egress')
        sg = self.create_security_group(rules=[sg_rule])
        bms_fixture2.add_security_groups([sg.uuid])
        bms_fixture1.add_security_groups([sg.uuid])
        assert bms_fixture2.ping_with_certainty(ip=bms_fixture1.bms_ip,expectation=False)
        assert bms_fixture2.ping_with_certainty(ip=vm2_fixture.vm_ip)
        assert bms_fixture1.ping_with_certainty(ip=vm2_fixture.vm_ip)
        bms_fixture2.delete_security_groups([sg.uuid])
        bms_fixture1.delete_security_groups([sg.uuid])
        sleep(60)
        assert bms_fixture2.ping_with_certainty(ip=bms_fixture1.bms_ip)
        assert bms_fixture2.ping_with_certainty(ip=vm2_fixture.vm_ip)
 
