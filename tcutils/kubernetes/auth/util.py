import os
from subprocess import Popen, PIPE
import shlex
import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
# MSG Create a Logger class


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
    def exec_kubectl_cmd_on_file(verb, template_file):
        kubectl = 'kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443'
        # MSG USE Popen instead of check_output
        cmd = shlex.split(f'{kubectl} {verb} -f {template_file}')
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
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
    def create_resource(resource):
        output, error = Util.exec_kubectl_cmd_on_file(
            verb='create', template_file=Util.templates[resource])
        if 'created' in output:
            logging.info(f'{resource} created')
        elif 'forbidden' in error:
            logging.info(f'{resource} creation forbidden')
        else:
            errorObject = error.split("[")[1].split("]")[0]
            import json
            errorMessage = json.loads(errorObject)['message']
            logging.error(errorMessage)


    @staticmethod
    def delete_resource(resource):
        output, error = Util.exec_kubectl_cmd_on_file(
            verb='delete', template_file=Util.templates[resource])
        if 'deleted' in output:
            logging.info(f'{resource} deleted')
        elif 'forbidden' in error:
            logging.info(f'{resource} deletion forbidden')
        else:
            errorObject = error.split("[")[1].split("]")[0]
            import json
            errorMessage = json.loads(errorObject)['message']
            logging.error(errorMessage)
