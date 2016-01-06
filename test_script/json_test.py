#!/usr/bin/env python
# coding=utf-8
import json

#读取文件
d2 = json.load(open('/Users/admin/json2.txt'))
#print d2


#以下可以拿出来json中的key ,value,可以通过target_key配置
target_key ='nihao'
def walk_find(k,v):
    if k == target_key:
        return v
    if isinstance(v,dict):
        for i, j in v.iteritems():
            res = walk_find(i,j)
            if res is not None:
                return res 
    if isinstance(v,(tuple, list)):
        for i in v:
            res = walk_find('',i)
            if res is not None:
                return res
    return None



#判断json中是否存在某个key ,value 
import json
src_str = '{"a":{"b":[{"c":"C"},{"d":"D"},{"e":"E"}]}}'
jdict = json.loads(src_str)
class FoundException(Exception): pass
global flag
flag =False
def check_key_value(jdict,key,value):
	global flag
	#import pdb;pdb.set_trace()
	if isinstance(jdict, list):
		for element in jdict:
			check_key_value(element,key,value)
	elif isinstance(jdict, dict):
		if key in jdict.keys():
			if jdict[key] == value:
				try:
					raise FoundException
				except FoundException, e:
					flag = True
			else:
				return False
		else:
			for x in jdict.keys():
				check_key_value(jdict[x],key,value)

if __name__ == "__main__":
   # arr1 = walk_find('',d2)
   # print 'arr1:',arr1
   check_key_value(jdict,"d","D")
   print flag
