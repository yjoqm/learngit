#!/usr/bin/env python
# coding=utf-8

print (['\t'.join("{}x{}={}".format(b,a,a*b) for b in range(1,a+1)) for a in range(1,10)])
#得到乘法口决
