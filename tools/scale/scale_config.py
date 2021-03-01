#python scale_v3.py --api_server_ip '10.204.216.64' --keystone_ip '10.204.216.150' --n_vns 10 --vnc --cleanup --n_process 2
#python scale_v3.py --api_server_ip '10.204.216.64' --keystone_ip '10.204.216.150' --n_policies 5 --n_policy_rules 2  --vnc --cleanup --n_process 2
#python scale_v3.py --api_server_ip '10.204.216.64' --keystone_ip '10.204.216.150' --n_sgs 5 --n_sg_rules 2  --vnc --cleanup --n_process 2
#python scale_v3.py --api_server_ip '10.204.216.64' --keystone_ip '10.204.216.150' --n_fips 1200  --vnc --cleanup --n_process 120
#python scale_v3.py --api_server_ip '10.204.216.64' --keystone_ip '10.204.216.150' --n_vns 1 --n_ports 10  --vnc --cleanup --n_process 10
from servicechain import ServiceChain
import argparse
import random
import socket
import struct
import os
import sys
import time
import uuid
import copy
import signal
import string
#import MySQLdb
from Queue import Empty
from netaddr import *
from datetime import datetime
from multiprocessing import Process, Queue
from neutronclient.neutron import client as neutron_client
from novaclient import client as nova_client
from keystoneclient.v3 import client as ks_client
from keystoneauth1 import identity as ks_identity
from keystoneauth1 import session as ks_session
try:
    from vnc_api.vnc_api import *
except:
    pass
from copy_reg import pickle
from types import MethodType

import threading
import thread
import logging

lock = dict()
def get_lock(key):
    global lock
    if key not in lock.keys():
        lock[key] = threading.Lock()
    return lock[key]
def _pickle_lock(lock):
    return _unpickle_lock, (lock.__hash__(),)
def _unpickle_lock(key):
    return get_lock(key)
pickle(thread.LockType, _pickle_lock, _unpickle_lock)


def _pickle_method(method):
    func_name = method.im_func.__name__
    obj = method.im_self
    cls = method.im_class
    return _unpickle_method, (func_name, obj, cls)

def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
    return func.__get__(obj, cls)

pickle(MethodType, _pickle_method, _unpickle_method)

alloc_addr_list = list()
debug = True
max_inst = 20

def retry(tries=12, delay=5):
    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, result = tries, False
            while mtries > 0:
                mtries -= 1
                try:
                    result = f(*args, **kwargs)
                except:
                    if not mtries:
                        raise
                if result is True:
                    break
                time.sleep(delay)
            if not result:
                return False
            else:
                return (tries - mtries)*delay
        return f_retry
    return deco_retry

class DB(object):
    def __init__(self, user, password, host, database):
        self.db = MySQLdb.connect(user=user, passwd=password,
                                  host=host, db=database)
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

    def query_db(self, query):
        self.db.rollback()
        self.cursor.execute(query)
        return self.cursor.fetchall()

