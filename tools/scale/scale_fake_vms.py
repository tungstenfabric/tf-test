from vnc_api.vnc_api import *
import argparse
import random
import socket
import struct
import sys
import time
from netaddr import *
alloc_addr_list = list()

class VNC(object):
    def __init__(self, username, password, tenant, ip, port, auth_host):
        self.vnc = VncApi(api_server_host=ip,
                          api_server_port=port,
                          username=username,
                          password=password,
                          tenant_name=tenant,
                          auth_host=auth_host)
        self.project_fqname = ['default-domain', tenant]
        self.vn_obj = dict()
        self.vm_obj = dict()
        self.port_obj = dict()

    def get_project_id(self):
        return self.vnc.fq_name_to_id('project', self.project_fqname)

    def create_network(self, vn_name, mask=16):
        ''' Create virtual network using VNC api '''
        cidr = get_random_cidr(mask=mask).split('/')[0]
        vn_obj = VirtualNetwork(vn_name, fq_name=self.project_fqname+[vn_name],
                                parent_type='project')
        vn_obj.add_network_ipam(NetworkIpam(),
                                VnSubnetsType([IpamSubnetType(
                                subnet=SubnetType(cidr, mask))]))
        uuid = self.vnc.virtual_network_create(vn_obj)
        self.vn_obj[uuid] = vn_obj
        return uuid

    def delete_network(self, vn_name):
        try:
            self.vnc.virtual_network_delete(fq_name=self.project_fqname+[vn_name])
        except NoIdError as e:
            print e

    def create_port(self, port_name, vn_id, vm_id):
        ''' Create Port through VNC api '''
        port_obj = VirtualMachineInterface(port_name, fq_name=self.project_fqname+[port_name],
                                           parent_type='project')
        port_obj.add_virtual_network(self.vn_obj[vn_id])
        port_obj.add_virtual_machine(self.vm_obj[vm_id])
        vmi_id = self.vnc.virtual_machine_interface_create(port_obj)
        self.port_obj[vmi_id] = port_obj
        iip_obj = InstanceIp(name=port_name)
        iip_obj.add_virtual_network(self.vn_obj[vn_id])
        iip_obj.add_virtual_machine_interface(port_obj)
        iip_id = self.vnc.instance_ip_create(iip_obj)
        iip_obj = self.vnc.instance_ip_read(id=iip_id)
        port_obj = self.vnc.virtual_machine_interface_read(id=vmi_id)
        return port_obj, iip_obj

    def delete_port(self, port_name):
        try:
            self.vnc.instance_ip_delete(fq_name=[port_name])
            self.vnc.virtual_machine_interface_delete(fq_name=self.project_fqname+[port_name])
        except NoIdError as e:
            print e

    def create_vm(self, vm_name):
        vm_obj = VirtualMachine(vm_name)
        uuid = self.vnc.virtual_machine_create(vm_obj)
        self.vm_obj[uuid] = vm_obj
        return uuid

    def delete_vm(self, vm_name):
        try:
            self.vnc.virtual_machine_delete(fq_name=[vm_name])
        except NoIdError as e:
            print e

