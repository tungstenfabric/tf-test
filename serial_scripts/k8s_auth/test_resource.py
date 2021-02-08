from serial_scripts.k8s_auth.base import BaseK8sAuth
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.wrappers import preposttest_wrapper
import test


class TestK8sResource(BaseK8sAuth):

    resource_expectation = {
        'pod': True,
        'deployment': True,
        'service': True,
        'namespace': True,
        'network_attachment_definition': True,
        'network_policy': True,
        'ingress': True,
        'daemonset': True
    }

    @classmethod
    def setUpClass(cls):
        super(TestK8sResource, cls).setUpClass()

    def parallel_cleanup(self):
        cmds = ['kubectl config use-context juju-context']
        for resource in TestK8sResource.resource_expectation:
            template_file = ResourceUtil.templates[resource]
            cmd = 'kubectl delete -f %s -n default' % template_file
            cmds.append(cmd)
        ResourceUtil.execute_cmds_on_remote(
            ip=self.inputs.juju_server, cmd_list=cmds)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_all_in_admin_project(self):
        '''
        Description: Test to validate admin user can perform all operations
         Test steps:
                1. Create stackrc_dict for admin user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
         Pass criteria: admin user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        self.stackrc_dict = ResourceUtil.admin_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestK8sResource.resource_expectation,
            stackrc_dict=self.stackrc_dict, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_all_in_custom_project(self):
        '''
        Description: Test to validate custom user can perform all operations
         Test steps:
                1. Create stackrc_dict and get Openstack match object for custom user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
         Pass criteria: custom user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        match, self.stackrc_dict = ResourceUtil.get_custom_match_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation=TestK8sResource.resource_expectation,
            stackrc_dict=self.stackrc_dict, inputs=self.inputs)


class TestK8sResourceCustom(BaseK8sAuth):

    @classmethod
    def setUpClass(cls):
        super(TestK8sResourceCustom, cls).setUpClass()

    def setUp(self):
        super(TestK8sResourceCustom, self).setUp()
        self.match, self.stackrc_dict = ResourceUtil.get_custom_match_stackrc(
            rand=True)

    def tearDown(self):
        super(TestK8sResourceCustom, self).tearDown()
        user = ExampleUser.admin()
        user.delete_user(
            user_name=self.stackrc_dict['user_name'],
            project_name=self.stackrc_dict['project_name'],
            domain_name=self.stackrc_dict['domain_name'])

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_pod_in_custom_project(self):
        '''
        Description: Test to validate custom user can perform all operations only on pod resource
         Test steps:
                1. Set resource to only pods
                2. Set the resource expectation list to only pod
                3. Perform create and delete operations on all resources
         Pass criteria: custom user must be able to perform all operations only on pod resource successfully
         Maintainer : nuthanc@juniper.net
        '''
        resource = {'resources': ['pods']}
        resource_expectation = {'pod': True}

        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=resource_expectation, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_deployment_in_custom_project(
            self):
        '''
        Description: Test to validate custom user can perform all operations only on deployment resource
         Test steps:
                1. Set resource to only deployments
                2. Set the resource expectation list to only deployment
                3. Perform create and delete operations on all resources
         Pass criteria: custom user must be able to perform all operations only on deployment resource successfully
         Maintainer : nuthanc@juniper.net
        '''
        resource = {'resources': ['deployments']}
        resource_expectation = {'deployment': True}

        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=resource_expectation, inputs=self.inputs)
