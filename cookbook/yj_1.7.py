#!/usr/bin/python3.4
# coding=utf-8

#控制字典顺序，可以使用collections中的OrderDict，它可以保待操作时插入的顺序 

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] =2
d['spam']=3
d['grok']=4

for key in d:
    print(key,d[key])

#比如想控制Json编码后字段的顺序，可以使用OrderedDict来构建这样的数据

import json
print(json.dumps(d))

#{"foo": 1, "bar": 2, "spam": 3, "grok": 4}

