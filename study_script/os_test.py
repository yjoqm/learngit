#!/usr/bin/env python
# coding=utf-8
#保存输入的字符地到一个文件
import os
filename = raw_input('Enter file name: ')
fobj = open(filename,'w')
while True:
    aline = raw_input("Enter a line ('.') to quit:")
    if aline != ".":
        fobj.write('%s%s' %(aline,os.linesep))
    else:
        break
fobj.close()
