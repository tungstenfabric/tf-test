from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
import test
from tcutils.util import get_random_name, is_v6
import random
from common.neutron.lbaasv2.base import BaseLBaaSTest
from common.servicechain.config import ConfigSvcChain
from common.servicechain.verify import VerifySvcChain

AF_TEST = 'v6'

class FatFlowAggrSerial(BaseVrouterTest, BaseLBaaSTest):

    @classmethod
    def setUpClass(cls):
        super(FatFlowAggrSerial, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FatFlowAggrSerial, cls).tearDownClass()

    @test.attr(type=['dev_reg'])
    @preposttest_wrapper
    def test_fat_flow_aggr_dest_udp_inter_vn_inter_node(self):
        """:
        Description: Verify fat flow prefix aggr dest (IPv4) for intra-vn inter-node
        Steps:
            1. Create 2 VNs and launch 3 VMs.2 client VMs in VN1 on same node
               and server VM in VN2 on different node.
               Client 1 in subnet 1, Client 2 in the next subnet.
               Policy p1 configured to allow udp traffic between VN1 and VN2.
            2. On server VM, config fat flow aggr prefix dest len 29 for UDP port 55.
            3. From both the client VMs, send ICMP traffic to the server VM twice with diff. src ports
        Pass criteria:
            1. On the remote CN, expect 2 pairs ( 1 for client 1, 1 for client 2)
               of fat flows with prefix aggregated for the src IPs
               (VM to fabric, Prefix Aggr Dest: Aggregation happens for SRC IPs)
            2. On client VM compute nodes, expect 4 pairs of flows and on server compute,
               expect 2 pairs of flows
            3. On server compute node, flow's source port should be 0 for fat flows

        Maintainer: Ankitja@juniper.net

        """
        prefix_length = 29
        ipv6 = False
        only_v6 = False
        if self.inputs.get_af() == 'dual':
            ipv6 = True
            only_v6 = True
        prefix_length6 = 125
        inter_node = True
        inter_vn = True
        proto = 'udp'
        port = 55
        policy_deny = False
        vn_policy = True
        self.fat_flow_with_prefix_aggr(prefix_length=prefix_length,
            inter_node=inter_node,inter_vn=inter_vn, proto=proto,
            port=port, vn_policy=vn_policy, policy_deny=policy_deny,
            dual=ipv6, prefix_length6=prefix_length6, only_v6=only_v6)
        return True

class FatFlowAggrIpv6Serial(FatFlowAggrSerial):
    @classmethod
    def setUpClass(cls):
        super(FatFlowAggrSerial, cls).setUpClass()
        cls.inputs.set_af(AF_TEST)

    @test.attr(type=['sanity','dev_reg'])
    @preposttest_wrapper
    def test_fat_flow_aggr_dest_udp_inter_vn_inter_node(self):
        """
        Description: Verify fat flow prefix aggr dest (IPv6) for intra-vn inter-node
        Steps:
            1. Create 2 VNs with IPv6 subnets and launch 3 VMs.2 client VMs in VN1 on same node
               and server VM in VN2 on different node.
               Client 1 in subnet 1, Client 2 in the next subnet.
               Policy p1 configured to allow udp traffic between VN1 and VN2.
            2. On server VM, config fat flow aggr prefix dest IPv6 len 125 for UDP port 55.
            3. From both the client VMs, send ICMP6 traffic to the server VM twice with diff. src ports
        Pass criteria:
            1. On the remote CN, expect 2 pairs ( 1 for client 1, 1 for client 2)
               of IPv6 fat flows with prefix aggregated for the src IPs
               (VM to fabric, Prefix Aggr Dest: Aggregation happens for SRC IPs)
            2. On client VM compute nodes, expect 4 pairs of IPv6 flows and on server compute,
               expect 2 pairs of IPv6 flows
            3. On server compute node, flow's source port should be 0 for fat flows

        Maintainer: Ankitja@juniper.net

        """
        self.inputs.set_af('dual')
        super(FatFlowAggrIpv6Serial, self).test_fat_flow_aggr_dest_udp_inter_vn_inter_node()

