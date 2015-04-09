#!/usr/bin/env python
# coding=utf-8
#使用robot创建会话,清空会话
import robot
import requests
import robot.libraries.BuiltIn import BuiltIn

Class Keywords(object):
    def __init__(self):  #初使化
        self._cache = robot.utils.ConnectionCache('NO SESSION CREATE')
        self.builtIn = BuiltIn
    '''创建会话'''
    def create_requests_session(self,req_alias='requets_test'):
        self._cache.register(req,alias=req_alias)
        req = requests.session()

    '''清空会话'''
    def delete_requests_session(self):
        self._cache.empty_cache()

     def json_post(self,url,data,req_alias = 'requets_test'):
         req = self._cache.switch(req_alias)
         return req.post(url,json.dumps(data))


