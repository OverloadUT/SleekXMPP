"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0172 import stanza
from sleekxmppfs.plugins.xep_0172.stanza import UserNick
from sleekxmppfs.plugins.xep_0172.user_nick import XEP_0172


register_plugin(XEP_0172)
