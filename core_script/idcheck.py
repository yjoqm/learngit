#!/usr/bin/env python
# coding=utf-8
#检查有效标识字符,python标识符是以字母或者下划线开头后跟字母,下划线或者数字
import string

begin = string.letters + '_'
nums = string.digits

myinput = raw_input("indentifief to test? ")
if len(myinput)>1:
    if myinput[0] not in begin:
        print "invalid: first must be alap"
    else:
         for otherchat  in myinput[1:]:
            if otherchat not in begin + nums:
                 print "faild"
                 break
         else:
            print "yes"
