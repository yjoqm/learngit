#!/usr/bin/env python
# coding=utf-8
from pprint import pprint
import protobuf_json

import test_pb2 as pb_test

#create and fill test message
pb = pb_test.TestMessage()
pb.id = 123
pb.b = b"\x08\xc8\x03\x12"
pb.query = "some text"
pb.flag = True
pb.test_enum = 2
msg = pb.nested_msg
msg.id = 1010
msg.title = 'test title'
msg.url = 'http://example.com'

msags = pb.nested_msgs.add()
msags.id = 456
msags.title='test title22'
msags.url='http://localhost/'

pb.rep_int.append(1)
pb.rep_int.append(22)

pb.bs.append('\x00\x01\x02\x03\x04')
pb.bs.append('\x05\x06\x07\x08\x09')

pprint(pb.SerializeToString)
json_obj = protobuf_json.pb2json(pb)
print json_obj

pb2=protobuf_json.json2pb(pb_test.TestMessage(),json_obj)
pprint(pb2.SerializeToString())

if pb == pb2:
    print "test passed."
else:
    print "Test FAILD"


