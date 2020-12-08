from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
import os
import unittest

class TestRestart(unittest.TestCase):
    def test_all_operations_for_admin_project_domain_with_kube_manager_restart(self):
        stackrc_dict = ResourceUtil.admin_stackrc()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                    'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


    def test_all_operations_for_admin_project_domain_with_agent_restart(self):
        stackrc_dict = ResourceUtil.admin_stackrc()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


    def test_all_operations_for_custom_user_project_domain_with_kube_manager_restart(self):
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


    def test_all_operations_for_custom_user_project_domain_with_agent_restart(self):
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                        'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


    def test_pod_with_all_operations_for_custom_user_project_domain_with_kube_manager_restart(self):
        # import pdb;pdb.set_trace()
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                        'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_kube_manager()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


    def test_pod_with_all_operations_for_custom_user_project_domain_with_agent_restart(self):
        # import pdb;pdb.set_trace()
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                        'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
        ResourceUtil.restart_vrouter_agent()
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


if __name__ == '__main__':
    unittest.main()