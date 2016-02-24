#!/usr/bin/env python
# coding=utf-8
#URLError

import urllib2
req = urllib2.Request('http://www.baibai.com')

try:
    urllib2.urlopen(req)
except urllib2.URLError,e:
        print e.reason #[Errno 8] nodename nor servname provided, or not known




#测试返回的状态码以及e.code, e.read(), e.info()等信息
req2 = urllib2.Request('http://bbs.csdn.net/callmewhy')

try:
    urllib2.urlopen(req2)
except urllib2.URLError,e:
    print e.code #返回错误码
    print e.read() #返回错误码
    print e.info()
    #Date: Wed, 17 Feb 2016 07:46:40 GMT
    #Content-Type: text/html; charset=utf-8
   # Content-Length: 162
    #Connection: close
    print e.geturl()



#异常处理模块
from urllib2 import Request, urlopen,URLError,HTTPError
req2 = urllib2.Request('http://www.baidu.com')
try:
    response = urlopen(req2)
except URLError,e:
    if hasattr(e,'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code',e.code

    elif hasattr(e,'reason'):
        print 'we faeild to reach a server'
        print 'Reason', e.reason

else:
    print 'no exception was raised.'

