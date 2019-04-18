"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.xmlstream.matcher.id import MatcherId
from sleekxmppfs.xmlstream.matcher.idsender import MatchIDSender
from sleekxmppfs.xmlstream.matcher.many import MatchMany
from sleekxmppfs.xmlstream.matcher.stanzapath import StanzaPath
from sleekxmppfs.xmlstream.matcher.xmlmask import MatchXMLMask
from sleekxmppfs.xmlstream.matcher.xpath import MatchXPath

__all__ = ['MatcherId', 'MatchMany', 'StanzaPath',
           'MatchXMLMask', 'MatchXPath']
