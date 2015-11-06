#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append('../gen-py')

from tutorial import Calculator
from tutorial.ttypes import *

from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class CalculatorHandler:
    def __init__(self):
        self.log = {}
    def ping():
        print 'ping()'
    def add(self,n1,n2):
        print  'add(%d, %d)' %(n1, n2)
        return n1 +n2
    def calculate(self,logid,work):
        print 'Calculator(%d,%r)' % (logid,work)
        if work.op == operator.ADD:
            va1 = work.num1 + work.num2
        elif work.op == operator.SUTRACT:
            va2 = work.num1 - work.num2
        elif work.op == operator.MULTIPLY:
            va3 = work.num1 * work.num2
        elif work.op == operator.DIVIDE:
            if work.num2 == 0:
                x = InvalidOperation()
                x.what = work.op
                x.why = 'cannot divide by 0'
                raise x
            val = work.num1/work.num2
        else:
            x = InvalidOperation()
            x.what = work.op
            x.why = 'Invalid Operation'
            raise x
    

        log = SharedStruct()
        log.key = logid
        log.value = '%d' % (val)
        self.log[logid] = log

        return val

    def getStruct(self, key):
        print 'getStruct(%d)' % (key)
        return self.log[key]

    def zid(self):
        print 'zip()'

handler = CalculatorHandler()
processor = Calculator.Processor(handler)
transport = TSocket.TServerSocket(9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print 'Starting the server...'
server.serve()
print 'done.'
