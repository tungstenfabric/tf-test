from builtins import range
import re
import time
from common.base import GenericTestBase
from common.connections import ContrailConnections
from common import isolated_creds
from vm_test import VMFixture
from vn_test import VNFixture
from tcutils.util import retry
from string import Template
from tcutils.commands import ssh, execute_cmd, execute_cmd_out

class BaseMacIpLearningTest(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(BaseMacIpLearningTest, cls).setUpClass()
        cls.inputs.set_af('v4')
        cls.orch = cls.connections.orch
        cls.quantum_h = cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.vnc_lib = cls.connections.vnc_lib
        cls.agent_inspect = cls.connections.agent_inspect
        cls.cn_inspect = cls.connections.cn_inspect
        cls.analytics_obj = cls.connections.analytics_obj
        cls.api_s_inspect = cls.connections.api_server_inspect
    # end setUpClass

    def get_intf_address(self, intf, pod):
        """
        Routine if to derive the ip address of the interface in a multi interface pod
        :param intf: name of the interface for which te ip address needed to be reutrned
        :param pod: name of the pod
        :return: ipv4 address of the interface
        """
        cmd = ["ifconfig " + intf + " | grep inet"]
        output = pod.run_cmd_on_vm(cmd)
        ip = re.search(
            r'inet\s+addr\s*:\s*(\d+.\d+.\d+.\d+)',
            output['ifconfig eth0 | grep inet'])
        ip_addr = ip.group(1)
        return ip_addr
    # end get_intf_address

    def attach_shc_to_vn(self, shc, vn_fixture):
        '''
        Attach the Health Check to VN
        '''
        result = vn_fixture.attach_shc(shc.uuid)
        return result
    # end attach_shc_to_vn

    def detach_shc_from_vn(self, shc, vn_fixture):
        '''
        Detach the Health Check from VN
        '''
        result = vn_fixture.detach_shc(shc.uuid)
        return result
    # end detach_shc_from_vn

    def check_bfd_packets(self, vm, vn):
        interface = vm.tap_intf[vn.vn_fq_name]['name']
        ip = self.inputs.host_data[vm.vm_node_ip]['host_ip']
        session = ssh(ip,self.inputs.host_data[ip]['username'],self.inputs.host_data[ip]['password'])
        cmd = "sudo timeout 30 tcpdump -nei %s ip | grep BFD" % (interface)
        self.logger.info("Starting tcpdump to capture the BFD packets on %s in server %s" % (interface, ip))
        out, err = execute_cmd_out(session, cmd, self.logger)
        result = False
        if out:
            result = True
        return result
    # end check_bfd_packets

    def config_bfd_on_vsrx(
            self,
            src_vm=None,
            dst_vm=None,
            target_ip=None,
            gw_ip=None,
            lo_ip=None):
        '''
        Pass BFD config to the vSRX
        '''

        cmdList = []
        cmdList.extend(('set system arp aging-timer 1',
                        'deactivate interfaces ge-0/0/1 unit 0 family inet dhcp',
                        'set interfaces ge-0/0/1 unit 0 family inet address %s' % target_ip,
                        'set interfaces ge-0/0/1 mac 00:1b:44:11:3a:b7',
                        'set interfaces lo0 unit 57 family inet address %s/32' % lo_ip,
                        'set routing-options static route %s/32 next-hop %s' % (
                            gw_ip, gw_ip),
                        'set routing-options static route %s/32 bfd-liveness-detection minimum-interval 1000' % gw_ip))

        cmd_string = (';').join(cmdList)
        assert self.set_config_via_netconf(src_vm, dst_vm, cmd_string, timeout=200,
                                           device='junos', hostkey_verify="False"), "Cmds not configured thru Netconf in vsrx"
    # end config_bfd_on_vsrx

    def remove_target_ip_on_vsrx(
            self,
            src_vm=None,
            dst_vm=None,
            target_ip=None):
        '''
        Configures and deletes target ip on ge-0/0/1 intf on vSRX
        '''
        cmd_string = "delete interfaces ge-0/0/1 unit 0 family inet address %s" % target_ip
        assert self.set_config_via_netconf(src_vm, dst_vm, cmd_string, timeout=200,
                                           device='junos', hostkey_verify="False"), 'Could not delete target ip on ge-0/0/1 intf thru Netconf'
    # end remove_target_ip_on_vsrx

    def get_intf_mac_addr(
            self,
            src_vm=None,
            dst_vm=None,
            intf="ge-0/0/1"):
        '''
        Returns intf mac addr on vSRX
        '''
        cmd_string = "show interfaces %s" % intf
        output = self.get_config_via_netconf(src_vm, dst_vm, cmd_string, timeout=200,
                                             device='junos', hostkey_verify="False")
        split_output = re.split("Current address: ", output, 1)
        mac = split_output[1].split(",")[0]
        return mac
    # end get_intf_mac_addr

    def check_bfd_state(
            self,
            src_vm=None,
            dst_vm=None,
            addr=None):
        '''
        Returns intf mac addr on vSRX
        '''
        cmd_string = "show bfd session address %s" % addr
        output = self.get_config_via_netconf(src_vm, dst_vm, cmd_string, timeout=200,
                                             device='junos', hostkey_verify="False")
        if "Up" in output:
            return "Up"
        elif "Down" in output:
            return "Down"
        else:
            return None
    # end check_bfd_state
