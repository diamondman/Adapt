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
        'adapt/deviceDrivers',
        'adapt/test',
        ],
    platforms='any',
    license='MIT',
    install_requires=[
        'bitarray >= 0.8.1',
        'proteusisc',
    ],
    entry_points = {
        'console_scripts': ['adapt=adapt.adapt:main'],
    },
    description="Reference implementation of a tool using the proteusisc library for configuring ISC devices.",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
)
