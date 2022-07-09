"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.features.feature_mechanisms.mechanisms import FeatureMechanisms
from sleekxmppfs.features.feature_mechanisms.stanza import Mechanisms
from sleekxmppfs.features.feature_mechanisms.stanza import Auth
from sleekxmppfs.features.feature_mechanisms.stanza import Success
from sleekxmppfs.features.feature_mechanisms.stanza import Failure


register_plugin(FeatureMechanisms)


# Retain some backwards compatibility
feature_mechanisms = FeatureMechanisms
