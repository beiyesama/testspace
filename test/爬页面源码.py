# coding:utf-8
from selenium import webdriver
import time
import re

driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/")
time.sleep(5)
page = driver.page_source #page_source方法可以直接返回页面源码
print(page)

#非贪婪匹配，re.(re.xx匹配字符,如换行符re.S)
url_list = re.findall('href="(.*?)"',page,re.S)
url_all=[]
for url in url_list:
    if "http" in url:
        url_all.append(url)
print(url_all)
driver.quit()


