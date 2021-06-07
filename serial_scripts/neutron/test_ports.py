# Need to import path to test/fixtures and test/scripts/
# Ex : export PYTHONPATH='$PATH:/root/test/fixtures/:/root/test/scripts/'
#
# To run tests, you can do 'python -m testtools.run tests'. To run specific tests,
# You can do 'python -m testtools.run -l tests'
# Set the env variable PARAMS_FILE to point to your ini file. Else it will try to pick params.ini in PWD
#
from common.neutron.base import BaseNeutronTest
from builtins import str
import os
import fixtures
import testtools
import time

from vn_test import *
from vm_test import *
from port_fixture import PortFixture
from common.connections import ContrailConnections
from tcutils.wrappers import preposttest_wrapper

import test
from tcutils.util import *
from netaddr import IPNetwork, IPAddress
from floating_ip import FloatingIPFixture


class TestPorts(BaseNeutronTest):

    @classmethod
    def setUpClass(cls):
        super(TestPorts, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestPorts, cls).tearDownClass()

    def reset_aap_prefix_length_limit(self):
        for node in self.inputs.cfgm_ips:
            self.inputs.add_knob_to_container(node_ip=node,
                container_name='config_api_1', level='DEFAULTS',
                knob='aap_prefix_len_limit=24', restart_container=True,
                file_name='entrypoint.sh')
    # end reset_aap_prefix_length_limit

    @preposttest_wrapper
    def test_custom_aap_prefix_length_limit(self):
        '''
    CEM-8237 :: Set aap_prefix_len_limit to custom value in config.
    1.  Set aap_prefix_len_limit to 15 in config and then try running
    the script with prefix_length = 20 this should pass in neutron
    configuration but fail in vrouter side as still on the vrouter
    side the code to create port with custom aap prefix length is
    missing.
    2. Next try will be running the script with prefix_length = 12
    this should fail in neutron configuration as the requested aap
    prefix length(12) is lesser than the configured aap prefix
    length(15).
        '''

        #Configure aap_prefix_length_limit back to 24 in cfgm/s in
        #in cleanup routine.
        self.addCleanup(self.reset_aap_prefix_length_limit)

        vn1_name = get_random_name('vn1')
        vn1_subnets = ['10.10.10.0/24']
        vm1_name = get_random_name('vm1')
        vIP = '10.10.10.10'
        result = True

        vn1_fixture = self.create_vn(vn1_name, vn1_subnets)

        port1_obj = self.create_port(net_id=vn1_fixture.vn_id)

        vm1_fixture = self.create_vm(vn1_fixture, vm1_name,
                                     image_name='cirros',
                                     #image_name='ubuntu-traffic',
                                     port_ids=[port1_obj['id']])
        assert vm1_fixture.wait_till_vm_is_up(), 'VM does not seem to be up'

        #Try with aap_prefix_length=20 without changing any config in cfgm.
        try:
            self.config_aap(port1_obj['id'], vIP, prefix_len=20,
                            mac=port1_obj['mac_address'])
        except Exception as e:
            assert e.status_code==400
            em='IPv4 Prefix length lesser than 24:it is 20 - is not acceptable.'
            assert em in e.message
        else:
            assert False, 'Able to add aap with prefix length lesser than \
                           default limit of 24 bit, Test Failed'

        #Configure aap_prefix_length_limit as 15 in cfgm/s.
        for node in self.inputs.cfgm_ips:
            self.inputs.add_knob_to_container(node_ip=node,
                container_name='config_api_1', level='DEFAULTS',
                knob='aap_prefix_len_limit=15', restart_container=True,
                file_name='entrypoint.sh')

        #Try with aap_prefix_length=20 after changing the limit in cfgm.
        try:
            self.config_aap(port1_obj['id'], vIP, prefix_len=20,
                            mac=port1_obj['mac_address'])
        except Exception as e:
            assert False, 'Failed to add aap with prefix length more than \
                           non-default limit of 15 configured in cfgm, Test Failed'

        #Try with aap_prefix_length=12 after changing the limit in cfgm.
        try:
            self.config_aap(port1_obj['id'], vIP, prefix_len=12,
                            mac=port1_obj['mac_address'])
        except Exception as e:
            assert e.status_code==400
            em='IPv4 Prefix length lesser than 15:it is 12 - is not acceptable.'
            assert em in e.message
        else:
            assert False, 'Able to add aap with prefix length lesser than \
                           configured limit of 15 bit, Test Failed'

        return True
    # end test_custom_aap_prefix_length_limit

