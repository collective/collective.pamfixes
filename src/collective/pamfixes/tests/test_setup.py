# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.pamfixes.testing import COLLECTIVE_PAMFIXES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.pamfixes is properly installed."""

    layer = COLLECTIVE_PAMFIXES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.pamfixes is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.pamfixes'))

    def test_browserlayer(self):
        """Test that ICollectivePamfixesLayer is registered."""
        from collective.pamfixes.interfaces import (
            ICollectivePamfixesLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectivePamfixesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_PAMFIXES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.pamfixes'])

    def test_product_uninstalled(self):
        """Test if collective.pamfixes is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.pamfixes'))

    def test_browserlayer_removed(self):
        """Test that ICollectivePamfixesLayer is removed."""
        from collective.pamfixes.interfaces import ICollectivePamfixesLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectivePamfixesLayer, utils.registered_layers())
