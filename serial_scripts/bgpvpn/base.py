from common.base import GenericTestBase
from tcutils.util import get_random_name, get_random_cidr

class BaseBgpvpn(GenericTestBase):

    @classmethod
    def setUpClass(cls):
        super(BaseBgpvpn, cls).setUpClass()
        cls.quantum_h = cls.connections.quantum_h
        cls.nova_h = cls.connections.nova_h
        cls.vnc_lib = cls.connections.vnc_lib
        cls.agent_inspect = cls.connections.agent_inspect
        cls.cn_inspect = cls.connections.cn_inspect
        cls.analytics_obj = cls.connections.analytics_obj
        cls.create_physical_router()
        cls.create_bgp_group_on_mx()
        cls.create_vrf_on_mx()
    # end setUpClass

    @classmethod
    def tearDownClass(cls):
        super(BaseBgpvpn, cls).tearDownClass()
    # end tearDownClass

    def setUp(self):
        super(BaseBgpvpn, self).setUp()

    def tearDown(self):
        super(BaseBgpvpn, self).tearDown()

    def create_basic_config(self, forwarding_mode='l2_l3'):
        vn_name = get_random_name('bgpvpn_vn')
        vm_name = get_random_name('bgpvpn_vm')
        vn_subnets = [get_random_cidr()]
        self.vn_fixture = self.create_vn(vn_name, vn_subnets,forwarding_mode=forwarding_mode)
        self.vm_fixture = self.create_vm(vn_fixture, vm_name, image_name='cirros')
        assert self.vm_fixture.wait_till_vm_is_up()

    def create_lr_config(self, forwarding_mode='l2_l3'):
        self.create_basic_config('l2_l3')
        vn2_name = get_random_name('bgpvpn_v2')
        vm2_name = get_random_name('bgpvpn_vm2')
        vn2_subnets = [get_random_cidr()]
        self.vn2_fixture = self.create_vn(vn2_name, vn2_subnets,forwarding_mode=forwarding_mode)
        self.vm2_fixture = self.create_vm(vn2_fixture, vm2_name, image_name='cirros')
        assert self.vm2_fixture.wait_till_vm_is_up()
        self.lr = self.create_lr([self.vn_fixture,self.vn2_fixture])
        self.lr_obj = self.vnc_api_h.logical_router_read(fq_name=self.lr.lr_fq_name)
        self.addCleanup(self.lr.delete)

    def create_physical_router(self):
        device_dict = list(self.inputs.physical_routers_data.values())[0]
        self.phy_router_obj = PhysicalRouterFixture(
                device_dict['name'],
                device_dict['mgmt_ip'],
                asn=device_dict['asn'],
                model=device_dict.get('model', 'mx'),
                vendor=device_dict.get('vendor', 'juniper'),
                ssh_username=device_dict.get('ssh_username'),
                ssh_password=device_dict.get('ssh_password'),
                tunnel_ip=device_dict.get('tunnel_ip'),
                ports=device_dict.get('ports'),
                cfgm_ip=self.inputs.cfgm_ip,
                auth_server_ip=self.inputs.auth_ip,
                inputs=self.inputs,
                username=self.inputs.admin_username,
                password=self.inputs.admin_password,
                project_name=self.inputs.admin_tenant,
                domain=self.inputs.admin_domain,
                orchestrator=self.inputs.orchestrator
                )
        self.phy_router_obj.setUp()
        self.phy_router_obj.verify_bgp_peer()

    def create_bgp_group_on_mx(self):
        if self.inputs.ext_routers:
            router_params = list(self.inputs.physical_routers_data.values())[0]
            if router_params['model'] == 'mx':
                cmd = []
                cmd.append('set groups bgpvpn routing-options router-id %s' % router_params['mgmt_ip'])
                cmd.append('set groups bgpvpn routing-options route-distinguisher-id %s' % router_params['mgmt_ip'])
                cmd.append('set groups bgpvpn routing-options autonomous-system %s' % router_params['asn'])
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn type internal')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn multihop')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn local-address %s' % router_params['mgmt_ip'])
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn hold-time 90')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn keep all')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn family inet-vpn unicast')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn family inet6-vpn unicast')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn family evpn signaling')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn family route-target')
                cmd.append('set groups bgpvpn protocols bgp group bgpvpn local-as %s' % router_params['asn'])
                for node in self.inputs.bgp_control_ips:
                    cmd.append('set groups bgpvpn protocols bgp group bgpvpn neighbor %s peer-as %s' % (node, router_params['asn']))
                cmd.append('set apply-groups bgpvpn')
                cmds.append('activate protocols bgp group bgpvpn')
                cli_output = self.run_mx_cmds(router_params['mgmt_ip'],cmd, timeout = 120)
                cleanup_cmds = []
                cleanup_cmds.append('delete groups bgpvpn')
                cleanup_cmds.append('delete apply-groups bgpvpn')
                self.addCleanup(self.run_mx_cmds, router_params['mgmt_ip'], cleanup_cmds)

    def create_vrf_on_mx(self):
        self.logger.info("Create VRF configuration in MX")
        router_params = list(self.inputs.physical_routers_data.values())[0]
        #ri_interface = router_params["vrf_interface"]
        rd = "64512:2223"
        rt = "target:64512:2223"
        static_route = ["74.74.74.74/32"]
        cmds = []
        cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf instance-type vrf")
        #cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf interface %s" %ri_interface)
        cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf route-distinguisher %s" %rd)
        cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf vrf-target %s" %rt)
        cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf vrf-table-label")
        cmds.append("set groups bgpvpn routing-instances bgpvpn_vrf routing-options static route %s discard " %static_route[0])
        cleanup_cmds = []
        self.run_mx_cmds(mx_config['control_ip'], cmds, cleanup_cmds)

    def run_mx_cmds(self, device_ip, cli_cmds, ignore_errors=False):

        mx_handle = NetconfConnection(host=device_ip)
        mx_handle.connect()
        cli_output = mx_handle.config(
            stmts=cli_cmds, ignore_errors=ignore_errors, timeout=120)
        mx_handle.disconnect()
        assert cli_output[0], "Not able to push config to mx"
        return cli_output

    def ping_from_mx(self,mx_ip, cmd):
        cli_output = self.run_mx_cmds(mx_ip, cmd)
        return cli_output

    def change_bgp_router_state(self,state=True):
        bgp_obj = self.phy_router_obj.bgp_router
        bgp_params = bgp_obj.get_bgp_router_parameters()
        bgp_params.set_admin_down(state)
        self.vnc_lib_h.bgp_router_update(bgp_obj)
        cn_bgp_entry = self.cn_inspect[
            self.inputs.bgp_control_ips[0]].get_cn_bgp_neigh_entry(encoding='BGP')
        for entry in cn_bgp_entry:
            if state:
                if (entry['encoding'] == 'BGP') and (entry['admin_down'] == 'true'):
                    return True
            if not state:
                if (entry['encoding'] == 'BGP') and (entry['admin_down'] == 'false'):
                    return True
        return False