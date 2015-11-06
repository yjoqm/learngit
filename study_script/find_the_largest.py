#!/usr/bin/env python
# coding=utf-8
import sys

def find_largest(file):
    fi = open(file,"r")
    for line in fi:
        line = line.split()
        print line
        #fi.close()
        #line = fi.readline()
    largest = -1
    for value in line.split():
         v = int(value[:-1])
         if v > largest:
             largest = v
    return largest

if __name__=='__main__':
    file = '/home/ellen/learngit/aaa.txt'
    test = find_largest(file)
    print test

    


