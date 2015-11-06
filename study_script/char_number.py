#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
xml_name = raw_input("input xml name: ").strip()
char_name = raw_input("input char name: ").strip()
fobj = open(xml_name).read()

for char in set(re.findall(char_name, fobj)):
    test=len(re.findall(char,fobj))/2
    print "material number is %s" % test
