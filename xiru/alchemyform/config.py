# -*- coding: utf-8 -*-

# Default database #
DEFAULT_DSN = 'mysql://root:root@localhost/alchemy_form?charset=utf8'
TABLE_ARGS = {}
DISABLE_VERSIONS = False

from z3c.saconfig import named_scoped_session
def Session():
    return named_scoped_session('alchemyform_session')

import zope.i18nmessageid
MessageFactory = zope.i18nmessageid.MessageFactory('xiru.alchemyform')
