#!/usr/bin/python3.4
# coding=utf-8

#程序 接受字符串输入，计算两日期的间隔
from datetime import datetime
text = '2016-09-12'
y = datetime.strptime(text,'%Y-%m-%d')
print(y)
z = datetime.now()
print(z)
diff = y-z
print(diff)



