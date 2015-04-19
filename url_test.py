#!/usr/bin/env python
# coding=utf-8
'''
import urllib

baidu = urllib.urlopen('http://www.baidu.com')
print baidu.info()
print baidu.geturl()
'''
import urllib2
req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
the_pate = response.read()
print the_pate
#或者用下面的方法
f = urllib2.urlopen("http://www.baidu.com")
test = f.read()
print test

