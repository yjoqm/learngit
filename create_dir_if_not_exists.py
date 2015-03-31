#!/usr/bin/env python
# coding=utf-8
#如果不存在一个目录时创建
import os
home = os.path.expanduser('~')
print home

if not os.path.exists(home+'/testdir'):
    os.makedirs(home + '/testdir')
else:
    exit(0)

