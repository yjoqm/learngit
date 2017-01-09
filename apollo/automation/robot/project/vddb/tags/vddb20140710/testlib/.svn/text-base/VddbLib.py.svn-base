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
from robot.api import logger
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class VddbLib:
    def __init__(self):
        self.cmd = ["python"]

    def __pyweb_sut_run(self, module, argv):
        cmd = self.__make_cmd(module, argv)
        #logger.warn(cmd)
        for i in range(len(cmd)):
            if i >= 8:
                cmd[i] = urllib.quote_plus(cmd[i])
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def set_pyweb_host(self, host, port, ssl):
        if ssl not in ['http', 'https']:
            raise AssertionError("'ssl' should be 'http' or 'https' but it was '%s'" % ssl)
        else:
            self.ssl = ssl
        self.host = host
        self.port = port

    def set_pyweb_sut_file(self, sut_file):
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

    def pyweb_api_call(self, method, url, body='None', header='{}'):
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

        return self.__pyweb_sut_run("pyweb_api_call", (method, url, body, header))
    
    def send_dna(self, method, url, file_name, dna_type, token):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, file_name, dna_type, token)))))
        return self.__pyweb_sut_run("send_dna", (method, url, file_name, dna_type, token))
    
    def dna_ingest(self, method, url, file_name, token):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, file_name, token)))))
        return self.__pyweb_sut_run("dna_ingest", (method, url, file_name, token))
    
    def send_idna(self, method, url, file_name, dna_type, file_type, token):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, file_name, dna_type, file_type, token)))))
        if dna_type not in ["frame", "screenshot"]:
            raise AssertionError("dna_type should be 'frame' or 'screenshot' but was '%s'" % dna_type)
        if file_type not in ["folder", "file"]:
            raise AssertionError("file_type should be 'file' or 'folder' but was '%s'" % file_type)
        return self.__pyweb_sut_run("send_idna", (method, url, file_name, dna_type, file_type, token))
    
    def custom_send_idna(self, method, url, token, *argv):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, token, argv)))))
        if len(argv) <= 1 or 0 != len(argv) % 2:
            raise AssertionError("args error")
        file_list = []
        
        for i in range(len(argv) / 2):
            arg_pare = {}
            arg_pare["file"] = argv[i * 2]
            arg_pare["args"] = argv[i * 2 + 1]
            file_list.append(arg_pare)
        
        return self.__pyweb_sut_run("custom_send_idna", (method, url, json.dumps(file_list), token))
    def download_dna(self, method, url, file_name, header):
        func_name = inspect.stack()[0][3]
        logger.info("call %s: args %s" % (func_name, str(list((method, url, file_name, header)))))
        return self.__pyweb_sut_run("download_dna", (method, url, file_name, header))        

    def parse_meta_attribute_from_db(self, data, sql):
        meta_attr_list = sql.split(' ')[1].split(',')
        d = {}
        for i in meta_attr_list:
            d[i] = data[0][meta_attr_list.index(i)]
        return d


    def update_data(self,old_info,update_info_list):
        old_info = eval(old_info)
        for i in update_info_list:
            i = eval(i)
            key = i.keys()[0]
            if old_info.has_key(key):
                old_info.update(i)
        return str(old_info).replace("'",'"')

    def get_customer_ref_id(self):
        return str(uuid1())

    def ingest_vddb_testdata_vdna_ingest(self, host, username, password, dna_file):
        #media_file = CI_SCRIPT_ROOT + "/" + media_file
        #vdna_ingest -s192.168.1.14 -uzhang_jin -w123 -TDNA -i tt.dna
        cmd = ["vdna_ingest", "-s%s" % host, "-u%s" % username, "-w%s" % password, "-TDNA -i", dna_file]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def vdna_query(self, cmd, *args, **kwargs):
        ''' host, username, password, dna_file'''
        keys_list = kwargs.keys()
        args_list = ['host', 'username', 'password', 'dna_file']
        in_list = list(set(args_list).intersection(set(keys_list)))
        if sorted(args_list) != sorted(in_list):
            raise AssertionError('%s args error: %s' % (cmd, in_list))
        cmd = ["%s" % cmd, "-u%s" % kwargs['username'], "-w%s" % kwargs['password'],
               "-s%s" % kwargs['host'], "-TDNA", "-i %s" % kwargs['dna_file']]
        for a in args:
            cmd.append(a)
        difference_list = list(set(keys_list).difference(set(args_list)))
        if difference_list:
            for a in difference_list:
                cmd.append(str(a) + '=' + kwargs[a])
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    

if __name__ == "__main__":
    pass
    pyweb = VddbLib()
    pyweb.convert_to_dict({'1':1})
    #pyweb.set_pyweb_sut_file("/home/yan_jiawei/workspace/automation/APOLLO/TVSYNC/trunk/common_op/sut/vddb/pyweb.py")
    #pyweb.set_pyweb_host("192.168.1.19", "88",'http')
    #ret = pyweb.pyweb_api_call("POST", "/mediawise/auth", '{"protocols": ["5.2.6"], "user": "zhang_jin", "password": "123"}')
    #print ret
