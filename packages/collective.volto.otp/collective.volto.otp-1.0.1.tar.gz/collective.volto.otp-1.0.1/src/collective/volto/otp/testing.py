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

import collective.volto.otp


class CollectiveVoltoOtpLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.otp)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.otp:default")


COLLECTIVE_VOLTO_OTP_FIXTURE = CollectiveVoltoOtpLayer()


COLLECTIVE_VOLTO_OTP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_VOLTO_OTP_FIXTURE,),
    name="CollectiveVoltoOtpLayer:IntegrationTesting",
)


COLLECTIVE_VOLTO_OTP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_VOLTO_OTP_FIXTURE,),
    name="CollectiveVoltoOtpLayer:FunctionalTesting",
)


COLLECTIVE_VOLTO_OTP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_VOLTO_OTP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveVoltoOtpLayer:AcceptanceTesting",
)
