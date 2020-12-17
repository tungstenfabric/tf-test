
from tcutils.kubernetes.auth import create_policy
from tcutils.kubernetes.auth.util import Util
from tcutils.kubernetes.auth.example_user import ExampleUser
import time
from tcutils.util import get_random_string
from common import log_orig as contrail_logging
import json

logger = contrail_logging.getLogger('auth')


class ResourceUtil(Util):
    @staticmethod
    def resource_with_expectation(
            verb,
            resource_expectation,
            namespace,
            stackrc_file, inputs):
        resources = [
            'pod',
            'deployment',
            'service',
            'namespace',
            'network_attachment_definition',
            'network_policy',
            'ingress',
            'daemonset']
        for key in resources:
            if key not in resource_expectation.keys():
                resource_expectation[key] = False
        for resource_exp in resource_expectation:
            expectation = False
            if resource_expectation[resource_exp]:
                resource = resource_exp
                expectation = True
            else:
                resource = resource_exp

            output, error = Util.exec_kubectl_cmd_on_file(
                verb=verb, resource=resource, namespace=namespace, stackrc_file=stackrc_file, inputs=inputs)
            if verb in output:
                if expectation:
                    logger.info(
                        f'{verb} {resource} successful in {namespace} namespace')
                else:
                    assert False, f'{verb} {resource} successful even when expectation is False'
            elif 'forbidden' in error:
                logger.warning(f'{verb} {resource} forbidden')
            else:
                if 'already' in error:
                    Util.exec_kubectl_cmd_on_file(
                        verb='delete',
                        resource=resource,
                        namespace=namespace,
                        stackrc_file=stackrc_file)
                    Util.exec_kubectl_cmd_on_file(
                        verb='create',
                        resource=resource,
                        namespace=namespace,
                        stackrc_file=stackrc_file)
                else:
                    if '[' in error:
                        errorObject = error.split("[")[1].split("]")[0]
                        errorMessage = json.loads(errorObject)['message']
                        logger.error(errorMessage)
                    else:
                        logger.error(error)
                    logger.error(f'Error while {resource} {verb}')
                    raise Exception(error)

    @staticmethod
    def create_policy_and_perform_operations(
            resource={},
            match=[],
            resource_expectation={},
            stackrc_dict={},
            inputs=None):
        create_policy.create_and_apply_policies(
            resource=resource, match=match, inputs=inputs)
        ResourceUtil.perform_operations(
            stackrc_dict, resource_expectation, inputs=inputs)

    @staticmethod
    def perform_operations(
            stackrc_dict={},
            resource_expectation={},
            namespace='default',
            inputs=None):
        stackrc_file = Util.source_stackrc_to_file(
            **stackrc_dict, inputs=inputs)
        ResourceUtil.resource_with_expectation(
            verb='create',
            resource_expectation=resource_expectation,
            namespace=namespace,
            stackrc_file=stackrc_file, inputs=inputs)
        ResourceUtil.resource_with_expectation(
            verb='delete',
            resource_expectation=resource_expectation,
            namespace=namespace,
            stackrc_file=stackrc_file, inputs=inputs)

    @staticmethod
    def get_custom_match_stackrc(
            rand=False):
        admin = ExampleUser.admin()
        user_name = get_random_string() if rand else 'test'
        admin.create_all(
            user_name=user_name,
            password='c0ntrail123',
            role='Member',
            project_name='test_project',
            domain_name='test_domain')
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
        admin.create_all(
            user_name='test',
            password='c0ntrail123',
            role='Member',
            project_name='test_project',
            domain_name='test_domain')
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
