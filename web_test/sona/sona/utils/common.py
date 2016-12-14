#!/usr/bin/env python
# coding=utf-8
import base64
from hashlib import md5
import os

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

def get_md5(string):
    return md5(string).hexdigest()

