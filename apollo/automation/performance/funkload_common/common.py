# -*- coding: UTF-8 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
import sys
import os
import httplib
from random import random
from funkload.utils import Data
from webunit.utility import Upload
from funkload.FunkLoadTestCase import FunkLoadTestCase
from ConfigParser import ConfigParser, NoSectionError, NoOptionError
import json
from datetime import datetime


class FunkloadCommon(FunkLoadTestCase):
    #def __init__(self, methodName='runTest', options=None):
        #FunkLoadTestCase.__init__(self, methodName, options)
    """This test use a configuration file Simple.conf."""
    def setUp(self):
        """Setting up test."""
        #读取配置文件中的URL和文件信息
        self.host = self.conf_get('main', 'url')
        self.error_log = self.conf_get('main', 'error_log')
        pass

    def test_common(self):
        try:
            #获取测试网页的数量
            page_number = int(self.conf_get("pages", "page_number"))
            #获取需测试网页编号
            test_page_list_conf = self.conf_get("pages", "test_page_list")
    
            for page_index in range(page_number):
                section = "page_%s_section" % page_index
                if test_page_list_conf.lower() not in ["noset", "all"]:
                    if page_index not in json.loads(test_page_list_conf):
                        continue
                elif test_page_list_conf.lower() == "noset":
                    if "false" == self.conf_get(section, "need_test").lower():
                        continue
                    
                http_method = self.conf_get(section, "page_method")
                function = getattr(self, http_method.lower())
                self.url_path = self.conf_get(section, "page_path")
                
                request_type = self.conf_get(section, "request_type").lower()
                if request_type == "none":
                    self.request = None
                elif request_type == "data":
                    data_type = self.conf_get(section, "data_type")
                    data = self.conf_get(section, "data")
                    if data.startswith("@"):
                        data = open(data[1:]).read()
                    
                    self.request = Data(data_type, data)
                elif request_type == "params":
                    data = json.loads(self.conf_get(section, "data").replace("'", '"'))
                    for items in data:
                        if items[1].startswith("upload@"):
                            items[1] = Upload(items[1][7:])
                        elif items[1].startswith("@"):
                            items[1] = open(items[1][1:]).read()
                    
                    #这里可能需要处理一下数据，请填写自定义代码
                    pass
                    self.request = data
                
                ok_codes = self.conf_get(section, "ok_codes")
                if ok_codes.lower() != "none":
                    ok_codes = map(lambda x:int(x.replace(" ", "")), ok_codes.split(","))
                else:
                    ok_codes = None
                    
                #添加头
                try:
                    self.clearHeaders()
                    heads = self.conf_get(section, "headers")
                    for head in heads.split("&&&"):
                        item = head.split("===")
                        self.addHeader(item[0], item[1])
                except NoOptionError, ex:
                    pass
                
                #前处理
                self.request_preprocess(page_index)
                
                #接口调用
                self.response = function(self.host + self.url_path, self.request, description = self.host + self.url_path, ok_codes = ok_codes)
                #print self.response.headers
                self.log_write(self.response.body)
                
                #后处理
                self.postprocess(page_index)
                
        except Exception,ex:
            self.error_log_write(str(ex))

    def request_preprocess(self, page_index):
        pass
    
    def postprocess(self, page_index):
        pass

    def error_log_write(self, msg):
        msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": %s\r\n" % msg
        print msg
        open(self.error_log, "a").write(msg)
        
    def log_write(self, msg):
        msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": %s\r\n" % msg
        #print msg
        if "true" == self.conf_get("main", "ok_log_write").lower():
            open(self.conf_get("main", "ok_log"), "a").write(msg)
        pass
        
if __name__ in ('main', '__main__'):
    unittest.main()
