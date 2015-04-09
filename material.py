#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
import json
import test_bak

PROJECT_ID = 23
advertiser_id = int(raw_input("input advertiser_id: ").strip())
material_id = int(raw_input("input material_id: ").strip())

def gen_48mid(advertiser_id, merchant_id):
    return (advertiser_id << 32) + merchant_id

def l48mid2l32(long_id):
    advertiser_id = long_id >> 32
    merchant_id = long_id - (advertiser_id << 32)
    return advertiser_id, merchant_id

def gen_64id(short_id, project_id=PROJECT_ID):
    return (1 << 60) + (project_id << 48) + short_id

def l64id2l48(long_id):
    version = long_id >> 60
    project_id = (long_id >> 48) - (version << 12)
    l48_id = long_id - (1 << 60) - (project_id << 48)
    return version, project_id, l48_id

def gen_64mid(advertiser_id, merchant_id):
    long48mid = gen_48mid(int(advertiser_id), int(merchant_id))
    return gen_64id(long48mid)
print "64id is: %s" % gen_64mid(advertiser_id,material_id)

def l64mid2l32(long_id):
    version, project_id, l48_id = l64id2l48(long_id)
    advertiser_id, merchant_id = l48mid2l32(l48_id)
    return version, project_id, advertiser_id, merchant_id

def material_info(advertiser_id,material_id):
    merchant_db = pymongo.MongoClient("mongodb://mc:mc@192.0.0.1/merchant").get_default_database()
    col = merchant_db["merchant_online_%s" % advertiser_id]
    for item in col.find({"_id":material_id}):
        test1 = json.dumps(item,sort_keys=True,indent=4,encoding="utf-8")
        return test1
print material_info(advertiser_id, material_id)

print test_bak.get_fetch(gen_64mid(advertiser_id,material_id))
