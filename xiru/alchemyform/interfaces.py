# -*- coding: utf-8 -*-

import re
from plone.directives import form
from zope import interface, schema
from xiru.alchemyform.config import MessageFactory as _
from xiru.alchemyform.config import EMAIL_RE
from xiru.alchemyform.util import valida_cpf_cnpj

# Formulários #

class IUF(form.Schema):

    form.mode(id='hidden')
    id = schema.Int(
        title=_(u'ID'),
        description=_(u'Identificador da UF.'),
        required=False)

    sigla = schema.TextLine(
        title=_(u'Sigla'),
        description=_(u'Informe a sigla da UF.'))

    nome = schema.TextLine(
        title=_(u'Nome'),
        description=_(u'Informe o nome da UF.'))

class IPessoa(form.Schema): 
    
    """ Interface que descreve representações de Pessoa.
    """

    form.fieldset('endereco',
      label=u"Endereço",
      fields=['endereco', 'bairro', 'cep', 'cidade', 'uf_id'])

    form.mode(id='hidden')
    id = schema.Int(
        title=_(u'ID'),
        description=_(u'Identificador da Pessoa.'),
        required=False)

    nome = schema.TextLine(
        title=_(u'Nome'),
        description=_(u'Nome completo da Pessoa.'),
        max_length=100)

    email = schema.TextLine(
        title=_(u'Email'),
        description=_(u'Informe o email da Pessoa.'),
        max_length=254)

    endereco = schema.TextLine(
        title=_(u'Endereço'),
        description=_(u'Logradouro, número e complemento.'),
        max_length=100,
        required=False)

    bairro = schema.TextLine(
        title=_(u'Bairro'),
        description=_(u'Informe o bairro.'),
        max_length=50,
        required=False)

    cep = schema.TextLine(
        title=_(u'CEP'),
        description=_(u'Informe o CEP (apenas números)'),
        required=False)

    cidade = schema.TextLine(
        title=_(u'Cidade'),
        description=_(u'Informe a cidade.'),
        max_length=50,
        required=False)

    uf_id = schema.Choice(
        title=_(u'UF'),
        description=_(u'Selecione o estado da federação.'),
        required=False,
        vocabulary='xiru.alchemyform.uf-vocab')

    tipopessoa = schema.Choice(
        title=_(u'Tipo'),
        description=_(u'Informe se a pessoa é física ou uma organização.'),
        default=u'F',
        vocabulary='xiru.alchemyform.tipopessoa-vocab')

    cpf_cnpj = schema.TextLine(
        title=_(u'CPF/CNPJ'),
        description=_(u'Informe o CPF ou CNPJ de acordo com o tipo de pessoa: física ou organização.'),
        max_length=20,
        required=False)

    telefone = schema.TextLine(
        title=_(u'Telefone'),
        description=_(u'Informe o telefone com DDD.'),
        max_length=30,
        required=False)

# Validadores #

@form.validator(field=IPessoa['cep'])
def validateCep(value):
    if value:
        value = ''.join([c for c in value if c.isdigit()])
        if len(value) != 8:
            raise interface.Invalid(_(u'CEP inválido.'))

@form.validator(field=IPessoa['email'])
def validateEmail(value):
    if value and re.compile(EMAIL_RE).match(value) is None:
        raise interface.Invalid(_(u'E-mail inválido.'))

@form.validator(field=IPessoa['cpf_cnpj'])
def validateCPFCNPJ(value):
    if value and not valida_cpf_cnpj(value):
        raise interface.Invalid(_(u'CPF/CNPJ inválido.'))
