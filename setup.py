"""
Publish a new version:
Change version in packageInfo file (lifepo4weredPyController)
pull changes
Execute:
$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags
$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel --universal
$ twine upload dist/*
"""
from tinyPeriodicTask.packageInfo import (PACKAGE_NAME, AUTHOR,
                                          VERSION, STATUS)

import codecs
import os
import sys
from setuptools import setup, find_packages

SCHEDULE_VERSION = '1.4.1'
SCHEDULE_DOWNLOAD_URL = (
    'https://github.com/fredericklussier/TinyPeriodicTask/' + SCHEDULE_VERSION
)


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
    name=PACKAGE_NAME,
    packages=['tinyPeriodicTask'],
    version=VERSION,
    description='Simple periodic execution of a function.',
    long_description=read_file('ReadMe.rst'),
    license='MIT',
    author=AUTHOR.split("<")[0].strip(),
    author_email=(AUTHOR.split("<")[1])[:-1],
    url='https://github.com/fredericklussier/TinyPeriodicTask',
    download_url=SCHEDULE_DOWNLOAD_URL,
    keywords=[
        'periodic', 'jobs', 'job scheduler', 'job scheduling'
    ],
    classifiers=[
        'Development Status :: ' + STATUS,
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)
