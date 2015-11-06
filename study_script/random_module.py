#!/usr/bin/env python
# coding=utf-8
import random

for i in range(5):
    #random float
    print random.random(),
    #print integer
    print random.randint(100,1000),
    print random.randrange(100,1000,2),
#用 random 模块从序列取出随机项
for i in range(5):
    print i,
    print random.choice([1,2,4,5,6,7,9,1])

