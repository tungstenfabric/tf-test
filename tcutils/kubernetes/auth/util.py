import os
import paramiko
import string
import random
from common import log_orig as contrail_logging
from common.contrail_test_init import ContrailTestInit

logger = contrail_logging.getLogger('auth')


class Util:
    templates = {
        'pod': '/var/tmp/templates/pod.yaml',
        'deployment': '/var/tmp/templates/deployment.yaml',
        'service': '/var/tmp/templates/service.yaml',
        'namespace': '/var/tmp/templates/namespace.yaml',
        'network_attachment_definition': '/var/tmp/templates/network_attachment_definition.yaml',
        'network_policy': '/var/tmp/templates/network_policy.yaml',
        'ingress': '/var/tmp/templates/ingress.yaml',
        'daemonset': '/var/tmp/templates/daemonset.yaml',
        'stackrc': '/var/tmp/templates/stackrc.sh'}

    @staticmethod
    def exec_kubectl_cmd_on_file(
            verb,
            resource,
            namespace,
            stackrc_file,
            inputs):
        # kubectl = 'kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443'
        kubectl = 'kubectl'
        template_file = Util.templates[resource]
        cmd = [f'{kubectl} {verb} -f {template_file} -n {namespace}']
        out, err = Util.execute_cmds_on_remote(
            ip=inputs.juju_server, cmd_list=cmd, stackrc_file=stackrc_file)
        return out, err

    @staticmethod
    def source_stackrc_to_file(
            user_name='admin',
            password='password',
            project_name='admin',
            domain_name='admin_domain',
            auth_url=None,
            inputs=None):
        export_list = [
            'export OS_IDENTITY_API_VERSION=3',
            f'export OS_USER_DOMAIN_NAME={domain_name}',
            f'export OS_USERNAME={user_name}',
            f'export OS_PROJECT_DOMAIN_NAME={domain_name}',
            f'export OS_PROJECT_NAME={project_name}',
            f'export OS_PASSWORD={password}',
            f'export OS_AUTH_URL={auth_url}',
            f'export OS_DOMAIN_NAME={domain_name}'
        ]
        filename = '/contrail-test/tcutils/kubernetes/auth/templates/stackrc.sh'
        with open(filename, 'w') as f:
            for exports in export_list:
                f.write(exports + os.linesep)
        inputs.copy_file_to_server(
            ip=inputs.juju_server,
            src=filename,
            dst='stackrc.sh',
            dstdir='/var/tmp/templates')
        return Util.templates['stackrc']

    @staticmethod
    def execute_cmds_on_remote(
            ip,
            cmd_list,
            stackrc_file=None,
            username='root',
            password='c0ntrail123'):
        output = ""
        error = ""
        client = paramiko.SSHClient()
        try:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=username, password=password)
        except BaseException:
            print("[!] Cannot connect to the SSH Server")
            exit()

        for cmd in cmd_list:
            if stackrc_file is not None:
                source_stackrc = f'source {stackrc_file}'
                cmd = f"{source_stackrc};{cmd}"
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode()
            error = stderr.read().decode()
        client.close()
        return output, error
