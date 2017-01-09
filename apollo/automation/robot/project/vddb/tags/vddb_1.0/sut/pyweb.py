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

def sort_func(val1, val2):
    tmp1 = int(val1.split('.')[-2].split("_")[-1])
    tmp2 = int(val2.split('.')[-2].split("_")[-1])
    
    if tmp1 == tmp2:
        return 0
    if tmp1 < tmp2:
        return -1
    if tmp1 > tmp2:
        return 1
    
def get_file_list (idna_dir, extra):
    idna_list = []
    
    tmp_list = os.listdir (idna_dir)
    #print tmp_list
    tmp_list2 = []
    for item in tmp_list:
        if extra != "":
            if os.path.splitext (item)[1] == extra:
                tmp_list2.append (item)
        else:
            tmp_list2.append (item)
    
    tmp_list2.sort (sort_func)
    
    for item in tmp_list2:
        idna_path = os.path.join (idna_dir, item)
        idna_list.append (idna_path)

    return idna_list

class PywebSut:
    def __init__(self, args):
        self.test_module = args[0]
        self.args = []
        for arg in args[1:]:
            self.args.append(arg)
    
    def pyweb_api_call(self, params):
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
    
    def dna_ingest(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        dna_file = urllib.unquote_plus(params[5])
        token = urllib.unquote_plus(params[6])
    
        try:
            dna_fp = file(dna_file)
        except IOError, ex:
            return "No such file or directory: '%s'" % dna_file
        
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
            
        header = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': token}
        request = dna_fp.read()
        if len(request) != 0:
            conn.request(method, url, request, header)
            response = conn.getresponse()
            body = response.read()
            header = response.getheaders()
            return_msg = {}
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
        
        conn.close()
        dna_fp.close()
        return json.dumps(return_msg)        
        
        
        
        
        

    def send_dna(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        dna_file = urllib.unquote_plus(params[5])
        dna_type = urllib.unquote_plus(params[6])
        token = urllib.unquote_plus(params[7])
        
        try:
            dna_fp = file(dna_file)
        except IOError, ex:
            return "No such file or directory: '%s'" % dna_file
        
        first_segment = True
        serial_no = 1
        
        if dna_type == "video":
            d_type = 0
        elif dna_type == "audio":
            d_type = 1
        
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
        
        return_msg = {}
        while True:
            if first_segment:
                read_size = 25 * 40 + 48
                first_segment = False
            else:
                read_size = 25 * 40
                
            dna_data = dna_fp.read(read_size)
            dna_data_size = len(dna_data)
            
            if 0 != dna_data_size:
                request = '%s\r\n%s\r\n%s\r\n%s\r\n' % (d_type, dna_type, dna_data_size, dna_data)
                request_header = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': token}                              
                conn.request(method, "%s/%s" % (url, serial_no), request, request_header)
                serial_no += 1
                response = conn.getresponse()
                body = response.read()
                header = response.getheaders()
                
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
                #time.sleep (1)
            else:
                break
                
        conn.close()
        dna_fp.close()
        return json.dumps(return_msg)
    
    def send_idna(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        dna_file = urllib.unquote_plus(params[5])
        dna_type = urllib.unquote_plus(params[6])
        file_type = urllib.unquote_plus(params[7])
        token = urllib.unquote_plus(params[8])
        if dna_type == "frame":
            extra = ".idna"
        elif dna_type == "screenshot":
            extra = ".jpg"
        if file_type == "folder":
            dna_list = get_file_list(dna_file, extra)
        elif file_type == "file":
            dna_list = [dna_file]
            
        
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
        
        serial_no = 1
        return_msg = {}
        for send_data in dna_list:
            data_fp = open(send_data, "rb")
            dna_data = data_fp.read()
            dna_size = len(dna_data)
            if 0 != dna_size:
                request = '%s\r\n%s\r\n%s\r\n%s\r\n' % (0, dna_type, dna_size, dna_data)
                request_header = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': token}                
                conn.request(method, "%s/%s" % (url, serial_no), request, request_header)
                serial_no += 1
                response = conn.getresponse()
                body = response.read()
                header = response.getheaders()
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
                data_fp.close()
                #time.sleep (1)
            else:
                data_fp.close()
        
        conn.close()
        return json.dumps(return_msg)
    
    def custom_send_idna(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        file_list = urllib.unquote_plus(params[5])
        token = urllib.unquote_plus(params[6])
        
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
            
        request_body = ""
        return_msg = {}
        file_list = json.loads(file_list)
        for file_arg in file_list:
            send_file = file_arg.get("file")
            send_args = str(file_arg.get("args"))
            try:
                fp = open(send_file, "rb")
            except IOError, ex:
                return "No such file or directory: '%s'" % send_file
            
            send_data = fp.read()
            send_len = len(send_data)
            fp.close()
            
            if send_len != 0:
                if request_body != "":
                    request_body += "\r\n"
                request_body += '%s\r\n%s\r\n%s\r\n%s\r\n' % (0, send_args, str(send_len), send_data)
        
        if request_body != "":
            request_header = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': token}                
            conn.request(method, url, request_body, request_header)
            response = conn.getresponse()
            body = response.read()
            header = response.getheaders()
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
        
        conn.close()
        return json.dumps(return_msg)            
            
            
    
    def download_dna(self, params):
        host = params[0]
        port = params[1]
        ssl = params[2]
        method = params[3]
        url = params[4]
        file_name = urllib.unquote_plus(params[5])
        request_header = urllib.unquote_plus(params[6])
            
        if ssl == 'https':
            conn = httplib.HTTPSConnection(host, port)
        else:
            conn = httplib.HTTPConnection(host, port)
        
        #request_header = { 'Content-type' : 'application/x-www-form-urlencoded', 'Cookie' : token }
        return_msg = {}
        conn.request(method, url, None, json.loads(request_header))
        response = conn.getresponse()
        body = response.read()
        try:
            fp = open(file_name, "wb")
            body_msg = "download file is %s" % file_name
            fp.write(body)
        except Exception, ex:
            body_msg = str(ex)
        finally:
            fp.close()
        
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
        return_msg["body"] = body_msg
        return_msg["header"] = ret_header
                
        return json.dumps(return_msg)        

    def run(self):
        function = getattr(self, self.test_module)
        fun_return = function(self.args)
        return fun_return
        
if __name__ == "__main__":
    sut = PywebSut(sys.argv[1:])
    print sut.run()
        