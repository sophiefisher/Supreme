#setup.py
"""
Usage:
    python setup.py py2app

"""

from setuptools import setup

APP = ['Supreme/supreme.py']
DATA_FILES = [('', ['font']), ('', ['game']), ('', ['images']), ('', ['sounds'])]
OPTIONS = {'iconfile':'icon2.icns',
           'includes':['pyglet']}

setup(
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app','pyglet'],
)
