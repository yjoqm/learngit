#!/usr/bin/env python
# coding=utf-8
#使用多个界定符分割字符串
#string.split()只能应用于简单的字符串分割
#使用re.split()方法可以更灵活的切分
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*',line))
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
#函数 re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式
