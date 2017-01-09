#!/usr/bin/python

import sys
import os
import httplib
import urllib
import poster
import json
import time
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class VTSericeSut:
    def __init__(self, args):
        self.test_module = args[0]
        self.args = []
        for arg in args[1:]:
            self.args.append(arg)
    
    def vts_http_api_call(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        request_body = urllib.unquote_plus(params[5])
        request_header = urllib.unquote_plus(params[6])
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
            
        if request_body == 'None' or request_body == 'none':
            request_body = None

        return_msg = {}
        conn.request(method, url, request_body, json.loads(request_header))
        response = conn.getresponse()
        body = response.read()
        header = response.getheaders()
        conn.close()
        ret_header = {}
        for item in header:
            ret_header[item[0]] = item[1]

        try:
            body = json.loads(body)
        except Exception,ex:
            body = body
        return_msg["code"] = response.status
        return_msg["body"] = body
        return_msg["header"] = ret_header
        
        return json.dumps(return_msg)

    def run(self):
        function = getattr(self, self.test_module)
        fun_return = function(self.args)
        return fun_return
        
if __name__ == "__main__":
    sut = VTSericeSut(sys.argv[1:])
    print sut.run()
        