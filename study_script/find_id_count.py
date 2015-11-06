#!/usr/bin/env python
# coding=utf-8
import re

li = []
with open("/home/ellen/ajk.txt","r") as f:
    for eachline in f:
        eachline = eachline.strip()
        id = re.findall('finish (\d+)',eachline)
        li.append(id[0])
    d = {k:li.count(k) for k in set(li)}
    print d
