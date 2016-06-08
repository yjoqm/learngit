#!/usr/bin/env python
# coding=utf-8

#getroot()方法
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file ='six.xml')
root = tree.getroot()
print root #<Element 'productList' at 0x10207e8d0>
print root.tag #productList

#find(match), findall(match), findtex(match, default=None)

for i in root.findall('product/name'):
    print i.text  #打印的有节点下name的内容
print "findtext:", root.findtext('product/name')
print "find: ", root.find('product/name')
#findtext: 测试价格测试价格　试4KG以下宠物狗狗用 单支
#find:  <Element 'name' at 0x10287e950>

#iter(tag=None),从 xml 根结点开始,根据传入的元素的 tag 返回所有的元素集合的迭代器
for i in root.iter(tag='command'):
    print "command iter:", i.text
##打印command: echo root:mytestpwd | sudo /usr/ sbin/chpasswd
#command: echo root:mytestpwd | sudo /usr/ sbin/chpasswd
#command: yjoqm 刘灿焕
#iterfind(match),根据传入的 tag 名称或者 path 以迭代器的形式返回所有的子元素
for i in root.iterfind('product/title'):
    print "command iterfind:", i.text

#tag 字符串，用来表示元素所代表的名称
print root[1].tag #打印product

#text 表示元素所对应的值
print root[1].text

#用字典表示的元素的属性
print root[1].attrib


#get(key, default=None) 根据元素属性字典的 key 值获取对应的值,如果找不到对应的属性,则返回 default
print root[0].attrib.get("platform") #linux

#items() 
print root[0].items()
#输出[('platform', 'linux'), ('name', 'linuxtest')]

#keys 返回元素属性的kys 值集合
print root[0].keys()
#['platform', 'name']

#统计某值name出现的次数
count = 0
for event, elem in ET.iterparse('six.xml'):
    print "event:", event
    print "elem:", elem
    if event=='end':
        if elem.tag == 'name':
            count += 1
        elem.clear()
print count 
