#!/usr/bin/env python
# coding=utf-8
import os
import yaml

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
yaml_dir = os.path.join(base_dir,'tmp','test')

platform_list = os.listdir(yaml_dir)
platform_list = [p.split('.')[0] for p in platform_list]
platform_list = [p for p in platform_list if p != '']

def get_input_info(yml_name):
    yml_path = os.path.join(yaml_dir, yml_name + '.yml')
    with open(yml_path,'rb') as f:
        var = f.read()
    yml_dict = yaml.load(var)
    return yml_dict




if __name__ == '__main__':
    print get_input_info('admob')


