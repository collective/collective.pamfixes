# -*- coding: utf-8 -*-
"""Test setup for collective.pamfixes"""

# plone imports
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
    setRoles,
    TEST_USER_ID,
)

# local imports
import collective.pamfixes


class CollectivePamfixesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.pamfixes)
        self.loadZCML(name='testing.zcml', package=collective.pamfixes)
        self.loadZCML(name='overrides.zcml', package=collective.pamfixes)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.pamfixes:testfixture')

        # Empower test user
        setRoles(portal, TEST_USER_ID, ['Manager'])


COLLECTIVE_PAMFIXES_FIXTURE = CollectivePamfixesLayer()


COLLECTIVE_PAMFIXES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PAMFIXES_FIXTURE,),
    name='CollectivePamfixesLayer:IntegrationTesting'
)


COLLECTIVE_PAMFIXES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PAMFIXES_FIXTURE,),
    name='CollectivePamfixesLayer:FunctionalTesting'
)
