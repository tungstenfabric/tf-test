from tcutils.kubernetes.auth.lib.o7k_lib import O7kLib
from common.contrail_test_init import ContrailTestInit
from tcutils.kubernetes.auth.util import Util


class ExampleUser(O7kLib):
    def __init__(
            self,
            username=None,
            password=None,
            domain_name=None,
            project_name=None,
            auth_url=None):
        super().__init__(
            username=username,
            password=password,
            domain_name=domain_name,
            project_name=project_name,
            auth_url=auth_url)

    @classmethod
    def admin(cls):
        return cls(
            username='admin',
            password='password',
            domain_name='admin_domain',
            project_name='admin',
            auth_url=cls.get_auth_url())

    @staticmethod
    def get_auth_url():
        cti_obj = ContrailTestInit(input_file='contrail_test_input.yaml')
        cmd = ["juju status | grep 5000 | awk '{print $5}'"]
        auth_ip, err = Util.execute_cmds_on_remote(
            ip=cti_obj.juju_server, cmd_list=cmd)
        auth_ip = auth_ip.strip()
        auth_url = f'http://{auth_ip}:5000/v3'
        return auth_url

    def create_all(
            self,
            user_name='test_user',
            password='test_password',
            role='Member',
            project_name='test_project',
            domain_name='test_domain'):
        self.create_domain(domain_name)
        self.create_project(project_name=project_name, domain_name=domain_name)
        self.create_user(user=user_name, password=password,
                         project_name=project_name, domain_name=domain_name)
        self.add_user_role(user_name=user_name, role_name=role,
                           project_name=project_name, domain_name=domain_name)

    def delete_all(
            self,
            user_name='test_user',
            project_name='test_project',
            domain_name='test_domain'):
        self.delete_user(user_name, project_name=project_name,
                         domain_name=domain_name)
        self.delete_project(project_name)
        self.delete_domain(domain_name)
