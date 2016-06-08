#!/usr/bin/env python
# coding=utf-8
#使用shutil复制文件
import shutil
import os

for file in os.listdir('.'):
    if os.path.splitext(file)[1] == '.py':
        print file
        shutil.copy(file,os.path.join("backup",file))



#利用shutil复制，删除目录树

SOURCE = 'backup'
BACKUP = 'backup-bak'

shutil.copytree(SOURCE,BACKUP) #如果BACKUP存在会报错，不存在时会自动创建目录
print  "backup file:", os.listdir(BACKUP)

shutil.rmtree(BACKUP) #删除目录树
print os.listdir(BACKUP)
