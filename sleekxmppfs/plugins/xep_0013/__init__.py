"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permissio
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0013.stanza import Offline
from sleekxmppfs.plugins.xep_0013.offline import XEP_0013


register_plugin(XEP_0013)
