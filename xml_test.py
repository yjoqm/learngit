#!/usr/bin/env python
# coding=utf-8
import xml.etree.ElementTree as ET
tree = ET.parse('/home/ellen/ellen.xml')
root = tree.getroot()
tag = root.tag #获取跟节点
print tag

#获取跟节点的属性
attrib = root.attrib
#获取全部的子节点与属性
for child in root:
    print (child.tag, child.attrib)

#获取属性对应的值
for goods in root.findall('goods'):
    no = goods.get('no')
    name = goods.find('goods_name').text
    print (no, name)
#修改xml内容,把价格增加20
for current_price in root.iter('current_price'):
    new_price = float(current_price.text) + float('20.00')
    current_price.text = str(new_price)
tree.write('/home/ellen/ellen.xml')



    

