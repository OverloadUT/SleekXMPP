"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0297 import stanza
from sleekxmppfs.plugins.xep_0297.stanza import Forwarded
from sleekxmppfs.plugins.xep_0297.forwarded import XEP_0297


register_plugin(XEP_0297)
