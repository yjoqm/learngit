#!/usr/bin/env python
# coding=utf-8
import os
for root,dirs,files in os.walk('/home/ellen/yjoqm/'):
    print root,
    print dirs,
    print files
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
print "basedir:",basedir
test = [x for x in os.listdir(basedir) if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print "test:",test
