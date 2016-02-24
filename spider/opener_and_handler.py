#!/usr/bin/env python
# coding=utf-8
import urllib2
#geturl() 用来获取真实的URL 
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)
print 'old url:', old_url
print 'real url:', response.geturl()



# info() 返回对像的字典 对像 该字典获取的页面情况
print 'INFO:',response.info()


#创建一个opener,可以实例化一个openerDirector,然后调用.add_handler(some_handler_instance).
#也可以使用build_opener，这是一个更加方便的函数，用来创建opener对象，他只需要一次函数调用
#install_opener 用来创建（全局）默认opener。这个表示调用urlopen将使用你安装的opener,opener有一个open方法。
#以下建一个urllib2_test12.py来测试一下info的应用

#创建一个密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加用户名和密码
top_level_url= "http://www.example/com/foo/"
#如果realm, 我们可以使用他代替 ``None``.  
# password_mgr.add_password(None, top_level_url, username, password)
password_mgr.add_password(None, top_level_url,'why','1223')

#创建一个新的handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# 创建 "opener" (OpenerDirector 实例) 
opener = urllib2.build_opener(handler)
a_url = 'http://wwwbaidu.com'

#使用"opener" (openerDirector实例) 
opener.open(a_url)

#安装 opener,# 现在所有调用 urllib2.urlopen 将用我们的 opener.
urllib2.install_opener(opener)




