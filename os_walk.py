#!/usr/bin/env python
# coding=utf-8
#delete some Specified files with path
import os

def del_files(path):
    for root, dirs, files in os.walk(path):
        print "root",root,
        print "dirs",dirs,
        print "files", files
        for name in files:
            if name.endswith(".CR2"):
                print ("delete file: " + os.path.join(root, name))


if __name__=="__main__":
    path = '/home/ellen/yjoqm/'
    del_files(path)

