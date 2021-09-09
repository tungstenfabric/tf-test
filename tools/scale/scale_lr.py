#!/usr/bin/env python3
import argparse
import random
import socket
import struct
import sys
from netaddr import *
from vnc_api.vnc_api import *
from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client

alloc_addr_list = list()

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

class VNC(object):
    def __init__(self, username, password, tenant, ip, port, domain, auth_url):
        auth_host = auth_url.split('//')[1].split(':')[0]
        self.vnc = VncApi(api_server_host=ip,
                          api_server_port=port,
                          username=username,
                          password=password,
                          tenant_name=tenant,
                          auth_host=auth_host)
        self.project_fqname = ['default-domain', tenant]
        self.project_uuid = self.vnc.fq_name_to_id('project',
                                self.project_fqname)
        auth = identity.Password(auth_url=auth_url,
                                username=username,
                                password=password,
                                project_name=tenant,
                                user_domain_name=domain,
                                project_domain_name=domain)
        self.neutron = client.Client(session=session.Session(auth=auth))

    def create_network(self, vn_name, mask=16):
        cidr = get_random_cidr(mask=mask).split('/')[0]
        vn_obj = VirtualNetwork(vn_name, fq_name=self.project_fqname+[vn_name],
                                parent_type='project')
        vn_obj.add_network_ipam(NetworkIpam(),
                                VnSubnetsType([IpamSubnetType(
                                subnet=SubnetType(cidr, mask))]))
        uuid = self.vnc.virtual_network_create(vn_obj)
        return self.vnc.virtual_network_read(id=uuid)

    def delete_network(self, vn_name):
        try:
            self.vnc.virtual_network_delete(fq_name=self.project_fqname+[vn_name])
        except NoIdError as e:
            print(e)

    def add_subnet_to_network(self, vn_obj, mask=16):
        try:
            cidr = get_random_cidr(mask=mask)
            subnet = {
                'cidr': cidr,
                'network_id': vn_obj.uuid,
                'ip_version': '4',
            }
            subnet_id = self.neutron.create_subnet({'subnet': subnet})
        except Exception as e:
            print(e)

    def create_port(self, port_name, vn_obj, vm_obj=None, device_owner=None):
        port_obj = VirtualMachineInterface(port_name,
                        fq_name=self.project_fqname+[port_name],
                        parent_type='project')
        port_obj.add_virtual_network(vn_obj)
        if vm_obj:
            port_obj.add_virtual_machine(vm_obj)
        if device_owner:
            port_obj.set_virtual_machine_interface_device_owner(device_owner)
        vmi_id = self.vnc.virtual_machine_interface_create(port_obj)
        port_obj = self.vnc.virtual_machine_interface_read(id=vmi_id)
        iip_obj = InstanceIp(name=port_name)
        iip_obj.add_virtual_network(vn_obj)
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
            print(e)

    def create_logical_router(self, lr_name, lr_type='vxlan-routing'):
        lr_obj = LogicalRouter(lr_name, fq_name=self.project_fqname+[lr_name],
                    logical_router_type=lr_type, parent_type='project')
        uuid = self.vnc.logical_router_create(lr_obj)
        return self.vnc.logical_router_read(id=uuid)

    def delete_logical_router(self, lr_name):
        try:
            self.vnc.logical_router_delete(fq_name=self.project_fqname+[lr_name])
        except NoIdError as e:
            print(e)

    def add_port_to_lr(self, lr_obj, vmi_obj):
        lr_obj.add_virtual_machine_interface(vmi_obj)
        self.vnc.logical_router_update(lr_obj)
        return self.vnc.logical_router_read(id=lr_obj.uuid)

    def get_lr_count(self):
        return len(self.vnc.logical_routers_list()['logical-routers'])

    def get_lr_vn_count(self, lr_name):
        lr = self.vnc.logical_router_read(fq_name=self.project_fqname + [lr_name])
        vns = lr.get_virtual_machine_interface_refs()
        return len(vns) if vns else 0

    def get_vn_subnet_count(self, vn_name):
        vn = self.vnc.virtual_network_read(fq_name=self.project_fqname + [vn_name])
        return len(vn.get_network_ipam_refs()[0]['attr'].get_ipam_subnets())

