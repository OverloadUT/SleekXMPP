"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

import logging
if hasattr(logging, 'NullHandler'):
    NullHandler = logging.NullHandler
else:
    class NullHandler(logging.Handler):
        def handle(self, record):
            pass
logging.getLogger(__name__).addHandler(NullHandler())
del NullHandler


from sleekxmppfs.stanza import Message, Presence, Iq
from sleekxmppfs.jid import JID, InvalidJID
from sleekxmppfs.xmlstream.stanzabase import ET, ElementBase, register_stanza_plugin
from sleekxmppfs.xmlstream.handler import *
from sleekxmppfs.xmlstream import XMLStream, RestartStream
from sleekxmppfs.xmlstream.matcher import *
from sleekxmppfs.basexmpp import BaseXMPP
from sleekxmppfs.clientxmpp import ClientXMPP
from sleekxmppfs.componentxmpp import ComponentXMPP

from sleekxmppfs.version import __version__, __version_info__
