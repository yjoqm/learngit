#!/usr/bin/python
#encoding=utf-8
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import os
import socket
import threading
import json
from binascii import *
#add user libs
user_module_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert (0, user_module_path)
from run_cmd import RunCmd
import time


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(("", 9999))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        socket_process = RequireProcess(connection, address)
        socket_process.start()
        


class RequireProcess(threading.Thread):
    def __init__(self, conncetion, address):
        threading.Thread.__init__(self)
        self.connection = conncetion
        self.address = address
        
    def run(self):
        while True:
            try:
                self.connection.settimeout(600)
                buf = self.connection.recv(2048)
                try:
                    msg = json.loads(buf)
                    if msg.keys()[0] == "RunCmd":
                        cmd = unhexlify(msg["RunCmd"])
                        process = RunCmd(cmd)
                        process.run()                    
                        print process.cmd
                        #print process.stdout
                        #print process.stderr
                        return_msg = ""
                        if msg["stdout"] == "true":
                            return_msg += process.stdout
                        if return_msg != "" and return_msg[-1] != "\n":
                            return_msg += "\r\n"
                        if msg["stderr"] == "true":
                            return_msg += process.stderr
                            
                        print return_msg
                        msg = hexlify(return_msg)
                        while True:
                            send_msg = {}
                            if len(msg) <= 1024:
                                send_msg["is_finish"] = True
                                send_msg["msg"] = msg
                                self.connection.send(json.dumps(send_msg))
                                break
                            else:
                                send_msg["is_finish"] = False
                                send_msg["msg"] = msg[0:1024]
                                self.connection.send(json.dumps(send_msg))
                                time.sleep(0.02)
                                msg = msg[1024:]
                        
                    else:
                        self.connection.send("message: %s error" % json.dumps(msg))
                except TypeError, ex:
                    self.connection.send("%s TypeError: %s" % (msg, str(ex)))
                except ValueError, ex:
                    self.connection.send("JSON format error")
                except Exception, ex:
                    self.connection.send("%s message error: %s" % (msg, str(ex)))
            except socket.timeout:
                pass
            finally:
                self.connection.close()
                break

if __name__ in ('main', '__main__'):
    main()
