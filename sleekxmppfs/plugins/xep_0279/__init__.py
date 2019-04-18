"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0279 import stanza
from sleekxmppfs.plugins.xep_0279.stanza import IPCheck
from sleekxmppfs.plugins.xep_0279.ipcheck import XEP_0279


register_plugin(XEP_0279)
