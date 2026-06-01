# -*- coding: UTF-8 -*-

"""
This file is part of ????.
(c) xxxx - ????
For COPYING and LICENSE details, please refer to the LICENSE file
"""

from setuptools import setup, find_packages
import io
import os
from os.path import dirname, join

# # Get the version from xxx/version.py
# __version__ = None
# with open('xxx/version.py') as f:
#     exec(f.read())  # Safely execute version.py to get __version__

# Function to read files with UTF-8 encoding
def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()

# Get the absolute path of the current directory
this_directory = os.path.abspath(os.path.dirname(__file__))

# Setup configuration
setup(
    name='xxx',
    # version=__version__,
    version='0.0.1',
    description='xxx',
    # long_description=read('README.md'),
    long_description_content_type='text/markdown',
    # license='GNU license',
    author='xxx',
    author_email='xxx',
    url='xxx',
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    zip_safe=False,
)
