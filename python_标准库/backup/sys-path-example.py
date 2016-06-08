#!/usr/bin/env python
# coding=utf-8

#使用sys.path 操作模块搜索路径.
import sys

print "path has", len(sys.path), "members"

sys.path.insert(0,'samples')
print sys.path

#查找已导入的模块
print sys.modules.keys()


#获取当前平台
if sys.platform == 'win32':
    import ntpath
    pathmodule = ntpath
elif sys.platform == 'mac':
    import macpath
    pathmodule=macpath
else:
    import posixpath
    pathmodule=posixpath

print pathmodule



