from ruamel.yaml import YAML
import pprint
import os
import time


def construct_config_map_dict(policies=None):
    policy_dict = {}
    policy_dict['apiVersion'] = 'v1'
    policy_dict['kind'] = 'ConfigMap'
    policy_dict['metadata'] = {
        'name': 'k8s-auth-policy',
        'namespace': 'kube-system',
        'labels': {
            'k8s-app': 'k8s-keystone-auth'
        }
    }
    if policies is None:
        policies = [
            {
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
        ]

    policy_dict['data'] = {
        'policies': policies
    }
    return policy_dict


def create_config_map_file(policy_dict, filename=None):
    DIR = os.path.dirname(os.path.realpath(__file__))
    if filename is None:
        filename = os.path.join(DIR, 'auth_policy.yaml')
    else:
        filename = os.path.join(DIR, filename)
    yaml = YAML()
    yaml.dump(policy_dict, open(filename, 'w'))
    return filename


def create_policies(resource={}, match=[]):
    if resource.get('verbs') is None:
        resource['verbs'] = ['*']
    if resource.get('resources') is None:
        resource['resources'] = ['*']
    if resource.get('version') is None:
        resource['version'] = ['*']
    if resource.get('namespace') is None:
        resource['namespace'] = ['*']

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

    policies = [{'resource': resource, 'match': match}]
    return policies


def apply_policies(filename):
    print(f"Filename:{filename}")
    os.system(
        f'juju config kubernetes-master keystone-policy="$(cat {filename})"')
    print("Applying Config. Sleeping 20s")
    time.sleep(20)
    os.system('juju config kubernetes-master keystone-policy')
    #MSG Need to reduce sleep time and add check_policy_in_config_map



def create_and_apply_policies(resource={}, match=[], filename=None):
    policies = create_policies(resource=resource, match=match)
    policy_dict = construct_config_map_dict(policies)
    filename = create_config_map_file(policy_dict, filename=filename)
    apply_policies(filename)


# pprint.pprint(create_policies(resource={'verbs': ['get'], 'resources': ['Pod']}))
# policies = create_policies(resource={'verbs': ['get'], 'resources': ['Pod']})
# policy_dict = construct_config_map_dict(policies)
# create_config_map_file(policy_dict)
# create_and_apply_policies(resource={'verbs': ['get', 'create'], 'resources': ['Pod']}, filename='policy.yaml')
