#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
import json
import test_bak

PROJECT_ID = xxxx
VERSION = 1
CUR_DFS_ID = 2

class Ids(object):
    def __init__(self):
        self.advertiser_id = 0
        self.merchant_id = 0
        self.version = VERSION
        self.dfs_id = CUR_DFS_ID
        self.project_id = PROJECT_ID

    def from_long(self, long_id):
        self.version = long_id >> 60
        long_str = bin(long_id)[2:].zfill(64)
        self.dfs_id = int(long_str[4:8], 2)
        self.project_id = int(long_str[8:16], 2)
        self.advertiser_id = int(long_str[16:32], 2)
        self.merchant_id = int(long_str[32:], 2)

    def to_long(self, advertiser_id=None, merchant_id=None, version=None, dfs_id=None, project_id=None):
        if advertiser_id is not None:
            self.advertiser_id = int(advertiser_id)
        if merchant_id is not None:
            self.merchant_id = int(merchant_id)
        if version is not None:
            self.version = int(version)
        if dfs_id is not None:
            self.dfs_id = int(dfs_id)
        if project_id is not None:
            self.project_id = int(project_id)
        l_version = self.version << 60
        l_dfs_id = self.dfs_id << 56
        l_project_id = self.project_id << 48
        l_advertiser_id = self.advertiser_id << 32
        return l_version | l_dfs_id | l_project_id | l_advertiser_id | self.merchant_id

advertiser_id = int(raw_input("input advertiser_id: ").strip())
material_id = int(raw_input("input material_id: ").strip())

def material_info(advertiser_id,material_id):
    merchant_db = pymongo.MongoClient("mongodb://mxx:xxx@192.168.0.xx9/met").get_default_database()
    col = merchant_db["merchant_online_%s" % advertiser_id]
    for item in col.find({"_id":material_id}):
        test1 = json.dumps(item,sort_keys=True,indent=4,encoding="utf-8")
        return test1
    print material_info(advertiser_id, material_id)

if __name__ == '__main__':
    c = Ids()
    mater_id = c.to_long(advertiser_id,material_id)
    print "64id is: %s" % mater_id
    print material_info(advertiser_id,material_id)
    print test_bak.get_fetch(mater_id)





