#!/usr/bin/env python
# coding=utf-8
#traceback主要是追踪异常

#分母为0时调用系统退出

import sys
def division(a=1,b=1):
    if b == 0:
        print 'b eq 0'
        sys.exit(1)
    else:
        return a/b


#使用try except捕获异常，然后traceback.print_exc()打印
import traceback
a = 10
b = 0
try:
    print division(a,b)
except:
    print 'invoking division faild'
    traceback.print_exc()
    sys.exit(1)


if __name__ == "__main__":
    test1 = division(a=20,b=4)
    print test1

