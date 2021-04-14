# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://aliyun.32.cn")
time.sleep(5)
#execute_script()可以执行js的脚本

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(3)

#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
time.sleep(3)

#滚动到某个位置
js = "window.scrollTo(0,100)"
driver.execute_script(js)
time.sleep(5)

#元素聚焦 先定位元素，然后页面直接跳到元素出现的位置
target = driver.find_element_by_css_selector("[href='/zhuanli/fmzl/'] .info")
driver.execute_script("arguments[0].scrollIntoView();",target)