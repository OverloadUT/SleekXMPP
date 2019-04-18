"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""


from sleekxmppfs.stanza import Message, Presence
from sleekxmppfs.xmlstream import register_stanza_plugin
from sleekxmppfs.plugins import BasePlugin
from sleekxmppfs.plugins.xep_0091 import stanza


class XEP_0091(BasePlugin):

    """
    XEP-0091: Legacy Delayed Delivery
    """

    name = 'xep_0091'
    description = 'XEP-0091: Legacy Delayed Delivery'
    dependencies = set()
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Message, stanza.LegacyDelay)
        register_stanza_plugin(Presence, stanza.LegacyDelay)
