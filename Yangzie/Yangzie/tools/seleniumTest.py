# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='G:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("https://www.taobao.com/")

print(driver.page_source)

driver.quit()