#!/usr/bin/env python
# coding=utf-8
#计算单词的个数
f = open('/home/ellen/111.txt')
word_number = len([word for line in f for word in line.split()])

print word_number
#计算文件大小
import os
os.stat('111.txt').st_size


