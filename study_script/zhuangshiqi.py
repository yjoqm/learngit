#!/usr/bin/env python
# coding=utf-8
'''
def now():
    print '2015-04-01'

print now.__name__    #print now 可以拿到函数的名字
'''
#如果要增强now()函数的功能,　比如,在函数用前后加个自动打印日志,但又不希望修改now()函数的定义,这种在代码支持期间动态增加功能的方式叫装饰器

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' %func.__name__
        return func(*args,**kw)
    return wrapper



@log
def now():
    print '2015-04-01'

test =now()
print test

#explain:http://www.cnblogs.com/vamei/archive/2013/02/16/2820212.html
def decortor(F):
    def new_F(a,b):
        print ("input", a,b)
        return F(a,b)
    return new_F

