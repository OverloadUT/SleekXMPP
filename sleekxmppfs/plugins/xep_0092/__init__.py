"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0092 import stanza
from sleekxmppfs.plugins.xep_0092.stanza import Version
from sleekxmppfs.plugins.xep_0092.version import XEP_0092


register_plugin(XEP_0092)


# Retain some backwards compatibility
xep_0092 = XEP_0092
