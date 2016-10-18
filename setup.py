#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-cesc.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-cesc.png'])
    ]

setup(
    name="Electrum-CESC",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'dnspython',
        'jsonrpclib',
    ],
    packages=[
        'electrum_cesc',
        'electrum_cesc_gui',
        'electrum_cesc_gui.qt',
        'electrum_cesc_plugins',
        'electrum_cesc_plugins.audio_modem',
        'electrum_cesc_plugins.cosigner_pool',
        'electrum_cesc_plugins.email_requests',
        'electrum_cesc_plugins.exchange_rate',
        'electrum_cesc_plugins.hw_wallet',
        'electrum_cesc_plugins.keepkey',
        'electrum_cesc_plugins.labels',
        'electrum_cesc_plugins.ledger',
        'electrum_cesc_plugins.plot',
        'electrum_cesc_plugins.trezor',
        'electrum_cesc_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_cesc': 'lib',
        'electrum_cesc_gui': 'gui',
        'electrum_cesc_plugins': 'plugins',
    },
    package_data={
        'electrum_cesc': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-cesc'],
    data_files=data_files,
    description="Lightweight Cryptoescudo Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="http://electrum-cesc.org",
    long_description="""Lightweight Cryptoescudo Wallet"""
)
