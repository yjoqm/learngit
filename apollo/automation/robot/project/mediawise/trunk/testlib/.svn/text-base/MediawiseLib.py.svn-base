import os
import sys
from robot.api import logger
from robot.api import *
from run_cmd import RunCmd
import json
import re
import copy
import urllib2
import inspect
import httplib
import poster
user_module_path = os.path.dirname(os.path.realpath(__file__))



class MediawiseLib:
    def __init__(self):
        pass

    def set_mediawise_host(self, host, port, ssl):
        if ssl not in ['http', 'https']:
            raise AssertionError("'ssl' should be 'http' or 'https' but it was '%s'" % ssl)
        else:
            self.ssl = ssl
        self.host = str(host)
        self.port = str(port)
        
        
    def mediawise_http_api_call(self, *argvs):
        for item in argvs[2:]:
            pare = item.split("=")
            if pare[0] == "action" and pare[1] == "submit":
                return self.__api_submit(argvs)
            
        return self.__api_not_submit(argvs)
    
    def __api_not_submit(self, argvs):
        method = argvs[0]
        url = argvs[1]
        conn_fun = getattr(httplib, "%sConnection" % self.ssl.upper())
        conn = conn_fun(self.host, self.port)
        request = "%s?" % url + "&".join(argvs[2:])
        conn.request("GET", request, None)
        response = conn.getresponse()
        body = response.read()
        conn.close()
        return body
    
    def __api_submit(self, argvs):
        method = argvs[0]
        url_path = argvs[1]
        params = argvs[2:]
        url = "%s://%s:%s%s" % (self.ssl, self.host, self.port, url_path)
        poster_params = {}
        for param in params:
            pare = param.split("=")
            if pare[0] == "dna":
                poster_params[pare[0]] = open(pare[1], "rb")
            else:
                poster_params[pare[0]] = pare[1]
        poster.streaminghttp.register_openers()
        datagen, headers = poster.encode.multipart_encode(poster_params)
        request = urllib2.Request(url, datagen, headers)
        result = urllib2.urlopen(request)
        return result.read()
    

        

    

    
    
    

if __name__ == "__main__":
    mediawise = MediawiseLib()
    mediawise.set_mediawise_host("192.168.1.181", "80", "http")
    body = mediawise.mediawise_http_api_call("GET", "/service/mediawise", "action=obtain_token", "username=test", "password=123456")
    print body
    body = mediawise.mediawise_submit_call("POST", "/service/mediawise", "action=submit", "username=test", "password=123456", "dna=/home/yan_jiawei/workspace/automation/APOLLO/TVSYNC/trunk/data/mediawise/26476828.far")
    print body
    pass
    