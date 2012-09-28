# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from xiru.alchemyform.config import Session
from xiru.alchemyform import db
from xiru.alchemyform.config import MessageFactory as _
from xiru.alchemyform.nav import url

class BaseListView(object):
    
    def show_url(self, id, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('show-'+vs, id=id)

    def add_url(self, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('add-'+vs)

class UFListView(grok.View, BaseListView):

    grok.name('list-uf')
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')

    dados = []
    view_sufix = 'uf'

    def update(self):
        self.request.set('disable_border', True)
        self.dados = []
        session = Session()
        items = session.query(db.UF).all()
        for i in items:
            self.dados.append({
               'id': i.id,
               'sigla': i.sigla,
               'nome': i.nome,
               })

class PessoaListView(grok.View, BaseListView):
    
    grok.name('list-pessoa')
    grok.context(INavigationRoot)
    grok.require('zope2.View')

    dados = []
    view_sufix = 'pessoa'

    def update(self):
        self.request.set('disable_border', True)
        self.dados = []
        session = Session()
        items = session.query(db.Pessoa).all()
        for i in items:
            self.dados.append({
               'id': i.id,
               'nome': i.nome,
               'email': i.email,
               })
