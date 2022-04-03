import re
from common.base import GenericTestBase
from common.connections import ContrailConnections
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

    def get_intf_address(self, intf, pod, v6=False):
        """
        Routine if to derive the ip address of the interface in a multi interface pod
        :param intf: name of the interface for which te ip address needed to be reutrned
        :param pod: name of the pod
        :return: ipv4/ global ipv6 address of the interface
        """
        if v6:
            cmd = ["ifconfig " + intf + " | grep Global"]
            output = pod.run_cmd_on_vm(cmd)
            ip6 = re.search(
                 r'inet6\s+addr\s*:\s*(\S*)',
                 output["ifconfig " + intf + " | grep Global"])
            if not ip6:
                ip6 = re.search(
                    r'inet6\s*(\S*)',
                    output["ifconfig " + intf + " | grep Global"])
            ip6_addr = ip6.group(1)
            return ip6_addr
        cmd = ["ifconfig " + intf + " | grep inet"]
        output = pod.run_cmd_on_vm(cmd)
        ip = re.search(
            r'inet\s+addr\s*:\s*(\d+.\d+.\d+.\d+)',
            output["ifconfig " + intf + " | grep inet"])
        if not ip:
            ip = re.search(
                r'inet\s*(\d+.\d+.\d+.\d+)',
                output["ifconfig " + intf + " | grep inet"])
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

    def config_bfd_on_crpd(
            self,
            vm,
            gw_ip,
            containerIP,
            lo_ip='100.100.100.100',
            container_name='crpd01'):
        '''
        Set config on the cRPD Container
        '''
        cmd = ['docker exec %s cli -c\
            "edit;\
                set interfaces eth0 unit 0 family inet address %s;\
                    set interfaces lo0 unit 0 family inet address %s;\
                        set routing-options static route 0.0.0.0/0 next-hop %s;\
                            set routing-options static route 0.0.0.0/0 bfd-liveness-detection minimum-interval 300;\
                                commit"' \
                                    % (container_name, containerIP, lo_ip, gw_ip)]

        out = vm.run_cmd_on_vm(cmd, as_sudo=True)
    # end config_bfd_on_crpd    
    
    def get_docker_image(
            self,
            vm,
            image_name='crpd'):
        '''
        Get cRPD Container Image
        '''
        cmd = ['docker images | grep %s' % image_name]
        out = vm.run_cmd_on_vm(cmd, as_sudo=True)
        for val in out.values():
            image = val.split()[1]
        return image

    # End of get_crpd_image

    def create_crpd_container(
            self,
            vm,
            container_ip,
            network_name='ipvlannet',
            container_name='crpd01'):
        '''
        Create cRPD Container
        '''
        cmds = ['sudo docker volume create %s-config &&'
                'sudo docker volume create %s-varlog' % (container_name, container_name)]
        vm.run_cmd_on_vm(cmds, as_sudo=True)
        
        cmd2 = ['docker run --rm --detach --name %s -h %s --net=%s --ip=%s --privileged -v %s-config:/config -v %s-varlog:/var/log -it crpd:%s' % (container_name, container_name, network_name, container_ip, container_name, container_name, self.get_docker_image(vm))]

        out = vm.run_cmd_on_vm(cmd2, as_sudo=True)

    # End create_crpd_container

    def delete_crpd_container(
            self,
            vm,
            container_name='crpd01'):
        '''
        Delete cRPD Container
        '''
        cmd2 = ['docker container rm -f %s' % container_name]
        out = vm.run_cmd_on_vm(cmd2, as_sudo=True)

        cmds = ['sudo docker volume rm %s-config &&'
                'sudo docker volume rm %s-varlog' % (container_name, container_name)]
        vm.run_cmd_on_vm(cmds, as_sudo=True)

    # End create_crpd_container   
 
    def create_crpd_network(
            self,
            vm,
            subnet,
            gateway,
            name='ipvlannet',
            ipvlan_mode=None):
        '''
        Create cRPD Network
        '''
        if ipvlan_mode:
            cmd1 = ['docker network create -d ipvlan -o ipvlan_mode=%s --subnet=%s --gateway=%s -o parent=eth0 %s' % (ipvlan_mode, subnet, gateway, name)]
        else:
            cmd1 = ['docker network create -d ipvlan --subnet=%s --gateway=%s -o parent=eth0 %s' % (subnet, gateway, name)]

        out = vm.run_cmd_on_vm(cmd1, as_sudo=True)

    # End create_crpd_network
     
    def delete_crpd_network(
            self,
            vm,
            name='ipvlannet'):
        '''
        Create cRPD Network
        '''
        cmd1 = ['docker network rm %s' % (name)]

        out = vm.run_cmd_on_vm(cmd1, as_sudo=True)

    # End create_crpd_network
 
    def get_bfd_state_crpd(
            self,
            vm,
            container_name='crpd01'):
        '''
        Returns intf mac addr on vSRX
        '''
        cmd = ['docker exec %s cli -c "show bfd session"' % container_name]
        output = vm.run_cmd_on_vm(cmd, as_sudo=True)
        for var in output.values():
            output = var.split()
        if "Up" in output:
            return "Up"
        elif "Down" in output:
            return "Down"
        else:
            return None
    # end check_bfd_state

    def ping_from_crpd_container(
            self,
            vm,
            dest_ip,
            count='3',
            container_name='crpd01'):
        '''
        Ping from the cRPD Container
        '''
        cmd = ['docker exec -it %s ping %s -c %s' % (container_name, dest_ip, count)]
        output = vm.run_cmd_on_vm(cmd, as_sudo=True)
        for var in output.values():
            output = var.split(',')
        if " 100% packet loss" in output:
            return False
        else:
            return True

    # end ping_from_crpd_container
    
