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
'''
struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。其函数原型为：struct.pack(fmt, v1, v2, ...)，参数fmt是格式字符串，关于格式字符串的相关信息在下面有所介绍。v1, v2, ...表示要转换的python值。下面的例子将两个整数转换为字符串（字节流）:
'''
str = struct.pack('ii',20,400)
print 'str:',str
print 'len(str):',len(str)

a =20
b = 400
str = struct.pack('ii',a,b)#格式符"i"表示转换为int，'ii'表示有两个int变量
print 'str:',str #打印乱码
print 'len(str):',len(str) #length:8,进行转换后的结果长度为8个字节（int类型占用4个字节，两个int为8个字节）
print repr(str)



#struct.unpack() 用于将字节流转换成python数据类型，struct.unpack(fmt,string),返回一个元组
str2 = struct.unpack('ii',str)
print 'length:', len(str)
print str2
print repr(str2)