class ScaleTest(object):
    def __init__ (self, args):
        self._args = args
        self._args.auth_url = 'http://%s:35357/v3' % self._args.keystone_ip
        self._args.admin_obj = Openstack(self._args.auth_url,
                                         self._args.admin_username,
                                         self._args.admin_password,
                                         self._args.admin_project)
        self.obj = self._args.admin_obj
        self.userid = self.obj.get_user_id(self._args.username)
        role = '_member_'
        if self._args.vnc or self._args.n_svc_chains or self._args.n_svc_templates:
            role = 'admin'
        self.roleid = self.obj.get_role_id(role)
        if self._args.project:
            self.project_id = Openstack(self._args.auth_url,
                                       self._args.username,
                                       self._args.password,
                                       self._args.project).project_id
        self._args.computes = self.get_compute_hosts()
        self._args.timeout = 60 if self._args.rate \
                                else self._args.timeout
        self.db = None
        if self._args.n_vms or self._args.n_svc_chains:
            self.db = DB(user='root', password=self._args.mysql_passwd,
                         host=self._args.keystone_ip, database='nova')
            self.initial_vm_count = self.get_active_vm_count()
            self.initial_port_count = self.get_port_count()

    def get_compute_hosts(self):
        ''' Check whether all compute nodes are up '''
        hosts = self.obj.nova.services.list(binary='nova-compute')
        computes = [h.host for h in hosts if h.status == 'enabled'
                                             and h.state == 'up']
        hosts = list(map((lambda x: x.host), hosts))
        if set(hosts) - set(computes):
            raise Exception('Few hosts are down %s'%list(set(hosts)
                                                   - set(computes)))
        return computes

    def is_per_project_obj_reqd(self):
        if self._args.n_vns or self._args.n_vms or self._args.n_sgs or \
           self._args.n_sg_rules or self._args.n_routers or \
           self._args.n_fips or self._args.n_ports or \
           self._args.n_svc_templates or self._args.n_svc_chains or \
           self._args.n_policies or self._args.n_policy_rules:
            return True
        return False

    @retry(30, 2)
    def get_vm_active_time(self, initial, expected):
        current = self.get_active_vm_count()
        if current - initial < expected:
            print('Not all VMs are active, actual: %s, expected: %s'%(
                                             current-initial, expected))
            return False
        return True

    def get_active_vm_count(self):
        query = 'select count(vm_state) from instances '+\
                'where vm_state = "active" and power_state = "1";'
        count_dict = self.db.query_db(query)[0]
        return count_dict['count(vm_state)']

    def get_port_count(self):
        return len(self.obj.list_ports())

    def setUp(self):
        kwargs_list = list()
        queues = list()
        self.projects_list = list()

        for index in range(self._args.n_process):
            queues.append(Queue())
            kwargs_list.append({'queue': queues[index]})

        (success, timediff) = create_n_process(self.create,
                                               self._args.n_process,
                                               kwargs_list,
                                               self._args.timeout,
                                               callback=self.read_from_queue)
        print('Time to create all projects %s'%timediff)

        kwargs_list = list()
        for projects in self.projects_list:
            kwargs_list.append({'projects': projects})

        # Get the boot time of VMs
        self.post_create()

        # Verify the created objects
        if self._args.verify:
            (success, timediff) = create_n_process(self.verify,
                                                   len(self.projects_list),
                                                   kwargs_list)
            print( 'Time to verify all projects %s Success Percentage: %s'%(timediff, success))

    def read_from_queue(self, process, kwargs):
         try:
             self.projects_list.append(kwargs['queue'].get(
                               timeout=self._args.timeout))
         except Empty:
             process.terminate()

    def create(self, queue):
        try:
            projects = list()
            create = False if self._args.project else True
            for index in range(self._args.n_projects):
                project_dict = {}
                if create is True:
                    self._args.project = random_string('Project')
                    self.project_id = self.obj.create_project(self._args.project,domain_id='default')
                    self.obj.add_user_to_project(self.userid, self.roleid,
                                                self.project_id)
                project_dict['name'] = self._args.project
                project_dict['id'] = self.project_id
                # Check if any objs has to be created per project
                if self.is_per_project_obj_reqd():
                    self._args.auth_token = None #self.obj.get_auth_token()
                    perprojectobj = PerprojectWrapper(self._args)
                    perprojectobj.setUp()
                    project_dict['perprojectobj'] = perprojectobj
                projects.append(project_dict)
        except:
            queue.put_nowait(projects)
            raise
        queue.put(projects)

    def post_create(self):
        # Check VM active count
        if self._args.n_vms or self._args.n_svc_chains:
            expected = self._args.n_process * self._args.n_projects *\
                       self._args.n_threads * ((self._args.n_vns or 1) * self._args.n_vms * max_inst + self._args.n_svc_chains)
            exp_ports = self._args.n_process * self._args.n_projects *\
                       self._args.n_threads * ((self._args.n_vns or 1) * self._args.n_vms * max_inst + self._args.n_svc_chains*2)
            print( "Took %s secs to have all vms in active state" %(
                   self.get_vm_active_time(self.initial_vm_count, expected)))
            current_port_count = self.get_port_count()
            if current_port_count - self.initial_port_count != exp_ports:
                print( 'Port count mismatch, current:%s, expected:%s'%(
                       current_port_count-self.initial_port_count, expected))
            for projects in self.projects_list:
                for project in projects:
                    project['perprojectobj'].populate_vm_obj()

    def verify(self, projects, delete=False):
        # Verify project got created

        # Call perproject verify
        for project_dict in projects:
            if project_dict.has_key('perprojectobj'):
                project_dict['perprojectobj'].verify()

    def cleanup(self):
        kwargs_list = list()
        for projects in self.projects_list:
            kwargs_list.append({'projects': projects})
        (success, timediff) = create_n_process(self.delete, 
                                               len(self.projects_list),
                                               kwargs_list,
                                               self._args.timeout)
        print( 'Time to delete all projects %s'%timediff)

    def delete(self, projects):
        for project_dict in projects:
            if project_dict.has_key('perprojectobj'):
                project_dict['perprojectobj'].cleanup()
            if not self._args.project:
                self.obj.delete_project(project_dict['id'])

