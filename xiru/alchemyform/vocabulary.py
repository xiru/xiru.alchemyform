# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import provideUtility
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from xiru.alchemyform.config import Session
from xiru.alchemyform import db
from xiru.alchemyform.config import MessageFactory as _
               
class UFVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        session = Session()
        query = session.query(db.UF).order_by(db.UF.nome).all()
        return SimpleVocabulary([SimpleTerm(a.id, a.id, a.nome) for a in query])

UFVocabularyFactory = UFVocabulary()
provideUtility(UFVocabularyFactory, IVocabularyFactory,
               name='xiru.alchemyform.uf-vocab')

               
def TipoPessoaVocabulary(context):
    return SimpleVocabulary([
        SimpleTerm('F','F', _(u'Física')),
        SimpleTerm('O','O', _(u'Organização')),
    ])

provideUtility(TipoPessoaVocabulary, IVocabularyFactory,
               name='xiru.alchemyform.tipopessoa-vocab')
