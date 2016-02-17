#!/usr/bin/env python
#encoding:utf8

import sys
import requests
import time

outerid = int(sys.argv[1]) if len(sys.argv) > 1 else 0
#account_id = int(sys.argv[2]) if len(sys.argv) > 2 else 0
data = {
        #130: ["test_yjoqm", "http://www.shunfeng.com"],
        #5: ["yule_upload", "http://192.168.0.54/01standcode.html"],
        200: ["e2b9f8793e37bdd37499675910da9f86", "http://www.suning.com"],
        #9: ["qita_jiedian", "http://www.xxxx.com"],
        #8: ["upload_anjuke", "http://www.anjuke.com"],
        #8: ["upload_anjuke2", "http://www.anjuke.com"],
        #163: ["upload_rrs", "http://www.rrs.com"],
        #100: ["upload_dangdang", "http://www.dangdang.com"],

        }
proxies = {
        "http": "http://10.8.8.228:8013"
        }

#url = "http://ut.gtags.net/imp/material"
url = "http://dat.gtags.net/imp/dasp3"
payload = {
        "a": 0,
        "t": "",
        "p_id": 10086858,
        "p_name": "产品名*",
        "p_price": 14.888,
        "p_img_url": "http://pic.womai.com/upload/601/603/606/64306/280375/82402/82505/578835/10086858_1_pic500_588.JPG",
        "p_url": "http://www.womai.com/Product-100-10086858.htm",
        "outerid": outerid,
        "test1":"yj_001",
        "test2":"yj_002",
        "aaa": "",
        "catag_1":"",
        "catag_2": "test223yj"
        }
p_id = 10086858
p_name = "产品名字"

start = time.clock()
try:

    for i in range(0, 10):
        #payload['outerid'] += 1
        #payload['p_price'] = payload['p_price'] + 1
        for k, v in data.iteritems():
            payload['a'] = k
            payload['t'] = v[0]
            payload['p_id'] = p_id
            payload['p_name'] = p_name
            for key, value in payload.iteritems():
                if key in ['p_id', 'p_name']:
                    payload[key] = '{}_{}_{}'.format(value, k, payload['outerid'])
            headers = {'Referer': v[1]}
            r = requests.get(url, params=payload, headers=headers, proxies=proxies)
            print ' total ',i, 'times.'
except requests.exceptions.ConnectionError:
    r.status_code = 'Commention refuesd' 
print "done~~~"
end = time.clock()
print 'total time is: %03f seconds' % (end - start)


