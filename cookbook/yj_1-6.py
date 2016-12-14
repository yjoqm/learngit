#!/usr/bin/python3.4
# coding=utf-8
#实现一个键对应多个值的字典
from collections import defaultdict

li = [1,2,3,4,5,6,7,8,9,12]

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(4)

print(d)


d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)

print(d)




