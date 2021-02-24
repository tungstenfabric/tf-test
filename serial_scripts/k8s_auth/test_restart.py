from serial_scripts.k8s_auth.base import BaseK8sAuth
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.wrappers import preposttest_wrapper
import test
from k8s.deployment import DeploymentFixture
from k8s.pod import PodFixture


class TestRestart(BaseK8sAuth):
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
        super(TestRestart, cls).setUpClass()

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_admin_project_with_kube_manager_restart(
            self):
        '''
        Description: Test to validate normal operations after kube manager restart
         Test steps:
                1. Create stackrc_dict for admin user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
                4. Restart kube manager
                5. Perform create and delete operations again
         Pass criteria: Even after kube manager restart, admin user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = ResourceUtil.admin_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)
        self.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_admin_project_with_agent_restart(self):
        '''
        Description: Test to validate normal operations after vrouter agent restart
         Test steps:
                1. Create stackrc_dict for admin user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
                4. Restart vrouter agent
                5. Perform create and delete operations again
         Pass criteria: Even after vrouter agent restart, admin user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = ResourceUtil.admin_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)
        self.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_custom_project_with_kube_manager_restart(
            self):
        '''
        Description: Test to validate normal operations after kube manager restart for custom user
         Test steps:
                1. Create stackrc_dict for custom user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
                4. Restart kube manager
                5. Perform create and delete operations again
         Pass criteria: Even after kube manager restart, custom user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        match, stackrc_dict = ResourceUtil.get_custom_match_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)
        self.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_custom_project_with_agent_restart(
            self):
        '''
        Description: Test to validate normal operations after vrouter agent restart for custom user
         Test steps:
                1. Create stackrc_dict for custom user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
                4. Restart vrouter agent
                5. Perform create and delete operations again
         Pass criteria: Even after vrouter agent restart, custom user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        match, stackrc_dict = ResourceUtil.get_custom_match_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)
        self.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_k8s_auth_pod_delete(self):
        '''
        Description: Test to validate normal operations after k8s auth pod deletion
         Test steps:
                1. Create stackrc_dict for admin user
                2. Set the resource expectation list to all k8s resources
                3. Delete the k8s keystone auth pods one after the other
                4. Perform create and delete operations with keystone context
         Pass criteria: Even after the k8s auth pods are deleted, they should come up fine and admin user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        dep = DeploymentFixture(
            self.connections, name='k8s-keystone-auth', namespace='kube-system')
        dep_obj = dep.read()
        pods = dep.get_pods_list()
        for pod in pods:
            auth_pod = PodFixture(
                self.connections, name=pod.metadata.name, namespace=pod.metadata.namespace)
            auth_pod.delete_only()
            auth_pod.verify_pod_is_not_in_k8s()
        stackrc_dict = ResourceUtil.admin_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation=TestRestart.resource_expectation,
            stackrc_dict=stackrc_dict, inputs=self.inputs)


class TestRestartWithPodResource(BaseK8sAuth):
    resource = {'resources': ['pods']}
    resource_expectation = {'pod': True}

    @classmethod
    def setUpClass(cls):
        super(TestRestartWithPodResource, cls).setUpClass()

    def setUp(self):
        super(TestRestartWithPodResource, self).setUp()
        self.match, self.stackrc_dict = ResourceUtil.get_custom_match_stackrc(
            rand=True)

    def tearDown(self):
        super(TestRestartWithPodResource, self).tearDown()
        user = ExampleUser.admin()
        user.delete_user(
            user_name=self.stackrc_dict['user_name'],
            project_name=self.stackrc_dict['project_name'],
            domain_name=self.stackrc_dict['domain_name'])

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_pod_with_kube_manager_restart(self):
        '''
        Description: Test to validate only pod operations after kube_manager restart for custom user
         Test steps:
                1. Create stackrc_dict for custom user
                2. Set the resource expectation list to only pods
                3. Perform create and delete operations on all resources
                4. Restart kube_manager
                5. Perform create and delete operations on all resources again
         Pass criteria: Even after kube_manager restart, custom user must be able to perform all operations only on pod resource successfully
         Maintainer : nuthanc@juniper.net
        '''
        ResourceUtil.create_policy_and_perform_operations(
            resource=TestRestartWithPodResource.resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=TestRestartWithPodResource.resource_expectation,
            inputs=self.inputs)
        self.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource=TestRestartWithPodResource.resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=TestRestartWithPodResource.resource_expectation,
            inputs=self.inputs)

    @test.attr(type=['auth'])
    @preposttest_wrapper
    def test_pod_with_agent_restart(self):
        '''
        Description: Test to validate only pod operations after vrouter agent restart for custom user
         Test steps:
                1. Create stackrc_dict for custom user
                2. Set the resource expectation list to only pods
                3. Perform create and delete operations on all resources
                4. Restart vrouter agent
                5. Perform create and delete operations on all resources again
         Pass criteria: Even after vrouter agent restart, custom user must be able to perform all operations only on pod resource successfully
         Maintainer : nuthanc@juniper.net
        '''
        ResourceUtil.create_policy_and_perform_operations(
            resource=TestRestartWithPodResource.resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=TestRestartWithPodResource.resource_expectation,
            inputs=self.inputs)
        self.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource=TestRestartWithPodResource.resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation=TestRestartWithPodResource.resource_expectation,
            inputs=self.inputs)
