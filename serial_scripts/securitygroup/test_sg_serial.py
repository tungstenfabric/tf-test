from common.securitygroup.base import BaseSGTest
import unittest
from tcutils.wrappers import preposttest_wrapper
from vnc_api.vnc_api import NoIdError
import os
import sys
from common.securitygroup.verify import VerifySecGroup
from common.policy.config import ConfigPolicy
from tcutils.topo.topo_helper import *
from tcutils.topo.sdn_topo_setup import *
import test
from common.securitygroup import sdn_sg_test_topo
from tcutils.util import skip_because, get_random_name
from tcutils.tcpdump_utils import *
from security_group import set_default_sg_rules

AF_TEST = 'v6'

class SecurityGroupRegressionTests9(BaseSGTest, VerifySecGroup, ConfigPolicy):

    @classmethod
    def setUpClass(cls):
        super(SecurityGroupRegressionTests9, cls).setUpClass()
        cls.option = 'openstack'

    def runTest(self):
        pass

    @preposttest_wrapper
    def test_add_remove_default_sg_active_flow(self):
        """ add/remove default SG from VM when flow is active and traffic from both ends"""

        topology_class_name = sdn_sg_test_topo.sdn_topo_flow_to_sg_rule_mapping
        topo_obj, config_topo = self.create_topo_setup(
            topology_class_name, "build_topo")

        port = 10000
        src_vm_name = 'vm1'
        dst_vm_name = 'vm2'
        src_vm_fix = config_topo['vm'][src_vm_name]
        dst_vm_fix = config_topo['vm'][dst_vm_name]
        src_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[src_vm_name]]
        dst_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[dst_vm_name]]
        src_vn_fq_name = ''
        dst_vn_fq_name = ''
        if self.option == 'openstack':
            src_vn_fq_name = src_vn_fix.vn_fq_name
            dst_vn_fq_name = dst_vn_fix.vn_fq_name
        else:
            src_vn_fq_name = ':'.join(src_vn_fix._obj.get_fq_name())
            dst_vn_fq_name = ':'.join(dst_vn_fix._obj.get_fq_name())

        sg_name = 'default'
        secgrp_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      sg_name]))

        filters1 = '\'(udp and src host %s and dst host %s)\'' % (
            src_vm_fix.vm_ip, dst_vm_fix.vm_ip)
        filters2 = '\'(tcp and src host %s and dst host %s)\'' % (
            dst_vm_fix.vm_ip, src_vm_fix.vm_ip)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting traffic udp and tcp on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'tcp')

        self.logger.info("Verify traffic udp and tcp on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove security group from source vm.")
        src_vm_fix.remove_security_group(secgrp=secgrp_id)
        sleep(5)

        self.logger.info("Starting tcpdump on src and dest vm after removing SG.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting traffic udp and tcp on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp', exp=False)
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'tcp', exp=False)

        self.logger.info("Verify traffic udp and tcp on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1, exp_count=0)
        assert verify_tcpdump_count(self, session2, pcap2, exp_count=0)

        self.logger.info("Add security group back to source vm.")
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        sleep(5)

        self.logger.info("Starting tcpdump on src and dest vm after adding SG.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting traffic on src and dest vm after adding SG.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        for loop in range(30):
            resp = self.send_nc_traffic(
                dst_vm_fix, src_vm_fix, port, port, 'tcp')
            if resp == True:
                break;
            sleep(5)

        self.logger.info("Verify traffic udp and tcp on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        return True
        # end test_add_remove_default_sg_active_flow

    @preposttest_wrapper
    def test_add_remove_sg_active_flow1(self):
        """ add/remove SG from VM when flow is active
        1.Traffic from both ends
        2.Test for SG with rule with remote as sg for both ingress-egress"""

        topology_class_name = sdn_sg_test_topo.sdn_topo_flow_to_sg_rule_mapping
        topo_obj, config_topo = self.create_topo_setup(
            topology_class_name, "build_topo")

        sg_allow_all = self.create_sec_group_allow_all()
        port = 10000
        src_vm_name = 'vm1'
        dst_vm_name = 'vm2'
        src_vm_fix = config_topo['vm'][src_vm_name]
        dst_vm_fix = config_topo['vm'][dst_vm_name]
        src_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[src_vm_name]]
        dst_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[dst_vm_name]]
        src_vn_fq_name = ''
        dst_vn_fq_name = ''
        if self.option == 'openstack':
            src_vn_fq_name = src_vn_fix.vn_fq_name
            dst_vn_fq_name = dst_vn_fix.vn_fq_name
        else:
            src_vn_fq_name = ':'.join(src_vn_fix._obj.get_fq_name())
            dst_vn_fq_name = ':'.join(dst_vn_fix._obj.get_fq_name())

        sg_name = topo_obj.sg_list[0]
        secgrp_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      sg_name]))

        default_sg_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      'default']))

        src_vm_fix.remove_security_group(secgrp=default_sg_id)
        dst_vm_fix.remove_security_group(secgrp=default_sg_id)
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        dst_vm_fix.add_security_group(secgrp=secgrp_id)
        # ingress-egress from same sg
        rule = [{'direction': '>',
                 'protocol': 'udp',
                 'dst_addresses': [{'security_group': topo_obj.domain + ':' + topo_obj.project + ':' + sg_name}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_addresses': [{'security_group': 'local'}],
                 },
                {'direction': '>',
                 'protocol': 'udp',
                 'src_addresses': [{'security_group': topo_obj.domain + ':' + topo_obj.project + ':' + sg_name}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_addresses': [{'security_group': 'local'}],
                 }]
        config_topo['sec_grp'][sg_name].replace_rules(rule)

        filters1 = '\'(udp and src host %s and dst host %s)\'' % (
            src_vm_fix.vm_ip, dst_vm_fix.vm_ip)
        filters2 = '\'(udp and src host %s and dst host %s)\'' % (
            dst_vm_fix.vm_ip, src_vm_fix.vm_ip)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove %s SG from source vm." % (sg_name))
        src_vm_fix.remove_security_group(secgrp=secgrp_id)
        self.logger.info("Add %s SG to source vm." % ('sg_allow_all'))
        src_vm_fix.add_security_group(secgrp=sg_allow_all)
        sleep(5)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp', exp=False)
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'udp', exp=False)

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1, exp_count=0)
        assert verify_tcpdump_count(self, session2, pcap2, exp_count=0)

        self.logger.info("Remove %s SG from source vm." % ('sg_allow_all'))
        src_vm_fix.remove_security_group(secgrp=sg_allow_all)

        return True
        # end test_add_remove_sg_active_flow1

    @preposttest_wrapper
    def test_add_remove_sg_active_flow2(self):
        """ add/remove SG from VM when flow is active
        1.Traffic from both ends
        2.Test for SG with egress cidr rule,ingress sg"""

        topology_class_name = sdn_sg_test_topo.sdn_topo_flow_to_sg_rule_mapping
        topo_obj, config_topo = self.create_topo_setup(
            topology_class_name, "build_topo")

        sg_allow_all = self.create_sec_group_allow_all()

        port = 10000
        port2 = 11000
        src_vm_name = 'vm1'
        dst_vm_name = 'vm2'
        src_vm_fix = config_topo['vm'][src_vm_name]
        dst_vm_fix = config_topo['vm'][dst_vm_name]
        src_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[src_vm_name]]
        dst_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[dst_vm_name]]
        src_vn_fq_name = ''
        dst_vn_fq_name = ''
        if self.option == 'openstack':
            src_vn_fq_name = src_vn_fix.vn_fq_name
            dst_vn_fq_name = dst_vn_fix.vn_fq_name
        else:
            src_vn_fq_name = ':'.join(src_vn_fix._obj.get_fq_name())
            dst_vn_fq_name = ':'.join(dst_vn_fix._obj.get_fq_name())

        sg_name = topo_obj.sg_list[0]
        secgrp_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      sg_name]))

        default_sg_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      'default']))

        src_vm_fix.remove_security_group(secgrp=default_sg_id)
        dst_vm_fix.remove_security_group(secgrp=default_sg_id)
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        dst_vm_fix.add_security_group(secgrp=secgrp_id)

        # ingress from same sg and egress to all
        rule = [{'direction': '>',
                 'protocol': 'udp',
                 'dst_addresses': [{'subnet': {'ip_prefix': '0.0.0.0', 'ip_prefix_len': 0}}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_addresses': [{'security_group': 'local'}],
                 },
                {'direction': '>',
                 'protocol': 'udp',
                 'src_addresses': [{'security_group': topo_obj.domain + ':' + topo_obj.project + ':' + sg_name}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_addresses': [{'security_group': 'local'}],
                 }]
        config_topo['sec_grp'][sg_name].replace_rules(rule)

        filters1 = '\'(udp and src host %s and dst host %s)\'' % (
            src_vm_fix.vm_ip, dst_vm_fix.vm_ip)
        filters2 = '\'(udp and src host %s and dst host %s)\'' % (
            dst_vm_fix.vm_ip, src_vm_fix.vm_ip)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port2, port2, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove %s SG from source vm." % (sg_name))
        src_vm_fix.remove_security_group(secgrp=secgrp_id)
        self.logger.info("Add %s SG to source vm." % ('sg_allow_all'))
        src_vm_fix.add_security_group(secgrp=sg_allow_all)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp', exp=False)
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port2, port2, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1, exp_count=0)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove %s SG from source vm." % ('sg_allow_all'))
        src_vm_fix.remove_security_group(secgrp=sg_allow_all)

        return True
        # end test_add_remove_sg_active_flow2

    @preposttest_wrapper
    def test_add_remove_sg_active_flow3(self):
        """ add/remove SG from VM when flow is active
        1. Traffic from both ends
        2. Test for SG with ingress cidr and egress sg"""

        topology_class_name = sdn_sg_test_topo.sdn_topo_flow_to_sg_rule_mapping
        topo_obj, config_topo = self.create_topo_setup(
            topology_class_name, "build_topo")

        sg_allow_all = self.create_sec_group_allow_all()

        port = 10000
        port2 = 11000
        src_vm_name = 'vm1'
        dst_vm_name = 'vm2'
        src_vm_fix = config_topo['vm'][src_vm_name]
        dst_vm_fix = config_topo['vm'][dst_vm_name]
        src_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[src_vm_name]]
        dst_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[dst_vm_name]]
        src_vn_fq_name = ''
        dst_vn_fq_name = ''
        if self.option == 'openstack':
            src_vn_fq_name = src_vn_fix.vn_fq_name
            dst_vn_fq_name = dst_vn_fix.vn_fq_name
        else:
            src_vn_fq_name = ':'.join(src_vn_fix._obj.get_fq_name())
            dst_vn_fq_name = ':'.join(dst_vn_fix._obj.get_fq_name())

        sg_name = topo_obj.sg_list[0]
        secgrp_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      sg_name]))

        default_sg_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      'default']))

        src_vm_fix.remove_security_group(secgrp=default_sg_id)
        dst_vm_fix.remove_security_group(secgrp=default_sg_id)
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        dst_vm_fix.add_security_group(secgrp=secgrp_id)

        # egress to same sg and ingress from all
        rule = [{'direction': '>',
                 'protocol': 'udp',
                 'dst_addresses': [{'security_group': topo_obj.domain + ':' + topo_obj.project + ':' + sg_name}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_addresses': [{'security_group': 'local'}],
                 },
                {'direction': '>',
                 'protocol': 'udp',
                 'src_addresses': [{'subnet': {'ip_prefix': '0.0.0.0', 'ip_prefix_len': 0}}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_addresses': [{'security_group': 'local'}],
                 }]
        config_topo['sec_grp'][sg_name].replace_rules(rule)

        filters1 = '\'(udp and src host %s and dst host %s)\'' % (
            src_vm_fix.vm_ip, dst_vm_fix.vm_ip)
        filters2 = '\'(udp and src host %s and dst host %s)\'' % (
            dst_vm_fix.vm_ip, src_vm_fix.vm_ip)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port2, port2, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove %s SG from source vm." % (sg_name))
        src_vm_fix.remove_security_group(secgrp=secgrp_id)
        self.logger.info("Add %s SG to source vm." % ('sg_allow_all'))
        src_vm_fix.add_security_group(secgrp=sg_allow_all)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port2, port2, 'udp', exp=False)

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2, exp_count=0)

        self.logger.info("Remove %s SG from source vm." % ('sg_allow_all'))
        src_vm_fix.remove_security_group(secgrp=sg_allow_all)

        return True
        # end test_add_remove_sg_active_flow3

    @preposttest_wrapper
    def test_add_remove_sg_active_flow4(self):
        """ add/remove SG from VM when flow is active
        1. Traffic from both ends
        2. Test for SG with cidr both ingress-egress"""

        topology_class_name = sdn_sg_test_topo.sdn_topo_flow_to_sg_rule_mapping
        topo_obj, config_topo = self.create_topo_setup(
            topology_class_name, "build_topo")

        port = 10000
        src_vm_name = 'vm1'
        dst_vm_name = 'vm2'
        src_vm_fix = config_topo['vm'][src_vm_name]
        dst_vm_fix = config_topo['vm'][dst_vm_name]
        src_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[src_vm_name]]
        dst_vn_fix = config_topo['vn'][topo_obj.vn_of_vm[dst_vm_name]]
        src_vn_fq_name = ''
        dst_vn_fq_name = ''
        if self.option == 'openstack':
            src_vn_fq_name = src_vn_fix.vn_fq_name
            dst_vn_fq_name = dst_vn_fix.vn_fq_name
        else:
            src_vn_fq_name = ':'.join(src_vn_fix._obj.get_fq_name())
            dst_vn_fq_name = ':'.join(dst_vn_fix._obj.get_fq_name())

        sg_name = topo_obj.sg_list[0]
        secgrp_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      sg_name]))

        default_sg_id = get_secgrp_id_from_name(
            self.connections,
            ':'.join([self.connections.domain_name,
                      self.inputs.project_name,
                      'default']))

        src_vm_fix.remove_security_group(secgrp=default_sg_id)
        dst_vm_fix.remove_security_group(secgrp=default_sg_id)
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        dst_vm_fix.add_security_group(secgrp=secgrp_id)

        # ingress-egress from all
        rule = [{'direction': '>',
                 'protocol': 'udp',
                 'dst_addresses': [{'subnet': {'ip_prefix': '0.0.0.0', 'ip_prefix_len': 0}}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'src_addresses': [{'security_group': 'local'}],
                 },
                {'direction': '>',
                 'protocol': 'udp',
                 'src_addresses': [{'subnet': {'ip_prefix': '0.0.0.0', 'ip_prefix_len': 0}}],
                 'src_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_ports': [{'start_port': 0, 'end_port': -1}],
                 'dst_addresses': [{'security_group': 'local'}],
                 }]
        config_topo['sec_grp'][sg_name].replace_rules(rule)

        filters1 = '\'(udp and src host %s and dst host %s)\'' % (
            src_vm_fix.vm_ip, dst_vm_fix.vm_ip)
        filters2 = '\'(udp and src host %s and dst host %s)\'' % (
            dst_vm_fix.vm_ip, src_vm_fix.vm_ip)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        self.logger.info("Remove %s SG from source vm." % (sg_name))
        src_vm_fix.remove_security_group(secgrp=secgrp_id)
        self.logger.info("Add %s SG to source vm." % (sg_name))
        src_vm_fix.add_security_group(secgrp=secgrp_id)
        sleep(5)

        self.logger.info("Starting tcpdump on src and dest vm.")
        # start tcpdump on dst VM
        session1, pcap1 = start_tcpdump_for_vm_intf(self,
                                    dst_vm_fix, dst_vn_fq_name,
                                    filters = filters1)
        # start tcpdump on src VM
        session2, pcap2 = start_tcpdump_for_vm_intf(self,
                                    src_vm_fix, src_vn_fq_name,
                                    filters = filters2)

        self.logger.info("Starting udp traffic on src and dest vm.")
        assert self.send_nc_traffic(
            src_vm_fix, dst_vm_fix, port, port, 'udp')
        assert self.send_nc_traffic(
            dst_vm_fix, src_vm_fix, port, port, 'udp')

        self.logger.info("Verify udp traffic on src and dest vm.")
        assert verify_tcpdump_count(self, session1, pcap1)
        assert verify_tcpdump_count(self, session2, pcap2)

        return True
        # end test_add_remove_sg_active_flow4

# end class SecurityGroupRegressionTests9

class SecurityGroupRegressionTests9_contrail(SecurityGroupRegressionTests9):

    @classmethod
    def setUpClass(cls):
        super(SecurityGroupRegressionTests9, cls).setUpClass()
        cls.option = 'contrail'
#end class SecurityGroupRegressionTests9_contrail

class SecurityGroupMultiProject(BaseSGTest, VerifySecGroup, ConfigPolicy):

    @classmethod
    def setUpClass(cls):
        super(SecurityGroupMultiProject, cls).setUpClass()
        cls.option = 'openstack'

    def runTest(self):
        pass

    @preposttest_wrapper
    @skip_because(feature='multi-tenant')
    def test_sg_multiproject(self):
        """
        Description: Test SG across projects
        Steps:
            1. define the topology for the test
            2. create the resources as defined in the topo
            3. verify the traffic
        Pass criteria: step 3 should pass
        """

        topology_class_name = None
        user = 'user' + get_random_name()
        result = True
        msg = []
        if not topology_class_name:
            topology_class_name = sdn_sg_test_topo.sdn_topo_config_multiproject

        self.logger.info("Scenario for the test used is: %s" %
                         (topology_class_name))

        topo = topology_class_name(username=user, password=user)
        self.topo = topo

        #
        # Test setup: Configure policy, VN, & VM
        # return {'result':result, 'msg': err_msg, 'data': [self.topo, config_topo]}
        # Returned topo is of following format:
        # config_topo= {'policy': policy_fixt, 'vn': vn_fixture, 'vm': vm_fixture}
        topo_objs = {}
        config_topo = {}
        setup_obj = self.useFixture(
            sdnTopoSetupFixture(self.connections, topo))
        out = setup_obj.sdn_topo_setup(config_option=self.option)
        self.assertEqual(out['result'], True, out['msg'])
        if out['result']:
            topo_objs, config_topo, vm_fip_info = out['data']

        self.start_traffic_and_verify_multiproject(
            topo_objs,
            config_topo,
            traffic_reverse=False)

        return True
    # end test_sg_multiproject

class SecurityGroupMultiProject_contrail(SecurityGroupMultiProject):

    @classmethod
    def setUpClass(cls):
        super(SecurityGroupMultiProject_contrail, cls).setUpClass()
        cls.option = 'contrail'

class SecurityGroupMultiProjectIpv6(SecurityGroupMultiProject):

    @classmethod
    def setUpClass(cls):
        super(SecurityGroupMultiProjectIpv6, cls).setUpClass()
        cls.inputs.set_af(AF_TEST)

    def is_test_applicable(self):
        if self.inputs.orchestrator == 'vcenter' and not self.orch.is_feature_supported(
                'ipv6'):
            return(False, 'Skipping IPv6 Test on vcenter setup')
        return (True, None)
