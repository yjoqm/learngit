#/usr/bin/env python
#coding=utf-8

'''
#dropping a database via pymongo
from pymongo import Connection
c = Connection()
c.drop_database('mydatabase')
 
# drop a collection via pymongo
from pymongo import Connection
c = Connection()
c['mydatabase'].drop_collection('mycollection')
'''
#以下是两种连接库的方法
import pymongo
'''
client = pymongo.MongoClient("localhost",27017)
db = client['yjoqm']
col = db['yjoqm']
col.insert({"ad_id":1,"name":"test_3"})
'''
#第二种方法
yjoqm_db = pymongo.MongoClient("mongodb://localhost:27017/yjoqm").get_default_database()
print yjoqm_db
col = yjoqm_db['yjoqm']

#常见的一些操作
#查询
for u in col.find({"ad_id":130}):
    print u
u2 = col.find_one({"ad_id":1})
print u2 #查不到时返回NONE
#排序 pymongo.ASCENDING或者pymongo.DESCENDING
for u in col.find().sort([("_id",pymongo.ASCENDING)]):
    print u

#使用正则
for u in col.find({"name" : {"$regex" : r"(?i)user[yj.*]"}}, ["name"]): print u

#使用切片
for u in col.find({"name":"user1"}):
    print u['im']['msn']

#取反set unset

col.update({'name':"user1"}, {'$unset':{'address':1, 'age':1}})
for u in col.find({"name":"user1"}):print u

