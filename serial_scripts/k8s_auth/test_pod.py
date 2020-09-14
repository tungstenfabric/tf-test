from tcutils.kubernetes.auth import create_policy
# from tcutils.kubernetes.auth.example_user import ExampleUser

def pod_with_all_operations_for_admin_project():
    resource = {}
    resource['resources'] = ['Pod']
    create_policy.create_and_apply_policies(resource=resource, filename='policy.yaml')

pod_with_all_operations_for_admin_project()