#!/usr/bin/env python
# coding=utf-8
import time
import os
import thread
'''
def timer(no,interval):
    cnt=0
    while cnt<10:
        print "Tread:(%d) Time:%s\n"%(no,time.ctime())
        cnt += 1
    thread.exit_thread()

#线程的结束可以等等线程自然结束，也可以在线程函数中调用exit_thread()或者thread.exit()

def test():
    #start_new_thead创建两个线程
    #thread.start_new_thread(function, args[, kwargs]) 的第一个参数是线程函数；第二个参数是传递给线程函数的参数，它必须是tuple类型；kwargs是可选参数
    thread1 = thread.start_new_thread(timer,(1,1))
    thread2 = thread.start_new_thread(timer,(2,2))
    print 'start~~~\n'
    time.sleep(1) #如果不写这个会报错，因为主进程结束而子线程没结束
    print 'end'
if __name__ == '__main__':
    test()


#增加了子进程级别的并行开发支持--multiprocessing
from multiprocessing import current_process,Pool

def test(x):
    print current_process().pid, x
    time.sleep(1)

if __name__ == '__main__':
    print "main:", os.getpid()
    p =Pool(3)#Pool 不过是创建多个 Process，然后将数据(args)提交给多个子进程完成
    p.map(test,range(13))#启动13个子进程
    time.sleep(1)
'''

#使用Process
from multiprocessing import Process,current_process

def test2(x):
    print current_process().pid,x
    time.sleep(1)

if __name__=='__main__':
    print "main:",os.getpid()
    p = Process(target = test2, args = [100])
    p.start()
    p.join()
