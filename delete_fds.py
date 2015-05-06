#!/usr/bin/env python
# coding=utf-8
import pymongo
def delete_fds(ad_id):
    merchant_db = pymongo.MongoClient("mongodb://mc:mc@192.168.0.229/merchant").get_default_database()
    offline_col = merchant_db["merchant_offline_%s"% ad_id]
    for item in offline_col.find():
        li_id = []
        li_id.append(item["_id"])
        for id in li_id:
            offline_col.update({"_id":id},{"$unset":{"dfs_path":""}})

    online_col = merchant_db["merchant_online_%s"% ad_id]
    for item in online_col.find():
        lion_id = []
        lion_id.append(item["_id"])
        for id in lion_id:
            online_col.update({"_id":id},{"$unset":{"dfs_path":""}})


if __name__=='__main__':
    test = delete_fds(8)
    print test

