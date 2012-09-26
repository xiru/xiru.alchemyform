# -*- coding: utf-8 -*-

# Banco de Dados #
DEFAULT_DSN = 'mysql://root:root@localhost/agenda?charset=utf8'
TABLE_ARGS = {'mysql_engine':'InnoDB','mysql_charset':'utf8'}
CREATE_ALL_TABLES = True
CREATE_SAMPLES = True
DISABLE_VERSIONS = True

# Validação de e-mails #
EMAIL_RE = "^([0-9a-zA-Z_&.'+-]+!)*[0-9a-zA-Z_&.'+-]+@(([0-9a-zA-Z]([0-9a-zA-Z-]*[0-9a-z-A-Z])?\.)+[a-zA-Z]{2,6}|([0-9]{1,3}\.){3}[0-9]{1,3})$"

from z3c.saconfig import named_scoped_session
def Session():
    return named_scoped_session('alchemyform_session')

import zope.i18nmessageid
MessageFactory = zope.i18nmessageid.MessageFactory('xiru.alchemyform')
