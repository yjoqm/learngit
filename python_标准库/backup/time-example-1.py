#!/usr/bin/env python
# coding=utf-8

import time

now =  time.localtime(time.time())
print now 
#now :truct_time(tm_year=2016, tm_mon=6, tm_mday=7, tm_hour=10, tm_min=45, tm_sec=36, tm_wday=1, tm_yday=159, tm_isdst=0) 

year, month, day, hour, minute, second, weekday, yearday, daylight = now

#格式化当前时间
print time.strftime('%Y-%m-%d %H:%M:%S')
print "%04d-%02d-%02d" % (year, month, day)
print "%02d:%02d:%02d" % (hour, minute, second) #打印当前小时分钟秒




