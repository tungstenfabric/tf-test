from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
import test
from compute_node_test import ComputeNodeFixture
from tcutils.traffic_utils.hping_traffic import Hping3
import time
import logging
from common.contrail_services import get_contrail_services_map


class TestFlowScale(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(TestFlowScale, cls).setUpClass()
        cls.logger.setLevel(logging.INFO)
        cls.get_compute_fixtures()
        cls.add_phy_intf_in_vrouter_env()
        flow_entries = 1024 * 1024 * 6
        cls.flow_timeout = 120
        cls.set_flow_entries_and_age_timeout(flow_entries, cls.flow_timeout)
        cls.start_tools_container()

    @classmethod
    def start_tools_container(cls):
        for compute in cls.compute_fixtures:
            cfg = cls.inputs.contrail_configs
            image = "%s/contrail-tools:%s" % (cfg['CONTAINER_REGISTRY'],
                                              cfg['CONTRAIL_VERSION'])
            cmd = "docker run -id --entrypoint bash "
            cmd += " --name tools "
            cmd += "-v /etc/contrail:/etc/contrail:ro -v /etc/hosts:/etc/hosts:ro "
            cmd += "-v /etc/localtime:/etc/localtime:ro -v /var/run:/var/run "
            cmd += "-v /dev:/dev -v /var/lib/containers:/var/lib/containers "
            cmd += "--pid host --net host --privileged "
            cmd += image
            compute.execute_cmd(cmd, container=None)

    @classmethod
    def tearDownClass(cls):
        super(TestFlowScale, cls).tearDownClass()

    def setUp(self):
        super(TestFlowScale, self).setUp()
        self.vn1_fixture = self.create_only_vn()
        vm1_node_name = self.inputs.host_data[self.inputs.compute_ips[0]]['name']
        self.vn1_vm1_fixture = self.create_vm(
            self.vn1_fixture, node_name=vm1_node_name)
        self.vn1_vm1_fixture.wait_till_vm_is_up()
        self.vn1_vm1_vrouter_fixture = self.useFixture(ComputeNodeFixture(
            self.connections,
            self.vn1_vm1_fixture.vm_node_ip))
        self.compute_fixture = ComputeNodeFixture(
            self.connections, self.vn1_vm1_fixture.vm_node_ip)
        self.flow_mem_usage = {}
        self.mem_usg = []
        self.min_mem_usg = 0

    @classmethod
    def get_compute_fixtures(cls):
        cls.compute_fixtures = []
        hset = set()
        for name, ip in cls.connections.inputs.compute_info.items():
            if ip not in hset:
                cls.compute_fixtures.append(
                    ComputeNodeFixture(cls.connections, ip))
                hset.add(ip)

    @classmethod
    def add_phy_intf_in_vrouter_env(cls):
        for compute_fixture in cls.compute_fixtures:
            intf = cls.inputs.inputs.host_data[compute_fixture.ip]['roles']['vrouter']['PHYSICAL_INTERFACE']
            line = "'PHYSICAL_INTERFACE=%s'" % intf
            file = '/etc/contrail/common_vrouter.env'
            cmd = "grep -F %s %s" % (line, file)
            output = compute_fixture.execute_cmd(cmd, container=None)

            if not output:
                echo_line = "echo %s >> %s" % (line, file)
                cd_vrouter = 'cd /etc/contrail/vrouter'
                down_up = 'docker-compose down && docker-compose up -d'
                cmd = '%s;%s;%s' % (echo_line, cd_vrouter, down_up)
                compute_fixture.execute_cmd(cmd, container=None)

    @classmethod
    def add_dpdk_flow_args_to_entrypoint(cls, compute_fixture, flow_entries):
        container_name = get_contrail_services_map(cls.inputs)['agent-dpdk'][0]
        file_name = 'entrypoint.sh'
        args = 'DPDK_COMMAND_ADDITIONAL_ARGS="--vr_flow_entries=%s"' % flow_entries
        level = '# base command'
        just_args = args[:args.find('=')]
        node_ip = compute_fixture.ip

        issue_cmd = 'docker cp %s:/%s .' % (container_name, file_name)
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        compute_fixture.execute_cmd(issue_cmd, container=None)

        issue_cmd = "awk 'BEGIN { section=0; doprint=1 } /%s/ { section=1 } /%s/ { if (section) {doprint=0; section=0} } { if (doprint) {print} else {doprint=1} }'  %s > %s.modified" % (
            level, just_args, file_name, file_name)
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        compute_fixture.execute_cmd(issue_cmd, container=None)

        issue_cmd = "mv entrypoint.sh.modified entrypoint.sh; chmod +x entrypoint.sh"
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        compute_fixture.execute_cmd(issue_cmd, container=None)

        issue_cmd = 'grep -q -F \''+args+'\' %s ||' % (file_name) + \
                    'sed -i  \'/'+level+'/a '+args+'\' %s' % (file_name)
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        compute_fixture.execute_cmd(issue_cmd, container=None)

        issue_cmd = 'docker cp %s %s:/%s' % (file_name, container_name,
                                             file_name)
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        op = compute_fixture.execute_cmd(issue_cmd, container=None)
        cls.logger.info(op)

        issue_cmd = 'docker restart %s -t 60' % (container_name)
        cls.logger.info('Running %s on %s' % (issue_cmd, node_ip))
        op = compute_fixture.execute_cmd(issue_cmd, container=None)
        cls.logger.info(op)

    @classmethod
    def set_flow_entries(cls, flow_entries):
        for compute_fixture in cls.compute_fixtures:
            if compute_fixture.ip in cls.inputs.dpdk_ips:
                cls.add_dpdk_flow_args_to_entrypoint(
                    compute_fixture, flow_entries)
            else:
                compute_fixture.add_vrouter_module_params(
                    {'vr_flow_entries': str(flow_entries)}, reload_vrouter=True)
                info_cmd = 'contrail-tools vrouter --info |grep "Flow Table limit"'
                output = compute_fixture.execute_cmd(info_cmd, container=None)
                cls.logger.info(output)

    @classmethod
    def add_flow_cache_timeout(cls, flow_timeout):
        for cmp_fix in cls.compute_fixtures:
            cmp_fix.set_flow_aging_time(flow_timeout)

    @classmethod
    def set_flow_entries_and_age_timeout(cls, flow_entries, flow_timeout):
        cls.set_flow_entries(flow_entries)
        cls.add_flow_cache_timeout(flow_timeout)

    def run_hping_udp(self, baseport):
        count = 1024 * 1024
        interval = 'u1'
        destport = '++1000'
        gateway_ip = self.vn1_fixture.vn_subnet_objs[0]['gateway_ip']
        hping_h = Hping3(self.vn1_vm1_fixture,
                         gateway_ip,
                         udp=True,
                         keep=True,
                         destport=destport,
                         baseport=baseport,
                         count=count,
                         interval=interval)
        hping_h.start(wait=False)
        self.logger.info('Running hping command for 5s')
        time.sleep(5)
        (stats, hping_log) = hping_h.stop()

    def run_hping_tcp(self, baseport):
        count = 1024 * 1024
        interval = 'u1'
        destport = '++1000'
        gateway_ip = self.vn1_fixture.vn_subnet_objs[0]['gateway_ip']
        hping_h = Hping3(self.vn1_vm1_fixture,
                         gateway_ip,
                         syn=True,
                         keep=True,
                         flood=True,
                         destport=destport,
                         baseport=baseport,
                         count=count,
                         interval=interval)
        hping_h.start(wait=False)
        self.logger.info('Running command for 5s')
        time.sleep(5)
        (stats, hping_log) = hping_h.stop()

    def calc_vrouter_mem_usage(self):
        cmd = "top -b -n 1 -p $(pidof contrail-vrouter-agent);free -h"
        out = self.compute_fixture.execute_cmd(cmd, container=None)
        self.logger.info('Top cmd info of agent process: %s' % out)
        cmd = "cat /proc/$(pidof contrail-vrouter-agent)/status | grep VmRSS | awk '{print $2}'"
        out = int(self.compute_fixture.execute_cmd(cmd, container=None))
        self.logger.info('vrouter agent resident memory usage: %s' % out)
        return out

    def wait_and_add_flows(self, baseport):
        self.logger.info('Wait 120s for flows to get cleared')
        time.sleep(self.flow_timeout)
        self.logger.info(
            'Checking flow_count and memory usage of vrouter')
        flow_count = self.get_flow_count()
        mem = self.calc_vrouter_mem_usage()
        l = len(self.mem_usg)
        diff = abs(self.mem_usg[l-1] - self.mem_usg[0])
        assert diff < self.tolerance, 'Memory not decreasing proportionately after flow deletion'
        self.flow_mem_usage[flow_count] = mem
        self.mem_usg.append(mem)

        # Add 1 Million flows
        self.logger.info('Adding 1 Million flows')
        for baseport in range(6001, 6050):
            self.run_hping_udp(baseport)
            flow_count = self.get_flow_count()
            mem = self.calc_vrouter_mem_usage()
            self.flow_mem_usage[flow_count] = mem
            self.mem_usg.append(mem)
            if flow_count >= 1024 * 1024:
                break

        time.sleep(5)
        flow_count = self.get_flow_count()
        self.logger.info(
            'Checking flow_count and memory usage of vrouter')
        flow_count = self.get_flow_count()
        mem = self.calc_vrouter_mem_usage()
        l = len(self.mem_usg)
        assert mem > self.mem_usg[l -
                                  1], 'Memory not increasing after addition of flows'
        self.flow_mem_usage[flow_count] = mem
        self.mem_usg.append(mem)

    def get_flow_count(self):
        cmd = "docker ps|grep tools|awk '{print $NF}'|tail -1"
        tools_container = self.compute_fixture.execute_cmd(cmd, container=None)
        cmd = "docker exec -it %s timeout 1 flow -r|awk '{print $5}'" % tools_container
        flow_count = self.compute_fixture.execute_cmd(cmd, container=None)
        if flow_count:
            flow_count = int(flow_count)
        else:
            flow_count = 0
        self.logger.info('Flow count: %s' % flow_count)
        return flow_count

    def memory_leak_checks(self):
        for i in range(3):
            baseport = 6000 + i
            self.wait_and_add_flows(baseport)

    def watch_for_fluctuations(self, flow_count_list):
        flow_count = self.get_flow_count()
        mem = self.calc_vrouter_mem_usage()
        flow_len = len(flow_count_list)
        assert abs(flow_count - flow_count_list[flow_len -
                                                1]) < 50, 'Flow count fluctuating'
        mem_len = len(self.mem_usg)
        assert abs(mem - self.mem_usg[mem_len-1]
                   ) < self.tolerance, 'Memory usage of vrouter fluctuating'
        self.flow_mem_usage[flow_count] = mem
        self.mem_usg.append(mem)
        flow_count_list.append(flow_count)

    @test.attr(type=['flow_scale'])
    @preposttest_wrapper
    def test_flow_scale_udp(self):
        '''
        Description: Test to scale above 1 million flows and check for memory leaks for UDP traffic
         Test steps:
                1. Add PHYSICAL_INTERFACE in vrouter env if absent
                2. Set flow entries to 1 million in vrouter module
                3. Send traffic through hping3 changing the source port with each iteration
                4. Check for flow count and memory usage
                5. Check for memory leaks
         Pass criteria: Flows scaled above 1 million and there is no memory leaks
         Maintainer : nuthanc@juniper.net 
        '''
        mem = self.calc_vrouter_mem_usage()
        flow_count = self.get_flow_count()
        self.flow_mem_usage[flow_count] = mem
        self.mem_usg.append(mem)

        for baseport in range(5001, 7050):
            self.run_hping_udp(baseport)
            flow_count = self.get_flow_count()
            mem = self.calc_vrouter_mem_usage()
            self.flow_mem_usage[flow_count] = mem
            self.mem_usg.append(mem)
            if flow_count >= 1024 * 1024 * 2:
                break

        # Difference between mem usage for each read
        diff = [abs(j-i) for i, j in zip(self.mem_usg[:-1], self.mem_usg[1:])]
        avg = sum(diff) / len(diff)
        self.min_mem_usg = min(diff)
        self.tolerance = avg * 0.01
        self.logger.info('DIFF: %s AND AVG: %s' % (diff, avg))
        self.logger.info('Min memory usage: %s' % self.min_mem_usg)
        self.logger.info('Flow to memory usage: %s' % self.flow_mem_usage)
        self.memory_leak_checks()

    @test.attr(type=['flow_scale'])
    @preposttest_wrapper
    def test_flow_scale_tcp(self):
        '''
        Description: Test to scale above 6 million flows and check for memory leaks for TCP traffic
         Test steps:
                1. Add PHYSICAL_INTERFACE in vrouter env if absent
                2. Set flow entries to 1 million in vrouter module
                3. Send traffic through hping3 changing the source port with each iteration
                4. Check for flow count and memory usage
                5. Check for memory leaks
         Pass criteria: Flows scaled above 1 million and there is no memory leaks
         Maintainer : nuthanc@juniper.net 
        '''
        for baseport in range(1001, 7050):
            self.run_hping_tcp(baseport)
            flow_count = self.get_flow_count()
            mem = self.calc_vrouter_mem_usage()
            self.flow_mem_usage[flow_count] = mem
            self.mem_usg.append(mem)
            if flow_count >= 1024 * 1024 * 2:
                break

        # Difference between mem usage for each read
        diff = [abs(j-i) for i, j in zip(self.mem_usg[:-1], self.mem_usg[1:])]
        avg = sum(diff) / len(diff)
        self.min_mem_usg = min(diff)
        self.tolerance = avg * 0.01
        self.logger.info('DIFF: %s AND AVG: %s' % (diff, avg))
        self.logger.info('Min memory usage: %s' % self.min_mem_usg)
        self.logger.info('Flow to memory usage: %s' % self.flow_mem_usage)
        self.memory_leak_checks()

    @test.attr(type=['flow_scale'])
    @preposttest_wrapper
    def test_flow_longevity(self):
        '''
        Description: Test for flow longevity
         Test steps:
                1. Add PHYSICAL_INTERFACE in vrouter env if absent
                2. Set flow entries to 6 million in vrouter module
                3. Increase flow timeout to high value like 1 hr
                4. Send traffic through hping3 changing the source port with each iteration
                5. Check for flow count in flow table
         Pass criteria: Flows remaining constant after long intervals of time and memory usage being the same
         Maintainer : nuthanc@juniper.net 
        '''
        flow_entries = 1024 * 1024 * 6
        flow_timeout = 60 * 60
        flow_count_list = []
        self.set_flow_entries_and_age_timeout(flow_entries, flow_timeout)
        for baseport in range(5001, 7050):
            self.run_hping_udp(baseport)
            flow_count = self.get_flow_count()
            mem = self.calc_vrouter_mem_usage()
            self.flow_mem_usage[flow_count] = mem
            self.mem_usg.append(mem)
            flow_count_list.append(flow_count)
            if flow_count >= 1024 * 1024 * 6:
                break

        self.logger.info('Sleeping for 30s')
        time.sleep(30)

        mem = self.calc_vrouter_mem_usage()
        self.flow_mem_usage[flow_count] = mem
        self.mem_usg.append(mem)

        for i in range(3):
            self.watch_for_fluctuations(flow_count_list)
            self.logger.info('Sleep for 20s')
            time.sleep(20)

        for i in range(3):
            self.watch_for_fluctuations(flow_count_list)
            self.logger.info('Sleep for 10m')
            time.sleep(10 * 60)

        diff = [j-i for i, j in zip(self.mem_usg[:-1], self.mem_usg[1:])]
        avg = sum(diff) / len(diff)
        self.min_mem_usg = min(diff)
        self.logger.info('DIFF: %s AND AVG: %s' % (diff, avg))
        self.logger.info('Min memory usage: %s' % self.min_mem_usg)
        self.logger.info('Flow to memory usage: %s' % self.flow_mem_usage)


if __name__ == '__main__':
    TestFlowScale.setUpClass()
