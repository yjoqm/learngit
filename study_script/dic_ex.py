#!/usr/bin/env/ python
#encoding:utf-8
#存在一个字典,字典中的一些键属于一个特定的集合,而你想创建一个包含这个键集合及期对应值的新字典
#不修改字典
def sub_dict(somedict,somekeys,defalut=None):
    return dict([(k, somedict.get(k,defalut)) for k in somekeys])
#从原字典中删除符合条件的条目
def sub_dict_remove(somedict,somekeys,default = None):
    return dict([(k , somedict.pop(k,default)) for k in somekeys])

'''
In [15]: def sub_dict(somedict, somekeys,default=None):
   ....:     return dict([(k, somedict.get(k,default)) for k in somekeys])
   ....: d = {'a':5, 'b':6,'c':7}
   ....: print sub_dict(d,'ab'),d
   ....: 
{'a': 5, 'b': 6} {'a': 5, 'c': 7, 'b': 6}

In [16]: def sub_dict(somedict, somekeys,default=None):
    return dict([(k, somedict.get(k,default)) for k in somekeys])
d = {'a':5, 'b':6,'c':7}
print sub_dict(d,'ab')
   ....: 
{'a': 5, 'b': 6}
'''

#反转字典的键与值
def invert_dict(d):
    return dict([(v,k) for k,v in iteritems()])
#结果:
'''
In [19]: test = {"a":1,"b":2,"b":4}

In [20]: invert_dict(test)
Out[20]: {1: 'a', 4: 'b'}
'''


if __name__ == '__main__':
    dic = {'a':1,'b':2,'c':3}
    t = sub_dict(dic,'a')
    print 't',t

