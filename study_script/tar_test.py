#!/usr/bin/env python
# coding=utf-8
import os
import tarfile

tar = tarfile.open('/tmp/tartest.tar.gz','w:gz') #创建压缩包名

for path, dir, files in os.walk('/tmp/test'):
    for file in files:
        fullpath = os.path.join(path,file)
        tar.add(fullpath)  #创建压缩包
tar.close()


#解压缩
tar = tarfile.open('/tmp/tartest.tar.gz')
names = tar.getnames()
for name in names:
    print name
    tar.extract(name,path = './') #解压指定文件
tar.close()

