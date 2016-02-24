#!/usr/bin/env python
# coding=utf-8
#

import  hashlib

def translate(time):
    data = 'O&VtQbgljz'
    res = hashlib.md5()
    src = data + str(time)
    print src
    res.update(src)
    return res.hexdigest().upper()

if __name__ == '__main__':
    t = translate('2016-02-19 15:33:33')
    print t
