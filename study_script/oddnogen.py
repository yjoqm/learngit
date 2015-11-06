#!/usr/bin/env python
# coding=utf-8
from random import randint
def odd(n):
    return n%2

allnum = []
for eachnum in range(9):
    allnum.append(randint(1,99))
print filter(odd,allnum)
#list替换
allnum = []
for eachnum in range(9):
    allnum.append(randint(1,99))
    print [n for n in allnum if n%2]


#map()

