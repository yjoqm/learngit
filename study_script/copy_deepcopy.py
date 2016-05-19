#!/usr/bin/env python
# coding=utf-8
import copy


class Pizza(object):
    def __init__(self, name,size,price):
        self.name = name
        self.size = size
        self.price = price

    def getPizzaInfo(self):
        return self.name, self.size,self.price
    def showPizzaInfo(self):
        print "Pizza name:" + str(self.name)
        print "Pizza size:" + str(self.size) 
        print "Pizza price:" + str(self.price) 
    def changeSize(self,size):
        self.size = size
    def changPrize(self,price):
        self.price = price 

class Order(object):
    def __init__(self,name):
        self.customername = name
        self.pizzaList = []
        self.pizzaList.append(Pizza("Mushroom",12,30))

    def ordermore(self,pizza):
        self.pizzaList.append(pizza)

    def changName(self,name):
        self.customername = name

    def getorderdetail(self):
        print "customer name:" +self.customername
        for i in self.pizzaList:
            i.showPizzaInfo()

    def getPizza(self, number):
        return self.pizzaList[number]


if __name__ == '__main__':
    customer1 = Order('yjoqm')
    customer1.ordermore(Pizza('seafood',9,10))
    customer1.ordermore(Pizza('fruit',12,40))
    print "customer1 order infomation:", customer1.getorderdetail()
    print "----------"

    customer2 = copy.copy(customer1)
    print "oder2 customer name:" + customer2.customername
    customer2.getPizza(2).changeSize(9)
    customer2.getPizza(2).changPrize(30)
    print "customer2 order info:", customer2.getorderdetail()
    print "=========="
    print "111111111:",customer1.getorderdetail()



    #实际上在包含引用的数据结构中, 浅拷贝并不能进行彻底的拷贝,当存在列表、字典等不可变对象的时候,它仅仅拷贝其引用 地址。要解决上述问题需要用到深拷贝,深拷贝不仅拷贝引用也拷贝引用所指向的对象,因 此深拷贝得到的对象和原对象是相互独立的
    #上面的程序应该将 customer2=copy.copy(customer1) 改为 copy.deepcopy()




    


