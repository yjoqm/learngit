# -*- coding: utf-8 -*-
import os
import sys
from robot.api import *
import json
from ctypes import *
import win32api
user_module_path = os.path.dirname(os.path.realpath(__file__))
from robot.api import logger
import time

def vcri_result_notify_t(overview, results, result_count, url, file_private_id):
    fp = open("c:/vcri_result_notify_callback.txt", "w")
    fp.write("overview: %s\n" % overview)
    try:
        fp.write("results: %s\n" % results.contents.path)
        fp.write("results: %s\n" % results.contents.result)
    except ValueError,ex:
        fp.write("results: 0x00000000\n")
    fp.write("result_count: %s\n" % result_count)
    fp.write("url: %s\n" % url)
    fp.write("file_private_id: %s\n" % file_private_id)
    fp.close()

class ThunderLib:
    def __init__(self):
        pass
    
    def load_dll(self, dll_name):
        if os.path.exists(dll_name):
            try:
                self.dll_handle = CDLL(dll_name)
            except Exception,ex:
                logger.warn(ex)
                open("c:/txt.txt","w").write(str(ex))
                raise AssertionError(ex)
        else:
            raise AssertionError("DLL file %s does not exist" % dll_name)
        
    def dll_api_call(self, func_name, *argv):
        #logger.warn(argv)
        if func_name in ["vcri_set_api_key", "vcri_set_program_info", "vcri_set_client_id"]:
            function = getattr(self, "_set_function")
            return function(func_name, *argv)
        else:
            function = getattr(self, "_%s" % func_name)
            return function(*argv)
        
    def _set_function(self, func_name, *argv):
        set_function = getattr(self.dll_handle, func_name)
        set_function.argtypes = [POINTER(c_char)]
        set_function.restype = c_int32
        res = set_function(argv[0])
        return res
    
    def _vcri_init(self, *argv):
        function = self.dll_handle.vcri_init
        function.argtypes = [c_int, POINTER(VcriProxyT)]
        function.restype = c_int32
        proxy_type = int(argv[0])
        if argv[1] != None:
            proxy_info = json.loads(argv[1])
            #logger.warn(proxy_info)
            str_proxy = VcriProxyT()
            if proxy_info.get("port")==0:
	        str_proxy.port = None
            else:
	        str_proxy.host = proxy_info.get("port")
	    if proxy_info.get("host")=="":
	        str_proxy.host = None
	    else:
	        str_proxy.host = proxy_info.get("host")
	    if proxy_info.get("username")=="":
	        str_proxy.username = None
	    else:
	        str_proxy.username = proxy_info.get("username")
	    if proxy_info.get("password")=="":
	        str_proxy.password = None
	    else:
	        str_proxy.password = proxy_info.get("password")
            str_proxy = byref(str_proxy)
        else:
            str_proxy = None
        res = function(proxy_type, str_proxy)
        return res
    
    def _vcri_identify(self, *argv):
        function = self.dll_handle.vcri_identify
        #function.argtypes = [CFUNCTYPE(c_void_p, c_int32, c_char_p, c_char_p), POINTER(VcriParamsT)]
        function.argtypes = [c_void_p, POINTER(VcriParamsT)]
        function.restype = c_int32
        if argv[0] != None:
            callback_handle = argv[0]
        else:
            callback_handle = None
            
        if argv[1] != None:
            params_info = json.loads(argv[1])
            params = VcriParamsT()
            params.struct_size = params_info.get("struct_size")
            params.struct_version = params_info.get("struct_version")
            params.url = params_info.get("url")
            params.referer = params_info.get("referer")
            params.file_private_id = params_info.get("file_private_id")
            params.mime_type = params_info.get("mime_type")
            params.file_name = params_info.get("file_name")
            params.file_size = params_info.get("file_size")
        else:
            params = None
            
        res = function(callback_handle, params)
        return res
    
    def _vcri_cancel(self, *argv):
        function = self.dll_handle.vcri_cancel
        function.argtypes = [POINTER(VcriParamsT)]
        function.restype = c_int32
        if argv[0] != None:
            params_info = json.loads(argv[0])
            params = VcriParamsT()
            params.struct_size = params_info.get("struct_size")
            params.struct_version = params_info.get("struct_version")
            params.url = params_info.get("url")
            params.referer = params_info.get("referer")
            params.file_private_id = params_info.get("file_private_id")
            params.mime_type = params_info.get("mime_type")
            params.file_name = params_info.get("file_name")
            params.file_size = params_info.get("file_size")
        else:
            params = None
                    
        res = function(params)
        return res
    
    def _vcri_progress(self, *argv):
        function = self.dll_handle.vcri_progress
        function.argtypes = [POINTER(VcriParamsT), c_ubyte]
        function.restype = c_int32
        
        if argv[0] != None:
            params_info = json.loads(argv[0])
            params = VcriParamsT()
            params.struct_size = params_info.get("struct_size")
            params.struct_version = params_info.get("struct_version")
            params.url = params_info.get("url")
            params.referer = params_info.get("referer")
            params.file_private_id = params_info.get("file_private_id")
            params.mime_type = params_info.get("mime_type")
            params.file_name = params_info.get("file_name")
            params.file_size = params_info.get("file_size")
        else:
            params = None
            
        res = function(params, argv[1])
        return res
    
    def _vcri_fini(self, *argv):
        function = self.dll_handle.vcri_fini
        function.argtypes = []
        function.restype = c_void_p
        function()
            
    
    def get_callback_handle(self, func_name):
        if "vcri_result_notify_t" == func_name:
            return CFUNCTYPE(c_void_p, c_int32, POINTER(VcriResultT), c_uint32, c_char_p, c_char_p)(vcri_result_notify_t)
    
    def release_dll(self):
        win32api.FreeLibrary(self.dll_handle._handle)
        
        
        
class VcriProxyT(Structure):
    _fields_ = [('port', c_uint32),
                ('host', c_char_p),
                ('username', c_char_p),
                ('password', c_char_p)]
    
class VcriParamsT(Structure):
    _fields_ = [("struct_size", c_uint32),
                ("struct_version", c_uint32),
                ("url", c_char_p),
                ("referer", c_char_p),
                ("file_private_id", c_char_p),
                ("mime_type", c_char_p),
                ("file_name", c_char_p),
                ("file_size", c_uint64)]
    
class VcriResultT(Structure):
    _fields_ = [("path", c_char_p),
                ("result", c_uint32)]
        
        
        
if __name__ in ('main', '__main__'):
    os.chdir("D:/workspace/automation/robot/project/thunder/trunk/sut")
    dll = ThunderLib()
    dll.load_dll("vcri.dll")
    ret = dll.dll_api_call("vcri_init", 0, '{"port":80, "host":"192.168.10.10","username":"user","password":"pass"}')
    #ret = dll.dll_api_call("vcri_init", 0, None)
    ret = dll.dll_api_call("vcri_set_api_key", "this-is-TMP-apikey")
    ret = dll.dll_api_call("vcri_set_program_info", "client_info")
    ret = dll.dll_api_call("vcri_set_client_id", "client_id")
    callback_handle = dll.get_callback_handle("vcri_result_notify_t")
    sret = dll.dll_api_call("vcri_identify", callback_handle, '{"struct_size":40,"struct_version":1,"url":"www.testurl.com","referer":"referer_url","file_private_id":"private_id","mime_type":"video/mp4","file_name":"file_name","file_size":32432}')
    time.sleep(1)
    dll.dll_api_call("vcri_fini")
    print ret
    dll.release_dll()
