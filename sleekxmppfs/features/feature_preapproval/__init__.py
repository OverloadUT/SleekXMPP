"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.features.feature_preapproval.preapproval import FeaturePreApproval
from sleekxmppfs.features.feature_preapproval.stanza import PreApproval


register_plugin(FeaturePreApproval)
