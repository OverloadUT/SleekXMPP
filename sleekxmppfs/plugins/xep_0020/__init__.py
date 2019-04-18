"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2013 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0020 import stanza
from sleekxmppfs.plugins.xep_0020.stanza import FeatureNegotiation
from sleekxmppfs.plugins.xep_0020.feature_negotiation import XEP_0020


register_plugin(XEP_0020)
