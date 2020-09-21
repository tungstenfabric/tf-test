from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
import os


def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['Pod']
    create_policy.create_and_apply_policies(resource=resource)


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='john', password='c0ntrail123', role='Member',
                     project_name='new_project', domain_name='new_domain')
    Util.source_stackrc(user_name='john', password='c0ntrail123',
                        project_name='new_project', domain_name='new_domain', auth_url=admin.auth_url)
    resource = {}
    resource['resources'] = ['pod']
    role_dict = {
        'type': 'role',
        'values': ['*']
    }
    project_dict = {
        'type': 'project',
        'values': ['new_project']
    }
    match = [role_dict, project_dict]
    create_policy.create_and_apply_policies(resource=resource, match=match)

    # Test required operation
    # Need to be able to create, delete, get Pod
    Util.create_resource('pod')

    # Shouldn't be able to create Deployment, Service, Ingress, NAD, Namespace, DaemonSet and NetworkPolicy


# pod_with_all_operations_for_admin_project_domain()
# pod_with_all_operations_for_custom_user_project_domain()
def test():
    resource = {}
    resource['resources'] = ['pod']
    role_dict = {
        'type': 'role',
        'values': ['*']
    }
    project_dict = {
        'type': 'project',
        'values': ['new_project']
    }
    policies = create_policy.create_policies(resource, match)
    policy_dict = construct_config_map_dict(policies)
    filename = create_config_map_file(policy_dict)


# pod_with_all_operations_for_custom_user_project_domain()
test()
