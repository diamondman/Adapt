#-*- coding: utf-8 -*-

"""
    adapt
    ~~~~~

    Setup
    `````

    $ pip install . # or python setup.py install
"""

import codecs
import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """Taken from pypa pip setup.py:
    intentionally *not* adding an encoding option to open, See:
    https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='adaptisc',
    version=find_version("adaptisc", "__init__.py"),
    url='https://github.com/diamondman/Adapt',
    author='Jessy Diamond Exum',
    author_email='jessy.diamondman@gmail.com',
    packages=[
        'adaptisc',
        'adaptisc/deviceDrivers',
        ],
    platforms='any',
    license='LGPL 2.1',
    install_requires=[
        'bitarray >= 0.8.1',
        'proteusisc',
    ],
    entry_points = {
        'console_scripts': ['adapt=adaptisc.adapt:main'],
    },
    description="Reference implementation of a tool using the proteusisc library for configuring ISC devices.",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.md')).read(),
)
