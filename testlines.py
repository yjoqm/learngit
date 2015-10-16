#!/usr/bin/env python
# coding=utf-8
# this is simple script open a file and print out 100 lines of whatover is #set for the line variable
line = "Test you want to print\n"
f = open('/home/ellen/mc/test_api.py','rb')
result = list()
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'):
        continue
    result.append(line)
#result.sort()
print result

f.close()

open('/home/ellen/learngit/test.txt','w').write('%s' % '\n'.join(result))

