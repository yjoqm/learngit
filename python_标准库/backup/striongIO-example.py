#!/usr/bin/env python
# coding=utf-8
#使用stringIO从内存文件读入内容

import StringIO
MESSAGE = "that man is depriving a village somewhere "

file = StringIO.StringIO(MESSAGE)
print file.read()

#向内存文件写入内容
file = StringIO.StringIO()
file.write('hello,yjoqm')
file.write('aaaaa bbbb')

print file.getvalue()

#使用stringIO模块捕获输出
import string, sys

stdout = sys.stdout
sys.stdout = file = StringIO.StringIO()

print """
According to Gbaya folktales, trickery and guile
are the best ways to defeat the python, king of
snakes, which was hatched from a dragon at the
world's start. -- National Geographic, May 1997
"""
sys.stdout = stdout

print string.upper(file.getvalue())
