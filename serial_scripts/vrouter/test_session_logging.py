from common.sessionlogging.base import *
from tcutils.wrappers import preposttest_wrapper
import test
import random
from tcutils.util import skip_because

AF_TEST = 'v6'

class SessionLogging(SessionLoggingBase):

    @classmethod
    def setUpClass(cls):
        super(SessionLogging, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SessionLogging, cls).tearDownClass()

    def _test_logging_intra_node(self):

        self._create_resources(test_type='intra-node')

        #For intra node traffic there is no tunnel so underlay_proto would be zero
        underlay_proto = 0
        proto_list = [17 , 1, 6]
        self.enable_logging_on_compute(self.client_fixture.vm_node_ip,
            log_type=AGENT_LOG)
        #Clear local ips after agent restart
        self.client_fixture.clear_local_ips()
        self.server_fixture.clear_local_ips()
        #Verify Session logs in agent logs
        for proto in proto_list:
            self.start_traffic_validate_sessions(self.client_fixture,
                self.server_fixture, self.policy_fixture, proto=proto,
                underlay_proto=underlay_proto)
            self.logger.info("Expected Session logs found in agent log for "
                "protocol %s" % (proto))

        self.enable_logging_on_compute(self.client_fixture.vm_node_ip,
            log_type=SYS_LOG)
        #Clear local ips after agent restart
        self.client_fixture.clear_local_ips()
        self.server_fixture.clear_local_ips()
        #Verify Session logs in syslog
        for proto in proto_list:
            self.start_traffic_validate_sessions_in_syslog(self.client_fixture,
                self.server_fixture, self.policy_fixture, proto=proto,
                underlay_proto=underlay_proto)
            self.logger.info("Expected Session logs found in syslog for "
                "protocol %s" % (proto))

    def _test_logging_inter_node(self):

        self._create_resources(test_type='inter-node')

        underlay_proto = UNDERLAY_PROTO[
            self.connections.read_vrouter_config_encap()[0]]
        proto_list = [17, 1, 6]
        self.enable_logging_on_compute(self.client_fixture.vm_node_ip,
            log_type=AGENT_LOG)
        self.enable_logging_on_compute(self.server_fixture.vm_node_ip,
            log_type=AGENT_LOG)
        #Clear local ips after agent restart
        self.client_fixture.clear_local_ips()
        self.server_fixture.clear_local_ips()
        #Verify Session logs in agent logs
        for proto in proto_list:
            self.start_traffic_validate_sessions(self.client_fixture,
                self.server_fixture, self.policy_fixture, proto=proto,
                underlay_proto=underlay_proto)
            self.logger.info("Expected Session logs found in agent log for "
                "protocol %s" % (proto))

        self.enable_logging_on_compute(self.client_fixture.vm_node_ip,
            log_type=SYS_LOG)
        self.enable_logging_on_compute(self.server_fixture.vm_node_ip,
            log_type=SYS_LOG)
        #Clear local ips after agent restart
        self.client_fixture.clear_local_ips()
        self.server_fixture.clear_local_ips()
        #Verify Session logs in syslog
        for proto in proto_list:
            self.start_traffic_validate_sessions_in_syslog(self.client_fixture,
                self.server_fixture, self.policy_fixture, proto=proto,
                underlay_proto=underlay_proto)
            self.logger.info("Expected Session logs found in syslog for "
                "protocol %s" % (proto))

    @preposttest_wrapper
    def test_local_logging_intra_node(self):
        """
        Description: Verify sessions logged for inter-VN intra-Node traffic
        Steps:
            1. create 2 VNs and connect them using policy
            2. launch 1 VM in each VN on same compute node
            3. start icmp/tcp/udp traffic and verify the session logs in agent log
                as well as in syslog
        Pass criteria:
            step 3 should pass
        """
        self._test_logging_intra_node()

    @preposttest_wrapper
    def test_local_logging_inter_node(self):
        """
        Description: Verify sessions logged for inter-VN inter-Node traffic
        Steps:
            1. create 2 VNs and connect them using policy
            2. launch 1 VM in each VN on different compute nodes
            3. start icmp/tcp/udp traffic and verify the session logs in agent log
                as well as in syslog
        Pass criteria:
            step 3 should pass
        """
        self._test_logging_inter_node()

class SessionLoggingIpv6(SessionLogging):
    @classmethod
    def setUpClass(cls):
        super(SessionLoggingIpv6, cls).setUpClass()
        cls.inputs.set_af(AF_TEST)

    def is_test_applicable(self):
        if (self.inputs.orchestrator == 'vcenter') and (
            not self.orch.is_feature_supported('ipv6')):
            return(False, 'Skipping IPv6 Test on vcenter setup')
        return (True, None)
