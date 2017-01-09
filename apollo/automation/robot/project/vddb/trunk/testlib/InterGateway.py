#!/usr/bin/python
#coding: utf-8

import sys
import json
import base64
import requests
import unittest
import copy
from datetime import date 

class InterGateway:
    def clear_empty(self,dicts):
        """ 清除空字符串 """
        for d in dicts:
            [d.pop(k)
             for k, v in d.iteritems()
             if (v is None
                 or (isinstance(v, (str, unicode)) and len(v)==0))]

    def gateway_get(self,case):
        ''' gateway get  requests\
            xxx
        '''
        URL = '{}://{}:{}/copyrighted'.format(case['scheme'], case['host'], case['port'])
        headers = {
            'User-Agent':case['user-agent'],
            'X-Progress': case['X-Progress'],
            'X-Client-Address': case['X-Client-Address'],
            'X-Client-ID': case['X-Client-ID'],
            'X-File-Name': case['X-File-Name'].encode('utf-8'),
            'X-File-Size': case['X-File-Size'],
            'X-Mime-Type': case['X-Mime-Type'],
            'Referer':case['Referer'].encode('utf-8'),
            'If-Modified-Since':date.today().ctime(),
            'Date':date.today().ctime(),
            'X-URL': case['url'].encode('utf-8')
        }

        params = {
            'key': case['key'],
            'hash': case['hash'],
            'digest': case['digest'],
            'digest-algorithm': case['digest-algorithm']
        }

        # 清除空字符串
        # clear_empty([headers, params])
        
        resp = requests.get(URL, headers=headers, params=params, verify=False)
        #print resp.status_code
        #print resp.headers
        #print resp.text
        return resp
        
    def gateway_get2(self,case):
        ''' gateway get  requests\
            xxx
        '''
        URL = '{}://{}:{}/copyrighted'.format(case['scheme'], case['host'], case['port'])
        headers = {
            'User-Agent':case['user-agent'].encode('utf-8'),
            'X-Progress': case['X-Progress'].encode('utf-8'),
            'X-Client-Address': case['X-Client-Address'].encode('utf-8'),
            'X-Client-ID': case['X-Client-ID'].encode('utf-8'),
            'X-File-Name': case['X-File-Name'].encode('utf-8'),
            'X-File-Size': case['X-File-Size'].encode('utf-8'),
            'X-Mime-Type': case['X-Mime-Type'].encode('utf-8'),
            'Referer':case['Referer'].encode('utf-8'),
            'If-Modified-Since':date.today().ctime(),
            'Date':date.today().ctime(),
            'X-URL': case['url'].encode('utf-8')
        }

        params = {
            'key': case['key'].encode('utf-8'),
            'hash': case['hash'].encode('utf-8'),
            'digest': case['digest'].encode('utf-8'),
            'digest-algorithm': case['digest-algorithm'].encode('utf-8')
        }

        # 清除空字符串
        # clear_empty([headers, params])
        
        resp = requests.get(URL, headers=headers, params=params, verify=False)
        #print resp.status_code
        #print resp.headers
        #print resp.text
        return resp

    def gateway_post(self,case):
        URL = '{}://{}:{}/copyrighted'.format(case['scheme'], case['host'], case['port'])
        headers = {
            'User-Agent':case['user-agent'],
            'X-Progress': case['X-Progress'],
            'X-Client-Address': case['X-Client-Address'],
            'X-Client-ID': case['X-Client-ID'],
            'X-File-Name': case['X-File-Name'].encode('utf-8'),
            'X-File-Size': case['X-File-Size'],
            'X-Mime-Type': case['X-Mime-Type'],
            'Referer':case['Referer'].encode('utf-8'),
            'If-Modified-Since':date.today().ctime(),
            'Date':date.today().ctime(),
            'X-URL': case['url'].encode('utf-8')
        }
        
        params = {
            'key': case['key'],
            'hash': case['hash'],
            'digest': case['digest'],
            'digest-algorithm': case['digest-algorithm']
        }

        if case['seed_file']=="":
            data = {
                "jsonrpc": "2.0",
                "id": "1",
                "method": "query",
                "params":{'seed_file': ""}
            }
        else:
            path = case['seed_file']
            with open(path, 'r') as f:
                content = base64.b64encode(f.read())
                #print 'cotent###############', content
            data = {
                "jsonrpc": "2.0",
                "id": "1",
                "method": "query",
                "params":{'seed_file': content}
            }


        # 清除空字符串
        # clear_empty([headers, params])

        resp = requests.post(URL, headers=headers, params=params, data=json.dumps(data), verify=False)
        #print resp.status_code
        #print resp.headers
        #print resp.text
        return resp

    def gateway_post2(self,case):
        URL = '{}://{}:{}/copyrighted'.format(case['scheme'], case['host'], case['port'])
        headers = {
            'User-Agent':case['user-agent'].encode('utf-8'),
            'X-Progress': case['X-Progress'].encode('utf-8'),
            'X-Client-Address': case['X-Client-Address'].encode('utf-8'),
            'X-Client-ID': case['X-Client-ID'].encode('utf-8'),
            'X-File-Name': case['X-File-Name'].encode('utf-8'),
            'X-File-Size': case['X-File-Size'].encode('utf-8'),
            'X-Mime-Type': case['X-Mime-Type'].encode('utf-8'),
            'Referer':case['Referer'].encode('utf-8'),
            'If-Modified-Since':date.today().ctime(),
            'Date':date.today().ctime(),
            'X-URL': case['url'].encode('utf-8')
        }
        
        params = {
            'key': case['key'].encode('utf-8'),
            'hash': case['hash'].encode('utf-8'),
            'digest': case['digest'].encode('utf-8'),
            'digest-algorithm': case['digest-algorithm'].encode('utf-8')
        }

        if case['seed_file']=="":
            data = {
                "jsonrpc": "2.0",
                "id": "1",
                "method": "query",
                "params":{'seed_file': ""}
            }
        else:
            path = case['seed_file']
            with open(path, 'r') as f:
                content = base64.b64encode(f.read())
                #print 'cotent###############', content
            data = {
                "jsonrpc": "2.0",
                "id": "1",
                "method": "query",
                "params":{'seed_file': content}
            }


        # 清除空字符串
        # clear_empty([headers, params])

        resp = requests.post(URL, headers=headers, params=params, data=json.dumps(data), verify=False)
        #print resp.status_code
        #print resp.headers
        #print resp.text
        return resp

    def req_http_url(self,ssl,host,port,method,*args, **kwargs):
        #http://host:port/vddb-async/matches?site_asset_id=url_hash#f8fabdde-e0f4-11e3-b471-fa163e4c5cc4
        URL = '{}://{}:{}/vddb-async/matches'.format(ssl, host, port)
        params={
            'site_asset_id':""
        }
        
        keys_list = kwargs.keys()
        difference_list = list(keys_list)
        for a in difference_list:
            params[str(a)] = kwargs[a].encode('utf-8')
        resp = requests.get(URL, headers={}, params=params, verify=False)
        print resp.status_code
        print resp.headers
        print resp.text
        return [resp.status_code,resp.text]       

    def set_value(self,template_json,case_json):
        use_json=copy.copy(template_json)
        for k, v in case_json.iteritems():
            use_json[k]=v
        return use_json

    def test_result(self,expect_result,resp):
        print expect_result
        print resp.status_code
        print resp.text
        resp_result=json.dumps(resp.text)

    def req_gateway(self,template_json,paramsDict):
        ''' 
         all params can input chinese character.

         template_file is a file and file format :
         {"scheme":"http","host":"182.92.9.187","port":8080,"key":"this-is-TMP-apikey",
         "X-Progress": "10","X-Client-Address": "192.168.1.1",
         "X-Client-ID": "client_id123456","X-File-Name":"qa_test",
         "X-File-Size": "123456","X-Mime-Type": "video/mp4","hash": "",
         "digest": "018e206e00bdc68374ff32bb0245d98ea703090e",
         "digest-algorithm": "sha1","method": "GET",
         "url": "http://115.29.36.65/clips/youku_28.flv",
         "seed_file":"123.torrent","seed_encoded":"true",
         "user-agent":"Thunder Windows Client 7.0"
         }

         paramsDict format:
            {"url":"http:/xxx/xxx/xxx"}

        '''
        template1_json = json.loads(template_json);
        print paramsDict
        use_case=self.set_value(template1_json,paramsDict);
        print use_case
        if use_case['method'] == 'post':
           resp= self.gateway_post2(use_case)
        else:
           resp= self.gateway_get2(use_case)
        d=[]
        d.append(resp.status_code)
        d.append(resp.text)
        return d

    def req_gateway2(self,template_json,paramsDict):
        '''
        template_json format:
         {"scheme":"http","host":"182.92.9.187","port":8080,"key":"this-is-TMP-apikey",
         "X-Progress": "10","X-Client-Address": "192.168.1.1",
         "X-Client-ID": "client_id123456","X-File-Name":"qa_test",
         "X-File-Size": "123456","X-Mime-Type": "video/mp4","hash": "",
         "digest": "018e206e00bdc68374ff32bb0245d98ea703090e",
         "digest-algorithm": "sha1","method": "GET",
         "url": "http://115.29.36.65/clips/youku_28.flv",
         "seed_file":"123.torrent","seed_encoded":"true",
         "user-agent":"Thunder Windows Client 7.0"
         }

         paramsDict format:
            {"url":"http:/xxx/xxx/xxx"}
        '''
        template1_json = json.loads(template_json);
        print paramsDict
        use_case=self.set_value(template1_json,paramsDict);
        print use_case
        if use_case['method'] == 'post':
           resp= self.gateway_post(use_case)
        else:
           resp= self.gateway_get(use_case)
        d=[]
        d.append(resp.status_code)
        d.append(resp.text)
        return d

if '__name__' == '__main__':
   print 1 
