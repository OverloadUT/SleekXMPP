#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007-2011 Nathanael C. Fritz
# All Rights Reserved
#
# This software is licensed as described in the README.rst and LICENSE
# file, which you should have received as part of this distribution.

import sys
import codecs
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command
# from ez_setup import use_setuptools

from testall import TestCommand
from sleekxmppfs.version import __version__
# if 'cygwin' in sys.platform.lower():
#     min_version = '0.6c6'
# else:
#     min_version = '0.6a9'
#
# try:
#     use_setuptools(min_version=min_version)
# except TypeError:
#     # locally installed ez_setup won't have min_version
#     use_setuptools()
#
# from setuptools import setup, find_packages, Extension, Feature

VERSION          = __version__
DESCRIPTION      = 'A fork of SleekXMPP with TLS cert validation disabled, intended only to be used with the sucks project'
with codecs.open('README.rst', 'r', encoding='UTF-8') as readme:
    LONG_DESCRIPTION = ''.join(readme)

CLASSIFIERS      = [ 'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                   ]

packages     = [ 'sleekxmppfs',
                 'sleekxmppfs/stanza',
                 'sleekxmppfs/test',
                 'sleekxmppfs/roster',
                 'sleekxmppfs/util',
                 'sleekxmppfs/util/sasl',
                 'sleekxmppfs/xmlstream',
                 'sleekxmppfs/xmlstream/matcher',
                 'sleekxmppfs/xmlstream/handler',
                 'sleekxmppfs/plugins',
                 'sleekxmppfs/plugins/xep_0004',
                 'sleekxmppfs/plugins/xep_0004/stanza',
                 'sleekxmppfs/plugins/xep_0009',
                 'sleekxmppfs/plugins/xep_0009/stanza',
                 'sleekxmppfs/plugins/xep_0012',
                 'sleekxmppfs/plugins/xep_0013',
                 'sleekxmppfs/plugins/xep_0016',
                 'sleekxmppfs/plugins/xep_0020',
                 'sleekxmppfs/plugins/xep_0027',
                 'sleekxmppfs/plugins/xep_0030',
                 'sleekxmppfs/plugins/xep_0030/stanza',
                 'sleekxmppfs/plugins/xep_0033',
                 'sleekxmppfs/plugins/xep_0047',
                 'sleekxmppfs/plugins/xep_0048',
                 'sleekxmppfs/plugins/xep_0049',
                 'sleekxmppfs/plugins/xep_0050',
                 'sleekxmppfs/plugins/xep_0054',
                 'sleekxmppfs/plugins/xep_0059',
                 'sleekxmppfs/plugins/xep_0060',
                 'sleekxmppfs/plugins/xep_0060/stanza',
                 'sleekxmppfs/plugins/xep_0065',
                 'sleekxmppfs/plugins/xep_0066',
                 'sleekxmppfs/plugins/xep_0071',
                 'sleekxmppfs/plugins/xep_0077',
                 'sleekxmppfs/plugins/xep_0078',
                 'sleekxmppfs/plugins/xep_0080',
                 'sleekxmppfs/plugins/xep_0084',
                 'sleekxmppfs/plugins/xep_0085',
                 'sleekxmppfs/plugins/xep_0086',
                 'sleekxmppfs/plugins/xep_0091',
                 'sleekxmppfs/plugins/xep_0092',
                 'sleekxmppfs/plugins/xep_0095',
                 'sleekxmppfs/plugins/xep_0096',
                 'sleekxmppfs/plugins/xep_0107',
                 'sleekxmppfs/plugins/xep_0108',
                 'sleekxmppfs/plugins/xep_0115',
                 'sleekxmppfs/plugins/xep_0118',
                 'sleekxmppfs/plugins/xep_0122',
                 'sleekxmppfs/plugins/xep_0128',
                 'sleekxmppfs/plugins/xep_0131',
                 'sleekxmppfs/plugins/xep_0152',
                 'sleekxmppfs/plugins/xep_0153',
                 'sleekxmppfs/plugins/xep_0172',
                 'sleekxmppfs/plugins/xep_0184',
                 'sleekxmppfs/plugins/xep_0186',
                 'sleekxmppfs/plugins/xep_0191',
                 'sleekxmppfs/plugins/xep_0196',
                 'sleekxmppfs/plugins/xep_0198',
                 'sleekxmppfs/plugins/xep_0199',
                 'sleekxmppfs/plugins/xep_0202',
                 'sleekxmppfs/plugins/xep_0203',
                 'sleekxmppfs/plugins/xep_0221',
                 'sleekxmppfs/plugins/xep_0224',
                 'sleekxmppfs/plugins/xep_0231',
                 'sleekxmppfs/plugins/xep_0235',
                 'sleekxmppfs/plugins/xep_0249',
                 'sleekxmppfs/plugins/xep_0257',
                 'sleekxmppfs/plugins/xep_0258',
                 'sleekxmppfs/plugins/xep_0279',
                 'sleekxmppfs/plugins/xep_0280',
                 'sleekxmppfs/plugins/xep_0297',
                 'sleekxmppfs/plugins/xep_0308',
                 'sleekxmppfs/plugins/xep_0313',
                 'sleekxmppfs/plugins/xep_0319',
                 'sleekxmppfs/plugins/xep_0323',
                 'sleekxmppfs/plugins/xep_0323/stanza',
                 'sleekxmppfs/plugins/xep_0325',
                 'sleekxmppfs/plugins/xep_0325/stanza',
                 'sleekxmppfs/plugins/xep_0332',
                 'sleekxmppfs/plugins/xep_0332/stanza',
                 'sleekxmppfs/plugins/google',
                 'sleekxmppfs/plugins/google/gmail',
                 'sleekxmppfs/plugins/google/auth',
                 'sleekxmppfs/plugins/google/settings',
                 'sleekxmppfs/plugins/google/nosave',
                 'sleekxmppfs/features',
                 'sleekxmppfs/features/feature_mechanisms',
                 'sleekxmppfs/features/feature_mechanisms/stanza',
                 'sleekxmppfs/features/feature_starttls',
                 'sleekxmppfs/features/feature_bind',
                 'sleekxmppfs/features/feature_session',
                 'sleekxmppfs/features/feature_rosterver',
                 'sleekxmppfs/features/feature_preapproval',
                 'sleekxmppfs/thirdparty',
                 ]

setup(
    name             = "sleekxmppfs",
    version          = VERSION,
    description      = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author       = 'Alex Szymanik',
    author_email = 'aszymanik@gmail.com',
    url          = 'http://github.com/aszymanik/SleekXMPP',
    license      = 'MIT',
    platforms    = [ 'any' ],
    packages     = packages,
    requires     = [ 'dnspython', 'pyasn1', 'pyasn1_modules' ],
    classifiers  = CLASSIFIERS,
    cmdclass     = {'test': TestCommand}
)
