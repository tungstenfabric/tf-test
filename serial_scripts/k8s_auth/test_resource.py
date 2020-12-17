from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth.wrappers import preposttest_wrapper
from testtools import TestCase

# If nothing is mentioned in the resource verbs, then all operations are
# permitted for that particular resource


class TestResource(TestCase):
    resource_expectation_list = [
        'pod-expected',
        'deployment-expected',
        'service-expected',
        'namespace-expected',
        'network_attachment_definition-expected',
        'network_policy-expected',
        'ingress-expected',
        'daemonset-expected']

    @preposttest_wrapper
    def test_all_operations_for_admin_project_domain(self):
        '''
        Description: Test to validate admin user can perform all operations
         Test steps:
                1. Create stackrc_dict for admin user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
         Pass criteria: admin user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        stackrc_dict = ResourceUtil.admin_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=TestResource.resource_expectation_list,
            stackrc_dict=stackrc_dict)

    @preposttest_wrapper
    def test_all_operations_for_custom_user_project_domain(self):
        '''
        Description: Test to validate custom user can perform all operations
         Test steps:
                1. Create stackrc_dict and get Openstack match object for custom user
                2. Set the resource expectation list to all k8s resources
                3. Perform create and delete operations
         Pass criteria: custom user must be able to perform all operations successfully
         Maintainer : nuthanc@juniper.net
        '''
        match, stackrc_dict = ResourceUtil.get_custom_match_stackrc()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation_list=TestResource.resource_expectation_list,
            stackrc_dict=stackrc_dict)


class TestResourceCustom(TestCase):
    def setUp(self):
        super(TestResourceCustom, self).setUp()
        self.match, self.stackrc_dict = ResourceUtil.get_custom_match_stackrc(
            rand=True)

    def tearDown(self):
        super(TestResourceCustom, self).tearDown()
        user = ExampleUser.admin()
        user.delete_user(
            user_name=self.stackrc_dict['user_name'],
            project_name=self.stackrc_dict['project_name'],
            domain_name=self.stackrc_dict['domain_name'])

    @preposttest_wrapper
    def test_pod_with_all_operations_for_custom_user_project_domain(self):
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
        resource_expectation_list = [
            'pod-expected',
            'deployment',
            'service',
            'namespace',
            'network_attachment_definition',
            'network_policy',
            'ingress',
            'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation_list=resource_expectation_list)

    @preposttest_wrapper
    def test_deployment_with_all_operations_for_custom_user_project_domain(
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
        resource_expectation_list = [
            'pod',
            'deployment-expected',
            'service',
            'namespace',
            'network_attachment_definition',
            'network_policy',
            'ingress',
            'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=self.match,
            stackrc_dict=self.stackrc_dict,
            resource_expectation_list=resource_expectation_list)
