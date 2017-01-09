import os
import sys
from robot.api import *
from run_cmd import RunCmd
import re
import copy
import time
import json
import copy
from uuid import uuid1
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class CommonLib:
    def __init__(self):
        pass

    def str_upper(self, string):
        return string.upper()

    def str_lower(self, string):
        return string.lower()

    def json_loads(self, string):
        return json.loads(string)

    def json_dumps(self, json_obj):
        return json.dumps(json_obj)

    def get_json_element(self, body, element_name):
        if type(body) is not dict:
            try:
                json_body = json.loads(body)
            except TypeError, ex:
                raise Exception(ex)
            except ValueError, ex:
                raise Exception("JSON format error")
        else:
            json_body = body

        elememt_tree = element_name.split(".")

        for element in elememt_tree:
            if json_body.has_key(element):
                json_body = json_body.get(element)
            else:
                raise Exception("has no element named %s" % element)

        return json_body

    def remote_run_cmd(self, host, port, cmd, stdout = "true", stderr = "false"):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        msg = {}
        recv = ''
        msg["RunCmd"] = cmd
        msg["stdout"] = stdout
        msg["stderr"] = stderr
        sock.send(json.dumps(msg))
        while True:
            t_recv = sock.recv(1448)
            if len(t_recv) < 1448:
                recv += t_recv
                break
            else:
                recv += t_recv
        sock.close()
        return recv

    def print_type(self, msg):
        logger.warn(str(type(msg)))

    def log_warn(self,string):
        logger.warn(string)

    def u8(self,s):
        return s.decode('utf-8')
    
    def deep_copy(self, src):
        dst = copy.deepcopy(src)
        return dst
    

    def cat_cmd(self,cmd):
        cmd = "cat " + CI_SCRIPT_ROOT + cmd
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def run_different_cmds(self, **kwargs):
        rlt = {}
        for k,v in kwargs.items():
            cmd = " ".join([k,v])
            process = RunCmd(cmd)
            return_code = process.run()
            r = process.stdout
            rlt.setdefault(k,r)
        return rlt

    def run_same_cmds(self, cmd, count, *cmdargs):
        rlt = {}
        for arg in cmdargs:
            t_r = []
            c = " ".join([cmd,str(arg)])
            for i in range(count):
                process = RunCmd(c)
                return_code = process.run()
                r = process.stdout
                t_r.append(r)
            rlt.setdefault(arg,t_r)
        return rlt

    def run_cmd(self,cmd):
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout

    def parse_data_from_db(self, data, sql):
        meta_attr_list = sql.split(' ')[1].split(',')
        d = {}
        for i in meta_attr_list:
            if type(data[0][meta_attr_list.index(i)]) not in [str,unicode]:
                t_d = str(data[0][meta_attr_list.index(i)])
            else:
                t_d = data[0][meta_attr_list.index(i)]
            d[i] = t_d
        return d


    def get_uuid(self):
        return str(uuid1())

    def convert_to_dict(self,string):
        if type(string) == dict:
            return string
        return eval(string)
    
    def get_sorted_file_list(self, file_dir, extra="", fun_name=""):
        file_list = []
                
        tmp_list = os.listdir(file_dir)
        tmp_list2 = []
        for item in tmp_list:
            if extra != "":
                if extra[0] != ".":
                    extra = "." + extra
                if os.path.splitext(item)[1] == extra:
                    tmp_list2.append(item)
            else:
                tmp_list2.append(item)
        if fun_name != "":
            function = getattr(self, fun_name)
            tmp_list2.sort(function)
        else:
            tmp_list2.sort()
        
        for item in tmp_list2:
            file_path = os.path.join(file_dir, item)
            file_list.append(file_path)
            
        return file_list
        
    def idna_sort_func(self, val1, val2):
        tmp1 = int(val1.split('.')[-2].split("_")[-1])
        tmp2 = int(val2.split('.')[-2].split("_")[-1])
                
        if tmp1 == tmp2:
            return 0
        if tmp1 < tmp2:
            return -1
        if tmp1 > tmp2:
            return 1

if __name__ == '__main__':
    c = CommonLib()
    flist = c.get_sorted_file_list('F:/workspace/automation/TVSYNC/trunk/data/frame/Joe_1m' ,"idna", "idna_sort_func")
    print flist