class PerprojectWrapper(object):
    def __init__(self, args):
        self._args = args
        self.admin_obj = self._args.admin_obj
        self.get_handles()

    def get_handles(self):
        if self._args.vnc:
            self.obj = VNC(self._args.auth_url,
                           self._args.username,
                           self._args.password,
                           self._args.project,
                           self._args.api_server_ip,
                           self._args.api_server_port,
                           self._args.keystone_ip,
                           self._args.auth_token)
        else:
            self.obj = Openstack(self._args.auth_url,
                                 self._args.username,
                                 self._args.password,
                                 self._args.project,
                                 self._args.auth_token)
        if self._args.n_svc_templates or self._args.n_svc_chains or self._args.n_policies:
            self.sc = ServiceChain(self.obj, self._args.username,
                                   self._args.password,
                                   self._args.project,
                                   self._args.api_server_ip,
                                   self._args.api_server_port,
                                   self._args.keystone_ip,
                                   self._args.auth_token)

    def pre_conf(self):
        ''' Create certain objects before staring test '''
        if self._args.vdns:
            self.obj.create_vdns(self.get_name('vdns', ''))
        if self._args.ipam:
            self.obj.create_ipam(self.get_name('ipam', ''))
        if (self._args.n_ports or self._args.n_vms)\
            and not self._args.n_vns:
            vn_name = self.get_name('VN', 'G')
            self.obj.create_network(vn_name, mask=16)

        if self._args.n_sg_rules and not self._args.n_sgs:
           sg_name = self.get_name('SG', 'G')
           self.obj.create_sg(sg_name)

        if self._args.n_fips or self._args.n_routers:
            if not self._args.public_vn_id:
                vn_name = random_string('EXT-VN')
                self.admin_obj.create_network(vn_name, mask=16, external=True)
            else:
                self.admin_obj.ext_vn_uuid = self._args.public_vn_id

        if self._args.n_svc_chains:
            st_name = random_string('ServiceT')
            self.sc.create_svc_template(name=st_name,
                                        image_id= self._args.image_id,
                                        service_mode='in-network')

        if self._args.n_policies or self._args.n_policy_rules:
            left_vn = random_string('Left-VN')
            right_vn = random_string('Right-VN')
            self.obj.create_network(left_vn)
            self.obj.create_network(right_vn)

        if self._args.n_policy_rules and not self._args.n_policies:
            self._args.n_policies = 1

    def setUp(self):
        ''' Create N objects '''
        self.pre_conf()
        queues = list()
        self.id_obj = list()
        kwargs_list = list()
        # Create Processes
        for i in range(self._args.n_threads):
            queues.append(Queue())
            kwargs_list.append({'queue':queues[i], 'index':i})
        (success, timediff) = create_n_process(self.start_create,
                                               self._args.n_threads,
                                               kwargs_list,
                                               self._args.timeout,
                                               callback=self.read_from_queue)
        print( 'Time to create objects for project %s is %s. Success %% %s' %(
               self._args.project, timediff, success))

    def read_from_queue(self, process, kwargs):
         try:
             self.id_obj.append(kwargs['queue'].get(timeout=self._args.timeout))
         except Empty:
             process.terminate()

    def merge_to_self(self, parent):
        for attr in parent.__dict__:
            if type(parent.__dict__[attr]) is list:
                self.__dict__[attr].extend(parent.__dict__[attr])
            if type(parent.__dict__[attr]) is dict:
                self.__dict__[attr].update(parent.__dict__[attr])

    def start_create(self, index, queue):
        parent_id = self.obj.id
        self.get_handles()
        self.obj.id = copy.deepcopy(parent_id)
        try:
            # Create virtual network
            for vn_index in range(index, index+self._args.n_vns):
                vn_name = self.get_name('VN', vn_index)
                self.obj.create_network(vn_name=vn_name)

            # Create Ports
            for vn_name in self.obj.id.vn_uuid.keys():
                for port_index in range(index, index+self._args.n_ports):
                    port_name = vn_name+'-Port'+str(port_index)
                    self.obj.create_port(vn_name, port_name)

            # Create Security Group
            for sg_index in range(index, index+self._args.n_sgs):
                sg_name = self.get_name('SG', sg_index)
                self.obj.create_sg(sg_name)

            # Create Security Group Rules
            for sg_name in self.obj.id.sg_id.keys():
                cidr = get_randmon_cidr(mask=29)
                for rule_index in range(index, index+self._args.n_sg_rules):
                    self.obj.create_sg_rule(sg_name, rule_index+1000,
                                            rule_index+1000, cidr)

            # Create Router
            for rtr_index in range(index, index+self._args.n_routers):
                router_name = self.get_name('RTR', rtr_index)
                self.obj.create_router(router_name)
                self.obj.add_gateway_router(router_name, self.admin_obj.ext_vn_uuid)

            # Attach all the VNs to a LR
            for vn_name in self.obj.id.vn_uuid.keys():
                 if self.obj.id.router_id.keys():
                    rtr_name = self.obj.id.router_id.keys()[0]
                    self.obj.add_interface_router(rtr_name, vn_name)

            # Create Floating IP
            port_ids = self.obj.id.port_id.values()
            for fip_index in range(index, index+self._args.n_fips):
                self.obj.create_floatingip(self.admin_obj.ext_vn_uuid)
                if fip_index < len(port_ids):
                    port_id = port_ids[fip_index]
                    fip_id = self.obj.id.fip_id[fip_index]
                    self.obj.assoc_floatingip(fip_id, port_id)

            # Create virtual machines
            for vn_name in self.obj.id.vn_uuid.keys():
                for vm_index in range(index, index+self._args.n_vms):
                    vm_name = vn_name+'-VM'+random_string(str(vm_index))
                    port_name = vn_name+'-Port'+str(vm_index)
                    self.obj.create_vm(image_id=self._args.image_id,
                                       vm_name=vm_name, port_name=port_name,
                                       vn_name=vn_name)

            # Create Service Template
            for st_index in range(index, index+self._args.n_svc_templates):
                st_name = random_string('ServiceT')
                self.sc.create_svc_template(name=st_name,
                                            image_id= self._args.image_id,
                                            service_mode='in-network')

            for st_name in self.obj.id.st_obj.keys():
                for si_index in range(index, index+self._args.n_svc_chains):
                    si_name = self.get_name('ServiceI', si_index)
                    pol_name = 'Policy-'+si_name
                    left_vn = self.get_name('leftVN', si_index)
                    right_vn = self.get_name('rightVN', si_index)
                    self.obj.create_network(vn_name=left_vn)
                    self.obj.create_network(vn_name=right_vn)
                    self.sc.create_svc_instance(si_name, st_name, left_vn, right_vn)
                    self.sc.create_policy(name=pol_name, si_name=si_name,
                                          src_vn=left_vn, dst_vn=right_vn)

            # Create Policies
            for policy_index in range(index, index+self._args.n_policies):
                policy_name = self.get_name('Policy', policy_index)
                vn_list = self.obj.id.vn_uuid.keys()
                self.sc.create_policy(name=policy_name,
                                      src_vn=vn_list[0],
                                      dst_vn=vn_list[1],
                                      n_rules=self._args.n_policy_rules)
        except:
            queue.put_nowait(self.obj.id)
            raise
        queue.put(self.obj.id)

    def cleanup(self):
        ''' Cleanup created objects '''
        kwargs_list = list()
        # Create Processes
        for i in range(self._args.n_threads):
            kwargs_list.append({'id':self.id_obj[i]})
        (success, timediff) = create_n_process(self.start_cleanup, 
                                               self._args.n_threads,
                                               kwargs_list,
                                               self._args.timeout)
        print( 'Time to delete objects for project %s is %s. Success %% %s' %(
               self._args.project, timediff, success))
        self.post_cleanup()

    def start_cleanup(self, id):
        # Delete VM
        for vm_obj in id.vm_obj.values():
            self.obj.delete_vm(vm_obj)
        # Delete Floating IP
        for fip_id in id.fip_id:
            self.obj.delete_floatingip(fip_id)
        # Delete Port
        if not id.vm_id:
            for port_id in id.port_id.values():
                self.obj.delete_port(port_id)
        # Delete Security Group rule
        for rules in id.rule_id.values():
            for rule in rules:
                self.obj.delete_sg_rule(rule)
        # Delete Security Group
        for sg_id in id.sg_id.values():
            self.obj.delete_sg(sg_id)
        # Delete Router
        for router_id in id.router_id.values():
            for subnet_id in id.subnet_uuid.values():
                self.obj.remove_interface_router(router_id, subnet_id)
            self.obj.remove_gateway_router(router_id)
            self.obj.delete_router(router_id)
        # Delete VN
        if not id.vm_id and not id.port_id:
            for vn_id in id.vn_uuid.values():
                self.obj.delete_network(vn_id)
        # Delete Policies
        for policy_id in id.policy_id.values():
            self.obj.delete_policy(policy_id)

    def post_cleanup(self):
        ''' Cleanup the parent created objects '''
        # If child has failed to cleanup certain objects then parent cleanup will fail too
        self.start_cleanup(self.obj.id)

    def populate_vm_obj(self):
        vm_objs = self.obj.list_vms()
        vm_dict = dict()
        for vm_obj in vm_objs:
            vm_dict[vm_obj.name] = vm_obj
        '''
            vm_obj.delete()
        logger.info( vm_dict.keys(), vm_dict.values()
        '''
        for id in self.id_obj:
            for actual_name in vm_dict.keys():
                for vm_name in id.vm_id.keys():
                    if vm_name in actual_name:
                        id.vm_obj[actual_name] = vm_dict[actual_name]

    def verify(self, op=None):
        pass

    def get_name(self, prefix, index):
        return random_string(self._args.project + '-' + str(prefix) + str(index))

