"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permissio
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0308.stanza import Replace
from sleekxmppfs.plugins.xep_0308.correction import XEP_0308


register_plugin(XEP_0308)