class ScaleTest(object):
    def __init__ (self, args):
        self.obj = VNC(args.username,
                       args.password,
                       args.tenant,
                       args.api_server_ip,
                       args.api_server_port,
                       args.keystone_ip)
        self._args = args

    def create(self):
        create_cmds = list()
        delete_cmds = list()
        port_ctrl = 'vrouter-port-control --tx_vlan_id=-1 --rx_vlan_id=-1'
        port_ctrl += ' --ipv6_address="" --port_type=NovaVMPort'
        port_ctrl += ' --vif_type=Vrouter --vm_project_uuid=%s'%self.obj.get_project_id()
        for vn_index in range(self._args.n_vns):
            vn_name = 'scale-test-VN-%s'%vn_index
            vn_id = self.obj.create_network(vn_name=vn_name)
            for vm_index in range(self._args.n_vms):
                vm_name = '%s-VM-%s'%(vn_name, vm_index)
                vm_id = self.obj.create_vm(vm_name=vm_name)
                vmi_obj, iip_obj = self.obj.create_port(vm_name, vn_id, vm_id)
                tap_name = 'tap%s'%(str(vmi_obj.uuid)[:11])
                mac_addr = vmi_obj.virtual_machine_interface_mac_addresses.mac_address[0]
                ip_addr = iip_obj.instance_ip_address
                cmd = 'ip tuntap add %s mode tap;'%tap_name
                cmd += 'ip link set dev %s address %s;'%(tap_name, mac_addr)
                cmd += 'ip link set dev %s up'%tap_name
                create_cmds.append(cmd)
                cmd = '%s --oper=add --uuid=%s --instance_uuid=%s --vn_uuid=%s --ip_address=%s\
                       --vm_name=%s --mac=%s --tap_name=%s'%(port_ctrl, vmi_obj.uuid, vm_id,
                       vn_id, ip_addr, vm_name, mac_addr, tap_name)
                create_cmds.append(cmd)
                cmd = 'ip link delete dev %s'%tap_name
                delete_cmds.append(cmd)
                cmd = 'vrouter-port-control --oper=delete --uuid=%s'%vmi_obj.uuid
                delete_cmds.append(cmd)
        with open(self._args.filename+'-create', 'w') as create_fp:
            create_fp.write('\n'.join(create_cmds))
        with open(self._args.filename+'-delete', 'w') as delete_fp:
            delete_fp.write('\n'.join(delete_cmds))

    def cleanup(self):
        for vn_index in range(self._args.n_vns):
            vn_name = 'scale-test-VN-%s'%vn_index
            for vm_index in range(self._args.n_vms):
                vm_name = '%s-VM-%s'%(vn_name, vm_index)
                self.obj.delete_port(vm_name)
                self.obj.delete_vm(vm_name)
            self.obj.delete_network(vn_name)

def parse_cli(args):
    '''Define and Parse arguments for the script'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api_server_ip',
                        action='store',
                        default='127.0.0.1',
                        help='API Server IP [127.0.0.1]')
    parser.add_argument('--api_server_port',
                        action='store',
                        default='8082',
                        help='API Server Port [8082]')
    parser.add_argument('--keystone_ip',
                        action='store',
                        default='127.0.0.1',
                        help='Keystone IP [127.0.0.1]')
    parser.add_argument('--username',
                        action='store',
                        default='admin',
                        help='Admin user name [admin]')
    parser.add_argument('--password',
                        action='store',
                        default='contrail123',
                        help="Admin user's password [contrail123]")
    parser.add_argument('--filename',
                        action='store',
                        default='./scale_fake_vms',
                        help="Filename to write the shell commands to execute on vrouter node")
    parser.add_argument('--tenant',
                        action='store',
                        default='admin',
                        help='Admin Tenant name [admin]')
    parser.add_argument('--n_vns',
                        action='store',
                        default='0', type=int,
                        help='No of Vns to create per tenant [0]')
    parser.add_argument('--n_vms',
                        action='store',
                        default='0', type=int,
                        help='No of VMs to create per VN [0]. Each create spawns 20 vms by default')
    parser.add_argument('--cleanup',
                        action='store_true',
                        help='Cleanup the created objects [False]')
    pargs = parser.parse_args(args)
    return pargs

def get_random_cidr(mask=16):
    ''' Generate random non-overlapping cidr '''
    global alloc_addr_list
    address = socket.inet_ntop(socket.AF_INET,
                               struct.pack('>I',
                               random.randint(2**24, 2**32 - 2**29 - 1)))
    address = str(IPNetwork(address+'/'+str(mask)).network)
    if address.startswith('169.254') or address.startswith('127') or address in alloc_addr_list:
        cidr = get_random_cidr()
    else:
        alloc_addr_list.append(address)
        cidr = address+'/'+str(mask)
    return cidr

def main():
    pargs = parse_cli(sys.argv[1:])
    obj = ScaleTest(pargs)
    if pargs.cleanup:
        obj.cleanup()
    else:
        obj.create()
if __name__ == '__main__':
    main()
