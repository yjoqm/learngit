#!/usr/bin/python3.4
# coding=utf-8

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

#使用zip()先将键值反过来，然后计算
min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))


#也可以使用zip(), sorted(）函数来排列字典数据
price_sorted = sorted(zip(prices.values(),prices.keys()))
print(price_sorted)

#[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

