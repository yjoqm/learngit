#!/usr/bin/env python
# coding=utf-8

import redis
import os
import sys


r = redis.Redis(host='192.168.0.229',port=6379,db=6)

def find_key(key):
    return r.get(key)
    

def find_all_data(key):
    return r.keys()

def remove_key(key):
    if r.exists(key):
        r.delete(key)
        return "delete success~~"
    else:
        return "key not exists~~"


def main(args):
    func = args[1]
    arg = args[2]
    if func == 'find_key':
        print find_key(arg)
    elif func == 'find_all_data':
        print find_all_data(arg)
    elif func == 'remove_key':
         print remove_key(arg)
    else:
        print "input erro~~r"
        sys.exit(2)

if __name__ == '__main__':
    #find_key("7ed6e14d7792cc29d31d50a7ddd16269")
    #remove_key("7ed6e14d7792cc29d31d50a7ddd16269")
    args = sys.argv
    if len(args) < 3:
        print "please input find_key or remove_key or find_all_data "
        sys.exit(2)
    main(args)
