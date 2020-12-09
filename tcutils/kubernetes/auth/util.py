import os
import paramiko
from subprocess import Popen, PIPE
import shlex
import string
import random
from common import log_orig as contrail_logging

logger = contrail_logging.getLogger(__name__)


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
    }

    @staticmethod
    def exec_kubectl_cmd_on_file(verb, template_file, namespace):
        # kubectl = 'kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443'
        kubectl = 'kubectl'
        cmd = shlex.split(f'{kubectl} {verb} -f {template_file} -n {namespace}')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        # p = Popen(f'{kubectl} {verb} -f {template_file}', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        output, error = p.communicate()
        return output, error


    @staticmethod
    def source_stackrc(user_name='admin', password='password', project_name='admin', domain_name='admin_domain', auth_url=None):
        os.environ['OS_IDENTITY_API_VERSION'] = '3'
        os.environ['OS_USER_DOMAIN_NAME'] = domain_name
        os.environ['OS_USERNAME'] = user_name
        os.environ['OS_PROJECT_DOMAIN_NAME'] = domain_name
        os.environ['OS_PROJECT_NAME'] = project_name
        os.environ['OS_PASSWORD'] = password
        os.environ['OS_AUTH_URL'] = auth_url
        os.environ['OS_DOMAIN_NAME'] = domain_name
        

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
    def execute_cmds_on_remote(ip, cmd_list):
        client = paramiko.SSHClient()
        try:
            # k = paramiko.RSAKey.from_private_key_file('~/.ssh/id_rsa')
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=ip, username='ubuntu')
        except:
            print("[!] Cannot connect to the SSH Server")
            exit()

        for cmd in cmd_list:
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
            err = stderr.read().decode()
        if err:
            print(err)
        client.close()

    # MSG Need to get the kubemanager ip from contrail_test_input
    @staticmethod
    def restart_kube_manager():
        Util.execute_cmds_on_remote(
            '192.168.7.29', ['sudo docker restart contrailkubernetesmaster_kubemanager_1'])

    # MSG Need to get vrouter agent ip from contrail_test_input
    @staticmethod
    def restart_vrouter_agent():
        Util.execute_cmds_on_remote(
            '192.168.7.19', ['sudo docker restart vrouter_vrouter-agent_1'])
