"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0196 import stanza
from sleekxmppfs.plugins.xep_0196.stanza import UserGaming
from sleekxmppfs.plugins.xep_0196.user_gaming import XEP_0196


register_plugin(XEP_0196)
