# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.pamfixes


class CollectivePamfixesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.pamfixes)

    def setUpPloneSite(self, portal):
        return


COLLECTIVE_PAMFIXES_FIXTURE = CollectivePamfixesLayer()


COLLECTIVE_PAMFIXES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PAMFIXES_FIXTURE,),
    name='CollectivePamfixesLayer:IntegrationTesting'
)


COLLECTIVE_PAMFIXES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PAMFIXES_FIXTURE,),
    name='CollectivePamfixesLayer:FunctionalTesting'
)


COLLECTIVE_PAMFIXES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PAMFIXES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectivePamfixesLayer:AcceptanceTesting'
)
