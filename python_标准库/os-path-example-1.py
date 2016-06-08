#!/usr/bin/env python
# coding=utf-8
#os.path处理文件名

import os

file = "/tmp/test/yjoqm.jpg"

print "using", os.name, "..."

print "split", "==>", os.path.split(file)
print "splitext", "==>", os.path.splitext(file)
print "dirname","==>", os.path.dirname(file)

print "basename","==>" , os.path.basename(file)
print "join","==>",os.path.join(os.path.dirname(file), os.path.basename(file))
print "abspath", "==>" , os.path.abspath(file)


basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data','imgs')
print basedir

'''
using posix ...
split ==> ('/tmp/test', 'yjoqm.jpg')
splitext ==> ('/tmp/test/yjoqm', '.jpg')
dirname ==> /tmp/test
basename ==> yjoqm.jpg
join ==> /tmp/test/yjoqm.jpg
abspath ==> /tmp/test/yjoqm.jpg
/Users/admin/mygit/learngit/python_标准库/../data/imgs
'''
