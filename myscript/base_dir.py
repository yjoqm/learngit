#!/usr/bin/env python
# coding=utf-8
import os
base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
print base_dir
def files(path):
    for root,dirs,files in os.walk(path):
        #print "root",root
        print "dirs",dirs
        #print "files",files
        for name in files:
            if name.endswith(".py"):
#                print "files: " +os.path.join(root,name)


import os


