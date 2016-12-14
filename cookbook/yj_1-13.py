#!/usr/bin/python3.4
# coding=utf-8
#通过某个关键字来排序一个字典

#使用operator模块中的itemgetter函数

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}

]

from operator import itemgetter

rows_by_fname = sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

#也可以使用Lamda函数

rows_by_fname = sorted(rows, key=lambda r: r['fname'])

#使用min max函数

min(rows,key=itemgetter('uid'))


