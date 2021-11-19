from builtins import object
from fabric_test import FabricFixture
from virtual_port_group import VPGFixture
from physical_device_fixture import PhysicalDeviceFixture
from pif_fixture import PhysicalInterfaceFixture
from lif_fixture import LogicalInterfaceFixture
from bms_fixture import BMSFixture
from port_profile import PortProfileFixture
from storm_control_profile import StormControlProfileFixture
from tcutils.util import retry, get_random_name
from lxml import etree
from tcutils.verification_util import elem2dict
from collections import defaultdict
import time

NODE_PROFILES = ['juniper-mx', 'juniper-qfx10k', 'juniper-qfx5120', 'juniper-qfx5220',
                 'juniper-qfx5k', 'juniper-qfx5k-lean', 'juniper-qfx10k-lean', 'juniper-srx']
VALID_OVERLAY_ROLES = ['dc-gateway', 'crb-access', 'dci-gateway',
                       'ar-client', 'crb-gateway', 'erb-ucast-gateway',
                       'crb-mcast-gateway', 'ar-replicator', 'route-reflector',
                       'collapsed-spine', 'pnf-servicechain']
DEFAULT_UPGRADE_PARAMS = {
    'bulk_device_upgrade_count': 4,
    'health_check_abort': True,
    'Juniper': {
        'bgp': {
            'bgp_flap_count': 15,
            'bgp_flap_count_check': True,
            'bgp_down_peer_count': 0,
            'bgp_down_peer_count_check': True,
            'bgp_peer_state_check': True
        },
        'alarm': { # Disabling alarm since it fails most of the time
          'system_alarm_check': False,
          'chassis_alarm_check': False
        },
        'interface': {
          'interface_error_check': True,
          'interface_drop_count_check': True,
          'interface_carrier_transition_count_check': True
        },
        'routing_engine': {
          'routing_engine_cpu_idle': 40,
          'routing_engine_cpu_idle_check': True
        },
        'fpc': {
          'fpc_cpu_5min_avg': 50,
          'fpc_cpu_5min_avg_check': True,
          'fpc_memory_heap_util': 45,
          'fpc_memory_heap_util_check': True
        },
        'active_route_count_check': True,
        'l2_total_mac_count_check': True,
        'storm_control_flag_check': True,
        'lacp': {
          'lacp_down_local_check': True,
          'lacp_down_peer_check': True
        }
    }
}

