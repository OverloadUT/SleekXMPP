"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.features.feature_starttls.starttls import FeatureSTARTTLS
from sleekxmppfs.features.feature_starttls.stanza import *


register_plugin(FeatureSTARTTLS)


# Retain some backwards compatibility
feature_starttls = FeatureSTARTTLS
