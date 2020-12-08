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

# test_individual_resource_with_all_operations_for_custom_user_project_domain()


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


# For manual test
def operations_for_custom_user_project_domain():
    resource = {'resources': ['deployments'], 'verbs': ['create']}
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
    resource_expectation_list = ['pod', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.create_policy_and_perform_operations(
        resource=resource, match=match, stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


# operations_for_custom_user_project_domain()

def delete_all():
    admin = ExampleUser.admin()
    ResourceUtil.source_stackrc(auth_url=admin.auth_url)
    resource_list = ['pod', 'deployment', 'service', 'namespace',
                     'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.resource('delete', resource_list)

# delete_all()


#For manual test
def manual_test2():
    # resource = {'resources': ['pods'], 'verbs': ['create','get','list'], 'namespace': 'easy'}
    resource = {'resources': ['pods'], 'verbs': ['create','get','list']}
    match, stackrc_dict = ResourceUtil.create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict()
    create_policy.create_and_apply_policies(resource=resource, match=match)

# manual_test2()

def test_all_in_one():
    # Create the required users, projects and domains
    admin = ExampleUser.admin()
    

    admin.create_all(user_name='zoro', password='c0ntrail123', role='Member',
                     project_name='zoro_project', domain_name='zoro_domain')
    admin.create_all(user_name='ola', password='c0ntrail123', role='Member',
                     project_name='ola_project', domain_name='ola_domain')
    admin.create_all(user_name='uber', password='c0ntrail123', role='Member',
                     project_name='uber_project', domain_name='uber_domain')
    admin.create_all(user_name='zomato', password='c0ntrail123', role='Member',
                     project_name='zomato_project', domain_name='zomato_domain')

    ResourceUtil.source_stackrc(**ResourceUtil.admin_stackrc())
    os.system('kubectl create ns zomsrc')
    os.system('kubectl create ns easy')
    # os.system('juju config kubernetes-master keystone-policy="$(cat /root/nuthanc-tf-test/tcutils/kubernetes/auth/templates/all_in_one_policy.yaml)"')
    # import pdb;pdb.set_trace()
    # kubectl describe configmap -n kube-system k8s-auth-policy
    # Stackrcs in o7k

    # For ola user, only create pods and deployments and nothing else
    print("For ola user, only create pods and deployments and nothing else")
    stackrc_dict = {
        'user_name': 'ola',
        'password': 'c0ntrail123',
        'project_name': 'ola_project',
        'domain_name': 'ola_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.perform_operations(
        stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)


    # For uber user, only delete pods and deployments and nothing else
    print("\nFor uber user, only delete pods and deployments and nothing else")
    stackrc_dict = {
        'user_name': 'uber',
        'password': 'c0ntrail123',
        'project_name': 'uber_project',
        'domain_name': 'uber_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod-expected', 'deployment-expected', 'service', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.perform_operations(
        stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)

    # For zomato user, create service in zomsrc namespace and nothing else should work
    print("\nFor zomato user, create service in zomsrc namespace and nothing else should work")
    stackrc_dict = {
        'user_name': 'zomato',
        'password': 'c0ntrail123',
        'project_name': 'zomato_project',
        'domain_name': 'zomato_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod', 'deployment', 'service-expected', 'namespace',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.perform_operations(
        stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list)
    ResourceUtil.perform_operations(
        stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list, namespace='zomsrc')

    # For zoro user, any operation on pods, deployments and services but only in easy namespace
    print("\nFor zoro user, any operation on pods, deployments and services but only in easy namespace")
    stackrc_dict = {
        'user_name': 'zoro',
        'password': 'c0ntrail123',
        'project_name': 'zoro_project',
        'domain_name': 'zoro_domain',
        'auth_url': admin.auth_url
    }
    resource_expectation_list = ['pod-expected', 'deployment-expected', 'service-expected', 'namespace-expected',
                                 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset']
    ResourceUtil.perform_operations(
        resource_expectation_list=resource_expectation_list, stackrc_dict=stackrc_dict)
    ResourceUtil.perform_operations(
        stackrc_dict=stackrc_dict, resource_expectation_list=resource_expectation_list, namespace='easy')
    
test_all_in_one()



