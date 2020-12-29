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
from common.policy import policy_test_helper
from tcutils.test_lib.test_utils import assertEqual
from vnc_api import vnc_api
from vnc_api.gen.resource_test import *
from heat_test import HeatStackFixture
from nova_test import *
import os
import yaml

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

    #end setup_vepg

    @classmethod
    def delete_vepg(cls):
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

#end class OrangeSolutionTest
