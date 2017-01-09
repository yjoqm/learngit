#!/usr/bin/env python
# coding=utf-8
valid = False
count = 3

passlist = ['ad','de']
while True:
    input = raw_input('enter: ')
    for eachpws in passlist:
        if input == eachpws:
            valid = True
            break
    if not valid:
        print 'invle input'
        count -= 1
        continue
    else:
        break

