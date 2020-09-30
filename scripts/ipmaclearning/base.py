from builtins import range
import re
from common.base import GenericTestBase
from common.connections import ContrailConnections
from common import isolated_creds
from vm_test import VMFixture
from vn_test import VNFixture
from tcutils.util import retry

class BaseIpMacLearningTest(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(BaseIpMacLearningTest, cls).setUpClass()
        cls.inputs.set_af('v4')
        cls.orch = cls.connections.orch
        cls.quantum_h= cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.vnc_lib= cls.connections.vnc_lib
        cls.agent_inspect= cls.connections.agent_inspect
        cls.cn_inspect= cls.connections.cn_inspect
        cls.analytics_obj=cls.connections.analytics_obj
        cls.api_s_inspect = cls.connections.api_server_inspect
    #end setUpClass

    def get_intf_address(self,intf,pod):
        """
        Routine if to derive the ip address of the interface in a multi interface pod
        :param intf: name of the interface for which te ip address needed to be reutrned
        :param pod: name of the pod
        :return: ipv4 address of the interface
        """
        cmd = ["ifconfig "+intf+" | grep inet"]
        output = pod.run_cmd_on_vm(cmd)
        ip = re.search('inet\s+addr\s*:\s*(\d+.\d+.\d+.\d+)', output['ifconfig eth0 | grep inet'])
        ip_addr = ip.group(1)
        return ip_addr

    @retry(delay=5, tries=20)
    def set_config_via_netconf_ipmaclearning(self, dst_vm, cmd_string, timeout=10, device='junos', hostkey_verify="False", reboot_required=False):
        python_code = Template('''
from ncclient import manager
conn = manager.connect(host='$ip', username='$username', password='$password',timeout=$timeout, device_params=$device_params, hostkey_verify=$hostkey_verify)
conn.lock()
send_config = conn.load_configuration(action='set', config=$cmdList)
check_config = conn.validate()
compare_config = conn.compare_configuration()
conn.commit()
'$reboot_cmd'
conn.unlock()
conn.close_session()
        ''')
        if hostkey_verify == 'False':
            hostkey_verify = bool(False)
        timeout = int(timeout)
        if device == 'junos':
            device_params = {'name': 'junos'}
        cmdList = cmd_string.split(';')
        if reboot_required:
            reboot_cmd='conn.reboot()'
        else:
            reboot_cmd=' '
        python_code = python_code.substitute(ip=str(dst_vm.vm_ip), username=str(dst_vm.vm_username), password=str(
            dst_vm.vm_password), device_params=device_params, cmdList=cmdList, timeout=timeout, hostkey_verify=hostkey_verify, reboot_cmd=reboot_cmd)
        assert dst_vm.wait_for_ssh_on_vm(port='830')
        op = dst_vm.run_python_code(python_code)
        if op != None:
            return False
        else:
            return True
    # end set_config_via_netconf

    def config_bfd_on_vsrx(
            self,
            mac=None,
            intf_ip=None,
            dst_vm=None,
            gw_ip=None,
            lo_ip=None): 
        ''' 
        Pass BFD config to the vSRX
        ''' 
        cmdList = []
        cmdList.extend(('delete interfaces ge-0/0/0 unit 0 family inet dhcp',
                        'set interfaces ge-0/0/0 mac %s' % mac,
                        'set interfaces ge-0/0/0 unit 0 family inet address %s' % intf_ip,
                        'set interfaces lo0 unit 57 family inet address %s/32' % lo_ip,
                        'set routing-options static route %s/32 next-hop %s' % (gw_ip, gw_ip),
                        'set routing-options static route %s/32 bfd-liveness-detection minimum-interval 1000' % gw_ip,
                        'set bfd traceoptions file bfd-trace',
                        'set bfd traceoptions flag all'))
        cmd_string = (';').join(cmdList)
        assert self.set_config_via_netconf_ipmaclearning(dst_vm, cmd_string, timeout=10,
                                           device='junos', hostkey_verify="False"), 'Could not configure BFD thru Netconf'
    # end config_bfd_on_vsrx

    def remove_target_ip_mac_on_vsrx(
            self,
            dest_vm=None,
            mac=None,
            intf_ip=None):
        ''' 
        Deletes mac and ip of ge-0/0/0 intf on vSRX
        ''' 
        cmdList = []
        cmdList.extend(('delete interfaces ge-0/0/0 mac %s' % mac,
                        'delete interfaces ge-0/0/0 unit 0 family inet address %s' % intf_ip))
        cmd_string = (';').join(cmdList)
        assert self.set_config_via_netconf_ipmaclearning(dst_vm, cmd_string, timeout=10,
                     device='junos', hostkey_verify="False"), 'Could not remove ip and mac from ge-0/0/0 intf thru Netconf'
    # end remove_target_ip_mac_on_vsrx

