#!/usr/bin/env python
# coding=utf-8
#过滤序列元素
#简单的使用列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
t = [n for n in mylist if n>0]
print(t)

#过滤规则复杂的时候可以使用filter()，把规则封在函数里
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
isvals = list(filter(is_int,values))
print(isvals)
#Outputs ['1', '2', '-3', '4', '5']

#因此如果你想得到一个列表的话，就得像示例那样使用 list() 去转换。
