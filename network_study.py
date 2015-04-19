#!/usr/bin/env python
# coding=utf-8
#程序把客户端发送过来的字条串加上一个时间戳返回给客户端.
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM) #创建服务套接字,tcp
tcpSerSock.bind(ADDR) #把地址绑定到套接字
tcpSerSock.listen(5) #报务器开始监听连接,最多接受５个连接

#开始服务器端的无限循环
while True:
    print "waiting for connecting..."
    tcpCliSock, addr = tcpSerSock.accept() #接受客户端的连接
    print "...connected from ..:", addr

    while True:
        #开始通信
        data = tcpCliSock.resv(BUFSIZ) #开始对话,接收与发送
        if not data:
            break
        tcpCliSock.send('[%s] %s') %(ctime(),data)
        tcpCliSock.close() #关闭客户端
tcpSerSock.close() #关闭服务器,可选

#创建TCP客户端,会提示用户输入要传给服务器的信息,显示服务器返回的加了时间戳的结果
from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ=1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM) #创建套接字
tcpCliSock.connect(ADDR)　#尝试连接服务器

while True:
    data = raw_input('>')
    if not data:
        break   #如果用户没有任何输入,程序退出
    tcpCliSock.send(data)
    data = tcpCliSock.resv(BUFSIZ) 
    if not data:
        break  #如果服务由于某种原因退出,导致resv失败,则退出
    print data
tcpCliSock.close()














