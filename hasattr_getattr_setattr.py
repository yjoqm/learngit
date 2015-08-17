#!/usr/bin/env python
# coding=utf-8

class Cat(object):
    def __init__(self,name='ketty'):
        self.name=name
    def sayHi(self):
        print self.name + 'say hi~'

cat = Cat('ketty')
if hasattr(cat,'name'):
    setattr(cat,'name','tiger') #cat.name='tiger'
    print getattr(cat,'name') #print cat.name

getattr(cat,'sayHi')()  #cat.sayHi()

#列出所有可调用的方法
methodlist = [method for method in dir(cat) if callable(getattr(cat,method))]
globals().get('Cat')()
