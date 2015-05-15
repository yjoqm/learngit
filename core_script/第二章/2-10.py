#!/usr/bin/env python
# coding=utf-8
input = int(raw_input("please input a numb in 0~100: "))

while input>100 or input<1:
    print "sorry, the number is not range(101)"
    input = int(raw_input("enter again:"))
print 'yes you are right.'


