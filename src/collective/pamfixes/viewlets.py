# -*- coding: utf-8 -*-
"""collective.pamfixes custom viewlets."""

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.multilingual.interfaces import ITranslationManager
from plone.memoize import ram
from zope.component import getUtility

from plone.app.multilingual.browser.viewlets import (
    _cache_until_catalog_change,
    AlternateLanguagesViewlet)


class CustomAlternateLanguagesViewlet(AlternateLanguagesViewlet):
    """Notify search engines about alternates languages of current content
    item.
    """

    @ram.cache(_cache_until_catalog_change)
    def get_alternate_languages(self):
        """Cache relative urls only. If we have multilingual sites and multi
        domain site caching absolute urls will result in very inefficient
        caching. Build absolute url in template.
        """
        tm = ITranslationManager(self.context)
        catalog = getToolByName(self.context, 'portal_catalog')
        results = catalog(TranslationGroup=tm.query_canonical())

        plone_site = getUtility(IPloneSiteRoot)
        portal_path = '/'.join(plone_site.getPhysicalPath())
        portal_path_len = len(portal_path)

        alternates = []
        for item in results:
            url = item.getURL(relative=1)
            path_len = len('{0:s}/'.format(item.Language))
            if url.startswith(portal_path):
                path_len += portal_path_len
            url = url[path_len:]
            alternates.append({
                'lang': item.Language,
                'url': url.strip('/'),
            })

        return alternates
