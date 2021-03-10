import test_v1
from common.connections import ContrailConnections
from common import isolated_creds
from common.base import GenericTestBase

class BaseIntfMirrorTest(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(BaseIntfMirrorTest, cls).setUpClass()
        cls.orch = cls.connections.orch
        cls.quantum_h= cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.vnc_lib= cls.connections.vnc_lib
        cls.agent_inspect= cls.connections.agent_inspect
        cls.cn_inspect= cls.connections.cn_inspect
        cls.analytics_obj=cls.connections.analytics_obj
    #end setUpClass

    @classmethod
    def tearDownClass(cls):
        super(BaseIntfMirrorTest, cls).tearDownClass()
    #end tearDownClass