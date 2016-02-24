#!/usr/bin/env python
# coding=utf-8
def fun_var_args(farg,*args):
    print "arg:",farg
    for value in args:
        print "anoter args:", value


fun_var_args(1,"two","3the","adf")

def fun_var_args2(farg,**args):
    print "arg is:", farg
    for key in args:
        print "key is %s and it's value is %s" %(key,args[key])

if __name__=='__main__':
    fun_var_args2(2,a=3,c=4)
