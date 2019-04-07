# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'skeleton', 'VERSION'), 'r') as version_file:
    __version__ = str(version_file.read().strip())

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'rb') as readme:
    README = str(readme.read())

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as reqs:
    install_requires = [
        str(line) for line in reqs.read().split('\n') if line
    ]

setup(
    name                    = 'skeleton',
    version                 = __version__,
    description             = 'starter project',
    license                 = 'http://opensource.org/licenses/MIT',
    long_description        = README,
    install_requires        = install_requires,
    packages                = find_packages(exclude = ['contrib', 'docs', 'tests']),
    include_package_data    = True
)
