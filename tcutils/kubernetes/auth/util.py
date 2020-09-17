import os
from subprocess import check_output
import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
#MSG Create a Logger class

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
        try:
            output = check_output(f'kubectl create -f {Util.templates[resource]}', shell=True, universal_newlines=True)
            if 'created' in output:
                logging.info(f'{resource} created')
        except Exception as e:
            logging.error(e)

        