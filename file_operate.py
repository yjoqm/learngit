#/usr/bin/env  python
#encoding = utf-8
#给出一个xml文件,目标拿出里面每个素材中的<Id> 等,如正则中所要求的
#使用判断开始是否以<Id>开始,如是则把结果写入result文件
f = open('/home/ellen/test1111.xml','r')
result = open('/home/ellen/result.txt','w')
for line in f.readlines():
    line = line.strip()
    if line.startswith('<Id>') or line.startswith('<Price>'):
        result.writelines(line)
result.close()       
f.close()

#第二种,使用正则,查看是否符合正则,如果符合则写入到result 

import re

f = open('/home/ellen/337_hotel.xml','r')
result = open('/home/ellen/result.txt','w')
regex = re.compile(r'<Id>.*Id>|<Bucket.*Bucket>')
for line in f.readlines():
    result_test = regex.findall(line)
    sample_list = [line + '\n' for line in result_test] #add 换行
    result.writelines(sample_list)
result.close()
f.close()
