#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import requests
import json



def get_json_element(body,element_name):
    
    if type(body) is not dict:
        try:
            json_body = json.loads(body)
        except TypeError,ex:
            raise Exception(ex)
        except ValueError,ex:
            raise Exception("JSON format error")
    else:
        json_body = body
    
    element_tree = element_name.split(".")
    for element in element_tree:
        if json_body.has_key(element):
            json_body = json_body.get(element)
        else:
            raise Exception("has no element named %s" % element)
    return json_body
    

#insight api

register_openers()
datagen, headers = multipart_encode({"file": open("dmp_api.py", "rb"), 'account_id':123, 'insight_date':20141118})
request = urllib2.Request('http://insight/input/put', datagen, headers)
#print urllib2.urlopen(request).read()
input_put_code = urllib2.urlopen(request)
if input_put_code.code != 200:
    print "insight file put failed"

#get insight
insight_getdata = {'insight_date':20141118, 'status':0}
r = requests.post("insight/input/get", data=insight_getdata)
if r.status_code != 200:
    print "insight get result failed"
get_reslut=r.text
insight_id = get_json_element(get_reslut, 'result.id')
print insight_id



