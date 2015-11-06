#!/usr/bin/env python
# coding=utf-8
numbers = [34,12,8,21,55]
for i in range(len(numbers)):
    print "i", i,
    for j in range(i):
        print "j:",j
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    print numbers
