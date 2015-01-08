#!/usr/bin/env python
#encoding:utf-8
import os 
import yaml
import json

dir_path = os.path.dirname(os.path.abspath(__file__))
dir_list = os.listdir(dir_path)


for f in dir_list:
    fs = f.split('.')
    if len(fs) == 2 and fs[1] == 'yml':
        with open('{}'.format(os.path.join(dir_path,f)),'rb') as fil:
            ori_ymlfile = fil.read()
            fin_ymlfile = yaml.load(ori_ymlfile)
            if f == 'xml.yml':
                for v in fin_ymlfile.itervalues():
                    for k1,v1 in v.iteritems():
                        if k1 == 'xml':
                            with open(os.path.join(dir_path,'files',v1),'rb') as ff:
                                var = ff.read()
                            v[k1] = var
            elif f == 'merchant.yml':
                for k,v in fin_ymlfile.iteritems():
                    if k.startswith('merchant_req'):
                        for k1,v1 in v.iteritems():
                            if k1 == 'merchant':
                                v[k1] = json.dumps(v1)

            globals().update(fin_ymlfile)




