#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
若列表中某元素存在时则返回,否则返回默认值,类似于字黄中的get方法L.get(i, v)
'''
def list_get(L,i, v = None):
    if -len(L) <= i < len(L):
        return L[i]
    else:
        return v

if '__name__' == '__main__':
    Li = [1,2,3,4,5,6]
    list_get(Li, 3)


