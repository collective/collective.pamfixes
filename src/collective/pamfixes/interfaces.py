# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.app.multilingual.interfaces import IPloneAppMultilingualInstalled

# from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectivePamfixesLayer(IPloneAppMultilingualInstalled):
    """Marker interface that defines a browser layer."""
