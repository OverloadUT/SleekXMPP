"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0084 import stanza
from sleekxmppfs.plugins.xep_0084.stanza import Data, MetaData
from sleekxmppfs.plugins.xep_0084.avatar import XEP_0084


register_plugin(XEP_0084)
