# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from xiru.alchemyform.browser.forms import base
from xiru.alchemyform.config import MessageFactory as _
from xiru.alchemyform.config import Session
from xiru.alchemyform.interfaces import IPessoa
from xiru.alchemyform.db import Pessoa

class PessoaAddForm(base.AddForm):
    """Formulário de cadastro de uma pessoa.
    """

    grok.context(INavigationRoot)
    grok.name('add-pessoa')
    grok.require('zope2.View')

    schema = IPessoa
    klass = Pessoa
    label = _(u'Adicionar Pessoa')
    description = _(u'Formulário de cadastro de uma pessoa.')

    def createAndAdd(self, data):
        del data['id']

        # garante que alguns campos são armazenados apenas como
        # números, mesmo sendo strings
        for campo in ('cep', 'cpf_cnpj'):
            if data[campo] is not None:
                data[campo] = ''.join([c for c in data[campo] if c.isdigit()])

        pessoa = Pessoa()
        pessoa.nome = data['nome']
        pessoa.email =  data['email']
        pessoa.endereco = data['endereco']
        pessoa.bairro = data['bairro']
        pessoa.cep = data['cep']
        pessoa.cidade = data['cidade']
        pessoa.uf_id = data['uf_id']
        pessoa.telefone = data['telefone']
        pessoa.cpf_cnpj = data['cpf_cnpj']
        pessoa.tipopessoa = data['tipopessoa']
        
        session = Session()
        session.add(pessoa)
        session.flush()

class PessoaEditForm(base.EditForm):
    """Formulário de edição de uma pessoa.
    """

    grok.context(INavigationRoot)
    grok.name('edit-pessoa')
    grok.require('zope2.View')

    schema = IPessoa
    klass = Pessoa
    label = _(u'Editar Pessoa')
    descrition = _(u'Formulário de edição de uma pessoa.')

    def applyChanges(self, data):
        content = self.getContent()
        if content:
            for k, v in data.items():

                # garante que alguns campos são armazenados apenas
                # como números, mesmo sendo strings
                if k in ('cep', 'cpf_cnpj') and v is not None:
                    v = ''.join([c for c in v if c.isdigit()])
                
                setattr(content, k, v)

class PessoaShowForm(base.ShowForm):
    """Formulário de visualização de uma pessoa.
    """
    
    grok.context(INavigationRoot)
    grok.name('show-pessoa')
    grok.require('zope2.View')

    schema = IPessoa
    klass = Pessoa
    label = _(u'Detalhes da Pessoa')
    description = _(u'Formulário de visualização de uma pessoa.')
