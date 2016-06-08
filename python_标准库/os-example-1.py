#!/usr/bin/env python
# coding=utf-8
#使用os 模块获取 文件属性
import os
import time

file = '/tmp/yjoqm.jpg'

def dump(st):

#    st = os.stat(file)
    mode, ino, dev,nlink,uid, gid, size, atime, mtime, ctime = st
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev

print "stat:",file
st = os.stat(file)
dump(st)

