#!/usr/bin/env python
# coding=utf-8
#创建一个文件,如果文件同名则报错,由用户输入每一行,写入该文件

import os
#ls = os.linesep()

#get file
fname = raw_input('please a file: ')
while True:
    if os.path.exists(fname):
        print "Error: '%s' already exists" % fname
    else:
        break 

#get filename
all = []
while True:
    entry = raw_input(">")
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file
fobj = open(fname,'w')
fobj.writelines([lines for lines in all])
fobj.close()
print 'Done'

fname = raw_input('Enter filename: ')
try:
    fobj = open(fname,'r')
except IOError,e:
    print "file open error",e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()
