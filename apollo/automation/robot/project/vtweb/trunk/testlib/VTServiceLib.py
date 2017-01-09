import os
import sys
from robot.api import logger
from robot.api import *
from run_cmd import RunCmd
import json
import re
import copy
import urllib
import inspect
from uuid import uuid1
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class VTServiceLib:
    def __init__(self):
        self.cmd = ["python"]
        
    def __vts_sut_run(self, module, argv):
        cmd = self.__make_cmd(module, argv)
        for i in range(len(cmd)):
            if i >= 8:
                cmd[i] = urllib.quote_plus(cmd[i])
        logger.warn(cmd)
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout
    
    def set_vts_host(self, host, port, ssl):
        if ssl not in ['http', 'https']:
            raise AssertionError("'ssl' should be 'http' or 'https' but it was '%s'" % ssl)
        else:
            self.ssl = ssl
        self.host = host
        self.port = port
    
    def set_vts_sut_file(self, sut_file):
        self.sut_file = sut_file
        self.cmd.append(self.sut_file)
        
    def __make_cmd(self, module, argv):
        cmd = copy.deepcopy(self.cmd)
        cmd.append(module)
        cmd.append(self.host)
        cmd.append(self.port)
        cmd.append(self.ssl)
        for arg in argv:
            cmd.append(arg)
        return cmd

    def vts_http_api_call(self, method, url, body='None', header='{}'):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, body, header)))))
        if body[0] == '{' and body[-1] == '}':
            try:
                json_body = json.loads(body)
            except TypeError, ex:
                raise AssertionError(ex)
            except ValueError, ex:
                raise AssertionError("request body json format error")
            body = json.dumps(json_body)
            
        try:
            json_header = json.loads(header)
        except TypeError, ex:
            raise AssertionError(ex)
        except ValueError, ex:
            raise AssertionError("request header json format error")
        header = json.dumps(json_header)

        return self.__vts_sut_run("vts_http_api_call", (method, url, body, header))

    def update_match_data(self,d_data,u_data):
        d_data = eval(d_data)
        u_data = eval(u_data)
        for k,v in u_data.items():
            d_data[k] = v
        return d_data

if __name__ == "__main__":
    a ={'rating': '', 'cast': 'test_cast', 'studio_owner': 'test_studio_owner', 'title': 'new_movie_test', 'updated_at': '0000-00-0000:00:00', 'release_date': '2013-03-06', 'company_id': 1, 'refresh_updated_at': 'true', 'id': {'type': 'ISRC', 'value': 'BigHead'}, 'genre': 'test_genre', 'tag': 'aaaa', 'duration': 100, 'typed_info': {'director': 'director', 'alternate_info': 'alternate_info', 'description': 'description', 'alternate_url': 'alternate_url', 'country': 'country', 'metalink': 'metalink', 'sub_type': 'Movie', 'track_no': 0}, 'created_at': '0000-00-0000:00:00', 'type': 'Movie', 'right_owner': 'test_right_owner', 'is_valid': 'valid'}
    print str(a)
    #pyweb = VddbLib()
    #pyweb.set_pyweb_sut_file("/home/yan_jiawei/workspace/automation/APOLLO/TVSYNC/trunk/common_op/sut/vddb/pyweb.py")
    #pyweb.set_pyweb_host("192.168.1.19", "88",'http')
    #ret = pyweb.pyweb_api_call("POST", "/mediawise/auth", '{"protocols": ["5.2.6"], "user": "zhang_jin", "password": "123"}')
    #print ret
