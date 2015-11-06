#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
#打开百度，定位搜索框，提交搜索关键字 
driver.get('http://www.baidu.com')
inputElement = driver.find_element_by_id('kw')
inputElement.send_keys('Cheese!')
inputElement.submit()
print driver.title
try:
    WebDriverWait(driver,10).until(EC.title_contains("cheese!"))
    print driver.title
finally:
    driver.quit()


