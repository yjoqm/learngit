#!/usr/bin/env python
# coding=utf-8

import random, string,re, datetime,time
 
def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])

#生成Imei号
def randomImei():
    reobj = re.compile(r'^\d{15}$')
    while(1):
        list = []
        for i in range(15):
            list.append(random.choice(string.digits))
        imei = ''.join(list)
        match = reobj.search(imei)
        if match:
            return match.group()

#生成一定范围内的日期列表
def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d%02d%02d %02d:%02d:%02d" % (curr_date.year, curr_date.month, curr_date.day, curr_date.hour, curr_date.min,curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result


#生成某天内的时间范围
def gen_date():
    return time.strftime("%Y-%m-%d %H:%M:%S")

#第二个思路，生成一定范围时间内的随机日期
from time import *
def random_time(a,b):
    a_s=mktime(strptime(a,"%Y/%m/%d %H:%M:%S"))
    b_s=mktime(strptime(b,"%Y/%m/%d %H:%M:%S"))
    r_s=int(random.uniform(a_s,b_s))
    r=strftime("%Y/%m/%d %H:%M:%S",localtime(r_s))
    return r


f = open('testfile.txt','a')
for i in range(1000):
    f.write( randomImei()+ ' '+ random_str() + ' ' + str(random.randint(0,9))  + ' ' + '123ellen' + ' ' + str(random.uniform(10, 20))) 
    f.write('\n')
f.close()

if __name__ == '__main__':
    #print datelist((2016,11,01),(2016,11,10))
    print random_time('2016/11/18 15:53:28','2016/11/18 15:53:2')