# A Class of UUIDs
class UUID(object):
    def __init__(self):
        self.vn_uuid = dict()
        self.subnet_uuid = dict()
        self.port_id = dict()
        self.sg_id = dict()
        self.rule_id = dict()
        self.router_id = dict()
        self.policy_id = dict()
        self.fip_id = list()
        self.vm_id = dict()
        self.vn_obj = dict()
        self.sg_obj = dict()
        self.fip_pool_obj = None
        self.vm_obj = dict()
        self.st_obj = dict()
        self.si_obj = dict()
        self.policy_obj = dict()
        self.ipam_obj = None
        self.vdns_obj = None

class Openstack(object):
    def __init__(self, auth_url, username, password, project, auth_token=None,
                domain_name=None, domain_id='default', insecure=True, region_name='RegionOne',
                logger=None, scope='domain'):
        ''' Get keystone client obj '''
        
        self.session = None
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project = project
        self.domain_name = domain_name or 'Default'
        self.domain_id = domain_id
        self.keystone = self.get_client()
        self.session = self.keystone.session
        self.project_id  =  self.keystone.projects.find(name=self.project, domain_id=domain_id).id
        ''' Get nova client handle '''
        self.nova = nova_client.Client('2',session=self.session,region_name=region_name)
        ''' Get neutron client handle '''
        self.neutron = neutron_client.Client('2.0',session=self.session,region_name=region_name)
        self.id = UUID()
        
    def get_session(self):
        self.auth =  ks_identity.v3.Password(auth_url=self.auth_url, username=self.username,
                     password=self.password, project_name=self.project,
                     user_domain_id="default", project_domain_id="default")

        session = ks_session.Session(auth=self.auth)
        return session

    def get_client(self):
        return ks_client.Client(session=self.get_session())

    def get_handle(self):
        return self.keystone

    def get_auth_token(self):
        return self.keystone.session.get_token()

    def create_project(self, project_name,domain_id):
        return self.keystone.projects.create(project_name,domain_id).id

    def get_user_id(self, username):
        users = self.keystone.users.list()
        for user in users:
            if user.name == username:
                return user.id
        return None

    def get_role_id(self, role_name):
        roles = self.keystone.roles.list()
        for role in roles:
            if role.name == role_name:
                return role.id
        return None

    def add_user_to_project(self, userid, roleid, projectid):
        self.keystone.roles.grant(project=projectid,
                                          user=userid,
                                          role=roleid,
                                          group=None)

    def delete_project(self, project_id):
        return self.keystone.projects.delete(project_id)

    def create_network(self, vn_name, mask=24, external=False):
        ''' Create Network via Neutron client call '''
        cidr = get_randmon_cidr(mask=mask)
        vn_dict = {'name': vn_name}
        if external:
            vn_dict['router:external'] = True
        response = self.neutron.create_network({'network': vn_dict})

        ''' Store VN uuid and subnet uuid dicts '''
        net_id = response['network']['id']
        if external:
            self.ext_vn_uuid = net_id
        else:
            self.id.vn_uuid[vn_name] = net_id
        response = self.neutron.create_subnet({'subnet':
                                    {'cidr': cidr,
                                     'ip_version': 4,
                                     'network_id': net_id
                                    }})
        self.id.subnet_uuid[vn_name] = response['subnet']['id']

    def update_network(self, vn_name, network_dict):
        vn_id = self.id.vn_uuid[vn_name]
        self.neutron.update_network(vn_id, {'network': network_dict})

    @retry(15, 2)
    def delete_network(self, vn_id):
        ''' Delete network '''
        self.neutron.delete_network(vn_id)
        return True

    def create_port(self, vn_name, port_name):
        ''' Create port using Neutron api '''
        port_dict = {'network_id': self.id.vn_uuid[vn_name]}
        response = self.neutron.create_port({'port': port_dict})
        ''' Store Port UUID's '''
        self.id.port_id[port_name] = response['port']['id']

    def delete_port(self, port_id):
        ''' Delete Port '''
        self.neutron.delete_port(port_id)

    def list_ports(self):
        ''' List Port '''
        return self.neutron.list_ports()['ports']

    def create_floatingip(self, ext_vn_uuid):
        ''' Create Floating IP '''
        fip_dict = {'floating_network_id': ext_vn_uuid}
        response = self.neutron.create_floatingip({'floatingip': fip_dict})
        self.id.fip_id.append(response['floatingip']['id'])

    def assoc_floatingip(self, fip_id, port_id):
        fip_dict = {'floatingip': {'port_id': port_id}}
        return self.neutron.update_floatingip(fip_id, fip_dict)

    def delete_floatingip(self, fip_id):
        ''' Delete FloatingIP '''
        self.neutron.delete_floatingip(fip_id)

    def create_router(self, router_name):
        ''' Create Logical Router '''
        router_dict = {'name': router_name, 'admin_state_up': True}
        response = self.neutron.create_router({'router': router_dict})
        self.id.router_id[router_name] = response['router']['id']

    def add_interface_router(self, router_name, vn_name):
        router_id = self.id.router_id[router_name]
        subnet_id = self.id.subnet_uuid[vn_name]
        self.neutron.add_interface_router(router_id, {'subnet_id': subnet_id})

    def remove_interface_router(self, router_id, subnet_id):
        self.neutron.remove_interface_router(router_id, {'subnet_id': subnet_id})

    def add_gateway_router(self, router_name, vn_uuid):
        router_id = self.id.router_id[router_name]
        self.neutron.add_gateway_router(router_id, {'network_id': vn_uuid})

    def remove_gateway_router(self, router_id):
        self.neutron.remove_gateway_router(router_id)

    def delete_router(self, router_id):
        ''' Delete Logical Router '''
        self.neutron.delete_router(router_id)

    def create_sg(self, sg_name):
        ''' Create Security Group '''
        sg_dict = {'name': sg_name}
        res = self.neutron.create_security_group({'security_group': sg_dict})
        self.id.sg_id[sg_name] = res['security_group']['id']

    def delete_sg(self, sg_id):
        self.neutron.delete_security_group(sg_id)

    def create_sg_rule(self, sg_name, min, max, cidr='0.0.0.0/0',
                       direction='ingress', proto='tcp'):
        sg_id = self.id.sg_id[sg_name]
        rule_dict = {'security_group_id': sg_id, 'direction': direction,
                     'remote_ip_prefix': cidr, 'protocol': proto,
                     'port_range_min': min, 'port_range_max': max}
        response = self.neutron.create_security_group_rule(
                         {'security_group_rule': rule_dict})
        if sg_name not in self.id.rule_id:
            self.id.rule_id[sg_name] = list()
        self.id.rule_id[sg_name].append(response['security_group_rule']['id'])

    def delete_sg_rule(self, rule_id):
        self.neutron.delete_security_group_rule(rule_id)

    def create_vm(self, vm_name, image_id, port_name=None,
                  vn_name=None, compute_host=None, zone='nova'):
        ''' Create virtual machine '''
        nics = []
        launch_on = None
        port_id = None
        ''' Few harcoded values '''
        flavor = 1 # m1.tiny

        if port_name in self.id.port_id:
            port_id = self.id.port_id[port_name]
        if port_id is not None:
            nics = [{'port-id': port_id}]
        else:
            nics = [{'net-id': self.id.vn_uuid[vn_name]}]

        if compute_host:
            launch_on = zone + ':' + compute_host

        '''
        with open("/tmp/userdata.sh", "w") as f:
            f.write("""#!/bin/sh
ls -al / | tee /tmp/output.txt
               """)
        '''
        response = self.nova.servers.create(name=vm_name,
                                            flavor=flavor,
                                            image=image_id,
                                            nics=nics,
                                            availability_zone=launch_on,
                                            max_count=max_inst)
