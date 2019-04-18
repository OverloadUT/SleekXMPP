from sleekxmppfs.plugins.base import register_plugin

from sleekxmppfs.plugins.xep_0065.stanza import Socks5
from sleekxmppfs.plugins.xep_0065.proxy import XEP_0065


register_plugin(XEP_0065)