class FabricUtils(object):

    @retry(delay=10, tries=12)
    def _get_fabric_fixture(self, name):
        fabric = FabricFixture(connections=self.connections,
                               name=name)
        fabric.read()
        if not fabric.uuid:
            return (False, None)
        return (True, fabric)

    def onboard_fabric(self, fabric_dict, wait_for_finish=True,
                       name=None, cleanup=False, enterprise_style=True, dc_asn=None ,serList=None):
        interfaces = {'physical': [], 'logical': []}
        devices = list()
        name = name if name else get_random_name('fabric')

        fq_name = ['default-global-system-config',
                   'fabric_onboard_template']
        if 'image_upgrade_os_version' in list(fabric_dict['namespaces'].keys()):
            self.logger.info("ZTP with image upgrade")
            os_version = fabric_dict['namespaces']['image_upgrade_os_version']
        else:
            self.logger.info("ZTP without image upgrade")
            os_version = ''

        payload = {'fabric_fq_name': ["default-global-system-config", name],
                   'fabric_display_name': name,
                   "supplemental_day_0_cfg":[{"name": dct["supplemental_day_0_cfg"]["name"],\
                                              "cfg": dct["supplemental_day_0_cfg"]["cfg"]}
                        for dct in list(self.inputs.physical_routers_data.values()) \
                           if dct.get('supplemental_day_0_cfg') \
                               if serList is None or dct["serial_number"] in serList],
                   'device_to_ztp': [{"serial_number": dct['serial_number'], \
                                      "hostname": dct['name'], \
                                      "supplemental_day_0_cfg": dct.get("supplemental_day_0_cfg",{}).get('name','')} \
                       for dct in list(self.inputs.physical_routers_data.values()) \
                           if dct.get('serial_number') \
                               if serList is None or dct["serial_number"] in serList],
                   'node_profiles': [{"node_profile_name": profile}
                       for profile in fabric_dict.get('node_profiles')\
                                      or NODE_PROFILES],
                   'device_auth': {"root_password": fabric_dict['credentials'][0]['password']},
                   'loopback_subnets': fabric_dict['namespaces']['loopback_subnets'],
                   'management_subnets': fabric_dict['namespaces']['management_subnets'],
                   'fabric_subnets': fabric_dict['namespaces']['fabric_subnets'],
                   'overlay_ibgp_asn': dc_asn or fabric_dict['namespaces']['overlay_ibgp_asn'],
                   'fabric_asn_pool': [{"asn_max": fabric_dict['namespaces']['asn'][0]['max'],
                                       "asn_min": fabric_dict['namespaces']['asn'][0]['min']}]
                   }
        if os_version:
            payload['os_version'] = os_version
        self.logger.info('Onboarding new fabric %s %s'%(name, payload))
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        status, fabric = self._get_fabric_fixture(name)
        assert fabric, 'Create fabric seems to have failed'
        if cleanup:
            self.addCleanup(self.cleanup_fabric, fabric, devices, interfaces)
        if wait_for_finish:
            try:
                status = self.wait_for_job_to_finish(':'.join(fq_name),
                    execution_id)[0]
            except AssertionError:
                self.cleanup_fabric(fabric, verify=False)
                raise
            assert status, 'job %s to create fabric failed'%execution_id
            for device in fabric.fetch_associated_devices() or []:
                device_dict = self.get_prouter_dict(device)
                device_fixture = PhysicalDeviceFixture(
                    connections=self.connections, name=device)
                device_fixture.read()
                device_fixture.add_csn()
                devices.append(device_fixture)
            for device in devices:
                for port in device.get_physical_ports():
                    pif = PhysicalInterfaceFixture(uuid=port, connections=self.connections)
                    pif.read()
                    interfaces['physical'].append(pif)
            for pif in interfaces['physical']:
                for port in pif.get_logical_ports():
                    lif = LogicalInterfaceFixture(uuid=port, connections=self.connections)
                    lif.read()
                    interfaces['logical'].append(lif)
        return (fabric, devices, interfaces)

    def onboard_existing_fabric(self, fabric_dict, wait_for_finish=True,
                                name=None, cleanup=False,
                                enterprise_style=True, dc_asn=None):
        interfaces = {'physical': [], 'logical': []}
        devices = list()
        name = name if name else get_random_name('fabric')
        fq_name = ['default-global-system-config',
                   'existing_fabric_onboard_template']
        payload = {'fabric_fq_name': ["default-global-system-config", name],
                   'node_profiles': [{"node_profile_name": profile}
                       for profile in fabric_dict.get('node_profiles')\
                                      or NODE_PROFILES],
                   'device_auth': [{"username": cred['username'],
                                    "password": cred['password']}
                       for cred in fabric_dict['credentials']],
                   'overlay_ibgp_asn': dc_asn or fabric_dict['namespaces']['asn'][0]['min'],
                   'management_subnets': [{"cidr": mgmt["cidr"]}
                        for mgmt in fabric_dict['namespaces']['management']],
                   'loopback_subnets': fabric_dict['namespaces'].get('loopback',
                        ["10.126.127.128/27"]),
                   'enterprise_style': enterprise_style,
                   'pnf_servicechain_subnets': \
                       fabric_dict['namespaces'].get('pnf_service_chain') or []
                   }
        self.logger.info('Onboarding existing fabric %s %s' %(name, payload))
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        status, fabric = self._get_fabric_fixture(name)
        assert fabric, 'Create fabric seems to have failed'
        if cleanup:
            self.addCleanup(self.cleanup_fabric, fabric, devices, interfaces)
        if wait_for_finish:
            try:
                status = self.wait_for_job_to_finish(':'.join(fq_name),
                    execution_id)[0]
                assert status, 'job %s to create fabric failed'%execution_id
            except AssertionError:
                self.cleanup_fabric(fabric, verify=False)
                raise
            for device in fabric.fetch_associated_devices() or []:
                device_fixture = PhysicalDeviceFixture(connections=self.connections,
                                                       name=device)
                device_fixture.read()
                device_fixture.add_csn()
                devices.append(device_fixture)
            for device in devices:
                for port in device.get_physical_ports():
                    pif = PhysicalInterfaceFixture(uuid=port, connections=self.connections)
                    pif.read()
                    interfaces['physical'].append(pif)
            for pif in interfaces['physical']:
                for port in pif.get_logical_ports():
                    lif = LogicalInterfaceFixture(uuid=port, connections=self.connections)
                    lif.read()
                    interfaces['logical'].append(lif)
        return (fabric, devices, interfaces, execution_id)

    def abort_job(self, execution_id, abort_mode, action):
        self.logger.info('Abort job %s; action %s, mode: %s'%(
            execution_id, action, abort_mode))
        if action == 'onboard':
            fq_name = ['default-global-system-config',
                       'existing_fabric_onboard_template']
        elif action == 'assign_roles':
            fq_name = ['default-global-system-config',
                       'role_assignment_template']
        self.vnc_h.abort_job(job_execution_ids=execution_id, abort_mode=abort_mode)
        try:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert not status, 'job %s didnt get aborted'%execution_id
        except AssertionError:
            self.logger.info('Job %s got aborted as expected'%execution_id)
        time.sleep(30)

    #routine to fetch the gdo info from the nodes
    def get_chassis_gdo_info(self, fabric_dict, fq_name, payload, gdo_type,
                                wait_for_finish=True, cleanup=False):
        fq_name = ['default-global-system-config',
                   fq_name]
        payload = {payload: gdo_type
                   }
        self.logger.info('Fetching info from the fabric nodes')
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        status = self.check_gdo_details(gdo_type)
        assert status, 'Mismatch between the fabric info and the details fetched from the nodes'

    @retry(delay=10, tries=10)
    #confirm that the gdo info matches the expected result
    def check_gdo_details(self, gdo_type):
        #todo: skiranh . Check if the response is correct instead of the below routine
        start_time='now-5m'
        ops_h = self.connections.ops_inspects[self.inputs.collector_ips[0]]
        table = 'ObjectJobExecutionTable'
        query = '(Messagetype=JobLog)'
        response = ops_h.post_query(table, start_time=start_time,end_time='now',select_fields=['MessageTS', 'Messagetype', 'ObjectLog'],where_clause=query)
        gdo_occurence = 0
        if response:
            for resp in response:
                dct = elem2dict(etree.fromstring(resp['ObjectLog']))
                if "Imported system info for juniper device" in dct:
                    gdo_occurence = gdo_occurence + 1
        if gdo_occurence != len(self.fabric.devices):
            return True
        else:
            return False

    #routine to fetch the gdo info from the nodes
    def get_chassis_gdo_info_multiple(self, fabric_dict, fq_name, payload1, value1, payload2, value2,
                                wait_for_finish=True, cleanup=False):
        fq_name = ['default-global-system-config',
                   fq_name]
        payload = {payload1: value1, payload2: value2
                   }
        self.logger.info('Fetching info from the fabric nodes')
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        status = self.check_gdo_details(value2)
        assert status, 'Mismatch between the fabric info and the details fetched from the nodes'

    def cleanup_fabric(self, fabric, devices=None, interfaces=None,
                       verify=True, wait_for_finish=True, retry=True):
        fq_name = ['default-global-system-config', 'fabric_deletion_template']
        payload = {'fabric_fq_name': fabric.fq_name}
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        self.logger.info('Started cleanup of fabric %s'%(fabric.name))
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            if retry and not status:
                self.cleanup_fabric(fabric, verify=False, retry=False)
            assert status, 'job %s to cleanup fabric failed'%execution_id
            if verify:
                for lif in interfaces['logical']:
                    assert lif.verify_on_cleanup()
                for pif in interfaces['physical']:
                    assert pif.verify_on_cleanup()
                for device in devices or []:
                    assert device.verify_on_cleanup()
            assert fabric.verify_on_cleanup()
        time.sleep(90)
        return execution_id

    def discover(self, fabric, wait_for_finish=True):
        devices = list()
        fq_name = ['default-global-system-config', 'discover_device_template']
        payload = {'fabric_uuid': fabric.uuid}
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        self.logger.info('Started device discovery for fabric %s'%(
                         fabric.name))
        self.addCleanup(self.cleanup_discover, fabric, devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert status, 'job %s to discover devices failed'%execution_id
            for device in fabric.fetch_associated_devices() or []:
                device_fixture = PhysicalDeviceFixture(connections=self.connections,
                                                       name=device)
                device_fixture.read()
                device_fixture.add_csn()
                devices.append(device_fixture)
            self.logger.info('discovered devices %s for fabric %s'%(
                             devices, fabric.name))
        return execution_id, devices

    def cleanup_discover(self, fabric, devices=None, wait_for_finish=True):
        device_list = [device.name for device in devices or []]
        self.logger.info('Cleanup discovered devices %s for fabric %s'%(
                         device_list, fabric.name))
#        fabric.disassociate_devices()
#        for device in devices or []:
#            device.cleanUp(force=True)
        fq_name = ['default-global-system-config', 'device_deletion_template']
        payload = {'fabric_fq_name': fabric.fq_name, 'devices' : device_list}

        execution_id = self.vnc_h.execute_job(fq_name, payload)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            self.logger.info('cleanup discover status after wait_for_job_to_finish : %s' % status)
            assert status, 'job %s to delete devices %s failed'%(
                   execution_id, device_list)
            for device in devices or []:
                assert device.verify_on_cleanup()
        return execution_id

    def get_filters(self, filters):
        filters = filters if filters is not None else ['^ge', '^xe', '^ae', '^em', '^lo']
        if not filters:
             return {}
        filter_dict = {'interface_filters': []}
        for fltr in filters or []:
            dct = {'op': 'regex', 'expr': fltr}
            filter_dict['interface_filters'].append(dct)
        return filter_dict

    def onboard(self, devices, filters=None, wait_for_finish=True):
        interfaces = {'physical': [], 'logical': []}
        fq_name = ['default-global-system-config', 'device_import_template']
        payload = self.get_filters(filters)
        device_list = [device.uuid for device in devices]
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        self.logger.info('Started onboarding devices %s'%devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert status, 'job %s to onboard devices failed'%execution_id
            for device in devices:
                for port in device.get_physical_ports():
                    pif = PhysicalInterfaceFixture(uuid=port, connections=self.connections)
                    pif._clear_cleanups()
                    pif.read()
                    interfaces['physical'].append(pif)
            for pif in interfaces['physical']:
                for port in pif.get_logical_ports():
                    lif = LogicalInterfaceFixture(uuid=port, connections=self.connections)
                    lif._clear_cleanups()
                    lif.read()
                    interfaces['logical'].append(lif)
            return execution_id, interfaces
        return execution_id, None

    def cleanup_onboard(self, devices, interfaces):
        self.logger.info('Cleaning up onboarded devices %s'%devices)
        for lif in interfaces['logical']:
            lif.cleanUp(force=True)
            #assert lif.verify_on_cleanup()
        for pif in interfaces['physical']:
            pif.cleanUp(force=True)
            #assert pif.verify_on_cleanup()

    def configure_underlay(self, devices, payload=None, wait_for_finish=True):
        payload = payload or dict()
        payload.update({'enable_lldp': 'true'})
        fq_name = ['default-global-system-config', 'generate_underlay_template']
        device_list = [device.uuid for device in devices]
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        self.logger.info('Started configuring devices %s'%devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert status, 'job %s to configure underlay failed'%execution_id
            return execution_id, status
        return execution_id, None

    def fetch_hardware_inventory(self, fabric, devices, wait_for_finish=True):
        payload = {'fabric_fq_name': fabric.fq_name}
        fq_name = ['default-global-system-config', 'hardware_inventory_template']
        device_list = [device.uuid for device in devices]
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        self.logger.info('Fetching hardware inventory for devices %s'%devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert status, 'job %s to fetch hw inventory failed'%execution_id
            return execution_id, status
        return execution_id, None

    def get_prouter_dict(self, device_name):
        for device in self.inputs.physical_routers_data.values():
            if device['name'] == device_name:
                return device

    def get_role_from_inputs(self, device_name):
        for device in self.inputs.physical_routers_data.values():
            if device['name'] == device_name:
                return device['role']

    def create_provisioning_network(self, fabric, fabric_dict, **kwargs):
        name = fabric.name
        ipam = self.create_only_ipam(
                   subnet_method="flat-subnet",
                   project_name='default-project',
                   name=name+'-ztp-ipam',
                   connections=self.connections,
                   ipamtype=None,
                   vlan_tag=fabric_dict['provisioning_network']['vlan_tag'],
                   subnet=fabric_dict['provisioning_network']['ip_subnet'],
                   dhcp_relay_server=fabric_dict['provisioning_network']['dhcp_relay_server'],
                   default_gateway=fabric_dict['provisioning_network']['default_gateway'])
        vn = self.create_only_vn(
                 vn_name=name+'-ztp-network',
                 project_name='default-project',
                 connections=self.connections,
                 vn_subnets=[fabric_dict['provisioning_network']['ip_subnet']],
                 vxlan_id=fabric_dict['provisioning_network']['vlan_tag'],
                 ipam_fq_name=ipam.fq_name,
                 orch=self.orchestrator,
                 option='contrail',
                 address_allocation_mode='flat-subnet-only',
                 virtual_network_category='infra',
                 **kwargs)
        label = vn.vn_name
        tag_id = self.vnc_h.create_tag([label], 'label', label)
        self.vnc_h.set_tag('label', label, is_global=True, obj=vn.api_vn_obj)
        return ipam, vn, tag_id

    def create_server_object(self, fabric, fabric_dict):
        servers = list()
        ports = list()
        for name, intfs in list(fabric_dict['ztp'].items()):
            servers.append(self.vnc_h.create_node(name))
            for port in intfs:
                ports.append(self.vnc_h.create_port(name=port['name'],
                    mac_address=port['mac_address'], server=name,
                    tor_port=port['tor_port'], tor=port['tor'],
                    switch_id=port['switch_id']))
            self.vnc_h.add_node_profile(name, name+'-np')
        return servers, ports

    def create_server_node_profile(self, fabric, fabric_dict, label):
        cards = list(); hardwares = list(); node_profiles = list()
        for name, ports in list(fabric_dict['ztp'].items()):
            vendor = 'Dell'
            cards.append(self.vnc_h.create_card(name+'-card', label,
                [port['name'] for port in ports]))
            hardwares.append(self.vnc_h.create_hardware(name+'-hw'))
            self.vnc_h.add_card(card_name=name+'-card',
                                hardware_name=name+'-hw')
            node_profiles.append(self.vnc_h.create_node_profile(name+'-np',
                                vendor=vendor, np_type='end-system'))
            self.vnc_h.add_hardware(node_profile_name=name+'-np',
                                    hardware_name=name+'-hw')
        return cards, hardwares, node_profiles

    def assign_roles(self, fabric, devices, rb_roles=None, wait_for_finish=True):
        ''' eg: rb_roles = {device1: ['CRB-Access'], device2: ['CRB-Gateway', 'DC-Gateway']}'''
        rb_roles = rb_roles or dict()
        roles_dict = dict()
        for device in devices:
            roles_dict.update({device: self.get_role_from_inputs(device.name)})
        fq_name = ['default-global-system-config', 'role_assignment_template']
        payload = {'fabric_fq_name': fabric.fq_name, 'role_assignments': list()}
        for device, role in roles_dict.items():
            if role == 'leaf':
                # skip role assignment of leaf devices with Collapsed-l2
                # role in case of collapsed-spine topology.
                if rb_roles.get(device.name) == ['Collapsed-l2']:
                    continue
                routing_bridging_role = rb_roles.get(
                    device.name, ['CRB-Access'])
            elif role == 'pnf':
                routing_bridging_role = rb_roles.get(
                    device.name, ['PNF-Servicechain'])
            elif role == 'spine':
                routing_bridging_role = rb_roles.get(device.name, ['CRB-Gateway',
                    'Route-Reflector'])
            dev_role_dict = {'device_fq_name': ['default-global-system-config',
                                                device.name],
                             'physical_role': role,
                             'routing_bridging_roles': routing_bridging_role}
            payload['role_assignments'].append(dev_role_dict)
        for device_roles in payload['role_assignments']:
            if device_roles['physical_role'].lower() == 'pnf':
                continue
            device = device_roles['device_fq_name']
            self.vnc_h.associate_physical_role(device,
                device_roles['physical_role'])
            for role in device_roles['routing_bridging_roles']:
                if role.lower() in VALID_OVERLAY_ROLES:
                    self.vnc_h.associate_rb_role(device, role.lower())
        execution_id = self.vnc_h.execute_job(fq_name, payload)
        self.logger.info('Started assigning roles for %s'%devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name),
                execution_id)[0]
            assert status, 'job %s to assign roles failed'%execution_id
            #ToDo: Adding sleep since assign roles triggers internal playbook
            #which we are not able to track till completion
            time.sleep(60)
            return execution_id, status
        return execution_id, None

    @retry(delay=30, tries=30)
    def wait_for_job_to_finish(self, job_name, execution_id, start_time='now-10m'):
        ops_h = self.connections.ops_inspects[self.inputs.collector_ips[0]]
        table = 'ObjectJobExecutionTable'
        query = '(Messagetype=JobLog)'
        response = ops_h.post_query(table, start_time=start_time,
                                    end_time='now',
                                    select_fields=['MessageTS', 'Messagetype', 'ObjectLog'],
                                    where_clause=query)
        if response:
            for resp in response:
                dct = elem2dict(etree.fromstring(resp['ObjectLog']))
                log = dct['log_entry']['JobLogEntry']
                if log['name'] == job_name and \
                    log['execution_id'] == execution_id:
                    if log['status'].upper() == 'SUCCESS':
                        self.logger.debug('job %s with exec id %s finished'%(job_name, execution_id))
                        return (True, log)
                    elif log['status'].upper() == 'FAILURE':
                        assert False, 'job %s with exec id %s failed'%(job_name, execution_id)
            else:
                self.logger.warn('job %s with exec id %s hasnt completed'%(job_name, execution_id))
        else:
            self.logger.warn('Query failed for table ObjectJobExecutionTable. Will retry...')
        return (False, None)

    def change_role_config_params(self, prouters, snmp_configs=None,
             ntp_servers=None, dns_domain_name='juniper.net', dns_servers=None):
        for prouter in prouters:
            np_uuid = prouter.node_profile
            self.vnc_h.update_role_config_params(np_uuid,
                snmp_configs=snmp_configs,
                ntp_servers=ntp_servers,
                dns_domain_name=dns_domain_name,
                dns_servers=dns_servers)
        time.sleep(30)
        assert self.check_role_config_params(prouters, ntp_servers,
                                             dns_domain_name,
                                             dns_servers, snmp_configs)

    @retry(delay=5, tries=10)
    def check_role_config_params(self, devices, ntp_servers=None,
            dns_domain_name=None, dns_servers=None, snmp_configs=None):
        payload = {"config_type": "current", "config_filter": "all",
                   "compare_configurations": False}
        fq_name = ['default-global-system-config', 'show_config_template']
        device_list = [device.uuid for device in devices]
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        status, dct = self.wait_for_job_to_finish(':'.join(fq_name),
                                                  execution_id)
        if not status:
            return False
        log = str(dct)
        if (ntp_servers and ntp_servers[0] not in log):
            return False
        if dns_servers and dns_servers[0] not in log:
            return False
        if dns_domain_name and dns_domain_name not in log:
            return False
        if snmp_configs and snmp_configs["communities"][0]["name"] not in log:
            return False
        return True

    def create_bms(self, bms_name, **kwargs):
        self.logger.info('Creating bms %s'%bms_name)
        kwargs['fabric_fixture'] = kwargs.get('fabric_fixture') or self.fabric
        bms = self.useFixture(BMSFixture(
                              connections=self.connections,
                              name=bms_name,
                              ep_style=getattr(self, 'enterprise_style', True),
                              **kwargs))
        status, msg = bms.run_dhclient()
        assert status, 'DHCP failed to fetch address'
        bms.verify_on_setup()
        return bms

    def create_vpg(self, interfaces=None, **kwargs):
        fabric_fixture = kwargs.get('fabric_fixture') or self.fabric
        pifs = list()
        for interface in interfaces or []:
            pifs.append(['default-global-system-config',
                         interface['tor'], interface['tor_port']])
        vpg = self.useFixture(VPGFixture(
                              connections=self.connections,
                              fabric_name=fabric_fixture.name,
                              pifs=pifs,
                              **kwargs))
        return vpg

    def create_port_profile(self, **kwargs):
        return self.useFixture(PortProfileFixture(
                               connections=self.connections, **kwargs))

    def create_sc_profile(self, **kwargs):
        return self.useFixture(StormControlProfileFixture(
                               connections=self.connections, **kwargs))

    def hitless_upgrade_strategy(self, device_images, fabric, advanced_params=None,
                                 upgrade_mode='upgrade', wait_for_finish=True):
        payload = dict()
        payload['fabric_uuid'] = fabric.uuid
        payload['upgrade_mode'] = upgrade_mode
        payload['advanced_parameters'] = advanced_params or DEFAULT_UPGRADE_PARAMS
        device_list = list()
        images_devices_dict = defaultdict(list)
        for device, image in device_images.items():
            image_id = self.vnc_h.get_device_image(image).uuid
            images_devices_dict[image_id].append(device.uuid)
            device_list.append(device.uuid)
        payload['image_devices'] = [{'image_uuid': image_id,
                                     'device_list': devices}
            for image_id, devices in images_devices_dict.items()]
        fq_name = ['default-global-system-config', 'hitless_upgrade_strategy_template']
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        self.logger.info('Started hitless_upgrade_strategy %s' % device_list)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name), execution_id)
            if not status and upgrade_mode == 'upgrade':
                status = self.wait_for_job_to_finish(':'.join(fq_name), execution_id)
            assert status, 'job %s to hitless_upgrade_strategy failed' %(execution_id)
            return execution_id, status
        return execution_id, None

    def activate_maintenance_mode(self, device, fabric, mode=None,
                                  advanced_params=None, wait_for_finish=True):
        payload = dict()
        payload['mode'] = mode
        payload['fabric_uuid'] = fabric.uuid
        payload['device_uuid'] = device.uuid
        payload['advanced_parameters'] = advanced_params
        fq_name = ['default-global-system-config', 'maintenance_mode_activate_template']
        device_list = [device.uuid]
        execution_id = self.vnc_h.execute_job(fq_name, payload, device_list)
        self.logger.info('Started activate_maintenance_mode %s' % devices)
        if wait_for_finish:
            status = self.wait_for_job_to_finish(':'.join(fq_name), execution_id)
            assert status, 'job %s to activate_maintenance_mode failed' %(execution_id)
            return execution_id, status
        return execution_id, None
