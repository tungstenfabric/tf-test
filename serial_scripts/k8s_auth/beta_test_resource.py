from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.resource_util import ResourceUtil
import os


# If nothing is mentioned in the resource verbs, then all operations are permitted for that particular resource
# If no match is provided, then it is admin_policy with everything enabled in resource

# Untested
# MSG Next to test
def resource_with_all_operations_for_custom_user_project_domain(res, match, stackrc_dict):
    resource = {'resources': [res]}
    resource_expectation_list = ['pod', 'deployment', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    # MSG Need to add condition properly here as r and res are different
    for i,r in enumerate(resource_expectation_list):
        if r in res:
            resource_expectation_list[i] = r + ':expected'
    ResourceUtil.create_policy_and_perform_operations(
        resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


def test_individual_resource_with_all_operations_for_custom_user_project_domain():
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
    resource_list = ['pods', 'deployments', 'services', 'namespaces',
                     'network-attachment-definitions', 'networkpolicies', 'ingresses', 'daemonsets']
    for resource in resource_list:
        resource_with_all_operations_for_custom_user_project_domain(resource, match, stackrc_dict)

test_individual_resource_with_all_operations_for_custom_user_project_domain()


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
    resource_expectation_list = ['pod:expected', 'deployment:expected', 'service:expected', 'namespace:expected',
                                 'network_attachment_definition:expected', 'network_policy:expected', 'ingress:expected', 'daemonset:expected']
    ResourceUtil.create_policy_and_perform_operations(resource=resource,
                                                      resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)


# Untested
def deployment_with_all_operations_for_custom_user_project_domain():
    resource = {'resources': 'deployments'}
    resource_expectation_list = ['pod', 'deployment:expected', 'service', 'namespace',
                                 'network_attachment_definit= ion', 'network_policy', 'ingress', 'daemonset']
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
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
    resource_expectation_list = ['pod', 'deployment:expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.create_policy_and_perform_operations(
        resource=resource, resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)

# MSG Add methods for other verbs, resources and namespaces
