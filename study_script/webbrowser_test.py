#!/usr/bin/env python
# coding=utf-8
import webbrowser
url = 'http://www.baidu.com'
webbrowser.open_new_tab(url)
#webbrowser.close()

def ov_open_new_tab(url):
    if url is not None and url != '':
        return webbrowser.open_new_tab(url)
    else:
        print "faild"
        exit(0)

