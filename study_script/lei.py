#!/usr/bin/env python
# coding=utf-8
''''
class MyClass(object):
    myVersion ='1.1'
    def showMyVerson(self):
        print MyClass.myVersion
'''
class A(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return "A" + self.name
class B(A):
    def getName(self):
        return "B" + self.name


class HotelRoomRate(object):
    def __init__(self,rt,sales=0.085,rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.rommRate=rt
    def calcTotal(self,days=1):
        daily = round((self.rommRate + self.salesTax),2)
        return float(days) * daily



if __name__ == '__main__':
    sfo = HotelRoomRate(229)
    sfo.calcTotal()
    sfo=HotelRoomRate(2)
    sfo.calcTotal()
    sfo = HotelRoomRate(189,0.086,0.058)
    sfo.calcTotal()
'''
if __name__ == '__main__':
    test = B('yj')
    print test.getName() #('B:', 'yj')
    print test.name #yj
'''
