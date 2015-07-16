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

#skip header 
def skip_header(r):
    line = r.readline()
    while line.startswith('#'):
        line = r.readline()
    return line
#process file 
def process_file(r):
    line = skip_header(r).strip()
    print line
    for line in r:
        line = line.strip()
        print line


if __name__ == '__main__':
    main()
    input_file = open(sys.argv[1], 'r')
    process_file(input_file)
    input_file.close()





