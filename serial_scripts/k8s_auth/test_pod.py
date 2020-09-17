from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.source_stackrc import source_stackrc
from tcutils.kubernetes.auth import templates
import os
from subprocess import check_output

def pod_with_all_operations_for_admin_project_domain():
    resource = {}
    resource['resources'] = ['Pod']
    create_policy.create_and_apply_policies(resource=resource)


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()
    admin.create_all(user_name='john', password='c0ntrail123', role='Member',
                     project_name='new_project', domain_name='new_domain')
    source_stackrc(user_name='john', password='c0ntrail123',
                   project_name='new_project', domain_name='new_domain', auth_url='http://auth:5000/v3')
    resource = {}
    resource['resources'] = ['Pod']
    create_policy.create_and_apply_policies(resource=resource)

    #Test required operation
    #Need to be able to create, delete, get Pod
    output = check_output('kubectl apply -f templates.pod.yaml',
                          shell=True, universal_newlines=True)
    if 'created' in output:
        print("Pod created")

    
    #Shouldn't be able to create Deployment, Service, Ingress, NAD, Namespace, DaemonSet and NetworkPolicy



# pod_with_all_operations_for_admin_project_domain()
pod_with_all_operations_for_custom_user_project_domain()
