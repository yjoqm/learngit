#!/usr/bin/env python
#encding=utf-8
def foo(positional_arg, keyword_arg = "default", *tuple_arg):
    print "positinal arg:" ,positional_arg
    print "keyword_arg:" , keyword_arg
    for each in tuple_arg:
        print each
foo(1,2,3,4,5)



def ( positional_arg, keyword_arg='default', **dict_arg ):
    print "positional arg: ", positional_arg
    print "keyword_arg: ", keyword_arg
    for each_dict_arg in dict_arg.keys():
        print "dict_arg: %s=>%s" % ( each_dict_arg, str( dict_arg[each_dict_arg] ) )
