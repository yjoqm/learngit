#!/usr/bin/env python
# coding=utf-8
import sys

def convert_n_bytes(n, b):
    bits = b*8
    return (n + 2**(bits-1)) % 2**bits - 2**(bits-1)

def convert_4_bytes(n):
    return convert_n_bytes(n, 4)

def getHashCode(s):
    h = 0
    n = len(s)
    for i, c in enumerate(s):
        h = h + ord(c)*31**(n-1-i)
    return convert_4_bytes(h)

if __name__ == '__main__':
    #print getHashCode('3f85fc7d59f742eab2f557a308f1fe19')
    print getHashCode(sys.argv[1])

