#!/usr/bin/env python
# coding=utf-8
#对字典排序
phonebook = {'Linda': '7750', 'Bob': '9345', 'Carol': '5834'}
from operator import itemgetter
sorted_ob = sorted(phonebook.iteritems(),key = itemgetter(0))
print sorted_ob 
from  collections import OrderedDict

#使用OrderDict
items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)
regular_dict = dict(items)
ordered_dict = OrderedDict(items)
print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v
print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v



#[('Carol', '5834'), ('Linda', '7750'), ('Bob', '9345')]

import operator
gameresult = [['Bob',95.00,'A'],['Alan',86.0,'C'],['Mandy',82.5,'A'],['Rob', 86,'E']]
print sorted(gameresult , key=operator.itemgetter(2, 1))
#[['Mandy', 82.5, 'A'], ['Bob', 95.0, 'A'], ['Alan', 86.0, 'C'], ['Rob', 86, 'E']]


