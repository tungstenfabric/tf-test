from builtins import range
import os
import sys
import re
import time
from common.base import GenericTestBase
from common.connections import ContrailConnections
from common import isolated_creds
from vm_test import VMFixture
from vn_test import VNFixture
from tcutils.util import retry, get_ips_of_host
from string import Template
from tcutils.commands import ssh, execute_cmd, execute_cmd_out
from compute_node_test import ComputeNodeFixture
from common.vdns.base import BasevDNSTest
from tcutils.traffic_utils.scapy_traffic_gen import ScapyTraffic
from router_fixture import LogicalRouterFixture
from project_test import ProjectFixture
from time import sleep
from netaddr import IPNetwork, IPAddress
trafficdir = os.path.join(os.path.dirname(__file__), '../../tcutils/pkgs/Traffic')
sys.path.append(trafficdir)

class BaseL3Multihoming(GenericTestBase, BasevDNSTest):

    @classmethod
    def setUpClass(cls):
        super(BaseL3Multihoming, cls).setUpClass()
        cls.inputs.set_af('v4')
        cls.orch = cls.connections.orch
        cls.quantum_h = cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.vnc_lib = cls.connections.vnc_lib
        cls.agent_inspect = cls.connections.agent_inspect
        cls.cn_inspect = cls.connections.cn_inspect
        cls.analytics_obj = cls.connections.analytics_obj
        cls.api_s_inspect = cls.connections.api_server_inspect
        cls.vnc_h = cls.connections.orch.vnc_h
        cls.logger = cls.connections.logger
    # end setUpClass

    def verify_vrouter_agent_l3_multihoming_parameters(self):
        option_set = True
        if self.inputs.compute_ips:
           for compute_ip in self.inputs.compute_ips:
                compute_fix = ComputeNodeFixture(self.connections, compute_ip)
                vhost0_name = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'name')
                if vhost0_name != 'vhost0':
                   option_set = False
                   self.logger.error(
                   "vhost0 name is not set under VIRTUAL-HOST-INTERFACE section in contrail-vrouter-agent.conf on %s" %compute_ip)
                gateway = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'gateway')
                if not gateway:
                   option_set = False
                   self.logger.error(
                   "gateway is not set under VIRTUAL-HOST-INTERFACE section in contrail-vrouter-agent.conf on %s" %compute_ip)
                physical_interface = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface')
                if not physical_interface:
                   option_set = False
                   self.logger.error(
                   "Physical_interface is not set under VIRTUAL-HOST-INTERFACE in contrail-vrouter-agent.conf on %s" %compute_ip)
                loopback_ip = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'loopback_ip')
                if not loopback_ip:
                   option_set = False
                   self.logger.error(
                   "loopback_ip is not set under VIRTUAL-HOST-INTERFACE section in contrail-vrouter-agent.conf on %s" %compute_ip)
                physical_interface_addr = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface_addr')
                if not physical_interface_addr:
                   option_set = False
                   self.logger.error(
                   "Physical_interface_addr is not set under VIRTUAL-HOST-INTERFACE in contrail-vrouter-agent.conf on %s" %compute_ip)

                physical_interface_count = len(physical_interface.split(' '))
                physical_interface_addr_count = len(physical_interface_addr.split(' '))
                gateway_count = len(gateway.split(' '))
                if physical_interface_count:
                   if physical_interface_count != physical_interface_addr_count:
                      self.logger.error("Mismatch in number of physical interface and physical interface address %s" % compute_ip)
                      option_set = False
                   elif (physical_interface_count != gateway_count):
                      self.logger.error("Mismatch in number of physical interface and gateway address %s" % compute_ip)
                      option_set = False
                else:
                    self.logger.error("Physical interface not found on compute %s" % compute_ip)
                    option_set = False
        else:
           self.logger.error("No Computes Found")
           option_set = False
        return option_set
    # end verify_vrouter_agent_l3_multihoming_parameters

    def verify_vhost0_interface_on_l3mh_compute(self):
         vhost0_config = True
         get_mac_cmd = "ifconfig | grep vhost0 -A3 | grep ether | awk {\'print $2\'}"
         get_ip_cmd = "ip addr show vhost0| grep 'inet .*/.* brd ' | awk '{print $2}'"
         if self.inputs.compute_ips:
             for compute_ip in self.inputs.compute_ips:
                 mac = self.inputs.run_cmd_on_server(
                 compute_ip, get_mac_cmd)
                 if mac != "00:00:5e:00:01:00":
                     vhost0_config = vhost0_config and False
                     self.logger.error("vrrp mac not set for vhost0 interface on compute %s" ,compute_ip)
                 ip_addr = None
                 ip_addr = self.inputs.run_cmd_on_server(
                 compute_ip, get_ip_cmd)
                 if ip_addr:
                     vhost0_config = vhost0_config and False
                     self.logger.error("ip address is set for vhost0 interface on compute %s ip is %s" % (compute_ip, ip_addr))
         else:
             vhost0_config = vhost0_config and False
             self.logger.error("No Computes Found")
         if len(self.inputs.compute_ips) < 2:
              self.logger.error("At least 2 computes are required to run Feature Tests")
              vhost0_config = vhost0_config and False
         return vhost0_config
    #end verify_vhost0_interface_on_l3mh_compute

    def verify_physical_interfaces_and_routes_in_default_vrf_on_l3mh_compute(self):
         verify_intf = True
         vif_id = 0
         if self.inputs.compute_ips:
             for compute_ip in self.inputs.compute_ips:
                 status_down, err = self.inputs.verify_service_down(compute_ip, service='agent')
                 if status_down:
                     self.logger.error('agent is not in Active state: %s on compute %s' % (err, compute_ip))
                     verify_intf = False
                 compute_fix = ComputeNodeFixture(self.connections, compute_ip)
                 gateway = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'gateway')
                 physical_interface = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface')
                 physical_interface_addr = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'physical_interface_addr')
                 physical_interface_count = len(physical_interface.split(' '))

                 while(vif_id < physical_interface_count):
                     flag_cmd = "vif --get %s | awk {'print $4'} | grep Flags" % (vif_id)
                     type_cmd = "vif --get %s | awk {'print $1'} | grep Type" % (vif_id)
                     vif_flag = self.inputs.run_cmd_on_server(
                                    compute_ip, flag_cmd)
                     vif_type = self.inputs.run_cmd_on_server(
                                    compute_ip, type_cmd)
                     if "X" in vif_flag:
                         self.logger.error(
                         "Physical interface still set in cross connect mode for vif  %s on compute %s" % (vif_id, compute_ip))
                         verify_intf = False
                     elif "Physical" not in vif_type:
                         self.logger.error(
                         "Interface with index %s not of type Physical Interface on l3mh compute %s" % (vif_id, compute_ip))
                         verify_intf = False
                     prefix = physical_interface_addr.split(' ')[vif_id].split('/')[0]
                     physical_intf_route_list = self.get_route_nh_from_host(compute_ip, "0", prefix)
                     physical_intf_route = None
                     if physical_intf_route_list:
                         physical_intf_route = physical_intf_route_list[0]
                     if physical_intf_route:
                        if 'nh' in physical_intf_route.keys():
                            if physical_intf_route['nh']['type'] != "Receive":
                               self.logger.error(
                               "Nexthop for interface route with vrf id %s on compute %s not of type RECEIVE" % (vif_id, compute_ip))
                               verify_intf = False
                            if physical_intf_route['nh']['encap_oif_id'] != str(physical_interface_count):
                               self.logger.error(
                               "Nexthop for interface route with vrf id %s on compute %s does not point to vhost0"
                                % (vif_id, compute_ip))
                               verify_intf = False
                            if physical_intf_route['prefix_len'] != '32':
                               self.logger.error(
                               "Route prefix length mismatch for prefix %s on compute %s"
                                % (prefix, compute_ip))
                               verify_intf = False
                        else:
                            self.logger.error("Invalid nh for route prefix %s on compute %s" %(prefix, compute_ip))
                            verify_intf = verify_intf and False 
                     else:
                        self.logger.error(
                        "No Receive Route for interface address on compute %s " %  (compute_ip))
                        verify_intf = False
                     # Verify Resolve nexthop is set for subnet routes for each fabric interfaces
                     ip_prefix = physical_interface_addr.split(' ')[vif_id].split('/')[0]
                     prefix_len = physical_interface_addr.split(' ')[vif_id].split('/')[1]
                     ip_prefix = ip_prefix.split('.')
                     subnet_prefix = ('.').join(ip_prefix[:3]) + ".0"
                     physical_intf_resolve_route_list = self.get_route_nh_from_host(compute_ip, "0", subnet_prefix)
                     physical_intf_resolve_route = None
                     if physical_intf_resolve_route_list:
                         physical_intf_resolve_route = physical_intf_resolve_route_list[0]
                     if physical_intf_resolve_route:
                        if 'nh' in physical_intf_resolve_route.keys():
                            if physical_intf_resolve_route['nh']['type'] != 'Resolve':
                               self.logger.error(
                               "Nexthop for interface route with vif id %s on compute %s not of type Resolve" % (vif_id, compute_ip))
                               verify_intf = False
                            if physical_intf_resolve_route['prefix_len'] != '24':
                               self.logger.error(
                               "Route prefix length mismatch for prefix %s on compute %s"
                                % (subnet_prefix, compute_ip))
                               verify_intf = False
                        else:
                            self.logger.error("Invalid nh for route prefix %s on compute %s" %(subnet_prefix, compute_ip))
                            verify_intf = verify_intf and False
                     else:
                        self.logger.error(
                        "No subnet route with resolve nh for vrf id %s on compute %s does not point to vhost0" % (vif_id, compute_ip))
                        verify_intf = False

                     # Verify Arp nexthop for gateway routes
                     gw_ip_prefix = gateway.split(' ')[vif_id].split('/')[0]
                     gw_route_list = self.get_route_nh_from_host(compute_ip, "0", gw_ip_prefix)
                     gw_route = None
                     if gw_route_list:
                         gw_route = gw_route_list[0]
                     if gw_route:
                        if 'nh' in gw_route.keys():
                            if gw_route['nh']['type'] != 'Encap':
                                self.logger.error("Arp nexthop not found for gw route %s on compute %s" % (gw_route, compute_ip))
                                verify_intf = False
                            if gw_route['prefix_len'] != '32':
                               self.logger.error(
                               "Route prefix length mismatch for prefix %s on compute %s"
                                % (gw_ip_prefix, compute_ip))
                               verify_intf = False
                        else:
                            self.logger.error("Invalid nh for route prefix %s on compute %s" %(gw_ip_prefix, compute_ip))
                            verify_intf = verify_intf and False
                     else:
                         self.logger.error("Gw route for prefix %s not found on compute" % (gw_route, compute_ip))
                         verify_intf = False

                     # Verify L2 Receive Route for each physical interface mac
                     get_intf_mac_cmd = "ifconfig | grep %s -A3 | grep ether | awk {\'print $2\'}" % physical_interface.split(' ')[vif_id]
                     intf_mac = self.inputs.run_cmd_on_server(
                                     compute_ip, get_intf_mac_cmd)
                     intf_mac_bytes = intf_mac.split(':')
                     vr_intf_mac = ''
                     for byte in intf_mac_bytes:
                         byte = byte.lstrip('0')
                         if byte == '':
                            byte = '0'
                         vr_intf_mac = vr_intf_mac + byte + ':'
                     vr_intf_mac = vr_intf_mac.rstrip(':')
                     nh_id = self.inputs.run_cmd_on_server(compute_ip,
                                 "contrail-tools rt --dump 0 --family bridge | grep %s | awk '{print $5}' " % (vr_intf_mac))
                     nh_type = self.inputs.run_cmd_on_server(compute_ip,
                                 "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" % nh_id)
                     if 'L2' not in nh_type:
                         self.logger.error("L2 route for Mac %s does not have nh l2 receive on compute %s" % (intf_mac, compute_ip))
                         verify_intf = False
                     # Proceed to next physical interface
                     vif_id+=1
             # Verify nexthop for default route is type composite
             def_rt_list = self.get_route_nh_from_host(compute_ip, "0", "0.0.0.0")
             def_rt = None
             if def_rt_list:
                 def_rt = def_rt_list[0]
             if def_rt:
                 if 'nh_id' in def_rt.keys():
                     nh_type = self.inputs.run_cmd_on_server(compute_ip,
                                 "contrail-tools  nh --get %s | grep Type | awk {'print $2'}" % def_rt['nh_id'])
                     if 'Composite' not in nh_type:
                         self.logger.error("Composite nexthop not found for def route on compute %s" % (compute_ip))
                         verify_intf = False
                 else:
                     self.logger.error("Invalid nh for route prefix %s on compute %s" %("0.0.0.0", compute_ip))
                     verify_intf = verify_intf and False
             else:
                 self.logger.error("Default route not found in vrf 0 on compute" % (compute_ip))
                 verify_intf = False

             # Verify Receive route for loopback ip address
             loopback_ip = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'loopback_ip')
             loopback_ip_prefix = loopback_ip.split('/')[0]
             loopback_route_list = self.get_route_nh_from_host(compute_ip, "0", loopback_ip_prefix)
             loopback_route = None
             if loopback_route_list:
                 loopback_route = loopback_route_list[0]
             if loopback_route:
                 if 'nh' in loopback_route.keys():
                     if 'Receive' not in loopback_route['nh']['type']:
                         self.logger.error(
                         "Receive nh not found for loopback rt prefix %s on compute %s" % (loopback_ip_prefix, compute_ip))
                         verify_intf = False
                 else:
                     self.logger.error("Invalid nh for route prefix %s on compute %s" %(loopback_ip_prefix, compute_ip))
                     verify_intf = verify_intf and False
             else:
                 self.logger.error("Route for loopback prefix %s not found on compute %s" % (loopback_ip_prefix, compute_ip))
                 verify_intf = False
         else:
             verify_intf = False

         return verify_intf
    #end verify_physical_interfaces_and_routes_in_default_vrf_on_l3mh_compute

    def verify_compute_loopbackip_and_controller_connectivity(self):
        result = True
        expected_result = ' 0% packet loss'
        if self.inputs.compute_ips:
           for compute_ip in self.inputs.compute_ips:
                compute_fix = ComputeNodeFixture(self.connections, compute_ip)
                loopback_ip_local = compute_fix.get_option_value('VIRTUAL-HOST-INTERFACE', 'loopback_ip')
                control_node_ips = []
                control_node_ips = compute_fix.get_option_value('CONTROL-NODE', 'servers').split(' ')
                for control_node_ip in control_node_ips:
                    control_node_ip = control_node_ip.split(':')[0]
                    cmd = 'ping -I %s -c 3 %s' % (loopback_ip_local, control_node_ip)
                    output = compute_fix.execute_cmd(cmd, container=None)
                    if expected_result not in output:
                         self.logger.error(
                         "ping to control node ip %s failed from compute %s " % (control_node_ip, compute_ip))
                         result = result and False
                for ip in self.inputs.compute_ips:
                    compute_fix_remote = ComputeNodeFixture(self.connections, ip)
                    loopback_ip = compute_fix_remote.get_option_value('VIRTUAL-HOST-INTERFACE', 'loopback_ip')
                    if not loopback_ip:
                        self.logger.error(
                        "loopback_ip is not set under VIRTUAL-HOST-INTERFACE section in contrail-vrouter-agent.conf on %s" %ip)
                        result = result and False
                    else:
                        cmd = 'ping -I %s -c 3 %s' % (loopback_ip_local, loopback_ip)
                        out = compute_fix.execute_cmd(cmd, container=None)
                        if expected_result not in out:
                            self.logger.error(
                            "Ping to loopback_ip %s from local compute %s to remote compute %s Failed"
                            % (loopback_ip, compute_ip, ip))
                            #result = result and False
        else:
            self.logger.error("Test Failed no computes found")
            result = result and False
        return result

    def start_tcpdump(self, server_ip, src_ip, tap_intf, filters=None):
        session = ssh(server_ip,self.inputs.host_data[server_ip]['username'],self.inputs.host_data[server_ip]['password'])
        pcap = '/tmp/%s.pcap' % tap_intf
        if (filters is not None):
            pcap = '/tmp/l2%s.pcap' % tap_intf
            cmd = "sudo tcpdump -nei %s " % (tap_intf)
            temp = " -w %s" % (pcap)
            cmd = cmd + filters + temp
        else:
            cmd = "sudo tcpdump -ni %s src %s and tcp -w %s" % (tap_intf, str(src_ip), pcap)
        self.logger.info("Starting tcpdump to capture the packets on server %s" % (server_ip))
        cmd = str(cmd)
        execute_cmd(session, cmd, self.logger)
        return pcap, session

    def send_tcp_traffic(self, vm_fix,
                         src_ip,
                         dst_ip,
                         count=10,
                         **kwargs):
        sport = kwargs.get('sport', 1500)
        dport = kwargs.get('dport_range', 10001)
        params = {}
        params['ip'] = {'src': src_ip , 'dst': dst_ip}
        params['tcp'] = {'sport': sport, 'dport': dport}
        params['count'] = count
        params['interval'] = 0
        params['mode'] = 'L3'
        scapy_obj = ScapyTraffic(vm_fix, **params)
        scapy_obj.start()
    #end send_tcp_traffic

    def send_l2_traffic(self,
                        src_vm_fixture,
                        src_mac,
                        dst_mac,
                        iface):
        '''
            Sends L2 traffic from VM src_vm_fixture:
                mandatory args:
                    1. src_vm_fixture: send l2 traffic from this VM
                    2. src_mac: mac address of src VM
                    3. dst_mac: mac address of dst VM
                    4. interface: use this interface to send traffic
        '''
        python_code = Template('''
from scapy.all import *
payload = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
a=Ether(src='$mac1',dst='$mac2')/payload
sendp(a, count=10, inter=0, iface='$iface')
             ''')
        python_code = python_code.substitute(mac1=src_mac,mac2=dst_mac,iface=iface)
        return src_vm_fixture.run_python_code(python_code)
    #end send_l2_traffic

    def get_ipv6_address(self, intf, pod):
        cmd = ["ifconfig " + intf + " | grep Global"]
        output = pod.run_cmd_on_vm(cmd)
        ip6 = re.search(
            r'inet6\s+addr\s*:\s*(\S*)',
            output['ifconfig eth0 | grep Global'])
        ip6_addr = ip6.group(1)
        ipv6_addr = ip6_addr.split("/")
        return ipv6_addr[0]
    #end get_ipv6_address

    def get_route_nh_from_host(self, compute_ip, vrf_id, prefix):
        #cmd = "rt --dump %s | grep %s | awk \'{print $5}\'" %(vrf_id, prefix)
        rt_dict = {}
        nh_dict ={}
        rt_keys = ['prefix','prefix_len','label','label_flags','nh_id']
        nh_keys = ['oif', 'flags', 'dip','type']
        cmd = "contrail-tools rt --dump %s 2>/dev/null | grep %s " %(vrf_id, prefix)
        output = self.inputs.run_cmd_on_server(compute_ip, cmd)
        if output:
            rt_values = output.split()[:-1]
            rt_dict = dict(zip(rt_keys,rt_values))
            if int(rt_dict['nh_id']) > 0:
                nh_cmd = 'contrail-tools nh --get %s'%rt_dict['nh_id']
                output = self.inputs.run_cmd_on_server(compute_ip, nh_cmd)
                if output:
                    output = output.split()
                    for out in output:
                        for key in nh_keys:
                            if key in out.lower():
                                nh_dict[key] = out.split(':')[1]
                    nh_dict['id'] = rt_dict['nh_id']
                    if nh_dict.get('oif'):
                        nh_dict['encap_oif_id'] = nh_dict.pop('oif')
                    if nh_dict.get('dip'):
                        nh_dict['tun_dip'] = nh_dict.pop('dip')
                    if nh_dict.get('type'):
                        if nh_dict['type'] == 'Tunnel':
                            nh_dict['flags'] = 'TUNNEL'
                rt_dict['nh'] = nh_dict
            return [rt_dict]

        return []

    def create_logical_router(self, vn_fixtures, vni=None, devices=None,
                              **kwargs):
        vn_ids = [vn.uuid for vn in vn_fixtures]
        vni = vni or str(get_random_vxlan_id(min=10000))
        self.logger.info('Creating Logical Router with VN uuids: %s, VNI %s'%(
            vn_ids, vni))
        lr = self.useFixture(LogicalRouterFixture(
            connections=self.connections,
            connected_networks=vn_ids, vni=vni, vxlan_enabled=True,
            **kwargs))
        return lr

    def allow_default_sg_to_allow_all_on_project(self, project_name):

        self.project_fixture = ProjectFixture(
                project_name=self.inputs.project_name,
                connections=self.connections)
        self.project_fixture.read()
        self.logger.info(
            'Default SG to be edited for allow all on project: %s' %
            project_name)
        self.project_fixture.set_sec_group_for_allow_all(
            project_name, 'default')
    # end allow_default_sg_to_allow_all_on_project

    def is_dpdk_compute(self, compute_ip):
        cmd = "docker ps -a | grep dpdk"
        compute_fix = ComputeNodeFixture(self.connections, compute_ip)
        ret = compute_fix.execute_cmd(cmd, None)
        if (ret != ""):
            return True
        else:
            return False
    # end is_dpdk_compute

    def get_qfx_device_creds_from_port_ip(self, ip):
        device_creds = {}
        l3_mh_configuration = \
            self.inputs.config['test_configuration'].get('l3_mh_configuration',None)
        if l3_mh_configuration:
            physical_routers = l3_mh_configuration.get('physical_routers', None)
        if physical_routers:
            for device in physical_routers.keys():
                if IPAddress(ip) in IPNetwork(physical_routers[device].get('cidr', None)):
                     device_creds['mgmt_ip'] = physical_routers[device]['mgmt_ip']
                     device_creds['ssh_username'] = physical_routers[device]['ssh_username']
                     device_creds['ssh_password'] = physical_routers[device]['ssh_password']
        return device_creds
    # end get_qfx_device_creds_from_port_ip
