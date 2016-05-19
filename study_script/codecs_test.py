#!/usr/bin/env python
# coding=utf-8
#Python:如何使用codecs模块将unicode数据保存成gbk格式

import codecs

def ReadFile(filePath, encoding):
    with codecs.open(filePath, "r", encoding=encoding) as f:
        return f.read()

def WriteFile(filePath, content, encoding):
    with codecs.open(filePath, "w", encoding=encoding) as f:
        f.write(content)

def UTF8_to_GBK(src, dst):
    content = ReadFile(src, encoding="utf-8")
    WriteFile(dst, content, "gbk")
