from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
import os


def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['pods']
    create_policy.create_and_apply_policies(resource=resource)


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='john', password='c0ntrail123', role='Member',
                     project_name='new_project', domain_name='new_domain')
    resource = {}
    resource['resources'] = ['deployments']
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
    # Need to be able to create, delete, get Pod
    Util.source_stackrc(user_name='john', password='c0ntrail123',
                        project_name='new_project', domain_name='new_domain', auth_url=admin.auth_url)
    Util.resource(verb='create', resource_list=['pod', 'deployment', 'service', 'namespace',
                                                'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=[
                  'pod', 'deployment', 'service', 'namespace', 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    # Shouldn't be able to create Deployment, Service, Ingress, NAD, Namespace, DaemonSet and NetworkPolicy


# pod_with_all_operations_for_admin_project_domain()
# pod_with_all_operations_for_custom_user_project_domain()
def test():
    resource = {}
    resource['resources'] = ['*']
    role_dict = {
        'type': 'role',
        'values': ['*']
    }
    project_dict = {
        'type': 'project',
        'values': ['admin']
    }
    match = [role_dict, project_dict]
    policies = create_policy.create_policies(resource, match)
    policy_dict = create_policy.construct_config_map_dict(policies)
    create_policy.create_config_map_file(policy_dict)


pod_with_all_operations_for_custom_user_project_domain()
# test()

