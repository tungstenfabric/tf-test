from tcutils.util import retry,get_random_name
from vnc_api.vnc_api import Bgpvpn, RouteListType, RouteTargetList
import fixtures

class BgpvpnFixture(fixtures.Fixture):

    def __init__(self, connections, name, route_target=None, mode=None):
        self.connections = connections
        self.inputs = connections.inputs
        self.logger = self.connections.logger
        self.vnc_lib_h = self.connections.get_vnc_lib_h()
        self.api_s_inspect = self.connections.api_server_inspect
        self.cn_inspect = self.connections.cn_inspect
        self.project = self.connections.project_name
        self.bgpvpn_name = get_random_name('bgpvpn')
        self.bgpvpn_id = None
        self.bgpvpn_fq_name = ['default-domain', self.bgpvpn_name]
        self.bgpvpn_obj = None
        self.mode = mode
        self.route_target = route_target or []

    def read(self):
        if self.bgpvpn_id:
            self.bgpvpn_obj = self.vnc_lib_h.bgpvpn_read(id=self.agg_id)
            self.bgpvpn_name = self.bgpvpn_obj.name
    # end read

    def setUp(self):
        super(BgpvpnFixture, self).setUp()
        self.create()
    # end setup

    def create(self):
        if not self.bgpvpn_id:
            project = self.vnc_lib_h.project_read(fq_name=['default-domain', self.project_name])
            bgpvpn = Bgpvpn(name=self.bgpvpn_name, parent_obj=project)
            bgpvpn.set_route_target_list(RouteTargetList(self.route_target))
            self.bgpvpn_id = self.vnc_lib_h.bgpvpn_create(bgpvpn)
            self.logger.info('created Bgpvpn %s'%self.bgpvpn_name)
            self.read()
    # end create

    def associate_bgpvpn_to_vn(self, vn_obj):
        vn_obj.add_bgpvpn(self.bgpvpn_obj)
        self.vnc_lib_h.virtual_network_update(vn_obj)

    def associate_bgpvpn_to_LR(self, lr_obj):
        lr_obj.add_bgpvpn(self.bgpvpn_obj)
        self.vnc_lib.logical_router_update(lr_obj)

    def update_bgpvpn_mode(self, route_target=[]):
        self.bgpvpn_obj.set_route_target_list(RouteTargetList(route_target))
        self.vnc_lib.bgpvpn_update(bgpvpn)

    def disassociate_bgpvpn_from_vn(self,vn_obj):
        vn_obj.delete_bgpvpn(self.bgpvpn_obj)
        self.vnc_lib_h.virtual_network_update(vn_obj)

    def disassociate_bgpvpn_from_lr(self,lr_obj):
        lr_obj.delete_bgpvpn(self.bgpvpn_obj)
        self.vnc_lib_h.virtual_network_update(lr_obj)

    def update_rt(self, rt=[]):
        self.bgpvpn_obj.set_route_target_list(RouteTargetList(rt))
        self.vnc_lib_h.bgpvpn_update(self.bgpvpn_obj)

    @retry(delay=1, tries=10)
    def verify_route_target_in_control(self, vn_fixture, vm_fixture, prefix = '', search_value = ''):
        search_in_cn = prefix
        found_value = True
        for cn in vm_fixture.get_control_nodes():
            found_value = found_value and re.findall(search_value, str(
                self.cn_inspect[cn
                ].get_cn_route_table_entry(search_in_cn,
                vn_fixture.vn_fq_name+":"+vn_fixture.vn_name)[0]))
            self.logger.info('Route prefix were found in control node %s'%cn)
        return True if found_value else False
    # end verify_route_target_in_control

    @retry(delay=1, tries=10)
    def verify_prefix_in_control(self, vn_fixture, vm_fixture, prefix = '', search_value = ''):
        search_in_cn = prefix
        found_value = True
        for cn in vm_fixture.get_control_nodes():
            found_value = found_value and re.findall(search_value, str(
                self.cn_inspect[cn
                ].get_cn_route_table_entry(search_in_cn,
                vn_fixture.vn_fq_name+":"+vn_fixture.vn_name)[0]))
            self.logger.info('Route prefix were found in control node %s'%cn)
        return True if found_value else False
    # end verify_prefix_in_control

    def delete(self):
        self.logger.info('Deleting Bgpvpn %s'%self.bgpvpn_name)
        self.vnc_lib_h.bgpvpn_delete(id=self.bgpvpn_id)
    # end delete

    def cleanUp(self):
        self.delete()
        self.logger.info('Deleted Bgpvpn %s' % self.bgpvpn_name)
        super(BgpvpnFixture, self).cleanUp()
    # end cleanup