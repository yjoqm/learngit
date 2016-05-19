#!/usr/bin/env python
# coding=utf-8
#delete some Specified files with path
import os

def del_files(path):
    for root, dirs, files in os.walk(path):
        print "root",root,
        print "dirs",dirs,
        print "files", files
        for name in files:
            if name.endswith(".CR2"):
                print ("delete file: " + os.path.join(root, name))


if __name__=="__main__":
    path = '/home/ellen/yjoqm/' 
    del_files(path)


import os.path
rootdir = "/home/ellen/yjoqm/"
# os.walk 返回一个三元组，其中parent表示所在目录, dirnames是所有目录名字的列表, filenames是所有文件名字的列表
for parent,dirnames,filenames in os.walk(rootdir):
    # 所在目录
    print("parent is:" + parent)
    # 遍历此目录下的所有目录(不包含子目录)
    for dirname in dirnames:
       print(" dirname is:" + dirname)
    # 遍历此目录下的所有文件
    for filename in filenames:
       print(" filename with full path:" + os.path.join(parent, filename))

# 列表显示出某目录下的所有文件及目录(不包括子目录的内容)
ls = os.listdir(rootdir)


spath = '/home/ellen/yjoqm/curl.py'
p,f = os.path.split(spath)
print('dir is:' + p)
print('file is:' + f)
#分隔文件名与扩展名
f,ext = os.path.splitext(spath)
print "f is:" +f
print "ext is:" +ext
