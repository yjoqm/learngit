#!/usr/bin/env python
# coding=utf-8
#使用三种方法替换hello world中hello ==> hi
#切片
test = 'hello world'
result = 'hi ' + test[6:]
print result

#re
import re
li = re.compile('hello')
res = re.sub(li,'hi',test)
print res

#替换
re3 = test.replace('hello','hi')
print re3

#shutils 实现copy把当前目录下的py=>backup_test
import shutil
import os

fi = [file for file in os.listdir('.') if os.path.splitext(file)[1] == '.py' ]

for i in fi:
    print i
dst = '/home/ellen/test_backup/'
shutil.copy(i, dst)
print os.listdir('/home/ellen/test_backup/')

#第二种
for file in os.listdir('.'):
    if os.path.splitext(file)[1] == '.py':
        shutil.copy(file,os.path.join('backup_test'),file)


#读取文件中100到200行
i = 0

file1 = open('test.txt','r')
file2 = open('out.txt','w')
while True:
    line = file1.readline()
    i += 1
    if i >=100 and i <= 200:
        file2.write(line)
    if i > 200:
        break
    if not line:
        break
file1.close()
file2.close()


































