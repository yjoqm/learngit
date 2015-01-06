#!/usr/bin/env python
#encoding:utf-8
import os
import robot
import requests
import pymongo
import json
import copy
from robot.libraries.BuiltIn import BuiltIn

from nose.tools import assert_equal, assert_dict_equal

img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','imgs' )

class McKeywords(object):

    def __init__(self):
        self._cache = robot.utils.ConnectionCache('No sessions created')
        self.builtin = BuiltIn()
        self.del_list = ['update_time','create_time','_id']


    def create_session(self,req_alias='mc'):
        """
        创建会话
        """
        req = requests.Session()
        self._cache.register(req,alias=req_alias)


    def create_mongo_client(self,uri,client_alias='mm'):
        """
        创建mongo客户端
        """
        client = pymongo.MongoClient(uri)
        self._cache.register(client,alias=client_alias)


    def delete_all_session(self):
        """
        清空会话
        """
        self._cache.empty_cache()


    def resp_should_be_equal(self,resp,expect):
        """
        断言相等
        """
        failed = {
                'resp':resp,
                'expect':expect,
                }
        self.builtin.log(failed)
        if isinstance(expect,dict):
            assert_dict_equal(resp,expect,failed)
        assert_equal(resp,expect,failed)


    def is_empty_list(self,t_list):
        assert isinstance(t_list,list)
        assert len(t_list) == 0


    def init_db(self,client_alias='mm'):
        """
        初始化db
        """
        client = self._cache.switch(client_alias)
        db = client[client_alias]
        col_list = db.collection_names()
        for col in col_list:
            if u'system' not in col:
                db.drop_collection(col)


    def json_post(self,url,data,req_alias='mc'):
        req = self._cache.switch(req_alias)
        return req.post(url,json.dumps(data))


    def kv_post(self,url,data,req_alias='mc'):
        req = self._cache.switch(req_alias)
        return req.post(url,data)

    def mer_post(self,url,data,req_alias='mc'):
        files = {
                'material':(data['material'],open(os.path.join(img_path,data['material']),'rb'),'image/jpeg')
                }
        del data['material']
        req = self._cache.switch(req_alias)
        return req.post(url,data,files=files)


    def xml_post(self,url,data,req_alias='mc'):
        req = self._cache.switch(req_alias)
        xml = data['xml']
        del data['xml']
        return req.post(url,params=data,data=xml)


    def get(self,url,params={},req_alias='mc'):
        req = self._cache.switch(req_alias)
        return req.get(url,params=params)


    def put(self,url,data,req_alias='mc'):
        req = self._cache.switch(req_alias)
        return req.put(url,data)


    def delete(self,url,req_alias='mc'):
        req = self._cache.switch(req_alias)
        return req.delete(url)


    def m_select(self,db_name,coll_name,mid='',*args):
        del_list = copy.deepcopy(self.del_list)
        del_list.extend(args)
        find_item = {}
        if mid:
            find_item = {"_id":mid}
        find_list = []
        client = self._cache.switch(db_name)
        coll = client[db_name][coll_name]
        curs = coll.find(find_item)
        for cur in curs:
            for item in del_list:
                if cur.has_key(item): del cur[item]
            find_list.append(cur)
        return find_list


    def mer_select(self,onoff,advertiser_id,mid='',client_alias='merchant',*args):
        del_list = copy.deepcopy(self.del_list)
        del_list.extend(args)
        if mid:
            find_item = {"_id":mid}
        find_list = []
        coll_name = "merchant_{}_{}".format(onoff,advertiser_id)
        client = self._cache.switch(client_alias)
        coll = client['merchant'][coll_name]
        curs = coll.find(find_item)
        for cur in curs:
            for item in del_list:
                if cur.has_key(item): del cur[item]
            find_list.append(cur)
        return find_list


    def to_json(self,string):
        return json.loads(string)


    def to_list(self,*args):
        return list(args)
                    

    def pipe_res(self,res,*args):
        del_list = copy.deepcopy(self.del_list)
        del_list.extend(args)
        if isinstance(res,list):
            for r in res:
                return self.delete_item(r,del_list)
        return self.delete_item(res,del_list)


    def delete_item(self,thin,*args):
        del_list = copy.deepcopy(self.del_list)
        del_list.extend(args)
        for item in del_list:
            if thin.has_key(item): del thin[item]
        return thin














