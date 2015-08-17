#!/usr/bin/env python
# coding=utf-8
#chain连接多个迭代器
import itertools
it = itertools.chain(range(3),"abc")
print(it)
print(list(it))

#combinations 返回指定的元素顺序列组合
it = itertools.combinations('abcd',2)
print(list(it))
#[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

#count 从起点开始，“无限”循环下去
for x in itertools.count(10):
    print "x:", x
    if x>20:
        break


