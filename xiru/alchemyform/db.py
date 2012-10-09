# -*- coding: utf-8 -*-

import sys
from sqlalchemy.ext.declarative import declarative_base
from xiru.alchemyform.history_meta import VersionedMeta, VersionedListener
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, Boolean, ForeignKey, func
from xiru.alchemyform.config import DEFAULT_DSN, TABLE_ARGS, CREATE_ALL_TABLES, CREATE_SAMPLES, Session
from xiru.alchemyform import interfaces

from zope.interface import implements
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base(metaclass=VersionedMeta)

if __name__ == '__main__':
    engine = create_engine(DEFAULT_DSN)
    Session = sessionmaker(bind=engine, extension=VersionedListener())

class UF(Base):
    implements(interfaces.IUF)
    __tablename__ = 'uf'
    __table_args__ = TABLE_ARGS
    id = Column(Integer, primary_key=True)
    sigla = Column(String(2), unique=True, nullable=False)
    nome = Column(String(40), unique=True, nullable=False)

class Pessoa(Base):
    implements(interfaces.IPessoa)
    __tablename__ = 'pessoa'
    __table_args__ = TABLE_ARGS
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    endereco = Column(String(100))
    bairro = Column(String(50))
    cep = Column(String(8))
    cidade = Column(String(50))
    uf_id = Column(Integer, ForeignKey('uf.id'))
    uf = relationship("UF", backref="pessoa")
    telefone = Column(String(30))
    cpf_cnpj = Column(String(20))
    tipopessoa = Column(String(1), nullable=False)

    def __repr__(self):
        return "<Pessoa:%s>" % self.email

if __name__ == '__main__':

    if CREATE_ALL_TABLES:
        metadata = Base.metadata
        metadata.drop_all(engine)
        metadata.create_all(engine)

    if not CREATE_SAMPLES:
        sys.exit()

    session = Session()

    # UF
    UFs = """
          AC Acre
          AL Alagoas
          AP Amapá
          AM Amazonas
          BA Bahia
          CE Ceará
          DF Distrito Federal
          ES Espirito Santo
          GO Goiás
          MA Maranhão
          MT Mato Grosso
          MS Mato Grosso do Sul
          MG Minas Gerais
          PA Pará
          PB Paraíba
          PR Paraná
          PE Pernambuco
          PI Piauí
          RJ Rio de Janeiro
          RN Rio Grande do Norte
          RS Rio Grande do Sul
          RO Rondônia
          RR Roraima
          SC Santa Catarina
          SP São Paulo
          SE Sergipe
          TO Tocantins
          """
    UFs = [{'sigla':uf.strip().split()[0],
            'nome':" ".join(uf.strip().split()[1:])} \
            for uf in UFs.split('\n') if uf.strip()]
    for uf in UFs:
        uf1 = UF(sigla=uf['sigla'], nome=uf['nome'])
        session.add(uf1)

    # Pessoa
    ps1 = Pessoa(nome=u'Xiru',
                 email=u'xiru@xiru.org',
                 tipopessoa='F')
    session.add(ps1)
    ps2 = Pessoa(nome=u'Tião Macalé',
                 email=u'tiao@macale.net',
                 uf_id=4,
                 tipopessoa='F')
    session.add(ps2)

    session.commit()
