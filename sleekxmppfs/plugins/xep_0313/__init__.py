"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permissio
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0313.stanza import Result, MAM, Preferences
from sleekxmppfs.plugins.xep_0313.mam import XEP_0313


register_plugin(XEP_0313)
