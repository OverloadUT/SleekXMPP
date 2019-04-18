"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0235 import stanza
from sleekxmppfs.plugins.xep_0235.stanza import OAuth
from sleekxmppfs.plugins.xep_0235.oauth import XEP_0235


register_plugin(XEP_0235)
