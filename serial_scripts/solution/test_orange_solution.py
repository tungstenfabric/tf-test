from __future__ import absolute_import
from builtins import str
from builtins import range
from .base import BaseSolutionsTest
from common.heat.base import BaseHeatTest
from tcutils.wrappers import preposttest_wrapper
from common.device_connection import NetconfConnection
import test
from ipam_test import *
from vn_test import *
from quantum_test import *
from floating_ip import FloatingIPFixture
from vm_test import *
from tcutils.test_lib.test_utils import assertEqual
from vnc_api import vnc_api
from vnc_api.gen.resource_test import *
from heat_test import HeatStackFixture
from nova_test import *
from tcutils.contrail_status_check import *
from random import randint
import os
import yaml
import time
import glob
from scripts.analytics.test_analytics import AnalyticsTestSanity
import pdb
#Set RHOSP_16 env to True for rhosp-16 deployments to use podman.
DOCKER='podman' if bool(os.getenv('RHOSP_16',False)) == True else 'docker'

VSRX_RESTART=int(540) #it takes 9min for 400+ ge sub-interfaces to come up.
CONVERGENCE_TIME=int(90)
NETWORK_RESTART_TIME=int(120)

class OrangeSolutionTest(BaseSolutionsTest):

    @classmethod
    def setUpClass(cls):
        super(OrangeSolutionTest, cls).setUpClass()
        #Can update deployment path based on variable.
        cls.deploy_path=os.getenv('DEPLOYMENT_PATH',
                            'serial_scripts/solution/topology/mini_deployment/')
        cls.fip=bool(os.getenv("USE_FIP", 'False').lower() in ['true', '1'])
        cls.setup_vepg()

    @classmethod
    def tearDownClass(cls):
        cls.delete_vepg()
        super(OrangeSolutionTest, cls).tearDownClass()

    @classmethod
    def setup_vepg(cls):

        if "orange" in cls.deploy_path:
            ## TBD - NEED TO DERIVE VALUES BASED ON INPUTS
            cls.NB_VSFO_CP_NODES=2
            cls.NB_VSFO_UP_NODES=2
            #vSFO CP sizing
            cls.NB_VSFO_CP_EXT_NIC=1
            cls.NB_VSFO_CP_SIGIF=3
            cls.NB_APN_RADIUS=5
            # vSFO UP sizing
            cls.NB_VSFO_UP_EXT_NIC=4
            cls.NB_VSFO_UP_CNNIC=2
            cls.NB_VSFO_UP_CNIF=2
            cls.NB_APN=100
            cls.NB_BGP_PREFIXES_PER_APN=384
        else:
            ## TBD - NEED TO DERIVE VALUES BASED ON INPUTS
            cls.NB_VSFO_CP_NODES=1
            cls.NB_VSFO_UP_NODES=1
            #vSFO CP sizing
            cls.NB_VSFO_CP_EXT_NIC=1
            cls.NB_VSFO_CP_SIGIF=3
            cls.NB_APN_RADIUS=5
            # vSFO UP sizing
            cls.NB_VSFO_UP_EXT_NIC=2
            cls.NB_VSFO_UP_CNNIC=1
            cls.NB_VSFO_UP_CNIF=2
            cls.NB_APN=5
            cls.NB_BGP_PREFIXES_PER_APN=10

    #Quota Create.
        cls.quota_env_file=cls.deploy_path+"env/quota.yaml"
        with open(cls.quota_env_file, 'r') as fd:
            cls.quota_env = yaml.load(fd, Loader=yaml.FullLoader)

        cls.quota_template_file=cls.deploy_path+"template/quota.yaml"
        with open(cls.quota_template_file, 'r') as fd:
            cls.quota_template = yaml.load(fd, Loader=yaml.FullLoader)

        #Update env with project name.
        cls.quota_env['parameters']['project'] = cls.connections.project_name
        cls.quota_stack = HeatStackFixture(
                              connections=cls.connections,
                              stack_name=cls.connections.project_name+'_quota',
                              template=cls.quota_template, env=cls.quota_env)
        cls.quota_stack.setUp()

    #Image Upload.
        cls.vrp31_image = cls.nova_h.get_image('VRP31-IMAGE')
        cls.vrp32_image = cls.nova_h.get_image('VRP32-IMAGE')
        cls.vsfo_cp1_image = cls.nova_h.get_image('VSFO-CP1-IMAGE')
        cls.vsfo_cp2_image = cls.nova_h.get_image('VSFO-CP2-IMAGE')
        cls.vsfo_up3_image = cls.nova_h.get_image('VSFO-UP3-IMAGE')
        cls.vsfo_up4_image = cls.nova_h.get_image('VSFO-UP4-IMAGE')

    #Flavor Create.
        cls.flavors_template_file=cls.deploy_path+"template/flavors.yaml"
        with open(cls.flavors_template_file, 'r') as fd:
            cls.flavors_template = yaml.load(fd, Loader=yaml.FullLoader)

        cls.flavors_stack = HeatStackFixture(
                              connections=cls.connections,
                              stack_name=cls.connections.project_name+'_flavors',
                              template=cls.flavors_template)
        cls.flavors_stack.setUp()

    #AZ Create.
        cls.agg_id = {}
        if not cls.inputs.dpdk_ips:
            cls.agg_id['kernel-computes'] = cls.connections.orch.create_agg(
                                                'kernel-computes',
                                                'kernel-computes')
            host_list = cls.connections.orch.get_hosts()
            cls.nova_hosts = copy.deepcopy(host_list)
            cls.connections.orch.add_host_to_agg(cls.agg_id['kernel-computes'],
                                                 cls.nova_hosts)
        else:
            cls.agg_id['kernel-computes'] = cls.connections.orch.create_agg(
                                                'kernel-computes',
                                                'kernel-computes')
            cls.agg_id['dpdk-computes'] = cls.connections.orch.create_agg(
                                              'dpdk-computes',
                                              'dpdk-computes')
            host_list = cls.connections.orch.get_hosts()
            cls.dpdk_hosts = [cls.inputs.host_data[host]['fqname'] \
                                 for host in cls.inputs.dpdk_ips]
            cls.nova_hosts = copy.deepcopy(host_list)
            for host in host_list:
                if host in cls.dpdk_hosts:
                    cls.nova_hosts.remove(host)
            cls.connections.orch.add_host_to_agg(cls.agg_id['kernel-computes'],
                                                 cls.nova_hosts)    
            cls.connections.orch.add_host_to_agg(cls.agg_id['dpdk-computes'],
                                                 cls.dpdk_hosts)    

    #Floating IP creation.
        if cls.fip == True:
            #Create IPAM
            cls.ipam_obj = IPAMFixture(connections=cls.connections,
                                       name='public-net')
            cls.ipam_obj.setUp()
            cls.ipam_obj.verify_on_setup()

            #Create VN
            cls.pub_vn_fixture = VNFixture(
                                     project_name=cls.project.project_name,
                                     connections=cls.connections,
                                     vn_name='public-net',
                                     inputs=cls.inputs,
                                     subnets=[cls.inputs.fip_pool],
                                     ipam_fq_name=cls.ipam_obj.fq_name)
            cls.pub_vn_fixture.setUp()
            cls.pub_vn_fixture.verify_on_setup()

            #Create FIP pool
            cls.fip_fixture = FloatingIPFixture(
                                  project_name=cls.project.project_name,
                                  connections=cls.connections,
                                  inputs=cls.inputs,
                                  pool_name='public-net',
                                  vn_id=cls.pub_vn_fixture.vn_id)
            cls.fip_fixture.setUp()
            cls.fip_fixture.verify_on_setup()

            #Create FIP stack
            cls.fip_template_file=cls.deploy_path+"template/vepg_floating.yaml"
            with open(cls.fip_template_file, 'r') as fd:
                cls.fip_template = yaml.load(fd, Loader=yaml.FullLoader)

            cls.fip_stack = HeatStackFixture(
                                connections=cls.connections,
                                stack_name=cls.connections.project_name+'_fip',
                                template=cls.fip_template)
            cls.fip_stack.setUp()

            #Create FIP assignment env parameter for vepg creation.
            cls.fip_env_file=cls.deploy_path+"env/vepg_b2b_main.yaml"
            with open(cls.fip_env_file, 'r') as fd:
                cls.fip_env = yaml.load(fd, Loader=yaml.FullLoader)

            for fip_dict in cls.fip_stack.heat_client_obj.stacks.get(
                                cls.fip_stack.stack_name).outputs:
                if 'floatip' in fip_dict['output_key']:
                    if cls.fip_env['parameters'] is not None:
                        cls.fip_env['parameters'].update(
                            {fip_dict['output_key']:fip_dict['output_value']})
                    else:
                        cls.fip_env['parameters'] = \
                            {fip_dict['output_key']:fip_dict['output_value']}

    #Create VEPG.
        if cls.fip == True:
            cls.vepg_template_file=cls.deploy_path+"template/vepg_b2b_main.yaml"
            with open(cls.vepg_template_file, 'r') as fd:
                cls.vepg_template = yaml.load(fd, Loader=yaml.FullLoader)

            for each_resource in cls.vepg_template['resources']:
                if 'personality' in cls.vepg_template['resources']\
                                        [each_resource]['properties']:
                    inject_file='/config/junos-config/configuration.txt'
                    fp1=open(cls.vepg_template['resources'][each_resource]\
                                 ['properties']['personality'][inject_file]\
                                 ['get_file'], 'r')
                    data=fp1.read()
                    cls.vepg_template['resources'][each_resource]['properties']\
                        ['personality'][inject_file]=data
                    fp1.close()
                    if 'commit_config' in "".join(cls.vepg_template['resources']\
                                              [each_resource]['properties']\
                                              ['personality'].keys()):
                        inject_file='/config/junos-config/commit_config.sh'
                        fp2=open(cls.vepg_template['resources'][each_resource]\
                                 ['properties']['personality'][inject_file]\
                                 ['get_file'], 'r')
                        data2=fp2.read()
                        cls.vepg_template['resources'][each_resource]\
                            ['properties']['personality'][inject_file]=data2
                        fp2.close()

            cls.vepg_stack = HeatStackFixture(
                                 connections=cls.connections,
                                 stack_name=cls.connections.project_name+'_vepg',
                                 template=cls.vepg_template, env=cls.fip_env,
                                 timeout_mins=15)
            cls.vepg_stack.setUp()
        else:
            cls.vepg_template_file=cls.deploy_path+"template/vepg_b2b_main.yaml"
            with open(cls.vepg_template_file, 'r') as fd:
                cls.vepg_template = yaml.load(fd, Loader=yaml.FullLoader)

            for each_resource in cls.vepg_template['resources']:
                if 'personality' in cls.vepg_template['resources']\
                                        [each_resource]['properties']:
                    inject_file='/config/junos-config/configuration.txt'
                    fp1=open(cls.vepg_template['resources'][each_resource]\
                                 ['properties']['personality'][inject_file]\
                                 ['get_file'], 'r')
                    data=fp1.read()
                    cls.vepg_template['resources'][each_resource]['properties']\
                        ['personality'][inject_file]=data
                    fp1.close()
 
            cls.vepg_stack = HeatStackFixture(
                                 connections=cls.connections,
                                 stack_name=cls.connections.project_name+'_vepg',
                                 template=cls.vepg_template,
                                 timeout_mins=15)
            cls.vepg_stack.setUp()

    # Get VM details and setup vsrx
        cls.logger.info("########## Sleeping for 10 Min before proceeding with VM verification ##########")
        time.sleep(7*CONVERGENCE_TIME)
        op = cls.vepg_stack.heat_client_obj.stacks.get(
                 cls.vepg_stack.stack_name).outputs
        vsfo_fix = dict()
        for output in op:
            key = output['output_key']
            for i in range(1,cls.NB_VSFO_CP_NODES+1):
                vsfo = "vsfo_%s_id" %(i)
                if key == vsfo:
                    vsfo_uuid = output['output_value']
                    vsfo_fix[i] = VMFixture(connections=cls.connections,uuid = vsfo_uuid, image_name = 'VSFO-CP-IMAGE')
                    vsfo_fix[i].read()
                    vsfo_fix[i].verify_on_setup()
                i = i + 1

            for i in range(cls.NB_VSFO_CP_NODES+1 ,cls.NB_VSFO_CP_NODES + cls.NB_VSFO_UP_NODES+1):
                vsfo = "vsfo_%s_id" %(i)
                if key == vsfo:
                    vsfo_uuid = output['output_value']
                    vsfo_fix[i] = VMFixture(connections=cls.connections,uuid = vsfo_uuid, image_name = 'VSFO-UP-IMAGE')
                    vsfo_fix[i].read()
                    vsfo_fix[i].verify_on_setup()
                i = i+1

            if key == "vrp_31_id":
                vrp31_uuid = output['output_value']
                vrp_31 = VMFixture(connections=cls.connections,uuid = vrp31_uuid, image_name = 'VRP-IMAGE')
                vrp_31.read()
                vrp_31.verify_on_setup()

            if key == "vrp_32_id":
                vrp32_uuid = output['output_value']
                vrp_32 = VMFixture(connections=cls.connections,uuid = vrp32_uuid, image_name = 'VRP-IMAGE')
                vrp_32.read()
                vrp_32.verify_on_setup()

        cls.vsfo_fix = vsfo_fix
        cls.vrp_31 = vrp_31
        cls.vrp_32 = vrp_32

    # Create BGPaaS stacks.
        #Define variables for template file, env file, bgpaas stack and
        #bfd_health_check_uuid
        cls.bgpaas_stack_status=True
        cls.bgpaas_env_f=glob.glob(cls.deploy_path+'env/VEPG_BGP*')
        cls.bgpaas_template_f=[]
        cls.bgpaas_env={}
        cls.bgpaas_template={}
        cls.bfd_hc_uuid=None
        cls.bgpaas_stacks={}
        #Get bfd_health_check_uuid from the vepg stack created earlier.
        for list_item in cls.vepg_stack.heat_client_obj.stacks.get(
                                            cls.vepg_stack.stack_name).outputs:
            if list_item['output_key'] == 'bfd_health_check':
                cls.bfd_hc_uuid=list_item['output_value']
        #Fail if no bfd_health_check_uuid received.
        if not cls.bfd_hc_uuid:
            cls.logger.error("No BFD Health check uuid found !!!")
            cls.bgpaas_stack_status=False
            return False
        #Create BGPaaS stack for each template file using corresponding env file
        #from env dir.
        for each_bef in cls.bgpaas_env_f:
            with open(each_bef, 'r') as fd:
                cls.bgpaas_env[each_bef] = yaml.load(fd, Loader=yaml.FullLoader)
            t1=re.findall("VSFO\d", each_bef)
            t2=re.findall("EXT\d", each_bef)
            #for each of the env file create vsfo_key to get vsfo uuid from
            #vepg stack.
            vsfo_key=t1[0].lower()[:4]+'_'+t1[0].lower()[4:]+'_'+\
                         t2[0].lower()[:3]+'_'+t2[0].lower()[3:]
            vsfo_uuid=None
            for list_item in cls.vepg_stack.heat_client_obj.stacks.get(
                                            cls.vepg_stack.stack_name).outputs:
                if list_item['output_key'] == vsfo_key:
                    #get vsfo uuid to be updated in env file
                    vsfo_uuid=list_item['output_value']
                    break
            vsfo_env_key=None
            #get the vsfo key name from env file that needs to be updated with
            #the uuid.
            for key, value in cls.bgpaas_env[each_bef]['parameters'].items():
                if 'vsfo' in key:
                    vsfo_env_key=key
            #update the bfd_health_check_uuid in env file.
            cls.bgpaas_env[each_bef]['parameters']['bfd_health_check_uuid']=\
                                                                cls.bfd_hc_uuid
            #update the vsfo_env_key in env file.
            cls.bgpaas_env[each_bef]['parameters'][vsfo_env_key]=vsfo_uuid
            #create string to find relevant template files for this
            #environment file.
            t=t1[0].lower()+'_'+t2[0].lower()
            cls.bgpaas_template_f=glob.glob(cls.deploy_path+'template/'+t+'*')
            #Create BGPaaS stack for each template file for this env.
            for each_btf in cls.bgpaas_template_f:
                #generate stack name based on env file name and number of APN's.
                stack_name=re.findall('VEPG\w*',each_bef)[0]+\
                               re.findall('apn_\d*_\d*',each_btf)[0][3:]
                with open(each_btf, 'r') as fd:
                    cls.bgpaas_template[each_btf] = yaml.load(fd,
                                                        Loader=yaml.FullLoader)
                cls.bgpaas_stacks[stack_name] = HeatStackFixture(
                                                    connections=cls.connections,
                                                    stack_name=stack_name,
                                                    template=cls.bgpaas_template[each_btf],
                                                    env=cls.bgpaas_env[each_bef],
                                                    timeout_mins=10)
                cls.bgpaas_stacks[stack_name].setUp()
        time.sleep(CONVERGENCE_TIME)
        for i in range(10):
            try:
                assert self.verify_bgp_session_state()
            except:
                time.sleep(3)
                continue
            else:
                break

    #end setup_vepg

    @classmethod
    def delete_vepg(cls):
        for each_stack in cls.bgpaas_stacks:
            for i in range(10):
                try:
                    cls.bgpaas_stacks[each_stack].cleanUp()
                except:
                    time.sleep(10)
                    continue
                else:
                    break

        #Delete vepg Stack
        for i in range(10):
            try:
                cls.vepg_stack.cleanUp()
            except:
                time.sleep(10)
                continue
            else:
                break

        #Delete fip stack, fip pool VN and ipam.
        if 'orange' in cls.deploy_path:
            cls.fip_stack.cleanUp()
            cls.fip_fixture.cleanUp()
            cls.pub_vn_fixture.cleanUp()
            cls.ipam_obj.cleanUp()

        #Delete AZ
        cls.connections.orch.del_host_from_agg(cls.agg_id['kernel-computes'],
                                               cls.nova_hosts)
        cls.connections.orch.delete_agg(cls.agg_id['kernel-computes'])
        if 'dpdk_hosts' in dir(cls):
            cls.connections.orch.del_host_from_agg(cls.agg_id['dpdk-computes'],
                                                   cls.dpdk_hosts)
            cls.connections.orch.delete_agg(cls.agg_id['dpdk-computes'])

        #Delete Flavor Stack
        cls.flavors_stack.cleanUp()

        #Delete Quota Stack
        cls.quota_stack.cleanUp()
        return True
    #end delete_vepg

    @preposttest_wrapper
    def test_01_verify_post_deploy(self):
        ''' Verify following, post Orange solution deployment at scale.
            1. OSPF session state.
            2. BGP sessions in vsfo control and data plane.
            3. BFD sessions.
            4. Routes in vsfo control and data plane.
            5. BGPaaS sessions in control nodes.
            6. BGPaaS routes in control nodes.
        '''
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_bgpaas_routes_ctrlnode()
    # end test_01_verify_post_deploy

    @preposttest_wrapper
    def test_02_interface_check(self):
        ''' CEM-16881
            Check virtual instances are properly started with network connectivity.
        '''

        ret=True
        ips_list=[]
        vm_fix_list=[self.vrp_31, self.vrp_32]

        #get list of all vm fixtures
        for i in range(1, self.NB_VSFO_CP_NODES + self.NB_VSFO_UP_NODES+1):
            vm_fix_list.append(self.vsfo_fix[i])

        #get ge-0/0/0.0 i/f ip of each vm
        for i in range(0, self.NB_VSFO_CP_NODES + self.NB_VSFO_UP_NODES+2):
            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o \
                   UserKnownHostsFile=/dev/null \
                   \"%s@%s\"  sshpass -p contrail123 ssh -o StrictHostKeyChecking=no \
                   -o UserKnownHostsFile=/dev/null root@%s \
                   \"ifconfig | grep 192.3.1 | cut -d ' ' -f 4 | cut -d = -f 2\""\
                   %(self.inputs.host_data[vm_fix_list[i].vm_node_ip]['username'] ,
                     vm_fix_list[i].vm_node_ip,vm_fix_list[i].local_ip)
            output = os.popen(cmd).read()
            output1=output.replace("\n","")
            ips_list.append(output1)

        #each vm should ping every other adjacent vm (ex: 4 vms, 6 ping sessions)
        for i in range(0, self.NB_VSFO_CP_NODES + self.NB_VSFO_UP_NODES+2):
            #loop to perform ping
            for j in range(i+1, self.NB_VSFO_CP_NODES + self.NB_VSFO_UP_NODES+2):
                cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o \
                       UserKnownHostsFile=/dev/null \
                       \"%s@%s\" sshpass -p contrail123 ssh -o StrictHostKeyChecking=no \
                       -o UserKnownHostsFile=/dev/null \
                       root@%s  \"ping -c 3 %s\""\
                       %(self.inputs.host_data[vm_fix_list[i].vm_node_ip]['username'] ,
                         vm_fix_list[i].vm_node_ip,vm_fix_list[i].local_ip,ips_list[j])
                output = os.popen(cmd).read()
                print(output)
                if ' 0% packet loss' not in output:
                    self.logger.error(" Ping from %s to %s FAILED!!",
                     vm_fix_list[i].vm_name,vm_fix_list[j].vm_name)
                    ret=ret and False
                else:
                    self.logger.info(" Ping from %s to %s PASSED!!",
                     vm_fix_list[i].vm_name,vm_fix_list[j].vm_name)

        return ret
    # end test_02_interface_check

    @preposttest_wrapper
    def test_03_giant_frame_test(self):
        ''' CEM-16882
            This test is required to check traffic with high Ethernet size are able
            to be carried accross the Contrail RedHat OpenStack platform.
        '''

        ret=True
        #copy set_mtu file and commit mtu config on up-vsfo
        for i in range (self.NB_VSFO_CP_NODES+1 ,self.NB_VSFO_CP_NODES +\
                        self.NB_VSFO_UP_NODES+1):
            self.vsfo_fix[i].vm_password='contrail123'
            file_name=self.deploy_path+'vsrx_config/'+\
                      'set_mtu.sh'
            cmd='sshpass -p \'%s\'' %(self.vsfo_fix[i].vm_password)
            cmd=cmd+' scp -o StrictHostKeyChecking=no %s heat-admin@%s:/tmp/'\
                %(file_name, self.vsfo_fix[i].vm_node_ip)
            op=os.system(cmd)
            if op is not 0:
                self.logger.error("Failed to copy file %s to %s"\
                    %(file_name, self.vsfo_fix[i].vm_node_ip))
                ret=False
            file_name='/tmp/'+'set_mtu.sh'
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
                 sshpass -p \'%s\' scp -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null %s root@%s:/tmp/'\
                 %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
                 self.vsfo_fix[i].vm_password, file_name,
                 self.vsfo_fix[i].local_ip)
            op=os.system(cmd)
            if op is not 0:
                self.logger.error("Failed to copy file %s to %s"\
                    %(file_name, self.vsfo_fix[i].local_ip))
                ret=False
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
                 sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null \
                 root@%s \'sh /tmp/set_mtu.sh\' '\
                 %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
                 self.vsfo_fix[i].vm_password, self.vsfo_fix[i].local_ip)
            op=os.popen(cmd).read()
            if 'commit complete' not in op:
                self.logger.error("Failed to commit config on %s"\
                    %(self.vsfo_fix[i].vm_name))
                ret=False

        #set mtu on vhost0 of computes hosting vsfo
        for i in range(self.NB_VSFO_CP_NODES+1 ,self.NB_VSFO_CP_NODES +\
                        self.NB_VSFO_UP_NODES+1):
            cmd='ssh -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null \
                 heat-admin@%s \
                 \'sudo ifconfig vhost0 mtu 9000 up\' '\
                 %(self.vsfo_fix[i].vm_node_ip)
            os.system(cmd)
            #check if correct mtu set on vhost0
            cmd='ssh -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null \
                 heat-admin@%s \'sudo ip ad | grep vhost0| grep mtu |\
                 cut -d " " -f 5\' '\
                 %(self.vsfo_fix[i].vm_node_ip)
            output = os.popen(cmd).read()
            if '9000' not in output:
                self.logger.error("Failed to set mtu on vhost0!")
                ret=False
            else:
                self.logger.info(" mtu set on vhost0!")

        #get the vsfo-up ge-0/0/0 ip
        ips_list=[]
        for i in range(self.NB_VSFO_CP_NODES+1 ,self.NB_VSFO_CP_NODES +\
                        self.NB_VSFO_UP_NODES+1):
            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o \
                   UserKnownHostsFile=/dev/null \
                   \"%s@%s\" sshpass -p contrail123 ssh -o StrictHostKeyChecking=no \
                   -o UserKnownHostsFile=/dev/null root@%s \
                   \"ifconfig | grep 192.3.1 | cut -d ' ' -f 4 | cut -d = -f 2\""\
                   %(self.inputs.host_data[self.vsfo_fix[i].vm_node_ip]['username'] ,
                   self.vsfo_fix[i].vm_node_ip,self.vsfo_fix[i].local_ip)
            output = os.popen(cmd).read()
            output1=output.replace("\n","")
            ips_list.append(output1)

        #send jumbo frames across up-vsfo from last up-vsfo
        j=self.NB_VSFO_CP_NODES + self.NB_VSFO_UP_NODES
        k=0
        for i in range(self.NB_VSFO_CP_NODES+1 ,self.NB_VSFO_CP_NODES +\
                        self.NB_VSFO_UP_NODES):
            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o \
                   UserKnownHostsFile=/dev/null \
                   \"%s@%s\" sshpass -p contrail123 ssh -o StrictHostKeyChecking=no \
                   -o UserKnownHostsFile=/dev/null \
                   root@%s  \"ping -c 3 -s 8910 -d %s\""\
                   %(self.inputs.host_data[self.vsfo_fix[j].vm_node_ip]['username'] ,
                   self.vsfo_fix[j].vm_node_ip,self.vsfo_fix[j].local_ip,ips_list[k])
            output = os.popen(cmd).read()
            print(output)
            k=k+1
            if ' 0% packet loss' not in output:
                self.logger.error(" Ping from %s to %s FAILED!!",
                     self.vsfo_fix[j].vm_name,self.vsfo_fix[i].vm_name)
                ret=False
            else:
                self.logger.info(" Ping from %s to %s PASSED!!",
                     self.vsfo_fix[j].vm_name,self.vsfo_fix[i].vm_name)

        return ret
    # end test_03_giant_frame_test

    @preposttest_wrapper
    def test_04_check_tls(self):
        ''' CEM-16894
            Check TLS feature is enabled.
        '''
        AnalyticsTestSanity.test_redis_stunnel_provision(self)
        return True
    # end test_04_check_tls

    @preposttest_wrapper
    def test_05_bfd_bgpaas_feature(self):
        ''' CEM-16889 & CEM-16891
            Check BFD sessions are established to UP.
            Check BGP sessions are established and all UP.
            Check interfaces are up and running.
            -Check BGP prefixes are well sent and received.
            Check that BFD session is going down when the interface is being
            shut onto the instance.
            ** TBD **
            Check IP traffic (ping) can be established between some IP belonging
            to announced and/or received prefixes. - Need a host behind the MX-GW
            to run such tests. Planned for later.
        '''
        #Check bgp and bfd sessions.
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_bgpaas_routes_ctrlnode()

        #Deactivate interface on a random user plane vsfo.
        i=randint(self.NB_VSFO_CP_NODES+1 ,self.NB_VSFO_CP_NODES +\
                  self.NB_VSFO_UP_NODES)
        self.vsfo_fix[i].vm_password='contrail123'
        file_name=self.deploy_path+'vsrx_config/'+\
                  'deactivate_interface.sh'
        cmd='sshpass -p \'%s\'' %(self.vsfo_fix[i].vm_password)
        cmd=cmd+' scp -o StrictHostKeyChecking=no %s heat-admin@%s:/tmp/'\
            %(file_name, self.vsfo_fix[i].vm_node_ip)
        op=os.system(cmd)
        if op is not 0:
            self.logger.error("Failed to copy deactivate interface file %s to %s"\
                %(file_name, self.vsfo_fix[i].vm_node_ip))
        file_name='/tmp/'+'deactivate_interface.sh'
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' scp -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null %s root@%s:/tmp/'\
             %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
               self.vsfo_fix[i].vm_password, file_name,
               self.vsfo_fix[i].local_ip)
        op=os.system(cmd)
        if op is not 0:
            self.logger.error("Failed to copy deactivate interface file %s to %s"\
                %(file_name, self.vsfo_fix[i].local_ip))
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null \
             root@%s \'sh /tmp/deactivate_interface.sh\' '\
             %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
               self.vsfo_fix[i].vm_password, self.vsfo_fix[i].local_ip)
        op=os.popen(cmd).read()
        if 'commit complete' not in op:
            self.logger.error("Failed to commit config on %s"\
                %(self.vsfo_fix[i].vm_name))

        #Check bgp and bfd sessions.
        for trial in range(3):
            time.sleep(CONVERGENCE_TIME)
            try:
                self.assertFalse(self.verify_bgpaas_session_ctrlnode())
                self.assertFalse(self.verify_bgpaas_routes_ctrlnode())
                self.assertFalse(self.verify_bgp_session_state())
            except:
                continue
            else:
                break

        #Aactivate interface the interface and check bfd sessions are up again.
        file_name=self.deploy_path+'vsrx_config/'+\
                  'activate_interface.sh'
        cmd='sshpass -p \'%s\'' %(self.vsfo_fix[i].vm_password)
        cmd=cmd+' scp -o StrictHostKeyChecking=no %s heat-admin@%s:/tmp/'\
            %(file_name, self.vsfo_fix[i].vm_node_ip)
        op=os.system(cmd)
        if op is not 0:
            self.logger.error("Failed to copy activate interface file %s to %s"\
                %(file_name, self.vsfo_fix[i].vm_node_ip))
        file_name='/tmp/'+'activate_interface.sh'
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' scp -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null %s root@%s:/tmp/'\
             %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
               self.vsfo_fix[i].vm_password, file_name,
               self.vsfo_fix[i].local_ip)
        op=os.system(cmd)
        if op is not 0:
            self.logger.error("Failed to copy activate interface file %s to %s"\
                %(file_name, self.vsfo_fix[i].local_ip))
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null \
             root@%s \'sh /tmp/activate_interface.sh\' '\
             %(self.vsfo_fix[i].vm_password, self.vsfo_fix[i].vm_node_ip,
               self.vsfo_fix[i].vm_password, self.vsfo_fix[i].local_ip)
        op=os.popen(cmd).read()
        if 'commit complete' not in op:
            self.logger.error("Failed to commit config on %s"\
                %(self.vsfo_fix[i].vm_name))

        #Check bgp and bfd sessions.
        for trial in range(3):
            time.sleep(CONVERGENCE_TIME)
            try:
                assert self.verify_bgpaas_session_ctrlnode()
                assert self.verify_bgpaas_routes_ctrlnode()
                assert self.verify_bgp_session_state()
            except:
                continue
            else:
                break

        return True
    # end test_05_bfd_bgpaas_feature

    @preposttest_wrapper
    def test_06_sdn_gw_feature(self):
        ''' CEM-16892
            This test is required to check BGP routing information exchange with
            SDN GW is working well.
            Some prefixes are announced by the SDN gateway.
            Some Virtual Networks are announced by Contrail.
            Verification:-
              - Check BGP sessions are all UP.
              - Check BGP prefixes are well sent and received.
              - Check IP traffic (ping) can be established between virtual instances
                and IP addresses belonging to external prefixes announced by the SDN
                Gateway.
        '''

        router_params = list(self.inputs.physical_routers_data.values())[0]
        mx_ip=router_params['control_ip']
        mx_pswd=router_params['ssh_password']
        # 4 VN's are created through heat template in Orange deployment with
        # rt -- 65000:3029 and each VN anounces 386 route prefixes. So we expect
        # 386*4 = 1544 active route prefixes in total.
        total_announced_prefix=1544
        rd = "65000:3029"
        rt = "target:65000:3029"
        ri_interface = "lo0.9"
        ri_ip='99.99.99.99'
        cmds = []
        cmds.append("set interfaces lo0 unit 9 family inet address %s/32" %ri_ip)
        cmds.append("set routing-instances contrail-window-mx1 instance-type vrf")
        cmds.append("set routing-instances contrail-window-mx1 interface %s"\
                     %ri_interface)
        cmds.append("set routing-instances contrail-window-mx1 \
                     route-distinguisher %s" %rd)
        cmds.append("set routing-instances contrail-window-mx1 vrf-target %s" %rt)

        # Configure MX.
        mx_handle = NetconfConnection(host=mx_ip)
        mx_handle.connect()
        cli_output = mx_handle.config(stmts=cmds, ignore_errors=False,
                                      timeout=120)
        mx_handle.disconnect()
        assert cli_output[0], "Not able to push config to mx."

        # Clear BGP neighborship
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null root@%s \
             \'cli clear bgp neighbor all\' ' %(mx_pswd, mx_ip)
        op=os.popen(cmd).read()
        if 'Cleared 3 connections' not in op:
            assert False, 'Failed to clear BGP neighborship.'
        time.sleep(CONVERGENCE_TIME)

        # Check BGP sessions are all UP
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null root@%s \
             \'cli show bgp summary | grep Est | wc -l\' ' %(mx_pswd, mx_ip)
        op=os.popen(cmd).read()
        self.assertEqual(int(op.strip()),
                         len(self.inputs.bgp_ips),
                         'All BGP neighbors are not in Established state.')

        # Check BGP prefixes are well sent and received
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null root@%s \
             \'cli show bgp group | grep bgp.l3vpn.0 | grep /\' ' %(mx_pswd, mx_ip)
        op=os.popen(cmd).read()
        self.assertEqual(int(op.split()[1].split('/')[0]),
                         total_announced_prefix,
                         '386 routes per VN * 4 VNs with route target 65000:3029.\
                          Total expected 1544 active routes not seen on the MX.')

        # Check IP traffic (ping) can be established between virtual
        # instances and IP addresses belonging to external prefixes
        # announced by the SDN Gateway.
        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null root@%s \'cli show route | grep %s\''\
             %(self.vsfo_fix[4].vm_password, self.vsfo_fix[4].vm_node_ip,
               self.vsfo_fix[4].vm_password, self.vsfo_fix[4].local_ip, ri_ip)
        op=os.popen(cmd).read()
        assert (len(op.split('\n')) > 0),\
            'Routes announced by SDN GW not seen in the VM.'

        cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no heat-admin@%s \
             sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no -o \
             UserKnownHostsFile=/dev/null root@%s \
             \'cli ping routing-instance apn_3029_ext4_vpn %s count 10\''\
             %(self.vsfo_fix[4].vm_password, self.vsfo_fix[4].vm_node_ip,
               self.vsfo_fix[4].vm_password, self.vsfo_fix[4].local_ip, ri_ip)
        op=os.popen(cmd).read()
        assert (' 0% packet loss' in op),\
            'Failed to ping external prefixes announced by the SDN GW.'

    # end test_06_sdn_gw_feature

    @preposttest_wrapper
    def test_07_ha_resiliency(self):
        ''' CEM-16886
            Shut one of the 3 contrail physical controller nodes
            (hosting 3 instances : control, analytics and analytics database).
            No impact is seen.
        '''
        self.cn_restart=int(os.getenv('CONTROL_RESTART','1'))
        for i in range(0, self.cn_restart):
            active_control_name=self.vsfo_fix[len(self.vsfo_fix)].get_active_controller()
            active_control_ip=self.inputs.host_data[active_control_name]['host_ip']
            self.inputs.restart_service('contrail-control', [active_control_ip],
                                            container='control')
            self.inputs.restart_service('contrail-analytics-api', [active_control_ip],
                                            container='analytics-api')
            time.sleep(CONVERGENCE_TIME)
            assert self.verify_bgpaas_routes_ctrlnode()
            assert self.verify_bgpaas_session_ctrlnode()
            assert self.verify_route_count()

        return True
    # end test_07_ha_resiliency

    @preposttest_wrapper
    def test_08_restart_from_os(self):
        ''' CEM-21753
            Check vsfo up can be restarted from os cli.
            Virtual instance connectivity properly restored once its back online.
            All BGP and BFD sessions are restored after convergence time.
        '''
        self.vm_restart=int(os.getenv('VM_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        os_controller_ip=random.choice(self.inputs.openstack_ips)
        for i in range(0, self.vm_restart):
            vm_fix=random.choice([self.vsfo_fix[3], self.vsfo_fix[4]])
            stop_reboot=random.choice(['stop', 'reboot'])
            if 'stop' in stop_reboot:
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                     heat-admin@%s source overcloudrc\; openstack server \
                     stop %s' \
                     %(self.inputs.password, os_controller_ip, vm_fix.uuid)
                output=os.popen(cmd).read()
                stat_cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                         heat-admin@%s source overcloudrc\; openstack server \
                         show %s | grep status' \
                         %(self.inputs.password, os_controller_ip, vm_fix.uuid)
                for i in range(10):
                    output = os.popen(stat_cmd).read()
                    if 'SHUTOFF' in output:
                        break
                    time.sleep(1)
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                     heat-admin@%s source overcloudrc\; openstack server \
                     start %s' \
                     %(self.inputs.password, os_controller_ip, vm_fix.uuid)
                output = os.popen(cmd).read()
                for i in range(20):
                    output = os.popen(stat_cmd).read()
                    if 'ACTIVE' in output:
                        break
                    time.sleep(3)
            else:
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                     heat-admin@%s source overcloudrc\; openstack server \
                     reboot %s' \
                     %(self.inputs.password, os_controller_ip, vm_fix.uuid)
                output = os.popen(cmd).read()
                stat_cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                         heat-admin@%s source overcloudrc\; openstack server \
                         show %s | grep status' \
                         %(self.inputs.password, os_controller_ip, vm_fix.uuid)
                for i in range(30):
                    output = os.popen(stat_cmd).read()
                    if 'ACTIVE' in output:
                        break
                    time.sleep(3)
            time.sleep(14*CONVERGENCE_TIME)
            exp_bfd=self.NB_VSFO_UP_CNIF*self.NB_APN
            exp_bgp=self.NB_VSFO_UP_CNNIC*self.NB_VSFO_UP_CNIF*self.NB_APN
            for i in range(20):
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                    heat-admin@%s sshpass -p \'%s\' ssh -o \
                    StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                    root@%s \'cli show bgp summary | grep Estab | wc -l\' '\
                    %(self.inputs.password, vm_fix.vm_node_ip, \
                      vm_fix.vm_password, vm_fix.local_ip)
                output = os.popen(cmd).read()
                bgp_s=int(output.replace("\n",""))
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                    heat-admin@%s sshpass -p \'%s\' ssh -o \
                    StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                    root@%s \'cli show bfd session | grep Up | wc -l\' '\
                    %(self.inputs.password, vm_fix.vm_node_ip, \
                      vm_fix.vm_password, vm_fix.local_ip)
                output = os.popen(cmd).read()
                bfd_s=int(output.replace("\n",""))
                if exp_bfd<bfd_s and exp_bgp<bgp_s:
                    break
                time.sleep(30)
                if i==19:
                    self.logger.error("BGP and BFD sessions failed to come up \
                        after VM stop-start or reboot through openstack cli")
            assert self.verify_ospf_session_state()
            assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        return True
    # end test_08_restart_from_os

    @preposttest_wrapper
    def test_09_vsrx_cli_restart(self):
        ''' CEM-22035
            Check vsfo up can be restarted through vsrx cli.
            Virtual instance connectivity properly restored once its back online.
            All BGP and BFD sessions are restored after convergence time.
        '''

        self.cli_restart=int(os.getenv('VM_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()
        for i in range(0, self.cli_restart):
            vm_fix=random.choice([self.vsfo_fix[3], self.vsfo_fix[4]])
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                 heat-admin@%s sshpass -p \'%s\' ssh -o \
                 StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                 root@%s \'cli request system reboot\' '\
                 %(self.inputs.password, vm_fix.vm_node_ip, \
                   vm_fix.vm_password, vm_fix.local_ip)
            output = os.popen(cmd).read()
            if 'Shutdown' not in output:
                self.logger.error("Failed reboot VSRX from cli!")
                continue
            time.sleep(VSRX_RESTART)
            time.sleep(4*CONVERGENCE_TIME)
            assert self.verify_ospf_session_state()
            assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()

        return True
    # end test_09_vsrx_cli_restart

    @preposttest_wrapper
    def test_10_virsh_restart(self):
        ''' CEM-21754
            Check vsfo up can be restarted through virsh.
            Virtual instance connectivity properly restored once its back online.
            All BGP and BFD sessions are restored after convergence time.
        '''
        self.virsh_restart=int(os.getenv('VM_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()
        for i in range(0, self.virsh_restart):
            vm_fix=random.choice([self.vsfo_fix[3], self.vsfo_fix[4]])
            cmd='ssh -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null \
                 heat-admin@%s \
                 \'sudo %s exec -it nova_libvirt virsh list | grep running | cut -d \" \" -f2\' '\
                 %(vm_fix.vm_node_ip, DOCKER)
            output = os.popen(cmd).read()
            cmd='ssh -o StrictHostKeyChecking=no -o \
                 UserKnownHostsFile=/dev/null \
                 heat-admin@%s \
                 \'sudo %s exec -it nova_libvirt virsh reboot %s\' '\
                 %(vm_fix.vm_node_ip, int(output, DOCKER))
            output = os.popen(cmd).read()
            if 'being rebooted' not in output:
                self.logger.error("Failed to reboot instance through virsh!")
                continue
            time.sleep(VSRX_RESTART)
            time.sleep(4*CONVERGENCE_TIME)
            assert self.verify_bgp_session_state()
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()

        return True
    # end test_10_virsh_restart

    @preposttest_wrapper
    def test_11_BGP_session_flap_before_convergence(self):
        ''' CEM-21617
            shut down/deactivate interfaces on the Vsrx
            wait for 30 sec
            bring up the interface
            wait less than the convergence time of 90 sec and repeat interface down
            repeat couple of times
            Wait for convergence time and check
            All BGP and BFD sessions are restored after convergence time.
        '''

        self.bgp_flap=int(os.getenv('BGP_FLAP','20'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()
        vm_fix=random.choice([self.vsfo_fix[3], self.vsfo_fix[4]])
        for i in range(0, self.bgp_flap):
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                 heat-admin@%s sshpass -p \'%s\' ssh -o \
                 StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                 root@%s \'ifconfig ge-0/0/8 down\' '\
                 %(self.inputs.password, vm_fix.vm_node_ip, \
                   vm_fix.vm_password, vm_fix.local_ip)
            output = os.popen(cmd).read()
            time.sleep(30)
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                 heat-admin@%s sshpass -p \'%s\' ssh -o \
                 StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
                 root@%s \'ifconfig ge-0/0/8 up\' '\
                 %(self.inputs.password, vm_fix.vm_node_ip, \
                   vm_fix.vm_password, vm_fix.local_ip)
            output = os.popen(cmd).read()
            time.sleep(CONVERGENCE_TIME/2) #wait for half the convergence time.
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()

        return True
    # end test_11_BGP_session_flap_before_convergence

    @preposttest_wrapper
    def test_12_vrouter_restart(self):
        ''' CEM-16883
            Check vrouter can be restarted.
            Virtual instance connectivity properly restored once the vrouter is back
            to live.
            Coredump is not generated.
        '''
        self.vr_restart=int(os.getenv('VROUTER_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        for i in range(0, self.vr_restart):
            node=random.choice(self.inputs.dpdk_ips)
            self.inputs.restart_service('contrail-vrouter-agent', [node],
                                        container='agent')
            cluster_status, error_nodes = ContrailStatusChecker(
                ).wait_till_contrail_cluster_stable(nodes=[node])
            assert cluster_status, 'Hash of error nodes and services : %s' % (
                error_nodes)
            time.sleep(10*CONVERGENCE_TIME)
            assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        return True
    # end test_12_vrouter_restart

    @preposttest_wrapper
    def test_13_restart_dpdk_compute_hosting_vsfoup(self):
        ''' 
            Restart all dpdk computes hosting vsfo user plane nodes.
            Check all the bgp, bfd, sessions come up fine.
        '''

        self.dpdk_restart=int(os.getenv('DPDK_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        assert self.verify_bgpaas_session_ctrlnode()
        controller_ip=random.choice(self.inputs.openstack_ips)
        
        for node in self.inputs.compute_ips:
            cluster_status, error_nodes = ContrailStatusChecker(
                ).wait_till_contrail_cluster_stable(nodes=[node])
            assert cluster_status, 'Hash of error nodes and services : %s' % (
                    error_nodes)

        #login to undercloud and reboot dpdk computes
        for i in range(0, self.dpdk_restart):
            self.logger.info("#### Starting Reboot of DPDK computes ####")
            node_ip=random.choice(self.inputs.dpdk_ips)
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                 heat-admin@%s \'sudo reboot\' '\
                 %(self.inputs.password, node_ip)
            op=os.popen(cmd).read()
            time.sleep(VSRX_RESTART)

            for node in self.inputs.dpdk_ips:
                cluster_status, error_nodes = ContrailStatusChecker(
                ).wait_till_contrail_cluster_stable(nodes=[node])
                assert cluster_status, 'Hash of error nodes and services : %s' % (
                    error_nodes)

            time.sleep(8*CONVERGENCE_TIME)
            assert self.verify_bgp_session_state()

        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()
        return True
    # end test_13_restart_dpdk_compute_hosting_vsfoup

    @preposttest_wrapper
    def test_14_restart_kernel_compute_hosting_vsfocp(self):
        '''
            Restart kernel computes hosting vsfo control plane nodes.
            Check all the bgp, bfd sessions on up nodes come
            up fine.
        '''
        
        self.kernel_restart=int(os.getenv('KERNEL_RESTART','1'))
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        assert self.verify_bgpaas_session_ctrlnode()

        for node in self.inputs.compute_ips:
            cluster_status, error_nodes = ContrailStatusChecker(
                ).wait_till_contrail_cluster_stable(nodes=[node])
            assert cluster_status, 'Hash of error nodes and services : %s' % (
                    error_nodes)

        nova_compute_ips=[]
        nova_compute_ips=list(set(self.inputs.compute_ips) - \
                              set(self.inputs.dpdk_ips))
        #login to undercloud and reboot kernel computes
        for i in range(0, self.kernel_restart):
            self.logger.info("#### Starting Reboot of KERNEL computes ####")
            node_ip=random.choice(nova_compute_ips)
            cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                 heat-admin@%s \'sudo reboot\' '\
                 %(self.inputs.password, node_ip)
            op=os.popen(cmd).read()
            time.sleep(VSRX_RESTART)

            for node in self.inputs.compute_ips:
                cluster_status, error_nodes = ContrailStatusChecker(
                ).wait_till_contrail_cluster_stable(nodes=[node])
                assert cluster_status, 'Hash of error nodes and services : %s' % (
                    error_nodes)

            time.sleep(8*CONVERGENCE_TIME)
            assert self.verify_bgp_session_state()

        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()
        return True
    # end test_14_restart_kernel_compute_hosting_vsfocp

    @preposttest_wrapper
    def test_15_network_restart_on_compute(self):
        ''' 
            Restart network services on kernel and dpdk computes.
            Verify all bgp, bfd sessions are up.
        '''

        self.vr_restart=int(os.getenv('VROUTER_RESTART','1'))
        kernel_ip=[]
        dpdk_ip=[]
        assert self.verify_ospf_session_state()
        assert self.verify_bgp_session_state()
        assert self.verify_route_count()
        assert self.verify_bgpaas_session_ctrlnode()

        #get separate list of kernel and dpdk compute ips
        for i in range(len(self.inputs.compute_ips)):
            if 'nova' in self.inputs.compute_names[i]:
                kernel_ip.append(self.inputs.compute_ips[i])
            elif 'dpdk' in self.inputs.compute_names[i]:
                 dpdk_ip.append(self.inputs.compute_ips[i])

        #looping through number of restarts
        for i in range(0, self.vr_restart):
            #network restart on kernel computes
            self.logger.info("Performing network Restart on Kernel computes")
            for i in range(len(kernel_ip)):
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                     heat-admin@%s sudo systemctl restart network' \
                     %(self.inputs.password, kernel_ip[i])
                os.system(cmd)

            #network restart on dpdk computes
            self.logger.info("Performing network Restart on DPDK computes")
            for i in range(len(dpdk_ip)):
                cmd='sshpass -p \'%s\' ssh -o StrictHostKeyChecking=no \
                     heat-admin@%s \'sudo %s stop contrail_vrouter_agent contrail-vrouter-agent-dpdk; \
                     sudo ifdown vhost0; \
                     sudo systemctl restart network\'' \
                     %(self.inputs.password, dpdk_ip[i], DOCKER)
                os.system(cmd)
            time.sleep(NETWORK_RESTART_TIME)
            time.sleep(VSRX_RESTART)
            time.sleep(2*CONVERGENCE_TIME)
            assert self.verify_ospf_session_state()
            assert self.verify_bgp_session_state()
            assert self.verify_bgpaas_session_ctrlnode()
        assert self.verify_route_count()   
        return True
    # end test_15_network_restart_on_compute

    @preposttest_wrapper
    @skip_because(deploy_path=os.getenv('DEPLOYMENT_PATH',
                      'serial_scripts/solution/topology/orange_deployment/'))
    def test_16_HC_on_BGPaaS(self):
        ''' CEM-20918(automation - CEM-21921)
            Issue seen before fix:
            At least one interface with BGPaaS configured, and with HC applied
            on the BGPaaS. Leave this HC unconfigured on the VM side, so that
            the agent detects it as down. After some time, all interfaces that
            are internally listed, before the one with HC on BGPaaS, will be
            incorrectly associated with the BGPaaS HC and will show HC as being
            down, at the same time as having BFD up.
        '''

        bgpaas_stack_env_file=glob.glob(self.deploy_path+'env/*VSFO3_EXT3*')
        if not bgpaas_stack_env_file:
            assert False, 'Env file for stack updation doesn\'t exist.\
                           Exiting the test case!!!'
        bgpaas_stack_env=self.bgpaas_env[bgpaas_stack_env_file[0]]
        bgpaas_stack_update_file=glob.glob(self.deploy_path + \
                                           'template/update_vsfo3_ext3*')
        if not bgpaas_stack_update_file:
            assert False, 'Template file for stack updation doesn\'t exist.\
                           Exiting the test case!!!'
        bgpaas_stack_update_template=''
        with open(bgpaas_stack_update_file[0], 'r') as fd:
            bgpaas_stack_update_template = yaml.load(fd, Loader=yaml.FullLoader)
        if self.bgpaas_stacks['VEPG_BGP_VSFO3_EXT3_000_049'].stack_name is None:
            assert False, 'Stack not created, nothing to update.\
                           Exiting the test case!!!'
        self.bgpaas_stacks['VEPG_BGP_VSFO3_EXT3_000_049'].update_template_env(
                                          template=bgpaas_stack_update_template,
                                          env=bgpaas_stack_env)

        #Check the BGP and BFD sessions are stable for 15 min after updating the
        #stack with HC on BGPaaS.
        for i in range(10):
            time.sleep(CONVERGENCE_TIME)
            assert self.verify_bgp_session_state()
            assert self.verify_bgpaas_session_ctrlnode()
        return True
    # end test_16_HC_on_BGPaaS

    @preposttest_wrapper
    def test_run_all_tests(self):
        '''
            Run all the tests after deployment of the solution.
        '''
        self.test_01_verify_post_deploy()
        self.test_02_interface_check()
        self.test_03_giant_frame_test()
        self.test_04_check_tls()
        self.test_05_bfd_bgpaas_feature()
        self.test_06_sdn_gw_feature()
        self.test_07_ha_resiliency()
        self.test_08_restart_from_os()
        self.test_09_vsrx_cli_restart()
        self.test_10_virsh_restart()
        self.test_11_BGP_session_flap_before_convergence()
        self.test_12_vrouter_restart()
        self.test_13_restart_dpdk_compute_hosting_vsfoup()
        self.test_14_restart_kernel_compute_hosting_vsfocp()
        self.test_15_network_restart_on_compute()
        self.test_16_HC_on_BGPaaS()

    # end run_all_tests

#end class OrangeSolutionTest
