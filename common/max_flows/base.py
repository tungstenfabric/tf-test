from common.base import GenericTestBase
import os
import sys
import time
from compute_node_test import ComputeNodeFixture
from tcutils.traffic_utils.scapy_traffic_gen import ScapyTraffic
trafficdir = os.path.join(os.path.dirname(__file__), '../../tcutils/pkgs/Traffic')
sys.path.append(trafficdir)
from traffic.core.stream import Stream
from traffic.core.profile import StandardProfile
from traffic.core.helpers import Host, Sender, Receiver

DEFAULT_SRC_PORT = 1500
DEFAULT_DST_PORT_START = 10001

class BaseMaxFlowsTest(GenericTestBase):

    @classmethod
    def setUpClass(cls, flow_timeout=80):
        super(BaseMaxFlowsTest, cls).setUpClass()
        cls.orch = cls.connections.orch
        cls.computes = {}
        for ip in cls.inputs.compute_ips:
            cls.computes[ip] = ComputeNodeFixture(cls.connections, ip)

        try:
            cls.set_flow_timeout(flow_timeout)
        except:
            cls.cleanup_flow_timeout()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.cleanup_flow_timeout()
        super(BaseMaxFlowsTest, cls).tearDownClass()

    @classmethod
    def set_flow_timeout(cls, flow_timeout):
        for cmp_fix in cls.computes.values():
            cls.logger.info('setting flow timeout %d on %s' % (flow_timeout,
                            cmp_fix.ip))
            cmp_fix.set_flow_aging_time(flow_timeout)
        return True

    @classmethod
    def cleanup_flow_timeout(cls):
        for cmp_fix in cls.computes.values():
            flow_timeout = cmp_fix.default_values['DEFAULT']['flow_cache_timeout']
            cls.logger.info('reset flow timeout %d on %s' % (flow_timeout,
                            cmp_fix.ip))
            cmp_fix.set_flow_aging_time(flow_timeout)
        return True

    def cleanup_test_max_vm_flows_vrouter_config(self, compute_fixtures):
        for cmp_fix in compute_fixtures:
            self.logger.info('resetting max_vm_flows on %s' % cmp_fix.ip)
            cmp_fix.set_per_vm_flow_limit(100.0)
        return True

    def create_flows(self,
                     src_ip,
                     dst_ip,
                     flow_count,
                     vm_fix,
                     sport=DEFAULT_SRC_PORT,
                     dport_start=DEFAULT_DST_PORT_START):
        '''
        runs udp traffic (scapy) to effect specified flow entries
        '''

        if flow_count % 2:
            raise Exception('odd number of flows cannot be created')
        # one stream of traffic generate two flow entries, one for
        # each direction
        flow_count //= 2
        dport_end = dport_start + flow_count - 1
        dport_range = (dport_start, dport_end)

        # start scapy based script to run traffic
        params = {}
        params['ip'] = {'src': src_ip , 'dst': dst_ip}
        params['udp'] = {'sport': sport, 'dport': dport_range}
        params['count'] = 1
        params['interval'] = 0
        params['mode'] = 'L3'
        scapy_obj = ScapyTraffic(vm_fix, **params)
        scapy_obj.start()

        sleep_time = flow_count // 100
        sleep_time = 5 if sleep_time < 5 else sleep_time
        self.logger.info("Started Traffic...for %d secs..." % sleep_time)
        time.sleep(sleep_time)

        # scapy_obj.stop() not required, scapy creates traffic in the
        # specifid port range and quits
        return dport_range[1]-dport_range[0]+1

    def get_total_flow_count(self,
                             vrf_id,
                             metadata_ip,
                             vrouter_fixture,
                             source_ip=None,
                             dest_ip=None):
        '''
        returns the count of flows matching specified source & destination
        '''

        flow_table = vrouter_fixture.get_flow_table()

        if dest_ip == None:
            (ff_count, rf_count) = vrouter_fixture.get_flow_count(
                flow_table=flow_table,
                refresh=False,
                source_ip=source_ip,
                proto='udp',
                vrf_id=vrf_id
                )
        elif source_ip == None:
            (ff_count, rf_count) = vrouter_fixture.get_flow_count(
                flow_table=flow_table,
                refresh=False,
                dest_ip=dest_ip,
                proto='udp',
                vrf_id=vrf_id
                )
        else:
            (ff_count, rf_count) = vrouter_fixture.get_flow_count(
                flow_table=flow_table,
                refresh=False,
                source_ip=source_ip,
                dest_ip=dest_ip,
                proto='udp',
                vrf_id=vrf_id
                )
        self.logger.info("Flow Count Forward: %d  Reverse: %d" % (ff_count,
                            rf_count))

        # dns flow entries
        (ff_dns_count, rf_dns_count) = vrouter_fixture.get_flow_count(
                flow_table=flow_table,
                refresh=False,
                source_ip=source_ip or dest_ip,
                dest_port=53,
                proto='udp',
                vrf_id=vrf_id
            )
        self.logger.info("DNS Flow Count Forward: %d  Reverse: %d" % (
                            ff_dns_count, rf_dns_count))

        # metadata flow entries
        (ff_meta_ip, rf_meta_ip) = vrouter_fixture.get_flow_count(
                flow_table=flow_table,
                refresh=False,
                dest_ip=metadata_ip
            )
        self.logger.info("Meta Data Flow Count Forward: %d  Reverse: %d" % (
                            ff_meta_ip, rf_meta_ip))

        total_flow_count = ff_count + rf_count + ff_dns_count + rf_dns_count + ff_meta_ip + rf_meta_ip
        return total_flow_count

    def verify_max_flows_limit(self,
                               src,
                               dst,
                               flow_count,
                               verify_at,
                               expected_flow_count):
        src_compute = self.computes[src.vm_node_ip]
        dst_compute = self.computes[dst.vm_node_ip]

        if verify_at == 'src':
            verify_at_compute = src_compute
            vrf_id = src_compute.get_vrf_id(src.vn_fq_name)
            local_ip = src.get_local_ip()
            query_src_ip = src.vm_ip
            query_dst_ip = dst.vm_ip
        elif verify_at == 'dst':
            verify_at_compute = dst_compute
            vrf_id = dst_compute.get_vrf_id(dst.vn_fq_name)
            local_ip = dst.get_local_ip()
            query_src_ip = dst.vm_ip
            query_dst_ip = src.vm_ip

        # cache flow count prior to traffic generation
        prior_flow_count = self.get_total_flow_count(
                source_ip=query_src_ip,
                dest_ip=query_dst_ip,
                vrf_id=vrf_id,
                metadata_ip=local_ip,
                vrouter_fixture=verify_at_compute
                )
        traffic_count = self.create_flows(
                src_ip=src.vm_ip,
                dst_ip=dst.vm_ip,
                flow_count=flow_count,
                vm_fix=src
                )
        # flow count after traffic
        total_flow_count = self.get_total_flow_count(
                source_ip=query_src_ip,
                dest_ip=query_dst_ip,
                vrf_id=vrf_id,
                metadata_ip=local_ip,
                vrouter_fixture=verify_at_compute
                )
        self.logger.info('flow count: sent(%d) pre-exists(%d) seen(%d)' %(
                         traffic_count * 2, prior_flow_count, total_flow_count))

        # adjust total flows seen based on prior flow count
        # since its possible that the pre-existing flows timeout, before
        # create_flows completed
        diff = abs(total_flow_count - expected_flow_count)
        if diff and diff <= prior_flow_count:
            total_flow_count = expected_flow_count
        return total_flow_count

    def verify_vms_and_traffic(self,
                               vm_pairs,
                               sport=DEFAULT_SRC_PORT,
                               dport=DEFAULT_DST_PORT_START):
        '''
        wait for vms & verify udp traffic between them succeeds
        '''

        proto='udp'
        count=100
        for sender_vm, receiver_vm in vm_pairs:
            self.logger.info('verify vms %s, %s' % (sender_vm.name,
                            receiver_vm.name))
            assert sender_vm.wait_till_vm_is_up(refresh=True), \
                    'vm %s not up!' % sender_vm.name
            assert receiver_vm.wait_till_vm_is_up(refresh=True), \
                    'vm %s not up!' % receiver_vm.name

            self.logger.info('verify traffic between %s %s' % (sender_vm.name,
                            receiver_vm.name))
            stream = Stream(sport=sport, dport=dport, proto=proto,
                            src=sender_vm.vm_ip, dst=receiver_vm.vm_ip)
            profile_kwargs = {'stream': stream, 'count': count}
            profile = StandardProfile(**profile_kwargs)

            send_node = Host(sender_vm.vm_node_ip,
                    self.inputs.host_data[sender_vm.vm_node_ip]['username'],
                    self.inputs.host_data[sender_vm.vm_node_ip]['password'])
            recv_node = Host(receiver_vm.vm_node_ip,
                    self.inputs.host_data[receiver_vm.vm_node_ip]['username'],
                    self.inputs.host_data[receiver_vm.vm_node_ip]['password'])
            send_host = Host(sender_vm.local_ip,
                    sender_vm.vm_username, sender_vm.vm_password)
            recv_host = Host(receiver_vm.local_ip,
                    receiver_vm.vm_username, receiver_vm.vm_password)

            sender = Sender("send%s" % proto, profile, send_node, send_host,
                            self.inputs.logger)
            receiver = Receiver("recv%s" % proto, profile, recv_node, recv_host,
                            self.inputs.logger)

            # TODO: hack, to be removed when ubuntu-traffic-py3 image is updated
            # copy the fixed listener.py into the VM
            receiver.copy_file_to_vm(trafficdir + '/traffic/core/listener.py')
            receiver_vm.run_cmd_on_vm(['cp /tmp/listener.py /usr/lib/python3.6/traffic/core/'], as_sudo=True)

            receiver.start()
            sender.start()
            time.sleep(5)
            sender.stop()
            receiver.stop()
            self.logger.info('Results of traffic %s -> %s' % (sender_vm.name,
                            receiver_vm.name))
            self.logger.info("Sent: %s; Received: %s", sender.sent,
                             receiver.recv)
            assert sender.sent == receiver.recv, \
                    "Failed Traffic between VMs %s-%s" % (sender_vm.vm_name,
                        receiver_vm.vm_name)
