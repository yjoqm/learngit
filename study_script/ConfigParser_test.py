#!/usr/bin/env python
# coding=utf-8
import ConfigParser

#read Config
cf = ConfigParser.ConfigParser()
cf.read("test.conf")
#return all section,type:list
secs = cf.sections()
print "all sections:",secs 

#-options(section) 得到该section的所有options
opts = cf.options('sec_a')
print 'sec_a opts:', opts
#-items(section) 得到该section的所有键值对
kvs = cf.items('sec_a')
print "items sec_a:", kvs

#-get(section,option) 得到section中option的值，返回为string类型
str_val = cf.get('sec_a', 'a_key1')
int_val = cf.getint('sec_a','a_key2')
print "value for sec_a a_key1:", str_val
print "value for sec_a a_key2:", int_val

#-add_section(section) 添加一个新的section
#-set( section, option, value ) 对section中的option进行设置，需要调用write将内容写入配置文件
#
#update value 
cf.set('sec_b','b_key3','new-$r')
#set a new value
cf.set("sec_b", "b_newkey", "new-value")
#create a new section 
cf.add_section('a_new_section') 
cf.set('a_new_section', 'new_key', 'new_value') 

#write back to configure file
cf.write(open('test.conf','w'))



