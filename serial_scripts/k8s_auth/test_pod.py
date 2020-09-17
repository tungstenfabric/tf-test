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
                   project_name='new_project', domain_name='new_domain', auth_url='http://auth:5000/v3')
    resource = {}
    resource['resources'] = ['pod']
    create_policy.create_and_apply_policies(resource=resource)

    #Test required operation
    #Need to be able to create, delete, get Pod
    Util.create_resource('pod')

    
    #Shouldn't be able to create Deployment, Service, Ingress, NAD, Namespace, DaemonSet and NetworkPolicy



# pod_with_all_operations_for_admin_project_domain()
# pod_with_all_operations_for_custom_user_project_domain()
def test():
    Util.source_stackrc(user_name='john', password='c0ntrail123',
                   project_name='new_project', domain_name='new_domain', auth_url='http://auth:5000/v3')
    Util.create_resource('pod')

test()