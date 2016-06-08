#!/usr/bin/env python
# coding=utf-8

#利用tempfile创建临时文件
import tempfile
import os

tempfile = tempfile.mktemp()
print "tempfile", tempfile

file = open(tempfile,'w+b')
file.write("*" * 10000)
file.seek(0)
print len(file.read()), "bytes"
file.close()

try:
    os.remove(tempfile)
except OSError:
    pass



#打开临时文件
file = tempfile.TemporaryFile()
for i in range(100):
    file.write("qq"*100)
file.close()
