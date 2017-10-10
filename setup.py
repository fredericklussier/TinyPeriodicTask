"""
Publish a new version:
$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags
$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel --universal
$ twine upload dist/*
"""
import codecs
import os
import sys
from setuptools import setup, find_packages


SCHEDULE_VERSION = '1.3.1'
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
    name='tinyPeriodicTask',
    packages=['schedule'],
    version=SCHEDULE_VERSION,
    description='Simple periodic execution of a function.',
    long_description=read_file('README.rst'),
    license='MIT',
    author='Frederick Lussier',
    author_email='frederick.lussier@hotmail.com',
    url='https://github.com/fredericklussier/TinyPeriodicTask',
    download_url=SCHEDULE_DOWNLOAD_URL,
    keywords=[
        'periodic', 'jobs', 'job scheduler', 'job scheduling'
    ],
    packages=['tinyPeriodicTask'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)
