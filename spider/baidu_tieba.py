#!/usr/bin/env python
# coding=utf-8
#练习baidu 贴吧的例子，
#功能：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数,下载对应页码内的所有页面并存储为html文件
#url:http://tieba.baidu.com/p/4097519444?pn=1/2/3/4/5/6

import string, urllib2

def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,4) + '.html' #zfill(i,4) 4位，i,不足4位默认使用0填充. 
        print 'downloading' + str(i) + 'website' + sName + '....'#自动填充成六位的文件名
        f = open(sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4097519444?pn='
    #begin = 1
    #end = 4
    baidu_url = str(raw_input('url is: \n'))
    begin_page = int(raw_input('begin page is: \n'))
    end_page = int(raw_input('end page is: \n'))

    baidu_tieba(url, begin_page, end_page)


