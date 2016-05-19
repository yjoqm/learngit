#!/usr/bin/env python
# coding=utf-8
import time

import requests
from pykafka import KafkaClient
import random
import os,time

with sem:
    global write_kafka_topic, producer, client
    if not write_kafka_topic:
	client = KafkaClient(hosts=write_kafka_hosts, zookeeper_hosts=write_kafka_hosts, use_greenlets=True,
			     socket_timeout_ms=3 * 1000, offsets_channel_socket_timeout_ms=3 * 1000)
	write_kafka_topic = client.topics['tracking_imp_dasp3']
    if not producer:
	producer = write_kafka_topic.get_producer(required_acks=0)

timestamp = time.time()

tag_id_list = [str(i) for i in tag_id_list]

for aid in advId_tagId_dict:
    _tag_id_list = advId_tagId_dict.get(aid, [])
    u_tag_id = list(set(_tag_id_list).intersection(set(tag_id_list)))
    if u_tag_id:
	# if aid == '104':
	#     print tag_id_list
	tag_id_str = ",".join(u_tag_id)
	s = "baidu_id=%s;tag_id=%s;is_baidu=1" % (quote_plus(cookie_id),tag_id_str)
	_param = quote_plus(s)

	param = "a=%s&ext_args=%s" % (aid, _param)
	kafka = {
	    "request_time": int(timestamp),
	    "ip": 0,
	    "status": 200,
	    "uri": "/imp/dasp3",
	    "zid": zid,
	    "param": param,  # Todo
	    "body": "",
	    "ua": "",
	    "process_time": 0,
	    "refer": "",
	    "cookie": "",
	}

	smartpixel_log = logger_pb2.smartpixel_log()
	smartpixel_log.request_time = kafka['request_time']
	smartpixel_log.ip = kafka['ip']
	smartpixel_log.status = kafka['status']
	smartpixel_log.uri = kafka['uri']
	smartpixel_log.zid = kafka['zid']
	smartpixel_log.param = kafka['param']
	smartpixel_log.body = kafka['body']
	smartpixel_log.ua = kafka['ua']
	smartpixel_log.process_time = kafka['process_time']
	smartpixel_log.refer = kafka['refer']
	smartpixel_log.cookie = kafka['cookie']
	import struct
	data = struct.pack(
		'i', 8)[0] + struct.pack('2i', 2, 2) + smartpixel_log.SerializeToString()
	try:
	    producer.produce(data)
	except Exception as e:
	    print 'error, is:', e
	    raise e
	else:
	    with open('./kafka.log', 'a') as f:
		f.write(json.dumps(kafka))
		f.write('\n')
    else:
	continue
