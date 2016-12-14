#!/usr/bin/env python
# coding=utf-8
#字符串开头或结尾匹配
#使用 str.startswith() 或者是 str.endswith() 方法
filename = 'spam.txt'
filename.endswith('.txt')
True
filename.startswith('file:')
False
url = 'http://www.python.org'
url.startswith('http:')
True

#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
import os
filenames = os.listdir('.')
print(filenames)
#[ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h'  ]
[name for name in filenames if name.endswith(('.c','.h'))]
#['foo.c', 'spam.c', 'spam.h']

any(name.endswith('.py') for name in filenames)
#True
if any(name.endswith(('.c','h') for name in listdir(dirname))):
    pass

