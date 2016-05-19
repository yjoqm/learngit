#!/usr/bin/env python
# coding=utf-8
#*args会返回元组形式，**args 返回字典，可以传默认参数
def fun_var_args(farg,*args):
    print "arg:",farg
    print "args is:", args 
    for value in args:
        print "another args:", value



def fun_var_args2(farg,**args):
    print "arg is:", farg
    print "**args is:", args
    for key in args:
        print "key is %s and it's value is %s" %(key,args[key])

if __name__=='__main__':
    fun_var_args(1,"two","3the","adf")
    fun_var_args2(2,a=3,c=4)



def foo(positional_arg, keyword_arg = "default", *tuple_arg):
    print "positinal arg:" ,positional_arg
    print "keyword_arg:" , keyword_arg
    for each in tuple_arg:
        print each



def test(positional_arg, keyword_arg='default', **dict_arg ):
    print "positional arg: ", positional_arg
    print "keyword_arg: ", keyword_arg
    for each_dict_arg in dict_arg.keys():
        print "dict_arg: %s=>%s" % ( each_dict_arg, str( dict_arg[each_dict_arg] ) )


if __name__ == "__main__":
    print foo('test1','a','b')

