#!/usr/bin/env python
# coding=utf-8
import os
import tempfile

temp = tempfile.TemporaryFile()
try:
    temp.write('some data')
    temp.writelines(['fist\n','second\n'])
    temp.seek(0)
    print temp.read()
    for line in temp:
        print line.rstrip()
finally:
    temp.close()

        
directory_name = tempfile.mkdtemp()
print directory_name

os.removedirs(directory_name) #创建临时目录需手动删除

#控制临时文件名
temp = tempfile.NamedTemporaryFile(suffix='_suffix',prefix ='prefix_',dir = '/tmp')
try:
    print 'temp:', temp
    print 'temp name :', temp.name
finally:
    temp.close()

'''
some datafist
second

/tmp/tmpm1ooJ2
temp: <open file '<fdopen>', mode 'w+b' at 0xb72cae38>
temp name : /tmp/prefix_Tye_YM_suffix
ellen@T430:~/learngit$ fg
vim tempfile_test.py

'''


