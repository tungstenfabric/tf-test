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
        admin.create_all(user_name='userD', password='c0ntrail123', role='Member',
                         project_name='userD_project', domain_name='userD_domain')
        admin.create_all(user_name='userA', password='c0ntrail123', role='Member',
                         project_name='userA_project', domain_name='userA_domain')
        admin.create_all(user_name='userB', password='c0ntrail123', role='Member',
                         project_name='userB_project', domain_name='userB_domain')
        admin.create_all(user_name='userC', password='c0ntrail123', role='Member',
                         project_name='userC_project', domain_name='userC_domain')
        ResourceUtil.source_stackrc(**ResourceUtil.admin_stackrc())
        os.system('kubectl create ns zomsrc')
        os.system('kubectl create ns easy')
        admin_policy = create_policy.get_admin_policy()
        userA_policy = create_policy.get_userA_policy()
        userB_policy = create_policy.get_userB_policy()
        userC_policy = create_policy.get_userC_policy()
        userD_policy = create_policy.get_userD_policy()
        policies = [admin_policy, userA_policy,
                    userB_policy, userC_policy, userD_policy]
        filename = create_policy.insert_policies_in_template_file(
            policies, 'all_in_one_policy.yaml')
        create_policy.apply_policies_and_check_in_config_map(
            policies, filename)

    def test_only_pods_and_deployments_create(self):
        '''
        For userA user, only create pods and deployments and nothing else
        '''
        print("\n"+self.id())
        print("For userA user, only create pods and deployments and nothing else")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'userA',
            'password': 'c0ntrail123',
            'project_name': 'userA_project',
            'domain_name': 'userA_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                     'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)

    def test_only_pods_and_deployments_delete(self):
        '''
        For userB user, only delete pods and deployments and nothing else
        '''
        print("\n"+self.id())
        print("\nFor userB user, only delete pods and deployments and nothing else")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'userB',
            'password': 'c0ntrail123',
            'project_name': 'userB_project',
            'domain_name': 'userB_domain',
            'auth_url': admin.auth_url
        }
        resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                     'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
        ResourceUtil.perform_operations(
            stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)

    def test_only_service_in_zomsrc_ns(self):
        '''
        For userC user, create service in zomsrc namespace and nothing else should work
        '''
        print("\n"+self.id())
        print("\nFor userC user, create service in zomsrc namespace and nothing else should work")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'userC',
            'password': 'c0ntrail123',
            'project_name': 'userC_project',
            'domain_name': 'userC_domain',
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
        For userD user, any operation on pods, deployments and services but only in easy namespace
        '''
        print("\n"+self.id())
        print("\nFor userD user, any operation on pods, deployments and services but only in easy namespace")
        admin = ExampleUser.admin()
        stackrc_dict = {
            'user_name': 'userD',
            'password': 'c0ntrail123',
            'project_name': 'userD_project',
            'domain_name': 'userD_domain',
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
