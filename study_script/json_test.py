#!/usr/bin/env python
# coding=utf-8
import json
data = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": True}, {"age": 29, "name": "Joe", "lactose_intolerant": False}]}
print json.dumps(data, indent=4)


#字符串转成json
json_input = '{"one": 1, "two": { "list": [ {"item":"A"},{"item":"B"}  ]  }}'
try:
    decoded = json.loads(json_input)
    print type(decoded)
    print json.dumps(decoded, sort_keys=True, indent=2)
    print "Json parsing ecample: ", decoded['one']
    print "complex json parsing example: ",decoded['two']['list'][1]['item'] 

except (ValueError, KeyError, TypeError):
    print "json format error "

