"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmppfs.xmlstream.handler.callback import Callback
from sleekxmppfs.xmlstream.handler.collector import Collector
from sleekxmppfs.xmlstream.handler.waiter import Waiter
from sleekxmppfs.xmlstream.handler.xmlcallback import XMLCallback
from sleekxmppfs.xmlstream.handler.xmlwaiter import XMLWaiter

__all__ = ['Callback', 'Waiter', 'XMLCallback', 'XMLWaiter']