#                                            userdata='/tmp/userdata.sh')
#        logger.info( '%s, %s' %(response, response.__dict__)
        self.id.vm_id[vm_name] = response.id

    def list_vms(self, all_projects=False):
        return self.nova.servers.list(search_opts={"all_projects": all_projects},
                                      detailed=False)

    def delete_vm(self, vm_obj):
        vm_obj.delete()

    def delete_policy(self, policy_id):
        self.neutron.delete_policy(policy_id)

class VNC(Openstack):
    def __init__(self, auth_url, username, password, project, ip, port, auth_host, auth_token=None):
        super(VNC, self).__init__(auth_url, username, password, project)
        self.vnc = VncApi(api_server_host=ip,
                          api_server_port=port,
                          username=username,
                          password=password,
                          tenant_name=project,
                          auth_host=auth_host)
        #print(self.project_id)
        #print(project)
        #print(self.vnc.projects_list())
        self.project_obj = self.vnc.project_read(id=str(uuid.UUID(self.project_id)))

    def create_vdns(self, vdns_name):
        vdns_type = VirtualDnsType(domain_name='juniper.net',
                                   dynamic_records_from_client=True,
                                   default_ttl_seconds=100,
                                   record_order='random')
        vdns_obj = VirtualDns(vdns_name, self.project_obj, virtual_DNS_data=vdns_type)
        vdns_id = self.vnc.virtual_DNS_create(vdns_obj)
        self.id.vdns_obj = self.vnc.virtual_DNS_read(id=vdns_id)

    def create_ipam(self, ipam_name):
        ipam_obj = NetworkIpam(ipam_name, self.project_obj, network_ipam_mgmt=IpamType("dhcp"))
        if self.id.vdns_obj:
            ipam_obj.add_virtual_DNS(self.id.vdns_obj)
        ipam_uuid = self.vnc.network_ipam_create(ipam_obj)
        self.id.ipam_obj = self.vnc.network_ipam_read(id=ipam_uuid)

    def create_network(self, vn_name, mask=24, external=False):
        ''' Create virtual network using VNC api '''
        cidr = get_randmon_cidr(mask=mask).split('/')[0]
        vn_obj = VirtualNetwork(vn_name, self.project_obj,
                                router_external=external)
        vn_obj.add_network_ipam(self.id.ipam_obj or NetworkIpam(),
                                VnSubnetsType([IpamSubnetType(
                                subnet=SubnetType(cidr, mask))]))
        net_id = self.vnc.virtual_network_create(vn_obj)
        if external:
            fip_pool_obj = FloatingIpPool(vn_name, vn_obj)
            self.vnc.floating_ip_pool_create(fip_pool_obj)
            self.project_obj.add_floating_ip_pool(fip_pool_obj)
            self.vnc.project_update(self.project_obj)
            self.id.fip_pool_obj = self.vnc.floating_ip_pool_read(fq_name=fip_pool_obj.get_fq_name())
            self.ext_vn_uuid = net_id
        else:
            self.id.vn_uuid[vn_name] = net_id
        self.id.vn_obj[vn_name] = self.vnc.virtual_network_read(fq_name=vn_obj.get_fq_name())

    def create_port(self, vn_name, port_name):
        ''' Create Port through VNC api '''
        port_obj = VirtualMachineInterface(port_name, parent_obj=self.project_obj)
        self.id.port_id[port_name] = port_obj.uuid = str(uuid.uuid4())
        port_obj.add_virtual_network(self.id.vn_obj[vn_name])
        self.vnc.virtual_machine_interface_create(port_obj)
        iip_id = str(uuid.uuid4())
        iip_obj = InstanceIp(name=iip_id)
        iip_obj.uuid = iip_id
        iip_obj.add_virtual_network(self.id.vn_obj[vn_name])
        iip_obj.add_virtual_machine_interface(port_obj)
        self.vnc.instance_ip_create(iip_obj)

    def create_floatingip(self, ext_vn_uuid):
        ''' Create Floating IP using VNC api '''
        vn_obj = self.vnc.virtual_network_read(id=ext_vn_uuid)
        fip_pool_obj = FloatingIpPool('floating-ip-pool', vn_obj)
        fip_id = str(uuid.uuid4())
        fip_obj = FloatingIp(name=fip_id, parent_obj=fip_pool_obj)
        fip_obj.uuid = fip_id
        fip_obj.set_project(self.project_obj)
        fip_obj.set_virtual_machine_interface_list([])
        fip_obj.set_floating_ip_fixed_ip_address(None)
        self.vnc.floating_ip_create(fip_obj)
        self.id.fip_id.append(fip_id)

    def create_sg(self, sg_name):
        ''' Create Security group using VNC api '''
        def _get_rule(prefix, ethertype):
            dst_addr = AddressType(subnet=SubnetType(prefix, 0))
            src_addr = AddressType(security_group='local')
            rule = PolicyRuleType(rule_uuid=str(uuid.uuid4()), direction='>',
                                  protocol='any', src_addresses=[src_addr],
                                  src_ports=[PortType(0, 65535)],
                                  dst_addresses=[dst_addr],
                                  dst_ports=[PortType(0, 65535)],
                                  ethertype=ethertype)
            return rule

        rules = [_get_rule('0.0.0.0', 'IPv4'), _get_rule('::', 'IPv6')]
        sg_obj = SecurityGroup(name=sg_name, parent_obj=self.project_obj,
                               security_group_entries=PolicyEntriesType(rules))
        self.id.sg_id[sg_name] = sg_obj.uuid = str(uuid.uuid4())
        self.vnc.security_group_create(sg_obj)
        self.id.sg_obj[sg_name] = self.vnc.security_group_read(id=sg_obj.uuid)

    def create_sg_rule(self, sg_name, min, max, cidr='0.0.0.0/0',
                       direction='ingress', proto='tcp'):
        ''' Create Security Group Rule using VNC api '''
        def _get_rule(dir, cidr, min, max, proto, ethertype):
            prefix = cidr.split('/')
            if dir == 'ingress':
                src_addr = AddressType(subnet=SubnetType(prefix[0], int(prefix[1])))
                dst_addr = AddressType(security_group='local')
            else:
                dst_addr = AddressType(subnet=SubnetType(prefix[0], int(prefix[1])))
                src_addr = AddressType(security_group='local')
            rule = PolicyRuleType(rule_uuid=str(uuid.uuid4()), direction='>',
                                  protocol=proto, src_addresses=[src_addr],
                                  src_ports=[PortType(0, 65535)],
                                  dst_addresses=[dst_addr],
                                  dst_ports=[PortType(min, max)],
                                  ethertype=ethertype)
            return rule

        rule = _get_rule(direction, cidr, min, max, proto, 'IPv4')
        sg_obj = self.id.sg_obj[sg_name]
        rules = sg_obj.get_security_group_entries()
        if rules is None:
            rules = PolicyEntriesType([rule])
        else:
            rules.add_policy_rule(rule)
        sg_obj.set_security_group_entries(rules)
        self.vnc.security_group_update(sg_obj)
        if sg_name not in self.id.rule_id:
            self.id.rule_id[sg_name] = list()
        self.id.rule_id[sg_name].append(rule.rule_uuid)
        self.id.sg_obj[sg_name] = self.vnc.security_group_read(id=sg_obj.uuid)

    def create_router(self, router_name):
        ''' Create Logical Router using VNC api '''
        router_obj = LogicalRouter(router_name, self.project_obj,
                                   id_perms=IdPermsType(enable=True))
        self.id.router_id[router_name] = router_obj.uuid = str(uuid.uuid4())
        self.vnc.logical_router_create(router_obj)
    
    def delete_policy(self, policy_id):
        self.vnc.network_policy_delete(id=policy_id)

