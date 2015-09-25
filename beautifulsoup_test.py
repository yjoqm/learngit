#!/usr/bin/env python
# coding=utf-8
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')

#print soup.prettify()
print soup.title # <title>The Dormouse's story</title>
print soup.title.string # u'title'
print soup.title.parent.name # u'head'
print soup.p # <p class="title"><b>The Dormouse's story</b></p>
print soup.p['class'] # u'title'
print soup.find('a') ## <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print soup.find(id='link3')
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


#found url
for link in soup.find_all('a'):
    print (link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

#extracting all the text form a page
print soup.get_text()

soup = BeautifulSoup('<html>dataatestestst</html>')
print "soup is:", soup

#TAG object
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print type(tag)



