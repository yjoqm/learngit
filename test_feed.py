#!/usr/bin/env python
# coding=utf-8
import pymongo
import time
import csv
import datetime

merchant_db = pymongo.MongoClient("mongodb://mc:mc@192.168.0.229/merchant").get_default_database()
col = merchant_db["merchant_offline_9"]

#feed.txt为结果文件,只包含materid_id

def time_str(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
li = []
with open("/home/ellen/result.txt","r") as f:
    for eachline in f:
        eachline = eachline.strip()
        li.append(int(eachline))
#print li
#验证结果文件中的素材不存在feed_id为false的情况,如果存在则会打印出来
for i in li:
    for item in col.find({"_id":i,"feed_id":{"$exists":False}}):
        print "feed_id not exists is: ",item

#需要跟据id查到该素材的updata_time,验证时间点
update_time = []
for i in li:
    for k in col.find({"_id":i}):
         update_time.append(k["update_time"])
#print [time_str(i) for i in update_time]
uptime = datetime.datetime.now() - datetime.timedelta(days=30)
#print uptime
timeArray = time.strptime(str(uptime), "%Y-%m-%d %H:%M:%S.%f")
timeStamp = int(time.mktime(timeArray))
for ti in update_time:
    if ti > timeStamp:
        print "time error:", ti


#验证csv中的素材r不存在于结果文件中
outerid = []
id = []
with open('/home/ellen/yjoqm/a.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=',',quotechar='|')
    for row in spamreader:
        outerid.append(','.join(row))
for i in range(len(outerid)):
    test_id = outerid[0].split(",")
    id.append(int(test_id[1])) #拿到outerid
#对比outerid不存在结果文件中
with open('/home/ellen/result.txt','r') as handle:
    for ln in handle:
        for outerid in id:
            if str(outerid)  in ln:
                 print "outerid in result file"