def get_randmon_cidr(mask=16):
    ''' Generate random non-overlapping cidr '''
    global alloc_addr_list
    address = socket.inet_ntop(socket.AF_INET,
                               struct.pack('>I',
                               random.randint(2**24, 2**32 - 2**29 - 1)))
    address = str(IPNetwork(address+'/'+str(mask)).network)
    if address.startswith('169.254') or address in alloc_addr_list:
        cidr = get_randmon_cidr()
    else:
        alloc_addr_list.append(address)
        cidr = address+'/'+str(mask)
    return cidr

def parse_cli(args):
    '''Define and Parse arguments for the script'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--api_server_ip',
                        action='store',
                        default='127.0.0.1',
                        help='API Server IP [127.0.0.1]')
    parser.add_argument('--keystone_ip',
                        action='store',
                        default='127.0.0.1',
                        help='Keystone IP [127.0.0.1]')
    parser.add_argument('--api_server_port',
                        action='store',
                        default='8082',
                        help='API Server Port [8082]')
    parser.add_argument('--admin_username',
                        action='store',
                        default='admin',
                        help='Admin user name [admin]')
    parser.add_argument('--admin_password',
                        action='store',
                        default='c0ntrail123',
                        help="Admin user's password [contrail123]")
    parser.add_argument('--admin_project',
                        action='store',
                        default='admin',
                        help='Admin project name [admin]')
    parser.add_argument('--username',
                        action='store',
                        default='admin',
                        help='project user name [admin]')
    parser.add_argument('--password',
                        action='store',
                        default='c0ntrail123',
                        help="project user's password [contrail123]")
    parser.add_argument('--mysql_passwd',
                        action='store',
                        default=None,
                        help="Root password for mysql, reqd in case of n_vms")
    parser.add_argument('--project',
                        action='store',
                        default='',
                        help='project name []')
    parser.add_argument('--n_projects',
                        action='store',
                        default='1', type=int,
                        help='No of projects to create [1]')
    parser.add_argument('--n_process',
                        action='store',
                        default='1', type=int,
                        help='No of Parallel processes to run [1]')
    parser.add_argument('--n_threads',
                        action='store',
                        default='1', type=int,
                        help='No of threads to run per process [1]')
    parser.add_argument('--image_id',
                        action='store',
                        default=None,
                        help='Image ID [None]')
    parser.add_argument('--public_vn_id',
                        action='store',
                        default=None,
                        help='UUID of public network')
    parser.add_argument('--n_vns',
                        action='store',
                        default='0', type=int,
                        help='No of Vns to create per project [0]')
    parser.add_argument('--n_ports',
                        action='store',
                        default='0', type=int,
                        help='No of Ports to create per VN [0]')
    parser.add_argument('--n_sgs',
                        action='store',
                        default='0', type=int,
                        help='No of Security Groups to create per project [0]')
    parser.add_argument('--n_sg_rules',
                        action='store',
                        default='0', type=int,
                        help='No of Security Group Rules to create per SG [0]')
    parser.add_argument('--n_routers',
                        action='store',
                        default='0', type=int,
                        help='No of Routers to create per project [0]')
    parser.add_argument('--n_vms',
                        action='store',
                        default='0', type=int,
                        help='No of VMs to create per VN [0]. Each create spawns 20 vms by default')
    parser.add_argument('--n_fips',
                        action='store',
                        default='0', type=int,
                        help='No of Floating-IPs to create per project [0]')
    parser.add_argument('--n_svc_chains',
                        action='store',
                        default='0', type=int,
                        help='No of Service chains(instances+policy) to create per project [0]')
    parser.add_argument('--n_svc_templates',
                        action='store',
                        default='0', type=int,
                        help='No of Service templates to create per project [0]')
    parser.add_argument('--n_policies',
                        action='store',
                        default='0', type=int,
                        help='No of policies to create per project [0]')
    parser.add_argument('--n_policy_rules',
                        action='store',
                        default='0', type=int,
                        help='No of policy rules to create per policy [0]')
    parser.add_argument('--vnc',
                        action='store_true',
                        help='Use VNC client to configure objects [False]')
    parser.add_argument('--vdns',
                        action='store_true',
                        help='Create VDNS per project [False]')
    parser.add_argument('--ipam',
                        action='store_true',
                        help='Create IPAM per project [False]')
    parser.add_argument('--cleanup',
                        action='store_true',
                        help='Cleanup the created objects [False]')
    parser.add_argument('--verify',
                        action='store_true',
                        help='Verify the created objects [False]')
    parser.add_argument('--rate',
                        action='store_true',
                        help='Terminate children after a min [False]')
    parser.add_argument('--timeout',
                        action='store',
                        default='180000', type=int,
                        help='Max wait time in secs [1 hr]')

    pargs = parser.parse_args(args)
    if pargs.n_projects > 1 and pargs.project:
        pargs.project = None
        print( 'Overriding --project as --n_projects is set')
        time.sleep(1)

    if pargs.n_vms and pargs.n_ports and (pargs.n_vms != pargs.n_ports):
        pargs.n_ports = pargs.n_vms
        print( 'Setting n_ports to be same as n_vms')
        time.sleep(1)

    return pargs

def create_n_process(target, n_process, kwargs_list, timeout=None, callback=None):
    process = list()
    events = list()
    for i in range(n_process):
        process.append(Process(target=target, kwargs=kwargs_list[i]))

    start_time = datetime.now()
    if debug is True:
        print( 'Time at start %s'%str(start_time))

    start_process(process)
    if callback:
        callback_process(callback, process, kwargs_list)
    join_process(process, timeout)
    success = get_success_percentile(process)

    end_time = datetime.now()
    if debug is True:
        print( 'Time at End %s'%str(end_time))

    return (success, end_time-start_time)

def start_process(processes):
    for process in processes:
        time.sleep(2)
        process.start()

def callback_process(callback, processes, kwargs_list):
    for i in xrange(len(processes)):
        callback(processes[i], kwargs_list[i])

def join_process(processes, timeout):
    for process in processes:
        process.join(timeout=timeout)
        process.terminate()

def get_success_percentile(processes):
    success = 0
    for process in processes:
        if process.exitcode == 0:
            success += 1
    return (success * 100)/len(processes)

def random_string(prefix):
    return prefix+''.join(random.choice(string.hexdigits) for _ in range(4))

def sig_handler(_signo, _stack_frame):
    raise KeyboardInterrupt

def main():
    signal.signal(signal.SIGTERM, sig_handler)
    pargs = parse_cli(sys.argv[1:])
    obj = ScaleTest(pargs)
    obj.setUp()
    if pargs.cleanup:
        print('Cleaning up all the objects')
        import pdb; pdb.set_trace()
        obj.cleanup()

if __name__ == '__main__':
    #logging.basicConfig(filename='scale.log', filemode='w')
    #logger=logging.getLogger()
    #logger.setLevel(logging.INFO)
    main()
