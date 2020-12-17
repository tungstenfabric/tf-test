import os
import paramiko
import string
import random
from common import log_orig as contrail_logging
from common.contrail_test_init import ContrailTestInit

logger = contrail_logging.getLogger('auth')


class Util:
    cwd = os.path.dirname(os.path.realpath(__file__))
    templates = {
        'pod': f'{cwd}/templates/pod.yaml',
        'deployment': f'{cwd}/templates/deployment.yaml',
        'service': f'{cwd}/templates/service.yaml',
        'namespace': f'{cwd}/templates/namespace.yaml',
        'network_attachment_definition': f'{cwd}/templates/network_attachment_definition.yaml',
        'network_policy': f'{cwd}/templates/network_policy.yaml',
        'ingress': f'{cwd}/templates/ingress.yaml',
        'daemonset': f'{cwd}/templates/daemonset.yaml',
        'stackrc': f'{cwd}/templates/stackrc.sh'
    }

    @staticmethod
    def exec_kubectl_cmd_on_file(verb, template_file, namespace, stackrc_file):
        # kubectl = 'kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443'
        kubectl = 'kubectl'
        cmd = [f'{kubectl} {verb} -f {template_file} -n {namespace}']
        cti_obj = ContrailTestInit(input_file='contrail_test_input.yaml')
        out, err = Util.execute_cmds_on_remote(
            ip=cti_obj.juju_server, cmd_list=cmd, stackrc_file=stackrc_file)
        return out, err

    @staticmethod
    def source_stackrc_to_file(
            user_name='admin',
            password='password',
            project_name='admin',
            domain_name='admin_domain',
            auth_url=None):
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
        filename = Util.templates['stackrc']
        with open(filename, 'w') as f:
            for exports in export_list:
                f.write(exports + os.linesep)
        return filename

    @staticmethod
    def resource(verb, resource_list):
        for resource in resource_list:
            output, error = Util.exec_kubectl_cmd_on_file(
                verb=verb, template_file=Util.templates[resource], namespace='default')
            if verb in output:
                logger.info(f'{verb} {resource} successful')
            elif 'forbidden' in error:
                logger.info(f'{verb} {resource} forbidden')
            else:
                errorObject = error.split("[")[1].split("]")[0]
                import json
                errorMessage = json.loads(errorObject)['message']
                logger.error(errorMessage)

    @staticmethod
    def get_random_string(size=8):
        return ''.join(random.choices(string.ascii_lowercase +
                                      string.digits, k=size))

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

    # MSG Need to get the kubemanager ip from contrail_test_input

    @staticmethod
    def restart_kube_manager():
        cti_obj = ContrailTestInit(input_file='contrail_test_input.yaml')
        ip = cti_obj.inputs.kube_manager_ips[0]
        Util.execute_cmds_on_remote(
            ip, ['sudo docker restart contrailkubernetesmaster_kubemanager_1'])

    # MSG Need to get vrouter agent ip from contrail_test_input
    @staticmethod
    def restart_vrouter_agent():
        cti_obj = ContrailTestInit(input_file='contrail_test_input.yaml')
        ip = cti_obj.inputs.k8s_slave_ips[0]
        Util.execute_cmds_on_remote(
            ip, ['sudo docker restart vrouter_vrouter-agent_1'])
