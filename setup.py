#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


setup(
    name='django-externaltestserver',
    version='0.2.5',
    description='Run your Django selenium tests against an external server',
    author='Saul Shanabrook',
    author_email='s.shanabrook@gmail.com',
    url='https://github.com/saulshanabrook/django-externaltestserver',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
