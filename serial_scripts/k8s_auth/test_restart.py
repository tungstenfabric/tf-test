from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth.wrappers import preposttest_wrapper
from testtools import TestCase

class TestRestart(TestCase):
    @preposttest_wrapper
    def test_all_operations_for_admin_project_domain_with_kube_manager_restart(self):
        stackrc_dict = ResourceUtil.admin_stackrc()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                    'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

    @preposttest_wrapper
    def test_all_operations_for_admin_project_domain_with_agent_restart(self):
        stackrc_dict = ResourceUtil.admin_stackrc()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

    @preposttest_wrapper
    def test_all_operations_for_custom_user_project_domain_with_kube_manager_restart(self):
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

    @preposttest_wrapper
    def test_all_operations_for_custom_user_project_domain_with_agent_restart(self):
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

    @preposttest_wrapper
    def test_pod_with_all_operations_for_custom_user_project_domain_with_kube_manager_restart(self):
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                        'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)

    @preposttest_wrapper
    def test_pod_with_all_operations_for_custom_user_project_domain_with_agent_restart(self):
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                        'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
