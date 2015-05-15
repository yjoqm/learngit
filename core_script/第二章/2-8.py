#!/usr/bin/env python
# coding=utf-8
#输入用户输入的数字的和
li = []
i = 0
while i<6:
    num = int(raw_input("input five num:"))
    li.append(num)
    i +=1
    print li
print sum(li)
