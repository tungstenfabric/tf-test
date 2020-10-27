from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
import os

# Tested and working


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='test', password='c0ntrail123', role='Member',
                     project_name='test_project', domain_name='test_domain')
    resource = {}
    resource['resources'] = ['pods']
    role_dict = {
        'type': 'role',
        'values': ['Member']
    }
    project_dict = {
        'type': 'project',
        'values': ['test_project']
    }
    user_dict = {
        "type": 'user',
        "values": ['test']
    }
    match = [role_dict, project_dict, user_dict]
    create_policy.create_and_apply_policies(resource=resource, match=match)

    # Test required operation
    Util.source_stackrc(user_name='test', password='c0ntrail123',
                        project_name='test_project', domain_name='test_domain', auth_url=admin.auth_url)
    Util.resource(verb='create', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    # MSG USE resource_with_expectation method after it is found to be working


# Untested
def resource_with_operations(resource={}, match=[], resource_expectation_list=[], stackrc_dict={}):
    create_policy.create_and_apply_policies(resource=resource, match=match)
    Util.source_stackrc(**stackrc_dict)
    Util.resource_with_expectation(
        verb='create', resource_expectation_list=resource_expectation_list)
    Util.resource_with_expectation(
        verb='delete', resource_expectation_list=resource_expectation_list)


# Untested
def all_operations_for_admin_project_domain():
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
    resource_with_operations(
        resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


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
    resource_with_operations(resource=resource,
                             resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


# Untested
# MSG DRY up code for custom_user_project
def deployment_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='test', password='c0ntrail123', role='Member',
                     project_name='test_project', domain_name='test_domain')
    resource = {}
    resource['resources'] = ['deployments']
    role_dict = {
        'type': 'role',
        'values': ['Member']
    }
    project_dict = {
        'type': 'project',
        'values': ['test_project']
    }
    user_dict = {
        "type": 'user',
        "values": ['test']
    }
    match = [role_dict, project_dict, user_dict]

    # Test required operation
    stackrc_dict = {
        'user_name': 'test',
        'password': 'c0ntrail123',
        'project_name': 'test_project',
        'domain_name': 'test_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    resource_with_operations(resource=resource, match=match,
                             resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


# Untested
def deployment_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['deployments']
    resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    resource_with_operations(
        resource=resource, resource_expectation_list=resource_expectation_list)

# MSG Add the above 2 methods for other resources


pod_with_all_operations_for_custom_user_project_domain()
# pod_with_all_operations_for_admin_project_domain()
