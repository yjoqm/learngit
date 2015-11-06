#!/usr/bin/env python
# coding=utf-8

import time
from hashlib import md5
from random import randint

class Md5Helper():
    #md5 key generator helper

    @staticmethod
    def key_gen(ori_str)：
        #生成key,主要用于生成惟一的id
        return "%s" % (md5("%s_%s_%s" % (ori_str,time.time(), randint(1,10000))),hexdigest())

