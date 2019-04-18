"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0091 import stanza
from sleekxmppfs.plugins.xep_0091.stanza import LegacyDelay
from sleekxmppfs.plugins.xep_0091.legacy_delay import XEP_0091


register_plugin(XEP_0091)
