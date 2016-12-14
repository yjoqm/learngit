#!/usr/bin/python3.4
# coding=utf-8


a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}


print(a.keys())

print(a.keys() & b.keys())

#dict_keys(['y', 'x', 'z'])
#{'y', 'x'}
a.keys() - b.keys() # { 'z' }
a.items() & b.items() # { ('y', 2) }

#这些操作也可以用于修改或者过滤字典元素。 比如，假如你想以现有字典构造一个排除几个指定键的新字典
c = {key:a[key] for key in a.keys() - {'z','w'}}

