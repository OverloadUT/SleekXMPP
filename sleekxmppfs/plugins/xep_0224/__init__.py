"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0224 import stanza
from sleekxmppfs.plugins.xep_0224.stanza import Attention
from sleekxmppfs.plugins.xep_0224.attention import XEP_0224


register_plugin(XEP_0224)


# Retain some backwards compatibility
xep_0224 = XEP_0224
