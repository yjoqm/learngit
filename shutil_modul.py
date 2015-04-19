#!/usr/bin/env python
# coding=utf-8
#shutil 实用模块包含了一些用于复制文件和文件夹的函数
#使用copy函数实现与ＣＰ一样的功能
import shutil
import os
'''
for file in os.listdir('.'):
    if os.path.splitext(file)[1] == ".py":
        print file
        shutil.copy(file,'/tmp/test/')
'''

#使用shutil 模块复制/删除目录树

source = "sample"
backup = "sample-backup"
#create a backup directory
shutil.copytree(source,backup)
print os.listdir(backup)

#remove it
shutil.rmtree(backup)
print os.listdir(backup)

