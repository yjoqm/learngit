#!/usr/bin/env python
# coding=utf-8
#随机产生一个８位数字,每位数字都是可以是1-6中的任意一个整数a
import random
result=[]
for i in range(8):
    result.append(str(random.randint(1,6)))
print ''.join(result)

