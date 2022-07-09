"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2013 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0319 import stanza
from sleekxmppfs.plugins.xep_0319.stanza import Idle
from sleekxmppfs.plugins.xep_0319.idle import XEP_0319


register_plugin(XEP_0319)
