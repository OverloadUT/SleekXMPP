"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0108 import stanza
from sleekxmppfs.plugins.xep_0108.stanza import UserActivity
from sleekxmppfs.plugins.xep_0108.user_activity import XEP_0108


register_plugin(XEP_0108)
