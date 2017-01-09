#!/usr/bin/env python
# coding=utf-8

import os
import string

file = "/tmp/sample/sample.txt"

def replace(file, search_for, replace_with):
    back = os.path.splitext(file)[0] + '.bak'
    temp= os.path.splitext(file)[0] + '.tmp'
    print "back:",back
    print "temp:",temp

    try:
       os.remove(temp)
    except os.error:
        pass

    fi = open(file)
    fo = open(temp,'w')
    for s in fi.readlines():
        fo.write(string.replace(s,search_for,replace_with))
        fi.close()
        fo.close()






t = replace(file,'hello','yjoqm')
print t


