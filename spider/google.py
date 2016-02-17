#!/usr/bin/env python
# coding=utf-8
import urllib

google = urllib.urlopen('https://www.google.com')
print '头文件',google.info()
print '状态码',google.getcode()
print 'url:',google.geturl()

for line in google:
    print line
google.close()

