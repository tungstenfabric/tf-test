from common.k8s.base import BaseK8sTest


class BaseK8sAuth(BaseK8sTest):

    @classmethod
    def setUpClass(cls):
        super(BaseK8sAuth, cls).setUpClass()
        juju_server = cls.inputs.juju_server
        cls.inputs.copy_file_to_server(
            ip=juju_server,
            src='/contrail-test/tcutils/kubernetes/auth/templates/',
            dst='templates',
            dstdir='/var/tmp/templates')

    @classmethod
    def tearDownClass(cls):
        super(BaseK8sAuth, cls).tearDownClass()
