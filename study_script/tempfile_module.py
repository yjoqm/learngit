#!/usr/bin/env python
# coding=utf-8
import tempfile
import os
#创建一个文件并操作,创建完成后需要删除
tempfile = tempfile.mktemp()
print "tempfile", "==>", tempfile

file = open(tempfile,'w')
file.write("yjoqn"*10)
file.seek(0)
#print len(file.read())
file.close()

try:
    #must remove file when done
    os.remove(tempfile)
except OSError:
    pass
#使用 tempfile 模块打开临时文件

file = tempfile.TemporaryFile()
for i in range(100):
    file.write("*" * 100)
file.close()


