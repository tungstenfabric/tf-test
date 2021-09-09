from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
import subprocess
import string

cmd_tmpl = string.Template('python3 tools/scale/scale_lr.py --api_server_ip ${api_server} --auth_url ${auth_url} --username ${user} --password ${password} --tenant ${project} --scale_n ${nr}')

class TestLRScale(GenericTestBase):

    def _run_cleanup(self, cmd):
        try:
            output = subprocess.check_output(cmd, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass

    def scale_test(self, scenario, scale_number):
        restart_services = ['api-server','schema']
        cmd_base = cmd_tmpl.substitute(api_server=self.inputs.cfgm_ips[0],
                        auth_url=self.inputs.auth_url,
                        user=self.connections.username,
                        password=self.connections.password,
                        project=self.connections.project_name,
                        nr=scale_number)
        cmd_create = cmd_base + ' {} create'.format(scenario)
        cmd_verify = cmd_base + ' {} verify'.format(scenario)
        cmd_cleanup = cmd_base + ' {} cleanup'.format(scenario)
        self.addCleanup(self._run_cleanup, cmd_cleanup)

        try:
            output= subprocess.check_output(cmd_create, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass

        try:
            output= subprocess.check_output(cmd_verify, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass
        assert b'Passed' in output, 'Not able scale expected scale number'

        assert self.inputs.verify_state()
        for service in restart_services:
            self.inputs.restart_container(self.inputs.cfgm_ips, service)

        try:
            output= subprocess.check_output(cmd_verify, shell=True)
            self.logger.info(output)
        except subprocess.CalledProcessError:
            pass
        assert b'Passed' in output, 'Expected scale number not seen after service restart'

    @preposttest_wrapper
    def test_lr(self):
        self.scale_test('scale_lr', self.inputs.config_node_lr_scale or 1000)

    @preposttest_wrapper
    def test_vn_per_lr(self):
        self.scale_test('scale_vn', self.inputs.config_node_vn_per_lr_scale or 1000)

    @preposttest_wrapper
    def test_subnet_per_vn_lr(self):
        self.scale_test('scale_subnet', self.inputs.config_node_subnet_vn_per_lr_scale or 1000)