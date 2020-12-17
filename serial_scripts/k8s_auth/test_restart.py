from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth.wrappers import preposttest_wrapper
from testtools import TestCase


class TestRestart(TestCase):
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
        resource_expectation_list = [
            'pod-expected',
            'deployment-expected',
            'service-expected',
            'namespace-expected',
            'network_attachment_definition-expected',
            'network_policy-expected',
            'ingress-expected',
            'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)

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
        resource_expectation_list = [
            'pod-expected',
            'deployment-expected',
            'service-expected',
            'namespace-expected',
            'network_attachment_definition-expected',
            'network_policy-expected',
            'ingress-expected',
            'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)

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
        resource_expectation_list = [
            'pod-expected',
            'deployment-expected',
            'service-expected',
            'namespace-expected',
            'network_attachment_definition-expected',
            'network_policy-expected',
            'ingress-expected',
            'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)

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
        resource_expectation_list = [
            'pod-expected',
            'deployment-expected',
            'service-expected',
            'namespace-expected',
            'network_attachment_definition-expected',
            'network_policy-expected',
            'ingress-expected',
            'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            match=match,
            resource_expectation_list=resource_expectation_list,
            stackrc_dict=stackrc_dict)

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
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.get_custom_match_stackrc()
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
            match=match,
            stackrc_dict=stackrc_dict,
            resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=match,
            stackrc_dict=stackrc_dict,
            resource_expectation_list=resource_expectation_list)

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
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.get_custom_match_stackrc()
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
            match=match,
            stackrc_dict=stackrc_dict,
            resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource,
            match=match,
            stackrc_dict=stackrc_dict,
            resource_expectation_list=resource_expectation_list)
