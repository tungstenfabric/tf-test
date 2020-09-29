from ruamel.yaml import YAML
import pprint
import os
import time
from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
from jinja2 import Environment, FileSystemLoader
import json


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


def create_policies(resource={}, match=[]):
    if resource.get('verbs') is None:
        resource['verbs'] = ['*']
    if resource.get('resources') is None:
        resource['resources'] = ['*']
    if resource.get('version') is None:
        resource['version'] = '*'
    if resource.get('namespace') is None:
        resource['namespace'] = '*'

    if len(match) == 0:
        role_dict = {
            'type': 'role',
            'values': ['*']
        }
        project_dict = {
            'type': 'project',
            'values': ['admin']
        }
        match.append(role_dict)
        match.append(project_dict)

    admin_policy = {
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

    policies = [admin_policy, {'resource': resource, 'match': match}]
    return policies


def apply_policies(filename):
    print(f"Applying policy file:{filename}")
    os.system(
        f'juju config kubernetes-master keystone-policy="$(cat {filename})"')
    admin = ExampleUser.admin()
    Util.source_stackrc(user_name='admin', password='password',
                        project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    print("Applying Config. Sleeping 30s")
    time.sleep(30)
    os.system(
        'kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443 describe configmap -n kube-system k8s-auth-policy')
    # MSG Need to reduce sleep time and add check_policy_in_config_map, can get -o yaml and then convert data policies to string and then compare
    # out = check_output("kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443 describe configmap -n kube-system k8s-auth-policy", shell=True, universal_newlines=True)
    # out.split("policies")[1].split("\n")[2]
    # Next compare with auth_policy data policies
    # import yaml
    # with open('/root/nuthanc-tf-test/tcutils/kubernetes/auth/templates/auth_policy.yaml') as f:
    # data = yaml.load(f, Loader=yaml.FullLoader)


def create_and_apply_policies(resource={}, match=[], filename=None):
    policies = create_policies(resource=resource, match=match)
    filename = insert_policies_in_template_file(policies)
    apply_policies(filename)

def check_policy_in_config_map():
    admin = ExampleUser.admin()
    Util.source_stackrc(user_name='admin', password='password',
                        project_name='admin', domain_name='admin_domain', auth_url=admin.auth_url)
    from subprocess import check_output
    out = check_output("kubectl -v=5 --insecure-skip-tls-verify=true -s https://192.168.30.29:6443 describe configmap -n kube-system k8s-auth-policy", shell=True, universal_newlines=True)
    cmd_policy_string = out.split("policies")[1].split("\n")[2]

    resource = {}
    resource['resources'] = ['pods']
    role_dict = {
        'type': 'role',
        'values': ['Member']
    }
    project_dict = {
        'type': 'project',
        'values': ['new_project']
    }
    user_dict = {
        "type": 'user',
        "values": ['john']
    }
    match = [role_dict, project_dict, user_dict]
    policies = create_policies(resource=resource, match=match)
    policies_json = json.dumps(policies)
    policies_string = str(policies_json)
    print(f"Policy_string: {policies_string}")
    print()
    print(f"cmd_policy_string: {cmd_policy_string}")
    print(cmd_policy_string == policies_string)


check_policy_in_config_map()

# pprint.pprint(create_policies(resource={'verbs': ['get'], 'resources': ['pods']}))
# policies = create_policies(resource={'verbs': ['get'], 'resources': ['pods']})
# policy_dict = construct_config_map_dict(policies)
# create_config_map_file(policy_dict)
# create_and_apply_policies(resource={'verbs': ['get', 'create'], 'resources': ['pods']}, filename='policy.yaml')
