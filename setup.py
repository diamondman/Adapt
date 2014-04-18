#-*- coding: utf-8 -*-

"""
    adapt
    ~~~~~

    Setup
    `````

    $ pip install . # or python setup.py install
"""

import os
from distutils.core import setup

setup(
    name='adapt',
    version='0.0.10',
    url='https://github.com/diamondman/Adapt',
    author='jessy',
    author_email='jessy.diamondman@gmail.com',
    packages=[
        'adapt',
        'adapt/test',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'libusb1 >= 1.0.11.10499',
        'bitarray == 0.8.1'
    ],
    description="Linux USB JTAG controller for Digilent boards",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
)
