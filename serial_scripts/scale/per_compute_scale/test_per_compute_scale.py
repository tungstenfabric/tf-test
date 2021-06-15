from .base import *
from tcutils.wrappers import preposttest_wrapper

class TestPerComputeScale(BaseComputeScale):

    @preposttest_wrapper
    def test_max_rules_per_sg(self):
        '''
        Verify maximum number of rules per security-group
        1. create a VN & launch a VM on it
        2. fetch the VMI of the VM
        3. clear any Security-Groups applied on the VMI
        4. create a Security-Group with 1000 rules & apply to VMI
        5. verify on the agent, that the Security-Group & its rules are synced to agent
        6. delete the Security-Group & iterate with larger number of rules
        '''
        self.create_networks(nr=1)
        self.create_virtual_machines()
        self.clear_sg_on_vms()
        max_rules = 0
        min_rules = 1000
        last_tested = 1300
        for nr in range(min_rules, 2000, 100):
            try:
                self.create_security_groups(port_range=[0,nr,1])
                self.apply_sgs_to_vms()
                max_rules = len(self.sgs[0].get_security_group_entries().policy_rule)
                self.clear_sg_on_vms()
                self.delete_security_groups()
            except Exception as err:
                self.logger.warn(err)
                break
        self.logger.info('SCALE-RESULTS: max %d rules per sg' % max_rules)
        assert max_rules >= min_rules, \
               'failed to achieve %d rules per sg' % min_rules
        assert max_rules >= last_tested, \
               'failed last tested max %d rules per sg' % last_tested

    @preposttest_wrapper
    def test_max_rules_per_np(self):
        '''
        Verify maximum number of rules per network-policy
        1. create a two VN & launch one VM on each
        2. create Network-Policy with 1000 rules & associate it with both VNs
        3. verify on agent, that rules from Network-Policy is complied into an ACL with expected number of rules & applied to the VN
        4. delete Network-Policy & iterate with larger number of rules
        '''
        self.create_networks(nr=2)
        self.create_virtual_machines()
        max_rules = 0
        min_rules = 1000
        last_tested = 1200
        for nr in range(min_rules, 2000, 100):
            try:
                self.create_network_policys(port_partition=nr)
                max_rules = len(self.nps[0].get_network_policy_entries().policy_rule)
                self.clear_np_on_vns()
                self.delete_network_policys()
            except Exception as err:
                self.logger.warn(err)
                break
        self.logger.info('SCALE-RESULTS: max %d rules per np' % max_rules)
        assert max_rules >= min_rules, \
               'failed to achieve %d rules per np' % min_rules
        assert max_rules >= last_tested, \
               'failed last tested max %d rules per np' % last_tested

    @preposttest_wrapper
    def test_max_sgs_per_vrouter(self):
        '''
        Verify maximum number of security-groups per vrouter
        1. launch VNs & VM with interface on all VNs
        2. create unique SG per VMI, with 1000 rules
        3. verify that the SG & its rules sync to agent
        4. iteratively add SGs on the VMI and record the maximum number of SGs
        5. iterate steps 2-4 for SG with 200 rules
        '''
        VN_NOS=10
        #MAX_VM_NOS = (VROUTER_INTF_LIMIT - PRE_EXIST_INTF) // VN_NOS
        #MAX_VM_NOS = min(MAX_VM_NOS, VRF_LIMIT // VN_NOS)
        compute = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        for i in range(1):
            idx = len(self.vns)
            self.create_networks(nr=VN_NOS, start_index=idx+1)
            self.logger.info("CHECK: VNS: {}".format(len(self.vns)))
            self.create_virtual_machines_multi_intf(nr=1,
                    compute=compute, start_index=i+1,
                    vns=self.vns[idx:])
            self.logger.info("CHECK: VMS: {}".format(len(self.vms)))

        def get_max_sgs_per_vrouter(test, nr_rules, sgs_per_iter=10):
            ret = 0
            try:
                while True:
                    for vmi in test.vmis:
                        cidrs = [get_random_cidr() for _ in range(sgs_per_iter)]
                        test.create_security_groups(start_index=ret + 1,
                            port_partition=nr_rules, cidrs=cidrs)
                        test.apply_sgs_to_vmi(vmi, self.sgs[ret:])
                        ret = len(test.sgs)
            except Exception as err:
                test.logger.warn(err)
            self.vmi_sgs_map = {}
            test.clear_sg_on_vms()
            test.delete_security_groups()
            test.logger.info('SCALE-RESULTS: max %d sgs (%d rules) per vrouter' % (ret,
                                nr_rules))
            return ret

        self.clear_sg_on_vms()
        self.vmis = self.fetch_vmis()

        failures = []
        expected = 1000
        nr_rules = 1000
        got = get_max_sgs_per_vrouter(self, nr_rules)
        if got < expected:
            failures.append('failed to achieve %d sg (%d rules) per vrouter' % (
                        expected, nr_rules))

        self.sleep(60 * 10)
        expected = 1
        nr_rules = 200
        got = get_max_sgs_per_vrouter(self, nr_rules)
        if got < expected:
            failures.append('failed to achieve %d sg (%d rules) per vrouter' % (
                        expected, nr_rules))

        if failures:
            self.logger.warn(failures)
        return False if failures else True

    @preposttest_wrapper
    def test_max_nps_per_vn(self):
        '''
        Verify maximum number of network-policys per virtual-network
        1. create a VN (VN1) & launch a VM on it
        2. iteratively launch VNs and setup Network-Policys between VN1 & other VNs
        3. verify that all Network-Policys are complied into ACL with expected number of rules on the agent
        4. execute step 3 & 4 for 1, 10, 20, 50, 100, 200, 500 & 1000 rules per Network-Policy
        '''
        self.create_networks(nr=1)
        self.create_virtual_machines()

        def get_max_nps_per_vn(test, nr_rules, min_nps, max_nps, step):
            ret = 0
            for nr in range(min_nps, max_nps, step):
                idx = len(test.vns)
                try:
                    test.create_networks(
                            name_prefix='VN' + str(nr_rules) + 'R',
                            start_index=idx, nr=nr - idx + 1)
                    test.create_network_policys(start_index=idx, tgt=test.vns[0],
                            vns=test.vns[idx:], port_partition=nr_rules)
                    ret = len(test.nps)
                except Exception as err:
                    test.logger.warn(err)
                    break
            test.logger.info('SCALE-RESULTS: max %d nps (%d rules) per vn' % (ret,
                                nr_rules))
            test.clear_np_on_vns()
            test.delete_network_policys()
            test.delete_networks(start=1)
            return ret

        failures = []
        expected = 1000
        nr_rules = 1
        got = get_max_nps_per_vn(self, nr_rules, 500, 2000, 100)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 10
        expected = 100
        got = get_max_nps_per_vn(self, nr_rules, 100, 150, 10)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 20
        expected = 50
        got = get_max_nps_per_vn(self, nr_rules, 50, 100, 10)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 50
        expected = 20
        got = get_max_nps_per_vn(self, nr_rules, 20, 100, 10)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 100
        expected = 10
        got = get_max_nps_per_vn(self, nr_rules, 10, 50, 1)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 200
        expected = 5
        got = get_max_nps_per_vn(self, nr_rules, 5, 50, 1)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 500
        expected = 2
        got = get_max_nps_per_vn(self, nr_rules, 2, 10, 1)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        nr_rules = 1000
        expected = 1
        got = get_max_nps_per_vn(self, nr_rules, 1, 10, 1)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per vn' % (
                        expected, nr_rules))
        if failures:
            self.logger.warn(failures)
        return False if failures else True

    @preposttest_wrapper
    def test_max_nps_per_vrouter(self):
        '''
        Verify maximum number of network-policys per vrouter
        1. launch VNs & VMs
        2. setup NP with 1000 rules, between the VNs, such total number of rules on VN doesn't exceed 1000
        3. verify that the NP & its rules sync to agent
        4. iterate steps 2-3 for NP with 200 rules
        '''
        VN_NOS = 100
        NR = 5
        #MAX_VM_NOS = (VROUTER_INTF_LIMIT - PRE_EXIST_INTF) // VN_NOS
        #MAX_VM_NOS = min(MAX_VM_NOS, VRF_LIMIT // VN_NOS)
        compute = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        for i in range(NR):
            idx = len(self.vns)
            self.create_networks(nr=VN_NOS,
                        start_index=idx+1)
            self.logger.info("CHECK: VNS: {}".format(len(self.vns)))
            self.create_virtual_machines_multi_intf(nr=1,
                    compute=compute, start_index=i+1,
                    vns=self.vns[idx:])
            self.logger.info("CHECK: VMS: {}".format(len(self.vms)))

        def get_max_nps_per_vrouter(test, nr_rules):
            ret = 0
            step = (MAX_RULES_PER_NP // nr_rules) + 1
            idx = slice(0, step)
            nr_iter = (len(self.vns) // step) + 1
            max_nps = (step * (step - 1) // 2) * (len(self.vns) // step)
            try:
                for _ in range(nr_iter, 0, -1):
                    test.create_network_policys(start_index=ret + 1,
                        vns=test.vns[idx], port_partition=nr_rules)
                    ret = len(self.nps)
                    idx = slice(idx.stop, idx.stop + step)
            except Exception as err:
                test.logger.warn(err)
            test.logger.info('SCALE-RESULTS: ')
            test.logger.info('max %d nps (%d rules) per compute' % (ret,
                                nr_rules))
            test.logger.info('np cluster size %d' % step)
            test.logger.info('max np possible %d for %d vns' % (max_nps,
                                len(self.vns)))
            test.clear_np_on_vns()
            test.delete_network_policys()
            return ret

        failures = []
        expected = 250
        nr_rules = 1000
        got = get_max_nps_per_vrouter(self, nr_rules)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per compute' % (
                        expected, nr_rules))
        expected = 1200
        nr_rules = 200
        got = get_max_nps_per_vrouter(self, nr_rules)
        if got < expected:
            failures.append('failed to achieve %d np (%d rules) per compute' % (
                        expected, nr_rules))
        if failures:
            self.logger.warn(failures)
        return False if failures else True

    @preposttest_wrapper
    def test_max_nps_sgs_per_vrouter(self):
        '''
        Verify maximum number of network-policys & security-groups on vrouter
        1. launch VNs & VMs with interfaces on all the VNs
        2. create SG with 200 rules and apply iteratively on the VMIs
        3. setup NP with 200 rules, between the VNs, such total number of rules on VN doesn't exceed 1000
        4. verify that SGs & NP & thier rules are synced to agent
        '''
        VN_NOS = 100
        #MAX_VM_NOS = (VROUTER_INTF_LIMIT - PRE_EXIST_INTF) // VN_NOS
        #MAX_VM_NOS = min(MAX_VM_NOS, VRF_LIMIT // VN_NOS)
        compute = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        for i in range(5):
            idx = len(self.vns)
            self.create_networks(nr=VN_NOS,
                        start_index=idx+1)
            self.logger.info("CHECK: VNS: {}".format(len(self.vns)))
            self.create_virtual_machines_multi_intf(nr=1,
                    compute=compute, start_index=i+1,
                    vns=self.vns[idx:])
            self.logger.info("CHECK: VMS: {}".format(len(self.vms)))

        def get_max_nps_sgs_per_vrouter(test, np_rules, sg_rules, target_sgs, sgs_per_iter=10):
            nps = 0
            sgs = 0
            try:
                while sgs < target_sgs:
                    for vmi in test.vmis:
                        cidrs = [get_random_cidr() for _ in range(sgs_per_iter)]
                        test.create_security_groups(start_index=sgs + 1,
                            port_partition=sg_rules, cidrs=cidrs)
                        test.apply_sgs_to_vmi(vmi, self.sgs[sgs:])
                        sgs = len(test.sgs)
                        if sgs >= target_sgs:
                            break
            except Exception as err:
                test.logger.warn(err)

            step = (MAX_RULES_PER_NP // np_rules) + 1
            idx = slice(0, step)
            nr_iter = (len(self.vns) // step) + 1
            max_nps = (step * (step - 1) // 2) * (len(self.vns) // step)
            try:
                for _ in range(nr_iter, 0, -1):
                    test.create_network_policys(start_index=nps + 1,
                        vns=test.vns[idx], port_partition=np_rules)
                    nps = len(self.nps)
                    idx = slice(idx.stop, idx.stop + step)
            except Exception as err:
                test.logger.warn(err)

            test.logger.info('SCALE-RESULTS: max %d sgs (%d rules) per vrouter' % (sgs,
                                sg_rules))
            test.logger.info('SCALE-RESULTS: max %d nps (%d rules) per compute' % (nps,
                                np_rules))
            self.vmi_sgs_map = {}
            test.clear_sg_on_vms()
            test.delete_security_groups()
            test.clear_np_on_vns()
            test.delete_network_policys()
            return nps, sgs

        self.clear_sg_on_vms()
        self.vmis = self.fetch_vmis()
        ret = True
        expected_nps = 1200
        expected_sgs = 5000
        got_nps, got_sgs = get_max_nps_sgs_per_vrouter(self, 200, 200, 5000)
        if got_nps < expected_nps:
            self.logger.error('failed to achieve %d np per compute' % (expected_nps))
            ret = False
        if got_sgs < expected_sgs:
            self.logger.error('failed to achieve %d sg per compute' % (expected_sgs))
            ret = False
        return ret

    @preposttest_wrapper
    def test_traffic_default_sg_np(self):
        '''
        1. launch 2 VN with VM each
        2. apply default SG on VMIs & allow all NP on VNs
        3. generate 100K flow & measure time taken
        '''
        self.create_networks(nr=2)
        self.create_virtual_machines(image='ubuntu-traffic')
        self.create_network_policys()
        port = random.randint(1000, 60000)
        self.run_hping(self.vms[0], self.vms[1:],
            "test with default SG & NP", base_port_range=(port, port+10))

    @preposttest_wrapper
    def test_traffic_sg_np_200rules(self):
        '''
        1. launch 2 VN with VM each
        2. apply SG with 200 rules, on VMIs
        3. apply NP with 200 rules on VNs
        3. generate 100K flow & measure time taken
        '''
        self.create_networks(nr=2)
        self.create_virtual_machines(image='ubuntu-traffic')
        self.clear_sg_on_vms()
        self.create_security_groups(port_partition=200)
        self.apply_sgs_to_vms()
        self.create_network_policys(port_partition=200)
        port = random.randint(1000, 60000)
        self.run_hping(self.vms[0], self.vms[1:],
            "test with 200 rules for SG & NP", base_port_range=(port, port+10))

    @preposttest_wrapper
    def test_traffic_sg_np_1krules(self):
        '''
        1. launch 2 VN with VM each
        2. apply SG with 1000 rules, on VMIs
        3. apply NP with 1000 rules on VNs
        3. generate 100K flow & measure time taken
        '''
        self.create_networks(nr=2)
        self.create_virtual_machines(image='ubuntu-traffic')
        self.clear_sg_on_vms()
        self.create_security_groups(port_partition=1000)
        self.apply_sgs_to_vms()
        self.create_network_policys(port_partition=1000)
        port = random.randint(1000, 60000)
        self.run_hping(self.vms[0], self.vms[1:],
            "test with 1K rules for SG & NP", base_port_range=(port, port+10))

    @preposttest_wrapper
    def test_100sg_np_200rules(self):
        '''
        1. launch 2 VN with VM each
        2. create 100 SGs with 200 rules, on VMIs
        3. apply NP with 200 rules on VNs
        3. generate 100K flow & measure time taken
        '''
        self.create_networks(nr=100)
        self.create_virtual_machines([self.vns[0], self.vns[-1]],
                                    image='ubuntu-traffic')
        subnets = [vn.vn_subnets[0]['cidr'] for vn in self.vns]
        self.create_security_groups(cidrs=subnets, port_partition=200)
        self.create_network_policys(vns=[self.vns[0], self.vns[-1]],
                                    port_partition=200)
        self.clear_sg_on_vms()
        self.apply_sgs_to_vms()
        port = random.randint(1000, 60000)
        self.run_hping(self.vms[0], self.vms[1:],
            "test with 100 SG & NP with 200 rules",
            base_port_range=(port, port+10))

    @preposttest_wrapper
    def test_100sg_np_1krules(self):
        '''
        1. launch 2 VN with VM each
        2. create 100 SGs with 1000 rules, on VMIs
        3. apply NP with 1000 rules on VNs
        3. generate 100K flow & measure time taken
        '''
        self.create_networks(nr=100)
        self.create_virtual_machines([self.vns[0], self.vns[-1]],
                                    image='ubuntu-traffic')
        subnets = [vn.vn_subnets[0]['cidr'] for vn in self.vns]
        self.create_security_groups(cidrs=subnets, port_partition=1000)
        self.create_network_policys(vns=[self.vns[0], self.vns[-1]],
                                    port_partition=1000)
        self.clear_sg_on_vms()
        self.apply_sgs_to_vms()
        port = random.randint(1000, 60000)
        self.run_hping(self.vms[0], self.vms[1:],
            "test with 100 SG & NP with 1K rules",
            base_port_range=(port, port+75))
