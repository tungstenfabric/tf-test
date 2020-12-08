from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth.util import Util
import os
import unittest

# Tested and working

# If nothing is mentioned in the resource verbs, then all operations are permitted for that particular resource


class TestResource(unittest.TestCase):
    def test_all_operations_for_admin_project_domain(self):
        print(self.id())
        stackrc_dict = ResourceUtil.admin_stackrc()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                    'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)



    def test_all_operations_for_custom_user_project_domain(self):
        print(self.id())
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                    'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
        ResourceUtil.create_policy_and_perform_operations(
            match=match, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)



    def test_pod_with_all_operations_for_custom_user_project_domain(self):
        print(self.id())
        resource = {'resources': ['pods']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict(rand=True)
        resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)



    def test_deployment_with_all_operations_for_custom_user_project_domain(self):
        print(self.id())
        resource = {'resources': ['deployments']}
        match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict(rand=True)
        resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.create_policy_and_perform_operations(
            resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


if __name__ == '__main__':
    unittest.main()

