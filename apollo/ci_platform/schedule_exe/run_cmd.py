#!/usr/bin/python
import sys
import os
import httplib
import time
import struct
from datetime import datetime
import subprocess
import shlex

class RunCmd():
    def __init__(self, cmd, timeout = None):
        if timeout is None:
            self.timeout = 99999999999
        else:
            self.timeout = timeout
        self.cmd =cmd

    def run(self):
        #cmd = shlex.split(self.cmd)
        cmd = self.cmd.split(" ")
        self.start = time.time()
        self.process = subprocess.Popen(cmd, stderr = subprocess.PIPE, stdout = subprocess.PIPE)
        while True:
            return_code = self.process.poll()
            if return_code is None:
                if time.time() - self.start > self.timeout:
                    self.process.kill()
                    self.process.wait()
            else:
                if return_code != -9:
                    self.stdout = self.process.stdout.read()
                    self.stderr = self.process.stderr.read()
                break

        return return_code




def main():
    pass

if __name__ == '__main__':
    main ()
