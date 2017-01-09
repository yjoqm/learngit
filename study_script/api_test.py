#!/usr/bin/env python
# coding=utf-8

#编写url：浏览器会自动将?后面识别为参数
urlpatterns = [
    url(r'^calc/$',aptset.calc, name='calc'),
]

#编写view
def calc(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    print a,b,c
    m = a+b+c
    return HttpResponse(str(m))

#浏览器返回json类型结果
import json
def calc(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    print a,b,c
    m = a+b+c
    n = b+a
    rets = {"m":m,'n':n}
    retsj = json.dumps(rets) #返回json类型数据 {"m": "aabb00", "n": "bbaa"}
    return HttpResponse(retsj)



import urllib,urllib2

url = 'http://192.168.50.74/aptest/calc/?' #定义接口地址
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
headers = {'User-agent':'Mozilla/5.0'} #---OK
url_args = urllib.urlencode({  #定义参数
                            "a":'aa',
                            "b":'bb',
                            "c":'00'}) 
print url_args #返回：a=aa&c=00&b=bb

urls = '%s%s' %(url,url_args)
print urls #返回：http://192.168.50.74/aptest/calc/?a=aa&c=00&b=bb
req = urllib2.Request(url=urls,headers=headers) #需要添加一个header，否则会提示403forbidden
print urllib2.urlopen(req).read() #返回：aabb00
#urllib2.urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象

