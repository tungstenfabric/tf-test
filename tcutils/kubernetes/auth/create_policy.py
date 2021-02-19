import pprint
import os
import time
import json
from jinja2 import Environment, FileSystemLoader
from common.contrail_test_init import ContrailTestInit

from tcutils.kubernetes.auth.example_user import ExampleUser
from tcutils.kubernetes.auth.util import Util
from common import log_orig as contrail_logging

logger = contrail_logging.getLogger('auth')


def insert_policies_in_template_file(policies, filename='auth_policy.yaml', inputs=None):
    THIS_DIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIR = os.path.join(THIS_DIR, 'templates')

    filename_with_path = os.path.join(TEMPLATE_DIR, filename)

    policies_json = json.dumps(policies)
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("policy.yaml.j2")
    with open(filename_with_path, 'w') as f:
        f.write(template.render(policies=policies_json))
    inputs.copy_file_to_server(
        ip=inputs.juju_server,
        src='/contrail-test/tcutils/kubernetes/auth/templates/%s' % filename,
        dst=filename,
        dstdir='/var/tmp/templates',
        force=True)
    rel_file = os.path.join(
        '/var/tmp/templates',
        filename)
    return rel_file


def get_custom_user_policy(
        verbs,
        resources,
        project,
        user,
        namespace='*',
        role='Member'):
    return {
        'resource': {
            'verbs': verbs,
            'resources': resources,
            'version': '*',
            'namespace': namespace
        },
        "match": [
            {
                "type": "role",
                "values": [
                    role
                ]
            },
            {
                "type": "project",
                "values": [
                    project
                ]
            },
            {
                "type": "user",
                "values": [
                    user
                ]
            }
        ]
    }


def get_userA_policy():
    verbs = ['create']
    resources = ['pods', 'deployments']
    project = 'userA_project'
    user = 'userA'
    return get_custom_user_policy(verbs, resources, project, user)


def get_userB_policy():
    verbs = ['delete']
    resources = ['pods', 'deployments']
    project = 'userB_project'
    user = 'userB'
    return get_custom_user_policy(verbs, resources, project, user)


def get_userC_policy():
    verbs = ['*']
    resources = ['services']
    project = 'userC_project'
    user = 'userC'
    return get_custom_user_policy(
        verbs,
        resources,
        project,
        user,
        namespace='zomsrc')


def get_userD_policy():
    verbs = ['*']
    resources = ['pods', 'deployments', 'services']
    project = 'userD_project'
    user = 'userD'
    return get_custom_user_policy(
        verbs, resources, project, user, namespace='easy')


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


def check_policy_in_config_map(policies, juju_server):
    cmds = ["kubectl config use-context juju-context",
            "kubectl describe configmap -n kube-system k8s-auth-policy"]
    out, err = Util.execute_cmds_on_remote(
        ip=juju_server, cmd_list=cmds)
    cmd_policy_string = out.split("policies")[1].split("\n")[2].strip()
    policies_json = json.dumps(policies)
    policies_string = str(policies_json)

    logger.info("Waiting for policy to update in ConfigMap")
    while cmd_policy_string != policies_string:
        out, err = Util.execute_cmds_on_remote(
            ip=juju_server, cmd_list=cmds)
        cmd_policy_string = out.split("policies")[1].split("\n")[2]
        time.sleep(2)
    time.sleep(5)  # For master to stabilize, give additional 5 seconds
    logger.info("Policy updated in ConfigMap")
    cmd = ["kubectl config use-context keystone"]
    out, err = Util.execute_cmds_on_remote(
        ip=juju_server, cmd_list=cmd)


def apply_policies_and_check_in_config_map(policies, filename, juju_server):
    logger.info(f"Applying policy file: {filename}")
    cmd = [
        'juju config kubernetes-master keystone-policy="$(cat %s)"' % filename]
    out, err = Util.execute_cmds_on_remote(
        ip=juju_server, cmd_list=cmd)
    check_policy_in_config_map(policies, juju_server)


def create_and_apply_policies(
        resource={},
        match=[],
        inputs=None,
        filename='auth_policy.yaml'):
    policies = create_policies(resource=resource, match=match)
    filename = insert_policies_in_template_file(
        policies, filename=filename, inputs=inputs)
    apply_policies_and_check_in_config_map(
        policies, filename, inputs.juju_server)
