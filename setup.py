#-*- coding: utf-8 -*-

"""
    adapt
    ~~~~~

    Setup
    `````

    $ pip install . # or python setup.py install
"""

import sys
import os
from distutils.core import setup

setup(
    name='adapt',
    version='0.0.12',
    url='https://github.com/diamondman/Adapt',
    author='Jessy Diamond Exum',
    author_email='jessy.diamondman@gmail.com',
    packages=[
        'adapt',
        'adapt/drivers',
        'adapt/test',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'libusb1 >= 1.5.0',
        'bitarray >= 0.8.1',
        'bs4 >= 0.0.1',
        'requests',
    ],
    description="Driver framework for In System Configureation (ISC) Controllers (for example, JTAG)",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
)
