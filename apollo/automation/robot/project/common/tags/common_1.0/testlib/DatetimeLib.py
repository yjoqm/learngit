import os
import sys
from robot.api import *
from run_cmd import RunCmd
import re
import copy
import time
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class DatetimeLib:
    def __init__(self):
        pass
        
    def strformat_to_second(self, format_time):
        second = 0
        try:
            format_list = format_time.split(":")
            if len(format_list) == 3:
                for i in range(len(format_list)):
                    if int(format_list[i]) in range(0, 60) or i == 0:
                        second += int(format_list[i]) * (3600 / (60 ** i))
                    else:
                        raise Exception("")
                return second
            else:
                raise Exception("")
        except Exception, ex:            
            raise AssertionError("%s: time format error !" % format_time)
        
    def date_to_str(self, date_time):
        if not date_time:
            return "0000-00-00"
        else:
            return date_time.strftime('%Y-%m-%d')
        
    def datetime_to_str(self, date_time): 
        if not date_time:
            return "0000-00-00"
        else:
            return date_time.strftime('%Y-%m-%d %H:%M:%S')        
    
                