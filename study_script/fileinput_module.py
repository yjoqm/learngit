#!/usr/bin/env python
# coding=utf-8
#fileinp ut module,用来循环一个或多个文件的内容
#读出文件中的内容:
'''
import fileinput
import sys

for line in fileinput.input('/home/ellen/learngit/char_number.py'):
    sys.stdout.write("->")
    sys.stdout.write(line)
'''
#输出符合glob.glob 中的文件的行
import fileinput
import glob
import sys, string

for line in fileinput.input(glob.glob("*.txt")):
    if fileinput.isfirstline():　
        sys.stderr.write("----reading %s ---\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))　#lineno返回当前读取的行的行号
