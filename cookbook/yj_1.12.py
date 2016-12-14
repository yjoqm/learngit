#!/usr/bin/env python
# coding=utf-8
#统计序列中出现次数最多的元素

words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'

]

from collections import Counter

words = Counter(words)
print words
#Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "you're": 1, "don't": 1, 'under': 1, 'not': 1})
#统计序列中出现次数最多的元素
top = words.most_common(3)
print top
#[('eyes', 8), ('the', 5), ('look', 4)]
print top[1]
print top[1][0] #可以对结果进行切片操作

print words['eyes'] #一个 Counter 对象就是一个字典，将元素映射到它出现的次数上

