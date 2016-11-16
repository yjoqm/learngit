#!/usr/bin/env python
# coding=utf-8
import time
from collections import Counter

#判断I_time 是否在start_t与end_t中
def compare_time(l_time,start_t,end_t):
    s_time = time.mktime(time.strptime(start_t,'%Y%m%d%H%M')) # get the seconds for specify date
    e_time = time.mktime(time.strptime(end_t,'%Y%m%d%H%M'))
    log_time = time.mktime(time.strptime(l_time,'%Y-%m-%d %H:%M:%S'))
    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True
    return False

with open('mock_profile5.txt', 'r') as f:
    s = f.read()

#取出每一行数据 
s = [x.strip().split('\t') for x in s.strip().split('\n')]
#判断时间是否在一天内，如果是，打印整行数据.
li= ([x[1] for x in s])
zid = ([j[0] for j in s])
with open('mock_profile5.txt','r') as f:
    for i in range(len(li)):
        with open('zid_file.txt','a') as zid_file:
            if float(li[i])>=float(1478696400) and float(li[i])<=float(1478699999):
            #print zid[i] + ' '+ li[i]
                zid_file.write(zid[i] + '\n')
                

d = {}
with open('zid_file.txt') as test_count:
    for line in test_count.readlines():
        key = line.rstrip()
        if d.has_key(key) ==False:
            d[key] = 1
        else:
            d[key] += 1
    for k, v in d.items():
        #打印每zid出现的次数
        print "%s==%s" % (k,v)
        #9号的zid去重后的个数为2203。
        #10号的zid去重后的个数为2188
        #11号的zid去重后的个数为2128
