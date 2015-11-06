#!/usr/bin/env python
# coding=utf-8
def hello(name,value):
    print "%s = % s!" % (name,value)
from fabric.api import local, lcd,cd,run,env
'''
def lsfab():
    with lcd('~/mygit'):
        local('ls')

def setting_ci():
    with lcd('.'):
        local('git add .')
        local("git commit -m 'test for fab'")
        local('git push origin master')
        local('git merge origin master')
env.hosts=['192.168.0.229']
env.user='ellen'
env.password ='ellen123'

def setting_ci2():
    local('echo some things~')

def update_setting_remote():
    print "remote update."
    with cd('/home/ellen/conf'): #cd 用于进入某个操作目录
        run('ls -l') #远程操作用run.

def update():
    setting_ci2()
    update_setting_remote()
'''

from fabric.api import * 
from fabric.colors import *
env.roledefs = {
    'testserver': ['ellen@192.168.0.229'],
    'realserver': ['ellen@192.168.0.229']
}
#操作一致的服务器可以放在一组，同一组的执行同一套操作
@roles('testserver')
def task1():
    with cd('/home/ellen/conf'):
        run('ls -l |wc -l ')

@roles('realserver')
def task2():
    run('ls -l')

def show():
    print green('success')
    print red('fail')

def dotask():
    execute(task1)
    execute(task2)
    show()
    





    


