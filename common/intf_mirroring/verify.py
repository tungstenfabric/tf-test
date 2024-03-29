import os
import re
from time import sleep
from tcutils.util import get_random_cidr
from tcutils.util import get_random_name
from tcutils.util import retry
from tcutils.util import get_af_type
from tcutils.commands import ssh, execute_cmd, execute_cmd_out
from tcutils.tcpdump_utils import *
from common.servicechain.mirror.verify import VerifySvcMirror
from random import randint
from vnc_api.gen.resource_xsd import StaticMirrorNhType
from vnc_api.gen.resource_xsd import MirrorActionType
from vnc_api.gen.resource_xsd import InterfaceMirrorType
from vnc_api.gen.resource_xsd import VirtualMachineInterfacePropertiesType
from tcutils.contrail_status_check import ContrailStatusChecker
from lxml import etree

class VerifyIntfMirror(VerifySvcMirror):


    def get_compute_nodes(self, src, dst, analyzer):
        host_list = []
        compute_nodes = []

        for host in self.inputs.compute_ips:
            if self.inputs.domainsuffix == 'englab.juniper.net' or self.inputs.domainsuffix == 'local': 
                host_list.append(self.inputs.host_data[host]['name'])
            else:
                host_list.append(self.inputs.host_data[host]['fqname'])

        no_of_computes = len(host_list)

        for compute_id in [src, dst, analyzer]:
            if compute_id == 0:
                compute_nodes.append(host_list[0])

            if compute_id == 1:
                if no_of_computes > 1:
                    compute_nodes.append(host_list[1])
                else:
                    compute_nodes.append(host_list[0])

            if compute_id == 2:
                if no_of_computes > 2:
                    compute_nodes.append(host_list[2])
                elif no_of_computes == 2:
                    compute_nodes.append(host_list[1])
                else:
                    compute_nodes.append(host_list[0])

        self.logger.info("src compute %s -> dst compute %s => analyzer compute %s" %
            (compute_nodes[0], compute_nodes[1], compute_nodes[2]))
        return compute_nodes


    def verify_intf_mirroring_disable_enable_scenarios(self):
        """Validate the interface mirroring
        Verify sub/parent interface mirroring various enable/disable combinations
        """
        return self.verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn3_vn3(sub_intf=True, parent_intf=True)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn1_analyzer_on_cn3_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, all in same VN
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf, ipv6=ipv6)

    # common testcase to verify juniper header
    def verify_juniper_header_testcase(self, sub_intf=False, parent_intf=False, nic_mirror=False, header = 1, nh_mode = 'dynamic', direction = 'both', ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, all in different VNs, verify header details
        """
        # When both sub_intf and parent_intf vars are set, verify disable/enable scenarios
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, parent_intf, nic_mirror, header = header, nh_mode=nh_mode, direction = direction, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn3_vn3(self, sub_intf=False, parent_intf=False, nic_mirror=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, all in different VNs
        """
        # When both sub_intf and parent_intf vars are set, verify disable/enable scenarios
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, parent_intf, nic_mirror, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn1_analyzer_on_cn3_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, src and dst in vn1, analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn3_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, src and analyzer in vn1, dst in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn3_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on different CNs, src in vn1, dst and analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 2)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 1], sub_intf, ipv6=ipv6)


    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn1_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on same CN, all in same VN
        """

        compute_nodes = self.get_compute_nodes(0, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn3(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on same CN, all in different VNs
        """

        compute_nodes = self.get_compute_nodes(0, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn1_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on same CN, src and dst in vn1, analyzer in vn2
        """

        compute_nodes = self.get_compute_nodes(0, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on same CN, src and analyzer in vn1, dst in vn2
        """

        compute_nodes = self.get_compute_nodes(0, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm and analyzer vm on same CN, src in vn1, dst and analyzer in vn2
        """

        compute_nodes = self.get_compute_nodes(0, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 1], sub_intf, ipv6=ipv6)


    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn1_analyzer_on_cn2_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm on same CN and analyzer vm on different CN, all in same VN
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn2_vn3(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm on same CN and analyzer vm on different CN, all in different VNs
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn1_analyzer_on_cn2_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm on same CN and analyzer vm on different CN, src and dst in vn1, analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn2_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm on same CN and analyzer vm on different CN, src and analyzer in vn1, dst in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn1_vn2_analyzer_on_cn2_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, dst vm on same CN and analyzer vm on different CN, src in vn1, dst and analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 1], sub_intf, ipv6=ipv6)


    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn1_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, analyzer vm on same CN and dst vm on different CN, all in same VN
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn1_vn3(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, analyzer vm on same CN and dst vm on different CN, all in different VNs
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn1_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, analyzer vm on same CN and dst vm on different CN, src and dst in vn1, analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, analyzer vm on same CN and dst vm on different CN, src and analyzer in vn1, dst in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_dst_on_cn2_vn2_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        src vm, analyzer vm on same CN and dst vm on different CN, src in vn1, dst and analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 1, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn2_vn1_dst_on_cn1_vn1_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        dst vm, analyzer vm on same CN and src vm on different CN, all in same VN
        """
        compute_nodes  = self.get_compute_nodes(1, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn2_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn3(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        dst vm, analyzer vm on same CN and src vm on different CN, all in different VNs
        """
        compute_nodes  = self.get_compute_nodes(1, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 2], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn2_vn1_dst_on_cn1_vn1_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        dst vm, analyzer vm on same CN and src vm on different CN, src and dst in vn1, analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(1, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 0, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn2_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn1(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        dst vm, analyzer vm on same CN and src vm on different CN, src and analyzer in vn1, dst in vn2
        """
        compute_nodes  = self.get_compute_nodes(1, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 0], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn2_vn1_dst_on_cn1_vn2_analyzer_on_cn1_vn2(self, sub_intf=False, ipv6=False):
        """Validate the interface mirroring
        dst vm, analyzer vm on same CN and src vm on different CN, src in vn1, dst and analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(1, 0, 0)
        return self.verify_intf_mirroring(compute_nodes, [0, 1, 1], sub_intf, ipv6=ipv6)

    def verify_intf_mirroring_src_on_cn1_vn1_analyzer_on_cn2_vn2(self):
        """Validate no duplicate mirrored traffic and NH ID is seen on analyser tap
           when using dynamic NH without Juniper Header -- CEM 8760 fix verification.
           analyzer vm and src vm on different CN, src in vn1 and analyzer in vn2
        """
        compute_nodes  = self.get_compute_nodes(0, 0, 1)
        return self.verify_cem_8760(compute_nodes)#, sub_intf, ipv6=ipv6)

    def create_sub_intf(self, vn_fix_uuid, intf_type, mac_address=None):

        vlan = self.vlan
        parent_port_vn_subnets = [get_random_cidr(af=self.inputs.get_af())]
        parent_port_vn_name = get_random_name( intf_type + "_parent_port_vn")
        parent_port_vn_fixture = self.config_vn(parent_port_vn_name, parent_port_vn_subnets)
        parent_port = self.setup_vmi(parent_port_vn_fixture.uuid)
        mac_address = parent_port.mac_address
        port = self.setup_vmi(vn_fix_uuid,
                                       parent_vmi=parent_port.vmi_obj,
                                       vlan_id=vlan,
                                       api_type='contrail',
                                       mac_address=mac_address)
        return port, parent_port, parent_port_vn_fixture
    # end get_sub_intf_port

    def create_policy_rule(self, src_vn, dst_vn):

        rules = [{'direction': '<>',
            'protocol': 'icmp',
            'source_network': src_vn,
            'src_ports': [0, 65535],
            'dest_network': dst_vn,
            'dst_ports': [0, 65535],
            'simple_action': 'pass',
            'action_list': {'simple_action': 'pass'}
            },
            {'direction': '<>',
            'protocol': 'icmp6',
            'source_network': src_vn,
            'src_ports': [0, 65535],
            'dest_network': dst_vn,
            'dst_ports': [0, 65535],
            'simple_action': 'pass',
            'action_list': {'simple_action': 'pass'}
            }]

        rules.append({'direction': '<>',
            'protocol': 'udp',
            'source_network': src_vn,
            'src_ports': [0, 65535],
            'dest_network': dst_vn,
            'dst_ports': [0, 65535],
            'simple_action': 'pass',
            'action_list': {'simple_action': 'pass'}
            })
        return rules
    # end create_policy_rule

    def verify_intf_mirroring(self, compute_nodes, vn_index_list, sub_intf=False, parent_intf=False, nic_mirror=False,
        header=1, nh_mode='dynamic', direction='both', ipv6=False):

        """Validate the interface mirroring
           Test steps:
           1. Create vn1/vm1_vn1, vn1/vm2_vn1, vn1/mirror_vm_vn1,  vn2/vm2_vn2, vn2/mirror_vm_vn2, vn3/mirror_vm_vn3
           2. Create the policies vn1_vn2 and vn1_vn3 for ICMP/UDP and attach to vn's
           3. Enable intf mirroring on src vm's port and test the following cases:
               src vm in vn1, mirror vm in vn1, and dst vm in vn2
               src vm in vn1, mirror vm in vn3, and dst vm in vn2
               src vm, dst vm and mirror vm all are in vn1
               src vm in vn1, dst vm in vn2, and mirror vm in vn2
           4. Send the traffic from vm1 to vm2 and verify if the packets gets mirrored to mirror_vm the analyzer
           Pass criteria :
            Pkts(based on direction) getting mirrored to mirror_vm
        """
        result = True
        if ipv6: self.inputs.set_af('v6')
        src_compute = compute_nodes[0]
        dst_compute = compute_nodes[1]
        analyzer_compute = compute_nodes[2]

        analyzer_port = 8099
        image_name = 'cirros'
        #changing it to ubuntu to use tshark later
        #image_name = 'ubuntu' if not sub_intf else 'ubuntu'
        if ipv6 or sub_intf or header in [2, 3] or self.inputs.pcap_on_vm or \
            self.inputs.ns_agilio_vrouter_data:
            image_name = 'ubuntu'

        vn1_subnets = [get_random_cidr(af=self.inputs.get_af())]
        vn2_subnets = [get_random_cidr(af=self.inputs.get_af())]
        vn3_subnets = [get_random_cidr(af=self.inputs.get_af())]


        vn1_fq_name = self.connections.domain_name +":"  + self.inputs.project_name + \
            ":" + get_random_name("vn1")
        vn2_fq_name = self.connections.domain_name +":"  + self.inputs.project_name + \
            ":" + get_random_name("vn2")
        vn3_fq_name = self.connections.domain_name +":"  + self.inputs.project_name + \
            ":" + get_random_name("vn3")

        vn1_name = vn1_fq_name.split(':')[2]
        vn2_name = vn2_fq_name.split(':')[2]
        vn3_name = vn3_fq_name.split(':')[2]

        self.vn1_fixture = self.config_vn(vn1_name, vn1_subnets)
        self.vn2_fixture = self.config_vn(vn2_name, vn2_subnets)
        self.vn3_fixture = self.config_vn(vn3_name, vn3_subnets)

        policy_name_vn1_vn2 = get_random_name("vn1_vn2_pass")
        policy_name_vn1_vn3 = get_random_name("vn1_vn3_pass")
        policy_name_vn2_vn3 = get_random_name("vn2_vn3_pass")

        rules_vn1_vn2 = self.create_policy_rule(vn1_name, vn2_name)
        rules_vn1_vn3 = self.create_policy_rule(vn1_name, vn3_name)
        rules_vn2_vn3 = self.create_policy_rule(vn2_name, vn3_name)

        policy_fixture_vn1_vn2 = self.config_policy(policy_name_vn1_vn2, rules_vn1_vn2)
        policy_fixture_vn1_vn3 = self.config_policy(policy_name_vn1_vn3, rules_vn1_vn3)
        policy_fixture_vn2_vn3 = self.config_policy(policy_name_vn2_vn3, rules_vn2_vn3)

        vn1_v2_attach_to_vn1 = self.attach_policy_to_vn(
            policy_fixture_vn1_vn2, self.vn1_fixture)
        vn1_vn2_attach_to_vn2 = self.attach_policy_to_vn(
            policy_fixture_vn1_vn2, self.vn2_fixture)

        vn1_v3_attach_to_vn1 = self.attach_policy_to_vn(
            policy_fixture_vn1_vn3, self.vn1_fixture)
        vn1_v3_attach_to_vn3 = self.attach_policy_to_vn(
            policy_fixture_vn1_vn3, self.vn3_fixture)

        vn2_v3_attach_to_vn2 = self.attach_policy_to_vn(
            policy_fixture_vn2_vn3, self.vn2_fixture)
        vn2_v3_attach_to_vn3 = self.attach_policy_to_vn(
            policy_fixture_vn2_vn3, self.vn3_fixture)

        vn1_vmi_ref, vn2_vmi_ref, vn3_vmi_ref = None, None, None

        self.vlan = 101

        if vn_index_list[0] == 0:
           src_vn_fixture = self.vn1_fixture
           src_vn_fq_name = vn1_fq_name
           src_vn_name = vn1_fq_name.split(':')[2]
           vn1_vmi_ref = True
           if sub_intf:
               intf_type = 'src'
               src_port, src_parent_port, src_parent_port_vn_fixture = self.create_sub_intf(self.vn1_fixture.uuid, intf_type)

        elif vn_index_list[0] == 1:
           src_vn_fixture = self.vn2_fixture
           src_vn_fq_name = vn2_fq_name
           src_vn_name = vn2_fq_name.split(':')[2]
           vn2_vmi_ref = True
           if sub_intf:
               intf_type = 'src'
               src_port, src_parent_port, src_parent_port_vn_fixture = self.create_sub_intf(self.vn2_fixture.uuid, intf_type)
        else:
           src_vn_fixture = self.vn3_fixture
           src_vn_fq_name = vn3_fq_name
           src_vn_name = vn3_fq_name.split(':')[2]
           vn3_vmi_ref = True
           if sub_intf:
               intf_type = 'src'
               src_port, src_parent_port, src_parent_port_vn_fixture = self.create_sub_intf(self.vn3_fixture.uuid, intf_type)

        if vn_index_list[1] == 0:
           dst_vn_fixture = self.vn1_fixture
           dst_vn_fq_name = vn1_fq_name
           dst_vn_name = vn1_fq_name.split(':')[2]
           vn1_vmi_ref = True
           if sub_intf:
               intf_type = 'dst'
               dst_port, dst_parent_port, dst_parent_port_vn_fixture = self.create_sub_intf(self.vn1_fixture.uuid, intf_type)

        elif vn_index_list[1] == 1:
           dst_vn_fixture = self.vn2_fixture
           dst_vn_fq_name = vn2_fq_name
           dst_vn_name = vn2_fq_name.split(':')[2]
           vn2_vmi_ref = True
           if sub_intf:
               intf_type = 'dst'
               dst_port, dst_parent_port, dst_parent_port_vn_fixture = self.create_sub_intf(self.vn2_fixture.uuid, intf_type)
        else:
           dst_vn_fixture = self.vn3_fixture
           dst_vn_fq_name = vn3_fq_name
           dst_vn_name = vn3_fq_name.split(':')[2]
           vn3_vmi_ref = True
           if sub_intf:
               intf_type = 'dst'
               dst_port, dst_parent_port, dst_parent_port_vn_fixture = self.create_sub_intf(self.vn3_fixture.uuid, intf_type)

        if vn_index_list[2] == 0:
           analyzer_vn_fixture = self.vn1_fixture
           analyzer_vn_fq_name = vn1_fq_name
           analyzer_vn_name = vn1_fq_name.split(':')[2]
           vn1_vmi_ref = True
           if sub_intf:
               intf_type = 'analyzer'
               analyzer_port, analyzer_parent_port, analyzer_parent_port_vn_fixture = self.create_sub_intf(self.vn1_fixture.uuid, intf_type)

        elif vn_index_list[2] == 1:
           analyzer_vn_fixture = self.vn2_fixture
           analyzer_vn_fq_name = vn2_fq_name
           analyzer_vn_name = vn2_fq_name.split(':')[2]
           vn2_vmi_ref = True
           if sub_intf:
               intf_type = 'analyzer'
               analyzer_port, analyzer_parent_port, analyzer_parent_port_vn_fixture = self.create_sub_intf(self.vn2_fixture.uuid, intf_type)
        else:
           analyzer_vn_fixture = self.vn3_fixture
           analyzer_vn_fq_name = vn3_fq_name
           analyzer_vn_name = vn3_fq_name.split(':')[2]
           vn3_vmi_ref = True
           if sub_intf:
               intf_type = 'analyzer'
               analyzer_port, analyzer_parent_port, analyzer_parent_port_vn_fixture = self.create_sub_intf(self.vn3_fixture.uuid, intf_type)

        #if parent_intf or self.inputs.get_af() == 'v6':
        if parent_intf:
            policy_name_src_parent_vn_analyzer_vn = get_random_name("src_parent_to_analyzer_pass")
            policy_name_dst_parent_vn_analyzer_vn = get_random_name("dst_parent_to_analyzer_pass")
            policy_name_src_parent_vn_dst_parent_vn = get_random_name("src_parent_to_dst_parent_pass")

            src_parent_vn_name = src_parent_port_vn_fixture.vn_name
            dst_parent_vn_name = dst_parent_port_vn_fixture.vn_name

            rules_src_parent_vn_analyzer_vn = self.create_policy_rule(src_parent_vn_name, analyzer_vn_name)
            rules_dst_parent_vn_analyzer_vn = self.create_policy_rule(dst_parent_vn_name, analyzer_vn_name)

            rules_src_parent_vn_dst_parent_vn = self.create_policy_rule(src_parent_vn_name, dst_parent_vn_name)

            policy_fixture_src_parent_vn_analyzer_vn = self.config_policy(
                policy_name_src_parent_vn_analyzer_vn, rules_src_parent_vn_analyzer_vn)
            policy_fixture_dst_parent_vn_analyzer_vn = self.config_policy(
                policy_name_dst_parent_vn_analyzer_vn, rules_dst_parent_vn_analyzer_vn)

            policy_fixture_src_parent_vn_dst_parent_vn = self.config_policy(
                policy_name_src_parent_vn_dst_parent_vn, rules_src_parent_vn_dst_parent_vn)

            self.attach_policy_to_vn(
                policy_fixture_src_parent_vn_analyzer_vn, analyzer_vn_fixture)

            self.attach_policy_to_vn(
                policy_fixture_src_parent_vn_analyzer_vn, src_parent_port_vn_fixture)

            self.attach_policy_to_vn(
                policy_fixture_dst_parent_vn_analyzer_vn, analyzer_vn_fixture)

            self.attach_policy_to_vn(
                policy_fixture_dst_parent_vn_analyzer_vn,dst_parent_port_vn_fixture)

            self.attach_policy_to_vn(
                policy_fixture_src_parent_vn_dst_parent_vn, src_parent_port_vn_fixture)

            self.attach_policy_to_vn(
                policy_fixture_src_parent_vn_dst_parent_vn,dst_parent_port_vn_fixture)


        src_vm_name = get_random_name("src_vm")
        dst_vm_name = get_random_name("dst_vm")
        analyzer_vm_name = get_random_name("analyzer_vm")

        analyzer_fq_name  = self.connections.domain_name +":"  + self.inputs.project_name + \
            ":" + analyzer_vm_name
        routing_instance = analyzer_vn_fq_name + ':' + analyzer_vn_name

        src_port_ids, dst_port_ids, analyzer_port_ids = [], [], []

        src_vn_objs = [src_vn_fixture.obj]
        dst_vn_objs = [dst_vn_fixture.obj]
        analyzer_vn_objs = [analyzer_vn_fixture.obj]

        if sub_intf:
            src_port_ids.append(src_parent_port.uuid)
            dst_port_ids.append(dst_parent_port.uuid)
            analyzer_port_ids.append(analyzer_parent_port.uuid)
            src_vn_objs = [src_parent_port_vn_fixture.obj]
            dst_vn_objs = [dst_parent_port_vn_fixture.obj]
            analyzer_vn_objs = [analyzer_parent_port_vn_fixture.obj]
        if ipv6:
            for addr in src_vn_objs[0]['network']['subnet_ipam']:
                if get_af_type(addr.get('subnet_cidr')) in ['v6', 'dual']:
                   src_mask = addr.get('subnet_cidr').split('/')[1]
                   break
            for addr in dst_vn_objs[0]['network']['subnet_ipam']:
                if get_af_type(addr.get('subnet_cidr')) in ['v6', 'dual']:
                   dst_mask = addr.get('subnet_cidr').split('/')[1]
                   break

            for addr in analyzer_vn_objs[0]['network']['subnet_ipam']:
                if get_af_type(addr.get('subnet_cidr')) in ['v6', 'dual']:
                   analyzer_mask = addr.get('subnet_cidr').split('/')[1]
                   break
        src_vm_fixture = self.create_vm(vn_objs=src_vn_objs, vm_name=src_vm_name,
            image_name=image_name, node_name=src_compute, port_ids=src_port_ids)

        dst_vm_fixture = self.create_vm(vn_objs=dst_vn_objs, vm_name=dst_vm_name,
            image_name=image_name, node_name=dst_compute, port_ids=dst_port_ids)

        analyzer_vm_fixture = self.create_vm(vn_objs=analyzer_vn_objs, vm_name=analyzer_vm_name,
            image_name=image_name, node_name=analyzer_compute, port_ids=analyzer_port_ids)

        assert src_vm_fixture.verify_on_setup()
        assert dst_vm_fixture.verify_on_setup()
        assert analyzer_vm_fixture.verify_on_setup()

        self.nova_h.wait_till_vm_is_up(src_vm_fixture.vm_obj)
        self.nova_h.wait_till_vm_is_up(dst_vm_fixture.vm_obj)
        self.nova_h.wait_till_vm_is_up(analyzer_vm_fixture.vm_obj)
        if vn1_vmi_ref:
            result, msg = self.validate_vn(vn_fq_name=vn1_fq_name)
            assert result, msg
        if vn2_vmi_ref:
            result, msg = self.validate_vn(vn_fq_name=vn2_fq_name)
            assert result, msg
        if vn3_vmi_ref:
            result, msg = self.validate_vn(vn_fq_name=vn3_fq_name)
            assert result, msg

        if sub_intf and not ipv6:
            src_vm_ip = src_port.get_ip_addresses()[0]
            dst_vm_ip = dst_port.get_ip_addresses()[0]
            analyzer_vm_ip = analyzer_port.get_ip_addresses()[0]
        elif sub_intf and ipv6:
            for ip in src_port.get_ip_addresses():
                if 'v6' in get_af_type(ip):
                    src_vm_ip = ip
            for ip in dst_port.get_ip_addresses():
                if 'v6' in get_af_type(ip):
                    dst_vm_ip = ip
            for ip in analyzer_port.get_ip_addresses():
                if 'v6' in get_af_type(ip):
                    analyzer_vm_ip = ip
        else:
            src_vm_ip = src_vm_fixture.get_vm_ips(src_vn_fq_name)[0]
            dst_vm_ip = dst_vm_fixture.get_vm_ips(dst_vn_fq_name)[0]
            analyzer_vm_ip = analyzer_vm_fixture.get_vm_ips(analyzer_vn_fq_name)[0]

        self.logger.info("Compute/VM: SRC: %s / %s, -> DST: %s / %s => ANALYZER: %s / %s" %
            (src_compute, src_vm_ip, dst_compute, dst_vm_ip, analyzer_compute, analyzer_vm_ip))
        if parent_intf:
            parent_src_vm_ip = src_vm_fixture.get_vm_ips()[0]
            parent_dst_vm_ip = dst_vm_fixture.get_vm_ips()[0]
            parent_analyzer_vm_ip = analyzer_vm_fixture.get_vm_ips()[0]

        sport = None

        if sub_intf:
            intf_type = 'src'
            cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo udhcpc -i eth0.101']
            if ipv6: cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo ifconfig eth0.101 inet6 add ' + src_vm_ip + '/' + src_mask]
            output = src_vm_fixture.run_cmd_on_vm(cmds = cmds)

            intf_type = 'dst'
            cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo udhcpc -i eth0.101']
            if ipv6: cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo ifconfig eth0.101 inet6 add ' + dst_vm_ip + '/' + dst_mask]
            output = dst_vm_fixture.run_cmd_on_vm(cmds = cmds)

            intf_type = 'analyzer'
            cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo udhcpc -i eth0.101']
            if ipv6: cmds = ['sudo vconfig add eth0 101','sudo ifconfig eth0.101 up','sudo ifconfig eth0.101 inet6 add ' + analyzer_vm_ip + '/' + analyzer_mask]
            output = analyzer_vm_fixture.run_cmd_on_vm(cmds = cmds)
            sport = src_port.vmi_obj
        if not self._verify_intf_mirroring(src_vm_fixture, dst_vm_fixture, analyzer_vm_fixture, \
                src_vn_fq_name, dst_vn_fq_name, analyzer_vn_fq_name,
                analyzer_vm_ip, analyzer_fq_name, routing_instance, src_port=sport, sub_intf=sub_intf, parent_intf=parent_intf, nic_mirror=nic_mirror, header = header, nh_mode=nh_mode, direction = direction):
            result = result and False

        return result
    # end verify_intf_mirroring

    def verify_cem_8760(self, compute_nodes, nic_mirror=False,
        header=1, nh_mode='dynamic'):

        result = True
        src_compute = compute_nodes[0]
        analyzer_compute = compute_nodes[2]

        image_name = 'ubuntu-traffic'
        vn1_subnets = [get_random_cidr(af=self.inputs.get_af())]
        vn2_subnets = [get_random_cidr(af=self.inputs.get_af())]

        vn1_fq_name = self.connections.domain_name +":" \
                      + self.inputs.project_name + \
                      ":" + get_random_name("vn1")
        vn2_fq_name = self.connections.domain_name +":" \
                      + self.inputs.project_name + \
                      ":" + get_random_name("vn2")

        vn1_name = vn1_fq_name.split(':')[2]
        vn2_name = vn2_fq_name.split(':')[2]

        self.vn1_fixture = self.config_vn(vn1_name, vn1_subnets)
        self.vn2_fixture = self.config_vn(vn2_name, vn2_subnets)

        src_vn_fixture = self.vn1_fixture
        src_vn_fq_name = vn1_fq_name
        src_vn_name = vn1_fq_name.split(':')[2]

        analyzer_vn_fixture = self.vn2_fixture
        analyzer_vn_fq_name = vn2_fq_name
        analyzer_vn_name = vn2_fq_name.split(':')[2]

        src_vm_name = get_random_name("src_vm")
        analyzer_vm_name = get_random_name("analyzer_vm")

        src_fq_name = self.connections.domain_name +":" \
                      + self.inputs.project_name + \
                      ":" + src_vm_name
        analyzer_fq_name = self.connections.domain_name +":" \
                           + self.inputs.project_name + \
                           ":" + analyzer_vm_name
        routing_instance = analyzer_vn_fq_name + ':' + analyzer_vn_name

        src_port_ids, analyzer_port_ids = [], []

        src_vn_objs = [src_vn_fixture.obj]
        analyzer_vn_objs = [analyzer_vn_fixture.obj]

        src_vm_fixture = self.create_vm(vn_objs=src_vn_objs, vm_name=src_vm_name,
            image_name=image_name, node_name=src_compute, port_ids=src_port_ids)

        analyzer_vm_fixture = self.create_vm(vn_objs=analyzer_vn_objs,
            vm_name=analyzer_vm_name, image_name=image_name,
            node_name=analyzer_compute, port_ids=analyzer_port_ids)

        assert src_vm_fixture.verify_on_setup()
        assert analyzer_vm_fixture.verify_on_setup()

        self.nova_h.wait_till_vm_is_up(src_vm_fixture.vm_obj)
        self.nova_h.wait_till_vm_is_up(analyzer_vm_fixture.vm_obj)

        src_vm_ip = src_vm_fixture.get_vm_ips(src_vn_fq_name)[0]
        analyzer_vm_ip = analyzer_vm_fixture.get_vm_ips(analyzer_vn_fq_name)[0]
        analyzer_vm_mac = analyzer_vm_fixture.get_mac_addr_from_config(
                              )[analyzer_vn_fq_name]
        self.logger.info("\nCompute/VM: SRC: %s / %s, => ANALYZER: %s / %s\n" %
            (src_compute, src_vm_ip, analyzer_compute, analyzer_vm_ip))

        # Make sure contrail-tools container is pulled and commands
        # can be executed with contrail-tools.
        cmd = "contrail-tools flow -l"
        for compute in self.inputs.compute_ips:
            self.inputs.run_cmd_on_server(compute, cmd)

        # Enable mirroring on the analyzer virtual network.
        vn_properties = {"mirror_destination": True}
        vn_fix_update = self.vnc_lib.virtual_network_read(
                            id = analyzer_vn_fixture.uuid)
        vn_fix_update.set_virtual_network_properties(vn_properties)
        self.vnc_lib.virtual_network_update(vn_fix_update)

        # Enable mirroring on source port of source VM.
        vnc = src_vm_fixture.vnc_lib_h
        src_port = src_vm_fixture.get_tap_intf_of_vm()[0]
        src_port_obj = vnc.virtual_machine_interface_read(id=src_port['uuid'])
        prop_obj = VirtualMachineInterfacePropertiesType()
        mirror_to = MirrorActionType(analyzer_name='cem-8760', encapsulation=None,
                        analyzer_ip_address=analyzer_vm_ip, juniper_header = False,
                        nh_mode='dynamic', routing_instance=routing_instance,
                        analyzer_mac_address = analyzer_vm_mac)
        interface_mirror = InterfaceMirrorType('both', mirror_to)
        prop_obj.set_interface_mirror(interface_mirror)
        src_port_obj.set_virtual_machine_interface_properties(prop_obj)
        src_port_obj = vnc.virtual_machine_interface_update(src_port_obj)

        # Enable/Disable packet mode/Policy (earlier flag) and
        # Ping dns from src VM and check mirrored icmp packets.
        vnc = analyzer_vm_fixture.vnc_lib_h
        analyzer_port = analyzer_vm_fixture.get_tap_intf_of_vm()[0]
        analyzer_port_obj = vnc.virtual_machine_interface_read(
                                id=analyzer_port['uuid'])
        dst_ip = src_vn_fixture.get_dns_ip()
        filters = '\'(icmp[0]=0 and src host %s)\'' % (dst_ip)
        enable_pkt_mode=False
        vm_fix_pcap_pid_files = []
        exp_count=3
        for i in range(20):
            enable_pkt_mode = True if i%2 == 0 else False
            analyzer_port_obj.set_virtual_machine_interface_disable_policy(
                bool(enable_pkt_mode))
            vnc.virtual_machine_interface_update(analyzer_port_obj)
            vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf(self, [analyzer_vm_fixture],
                                analyzer_vn_fq_name, filters=filters, pcap_on_vm=True)
            sleep(5)
            assert src_vm_fixture.ping_with_certainty(dst_ip, count=exp_count,
                       expectation=True)
            sleep(5)
            if not verify_tcpdump_count(self, session=None, pcap=None,
                       exp_count=exp_count, mac=None, raw_count=False,
                       exact_match=True, vm_fix_pcap_pid_files=vm_fix_pcap_pid_files,
                       svm=False, grep_string=None):
                self.logger.error("\n Duplicate packates seen in packet capture of\
                           \n mirrored, packets from source VN. There can be a\
                           \n potential duplicate NH ID.\n\n")
                result=False
                break

        #Check for duplicate NH.
        cmd = "contrail-tools mirror --dump | grep VNI -A2 "
        cmd = cmd + "| grep -v VNI | grep -v '\\-\\-\\-\\-'"
        vni_id = self.inputs.run_cmd_on_server(src_vm_fixture.vm_node_ip, cmd)
        vni_id = vni_id.split()[3] if len(vni_id.split())==5 else vni_id.split()[2]
        cmd = "contrail-tools vxlan --get %s | grep NextHop -A2" % vni_id
        cmd = cmd + "| grep -v NextHop | grep -v '\\-\\-\\-\\-'"
        nh_id = self.inputs.run_cmd_on_server(analyzer_vm_fixture.vm_node_ip, cmd)
        nh_id = nh_id.split()[1]
        cmd = "contrail-tools nh --get %s | grep 'Sub NH'" % nh_id
        nh_ids = self.inputs.run_cmd_on_server(analyzer_vm_fixture.vm_node_ip, cmd)
        if len(nh_ids.split()) > 3:
            self.logger.error("\n Duplicate NH IDs observed for the VMI of the source VM.")
            self.logger.error("\n Duplicate NH IDs: %s" % nh_ids)
            result=False
        return result
    # end verify_cem_8760

    #when no header is specified, this routine has to be called to add "mirroring" to vn properties
    def add_vn_mirror_properties(self):
        vn_properties = {"allow_transit": False, "mirror_destination": True, "rpf": "enable"}
        vn_fix_update = self.vnc_lib.virtual_network_read(id = self.vn1_fixture.uuid)
        vn_fix_update.set_virtual_network_properties(vn_properties)
        self.vnc_lib.virtual_network_update(vn_fix_update)

        vn_fix_update = self.vnc_lib.virtual_network_read(id = self.vn2_fixture.uuid)
        vn_fix_update.set_virtual_network_properties(vn_properties)
        self.vnc_lib.virtual_network_update(vn_fix_update)

        vn_fix_update = self.vnc_lib.virtual_network_read(id = self.vn3_fixture.uuid)
        vn_fix_update.set_virtual_network_properties(vn_properties)
        self.vnc_lib.virtual_network_update(vn_fix_update)

    def config_intf_mirroring(self, src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, \
            src_port=None, sub_intf=False, parent_intf=False, nic_mirror=False, header = 1, nh_mode = 'dynamic', direction = 'both', analyzer_mac_address = '', mirror_vm_fixture = None):

        #Short desc of what the header values are:
        #header 1 is the default value, which is header enabled. All present testcases will have this as default, should not affect legacy cases
        #header 2 is for dynamic mirroring, with juniper header, and directionality of traffic and want the header verification to be done
        #header 3 would mean header disabled. In this case, routes have to be imported from other VN vrf, so a change vn properties is needed
        if header == 3:
            self.add_vn_mirror_properties()
            analyzer_mac_address = mirror_vm_fixture.mac_addr[self.vn3_fixture.vn_fq_name]

        vnc = src_vm_fixture.vnc_lib_h
        vlan = None
        tap_intf_obj = None
        parent_tap_intf_obj = None
        vlan = None
        tap_intf_objs = src_vm_fixture.get_tap_intf_of_vm()
        for tap_intf_obj in tap_intf_objs:
            intf_type = 'tap'
            if self.inputs.ns_agilio_vrouter_data:
                intf_type = 'nfp'
            if intf_type in tap_intf_obj['name']:
                parent_tap_intf_uuid = tap_intf_obj['uuid']
            else:
                sub_intf_tap_intf_uuid = tap_intf_obj['uuid']
        if not sub_intf:
            tap_intf_uuid = src_vm_fixture.get_tap_intf_of_vm()[0]['uuid']
            tap_intf_obj = vnc.virtual_machine_interface_read(id=tap_intf_uuid)
        else:
            tap_intf_obj = src_port
            vlan = self.vlan

        if parent_intf:
            parent_tap_intf_obj = vnc.virtual_machine_interface_read(id=parent_tap_intf_uuid)
        if header == 1 or header == 2:
            header_value = True
        else:
            header_value = False
        if not nic_mirror:
            self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = header_value, nh_mode=nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)
            if parent_intf:
                self.logger.info("Intf mirroring enabled on both sub intf port and parent port")
                self.enable_intf_mirroring(vnc, parent_tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = header_value, nh_mode=nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)
            return vnc, tap_intf_obj, parent_tap_intf_obj, vlan
        else:
            self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address=None, analyzer_name=analyzer_name, \
                routing_instance=None, udp_port=None, nic_assisted_mirroring=True, nic_assisted_mirroring_vlan=100, header = header_value, nh_mode=nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)
            if src_vm_fixture.vm_obj.status == 'ACTIVE':
                host = self.get_svm_compute(src_vm_fixture.vm_obj.name)
            session = ssh(host['host_ip'], host['username'], host['password'])
            agent_physical_interface = src_vm_fixture.agent_inspect[host['host_ip']].get_agent_physical_interface()
            pcap = self.start_tcpdump(session, agent_physical_interface, vlan=100)
            src_vm_fixture.ping_with_certainty(mirror_vm_fixture.vm_ip, count=11, size='1400')
            filt = '-e | grep \"vlan 100\"'
            mirror_pkt_count = self.stop_tcpdump(session, pcap, filt)
            if mirror_pkt_count == 0:
                self.logger.error("Nic mirroring doesn't works correctly")
                result = result and False
            else:
                self.logger.info("Nic mirroring works correctly")
    # end config_intf_mirroring
    #routine to verify inner header by checking the source and dst ip based in direction mirrored
    def verify_inner_header(self, vm_fix_pcap_pid_files, src_vm_ip, dst_vm_ip, direction = 'both'):
        cmds = 'tshark -r %s -n -d udp.port==8099,juniper' % vm_fix_pcap_pid_files[0][1]
        outer_header = vm_fix_pcap_pid_files[0][0].run_cmd_on_vm(cmds = [cmds])
        proto = 'ICMP'
        if self.inputs.get_af() in ['v6', 'dual']:
            proto = 'ICMPv6'

        if direction == 'both':
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *request' % (src_vm_ip, dst_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if not is_header_correct.group(0):
                self.logger.error("With birectional mirroring, src to dst mirrored packets seem to be absent")
                return False
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *reply' % (dst_vm_ip, src_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if not is_header_correct.group(0):
                self.logger.error("With birectional mirroring, dst to src mirrored packets seem to be absent")
                return False
        if direction == 'ingress':
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *request' % (src_vm_ip, dst_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if not is_header_correct.group(0):
                self.logger.error("With ingress mirroring, src to dst mirrored packets seem to be absent")
                return False
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *reply' % (dst_vm_ip, src_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if is_header_correct:
                self.logger.error("With ingress mirroring, dst to src mirrored packets seem to be present")
                return False
        if direction == 'egress':
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *reply' % (dst_vm_ip, src_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if not is_header_correct.group(0):
                self.logger.error("With egress mirroring, src to dst mirrored packets seem to be present")
                return False
            regex = re.compile('%s.*%s *%s *\d* *Echo *\(ping\) *request' % (src_vm_ip, dst_vm_ip, proto))
            is_header_correct = re.search(regex, str(outer_header))
            if is_header_correct:
                self.logger.error("With egress mirroring, dst to src mirrored packets seem to be absent")
                return False
        self.logger.info("The directionality configured and mirrored packets actually captured seem to match")
        return True

    #routine to verify juniper header, called if header is enabled
    def verify_juniper_header(self, vm_fix_pcap_pid_files, src_vn_fq):
        cmds = 'tshark -r %s -n -d udp.port==8099,juniper -Tfields -e juniper.vn.src -e juniper.vn.dst' % vm_fix_pcap_pid_files[0][1]
        juniper_header = vm_fix_pcap_pid_files[0][0].run_cmd_on_vm(cmds = [cmds])
        regex = re.compile('%s' % src_vn_fq)
        is_header_correct = re.search(regex, str(juniper_header))
        if not is_header_correct.group(0):
            return False
        return True

    def verify_header_details(self, src_vm_fixture, mirror_vm_fixture, src_vm_ip, dst_vm_ip, mirror_vm_ip, src_vn_fq, direction = 'both', header = 1):

        vm_fix_pcap_pid_files = start_tcpdump_for_vm_intf(None, [mirror_vm_fixture], None, pcap_on_vm=True)
        if self.inputs.get_af() in ['v6', 'dual']:
            src_vm_fixture.run_cmd_on_vm(["ping6 %s -c 5" % dst_vm_ip])
        else:
           src_vm_fixture.run_cmd_on_vm(["ping %s -c 5" % dst_vm_ip])
        stop_tcpdump_for_vm_intf(None, None, None, vm_fix_pcap_pid_files=vm_fix_pcap_pid_files)
        assert self.verify_inner_header(vm_fix_pcap_pid_files, src_vm_ip, dst_vm_ip, direction = direction)
        if header == 2:
            assert self.verify_juniper_header(vm_fix_pcap_pid_files, src_vn_fq)

    def _verify_intf_mirroring(self, src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, src_vn_fq, dst_vn_fq, mirr_vn_fq,\
            analyzer_ip_address, analyzer_name, routing_instance, src_port=None, sub_intf=False, parent_intf=False, nic_mirror=False, header = 1, nh_mode = 'dynamic', direction = 'both'):
        result = True
        vnc, tap_intf_obj, parent_tap_intf_obj, vlan = self.config_intf_mirroring(
            src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, src_port=src_port, sub_intf=sub_intf, parent_intf=parent_intf, nic_mirror=nic_mirror, header = header, nh_mode=nh_mode, direction = direction, mirror_vm_fixture = mirror_vm_fixture)
        no_header = False
        if header == 3:
            no_header = True
        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, vlan=vlan, parent=parent_intf, direction = direction, no_header = no_header):
            result = result and False
            if parent:
                self.logger.error("Traffic mirroring from both the ports expected, failed from one or both")
            elif vlan:
                self.logger.error("Traffic mirroring from the sub intf port failed")
            else:
                self.logger.error("Intf mirroring not working")

        if (header == 2 or header == 3):
            self.verify_header_details(src_vm_fixture, mirror_vm_fixture, src_vm_fixture.vm_ip, dst_vm_fixture.vm_ip, mirror_vm_fixture.vm_ip, src_vn_fq, direction = direction, header = header)

        self.logger.info("Disabling intf mirroring on sub intf port")
        self.disable_intf_mirroring(vnc, tap_intf_obj)

        if parent_tap_intf_obj:
            self.logger.info("Disabling intf mirroring on parent intf port")
            self.disable_intf_mirroring(vnc, parent_tap_intf_obj)

        if parent_intf:
            if not self.verify_disable_enable_combinations(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, \
                    analyzer_ip_address, analyzer_name, routing_instance, src_port=src_port, sub_intf=sub_intf, parent_intf=parent_intf):
                result = result and False

        return result
    # end _verify_intf_mirroring

    def verify_disable_enable_combinations(self, src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, \
            analyzer_ip_address, analyzer_name, routing_instance, src_port=None, sub_intf=False, parent_intf=False):
        result = True
        vnc, tap_intf_obj, parent_tap_intf_obj, vlan = self.config_intf_mirroring(
            src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, src_port=src_port, sub_intf=sub_intf, parent_intf=parent_intf)

        # Mirroring disabled on sub intf, but enabled on parent port, expect sub intf traffic to get mirrored via parent port
        self.disable_intf_mirroring(vnc, tap_intf_obj)
        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, vlan=vlan):
            result = result and False
            self.logger.error("Traffic stopped getting mirrored from parent port after disabling intf mirroring on sub intf port")
        else:
            self.logger.info("Traffic is getting mirrored from parent port as expected")

        self.logger.info("Enabling intf mirroring on sub intf, expect pkts to get mirrored from both the ports")
        self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = True)

        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, vlan=vlan, parent=parent_intf):
            result = result and False
            self.logger.error("Traffic is not getting mirrored from both parent port and sub intf")
        else:
            self.logger.info("Traffic is getting mirrored from both parent port and sub intf as expected")
        # Disable intf mirroring on parent port
        self.disable_intf_mirroring(vnc, parent_tap_intf_obj)

        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, vlan=vlan):
            result = result and False
            self.logger.error("Traffic stopped getting mirrored from sub intf after disabling intf mirroring on parent port")
        else:
            self.logger.info("Traffic is getting mirrored from sub intf as expected")

        # enable intf mirroring on parent port
        self.enable_intf_mirroring(vnc, parent_tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = True)

        self.logger.info("Check traffic is getting mirrored from both the ports")

        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, mirror_vm_fixture, vlan=vlan, parent=parent_intf):
            result = result and False
            self.logger.error("Traffic not is getting mirrored from both the ports")
        else:
            self.logger.info("Traffic is getting mirrored from both the ports as expected")

        self.disable_intf_mirroring(vnc, tap_intf_obj)
        self.disable_intf_mirroring(vnc, parent_tap_intf_obj)

        return result
    # end verify_disable_enable_combinations

    def enable_intf_mirroring(self, vnc, tap, analyzer_ip_address, analyzer_name, routing_instance,
                             direction='both', udp_port=8099,  encapsulation=None, \
                             nic_assisted_mirroring=None, nic_assisted_mirroring_vlan = None, header = False, nh_mode = 'dynamic', analyzer_mac_address = ''):
        prop_obj = tap.get_virtual_machine_interface_properties()
        if not prop_obj:
            prop_obj = VirtualMachineInterfacePropertiesType()
        interface_mirror = prop_obj.get_interface_mirror()
        if not interface_mirror:
            #if the mode is static, the mirroring config changes, so the call to MirrorActionType changes
            if nh_mode == 'static':
                hosted_node = str(tap.get_virtual_machine_interface_bindings().get_key_value_pair()[0].value)
                hosted_node_ip = self.inputs.host_data[hosted_node]['data-ip']
                vn_uuid = tap.get_virtual_network_refs()[0]['uuid']
                vni = vnc.virtual_network_read(id = vn_uuid).virtual_network_network_id
                staticmirror_nh = StaticMirrorNhType(vtep_dst_ip_address = hosted_node_ip, vni = vni)
                mirror_to = MirrorActionType(analyzer_name=analyzer_name, encapsulation=None,analyzer_ip_address=analyzer_ip_address, juniper_header = header, nh_mode=nh_mode, static_nh_header=staticmirror_nh, routing_instance=routing_instance,udp_port=udp_port, analyzer_mac_address = analyzer_mac_address)
            else:
                mirror_to = MirrorActionType(analyzer_name=analyzer_name, encapsulation=None, analyzer_ip_address=analyzer_ip_address, juniper_header = header, routing_instance=routing_instance, udp_port=udp_port, nic_assisted_mirroring = nic_assisted_mirroring, nic_assisted_mirroring_vlan=nic_assisted_mirroring_vlan, analyzer_mac_address = analyzer_mac_address)
            interface_mirror = InterfaceMirrorType(direction, mirror_to)
            prop_obj.set_interface_mirror(interface_mirror)
            tap.set_virtual_machine_interface_properties(prop_obj)
            tap = vnc.virtual_machine_interface_update(tap)
        else:
            mirror_to = interface_mirror.get_mirror_to()
            self.logger.info("interface_mirror obj already present")
    # end enable_intf_mirrroing

    def disable_intf_mirroring(self, vnc, tap):
        prop_obj = tap.get_virtual_machine_interface_properties()
        if not prop_obj:
            self.logger.info("interface_mirror not enabled")
        else:
            self.logger.info("interface_mirror enabled..disabling it..")
            prop_obj.set_interface_mirror(None)
            tap.set_virtual_machine_interface_properties(prop_obj)
            tap = vnc.virtual_machine_interface_update(tap)
    # end disable_intf_mirrroing

    def verify_intf_mirroring_scale_number(self):

        compute_nodes = self.get_compute_nodes(0, 1, 2)
        src_compute = compute_nodes[0]
        analyzer_compute = compute_nodes[1]
        dst_compute = compute_nodes[2]
        analyzer_port = 8099
        vn_fixtures = []
        vn_objs = []
        image_name = 'ubuntu'

        # Agent restart to avoid stale entries in 'mirror --dump' output
        self.inputs.restart_service('contrail-vrouter-agent', [src_compute], container='agent')
        cluster_status, error_nodes = ContrailStatusChecker().wait_till_contrail_cluster_stable(nodes=[src_compute])
        assert cluster_status, 'Hash of error nodes and services : %s' % (error_nodes)

        # Create 51 VNs
        for count in range(1,52):
            vn_subnet = [get_random_cidr(af=self.inputs.get_af())]
            vn_fq_name = self.connections.domain_name +":"  + self.inputs.project_name + \
                        ":" + get_random_name("src_vn_%s" %count)
            vn_name = vn_fq_name.split(':')[2]
            self.vn_fixture = self.config_vn(vn_name, vn_subnet)
            vn_fixtures.append(self.vn_fixture)
            vn_objs.append(self.vn_fixture.obj)

            if count == 1:

                # Configure analyzer_vm and dest_vm in first VN
                vn_obj = [self.vn_fixture.obj]
                analyzer_vm_name = get_random_name("analyzer_vm")
                routing_instance = vn_fq_name + ':' + vn_name
                analyzer_vm_fixture = self.create_vm(vn_objs=vn_obj, vm_name=analyzer_vm_name,
                            image_name=image_name, node_name=analyzer_compute)
                sleep(10)
                assert analyzer_vm_fixture.verify_on_setup()
                self.nova_h.wait_till_vm_is_up(analyzer_vm_fixture.vm_obj)
                analyzer_ip_address = analyzer_vm_fixture.get_vm_ips(vn_fq_name)[0]

                dst_vm_name = get_random_name("dst_vm")
                dst_vm_fixture = self.create_vm(vn_objs=vn_obj, vm_name=dst_vm_name,
                            image_name=image_name, node_name=dst_compute)
                sleep(10)
                assert dst_vm_fixture.verify_on_setup()
                self.nova_h.wait_till_vm_is_up(dst_vm_fixture.vm_obj)

        # Create 51 Sub interface VMIs and Enable Interface mirroring on that
        sub_vn_subnet = [get_random_cidr(af=self.inputs.get_af())]
        sub_vn_fq_name = self.connections.domain_name +":"  + self.inputs.project_name + \
                        ":" + get_random_name("sub_vn")
        sub_vn_name = sub_vn_fq_name.split(':')[2]
        self.sub_vn_fixture = self.config_vn(sub_vn_name, sub_vn_subnet)

        intf_type = 'src'
        vlan_range = range(2001, 2052)
        sub_port, sub_parent_port, sub_parent_port_vn_fixture = self.create_sub_intf_scale(self.sub_vn_fixture.uuid, \
                                                                         intf_type, vlan_range)
        sub_port_ids=[]
        sub_port_ids.append(sub_parent_port.uuid)
        sub_vn_objs = [sub_parent_port_vn_fixture.obj]
        sub_vm_name = get_random_name("sub_vm")

        sub_vm_fixture = self.create_vm(vn_objs=sub_vn_objs, vm_name=sub_vm_name,
            image_name=image_name, node_name=src_compute, port_ids=sub_port_ids)

        total_mirror_entries_before_test=self.inputs.run_cmd_on_server(sub_vm_fixture.vm_node_ip, \
                                                        "contrail-tools mirror --dump | wc -l")

        assert sub_vm_fixture.verify_on_setup()
        self.nova_h.wait_till_vm_is_up(sub_vm_fixture.vm_obj)
        count = 1
        for sport in sub_port:
            analyzer_name='tap'+'-'+'sub'+'-'+str(count)
            self.config_scale_intf_mirroring(sub_vm_fixture, analyzer_ip_address, analyzer_name, \
                    routing_instance, src_port=sport, sub_intf=True)
            count = count+1

        # Create four VM with 51 VMIs each, enable mirroring on all, Verify traffic gets mirrored from first VMI of each VM
        for source_vm_count in range(1,5):
            src_vm_name = get_random_name("src_vm_%s" %source_vm_count )
            src_vm_fixture = self.create_vm(vn_objs=vn_objs, vm_name=src_vm_name, image_name=image_name, node_name=src_compute)
            sleep(10)
            assert src_vm_fixture.verify_on_setup()
            self.nova_h.wait_till_vm_is_up(src_vm_fixture.vm_obj)
            self.config_scale_intf_mirroring(src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, \
                      count=source_vm_count, scale_num=51)
            if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, analyzer_vm_fixture):
                assert False, 'Intf mirroring not working on VM %s' % (source_vm_count)

        total_mirror_entries=self.inputs.run_cmd_on_server(src_vm_fixture.vm_node_ip, "contrail-tools mirror --dump | wc -l")
        total_mirror_entries= int(total_mirror_entries) - int(total_mirror_entries_before_test)

        # Verify Mirroring is enabled on 255 interace
        if  total_mirror_entries != 255:
            assert False, 'Expected total 255 mirroring entries found : %s' % (total_mirror_entries)
        else:
            self.logger.info('Found mirror entries : %s' % (total_mirror_entries))

        # Performe Agent Restart
        self.inputs.restart_service('contrail-vrouter-agent', [src_compute], container='agent')
        cluster_status, error_nodes = ContrailStatusChecker().wait_till_contrail_cluster_stable(nodes=[src_compute])
        assert cluster_status, 'Hash of error nodes and services : %s' % (error_nodes)

        assert src_vm_fixture.wait_till_vm_is_up()

        total_mirror_entries=self.inputs.run_cmd_on_server(src_vm_fixture.vm_node_ip, "contrail-tools mirror --dump | wc -l")
        total_mirror_entries= int(total_mirror_entries) - int(total_mirror_entries_before_test)

        # Verify Mirroring is enabled on 255 interace
        if  total_mirror_entries!= 255:
            assert False, 'Expected total 255 mirroring entries found : %s' % (total_mirror_entries)
        else:
            self.logger.info('Found mirror entries : %s' % (total_mirror_entries))

        # Verify traffic gets forwarded to analyzer
        if not self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, analyzer_vm_fixture):
            assert False, 'Intf mirroring not working on VM %s' % (source_vm_count)

        # Create one more VM, and configure mirroring and test traffic is not mirrored for this interface
        src_vm_name = get_random_name("src_vm_5")
        vn_obj=[]
        vn_obj.append(vn_objs[0])
        analyzer_name= "analyzer_beyond_255"
        src_vm_fixture = self.create_vm(vn_objs=vn_obj, vm_name=src_vm_name, image_name=image_name, node_name=src_compute)
        assert src_vm_fixture.verify_on_setup()
        self.nova_h.wait_till_vm_is_up(src_vm_fixture.vm_obj)

        self.config_scale_intf_mirroring(src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, \
                 agent_insp=False )

        inspect_h = self.agent_inspect[src_vm_fixture.vm_node_ip]
        mirror_entry_list = inspect_h.get_vna_mirror_entries()
        mirror_entry_name_list=mirror_entry_list[0].xpath("//analyzer_name")

        for entry in mirror_entry_name_list:
            name=etree.tostring(entry, encoding='unicode')
            if analyzer_name in name:
                assert False, 'Mirror Entry should not be present in Agent, when configured for more than 255 interaces'

        # Verify traffic should not forwarded to analyzer
        if self.verify_port_mirroring(src_vm_fixture, dst_vm_fixture, analyzer_vm_fixture, mirror = False):
            assert False, 'Intf mirroring should not work when configured for 255th VM: %s' % (source_vm_count)

    def create_sub_intf_scale(self, vn_fix_uuid, intf_type, vlan_range, mac_address=None):

        parent_port_vn_subnets = [get_random_cidr(af=self.inputs.get_af())]
        parent_port_vn_name = get_random_name( intf_type + "_parent_port_vn")
        parent_port_vn_fixture = self.config_vn(parent_port_vn_name, parent_port_vn_subnets)
        parent_port = self.setup_vmi(parent_port_vn_fixture.uuid)
        mac_address = parent_port.mac_address
        vlan_port = []

        for vlan in vlan_range:
            port = self.setup_vmi(vn_fix_uuid,
                                           parent_vmi=parent_port.vmi_obj,
                                           vlan_id=vlan,
                                           api_type='contrail',
                                           mac_address=mac_address)
            vlan_port.append(port.vmi_obj)

        return vlan_port, parent_port, parent_port_vn_fixture

    def config_scale_intf_mirroring(self, src_vm_fixture, analyzer_ip_address, analyzer_name, routing_instance, \
                src_port=None, sub_intf=False, nh_mode = 'dynamic', direction = 'both', \
                analyzer_mac_address = '', count = None, agent_insp=True, scale_num=None, ):

        vnc = src_vm_fixture.vnc_lib_h

        if sub_intf:

            tap_intf_obj = src_port
            self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = True, \
                  nh_mode = nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)

            if agent_insp:

                sleep(2)
                inspect_h = self.agent_inspect[src_vm_fixture.vm_node_ip]
                mirror_entry_list = inspect_h.get_vna_mirror_entries()
                mirror_entry_text = etree.tostring(mirror_entry_list[0], encoding='unicode')
                if analyzer_name not in mirror_entry_text:
                    result = False
                    assert False, 'Mirror entry not found in Agent Introspect for analyzer: %s' % (analyzer_name)
                else:
                    self.logger.info('Mirror Entry found in Agent Introspect for analyzer: %s' % (analyzer_name))
        else:

            if scale_num != None:

                analyzer_name_list=[]

                for i in range(0, scale_num):

                    analyzer_name='svm'+'-'+str(count)+'tap'+'-'+str(i)
                    tap_intf_uuid = src_vm_fixture.get_tap_intf_of_vm()[i]['uuid']
                    tap_intf_obj = vnc.virtual_machine_interface_read(id=tap_intf_uuid)
                    self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = True, \
                          nh_mode = nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)
                    analyzer_name_list.append(analyzer_name)

                if agent_insp:

                    inspect_h = self.agent_inspect[src_vm_fixture.vm_node_ip]
                    mirror_entry_list = inspect_h.get_vna_mirror_entries()

                    mirror_entry_name_list=mirror_entry_list[0].xpath("//analyzer_name")
                    for entry in mirror_entry_name_list:
                        analyzer_name=etree.tostring(entry, encoding='unicode')

                    for name in analyzer_name_list:
                        for entry in mirror_entry_name_list:
                            analyzer_name=etree.tostring(entry, encoding='unicode')
                            if name in analyzer_name:
                                self.logger.info('Mirror Entry found in Agent Introspect for analyzer: %s' % (name))
                                result = True
                                break
                            resutl = False
                        if result == False:
                            assert False, 'Mirror entry not found in Agent Introspect for analyzer: %s' % (name)
            else:

                tap_intf_uuid = src_vm_fixture.get_tap_intf_of_vm()[0]['uuid']
                tap_intf_obj = vnc.virtual_machine_interface_read(id=tap_intf_uuid)

                self.enable_intf_mirroring(vnc, tap_intf_obj, analyzer_ip_address, analyzer_name, routing_instance, header = True, \
                    nh_mode = nh_mode, direction = direction, analyzer_mac_address = analyzer_mac_address)

                name = analyzer_name
                if agent_insp:
                    inspect_h = self.agent_inspect[src_vm_fixture.vm_node_ip]
                    mirror_entry_list = inspect_h.get_vna_mirror_entries()
                    mirror_entry_name_list=mirror_entry_list[0].xpath("//analyzer_name")
                    for entry in mirror_entry_name_list:
                        analyzer_name=etree.tostring(entry, encoding='unicode')
                        if name in analyzer_name:
                            self.logger.info('Mirror Entry found in Agent Introspect for analyzer: %s' % (name))
                            result = True
                            break
                        resutl = False
                    if result == False:
                        assert False, 'Mirror entry not found in Agent Introspect for analyzer: %s' % (name)

    def cleanUp(self):
        super(VerifyIntfMirror, self).cleanUp()
