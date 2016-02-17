#!/usr/bin/env python
# coding=utf-8
#利用urllib2通过指定的url攫取网页内容
# urllib2 用一个request对像来映射你提出的http请求,将返回一个相关请求response对像
import urllib2
req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
page = response.read()
#print page

#在http请求时，可以发送data表单数据 
import urllib
url = 'https://api.github.com/some/endpoint'

values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }  

data = urllib.urlencode(values) #编码工作
req = urllib2.Request(url,data) #发送请求同时传data表单
reqponse = urllib2.urlopen(req) #接受反馈的信息
the_page = response.read()
print the_page

#设置Headers到http请求


