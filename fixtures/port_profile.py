import vnc_api_test
from vnc_api.exceptions import NoIdError
from tcutils.util import get_random_name, retry

class PortProfileFixture(vnc_api_test.VncLibFixture):
    '''Fixture to handle port profile object
    Optional:
    :param name : name of the port profile
    :param uuid : UUID of the port profile
    :param flow_control :
    :param port_cos_untrust :
    :param bpdu_loop_protection :
    :param lacp_enable :
    :param lacp_interval : one of fast, slow
    :param lacp_mode : one of active, passive
    :param port_disable :
    :param port_description : sample string to describe
    :param port_mtu : int value in range of 256 to 9216
    :param storm_control_profiles : list of sc profile objects
    '''
    def __init__(self, *args, **kwargs):
        super(PortProfileFixture, self).__init__(*args, **kwargs)
        self.name = kwargs.get('name') or get_random_name('pp')
        self.uuid = kwargs.get('uuid')
        self.flow_control = kwargs.get('flow_control') or False
        self.port_cos_untrust = kwargs.get('port_cos_untrust') or False
        self.bpdu_loop_protection = kwargs.get('bpdu_loop_protection') or \
            False
        self.port_disable = kwargs.get('port_disable') or False
        self.port_description = kwargs.get('port_desc')
        self.port_mtu = kwargs.get('port_mtu')
        self.lacp_enable = kwargs.get('lacp_enable') or False
        self.lacp_mode = kwargs.get('lacp_mode')
        self.lacp_interval = kwargs.get('lacp_interval')
        self.sc_profiles = kwargs.get('storm_control_profiles') or list()
        self.created = False
        self.verify_is_run = False
        self.fq_name = [self.domain, self.project_name, self.name]

    def setUp(self):
        super(PortProfileFixture, self).setUp()
        self.create()

    def cleanUp(self):
        if self.created == False and self.inputs.fixture_cleanup != 'force':
            self.logger.info('Skipping deletion of port profile %s:'
                              %(self.fq_name))
        else:
            self.delete()
        super(PortProfileFixture, self).cleanUp()

    def get_object(self):
        return self.vnc_h.read_port_profile(id=self.uuid)

    def read(self):
        obj = self.vnc_h.read_port_profile(id=self.uuid)
        self.name = obj.name
        self.fq_name = obj.get_fq_name()
        self.parent_type = obj.parent_type
        params = obj.get_port_profile_params()
        if params:
            self.bpdu_loop_protection = params.get_bpdu_loop_protection()
            self.flow_control = params.get_flow_control()
            self.port_cos_untrust = params.get_port_cos_untrust()
            lacp_params = params.get_lacp_params()
            if lacp_params:
                self.lacp_enable = lacp_params.get_lacp_enable()
                self.lacp_mode = lacp_params.get_lacp_mode()
                self.lacp_interval = lacp_params.get_lacp_interval()
            port_params = params.get_port_params()
            if port_params:
                self.port_description = port_params.get_port_description()
                self.port_disable = port_params.get_port_disable()
                self.port_mtu = port_params.get_port_mtu()

        sc_profiles = list()
        for sc_ref in obj.get_storm_control_profile_refs() or []:
            sc_profiles.append(sc_ref['uuid'])
        self.sc_profiles = sc_profiles

    def create(self):
        if not self.uuid:
            try:
                obj = self.vnc_h.read_port_profile(fq_name=self.fq_name)
                self.uuid = obj.uuid
            except NoIdError:
                self.uuid = self.vnc_h.create_port_profile(
                    fq_name=self.fq_name,
                    flow_control=self.flow_control,
                    bpdu_loop_protection=self.bpdu_loop_protection,
                    port_cos_untrust=self.port_cos_untrust,
                    lacp_enable=self.lacp_enable,
                    lacp_interval=self.lacp_interval,
                    lacp_mode=self.lacp_mode,
                    port_desc=self.port_description,
                    port_disable=self.port_disable,
                    port_mtu=self.port_mtu
                )
                self.created = True
                self.logger.info('Created Port Profile %s(%s)'%(
                    self.name, self.uuid))
        if not self.created:
            self.read()
        self.add_storm_control_profiles(self.sc_profiles)

    def delete(self):
        self.logger.info('Deleting Port Profile %s(%s)'%(self.name, self.uuid))
        try:
            self.vnc_h.delete_port_profile(id=self.uuid)
        except NoIdError:
            pass

    def update(self, **kwargs):
        self.update_port_profile(self.uuid, **kwargs)
        if 'bpdu_loop_protection' in kwargs:
            self.bpdu_loop_protection = kwargs['bpdu_loop_protection']
        if 'flow_control' in kwargs:
            self.flow_control = kwargs['flow_control']
        if 'port_cos_untrust' in kwargs:
            self.port_cos_untrust = kwargs['port_cos_untrust']
        if 'lacp_enable' in kwargs:
            self.lacp_enable = kwargs['lacp_enable']
        if 'lacp_mode' in kwargs:
            self.lacp_mode = kwargs['lacp_mode']
        if 'lacp_interval' in kwargs:
            self.lacp_interval = kwargs['lacp_interval']
        if 'port_desc' in kwargs:
            self.port_description = kwargs['port_desc']
        if 'port_disable' in kwargs:
            self.port_disable = kwargs['port_disable']
        if 'port_mtu' in kwargs:
            self.port_mtu = kwargs['port_mtu']

    def add_storm_control_profiles(self, sc_profiles):
        for profile in sc_profiles:
            self.vnc_h.assoc_sc_to_port_profile(self.uuid, profile)
        self.sc_profiles = list(set(self.sc_profiles).union(set(sc_profiles)))

    def delete_storm_control_profiles(self, sc_profiles):
        for profile in sc_profiles:
            self.vnc_h.disassoc_sc_from_port_profile(self.uuid, profile)
        self.sc_profiles = list(set(self.sc_profiles) - set(sc_profiles))

    def _compare_pp_retrieved(self, pp_dct, exp=True, model=None):

        if exp != (self.flow_control == pp_dct.get('flow_control', False)):
            self.logger.debug('PP flow control did not match, exp: %s, '
                              'got: %s' % (self.flow_control,
                                           pp_dct.get('flow_control',
                                                      False)))
            return False

        if exp != (self.port_cos_untrust == pp_dct.get('port_cos_untrust',
                                                       False)):
            self.logger.debug('PP cos untrust did not match, exp: %s, '
                              'got: %s' % (self.port_cos_untrust,
                                           pp_dct.get('port_cos_untrust',
                                                      False)))
            return False

        if exp != (self.bpdu_loop_protection == pp_dct.get(
                'bpdu_loop_protection', False)):
            self.logger.debug('PP bpdu_loop_protection did not match, '
                              'exp: %s, got: %s' % (
                                  self.bpdu_loop_protection,
                                  pp_dct.get('bpdu_loop_protection', False)))
            return False

        if exp != (self.lacp_enable == pp_dct.get('lacp_enable', False)):
            self.logger.debug('PP lacp enable did not match, '
                              'exp: %s, got: %s' % (
                                  self.lacp_enable,
                                  pp_dct.get('lacp_enable', False)))
            return False

        if exp != (self.lacp_interval == pp_dct.get('lacp_interval')):
            self.logger.debug('PP lacp interval did not match, '
                              'exp: %s, got: %s' % (
                                  self.lacp_interval,
                                  pp_dct.get('lacp_interval')))
            return False

        if exp != (self.lacp_mode == pp_dct.get('lacp_mode')):
            self.logger.debug('PP lacp mode did not match, '
                              'exp: %s, got: %s' % (
                                  self.lacp_mode,
                                  pp_dct.get('lacp_mode')))
            return False

        if exp != (self.port_disable == pp_dct.get('port_disable', False)):
            self.logger.debug('PP port disable did not match, '
                              'exp: %s, got: %s' % (
                                  self.port_disable,
                                  pp_dct.get('port_disable', False)))
            return False

        if exp != (self.port_description == pp_dct.get('port_description')):
            self.logger.debug('PP port desc did not match, '
                              'exp: %s, got: %s' % (
                                  self.port_description,
                                  pp_dct.get('port_description')))
            return False

        if exp != (self.port_mtu == pp_dct.get('port_mtu')):
            self.logger.debug('PP port mtu did not match, '
                              'exp: %s, got: %s' % (
                                  self.port_mtu,
                                  pp_dct.get('port_mtu')))
            return False

        return True

    @retry(tries=10, delay=6)
    def validate_config_pushed(self, prouters, interfaces, exp=True):
        for prouter in prouters:
            prouter_config = prouter.get_config()
            details = self.inputs.physical_routers_data[prouter.name]
            pr_interfaces = [interface['tor_port'].replace('_', ':')
                for interface in interfaces if interface['tor'] == prouter.name]
            intf = pr_interfaces[0]
            if len(interfaces) > 1:
                intfs = set()
                for interface in pr_interfaces:
                    intf = prouter.get_associated_ae_interface(interface,
                                                               prouter_config)
                    if len(intf) != 1:
                        self.logger.debug('Expect one ae intf associated to %s got %s'%(
                                   interface, intf or None))
                        return False
                    intfs.add(intf[0])
                if len(intfs) != 1:
                    return False, 'Expect one ae intf associated to %s got %s'%(
                                   pr_interfaces, intf or None)
                intf = list(intfs)[0]
            pp_config = prouter.get_port_profile_config(intf, prouter_config)
            if not self._compare_pp_retrieved(pp_config, exp, model=prouter.model):
                return False
        return True
