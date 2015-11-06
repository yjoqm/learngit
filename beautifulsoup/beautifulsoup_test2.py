#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests

t = requests.get('http://www.baidu.com')
#print t.text
soup = BeautifulSoup(requests.get('http://www.baidu.com').text)
#print soup.title
#print soup.find_all('a')
for link in soup.find_all('a'):
    print link.get('href')

