#!/usr/bin/env python
# coding=utf-8
#remove duplicate value from list
def remove_duplicates(list):
    ret = []
    for item in list:
        if item not in ret:
            ret.append(item)
    return ret

li = [2,4,5,4,6]
test = remove_duplicates(li)
print test

