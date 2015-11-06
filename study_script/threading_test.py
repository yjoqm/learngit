#!/usr/bin/env python
# coding=utf-8
#一个售票系统
import threading
import time,os

def  doChore():
    time.sleep(1)


lock = threading.Lock()
def booth(tid):
    global i 
    while True:
        lock.acquire()
        if i != 0:
            i -= 1
            print (tid,'now left:',i)
            doChore()
        else:
            print ("Thread_id",tid,"no more tickets")
            os._exit(0)
        lock.release()
        doChore()

i = 100

for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))
    new_thread.start()

def main():
    pass

if __name__ == '__main__':
    main()




