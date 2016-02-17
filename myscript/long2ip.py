#!/usr/bin/env python
# coding=utf-8

import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

print socket.inet_ntoa(struct.pack('!L', 1453269278))
