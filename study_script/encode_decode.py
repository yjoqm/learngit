#!/usr/bin/env python
# coding=utf-8

def decodeGBKwithUtf8():
    gbk_test = '刘焕焕'
    print 'gbk_test',gbk_test
    unicode_test = gbk_test.decode('utf-8')
    print 'unicode_test:',unicode_test

def unicode_init(obj,encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj,unicode):
            obj = unicode(obj,encoding)
    return obj

if __name__ == '__main__':
    decodeGBKwithUtf8()
