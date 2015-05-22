#!/usr/bin/env python
# coding=utf-8
def fun_var_args(farg,*args):
    print "arg:",farg
    for value in args:
        print "anoter args:", value

fun_var_args(1,"two","3the","adf")


