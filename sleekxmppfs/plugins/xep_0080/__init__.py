"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010 Nathanael C. Fritz, Erik Reuterborg Larsson
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0080.stanza import Geoloc
from sleekxmppfs.plugins.xep_0080.geoloc import XEP_0080


register_plugin(XEP_0080)
