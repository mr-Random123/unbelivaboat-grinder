from setuptools import setup

APP = ['main.py']
DATA_FILES = ['icon']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'E.ico',
    'plist': {'CFBundleShortVersionString': '1.1.3', }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
