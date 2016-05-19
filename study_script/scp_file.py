#!/usr/bin/env python
# coding=utf-8
import sys,os

dir = '/home/ellen/yjoqm/fdfs_client/pic'

def scp_file(filename):
    cmd = 'scp ellen@61.147.182.142:/home/ellen/yjoqm/fdfs_client/pic/%s .' %filename
    os.system(cmd)

def main(args):
    args = sys.argv[1]
    
    scp_file(args)
    print 'done~~~~'

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 1:
        print 'usage: python scp_file xxxx'
        sys.exit(2)
    main(args)
