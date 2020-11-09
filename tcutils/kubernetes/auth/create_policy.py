from subprocess import check_output
import pprint
import os
import time
import json
from jinja2 import Environment, FileSystemLoader

from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
from common import log_orig as contrail_logging

logger = contrail_logging.getLogger(__name__)


def insert_policies_in_template_file(policies, filename=None):
    THIS_DIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIR = os.path.join(THIS_DIR, 'templates')

    if filename is None:
        filename = os.path.join(TEMPLATE_DIR, 'auth_policy.yaml')
    else:
        filename = os.path.join(TEMPLATE_DIR, filename)

    policies_json = json.dumps(policies)
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("policy.yaml.j2")
    with open(filename, 'w') as f:
        f.write(template.render(policies=policies_json))
    return filename


def get_admin_policy():
    return {
        'resource': {
            'verbs': ['*'],
            'resources': ['*'],
            'version': '*',
            'namespace': '*'
        },
        'match': [
            {
                'type': 'role',
                'values': ['*']
            },
            {
                'type': 'project',
                'values': ['admin']
            }
        ]
    }


def create_policies(resource={}, match=[]):
    '''
    If no match is provided, then admin_policy is returned with everything enabled in resource
    '''
    admin_policy = get_admin_policy()
    if len(match) == 0:
        policies = [admin_policy]
        return policies

    if resource.get('verbs') is None:
        resource['verbs'] = ['*']
    if resource.get('resources') is None:
        resource['resources'] = ['*']
    if resource.get('version') is None:
        resource['version'] = '*'
    if resource.get('namespace') is None:
        resource['namespace'] = '*'

    policies = [admin_policy, {'resource': resource, 'match': match}]
    return policies

# MSG need to add condition when the same policy is applied again
def check_policy_in_config_map(policies):
    admin = ExampleUser.admin()
    Util.source_stackrc(user_name='admin', password='password',
                        project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    out = check_output("kubectl describe configmap -n kube-system k8s-auth-policy",
                       shell=True, universal_newlines=True)
    cmd_policy_string = out.split("policies")[1].split("\n")[2]
    policies_json = json.dumps(policies)
    policies_string = str(policies_json)

    logger.info("Waiting for policy to update in ConfigMap")
    while cmd_policy_string != policies_string:
        out = check_output("kubectl describe configmap -n kube-system k8s-auth-policy",
                           shell=True, universal_newlines=True)
        cmd_policy_string = out.split("policies")[1].split("\n")[2]
        time.sleep(2)
    time.sleep(5)  # For master to stabilize, give additional 5 seconds
    logger.info("Policy updated in ConfigMap")


def apply_policies_and_check_in_config_map(policies, filename):
    logger.info(f"Applying policy file: {filename}")
    os.system(
        f'juju config kubernetes-master keystone-policy="$(cat {filename})"')
    check_policy_in_config_map(policies)


def create_and_apply_policies(resource={}, match=[], filename=None):
    policies = create_policies(resource=resource, match=match)
    filename = insert_policies_in_template_file(policies)
    apply_policies_and_check_in_config_map(policies, filename)


# pprint.pprint(create_policies(resource={'verbs': ['get'], 'resources': ['pods']}))
# policies = create_policies(resource={'verbs': ['get'], 'resources': ['pods']})
# policy_dict = construct_config_map_dict(policies)
# create_config_map_file(policy_dict)
# create_and_apply_policies(resource={'verbs': ['get', 'create'], 'resources': ['pods']}, filename='policy.yaml')
