"""Intf mirroring Scale tests."""
from __future__ import absolute_import
import os
import unittest
import fixtures
import testtools
import test

from common.connections import ContrailConnections
from common.contrail_test_init import ContrailTestInit
from tcutils.wrappers import preposttest_wrapper
from common.intf_mirroring.verify import VerifyIntfMirror
from .base import BaseIntfMirrorTest

class TestIntfMirrorScale(BaseIntfMirrorTest, VerifyIntfMirror):

    @classmethod
    def setUpClass(cls):
        super(TestIntfMirrorScale, cls).setUpClass()

    def runTest(self):
        pass
    # end runTest

    @preposttest_wrapper
    def test_intf_mirroring_scale_max_number(self):
        """
        Description: Verify Mirroring entries can scale to 255
        Test steps:
        1. Create VM with 51 sub subinterface,
        2. Enable mirroring on all 51 sub interface
        3. Configure 4 VM and on each VM create 51 VMIs
        4. On all VMIs enable Mirroring
        5. Verify Mirroring in Agent Introspect
        6. Verify on each VM's first interface traffic gets mirrored to analyzer
        7. Verify all 255 entries presnt on 'mirror --dump'
        8. Restart Agent and verify all 255 entries are presnt
        9. Create one more VM and enable mirroring on VMI of that VM
        10. Verify that on 256th interface morring should not work
        Pass criteria: All verification steps should pass
        Maintainer : kpatel@juniper.net
        """
        # Incresing quota to avoid resource limit during test
        quota_dict={'cores': 30, 'instances': 30}
        self.nova_h.update_quota(self.connections.project_id, **quota_dict)
        return self.verify_intf_mirroring_scale_number()
