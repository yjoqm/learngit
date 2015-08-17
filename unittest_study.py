#!/usr/bin/env python
# coding=utf-8
#单元测试的加载方式有2种：一种是通过unittest #main()来启动单元测试的测试模块；一种是添加到testsuite集合中再加载所有的被测试对象，而testsuit里存放的就是单元测试的用例
import unittest
import test_myclass
class mytest(unittest.TestCase):
    #初始化
    def setUp(self):
        self.tclass = test_myclass.myclass() #实例化被测试模块中的类
    #退出清理
    def tearDown(self):
        pass
    def testsum(self):
        self.assertEqual(self.tclass.sum(1,2),3,'test sum fail')
    def testsub(self):
        self.assertEqual(self.tclass.sub(4,1),3,'test sub fail')


if __name__=='__main__':
    unittest.main()
#测试4个网址是否返回200
import requests
class TestUrlHttpcode(unittest.TestCase):
    def setUp(self):
       self.urlinfo = [
            'http://www.baidu.com',
            'http://www.163.com',
            'http://www.sohou.com',
            'http://www.cnpythoner.com'
        ]
       # self.checkurl = urlinfo 可以直接初始化也可以像这样初始化,后续调用会有点差别
    def tearDown(self):
            pass

    def test_resulrt(self):
        #for i in self.checkurl:
        for i in self.urlinfo:
            httpcode = requests.get(i).status_code
            self.assertEqual(httpcode,200)
            


if __name__ == '__main__':
    unittest.main()
