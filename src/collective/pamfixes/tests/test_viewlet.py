# -*- coding: utf-8 -*-
"""Test viewlet of collective.pamfixes."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# plone imports
from plone.app.multilingual.browser.setup import SetupMultilingualSite

# local imports
from collective.pamfixes import testing
from collective.pamfixes.viewlets import CustomAlternateLanguagesViewlet


class TestViewlet(unittest.TestCase):
    """Validate setup process for collective.pamfixes."""

    layer = testing.COLLECTIVE_PAMFIXES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']

        # Setup language root folders
        setup_tool = SetupMultilingualSite()
        setup_tool.setupSite(self.portal)

    def test_viewlet_render(self):
        """Validate that the alternate languages viewlet renders correctly."""
        viewlet = CustomAlternateLanguagesViewlet(
            self.portal['en'],
            self.app.REQUEST,
            None,
        )
        viewlet.update()
        self.assertTrue(len(viewlet.alternates), 3)

        viewlet = CustomAlternateLanguagesViewlet(
            self.portal['es'],
            self.app.REQUEST,
            None,
        )
        viewlet.update()
        self.assertTrue(len(viewlet.alternates), 3)

        viewlet = CustomAlternateLanguagesViewlet(
            self.portal['de'],
            self.app.REQUEST,
            None,
        )
        viewlet.update()
        self.assertTrue(len(viewlet.alternates), 3)
