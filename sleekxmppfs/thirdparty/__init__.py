try:
    from collections import OrderedDict
except:
    from sleekxmppfs.thirdparty.ordereddict import OrderedDict

try:
    from gnupg import GPG
except:
    from sleekxmppfs.thirdparty.gnupg import GPG

from sleekxmppfs.thirdparty import socks
from sleekxmppfs.thirdparty.mini_dateutil import tzutc, tzoffset, parse_iso
from sleekxmppfs.thirdparty.orderedset import OrderedSet
