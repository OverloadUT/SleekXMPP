"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.features.feature_rosterver.rosterver import FeatureRosterVer
from sleekxmppfs.features.feature_rosterver.stanza import RosterVer


register_plugin(FeatureRosterVer)


# Retain some backwards compatibility
feature_rosterver = FeatureRosterVer
