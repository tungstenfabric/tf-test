from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.source_stackrc import source_stackrc
import os

def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['Pod']
    create_policy.create_and_apply_policies(resource=resource)


def pod_with_all_operations_for_custom_user_project_domain():
    resource = {}
    resource['resources'] = ['Pod']
    admin = ExampleUser.admin()
    admin.create_all(user_name='john', password='c0ntrail123', role='Member',
                     project_name='new_project', domain_name='new_domain')
    source_stackrc(user_name='john', password='c0ntrail123',
                   project_name='new_project', domain_name='new_domain', auth_url='http://auth:5000/v3')


# pod_with_all_operations_for_admin_project_domain()
pod_with_all_operations_for_custom_user_project_domain()
