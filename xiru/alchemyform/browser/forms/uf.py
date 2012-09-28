# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from xiru.alchemyform.browser.forms import base
from xiru.alchemyform.config import MessageFactory as _
from xiru.alchemyform.config import Session
from xiru.alchemyform.interfaces import IUF
from xiru.alchemyform.db import UF

class UFAddForm(base.AddForm):
    """Formulário de cadastro de uma UF.
    """

    grok.context(INavigationRoot)
    grok.name('add-uf')
    grok.require('cmf.ManagePortal')

    schema = IUF
    klass = UF
    label = _(u'Adicionar UF')
    description = _(u'Formulário de cadastro de uma UF.')

    def createAndAdd(self, data):
        uf = UF()
        uf.sigla = data['sigla']
        uf.nome = data['nome']
        session = Session()
        session.add(uf)
        session.flush()

class UFEditForm(base.EditForm):
    """Formulário de edição de uma UF.
    """

    grok.context(INavigationRoot)
    grok.name('edit-uf')
    grok.require('cmf.ManagePortal')

    schema = IUF
    klass = UF
    label = _(u'Editar UF')
    descrition = _(u'Formulário de edição de uma UF.')

class UFShowForm(base.ShowForm):
    """Formulário de visualização de uma UF.
    """
    
    grok.context(INavigationRoot)
    grok.name('show-uf')
    grok.require('cmf.ManagePortal')

    schema = IUF
    klass = UF
    label = _(u'Detalhes da UF')
    description = _(u'Formulário de visualização de uma UF.')
