#!/usr/bin/env python
# coding=utf-8
#通过base64，简单容易被破解
import logging
import os
logging.basicConfig(level=logging.DEBUG,
                                           format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
                                           datefmt='%a, %d %b %Y %H:%M:%S',\
                                           filename=os.path.join(os.getcwd(),'myapp.log'))
'''
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
'''



import base64
s1 = base64.encodestring('heool world')
print s1
s2 = base64.decodestring(s1)
print s2
logging.debug(s2)

import md5
m = md5.new('1234').hexdigest()
print m
