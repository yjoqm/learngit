#!/usr/bin/env python
# coding=utf-8
#来验证用户输入,有三次机会
valid = False
count = 3
passwdlist = ['ad','de']
while count > 0:
    input = raw_input("enter password")
    #check for valid passwd
    for eachpasswd in passwdlist:
        if input == eachpasswd:
            valid = True
            break
    if not valid:
        print "invaild input"
        count -= 1
        continue
    else:
        break

        
