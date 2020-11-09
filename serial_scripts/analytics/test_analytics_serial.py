from analytics import base
from builtins import str
from builtins import range
import os
import time
import fixtures
import testtools
import re
from common.base import GenericTestBase
from vn_test import *
from vm_test import *
from policy_test import *
from alarm_test import *
from multiple_vn_vm_test import *
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import skip_because, get_random_name
from fabric.api import run, local
import fixtures
import test
from tcutils.verification_util import VerificationUtilBase, XmlDrv

class AnalyticsTestHA(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(AnalyticsTestHA, cls).setUpClass()
        cls.triggered_vn = cls.untriggered_vn = None
        cls.alarm_fix = cls.policy_fix = None
        try:
            cls.saved_func = cls.connections.analytics_obj.has_opserver
            cls.connections.analytics_obj.has_opserver = lambda : False
            cls.triggered_vn = cls.create_only_vn()
            cls.untriggered_vn = cls.create_only_vn()           
            alarm_rule = [{'operation': '>=',
                    'operand1': "UveVirtualNetworkConfig.total_acl_rules",
                    'operand2': {'json_value': '1'}}]
            cls.alarm_fix = AlarmFixture(connections=cls.connections,
                                alarm_name=get_random_name('vn_acl_rule'),
                                uve_keys=['virtual-network'])
            cls.alarm_fix.setUp()
            cls.alarm_fix.create(cls.alarm_fix.configure_alarm_rules(alarm_rule))
            policy = [{
                'direction': '<>', 'simple_action': 'pass',
                'protocol': 'any', 'src_ports': 'any',
                'dst_ports': 'any',
                'source_network': 'any',
                'dest_network': 'any',}]
            cls.policy_fix = PolicyFixture(get_random_name('alarm'), policy,
                                cls.inputs, cls.connections)
            cls.policy_fix.setUp()
            assert cls.triggered_vn.verify_on_setup(), "VN not created"
            assert cls.untriggered_vn.verify_on_setup(), "VN not created"
            assert cls.alarm_fix.verify_on_setup(), "alarm not created"
            assert cls.policy_fix.verify_on_setup(), "policy not created"
        except:
            cls.tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.connections.analytics_obj.has_opserver = cls.saved_func
        if cls.alarm_fix:
            cls.alarm_fix.cleanUp()
        if cls.policy_fix:
            cls.policy_fix.cleanUp()
        if cls.triggered_vn:
            cls.triggered_vn.cleanUp()
        if cls.untriggered_vn:
            cls.untriggered_vn.cleanUp()
        super(AnalyticsTestHA, cls).tearDownClass()

    def is_test_applicable(self):
        if self.inputs.alarmgen_nrs < 3:
            return (False, 'min 3 instances of alarmgen required')
        if len(self.inputs.collector_ips) < 3:
            return (False, 'min 3 analytics nodes required')
        return True, None

    def verify_existing_and_new_object_uve(self, skip_list):
        # 1. verify UVEs for pre-created VN
        msg = 'pre-created VN link not found'
        assert self.connections.analytics_obj.get_vn_uve(
            self.triggered_vn.vn_fq_name, skip_opservers=skip_list), msg
        # 2. verify UVEs for newly created VN
        msg = 'newly created VN link not found'
        vn_fix = self.create_vn()
        assert self.connections.analytics_obj.get_vn_uve(
            vn_fix.vn_fq_name, skip_opservers=skip_list), msg

    def verify_systemdef_alarms(self, skip_list):
        ip = self.inputs.compute_ips[0]
        self.inputs.stop_container([ip], 'agent')
        self.addCleanup(self.inputs.start_container, [ip], 'agent')
        assert self.analytics_obj._verify_alarms_by_type('vrouter', ip,
            role='vrouter', alarm_type='process-status',
            skip_nodes=skip_list), 'system-defined alarm not raised'
        self.inputs.start_container([ip], 'agent')
        assert self.analytics_obj._verify_alarms_by_type('vrouter', ip,
            role='vrouter', alarm_type='process-status', skip_nodes=skip_list,
            verify_alarm_cleared=True), 'system-defined alarm not cleared'

    def verify_alarm_trigger(self, skip_list):
        self.untriggered_vn.bind_policies([self.policy_fix.policy_fq_name])
        sleep(10)
        assert self.analytics_obj.verify_configured_alarm(
            alarm_type=self.alarm_fix.alarm_fq_name,
            alarm_name=self.untriggered_vn.vn_fq_name,
            skip_nodes=skip_list), 'Alarm not raised'
        self.untriggered_vn.unbind_policies(self.untriggered_vn.vn_id,
            [self.policy_fix.policy_fq_name])
        assert self.analytics_obj.verify_configured_alarm(
            alarm_type=self.alarm_fix.alarm_fq_name,
            alarm_name=self.untriggered_vn.vn_fq_name,
            verify_alarm_cleared=True,
            skip_nodes=skip_list), 'Alarm not cleared'

    def verify_alarm_partitions(self, skip_list, count=30):
        partitions = 0
        skip_list = skip_list or []
        for ip in self.inputs.collector_ips:
            if ip in skip_list:
                continue
            info = VerificationUtilBase(ip, 5995,
                    XmlDrv).dict_get('Snh_SandeshUVECacheReq?x=AlarmgenPartition')
            sz = info.xpath('AlarmgenPartitionUVE/data/AlarmgenPartition/' +
                    'inst_parts/list/AlarmgenPartionInfo/partitions/list')[0].get('size')
            self.logger.info('partitions on ' + ip + ':' + sz)
            partitions += int(sz)
        assert count == partitions, 'Partition count mismatch'

    def verify_query_fns(self, skip_list):
        for ip in self.inputs.collector_ips:
            if ip not in skip_list:
                break
        assert self.connections.ops_inspects[ip].post_query('ObjectXmppPeerInfo',
            'now-30m', 'now', limit=5, select_fields=['Source', 'MessageTS'])

    def verify_uves_and_alarms(self, skip_list):
        # 1. verify fetching UVE works
        self.verify_existing_and_new_object_uve(skip_list)
        # 2. verify triggering & clearing alarms
        self.verify_alarm_trigger(skip_list)
        # 3. verify pre-triggered alarm is still present
        assert self.analytics_obj.verify_configured_alarm(
            alarm_type=self.alarm_fix.alarm_fq_name,
            alarm_name=self.triggered_vn.vn_fq_name,
            skip_nodes=skip_list), 'pretriggered Alarm not found'
        # 4. verify system-defined alarms
        self.verify_systemdef_alarms(skip_list)
        # 5. verify query api
        self.verify_query_fns(skip_list)

    def verify_service_failover(self, svc, multiple_instance=True):
        self.triggered_vn.bind_policies([self.policy_fix.policy_fq_name])
        self.addCleanup(self.triggered_vn.unbind_policies,
                    self.triggered_vn.vn_id, [self.policy_fix.policy_fq_name])
        self.addCleanup(self.untriggered_vn.unbind_policies,
                    self.untriggered_vn.vn_id, [self.policy_fix.policy_fq_name])
        try:
            nodes = self.inputs.collector_ips[:]
            for node in nodes:
                self.inputs.stop_container([node], svc)
                self.verify_uves_and_alarms([node])
                self.verify_alarm_partitions([node] if svc=='alarmgen' else None)
                self.inputs.start_container([node], svc, verify_service=False)
                time.sleep(10)
            if multiple_instance:
                node_pairs = [nodes[:i] + nodes[i+1:] for i in range(len(nodes))]
                for pairs in node_pairs:
                    self.inputs.stop_container(pairs, svc)
                    self.verify_uves_and_alarms(pairs)
                    self.verify_alarm_partitions(pairs if svc=='alarmgen' else None)
                    self.inputs.start_container(pairs, svc, verify_service=False)
                    time.sleep(10)
        finally:
            self.inputs.start_container(self.inputs.collector_ips, svc, verify_service=False)
        return True

    @preposttest_wrapper
    @skip_because(ssl_enabled=False)
    def test_stunnel_failover(self):
        return self.verify_service_failover('stunnel')

    @preposttest_wrapper
    def test_redis_failover(self):
        return self.verify_service_failover('redis')

    @preposttest_wrapper
    def test_analytics_api_failover(self):
        return self.verify_service_failover('analytics-api')

    @preposttest_wrapper
    def test_collector_failover(self):
        return self.verify_service_failover('collector')

    @preposttest_wrapper
    def test_alarmgen_failover(self):
        return self.verify_service_failover('alarmgen')

    @preposttest_wrapper
    def test_qe_failover(self):
        return self.verify_service_failover('query-engine')

    @preposttest_wrapper
    def test_zookeeper_failover(self):
        return self.verify_service_failover('config-zookeeper', multiple_instance=False)

    @preposttest_wrapper
    def test_cassandra_failover(self):
        return self.verify_service_failover('analytics-cassandra', multiple_instance=False)

class AnalyticsTestSanity(base.AnalyticsBaseTest):

    @classmethod
    def setUpClass(cls):
        super(AnalyticsTestSanity, cls).setUpClass()

    def runTest(self):
        pass
    # end runTest

    @preposttest_wrapper
    def test_verify_bgp_peer_object_logs(self):
        ''' Test to validate bgp_peer_object logs

        '''
        if (len(self.inputs.bgp_ips) < 2):
            self.logger.info("bgp ips less than 2...skipping the test...")
            return True
        result = True
        try:
            start_time = self.analytics_obj.getstarttime(
                self.inputs.bgp_ips[0])
            start_time1 = self.analytics_obj.getstarttime(
                self.inputs.compute_ips[0])
            object_id = 'default-domain:default-project:ip-fabric:__default__:' +\
                self.inputs.bgp_names[1] +\
                ':default-domain:default-project:ip-fabric:__default__:'\
                + self.inputs.bgp_names[0]
            object_id1 = self.inputs.bgp_control_ips[0]
            query = '(' + 'ObjectId=' + "".join(object_id.split()) + ')'
            query1 = '(' + 'ObjectId=' + object_id1 + \
                ' AND Source=' + self.inputs.compute_names[0] +\
                ' AND ModuleId=contrail-vrouter-agent)'
#            query1='('+'ObjectId='+ object_id1 +')'
            self.logger.info(
                "Stopping the control node in %s" %
                (self.inputs.bgp_ips[0]))
            self.inputs.stop_service(
                'contrail-control', [self.inputs.bgp_ips[0]],
                container='control')
            self.logger.info(
                "Waiting for the logs to be updated in database..")
            time.sleep(20)
            self.logger.info("Verifying ObjectBgpPeer \
                        Table through opserver %s.." % (self.inputs.collector_ips[0]))
            self.res1 = self.analytics_obj.ops_inspect[
                self.inputs.collector_ips[0]].post_query(
                'ObjectBgpPeer',
                start_time=start_time,
                end_time='now',
                select_fields=[
                    'ObjectId',
                    'Source',
                    'ObjectLog',
                    'SystemLog',
                    'Messagetype',
                    'ModuleId',
                    'MessageTS'],
                where_clause=query)
            #object xmpp_connection module got removed
            if self.res1:
                self.logger.info("Verifying logs from ObjectBgpPeer table")
                result1 = False
                result2 = False
                for elem in self.res1:
                    if re.search(
                        'EvConnectTimerExpired', str(
                            elem['ObjectLog'])):
                        self.logger.info("EvConnectTimerExpired log sent")
                        result1 = True
                    if re.search('EvTcpConnectFail', str(elem['ObjectLog'])):
                        self.logger.info("EvTcpConnectFail log sent")
                        result2 = True
                if not result1:
                    self.logger.warn("EvConnectTimerExpired log NOT sent")
                if not result2:
                    self.logger.warn("EvTcpConnectFail log NOT sent")

            start_time = self.analytics_obj.getstarttime(
                self.inputs.bgp_ips[0])
            start_time1 = self.analytics_obj.getstarttime(
                self.inputs.compute_ips[0])
            time.sleep(2)
            self.inputs.start_service(
                'contrail-control', [self.inputs.bgp_ips[0]],
                container='control')
            self.logger.info(
                "Waiting for the logs to be updated in database..")
            time.sleep(30)
            self.logger.info("Verifying ObjectBgpPeer \
                            Table through opserver %s.." % (self.inputs.collector_ips[0]))
            self.res1 = self.analytics_obj.ops_inspect[
                self.inputs.collector_ips[0]].post_query(
                'ObjectBgpPeer',
                start_time=start_time,
                end_time='now',
                select_fields=[
                    'ObjectId',
                    'Source',
                    'ObjectLog',
                    'SystemLog',
                    'Messagetype',
                    'ModuleId',
                    'MessageTS'],
                where_clause=query)

#            self.logger.info("query output : %s"%(self.res1))
            if not self.res1:
                self.logger.info("query output : %s" % (self.res1))
                st = self.analytics_obj.ops_inspect[
                    self.inputs.collector_ips[0]]. send_trace_to_database(
                    node=self.inputs.collector_names[0],
                    module='QueryEngine',
                    trace_buffer_name='QeTraceBuf')
                self.logger.info("status: %s" % (st))
                result = result and False
            if self.res1:
                self.logger.info("Verifying logs from ObjectBgpPeer table")
                result3 = False
                result4 = False
                result5 = False
                for elem in self.res1:
                    if re.search('EvTcpPassiveOpen', str(elem['ObjectLog'])):
                        self.logger.info("EvTcpPassiveOpen log sent")
                        result3 = True
                    if re.search('OpenConfirm', str(elem['ObjectLog'])):
                        self.logger.info("OpenConfirm log sent")
                        result4 = True
                    if re.search('Established', str(elem['ObjectLog'])):
                        self.logger.info("Established log sent")
                        result5 = True
                if not result3:
                    self.logger.warn("EvTcpPassiveOpen log NOT sent")
                if not result4:
                    self.logger.warn("OpenConfirm log NOT sent")
                if not result5:
                    self.logger.warn("Established log NOT sent")

        except Exception as e:
            self.logger.exception("%s" % str(e))
            result = result and False
        finally:
            self.inputs.start_service(
                'contrail-control', [self.inputs.bgp_ips[0]],
                container='control')
            time.sleep(4)
            result = result and result1 and result2 and result3 and result4\
                and result5
            assert result
            return True

    @preposttest_wrapper
    def test_verify_xmpp_peer_object_logs(self):
        ''' Test to validate xmpp peer object logs
        '''
        result = True
        try:
            start_time = self.analytics_obj.getstarttime(
                self.inputs.compute_ips[0])
            object_id = self.inputs.bgp_names[
                0] + ':' + self.inputs.compute_control_ips[0]
            query = '(' + 'ObjectId=' + object_id + ')'
            self.logger.info(
                "Stopping the xmpp node in %s" %
                (self.inputs.compute_ips[0]))
            self.inputs.stop_service(
                'contrail-vrouter-agent', [self.inputs.compute_ips[0]],
                container='agent')
            self.logger.info(
                "Waiting for the logs to be updated in database..")
            time.sleep(20)
            self.logger.info("Verifying ObjectXmppPeerInfo \
                        Table through opserver %s.." % (self.inputs.collector_ips[0]))
            self.res1 = self.analytics_obj.ops_inspect[
                self.inputs.collector_ips[0]].post_query(
                'ObjectXmppPeerInfo',
                start_time=start_time,
                end_time='now',
                select_fields=[
                    'ObjectId',
                    'Source',
                    'ObjectLog',
                    'SystemLog',
                    'Messagetype',
                    'ModuleId',
                    'MessageTS'],
                where_clause=query)
            if not self.res1:
                self.logger.info("Verifying ObjectXmppPeerInfo failed")
                result = result and False
            start_time = self.analytics_obj.getstarttime(
                self.inputs.compute_ips[0])
            time.sleep(2)
            self.inputs.start_service(
                'contrail-vrouter-agent', [self.inputs.compute_ips[0]],
                container='agent')
            self.logger.info(
                "Waiting for the logs to be updated in database..")
            time.sleep(30)
            self.logger.info("Verifying ObjectXmppPeerInfo \
                        Table through opserver %s.." % (self.inputs.collector_ips[0]))
            self.res1 = self.analytics_obj.ops_inspect[
                self.inputs.collector_ips[0]].post_query(
                'ObjectXmppPeerInfo',
                start_time=start_time,
                end_time='now',
                select_fields=[
                    'ObjectId',
                    'Source',
                    'ObjectLog',
                    'SystemLog',
                    'Messagetype',
                    'ModuleId',
                    'MessageTS'],
                where_clause=query)
#            self.logger.info("query output : %s"%(self.res1))
            if not self.res1:
                self.logger.info("Verifying ObjectXmppPeerInfo after restart failed")
                result = result and False

        except Exception as e:
            self.logger.exception("%s" % str(e))
            result = result and False
        finally:
            #            start_time=self.analytics_obj.getstarttime(self.inputs.compute_ips[0])
            self.inputs.start_service(
                'contrail-vrouter-agent', [self.inputs.compute_ips[0]],
                container='agent')
            time.sleep(20)
            self.logger.info(
                "Verifying ObjectVRouter Table through opserver %s.." %
                (self.inputs.collector_ips[0]))
            object_id = self.inputs.compute_names[0]
            query = '(' + 'ObjectId=' + object_id + ')'
            self.res1 = self.analytics_obj.ops_inspect[
                self.inputs.collector_ips[0]].post_query(
                'ObjectVRouter',
                start_time=start_time,
                end_time='now',
                select_fields=[
                    'ObjectId',
                    'Source',
                    'ObjectLog',
                    'SystemLog',
                    'Messagetype',
                    'ModuleId',
                    'MessageTS'],
                where_clause=query)
            if (self.res1):
                self.logger.info("ObjectVRouter table query passed")
                result = result and True
            else:
                self.logger.warn("ObjectVRouter table query failed")
                result = result and False

            assert result
            return True
