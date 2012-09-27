# -*- coding: utf-8 -*-

from zope.component import provideUtility
from zope.component.interfaces import ComponentLookupError
from zope.app.component.hooks import getSite
from z3c.saconfig import EngineFactory, GloballyScopedSession, SiteScopedSession
from z3c.saconfig.interfaces import IEngineFactory, IScopedSession
from collective.saconnect.interfaces import ISQLAlchemyConnectionStrings
from Products.CMFCore.utils import getToolByName

from xiru.alchemyform.config import DEFAULT_DSN
from xiru.alchemyform.history_meta import ZopeVersionedExtension

class AlchemyFormEngineFactory(EngineFactory):

    def configuration(self):
        urltool = getToolByName(getSite(), 'portal_url')
        portal = urltool.getPortalObject()
        try:
            saconnect = ISQLAlchemyConnectionStrings(portal)
            dsn = saconnect['alchemyform']
        except (ComponentLookupError, KeyError), e:
            dsn = DEFAULT_DSN
        return (dsn,),{}

AlchemyFormEngineGlobalUtility = EngineFactory(DEFAULT_DSN)
provideUtility(AlchemyFormEngineGlobalUtility, provides=IEngineFactory, name=u'alchemyform_engine')

def ScopeID():
    urltool = getToolByName(getSite(), 'portal_url')
    obj = urltool.getPortalObject()
    return '-'.join(obj.getPhysicalPath()[1:])

# SiteScopedSession - um banco de dados por site
class AlchemyFormSiteScopedSession(SiteScopedSession):
    def siteScopeFunc(self):
        return ScopeID()
provideUtility(AlchemyFormSiteScopedSession(u'alchemyform_engine', extension=ZopeVersionedExtension()), provides=IScopedSession, name=u'alchemyform_session')
