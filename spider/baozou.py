#!/usr/bin/env python
# coding=utf-8
#爬取暴走的图片，测试下

import re
import urllib
import os

BASE_HERE = os.path.abspath(os.path.dirname(__file__))
print BASE_HERE
#/Users/admin/mygit/learngit/spider

#获取页面源码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#正则得到页面中想要的地址,imglist会返回一个列表
def getImg(html):
    reg = r'http://wallpaper\.baozou\.com/s/.+\.jpg-small3'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    #print imglist
    x = 0
    for imgurl in imglist:
        #urllib.urlretrieve(imgurl, '/Users/admin/mygit/learngit/spider/baozou_pic/%s.jpg'%x)
        urllib.urlretrieve(imgurl, BASE_HERE +'/baozou_pic/%s.jpg'%x)
        x = x+1
    return imglist

if __name__ == '__main__':
    test = getHtml('http://baozoumanhua.com/wall_papers?zg_event=%E5%A3%81%E7%BA%B8')
    getImg(test)
