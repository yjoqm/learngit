#!/usr/bin/env python
# coding=utf-8

# 由于在args变量前有*前缀, 所有多余的函数参数都会作为一个元组存储在args中
def sum(message, *args):
    '''Return the sum of each argument.'''
    total = 0
    # 除了用循环,也可以用下标来读取参数,如: args[0]
    for i in args:
        total += i
    print (str(type(args)) + ' ' + message + ":" + str(total))
#    sum2(args) # 这样传过去的 args 是一个元组；打印如： ((3, 5.5),)
#    sum2(*args) # 这样传过去的 *args 表示多个参数；打印如：(3, 5.5)

#def sum2(*args):
#    print(args)

sum('hight', 3, 5.5) # 打印: <type 'tuple'>  hight:8.5
sum('weight', 10)    # 打印: <type 'tuple'>  weight:10

#默认参数建议使用基本类型，如果不是基本类型，建议写None,然后在函数里面设默认值
# 范例1，默认参数如果是 []、{}
def t1(a,b=[]):
    b.append(a)
    print ('%s %s' %(id(b),b))

#t1(1)       # 打印： 12523400  [1]
#t1(2)       # 打印： 12523400  [1, 2]
#t1(3, b=[]) # 打印： 12545000  [3]

#修改后,使用None参数代替
def t1_fix(a,b=None):
    if b is None:
        b  = []
    b.append(a)
    print ( 'ttt:', '%s %s'% (id(b),b))
def t1_fix(a,b=None):
    b = b or []
    b.append(a)
    print "......"
t1_fix(3,[5,4])

def t2(a, b = {}):
    b[len(b)] = a
    print('%s  %s' % (id(b), b))



def t2_fix(a, b = None):
    b = b or {}
    b[len(b)] = a
    print('%s  %s' % (id(b), b))       
