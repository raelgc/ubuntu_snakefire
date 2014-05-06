#!/usr/bin/env python

'''
Setup file largely inspired by http://gitorious.org/smewt/smewt/blobs/master/setup.py
'''

import os, sys
from setuptools import find_packages, setup

args = dict(name="snakefire",
    version="1.0.5",
    description="A Campfire Desktop client for Linux",
    long_description="""\
Snakefire is a desktop client for Campfire that can run on Linux, and any other
OS that has QT support.""",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Communications :: Chat"
    ],
    keywords='linux campfire chat desktop client',
    author='Mariano Iglesias',
    author_email='mgiglesias@gmail.com',
    url='http://snakefire.org',
    license='MIT',
    include_package_data=True,
    packages=find_packages(exclude = [ 'ez_setup', 'examples', 'tests', 'utils' ]),
    install_requires=[
        "pyfire>=0.3.4",
        "pyqt",
        "keyring",
        "pyenchant"
    ],
    scripts=["bin/snakefire"]
)


import re, subprocess
from setuptools.command import install

class SnakefireInstall(install.install):

    def initialize_options(self):
        install.install.initialize_options(self)

    def run(self):
        install.install.run(self)

args.update(dict(
    cmdclass = { "install": SnakefireInstall }
))

setup(**args)
