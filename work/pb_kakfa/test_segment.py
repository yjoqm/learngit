#!/usr/bin/env python
# coding=utf-8

import sys
import requests
import time


id = int(sys.argv[1]) if len(sys.argv) > 1 else 0

data = {
        9: ["qita", "http://hotels.ctrip.com/"],
       }
proxies = {
        "http": "http://hotels.ctrip.com/"
        }

url = "http://dat.gtags.net/imp/dasp3"

payload = {
        "a": 9,
        "t": "",
        "p_id": 10086858,
        "p_name": "产品名字",
        "p_price": 14.888,
        "p_img_url": "http://pic.womai.com/upload/601/603/606/64306/280375/82402/82505/578835/10086858_1_pic500_588.JPG",
        "p_url": "http://www.womai.com/Product-100-10086858.htm",
        "outerid": id,
        "test1":"yj_001",
        "test2":"yj_002",
        "test3":"yj_003",
        }
p_id = 10086858
p_name = "产品名字"

start = time.clock()
for i in range(1):
    payload['outerid'] += 1
    payload['p_price'] = payload['p_price'] + 1
    for k, v in data.iteritems():
        payload['a'] = k 
        payload['t'] = v[1]
        payload['p_id'] = p_id
        payload['p_name'] = p_name      
        for key, value in payload.iteritems():
            if key in ['p_id', 'p_name']:
                payload[key] = '{}_{}_{}'.format(value, 9, payload['outerid'])
        headers = {'Referer': v[1]} 
        r = requests.get(url, params=payload, headers=headers)
        print type(r)
        #time.sleep(0.1)
        print "the", i, "times click done..."

print "done~~~"
end = time.clock()
print 'total time is: %03f seconds' % (end - start)

