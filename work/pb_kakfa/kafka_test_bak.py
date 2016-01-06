#!/usr/bin/env python
# coding=utf-8
import sys
import requests
from pykafka import KafkaClient
import random
import os,time
import tracking_pb2
import pickle

dir_path = os.path.dirname(os.path.abspath(__file__))
test = os.path.join(dir_path,'zid.txt')
id = int(sys.argv[1]) if len(sys.argv) > 1 else 0

client = KafkaClient('172.22.50.129:9092')
#print client.topics
topic = client.topics['tracking_imp_dasp3']



zid_list = []
with open(os.path.join(dir_path,'zid.txt')) as f:
    for li in f.readlines():
        li = li.strip()
        zid_list.append(li)

def args_url():
    data = {
        9: ["http://hotels.ctrip.com/"],
    }
    url = "http://dat.gtags.net/imp/dasp3"
    payload = {
        "a": 9,
        "t": 'test_ttt',
        "p_id":10086,
        "p_url":"http://www.womai.com/Product-100-10086858.htm",
        "outerid": id,
        "test3":"yjoqm_11111",
        "p_name":"name_p"
    }
    payload['outerid'] += 1
    for k,v in data.iteritems():
        payload['a']= k
        payload['t'] = v[0]
        for key, value in payload.iteritems():
            if key in ['p_id','p_name']:
                payload[key] = '{}_{}_{}'.format(value, 9, payload['outerid'])
        headers = {'Referer': v[0]} 
        r = requests.get(url, params=payload, headers=headers)
        test_url = r.url[31:]
        return test_url
url = args_url()

def time_fromat():
    #timestamp = time.strftime('%Y-%m-%d %X',time.localtime(os.path.getmtime))
    timestamp = time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())
    timestamp = timestamp+'+08:00'
    return timestamp
timestamp = time_fromat()

with topic.get_producer() as producer:
    for i in range(4):
        kafka = {
            "time":timestamp,
            "ip": '127.0.0.1',
            "imp": '/imp/dasp3',
            "zid": random.choice(zid_list),
            "args": url,
            "http": 'http://hotels.ctrip.com',
            "status": 200,
            "no":'-',
            "req":"python-requests/2.8.1"
        }

        pb_sp = tracking_pb2.Smartpixel()
        pb_sp.request_time = kafka['time']
        pb_sp.ip = kafka['ip']
        pb_sp.status = kafka['status']
        pb_sp.uri = kafka['imp']
        pb_sp.zid = kafka['zid']
        pb_sp.param = kafka['args']
        pb_sp.body = kafka['no']
        pb_sp.ua = kafka['req']
        pb_sp.process_time = kafka['no']
        pb_sp.refer = kafka['http']
        pb_sp.cookie = kafka['no']

        kafka_message = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(kafka['time'], kafka['ip'],kafka['status'], kafka['imp'],kafka['zid'],kafka['args'],kafka['no'],kafka['req'], kafka['no'],kafka['http'],kafka['no'])
        #producer.produce(kafka_message)
        producer.produce(pickle.dumps(kafka_message))

if __name__ == '__main__':
    test = time_fromat()
    #print time
