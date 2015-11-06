#!/usr/bin/env python
# coding=utf-8
#查找文件中最长的一行
f = open('/home/ellen/111.txt','r')
longest = 0
alllines = [x.strip() for x in f.readlines()]
f.close()
for line in alllines:
    linelen = len(line)
    if linelen > longest:
        longest = linelen
        print longest
#使用max函数
f = open('/home/ellen/111.txt','r')
alllines = [len(x.strip()) for x in f]
f.close
print max(alllines)

