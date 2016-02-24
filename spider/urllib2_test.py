#!/usr/bin/env python
# coding=utf-8
#urllib2的使用细节与抓站技巧

#1.proxy的设置
#urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy,如果想在程序中明确控制 Proxy #而不受环境变量的影响，可以使用代理

import urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)


#2设置超时
response = urllib2.urlopen('http://www.123.com',timeout=10)

#3.在http resquest 中加入特定的Header

request = urllib2.Request('http://www.baidu.com')
request.add_header('User-Agent','fake-client')
response = urllib2.urlopen(request)
print response

#3.redirect
#urllib2 默认情况下会针对 HTTP 3XX 返回码自动进行 redirect 动作，无需人工配置。要检测是否发生了 redirect 动作，只要检查一下 Response 的 URL 和 Request 的 URL 是否一致就可以了

my_url = 'http://google.con'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected

#cookie 
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baiud.com')

for item in cookie:
    print 'name= ' + item.name
    print 'value= ' + item.value

#4.http 返回码
try:
    response = urllib2.urlopen('http://www.baidu.com')
except urllib2.HTTPError,e:
    print e.code

