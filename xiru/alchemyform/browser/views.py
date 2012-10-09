# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from xiru.alchemyform.nav import url

class BaseListView(object):

    grok.context(INavigationRoot)

    def show_url(self, id, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('show-'+vs, id=id)

    def add_url(self, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('add-'+vs)
