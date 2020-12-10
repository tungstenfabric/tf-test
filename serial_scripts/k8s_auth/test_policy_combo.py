from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
from tcutils.kubernetes.auth import create_policy
import unittest
import os

class TestPolicyCombo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create the required users, projects and domains
        admin = ExampleUser.admin()
        admin.create_all(user_name='zoro', password='c0ntrail123', role='Member',
                        project_name='zoro_project', domain_name='zoro_domain')
        admin.create_all(user_name='ola', password='c0ntrail123', role='Member',
                        project_name='ola_project', domain_name='ola_domain')
        admin.create_all(user_name='uber', password='c0ntrail123', role='Member',
                        project_name='uber_project', domain_name='uber_domain')
        admin.create_all(user_name='zomato', password='c0ntrail123', role='Member',
                        project_name='zomato_project', domain_name='zomato_domain')
        ResourceUtil.source_stackrc(**ResourceUtil.admin_stackrc())
        os.system('kubectl create ns zomsrc')
        os.system('kubectl create ns easy')
        # MSG Add code in create_policy for the below
        policies = [admin_policy, ola_policy, uber_policy, zomato_policy, zoro_policy]
        filename = create_policy.insert_policies_in_template_file(policies, 'all_in_one_policy.yaml')
        create_policy.apply_policies_and_check_in_config_map(policies, filename)


    def test_only_pods_and_deployments_create(self):
        '''
        For ola user, only create pods and deployments and nothing else
        '''
        print("For ola user, only create pods and deployments and nothing else")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'ola',
            'password': 'c0ntrail123',
            'project_name': 'ola_project',
            'domain_name': 'ola_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


    def test_only_pods_and_deployments_delete(self):
        '''
        For uber user, only delete pods and deployments and nothing else
        '''
        print("\nFor uber user, only delete pods and deployments and nothing else")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'uber',
            'password': 'c0ntrail123',
            'project_name': 'uber_project',
            'domain_name': 'uber_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)

    def test_only_service_in_zomsrc_ns(self):
        '''
        For zomato user, create service in zomsrc namespace and nothing else should work
        '''
        print("\nFor zomato user, create service in zomsrc namespace and nothing else should work")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'zomato',
            'password': 'c0ntrail123',
            'project_name': 'zomato_project',
            'domain_name': 'zomato_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod', 'deployment', 'service-expected', 'namespace',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list, namespace='zomsrc')


    def test_only_pods_deployments_services_in_easy_ns(self):
        '''
        For zoro user, any operation on pods, deployments and services but only in easy namespace
        '''
        print("\nFor zoro user, any operation on pods, deployments and services but only in easy namespace")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'zoro',
            'password': 'c0ntrail123',
            'project_name': 'zoro_project',
            'domain_name': 'zoro_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                    'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list, namespace='easy')


if __name__ == '__main__':
    unittest.main()