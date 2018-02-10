#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(p6rguvyrst): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='testingapp',
    version='0.1.0',
    description="Testing APIs",
    long_description=readme + '\n\n' + history,
    author="Toomas Ormisson",
    author_email='Toomas.Ormisson@gmail.com',
    url='',
    packages=find_packages(include=['testingapp']),
    #entry_points={
    #    'console_scripts': [
    #        'directory_monitor=dirmon.cli:main'
    #    ]
    #},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='testingapp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
    ]
)
