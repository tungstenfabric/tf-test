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
    create_policy.apply_policies(filename)

    Util.source_stackrc(user_name='admin', password='password',
                        project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    Util.create_resource('pod')
    Util.create_resource('deployment')
    Util.create_resource('service')
    Util.create_resource('namespace')
    Util.create_resource('network_attachment_definition')
    Util.create_resource('network_policy')
    Util.create_resource('ingress')
    Util.create_resource('daemonset')

    Util.delete_resource('pod')
    Util.delete_resource('deployment')
    Util.delete_resource('service')
    Util.delete_resource('namespace')
    Util.delete_resource('network_attachment_definition')
    Util.delete_resource('network_policy')
    Util.delete_resource('ingress')
    Util.delete_resource('daemonset')


def pod_with_all_operations_for_custom_user_project_domain():
    admin = ExampleUser.admin()

    filename = get_absolute_file_path('john_pod_policy.yaml')
    create_policy.apply_policies(filename)

    Util.source_stackrc(user_name='john', password='c0ntrail123',
                        project_name='new_project', domain_name='new_domain', auth_url=admin.auth_url)
    Util.create_resource('pod')
    Util.create_resource('deployment')
    Util.create_resource('service')
    Util.create_resource('namespace')
    Util.create_resource('network_attachment_definition')
    Util.create_resource('network_policy')
    Util.create_resource('ingress')
    Util.create_resource('daemonset')

    Util.delete_resource('pod')
    Util.delete_resource('deployment')
    Util.delete_resource('service')
    Util.delete_resource('namespace')
    Util.delete_resource('network_attachment_definition')
    Util.delete_resource('network_policy')
    Util.delete_resource('ingress')
    Util.delete_resource('daemonset')


all_operations_for_admin_project_domain()
pod_with_all_operations_for_custom_user_project_domain()
