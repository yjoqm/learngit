#!/usr/bin/env python
# coding=utf-8
import urllib2
import re
import thread
import time 

class Spider_Model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    #将所有的段子扣出来，添加到列表并返回列表
    def GetPage(self,page):
        myUrl = 'http://m.qiushibaike.com/hot/page/' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        req = urllib2.Request(myUrl,headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        #encode 的作用是将unicode 编码转换成其他的编码的字符串
        #decode是将其它编码的字符串转换成unicode
        unicodePage = myPage.decode('utf-8')
       # print unicodePage 
       # 找出甩的class = 'content' 的div 标记
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            items.append([item[0].replace("\n",""),item[1].replace("\n","")]) 
        return item 
    def LoadPage(self):
        #如果用户未输入quit，则一直运动
        while self.enable:
            #如果 page 数姐中的页面中的内容小于2个
            if len(self.pages) < 2:
                try:
                    #获取新的页面中的内容
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法连接网面'
            else:
                time.sleep(1)

    def ShowPage(self,nowPage,page):
        for items in nowPage:
            print u'第%d页' % page, items[0], items[1]
            myInput = raw_input()
            if myInput == 'quit':
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page
        print u'正在加载中。。。'

        #新建一个线程在后台加载并存储
        thread.start_new_thread(self.LoadPage,())

        while self.enable:
            #如果selfpage 数组中有元素
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1





if __name__ == '__main__':
    myModel = Spider_Model()
    #myModel.GetPage(1)
    myModel.Start()

