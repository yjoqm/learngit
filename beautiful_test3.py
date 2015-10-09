#!/usr/bin/env python
# coding=utf-8
html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

#操作文档树最简单的方法就是告诉它你想获取的tag的name.如果想获取 <head> 标签,只要用 soup.head :
print soup.head
# <head><title>The Dormouse's story</title></head>

print soup.title
# <title>The Dormouse's story</title>

print soup.body.b
# <b>The Dormouse's story</b>
#通过点取属性的方式只能获得当前名字的第一个tag:
print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print soup.find_all('a') #find_all获取所有的标签
#tag的 .contents 属性可以将tag的子节点以列表的方式输出:
head_tag = soup.head
print "head_tag:", head_tag #<head><title>The Dormouse's story</title></head>
title_tag = head_tag.contents[0].contents
print "title_tag:", title_tag #[u"The Dormouse's story"]
#通过tag的 .children 生成器,可以对tag的子节点进行循环
title_tag = head_tag.contents[0]
for child in title_tag.children:
    print "child:",child

#.descendants 属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
        print(child)

#BeautifulSoup 有一个直接子节点(<html>节点),却有很多子孙节点
len(list(soup.children))
# 1
len(list(soup.descendants))
# 25
#如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
title_tag.string
# u'The Dormouse's story'
head_tag.contents
# [<title>The Dormouse's story</title>]

head_tag.string
# u'The Dormouse's story'
#如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:
for string in soup.strings:
    print repr(string)
    #print "string:",str(string)
#使用.stripped_strings除去多的空白内容

for string in soup.stripped_strings:
    print "repr string: ",(repr(string))



#通过 .parent 属性来获取某个元素的父节点
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>
link = soup.a
print link #<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print "parent:", parent
    else:
        print "parent.name:", parent.name

