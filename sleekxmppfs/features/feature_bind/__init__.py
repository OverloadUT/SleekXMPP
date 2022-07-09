"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.features.feature_bind.bind import FeatureBind
from sleekxmppfs.features.feature_bind.stanza import Bind


register_plugin(FeatureBind)


# Retain some backwards compatibility
feature_bind = FeatureBind
