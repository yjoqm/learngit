#!/usr/bin/env python
#encoding:utf-8
import os
from setuptools import setup, find_packages


if not os.path.isdir('/tmp/sona'):
    os.mkdir('/tmp/sona')




here = os.path.abspath(os.path.dirname(__file__))



def read(fname):
    return open(os.path.join(here,fname)).read()


setup(
    name='hc_test',
    version='0.0.1',
    author='Max',
    description=('hc test','test hc'),
    packages=find_packages(),
    platforms='any',
    package_data={
        '': ['*.yml','*.html','*.css','*.js','*.gif','*.png','*.map']
        },
    install_requires=read('requirements.txt'),
)
