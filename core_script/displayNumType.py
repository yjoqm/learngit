#!/usr/bin/env python
# coding=utf-8
#接受一个数据参数,来确定类型
def displayNumType(num):
    print num,"is", 
    if isinstance(num,(int,long,float,complex)):
        print "a number of type:",type(num).__name__
    else:
        print 'not a number  at all'

displayNumType(-69)
displayNumType(9999.2222)

import math
for eachNum in range(10):
    print round(math.pi, eachNum)

s = 'abcedes'
for i in [None] + range(-1,-len(s),-1):
    print range(-1,-len(s),-1)
    print s[:i]

