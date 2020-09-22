from example_user import ExampleUser
from util import Util
import create_policy
import os

def get_absolute_file_path(name):
    DIR = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(DIR, 'policies', name)


def pod_with_all_operations_for_admin_project_domain():
    admin = ExampleUser.admin()
    Util.source_stackrc(user_name='admin', password='password',
                        project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    
    filename = get_absolute_file_path('admin_policy.yaml')
    create_policy.apply_policies(filename)


def pod_with_all_operations_for_custom_user_project_domain():
    pass
