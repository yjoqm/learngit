#!/usr/bin/env python
# coding=utf-8
import pymongo
merchant_db = pymongo.MongoClient("mongodb://mc:mc@192.168.0.229/merchant").get_default_database()
col = merchant_db["merchant_offline_9"]
outid = []
for item in col.find({"feed_id":607}):
    i = item['outerID']
    outid.append(i)

with open('/home/ellen/test.txt','a') as f:
    for i in outid:
        f.write('9,')
        f.write(i)
        f.write(',2')
        f.write("\n")
f.close()

   
