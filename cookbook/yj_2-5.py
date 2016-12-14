#!/usr/bin/env python
# coding=utf-8
#字符串搜索与替换
#1.string.replace() 相对简单一些的
text = 'yeah, but no, but yeah, but no, but yeah'
t = text.replace('no','yjoqm')
print t
#yeah, but yjoqm, but yeah, but yjoqm, but yeah

#复杂的模式，请使用 re 模块中的 sub() 函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.sub(r'\3-\1-\2',text) #反斜杠数字比如 \3 指向前面模式的捕获组号



