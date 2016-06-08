#!/usr/bin/env python
# coding=utf-8

import redis

r = redis.Redis(host='127.0.0.1',port=6379)
#r = redis.Redis(host='192.168.0.229',port=6379) 也可以不选择DB

def find_key(key):
    print r.get(key)

def find_all_data():
    count =  r.keys()
    return len(count)

def all_key():
    keys = r.keys()
    return keys

def remove_key(key):
    if r.exists(key):
        r.delete(key)
        print "delete success~~"
    else:
        print "key not exists~~"

def remove_all(keys):
    for i in keys:
        print i
        r.delete(i)

if __name__ == '__main__':
    #test = find_all_data()
   # print test
    keys = all_key()
    #print keys
    remove_all(keys)
    print "done"
    #find_key("7ed6e14d7792cc29d31d50a7ddd16269")
    #remove_key("7ed6e14d7792cc29d31d50a7ddd16269")
