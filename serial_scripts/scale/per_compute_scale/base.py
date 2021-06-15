from common.base import GenericTestBase
from vnc_api.vnc_api import *
from tcutils.util import get_random_cidr, run_cmd_on_server, retry
from compute_node_test import ComputeNodeFixture
from tcutils.agent.vna_introspect_utils import AgentInspect
from tcutils.traffic_utils.hping_traffic import Hping3
from contrailapi import ContrailVncApi
from common import log_orig as contrail_logging
import random
import datetime
import re
import logging as LOG

VROUTER_INTF_LIMIT = 4352
PRE_EXIST_INTF = 5   # pre-existing intfs: host-intf, vhost0, pkt0, pkt1, pkt3
VRF_LIMIT = 4096
MAX_RULES_PER_NP = 1000
FLOW_TIMEOUT=60*3
FLOW_THREADS=4
TOOLS_CONTAINER='tools'

class BaseComputeScale(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        contrail_logging.getLogger('introspect', log_to_console=False,
                                    max_message_size='10240',
                                    level=LOG.WARNING)
        super(BaseComputeScale, cls).setUpClass()
        cls.api_helper = ContrailVncApi(cls.vnc_lib, _log=cls.logger)
        cls._inspect = {}
        for ip in cls.inputs.compute_ips:
            cls.setup_compute_for_scale(ip)

    @classmethod
    def setup_compute_for_scale(cls, ip):
        compute = ComputeNodeFixture(cls.connections, ip)
        compute.set_flow_aging_time(FLOW_TIMEOUT)
        compute.set_flow_thread_count(FLOW_THREADS)
        cfg = cls.inputs.contrail_configs
        image = "%s/contrail-tools:%s" % (cfg['CONTAINER_REGISTRY'],
                                          cfg['CONTRAIL_VERSION'])
        cmd = "docker run -id --entrypoint bash "
        cmd += " --name %s " % TOOLS_CONTAINER
        cmd += "-v /etc/contrail:/etc/contrail:ro -v /etc/hosts:/etc/hosts:ro "
        cmd += "-v /etc/localtime:/etc/localtime:ro -v /var/run:/var/run "
        cmd += "-v /dev:/dev -v /var/lib/containers:/var/lib/containers "
        cmd += "--pid host --net host --privileged "
        cmd += image
        compute.execute_cmd(cmd, container=None)

    def setUp(self):
        super(BaseComputeScale, self).setUp()
        self.vns = []
        self.vn_ids = []
        self.vms = []
        self.sgs = []
        self.nps = []
        self.seq_map = {}
        self.vn_nps_map = {}
        self.vmi_sgs_map = {}
        self.cleanup_added = False

    def delete_security_groups(self):
        sgs = self.sgs
        self.sgs = []
        for sg in sgs:
            self.logger.info('deleteing ' + sg.name)
            try:
                self.vnc_lib.security_group_delete(id=sg.uuid)
            except Exception as err:
                self.logger.warn('error while deleting {}'.format(sg.name))
                self.logger.warn(err)

    def delete_network_policys(self):
        nps = self.nps
        self.nps = []
        for np in nps:
            self.logger.info('deleteing ' + np.name)
            try:
                self.vnc_lib.network_policy_delete(id=np.uuid)
            except Exception as err:
                self.logger.warn('error while deleting {}'.format(sg.name))
                self.logger.warn(err)

    def delete_networks(self, start=None, end=None):
        start = 0 if start == None else start
        end = len(self.vns) if end == None else end
        vns = self.vns[start:end]
        for vn in vns:
            vn.cleanUp()
            self.remove_from_cleanups(vn.cleanUp)
        self.vns = self.vns[0:start] + self.vns[end: -1]

    def clear_np_on_vns(self):
        self.seq_map = {}
        self.vn_nps_map = {}
        for vn in self.vns:
            vn.unbind_policies()
        self._verify_np_rules_on_agent(self.vns)

    def clear_sg_on_vms(self, vms=None):
        vms = vms or self.vms
        for vm in vms:
            vm.disassociate_security_groups()
        ret, _ = self._verify_sgs_on_vmi(self.vms, [])
        if not ret:
            for vm in vms:
                vm.disassociate_security_groups()
            self._verify_sgs_on_vmi(self.vms, [])

    def _cleanup(self):
        self.clear_sg_on_vms()
        self.delete_security_groups()
        self.clear_np_on_vns()
        self.delete_network_policys()

    def _add_cleanup(self):
        if not self.cleanup_added:
            self.addCleanup(self._cleanup)
            self.cleanup_added = True

    def _create_np_rule(self,
                      src_addr, dst_addr,
                      src_port_min, src_port_max,
                      dst_port_min, dst_port_max,
                      proto='any'):
        return PolicyRuleType(direction='<>', protocol=proto,
                              src_addresses=[src_addr],
                              dst_addresses=[dst_addr],
                              src_ports=[PortType(src_port_min,
                                                  src_port_max)],
                              dst_ports=[PortType(dst_port_min,
                                                  dst_port_max)],
                              action_list={'simple_action': 'pass'})

    def _create_np(self, name, rules):
        np = NetworkPolicy(name=name, parent_obj=self.project.project_obj,
                           network_policy_entries=PolicyEntriesType(rules))
        np_id = self.vnc_lib.network_policy_create(np)
        assert np_id, 'unable to create np ' + name
        self.logger.info('created NP:%s (%s) ' %(name, np_id))
        return np_id, self.vnc_lib.network_policy_read(id=np_id)

    def _create_pairs(self, lst, tgt=None):
        if tgt:
            firsts = [tgt] * len(lst)
            return zip(firsts, lst)

        ret = []
        firsts = lst[:]
        while firsts:
            no1 = firsts.pop(0)
            if len(firsts):
                pairs = [[no1, x] for x in firsts]
                ret.extend(pairs)
        return ret

    def _bind_policy(self, vn_fix, policy_obj):
        if self.seq_map.get(vn_fix.vn_name, None):
            self.seq_map[vn_fix.vn_name] += 1
            self.vn_nps_map[vn_fix.vn_name].append(policy_obj)
        else:
            self.seq_map[vn_fix.vn_name] = 1
            self.vn_nps_map[vn_fix.vn_name] = [policy_obj]
        vn_obj = self.vnc_lib.virtual_network_read(id=vn_fix.uuid)
        vn_obj.add_network_policy(policy_obj,
                VirtualNetworkPolicyType(sequence=SequenceType(
                  major=self.seq_map[vn_fix.vn_name], minor=0)))
        self.vnc_lib.virtual_network_update(vn_obj)

    def _create_np_rules_combo(self, vn1, vn2, port_partition=1):
        rules = []
        port_step = 65536//port_partition
        for p in range(0, 65535, port_step):
            d_p = p + port_step - 1
            d_p = 65535 if d_p > 65535 else d_p
            rules.append(self._create_np_rule(
                            AddressType(virtual_network=vn1.vn_fq_name),
                            AddressType(virtual_network=vn2.vn_fq_name),
                            -1, -1, p, d_p))
        return rules

    def create_network_policys(self, tgt=None, vns=None, start_index=1,
                                name_prefix='NP', port_partition=1,
                                verify=True):
        if type(vns) == list and len(vns) < 2 and not tgt:
            self.logger.error('at least two vns required for network-policy')
            return
        vns = vns or self.vns
        self._add_cleanup()
        try:
            for vn1, vn2 in self._create_pairs(vns, tgt=tgt):
                rules = self._create_np_rules_combo(vn1, vn2,
                            port_partition=port_partition)
                np_id, np_obj = self._create_np(
                            name_prefix + str(start_index), rules)
                self._bind_policy(vn1, np_obj)
                self._bind_policy(vn2, np_obj)
                self.nps.append(np_obj)
                start_index += 1
        except Exception as e:
            self.logger.error(e)
        self.logger.info('RESULTS:NP %d' % len(self.nps))
        if verify:
            ret, msg = self._verify_np_rules_on_agent(vns)
            assert ret, msg
        self.logger.info('all np acls sycned to agent')

    def _create_sg_rule(self, direction, cidr, port_min, port_max, proto,
                        ether_type='IPv4'):
        if direction == 'ingress':
            src_addr = AddressType(subnet=SubnetType('0.0.0.0', 0))
            dst_addr = AddressType(security_group='local')
        else:
            subnet, mask = cidr.split('/')
            dst_addr = AddressType(subnet=SubnetType(subnet, mask))
            src_addr = AddressType(security_group='local')
        return PolicyRuleType(direction='>',
                       protocol=proto,
                       src_addresses=[src_addr],
                       dst_addresses=[dst_addr],
                       dst_ports=[PortType(port_min, port_max)],
                       ethertype=ether_type)

    def _create_sg(self, name, rules):
        sg = SecurityGroup(name=name, parent_obj=self.project.project_obj,
                           security_group_entries=PolicyEntriesType(rules))
        sg_id = self.vnc_lib.security_group_create(sg)
        assert sg_id, 'unable to create sg ' + name
        self.logger.info('created SG:%s (%s) ' % (name, sg_id))
        return sg_id, self.vnc_lib.security_group_read(id=sg_id)

    def _create_sg_rules_combo(self, cidrs=None, protos=None,
                            port_partition=1, port_range=None,
                            direction='egress', nr_rules=None):
        cidrs = cidrs or ['0.0.0.0/0']
        protos = protos or ['any']
        port_step = 65536//port_partition
        if nr_rules:
            p = random.randint(0, 65535 - nr_rules)
            port_range = (p, p + nr_rules, 1)
        rules = []
        for cidr in cidrs:
            for proto in protos:
                if port_range:
                    for p in range(port_range[0], port_range[1],
                                    port_range[2]):
                        dp = p + port_range[2]  - 1
                        dp = port_range[1] if dp > port_range[1] else dp
                        rules.append(self._create_sg_rule(direction, cidr,
                                                      p, dp, proto))
                else:
                    for p in range(0, 65535, port_step):
                        d_p = p + port_step - 1
                        d_p = 65535 if d_p > 65535 else d_p
                        rules.append(self._create_sg_rule(direction, cidr,
                                                          p, d_p, proto))
        return rules

    def create_security_groups(self, cidrs=None, start_index=1,
                               name_prefix='SG', protos=None, port_partition=1,
                               port_range=None, nr_rules=None):
        self._add_cleanup()
        cidrs = cidrs or ['0.0.0.0/0']
        try:
            for cidr in cidrs:
                rules = [self._create_sg_rule('ingress', None,
                                0, 65535, 'any')]
                rules.extend(self._create_sg_rules_combo(direction='egress',
                                            cidrs=[cidr],
                                            protos=protos,
                                            port_partition=port_partition,
                                            port_range=port_range,
                                            nr_rules=nr_rules))
                sg_id, sg_obj = self._create_sg(
                            name_prefix + str(start_index), rules)
                start_index += 1
                self.sgs.append(sg_obj)
        except Exception as err:
            self.logger.warn(err)
        self.logger.info('RESULTS: SG {}'.format(len(self.sgs)))

    def apply_sg_to_vmi(self, vmi, sg):
        self.api_helper.add_security_group(vmi_id=vmi, sg_id=sg.uuid)
    
        vmi = self.vnc_lib.virtual_machine_interface_read(id=vmi)
        for item in vmi.virtual_machine_interface_bindings.get_key_value_pair():
            if item.key == 'host_id':
                compute = item.value
                break
    
        ret, msg = self._verify_sgs_sync_to_agent(self.sgs, compute)
        assert ret, msg
        self.logger.info('{} SG synced to agent'.format(len(self.sgs)))

        ret, msg = self._verify_sg_rules_on_agent([sg], compute)
        assert ret, msg
        self.logger.info('all sgs rules synced to compute')

    def apply_sgs_to_vmi(self, vmi, sgs):
        if vmi not in self.vmi_sgs_map:
            self.vmi_sgs_map[vmi] = sgs
        else:
            self.vmi_sgs_map[vmi].extend(sgs)
        self.api_helper.set_security_group(vmi_id=vmi, sg_ids=[], sgs=[])
        self._verify_sgs_on_vmi(vmi=vmi)
        self.api_helper.set_security_group(vmi_id=vmi,
                sgs=self.vmi_sgs_map[vmi])

        obj = self.vnc_lib.virtual_machine_interface_read(id=vmi)
        for item in obj.virtual_machine_interface_bindings.get_key_value_pair():
            if item.key == 'host_id':
                compute = item.value
                break
    
        ret, msg = self._verify_sgs_sync_to_agent(self.sgs, compute)
        assert ret, msg
        self.logger.info('{} SG synced to agent'.format(len(self.sgs)))

        ret, msg = self._verify_sg_rules_on_agent(self.vmi_sgs_map[vmi],
                            compute)
        assert ret, msg
        self.logger.info('all sgs rules synced to compute')

    def fetch_vmis(self, vms=None):
        vms = vms or self.vms
        vmis = []
        for vm in vms:
            vmis.extend(list(vm.get_vmi_ids().values()))
        return vmis

    @retry(tries=120, delay=10)
    def _verify_np_rules_on_agent(self, vns):
        for vn in vns:
            vn_obj = self.vnc_lib.virtual_network_read(id=vn.uuid)
            vmis = vn_obj.get_virtual_machine_interface_back_refs()
            if not vmis:
                return True, None
            vmi = vmis[0]['uuid']
            vmi = self.vnc_lib.virtual_machine_interface_read(id=vmi)
            for item in vmi.virtual_machine_interface_bindings.get_key_value_pair():
                if item.key == 'host_id':
                    compute = item.value
                    break
            inspect = self.agent_inspect[compute]
            expected = 0
            for np in self.vn_nps_map.get(vn.vn_name, []):
                expected += len(np.get_network_policy_entries().policy_rule)
            expected *= 2 # 1 rule for each direction
            acl_dict = inspect.get_vna_acl_by_vn(vn.vn_fq_name)
            acls = len(acl_dict['entries']) if acl_dict else 0
            self.logger.info('{} np acl expected:{} seen:{}'.format(
                    vn.vn_name, expected, acls))
            if expected == 0 and acls != 0:
                return False, 'acl on vn {} not cleared {}'.format(
                    vn.vn_name, acls)
            if acls < expected:
                return False, 'acls on vn {} expected {} seen {}'.format(
                    vn.vn_name, expected, acls)
        return True, None

    @retry(tries=120, delay=5)
    def _verify_sgs_sync_to_agent(self, sgs, compute):
        inspect = self.agent_inspect[compute]
        expected = len(sgs)
        seen = len(inspect.get_sg_list())
        self.logger.info('sg on compute expected:{} seen:{}'.format(
                            expected, seen))
        return expected == seen, "SG: expected {} seen {}".format(
                            expected, seen)

    @retry(tries=120, delay=5)
    def _verify_sgs_on_vmi(self, vms=None, sgs=None, vmi=None):
        expected = len(sgs or [])
        if vmi:
            obj = self.vnc_lib.virtual_machine_interface_read(id=vmi)
            for item in obj.virtual_machine_interface_bindings.get_key_value_pair():
                if item.key == 'host_id':
                    compute = item.value
                    break
            inspect = self.agent_inspect[compute]
            intf = inspect.get_vna_tap_interface_by_vmi(vmi)[0]
            seen = len(intf['sg_uuid_list'])
            self.logger.info('vmi:{}, has {} sgs'.format(vmi, seen))
            if seen != expected:
                return False, 'vmi:{} seen:{} expected{} sgs'.format(
                                   vmi, expected, seen)
            return True, None

        for vm in vms:
            inspect = self.agent_inspect[vm.get_host_of_vm()]
            for intf in inspect.get_vna_tap_interface_by_vm(vms[0].vm_id):
                seen = len(intf['sg_uuid_list'])
                self.logger.info('vm:{}, has {} sgs'.format(vm.name, seen))
                if seen != expected:
                    return False, 'vm:{} seen:{} expected{} sgs'.format(
                                   vm.vm_name, expected, seen)
        return True, None

    @retry(tries=120, delay=5)
    def _verify_sg_rules_on_agent(self, sgs, compute):
        inspect = self.agent_inspect[compute]
        for sg in sgs:
            expected = len(sg.get_security_group_entries().policy_rule)
            seen = 0
            try:
                acls = inspect.get_sg_acls_list(sg.uuid)
            except:
                acls = []
            for acl in acls:
                seen += len(acl['entries'])
            self.logger.info("SG {} expected rules: {} seen {}".format(
                                   sg.name, expected, seen))
            if seen != expected:
                return False, "SG {} expected rules: {} seen {}".format(
                                   sg.name, expected, seen)
        return True, None

    def apply_sgs_to_vms(self, vms=None, sgs=None):
        sgs = sgs or self.sgs
        vms = vms or self.vms
        for vm in vms:
            self.api_helper.set_security_group(vm.vm_id, sgs=sgs)

        ret, msg = self._verify_sgs_sync_to_agent(sgs, vms[0].get_host_of_vm())
        assert ret, msg
        self.logger.info('{} SG synced to agent'.format(len(sgs)))

        ret, msg = self._verify_sgs_on_vmi(vms, sgs)
        assert ret, msg
        self.logger.info('all sgs applied on all vms')

        ret, msg = self._verify_sg_rules_on_agent(sgs, vms[0].get_host_of_vm())
        assert ret, msg
        self.logger.info('all sgs rules synced to compute')

    def create_networks(self, nr, start_index=1, name_prefix='VN'):
        try:
            for i in range(start_index, start_index + nr):
                vn_fixture = self.create_vn(vn_name=name_prefix + str(i),
                                  vn_subnets=[get_random_cidr(mask=16)])
                vn_fixture.read()
                self.logger.info("created VN: %s (%s)"%(vn_fixture.vn_name,
                        vn_fixture.uuid))
                self.vns.append(vn_fixture)
                self.vn_ids.append(vn_fixture.uuid)
        except Exception as e:
            self.logger.error(e)
        self.logger.info('RESULTS:VN %d' % len(self.vn_ids))

    def create_virtual_machines(self, vns=None, start_index=1,
                                name_prefix='VM',
                                image='cirros-traffic'):
        vns = vns or self.vns
        for vn in vns:
            try:
                vm_fixture = self.create_vm(vn_fixture=vn,
                                  image_name=image,
                                  vm_name=name_prefix + str(start_index))
                self.logger.info('created VM: %s (%s)' % (vm_fixture.vm_name,
                                    vm_fixture.vm_id))
                start_index += 1
                assert vm_fixture.wait_till_vm_is_up()
                self.vms.append(vm_fixture)
            except Exception as e:
                 self.logger.error("RESULTS:created %d VMs" % len(self.vms))
                 vm_fixture.delete(force=True)
                 self.remove_from_cleanups(vm_fixture)
                 raise e
        self.logger.info("RESULTS:created %d VMs" % len(self.vms))

    @retry(delay=30, tries=5)
    def _wait_for_vm(self, vm):
        return vm.wait_till_vm_is_active()

    def create_virtual_machines_multi_intf(self, nr, start_index=1,
                                vns=None,
                                name_prefix='VM',
                                image='cirros-traffic',
                                compute=None,
                                ping_test=False):
        vns = vns or self.vns
        vn_ids = [vn.uuid for vn in vns]
        #cmd1 = []
        #cmd2 = []
        #for i in range(1, len(vns)):
        #    cmd1.append('echo "auto eth%d" >> /etc/network/interfaces && echo "iface eth%d inet dhcp" >> /etc/network/interfaces'%(i,i))
        #    cmd2.append('ifdown eth%d && ifup eth%d'%(i,i))

        for _ in range(nr):
            try:
                vm_fixture = self.create_vm(image_name=image,
                                  node_name=compute, vn_ids=vn_ids,
                                  vm_name=name_prefix + str(start_index))
                self.logger.info('created VM: %s (%s)' % (vm_fixture.vm_name,
                                    vm_fixture.vm_id))
                start_index += 1
                self.sleep(len(vns))
                assert self._wait_for_vm(vm_fixture)
                #assert vm_fixture.wait_till_vm_is_up()
                #vm_fixture.run_cmd_on_vm(cmds=cmd1, as_sudo=True)
                #vm_fixture.run_cmd_on_vm(cmds=cmd2, as_sudo=True)
                if len(self.vms) and ping_test:
                    dst = random.choice(self.vms)
                    assert vm_fixture.ping_with_certainty(
                           dst_vm_fixture=dst),'Ping failed'
                self.vms.append(vm_fixture)
            except Exception as e:
                 self.logger.error("RESULTS:created %d VMs" % len(self.vms))
                 vm_fixture.delete(force=True)
                 self.remove_from_cleanups(vm_fixture)
                 raise e
        self.logger.info("RESULTS:created %d VMs" % len(self.vms))

    def run_hping(self, src, tgts, msg, base_port_range,
                tgt_flow_count=100000, udp=True, wait_time=180):
        self.logger.info("*" * 40)
        self.logger.info(msg)
        count = 1024 * 1024
        interval = 'u1'
        destport = '++1000'
        ip = self.inputs.host_data[src.get_host_of_vm()]['host_ip']
        compute = ComputeNodeFixture(self.connections, ip)
        flow_file = '/tmp/flowr.txt'
        run_cmd_on_server("timeout %d flow -r > %s" % (wait_time, flow_file),
                          compute.ip,
                          compute.username, compute.password,
                          detach=True,
                          container=TOOLS_CONTAINER,
                          logger=self.logger)
        hpings = []
        tgt = tgts[0]
        for base_port in range(base_port_range[0], base_port_range[1]):
            tgt_ip = tgt.get_vm_ips()[0]
            hping_h = Hping3(src, tgt_ip, udp=udp, keep=True,
                         destport=destport, baseport=base_port,
                         interval=interval)
            hping_h.start(wait=False)
            hpings.append(hping_h)
        self.logger.info('Running hping command')
        self.sleep(30)
        for hping_h in hpings:
            (stats, hping_log) = hping_h.stop()
        while compute.execute_cmd("pidof flow", container=None):
            self.sleep(5)
        flow_records = run_cmd_on_server("cat %s" % flow_file,
                            compute.ip,
                            compute.username, compute.password,
                            container=TOOLS_CONTAINER,
                            logger=self.logger)
        return self._get_time_taken(flow_records, tgt_flow_count)

    def _get_time_taken(self, records, tgt):
        start_time = None
        for rec in records.split('\n'):
            m = re.match(r'.*? ([\d]+):([\d]+):([\d]+)\.([\d]+):[ ]* Entries =[ ]* ([\d]+) .*',
                     rec, re.M|re.I) 
            if not start_time and int(m.group(5)) > 100:
                start_time = datetime.timedelta(hours=int(m.group(1)),
                                   minutes=int(m.group(2)),
                                   seconds=int(m.group(3)),
                                   milliseconds=int(m.group(4)))
                start_entries = int(m.group(5))
                self.logger.info('START {} {}'.format(start_time,
                                                start_entries))
            elif start_time and \
                    int(m.group(5)) - start_entries > tgt:
                stop_time = datetime.timedelta(hours=int(m.group(1)),
                                   minutes=int(m.group(2)),
                                   seconds=int(m.group(3)),
                                   milliseconds=int(m.group(4)))
                stop_entries = int(m.group(5))
                self.logger.info('END {} {}'.format(stop_time, stop_entries))
                break
        assert start_time and stop_time, 'Unable to parse flow records'
        tt = stop_time - start_time
        nr_flows = stop_entries - start_entries
        self.logger.info("RESULTS: {} flows in {}".format(nr_flows, tt))
        self.logger.info("*" * 40)
        return tt, nr_flows
