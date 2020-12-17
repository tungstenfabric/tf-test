from example_user import ExampleUser
from util import Util
import create_policy
import os


def get_absolute_file_path(name):
    DIR = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(DIR, 'policies', name)


def all_operations_for_admin_project_domain():
    admin = ExampleUser.admin()

    filename = get_absolute_file_path('admin_all_policy.yaml')

    create_policy.create_and_apply_policies(filename=filename)

    Util.source_stackrc_to_file(user_name='admin', password='password',
                                project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    Util.resource(verb='create', resource_list=[
                  'pod', 'deployment', 'service', 'namespace', 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=[
                  'pod', 'deployment', 'service', 'namespace', 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()

    filename = get_absolute_file_path('john_pod_policy.yaml')
    resource = {}
    resource['resources'] = ['pods']
    create_policy.create_and_apply_policies(
        resource=resource, filename=filename)

    Util.source_stackrc_to_file(user_name='john', password='c0ntrail123',
                                project_name='new_project', domain_name='new_domain', auth_url=admin.auth_url)
    Util.resource(verb='create', resource_list=[
                  'pod', 'deployment', 'service', 'namespace', 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])
    Util.resource(verb='delete', resource_list=[
                  'pod', 'deployment', 'service', 'namespace', 'network_attachment_definition', 'network_policy', 'ingress', 'daemonset'])


all_operations_for_admin_project_domain()
pod_with_all_operations_for_custom_user_project_domain()
