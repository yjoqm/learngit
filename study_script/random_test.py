#!/usr/bin/env python
# coding=utf-8
#随机产生一个８位数字,每位数字都是可以是1-6中的任意一个整数a
import random
result=[]
for i in range(8):
    result.append(str(random.randint(1,6)))
print ''.join(result)

#!/usr/bin/env python
# coding=utf-8
import random

for i in range(5):
    #random float
    print random.random(),
    #print integer
    print random.randint(100,1000),
    print random.randrange(100,1000,2),
#用 random 模块从序列取出随机项
for i in range(5):
    print i,
    print random.choice([1,2,4,5,6,7,9,1])

