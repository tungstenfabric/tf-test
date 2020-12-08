
import os
from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.util import Util
from tcutils.kubernetes.auth.example_user import ExampleUser
import time
import random

import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')


class ResourceUtil(Util):
    @staticmethod
    def resource_with_expectation(verb, resource_expectation_list, namespace):
        for resource_exp in resource_expectation_list:
            expectation = False
            if "-expected" in resource_exp:
                resource = resource_exp.split("-")[0]
                expectation = True
            else:
                resource = resource_exp

            output, error = Util.exec_kubectl_cmd_on_file(
                verb=verb, template_file=Util.templates[resource], namespace=namespace)
            if verb in output:
                if expectation == True:
                    logging.info(f'{verb} {resource} successful in {namespace} namespace')
                else:
                    logging.warning(
                        f'{verb} {resource} successful even when expectation is False')
            elif 'forbidden' in error:
                logging.warning(f'{verb} {resource} forbidden')
            else:
                if 'already' in error:
                    Util.exec_kubectl_cmd_on_file(
                        verb='delete', template_file=Util.templates[resource], namespace=namespace)
                    time.sleep(10)
                    Util.exec_kubectl_cmd_on_file(
                        verb='create', template_file=Util.templates[resource], namespace=namespace)
                else:
                    errorObject = error.split("[")[1].split("]")[0]
                    import json
                    errorMessage = json.loads(errorObject)['message']
                    logging.error(errorMessage)

    @staticmethod
    def create_policy_and_perform_operations(resource={}, match=[], resource_expectation_list=[], stackrc_dict={}):
        create_policy.create_and_apply_policies(resource=resource, match=match)
        ResourceUtil.perform_operations(
            stackrc_dict, resource_expectation_list)

    @staticmethod
    def perform_operations(stackrc_dict={}, resource_expectation_list=[], namespace='default'):
        Util.source_stackrc(**stackrc_dict)
        ResourceUtil.resource_with_expectation(
            verb='create', resource_expectation_list=resource_expectation_list, namespace=namespace)
        ResourceUtil.resource_with_expectation(
            verb='delete', resource_expectation_list=resource_expectation_list, namespace=namespace)

    @staticmethod
    def create_test_user_openstack_objects_and_return_match_list_and_stackrc_dict(rand=False):
        admin = ExampleUser.admin()
        user_name = Util.get_random_string() if rand else 'test'
        admin.create_all(user_name=user_name, password='c0ntrail123', role='Member',
                         project_name='test_project', domain_name='test_domain')
        role_dict = {
            'type': 'role',
            'values': ['Member']
        }
        project_dict = {
            'type': 'project',
            'values': ['test_project']
        }
        user_dict = {
            "type": 'user',
            "values": [user_name]
        }
        match = [role_dict, project_dict, user_dict]
        stackrc_dict = {
            'user_name': user_name,
            'password': 'c0ntrail123',
            'project_name': 'test_project',
            'domain_name': 'test_domain',
            'auth_url': admin.auth_url
        }
        return match, stackrc_dict

    @staticmethod
    def admin_stackrc():
        admin = ExampleUser.admin()
        return {
            'user_name': 'admin',
            'password': 'password',
            'project_name': 'admin',
            'domain_name': 'admin_domain',
            'auth_url': admin.auth_url
        }

    # Temp method
    @staticmethod
    def create_custom_user_openstack_objects_and_return_match_list_and_stackrc_dict():
        admin = ExampleUser.admin()
        admin.create_all(user_name='test', password='c0ntrail123', role='Member',
                         project_name='test_project', domain_name='test_domain')
        role_dict = {
            'type': 'role',
            'values': ['Member']
        }
        project_dict = {
            'type': 'project',
            'values': ['test_project']
        }
        user_dict = {
            "type": 'user',
            "values": ['test']
        }
        match = [role_dict, project_dict, user_dict]
        stackrc_dict = {
            'user_name': 'test',
            'password': 'c0ntrail123',
            'project_name': 'test_project',
            'domain_name': 'test_domain',
            'auth_url': admin.auth_url
        }
        return match, stackrc_dict
