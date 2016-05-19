#!/usr/bin/env python
# coding=utf-8
import subprocess
import sys
import socket
import os
import paramiko

def here(script_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),script_name))

def ssh_clinet(hostname,cmd):
    username = 'ellen'
    password = 'ellen123'
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname=hostname, username=username,password=password)
    stdin,stdout,stderr=s.exec_command(cmd)
    print stdout.read()
    s.close()

#使用进程方法监控
def monitor_process(ip,key_word,cmd):
    p1 = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE) #subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)
    p2 = subprocess.Popen(['grep',key_word],stdin=p1.stdout,stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['grep', '-v', 'grep'], stdin=p2.stdout, stdout=subprocess.PIPE) #利用管道的方法操作
    lines = p3.stdout.readlines()
    if len(lines) > 0:
        return 'process is running.' 
    sys.stderr.write('process[%s] is lost, run [%s]\n' % (key_word, cmd))
    subprocess.call(cmd, shell=True)
#使用端口号监控方法

def monitor_port(protocol, port,cmd):
    address = ('127.0.0.1',port)
    socket_type = socket.SOCK_STREAM if protocol == 'tcp ' else socket.SOCK_DGRAM
    client = socket.socket(socket.AF_INET,socket_type)

    try:
        client.bind(address) 
    except Exception,e:
        print e 
    else:
        sys.stderr.write('port[%s-%s] is lost, run [%s]\n' % (protocol, port, cmd))
        subprocess.call(cmd, shell=True)
    finally:
        client.close()   

#---------------------------------------------------------------------------
def test():
    #cmd = '%s start' % here('gun.sh')
    #monitor_port('tcp',8635, cmd)
    #ssh_clinet('61.147.182.140')
    test = monitor_process('61.147.182.140','rtmerchant','ps aux |grep rtmerchant')
    print test
    
def main():
    test()

if __name__ == '__main__':
    #test = monitor_process('rtmerchant','ps aux |grep merchant')
    #test = monitor_port('tcp',9092,'ps aux |grep merchant')
    #print test
    main()
