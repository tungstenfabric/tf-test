from __future__ import absolute_import
from builtins import str
from builtins import range
from .base import BaseSolutionsTest
from common.heat.base import BaseHeatTest
from tcutils.wrappers import preposttest_wrapper
import test
from vn_test import *
from quantum_test import *
from policy_test import *
from vm_test import *
from tcutils.test_lib.test_utils import assertEqual
from vnc_api import vnc_api
from vnc_api.gen.resource_test import *
from heat_test import HeatStackFixture
from nova_test import *
import os
import yaml
import time
import glob

af_test = 'dual'

class OrangeSolutionTest(BaseSolutionsTest):
    _interface = 'json'

    @classmethod
    def setUpClass(cls):
        super(OrangeSolutionTest, cls).setUpClass()
        #Can update deployment path based on variable.
        cls.deploy_path=os.getenv('DEPLOYMENT_PATH',
                            'serial_scripts/solution/topology/mini_deployment/')
        cls.setup_vepg()

    @classmethod
    def tearDownClass(cls):
        cls.delete_vepg()
        super(OrangeSolutionTest, cls).tearDownClass()

    @classmethod
    def setup_vepg(cls):

        ## TBD - NEED TO DERIVE VALUES BASED ON INPUTS
        cls.NB_VSFO_CP_NODES=1
        cls.NB_VSFO_UP_NODES =1
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
        cls.vrp_image = cls.nova_h.get_image('VRP-IMAGE')
        cls.vsfo_cp_image = cls.nova_h.get_image('VSFO-CP-IMAGE')
        cls.vsfo_up_image = cls.nova_h.get_image('VSFO-UP-IMAGE')

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
            cls.dpdk_hosts = [cls.inputs.host_data[host]['name'] \
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
    #TBD. For now setting this know to false, just as a place holder.
        cls.fip = False

    #Create VEPG.
        if cls.fip == True:
            cls.vepg_env_file=cls.deploy_path+"env/vepg_fip_details.yaml"
            with open(cls.vepg_env_file, 'r') as fd:
                cls.vepg_env = yaml.load(fd, Loader=yaml.FullLoader)

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
                                 template=cls.vepg_template, env=cls.vepg_env,
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
            
        #cls.fip = False
        stack_name = cls.connections.project_name+'_vepg'
        op = cls.vepg_stack.heat_client_obj.stacks.get(stack_name).outputs
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
            self.logger.error("No BFD Health check uuid found !!!")
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
        import pdb; pdb.set_trace()

    #end setup_vepg

    @classmethod
    def delete_vepg(cls):
        for each_stack in cls.bgpaas_stacks:
            cls.bgpaas_stacks[each_stack].cleanUp()

        #Delete vepg Stack
        cls.vepg_stack.cleanUp()

        #Delete AZ
        cls.connections.orch.del_host_from_agg(cls.agg_id['kernel-computes'],
                                               cls.nova_hosts)
        cls.connections.orch.delete_agg(cls.agg_id['kernel-computes'])
        if 'dpdk_hosts' in dir(cls):
            cls.connections.orch.del_host_from_agg(cls.agg_id['dpdk-computes'],
                                                   cls.dpdk_hosts)
            cls.connections.orch.delete_agg(self.agg_id['dpdk-computes']) 

        #Delete Flavor Stack
        cls.flavors_stack.cleanUp()

        #Delete Quota Stack
        cls.quota_stack.cleanUp()
        time.sleep(10)
        return True
    #end delete_vepg

    @preposttest_wrapper
    def test_orange_deploy(self):
        ''' Dummy test routine to be changed in later commits.
        '''
        result = True
        self.logger.info("Running test orange deployment.")
        self.logger.info(self.connections.project_name)
        self.logger.info(self.connections.username)

        sleep(10)
        self.logger.info("DONE... Sleeping for 10 secs.")
        return True
    # end test_orange_deploy

    @preposttest_wrapper
    def test_session_state(self):
        ''' Test routine to validate BGP/BFD/OSPF session state.
        '''
        ret = True

        vsfo_fix = self.vsfo_fix
        vrp_31 = self.vrp_31
        vrp_32 = self.vrp_32

        NB_VSFO_CP_NODES= self.NB_VSFO_CP_NODES
        NB_VSFO_UP_NODES=self.NB_VSFO_UP_NODES
        NB_VSFO_CP_EXT_NIC=self.NB_VSFO_CP_EXT_NIC
        NB_VSFO_CP_SIGIF=self.NB_VSFO_CP_SIGIF
        NB_APN_RADIUS=self.NB_APN_RADIUS
        NB_VSFO_UP_EXT_NIC=self.NB_VSFO_UP_EXT_NIC
        NB_VSFO_UP_CNNIC=self.NB_VSFO_UP_CNNIC
        NB_VSFO_UP_CNIF=self.NB_VSFO_UP_CNIF
        NB_APN=self.NB_APN
        NB_BGP_PREFIXES_PER_APN=self.NB_BGP_PREFIXES_PER_APN

        # Validate OSPF session

        cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J \"%s@%s\"  -o GlobalKnownHostsFile=/dev/null root@%s  \"cli\" \"show ospf neighbor\" | grep -c Full" %(self.inputs.host_data[vrp_31.vm_node_ip]['username'] ,vrp_31.vm_node_ip,vrp_31.local_ip)
        op = os.popen(cmd).read()
        vrp_31_ospf = int(re.match(r'\d',op).group())
        EXP_SESS=((NB_VSFO_CP_NODES + NB_VSFO_UP_NODES + 1))
        if EXP_SESS == vrp_31_ospf:
            self.logger.info("All ospf sessions are UP")
        else:
            self.logger.error("All ospf sessions are not UP")
            ret = False

        # Validate BGP & BFD sessions on vsfo CP nodes

        for i in range(1,NB_VSFO_CP_NODES+1):

            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J \"%s@%s\"  -o GlobalKnownHostsFile=/dev/null root@%s  \"cli\" \"show bgp summary\" | grep -c Establ" %(self.inputs.host_data[vsfo_fix[i].vm_node_ip]['username'] ,vsfo_fix[i].vm_node_ip,vsfo_fix[i].local_ip)
            op = os.popen(cmd).read()
            vsfo_cp_session = int(re.match(r'\d+',op).group())

            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J \"%s@%s\"  -o GlobalKnownHostsFile=/dev/null root@%s  \"cli\" \"show bfd session\" | grep ge-0/0 | grep -c Up" %(self.inputs.host_data[vsfo_fix[i].vm_node_ip]['username'] ,vsfo_fix[i].vm_node_ip,vsfo_fix[i].local_ip)
            op = os.popen(cmd).read()
            vsfo_cp_bfd_session = int(re.match(r'\d+',op).group())

            EXP_SESS=((2 * (NB_VSFO_CP_SIGIF + NB_APN_RADIUS + 1) * NB_VSFO_CP_EXT_NIC ))

            if EXP_SESS == vsfo_cp_session:
                self.logger.info("All bgp sessions are UP")
            else:
                self.logger.error("All bgp sessions are not UP")
                ret = False

            if EXP_SESS/2 == vsfo_cp_bfd_session:
                self.logger.info("All bfd sessions are UP")
            else:
                self.logger.error("All bfd sessions are not UP")
                ret = False
            i = i + 1

        # Validate BGP & BFD sessions on vsfo CP nodes

        for i in range(NB_VSFO_CP_NODES+1 ,NB_VSFO_CP_NODES + NB_VSFO_UP_NODES+1):

            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J \"%s@%s\"  -o GlobalKnownHostsFile=/dev/null root@%s  \"cli\" \"show bgp summary\" | grep -c Establ" %(self.inputs.host_data[vsfo_fix[i].vm_node_ip]['username'] ,vsfo_fix[i].vm_node_ip,vsfo_fix[i].local_ip)
            op = os.popen(cmd).read()
            vsfo_up_session = int(re.match(r'\d+',op).group())

            cmd = "sshpass -p contrail123 ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -J \"%s@%s\"  -o GlobalKnownHostsFile=/dev/null root@%s  \"cli\" \"show bfd session\" | grep ge-0/0 | grep -c Up" %(self.inputs.host_data[vsfo_fix[i].vm_node_ip]['username'] ,vsfo_fix[i].vm_node_ip,vsfo_fix[i].local_ip)
            op = os.popen(cmd).read()
            vsfo_up_bfd_session = int(re.match(r'\d+',op).group())
            
            EXP_SESS=(( 2*((NB_VSFO_UP_CNNIC * NB_VSFO_UP_CNIF) + (NB_VSFO_UP_EXT_NIC - NB_VSFO_UP_CNNIC) * NB_APN) ))

            if EXP_SESS == vsfo_up_session:
                self.logger.info("All bgp sessions are UP")
            else:
                self.logger.error("All bgp sessions are not UP")
                ret = False

            if EXP_SESS/2 == vsfo_up_bfd_session:
                self.logger.info("All bfd sessions are UP")
            else:
                self.logger.error("All bfd sessions are not UP")
                ret = False
            i = i+1

        return ret


#end class OrangeSolutionTest
