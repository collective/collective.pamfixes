# -*- coding: utf-8 -*-
"""collective.pamfixes interfaces."""

# python imports
import pkg_resources
from pkg_resources import parse_version


pam_distribution = pkg_resources.get_distribution('plone.app.multilingual')
pam_version = pam_distribution.version

# version-dependent import
if parse_version(pam_version) < parse_version('2.0'):
    from plone.multilingual.interfaces import (
        ITranslatable,
        ITranslationManager)
else:
    from plone.app.multilingual.interfaces import (
        ITranslatable,
        ITranslationManager)

ITranslatable  # noqa
ITranslationManager  # noqa
