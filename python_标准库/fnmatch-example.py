#!/usr/bin/env python
# coding=utf-8
#使用fnmatch模块匹配文件
import fnmatch
import os

for file in os.listdir("backup"):
    if fnmatch.fnmatch(file, "*.py"):
        print file


