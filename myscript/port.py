#!/usr/bin/env python
# coding=utf-8
import os

#path = '/usr/local'
#查找以conf结尾的文件
def find_conf():
    filename = []
    path = '/usr/local/'
    for root,dirs,files in os.walk(path):
       # print "files",files
	for name in files:
            if name.endswith(".conf"):
                file = os.path.join(root,name)
                filename.append(file)
    return filename

 
def find_port(filename):
    port_list = []
    with open(filename,'r') as f:
        for line in f:
            if ":" in line:
                p = line.strip().split(":")
                if p[-1].isdigit():
                    if p[-1] not in port_list:
                        port_list.append(p[-1])
    return port_list



if __name__ == '__main__':
    test = find_conf()
  #  print test
    for x in test:
       y =  find_port(x)
       print "filename is %s and port is %s" % (x, y)

