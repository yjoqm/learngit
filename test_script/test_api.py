#!/usr/bin/env python

import requests
from nose.tools import assert_equal
import json
import pymongo


def delete_666():
    merchant_db = pymongo.MongoClient("mongodb://XX:XX@192.168.0.8888/merchant").get_default_database()
    col = merchant_db['merchant_online_666']
    merchant_db.drop_collection('merchant_online_666')


def post_mer_jpg():
    files = {'material': ('sf.jpg',open('/home/ellen/sf.jpg','rb'),'image/jpeg')}
    merchant_item = json.dumps({"name": "yjoqmtest", "loc": "http://XX.com", "advertiser_id":666, "outerID": "1","_id":1})
    merchant_post= {"offline":False,"advertiser_id":666, "merchant":merchant_item}
    url = "http://192.168.0.8888:8000/v1/api/merchants/"
    r = requests.post(url, data=merchant_post,files=files)
    assert_equal(r.status_code, 200)
    print r.text

def post_mer_gif():
    files = {'material': ('pingan_336x280_1031.gif',open('/home/ellen/XX/image/pingan_336x280_1031.gif','rb'),'image/gif')}
    merchant_item = json.dumps({"name": "yjoqmtest", "loc": "http://XX.com", "advertiser_id":666, "outerID": "2","_id":2})
    merchant_post= {"offline":False,"advertiser_id":666, "merchant":merchant_item}
    url = "http://192.168.0.8888:8000/v1/api/merchants/"
    r = requests.post(url, data=merchant_post,files=files)
    print r.text
    assert_equal(r.status_code, 200)

def post_mer_flv():
    files = {'material': ('test.flv',open('/home/ellen/XX/image/test.flv','rb'),'video/x-flv')}
    merchant_item = json.dumps({"name": "test_flv", "loc": "http://XX.com", "advertiser_id":666, "outerID": "4","_id":4})
    merchant_post= {"offline":False,"advertiser_id":666, "merchant":merchant_item}
    url = "http://192.168.0.8888:8000/v1/api/merchants/"
    r = requests.post(url, data=merchant_post,files=files)
    print r.text
    assert_equal(r.status_code, 200)


def post_mer_swf():
    files = {'material': ('100_300flash1.swf',open('/home/ellen/XX/image/100_300flash1.swf','rb'),'application/x-shockwave-flash')}
    merchant_item = json.dumps({"name": "test_swf", "loc": "http://XX.com", "advertiser_id":666, "outerID": "5","_id":5})
    merchant_post= {"offline":False,"advertiser_id":666, "merchant":merchant_item}
    url = "http://192.168.0.8888:8000/v1/api/merchants/"
    r = requests.post(url, data=merchant_post,files=files)
    print r.text
    assert_equal(r.status_code, 200)
 
def main():
     delete_666()
     post_mer_jpg()
     post_mer_gif()
     post_mer_flv()
     post_mer_swf()
    

if __name__ == '__main__':
    main()
    #test =  delete_666()
    #test = post_mer_jpg()
    #test = post_mer_gif()
    #test = post_mer_flv()
    #test = post_mer_swf()
