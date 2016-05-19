#!/usr/bin/env python
#encoding:utf8

import sys
import requests
import time
import random
outerid = int(sys.argv[1]) if len(sys.argv) > 1 else 0
data = {
        #130: ["test_yjoqm", "http://www.shunfeng.com"],
        #5: ["yule_upload", "http://192.168.0.54/01standcode.html"],
        200: ["e2b9f8793e37bdd37499675910da9f86", "http://www.suning.com"],
        }
uphone = 18658879839

def get_uphone():
    li = ['1','2','3','4','5','6','7','8','9','0']
    choice_num = random.sample(li,8)
    num = ''.join(choice_num)
    return  '186'+ num 
    
name = " 郎组合 安七炫 艾敬 安成基 安又琪 安以轩 阿雅柳瀚雅 爱戴 安在旭 安琥 艾雨 安雅 阿朵 安雅 安志杰 保剑峰 宝儿 卜学亮 鲍逸琳 鲍蕾 白玉芬 仓春莲 仓红 陈超云 陈高 陈国祥 陈宏柳 陈金娣 陈丽丽 陈丽丽 陈平 陈向东 陈晓冬 陈小荣 陈秀芬 陈艳华 陈兆国 成秀山 仇腊梅 戴金辉 邓海燕"

choice_name = name.split(' ')
#print t

url = "http://sina2yiche.com/api/askPrice"
payload = {
        "brand": u'睿骋',
        "carname": "2014款睿骋2.0L自动豪华周年版",
        "uname": random.choice(choice_name),
        "uphone": get_uphone(),
        "prov": "甘肃",
        "city": "平凉",
        "subid":1497,
        "carid": 20401,
        "subname": "长安轿车",
        }
start = time.clock()
for i in range(0, 2):
    r = requests.get(url, params=payload)
    print 'url is:', r.url
print ' total ',i, 'times.'
print "done~~~"
end = time.clock()
print 'total time is: %03f seconds' % (end - start)

if __name__ == '__main__':
    te = get_uphone()
    print te
