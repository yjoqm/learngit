#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素
#此脚本的目的是验证xml中有多少个素材
import re
xml_name = raw_input("input xml name: ").strip()
char_name = raw_input("input char name: ").strip()
fobj = open(xml_name).read()

for char in set(re.findall(char_name, fobj)):
    num=len(re.findall(char,fobj))/2
    print "material number is %s" % num 
