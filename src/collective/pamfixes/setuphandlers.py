# -*- coding: utf-8 -*-
"""Post install import steps for collective.pamfixes."""

# zope imports
from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from zope.interface import implementer

# local imports
from collective.pamfixes import logger


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.pamfixes:testfixture',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def post_install_testfixture(context):
    """Post install script for testfixture environments."""
    if is_not_testfixture_profile(context):
        return
    setup_pam(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def is_not_testfixture_profile(context):
    return context.readDataFile(
        'collectivepamfixes_testfixture_marker.txt'
    ) is None


def setup_pam(context):
    """Setup a multilingual site using p.a.m."""
    try:
        from plone.app.multilingual.browser.setup import SetupMultilingualSite
    except ImportError:
        logger.info(
            'plone.app.multilingual is not available. '
            'The setup of a multilingual site is not possible.'
        )
        return

    # Define available languages
    language_tool = api.portal.get_tool(name='portal_languages')
    languages = language_tool.getSupportedLanguages()
    for lang in ['en', 'es', 'de']:
        if lang not in languages:
            language_tool.addSupportedLanguage(lang)

    # Enable request negotiator
    language_tool.use_request_negotiation = True

    site = api.portal.get()
    setup_tool = SetupMultilingualSite()
    setup_tool.setupSite(site)
    try:
        SetupMultilingualSite(site).move_default_language_content()
    except AttributeError:
        logger.info('move_default_language_content not supported.')
    logger.info('Setup of multilingual site finished.')
