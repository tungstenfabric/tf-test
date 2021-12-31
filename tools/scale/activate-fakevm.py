import sys
import argparse
import os
import time
from fabric.api import *

class ActivateScaleVMTest(object):
    def __init__ (self, args):
        self.username = args.username
        self.password = args.password
        self.file = args.filename
        self.create_file = args.filename+'-create'
        self.delete_file = args.filename+'-delete'
        self.computes = args.computes
        self._args = args
    
    def create_scale_vms(self):
        self.copy_files()
        start_time = time.time()
        self.create_fake_vms()
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        print ("============================================")
        print (">> Total Time Taken to Create Fake VMs on compute : %s Seconds <<" %(time_taken))
        print ("============================================")

    def delete_scale_vms(self):
        start_time = time.time()
        self.delete_fake_vms()
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        print ("============================================")
        print (">> Total Time Taken to Delete Fake VMs on compute : %s Seconds <<" %(time_taken))
        print ("============================================")

    def copy_files(self):
        for compute in self.computes:
            os.system("sshpass -p '%s' scp -o StrictHostKeyChecking=no %s %s %s@%s:/root" %(self.password, self.create_file, 
                                                                self.delete_file, self.username, compute))
    
    def create_fake_vms(self):
        for compute in self.computes:
            with settings(host_string='%s@%s'%(self.username, compute),
                      password=self.password, warn_only=True):
                start_time = time.time()
                self.run_fake_vm_file(self.create_file, compute)
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print ("============================================")
                print (">> Time Taken to Create Fake VMs on compute %s : %s Seconds <<" %(compute, time_taken))
                print ("============================================")

    def delete_fake_vms(self):
        for compute in self.computes:
            with settings(host_string='%s@%s'%(self.username, compute),
                      password=self.password, warn_only=True):
                start_time = time.time()
                self.run_fake_vm_file(self.delete_file, compute)
                self.delete_files_from_container(compute)
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print ("============================================")
                print (">> Time Taken to Delete Fake VMs on compute %s : %s Seconds <<" %(compute, time_taken))
                print ("============================================")

    def run_fake_vm_file(self, file, compute):
        with settings(host_string='%s@%s' % (self.username, compute),
                        password=self.password, warn_only=True):
            self.copy_file_to_container(file, compute)
            start_time = time.time()
            sudo("docker exec -it %s bash %s > /dev/null 2>&1" % (self.container(compute), file))

    def copy_file_to_container(self, file, compute):
        with settings(host_string='%s@%s' % (self.username, compute),
                      password=self.password, warn_only=True):
            sudo("docker cp %s %s:/" % (file, self.container(compute))

    def delete_files_from_container(self, compute):
        os.system("sshpass -p '%s' ssh %s@%s rm -rf %s*" % (self.password, self.username, compute, self.file))
        with settings(host_string='%s@%s' % (self.username, compute),
                      password=self.password, warn_only=True):
            sudo("docker exec -it %s rm -rf %s*" % (self.container(compute), self.file))

    def container(self, compute):
        with settings(host_string='%s@%s' % (self.username, compute),
                      password=self.password, warn_only=True):
            container = sudo("docker ps -a| grep agent | awk '{print $NF}'")
        return container



def parse_cli(args):
    '''Define and Parser arguments for the script'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--username',
                        action='store',
                        required=True,
                        help='Login ID')
    parser.add_argument('--password',
                        action='store',
                        required=True,
                        help='Password')
    parser.add_argument('--computes',
                        action='store',
                        default=[],
                        nargs='+',
                        help='Space separated list of compute nodes')
    parser.add_argument('--filename',
                        action='store',
                        default='./scale_fake_vms',
                        help="Filename to write the shell commands to execute on vrouter node")
    parser.add_argument('--cleanup',
                        action='store_true',
                        help='Cleanup the created objects [False]')
    pargs = parser.parse_args(args)
    return pargs

def main():
    args = parse_cli(sys.argv[1:])
    obj = ActivateScaleVMTest(args)
    if args.cleanup:
        obj.delete_scale_vms()
    else:
        obj.create_scale_vms()

if __name__ == '__main__':
    main()

