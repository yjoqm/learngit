#!/usr/bin/env python
# coding=utf-8
class Fib:
    def __init__(self,max):
        self.max = max
    def __iter__(self):
        self.a=0
        self.b=1
        return self
    def next(self):
        fib=self.a
        if fib>self.max:
            raise StopIteration
        self.a,self.b=self.b, self.a + self.b
        return fib

#for n in Fib(100):
#    print n
def fib(max):
    a,b=0,1
    while a<max:
        yield a
        a,b=b,a+b
test = fib(100)
#for i in test:
#    print i

def h():
    print 'hello1'
    yield 5
    print 'hello222'

c = h()
print c.next()
print c.next()
