#!/usr/bin/env python
# coding=utf-8
__metaclass__=type

#调用自身
class  test:
 def  sist(name_1):
    name_1=raw_input('是屌丝吗？')
    na=name_1.find('是')
    nb=name_1.find('不是')
    if  na==0 and nb==-1:
          print '真聪明！'
              
    elif na==-1 and nb==0:
          print '不对哦~'
          return  sist(name_1)
    else:
          return sist(name_1)

if __name__ == '__main__':
    c = test()
    print c.sist()
