#!/usr/bin/env python
# coding=utf-8
def hello(name,value):
    print "%s = % s!" % (name,value)
from fabric.api import local, lcd
'''
def lsfab():
    with lcd('~/mygit'):
        local('ls')
'''

def setting_ci():
    with lcd('.'):
        local('git add .')
        local("git commit -m 'test for fab'")
        local('git push origin/master')
        local('git merge origin/master')
    


