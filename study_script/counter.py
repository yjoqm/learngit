#!/usr/bin/env python
# coding=utf-8
#使用dict排序

some_data = ['a','2',2,4,5,'2','b',4,7,'a',5,'d','a','z']
count_frq = dict()

for item in some_data:
    if item in count_frq:
        count_frq[item] += 1
    else:
        count_frq[item] = 1
print count_frq


#使用defaultdict 

from collections import defaultdict

count_frq = defaultdict(int)
for item in some_data:
    count_frq[item] += 1

print count_frq

#使用collections.Counter 

from collections import Counter
some_data = ['a','2',2,4,5,'2','b',4,7,'a',5,'d','a','z']
print Counter(some_data)
#Counter({'a': 3, 4: 2, 5: 2, '2': 2, 2: 1, 'b': 1, 7: 1, 'z': 1, 'd': 1})


#可以使用elements()方法获取Counter中的key值
print list(Counter(some_data).elements())
#['a', 'a', 'a', 2, 'b', 4, 4, 5, 5, 7, '2', '2', 'z', 'd']
#利用most_common() 可以使用找出前N个出现频次最高的无素以及它们对应的次数
print Counter(some_data).most_common(2)
#[('a', 3), (4, 2)]
#当访问不存在的元素时，默认返回为0而不是抛出异常
print (Counter(some_data))['y']
#print 0

