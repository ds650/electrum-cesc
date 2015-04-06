#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-cesc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-cesc.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-cesc")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-CESC",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'cesc_scrypt'],
    package_dir={
        'electrum_cesc': 'lib',
        'electrum_cesc_gui': 'gui',
        'electrum_cesc_plugins': 'plugins',
    },
    scripts=['electrum-cesc'],
    data_files=data_files,
    py_modules=[
        'electrum_cesc.account',
        'electrum_cesc.bitcoin',
        'electrum_cesc.blockchain',
        'electrum_cesc.bmp',
        'electrum_cesc.commands',
        'electrum_cesc.daemon',
        'electrum_cesc.i18n',
        'electrum_cesc.interface',
        'electrum_cesc.mnemonic',
        'electrum_cesc.msqr',
        'electrum_cesc.network',
        'electrum_cesc.plugins',
        'electrum_cesc.pyqrnative',
        'electrum_cesc.scrypt',
        'electrum_cesc.simple_config',
        'electrum_cesc.socks',
        'electrum_cesc.synchronizer',
        'electrum_cesc.transaction',
        'electrum_cesc.util',
        'electrum_cesc.verifier',
        'electrum_cesc.version',
        'electrum_cesc.wallet',
        'electrum_cesc.wallet_bitkey',
        'electrum_cesc_gui.gtk',
        'electrum_cesc_gui.qt.__init__',
        'electrum_cesc_gui.qt.amountedit',
        'electrum_cesc_gui.qt.console',
        'electrum_cesc_gui.qt.history_widget',
        'electrum_cesc_gui.qt.icons_rc',
        'electrum_cesc_gui.qt.installwizard',
        'electrum_cesc_gui.qt.lite_window',
        'electrum_cesc_gui.qt.main_window',
        'electrum_cesc_gui.qt.network_dialog',
        'electrum_cesc_gui.qt.password_dialog',
        'electrum_cesc_gui.qt.qrcodewidget',
        'electrum_cesc_gui.qt.receiving_widget',
        'electrum_cesc_gui.qt.seed_dialog',
        'electrum_cesc_gui.qt.transaction_dialog',
        'electrum_cesc_gui.qt.util',
        'electrum_cesc_gui.qt.version_getter',
        'electrum_cesc_gui.stdio',
        'electrum_cesc_gui.text',
        'electrum_cesc_plugins.exchange_rate',
        'electrum_cesc_plugins.labels',
        'electrum_cesc_plugins.pointofsale',
        'electrum_cesc_plugins.qrscanner',
        'electrum_cesc_plugins.virtualkeyboard',
    ],
    description="Lightweight CryptoEscudo Wallet",
    author="ecdsa",
    author_email="ecdsa@github",
    license="GNU GPLv3",
    url="http://electrum-cesc.org",
    long_description="""Lightweight CryptoEscudo Wallet"""
)
