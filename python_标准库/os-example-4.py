#!/usr/bin/env python
# coding=utf-8
#使用os模块改变当前工作目录

import os
cwd = os.getcwd()
print "here you are:",cwd

os.chdir('/tmp/sample')
print "here you are2:", os.getcwd()

os.chdir(os.pardir)
print "3:", os.getcwd()

import shutil #可以删除path下的所有目录及文件

shutil.rmtree('/tmp/sample/')
os.mkdir("/tmp/test")
#os.rmdir('/tmp/sample/sample.bak') #只能删除空的目录
os.removedirs('/tmp/sample')


