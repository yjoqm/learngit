#!/usr/bin/env python
# coding=utf-8
import requests
import fileinput
import sys
import re
import json

#打开文件中符合要求的链接 
def open_url(file):
    for line in fileinput.input(file):
        r = re.compile(r'130.*jpg')
        test=re.findall(r,line)
        list_url = ''.join(test)
        t = requests.get('http://192.168.0.229:8001/merchant/' +list_url)
        #print(t.url)
        print t.text
        test = json.loads(t.text)
        print test
        

if __name__=='__main__':
    args = sys.argv
    test = open_url('/home/ellen/result.txt')
    print test
