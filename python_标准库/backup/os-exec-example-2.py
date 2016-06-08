#!/usr/bin/env python
# coding=utf-8
import os
import sys

import os
import sys

def run(program, *args):
    pid = os.fork()
    print "pid", pid
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]

run("python", "hello.py")

