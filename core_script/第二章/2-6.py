#!/usr/bin/env python
# coding=utf-8
#判断一个数是正数还是负数,或者是0
num = int(raw_input("please input a number:"))

if num > 0:
    print "the number is > 0."
elif num < 0:
    print "the number is < 0."
else:
    print "num = 0."
