"""
Publish a new version:
Change version in packageInfo file (tinyPeriodicTask)
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

SCHEDULE_DOWNLOAD_URL = (
    'https://github.com/fredericklussier/TinyPeriodicTask/tree/' + VERSION
)


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

_LONG_DESCRIPTION = """
Simple periodic execution of a function at every laps 
of time or every day at specifique time.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

By design, when you start a tinyPeriodicTask instance,
the runner will delay the first call to the callback function
according to the interval.

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:

"""

setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=VERSION,
    description='Simple periodic execution of a function.',
    long_description=_LONG_DESCRIPTION,
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
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)
