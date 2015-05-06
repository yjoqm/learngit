#!/usr/bin/env python
# coding=utf-8
import struct
import binascii

values = (1,'abc',2.7)
s = struct.Struct('i3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)

print "original values:", values
print "format string: ",s.format
print "Uses:",s.size,'bytes'
print "packed value", binascii.hexlify(packed_data)
print "unpacked_data:", type(unpacked_data),'values',unpacked_data

