from __future__ import absolute_import
from .base import BaseBgpvpn
from common.base import GenericTestBase
from tcutils.wrappers import preposttest_wrapper
from bgpvpn_test import BgpvpnFixture

class TestBgpvpn(BaseBgpvpn):

    def setUp(self):
        super(TestBgpvpn, self).setUp()

    @preposttest_wrapper
    def test_bgpvpn_basic(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223
            2)Create VN1 and VM1
            3) Associate bgpvpn1 to VN1
            4)Verify Route-target in VN1 routing-instance
            5)Ping from MX to VM and ping should pass
            6)Disassociate bgpvpn1 from VN
            7)Verify Route-target in VN1 routing-instance
            8)Ping to VM should fail
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt]))
        self.create_basic_config(forwarding_mode='l2_l3')
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)

    @preposttest_wrapper
    def test_l3_bgpvpn_with_l3_vn(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223 and l3 mode
            2)Create VN1 in L3 mode and VM1
            3) Associate bgpvpn1 to VN1
            4)Verify Route-target in VN1 routing-instance
            5)Ping from MX to VM and ping should pass
            6)Disassociate bgpvpn1 from VN
            7)Verify Route-target in VN1 routing-instance
            8)Ping to VM should fail
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt], mode='l3'))
        self.create_basic_config(forwarding_mode='l3')
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)

    @preposttest_wrapper
    def test_l2_bgpvpn_with_l2_vn(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223 and l2 mode
            2)Create VN1 in L2 mode and VM1
            3)Associate bgpvpn1 to VN1
            4)Verify Route-target in VN1 routing-instance
            5)send L2 traffic rom MX to VM and should pass
            6)Disassociate bgpvpn1 from VN
            7)Verify Route-target in VN1 routing-instance
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt], mode='l2'))
        self.create_basic_config(forwarding_mode='l2')
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)

    @preposttest_wrapper
    def test_bgpvpn_logical_router(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223
            2)Create VN1  and VN1-VM and VN2 and VN2-VM2
            3)Create logical router LR1 and attach VN1 and VN2
            4) Associate bgpvpn1 to LR1
            5)Verify Route-target in VN1 and VN2 routing-instance
            6)Ping from MX to VN1-VM and VN2-VM ping should pass
            7)Disassociate bgpvpn1 from LR1
            7)Verify Route-target in VN1 and VN2 routing-instance
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt], mode='l2_l3'))
        self.create_LR_config(forwarding_mode='l2_l3')
        bgpvpn_fixture.associate_bgpvpn_to_lr(self.lr_obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn1_fixture, search_value=rt)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn2_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm2_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_lr(self.lr_obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn1_fixture, search_value=rt)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn2_fixture, search_value=rt)

    @preposttest_wrapper
    def test_bgpvpn_update_RT(self):
        '''
            1)Create BGP VPN bgpvn1
            2)Create VN1 in L2 mode and VM1
            3) Associate bgpvpn1 to VN1
            4)Ping from MX to VM and pingg should fail
            5)Update bgpvpn1 with Route Target target:64512:2223
            6)Verify Route-target in VN1 routing-instance
            7)Ping to VM should pass
            6)Disassociate bgpvpn1 from VN
            7)Verify Route-target in VN1 routing-instance
            8)Ping to VM should fail
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[]))
        self.create_basic_config(forwarding_mode='l2_l3')
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert not self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.update_rt([rt])
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)

    @preposttest_wrapper
    def test_bgpvpn_attach_to_multiple_vns(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223
            2)Create VN1 and VN1-VM and VN2 and VN2-VM
            3) Associate bgpvpn1 to VN1 and VN2
            4)Verify Route-target in VN1 and VN2 routing-instance
            5)Ping from MX to VN1-VM and VN2-vm ping should pass
            6)Disassociate bgpvpn1 from VN1 and VN2
            7)Verify Route-target in VN1 routing-instance
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt]))
        self.create_basic_config(forwarding_mode='l2_l3')
        vn2_name = get_random_name('bgpvpn_v2')
        vm2_name = get_random_name('bgpvpn_vm2')
        vn2_subnets = [get_random_cidr()]
        self.vn2_fixture = self.create_vn(vn2_name, vn2_subnets,forwarding_mode=forwarding_mode)
        self.vm2_fixture = self.create_vm(vn2_fixture, vm2_name, image_name='cirros')
        assert self.vm2_fixture.wait_till_vm_is_up()
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn2_fixture.obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn2_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm2_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture2.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)


    @preposttest_wrapper
    def test_bgpvpn_flap_bgp_session(self):
        '''
            1)Create BGP VPN bgpvn1 with Route Target target:64512:2223
            2)Create VN1 and VM1
            3) Associate bgpvpn1 to VN1
            4)Verify Route-target in VN1 routing-instance
            5)Ping from MX to VM and ping should pass
            6)Make peering with MX inactive
            7)Ping from MX to VM and ping should fail
            8)Establish peeringg wiith MX
            9)Ping from MX to VM and ping should pass
            10)Disassociate bgpvpn1 from VN
            11)Verify Route-target in VN1 routing-instance
        '''
        rt = 'target:64512:2223'
        mx_params = list(self.inputs.physical_routers_data.values())[0]
        bgpvpn_fixture = self.useFixture(BgpvpnFixture(
                                      self.connections,route_target=[rt], mode='l2_l3'))
        self.create_basic_config(forwarding_mode='l2_l3')
        bgpvpn_fixture.associate_bgpvpn_to_vn(self.vn_fixture.obj)
        assert bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)
        ping_cmd = "run ping %s routing-instance bgpvpn source 74.74.74.74"%self.vm_fixture.vm_ip
        assert self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        assert self.change_bgp_router_state(),'Not able to change bgp_router state'
        assert not self.ping_from_mx(mx_params['mgmt_ip'], [ping_cmd])
        assert self.change_bgp_router_state(False),'Not able to change bgp_router state'
        bgpvpn_fixture.disassociate_bgpvpn_from_vn(self.vn_fixture.obj)
        assert not bgpvpn_fixture.verify_route_target_in_control(self.vn_fixture, search_value=rt)