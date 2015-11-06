#!/usr/bin/env python
# coding=utf-8
import logging
import os 
import commands
import signal

def getPid(process):
    cmd = "ps aux |grep '%s' " % process
    logging.info(cmd)
    info = commands.getoutput(cmd)
    infos = info.split()
    if len(infos) > 1:
        return infos[1]
    else:
        return -1 

if __name__ == '__main__':
  test = getPid('Server.py')
  print test
  os.kill(int(test),signal.SIGTERM)
