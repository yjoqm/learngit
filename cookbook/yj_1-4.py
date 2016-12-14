#!/usr/bin/python3.4
# coding=utf-8

#使用heapq
#找到最大或最小的N个元素

import heapq

nums = [1,5,7,3,2,9,23,74,78,54,45,-21]
print (heapq.nlargest(3,nums))
print(heapq.nsmallest(2,nums))

#[78, 74, 54]
#[-21, 1]
   
#两个函数都接受一个关键字函数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


print(heapq.nlargest(3,portfolio,key=lambda s:s['price']))
print(heapq.nsmallest(3,portfolio,key=lambda s:s['price']))
#会打印该字典中的最大与最小的集合
#[{'price': 543.22, 'name': 'AAPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}]
#[{'price': 16.35, 'name': 'YHOO', 'shares': 45}, {'price': 21.09, 'name': 'FB', 'shares': 200}, {'price': 31.75, 'name': 'HPQ', 'shares': 35}]

