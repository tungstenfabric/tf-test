from tcutils.kubernetes.auth.lib.o7k_lib import O7kLib
from subprocess import check_output


class ExampleUser(O7kLib):
    def __init__(self, username=None, password=None, domain_name=None, project_name=None, auth_url=None):
        super().__init__(username=username, password=password,
                         domain_name=domain_name, project_name=project_name, auth_url=auth_url)

    @classmethod
    def admin(cls):
        return cls(username='admin', password='password', domain_name='admin_domain', project_name='admin', auth_url=cls.get_auth_url())

    @staticmethod
    def get_auth_url():
        auth_ip = check_output(
            "juju status | grep 5000 | awk '{print $5}'", shell=True, universal_newlines=True).strip()
        auth_url = f'http://{auth_ip}:5000/v3'
        return auth_url

    def create_all(self, user_name='test_user', password='test_password', role='Member', project_name='test_project', domain_name='test_domain'):
        self.create_domain(domain_name)
        self.create_project(project_name=project_name, domain_name=domain_name)
        self.create_user(user=user_name, password=password,
                         project_name=project_name, domain_name=domain_name)
        self.add_user_role(user_name=user_name, role_name=role,
                           project_name=project_name, domain_name=domain_name)

    def delete_all(self, user_name='test_user', project_name='test_project', domain_name='test_domain'):
        self.delete_user(user_name, project_name=project_name,
                         domain_name=domain_name)
        self.delete_project(project_name)
        self.delete_domain(domain_name)


# admin = ExampleUser(username='admin', password='password', domain_name='admin_domain',
#                project_name='admin', auth_url='http://192.168.30.76:5000/v3')
# Utilizing classmethod to act as factory functions to get similar parameters as above
admin = ExampleUser.admin()
admin.create_all('john', 'c0ntrail123', 'Member', 'new_project', 'new_domain')
admin.delete_all('john', 'new_project', 'new_domain')

# Create and Delete for test_user
admin.create_all()
admin.delete_all()
