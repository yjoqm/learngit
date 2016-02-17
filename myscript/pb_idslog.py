#!/usr/bin/env python
# coding=utf-8
from pykafka import KafkaClient
import struct
import IdsLog_pb2
from StringIO import StringIO

attrs = ['zid','pids', 'timestamp','adverID']

client = KafkaClient('172.22.50.129:9092')
#print client.topics
topic = client.topics['idmap_pb_log']
consumer = topic.get_simple_consumer()

for message in consumer:
   # print message.value
    try:
        buf = StringIO(message.value)
        buf.seek(9)
        content = buf.read()
        idProduct = IdsLog_pb2.PlatformIds()
        idProduct.ParseFromString(content)
        print idProduct
    except Exception as e:
        print 'parse error'

'''
for message in consumer:
    f = open('test.pb','w+')
    if message is not None:
        #print message.value
        f.write(message.value)
        f.close()
        f1 = open('test.pb')
        #head = struct.unpack('!B', f1.read(1))[0]
        #size = struct.unpack('!Q', f1.read(8))[0]

        while size > 0:
            content = f1.read(9)
            if content is not None:
                ucproduct = SegmentsLog_pb2.UcSegments()
                ucproduct.ParseFromString(content)
                print "=============="
                for attr in  attrs:
                    print attr, ":",getattr(ucproduct,attr)
                f1.read(1)
                try:
                    size = struct.unpack('!I',f1.read(4))[0]
                except:
                    size = -1
        f.close()
'''    

if __name__ == '__main__':
    print 'time'
