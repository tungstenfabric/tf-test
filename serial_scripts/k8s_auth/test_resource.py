from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
import os

# Tested and working
def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='john', password='c0ntrail123', role='Member',
                     project_name='new_project', domain_name='new_domain')
    resource = {}
    resource['resources'] = ['pods']
    role_dict = {
        'type': 'role',
        'values': ['Member']
    }
    project_dict = {
        'type': 'project',
        'values': ['new_project']
    }
    user_dict = {
        "type": 'user',
        "values": ['john']
    }
    match = [role_dict, project_dict, user_dict]
    create_policy.create_and_apply_policies(resource=resource, match=match)

    # Test required operation
    Util.source_stackrc(user_name='john', password='c0ntrail123',
                        project_name='new_project', domain_name='new_domain', auth_url=admin.auth_url)
    Util.resource(verb='create', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    #MSG USE resource_with_expectation method after it is found to be working


# Untested
def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['pods']
    create_policy.create_and_apply_policies(resource=resource)
    Util.source_stackrc()
    Util.resource(verb='create', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource_with_expectation(verb='create', resource_expectation_list=['pod-expected', 'deployment', 'service', 'namespace',
                                                                     'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource_with_expectation(verb='delete', resource_expectation_list=['pod-expected', 'deployment', 'service', 'namespace',
                                                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])

pod_with_all_operations_for_custom_user_project_domain()
# pod_with_all_operations_for_admin_project_domain()
