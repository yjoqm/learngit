#!/usr/bin/env python
# coding=utf-8
#yield指令,可以暂停一个函数并返回中间结果
def gen():
    for x in range(4):
        tmp = yield x
        if x == 'hello':
            print 'world'
        else:
            str(tmp)

t = gen()
#print t.next()
#print t.next()
print t.send('hello')

