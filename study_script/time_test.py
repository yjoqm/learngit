#!/usr/bin/env python
# coding=utf-8
import time
import datetime

print time.strftime('%Y%m%d_%H:%M') #格式化时间

print time.time() #浮点型
print int(time.time()) #时间戳整S
print time.localtime()[1]-1 #上个月
print time.strftime('%Y-%m-%d_%X',time.localtime(time.time())) #日期转时间戳
print time.strftime('%Y-%m-%d_%X',time.localtime(1437717758.21)) #日期转时间戳,localtime的参数是时间戳
'''
#判断日期输入格式是否正确
while 1:
    atime = raw_input('输入格式[14.05.13 13:00]:')
    try:
        btime = time.mktime(time.strftime('%s:00' %atime, '%y.%m.%d %H:%M:%s'))
        break
    except:
        print '时间输入错误'

'''
#两天相差的天数
d1 = datetime.datetime(2005,2,16)
d2 = datetime.datetime(2015,2,18)
print (d2-d1).days


#向后推10小时
d1 = datetime.datetime.now()
d2 = d1 + datetime.timedelta(hours=10)
print d2.ctime()
print d2

