from serial_scripts.k8s_auth.base import BaseK8sAuth
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from common.contrail_test_init import ContrailTestInit
from tcutils.kubernetes.auth import create_policy
from tcutils.wrappers import preposttest_wrapper
import test


class TestPolicyCombo(BaseK8sAuth):

    @classmethod
    def setUpClass(cls):
        # Create the required users, projects and domains
        cmd = 'kubectl config use-context juju-context'
        cti_obj = ContrailTestInit(input_file='contrail_test_input.yaml')
        cti_obj.run_cmd_on_server(
            server_ip=cti_obj.juju_server,
            username='root',
            password='c0ntrail123',
            issue_cmd=cmd)
        super(TestPolicyCombo, cls).setUpClass()
        cls.admin = ExampleUser.admin()
        cls.admin.create_all(
            user_name='userD',
            password='c0ntrail123',
            role='Member',
            project_name='userD_project',
            domain_name='userD_domain')
        cls.admin.create_all(
            user_name='userA',
            password='c0ntrail123',
            role='Member',
            project_name='userA_project',
            domain_name='userA_domain')
        cls.admin.create_all(
            user_name='userB',
            password='c0ntrail123',
            role='Member',
            project_name='userB_project',
            domain_name='userB_domain')
        cls.admin.create_all(
            user_name='userC',
            password='c0ntrail123',
            role='Member',
            project_name='userC_project',
            domain_name='userC_domain')

        cmd = 'kubectl create ns zomsrc; kubectl create ns easy'
        cls.inputs.run_cmd_on_server(
            server_ip=cti_obj.juju_server,
            username='root',
            password='c0ntrail123',
            issue_cmd=cmd)
        admin_policy = create_policy.get_admin_policy()
        userA_policy = create_policy.get_userA_policy()
        userB_policy = create_policy.get_userB_policy()
        userC_policy = create_policy.get_userC_policy()
        userD_policy = create_policy.get_userD_policy()
        policies = [admin_policy, userA_policy,
                    userB_policy, userC_policy, userD_policy]
        filename = create_policy.insert_policies_in_template_file(
            policies, filename='all_in_one_policy.yaml', inputs=cls.inputs)
        create_policy.apply_policies_and_check_in_config_map(
            policies, filename, cti_obj.juju_server)

    @classmethod
    def tearDownClass(cls):
        super(TestPolicyCombo, cls).tearDownClass()
        cls.admin.delete_all(
            user_name='userD',
            project_name='userD_project',
            domain_name='userD_domain')
        cls.admin.delete_all(
            user_name='userA',
            project_name='userA_project',
            domain_name='userA_domain')
        cls.admin.delete_all(
            user_name='userB',
            project_name='userB_project',
            domain_name='userB_domain')
        cls.admin.delete_all(
            user_name='userC',
            project_name='userC_project',
            domain_name='userC_domain')

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_only_pods_and_deployments_create(self):
        '''
        Description: Test to validate only userA can create pods and deployments
         Test steps:
                1. Create stackrc_dict for userA
                2. Create the resource expectation list
                3. Perform create and delete operations
         Pass criteria: userA must only be able to create pods and deployments and nothing else
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = {
            'user_name': 'userA',
            'password': 'c0ntrail123',
            'project_name': 'userA_project',
            'domain_name': 'userA_domain',
            'auth_url': self.__class__.admin.auth_url
        }
        resource_expectation = {'pod': True, 'deployment': True}
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict,
            resource_expectation=resource_expectation, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_only_pods_and_deployments_delete(self):
        '''
        Description: Test to validate only userB can delete pods and deployments
         Test steps:
                1. Create stackrc_dict for userB
                2. Create the resource expectation list
                3. Perform create and delete operations
         Pass criteria: userB must only be able to delete pods and deployments and nothing else
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = {
            'user_name': 'userB',
            'password': 'c0ntrail123',
            'project_name': 'userB_project',
            'domain_name': 'userB_domain',
            'auth_url': self.__class__.admin.auth_url
        }
        resource_expectation = {'pod': True, 'deployment': True}
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict,
            resource_expectation=resource_expectation, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_only_service_in_zomsrc_ns(self):
        '''
        Description: Test to validate only userC can create and delete service in zomsrc namespace
         Test steps:
                1. Create stackrc_dict for userC
                2. Create the resource expectation list
                3. Perform create and delete operations in default namespace and zomsrc namespace
         Pass criteria: userC must only be able to create and delete service in zomsrc namespace and nothing else
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = {
            'user_name': 'userC',
            'password': 'c0ntrail123',
            'project_name': 'userC_project',
            'domain_name': 'userC_domain',
            'auth_url': self.__class__.admin.auth_url
        }
        resource_expectation = {'service': True}
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict,
            resource_expectation=resource_expectation, inputs=self.inputs)
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict,
            resource_expectation=resource_expectation,
            namespace='zomsrc', inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_only_pods_deployments_services_in_easy_ns(self):
        '''
        For userD user, any operation on pods, deployments and services but only in easy namespace
        Description: Test to validate only userD can perform any operation on pods, deployments and services but only in easy namespace
         Test steps:
                1. Create stackrc_dict for userD
                2. Create the resource expectation list
                3. Perform create and delete operations in default namespace and easy_ns namespace
         Pass criteria: userD must only be able to perform any operation on pods, deployments and services in easy namespace and nothing else
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = {
            'user_name': 'userD',
            'password': 'c0ntrail123',
            'project_name': 'userD_project',
            'domain_name': 'userD_domain',
            'auth_url': self.__class__.admin.auth_url
        }
        resource_expectation = {
            'pod': True,
            'deployment': True,
            'service': True,
            'namespace': True}
        ResourceUtil.perform_operations(
            resource_expectation=resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict,
            resource_expectation=resource_expectation,
            namespace='easy', inputs=self.inputs)
