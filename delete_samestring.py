#!/usr/bin/env python
# coding=utf-8
import os
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
print base_dir
aaaa = os.path.join(base_dir,'tmp')
print aaaa
print 'test:', os.path.dirname(os.path.abspath(__file__))
list = ['a','d','f','b','d','d','e']
print "the list is: ", list

if list:
    list.sort()
    last = list[-1]
    for i in range(len(list)-2,-1,-1):
        if last == list[i]:
            del list[i]
        else:
            last = list[i]

print list

#第二种方法

list = ['a','d','f','b','d','d','e']
l2 = []
[l2.append(i) for i in list if not i in l2]
