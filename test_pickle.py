#!/usr/bin/env python
# coding=utf-8
import cPickle as p
import os


shoplistfile = 'shoplist.data' #将会把资料保存在这个文件里面
shoplist = ['apple','mango','carrot',2,4] #需要保存的资料

#写入文件
f = open(shoplistfile,'wb') #以二进制写入
p.dump(shoplistfile,f)
f.close()

#取出资料
f = open(shoplistfile,"rb")
storedlist2 = p.load(f)
#print(storedlist2)
with open(storedlist2) as y:
    print y.readlines()
f.close()
os.remove(shoplistfile)
