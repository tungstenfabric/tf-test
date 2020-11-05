from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
import os


# If nothing is mentioned in the resource verbs, then all operations are permitted for that particular resource


# Untested
def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='test', password='c0ntrail123', role='Member',
                     project_name='test_project', domain_name='test_domain')
    resource = {}
    resource['resources'] = ['pods']
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_object_and_match_list()
    resource_expectation_list = ['pod-expected', 'deployment', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.create_policy_and_perform_operations(resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


# Untested
def all_operations_for_admin_project_domain():
    # admin = ExampleUser.admin()
    # stackrc_dict = {
    #     'user_name': 'admin',
    #     'password': 'password',
    #     'project_name': 'admin',
    #     'domain_name': 'admin_domain',
    #     'auth_url': admin.auth_url
    # }
    resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                 'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
    ResourceUtil.create_policy_and_perform_operations(
        resource_expectation_list=resource_expectation_list)


pod_with_all_operations_for_custom_user_project_domain()

# Untested
def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['pods']
    admin = ExampleUser.admin()
    stackrc_dict = {
        'user_name': 'admin',
        'password': 'password',
        'project_name': 'admin',
        'domain_name': 'admin_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                 'network_attachment_definition-expected', 'network_policy-expected', 'ingress-expected', 'daemonset-expected']
    ResourceUtil.create_policy_and_perform_operations(resource=resource,
                                        resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


# Untested
# MSG DRY up code for custom_user_project
def deployment_with_all_operations_for_custom_user_project_domain():
    resource = {'resources': 'deployments'}
    resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definit= ion', 'network_policy', 'ingress', 'daemonset']
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_object_and_match_list()
    ResourceUtil.create_policy_and_perform_operations(resource=resource, match=match,
                                        resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


# Untested
def deployment_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['deployments']
    admin = ExampleUser.admin()
    stackrc_dict = {
        'user_name': 'admin',
        'password': 'password',
        'project_name': 'admin',
        'domain_name': 'admin_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.create_policy_and_perform_operations(
        resource=resource, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

# MSG Add the above 2 methods for other resources


# pod_with_all_operations_for_custom_user_project_domain()
# pod_with_all_operations_for_admin_project_domain()
