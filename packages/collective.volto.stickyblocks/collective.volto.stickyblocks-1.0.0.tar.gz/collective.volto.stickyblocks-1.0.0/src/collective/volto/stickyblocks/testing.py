# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    PLONE_FIXTURE,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import collective.volto.stickyblocks


class CollectiveVoltoStickyblocksLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.stickyblocks)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.stickyblocks:default")


COLLECTIVE_VOLTO_STICKYBLOCKS_FIXTURE = CollectiveVoltoStickyblocksLayer()


COLLECTIVE_VOLTO_STICKYBLOCKS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_VOLTO_STICKYBLOCKS_FIXTURE,),
    name="CollectiveVoltoStickyblocksLayer:IntegrationTesting",
)


COLLECTIVE_VOLTO_STICKYBLOCKS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_VOLTO_STICKYBLOCKS_FIXTURE,),
    name="CollectiveVoltoStickyblocksLayer:FunctionalTesting",
)


COLLECTIVE_VOLTO_STICKYBLOCKS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_VOLTO_STICKYBLOCKS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveVoltoStickyblocksLayer:AcceptanceTesting",
)
