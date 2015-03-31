#!/usr/bin/env python
# coding=utf-8
#check a file exits and that we can read the file
import sys
import os

def readfile(filename):
    f = open(filename,'r')
    line = f.read()
    print line

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-]' + filename + 'does not exits'
            exit(0)
        if not os.access(filename, os.R_OK):        #CHECK you can read the file
            print '[-]' + filename + 'access denied'
            exit(0)
    else:
        print '[-]Usage:' + str(sys.argv[0]) + 'filename'
        exit(0)
    readfile(filename)
    
if __name__ == '__main__':
    main()