class ScaleLR(object):
    def __init__ (self, args):
        self.obj = VNC(args.username,
                       args.password,
                       args.tenant,
                       args.api_server_ip,
                       args.api_server_port,
                       args.domain,
                       args.auth_url)
        self._args = args

    def create(self):
        for idx in range(self._args.scale_n):
            lr_name = 'ScaleLR{}'.format(idx)
            lr = self.obj.create_logical_router(lr_name)
            for i in range(2):
                vn_name = lr_name + '-VN{}'.format(i)
                vn = self.obj.create_network(vn_name)
                vmi, iip = self.obj.create_port(vn_name + '-LR', vn,
                            device_owner='network:router_interface')
                lr = self.obj.add_port_to_lr(lr, vmi)

    def cleanup(self):
        for idx in range(self._args.scale_n):
            lr_name = 'ScaleLR{}'.format(idx)
            self.obj.delete_logical_router(lr_name)
            for i in range(2):
                vn_name = lr_name + '-VN{}'.format(i)
                self.obj.delete_port(vn_name + '-LR')
                self.obj.delete_network(vn_name)

    def verify(self):
        exp = self._args.scale_n
        count = self.obj.get_lr_count()
        msg = 'expected {} got {}'.format(exp, count)
        if count == exp:
            print('Passed: {}'.format(msg))
        else:
            print('Failed: {}'.format(msg))

class ScaleVNPerLR(ScaleLR):

    lr_name = 'ScaleVNPerLR'

    def create(self):
        lr = self.obj.create_logical_router(self.lr_name)
        for idx in range(self._args.scale_n):
            vn_name = self.lr_name + '-VN{}'.format(idx)
            vn = self.obj.create_network(vn_name)
            vmi, iip = self.obj.create_port(vn_name + '-LR', vn,
                        device_owner='network:router_interface')
            lr = self.obj.add_port_to_lr(lr, vmi)

    def cleanup(self):
        self.obj.delete_logical_router(self.lr_name)
        for idx in range(self._args.scale_n):
            vn_name = self.lr_name + '-VN{}'.format(idx)
            self.obj.delete_port(vn_name + '-LR')
            self.obj.delete_network(vn_name)

    def verify(self):
        exp = self._args.scale_n
        try:
            count = self.obj.get_lr_vn_count(self.lr_name)
        except NoIdError as e:
            print('Failed: LR {}, not found'.format(self.lr_name))
            return
        msg = 'expected {} got {}'.format(exp, count)
        if count == exp:
            print('Passed: {}'.format(msg))
        else:
            print('Failed: {}'.format(msg))

class ScaleSubnetPerVN(ScaleLR):

    lr_name = 'ScaleSubnetPerVN'

    def create(self):
        lr = self.obj.create_logical_router(self.lr_name)
        vn_name = self.lr_name + '-VN'
        vn = self.obj.create_network(vn_name)
        vmi, iip = self.obj.create_port(vn_name + '-LR', vn,
                        device_owner='network:router_interface')
        lr = self.obj.add_port_to_lr(lr, vmi)
        for idx in range(self._args.scale_n):
            self.obj.add_subnet_to_network(vn)

    def cleanup(self):
        self.obj.delete_logical_router(self.lr_name)
        vn_name = self.lr_name + '-VN'
        self.obj.delete_port(vn_name + '-LR')
        self.obj.delete_network(vn_name)

    def verify(self):
        vn_name = self.lr_name + '-VN'
        exp = self._args.scale_n
        try:
            count = self.obj.get_vn_subnet_count(vn_name)
        except NoIdError as e:
            print('Failed: VN {}, not found'.format(vn_name))
            return
        msg = 'expected {} got {}'.format(exp, count)
        if count >= exp:
            print('Passed: {}'.format(msg))
        else:
            print('Failed: {}'.format(msg))

def parse_cli(args):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api_server_ip',
                        action='store',
                        default='127.0.0.1',
                        help='API Server IP [127.0.0.1]')
    parser.add_argument('--api_server_port',
                        action='store',
                        default='8082',
                        help='API Server Port [8082]')
    parser.add_argument('--auth_url',
                        action='store',
                        default='http://127.0.0.1:35357/v3',
                        help='Keystone URL [http://127.0.0.1:35357/v3]')
    parser.add_argument('--username',
                        action='store',
                        default='admin',
                        help='Admin user name [admin]')
    parser.add_argument('--password',
                        action='store',
                        default='contrail123',
                        help="Admin user's password [contrail123]")
    parser.add_argument('--tenant',
                        action='store',
                        default='admin',
                        help='Admin Tenant name [admin]')
    parser.add_argument('--domain',
                        action='store',
                        default='default',
                        help='Project and User domain name [default]')
    parser.add_argument('--scale_n',
                        action='store',
                        default='1', type=int,
                        help='Scale number to achieve [1]')
    parser.add_argument('scenario',
                        choices=['scale_lr', 'scale_vn', 'scale_subnet'],
                        help='Scale scenario to run')
    parser.add_argument('ops',
                        choices=['create', 'cleanup', 'verify'],
                        help='Operation to perform')
    pargs = parser.parse_args(args)
    return pargs

def main():
    pargs = parse_cli(sys.argv[1:])
    scale = {'scale_lr': ScaleLR,
             'scale_vn': ScaleVNPerLR,
             'scale_subnet': ScaleSubnetPerVN
           }[pargs.scenario](pargs)
    getattr(scale, pargs.ops)()

if __name__ == '__main__':
    main()