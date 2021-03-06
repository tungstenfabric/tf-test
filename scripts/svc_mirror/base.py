import test_v1
from common.connections import ContrailConnections
from common import isolated_creds

class BaseMirrorTest(test_v1.BaseTestCase_v1):

    @classmethod
    def setUpClass(cls):
        super(BaseMirrorTest, cls).setUpClass()
        cls.quantum_h= cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.orch = cls.connections.orch
        cls.vnc_lib= cls.connections.vnc_lib
        cls.agent_inspect= cls.connections.agent_inspect
        cls.cn_inspect= cls.connections.cn_inspect
        cls.analytics_obj=cls.connections.analytics_obj
    #end setUpClass

    @classmethod
    def tearDownClass(cls):
        super(BaseMirrorTest, cls).tearDownClass()
    #end tearDownClass

    def remove_from_cleanups(self, fix):
        for cleanup in self._cleanups:
            if fix in cleanup:
                self._cleanups.remove(cleanup)
                break
    #end remove_from_cleanups
