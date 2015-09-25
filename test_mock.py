#!/usr/bin/env python
# coding=utf-8
import requests
import mock
import unittest
import test_mockclient

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_request('http://www.baidu.com')

#mock，找到要替换的对像， 也就是send_request, 实例化mock类， 使用该对像替换想要换掉的对像, 然后写测试代码

class TestClient(unittest.TestCase):
    def test_success_request(self):
        success_send = mock.Mock(return_value='200') #需要测试visit_ustack，则需要替换掉send_request。
        test_mockclient.send_request = success_send
        self.assertEqual(test_mockclient.visit_ustack(),200)

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        test_mockclient.send_request = fail_send
        self.assertEqual(test_mockclient.visit_ustack(),404)


