#!/usr/bin/env python
# coding=utf-8
import StringIO
message = "that man is moon"
file = StringIO.StringIO(message)
print file.read()
#使用 StringIO 模块向内存文件写入内容

file = StringIO.StringIO()
file.write("this man is no ordinary man.")
file.write("this is yjoqm")
print file.getvalue()

#使用 StringIO 模块捕获输出
import string,sys
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


#import cStirngIO
try:
    import cStirngIO
    StringIO = cStirngIO
except:
    import StringIO



