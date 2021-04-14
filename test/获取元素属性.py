# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

#获取页面title
title = driver.title
print(title)

# <a class="text-color" href="//www.baidu.com/cache/setindex/index.html" target="_blank">设为首页</a>
#获取元素的文本
t1 = driver.find_element_by_xpath("//a[.='设为首页']")
print(t1.text)

#获取元素的标签
t2 = driver.find_element_by_xpath("//a[.='设为首页']")
print(t2.tag_name)

#获取元素的其他属性
t3 = driver.find_element_by_xpath("//a[.='设为首页']")
print(t3.get_attribute('class'))

# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
#获取输入框的文本值
driver.find_element_by_id("kw").send_keys("hello dbb")
t4 = driver.find_element_by_id("kw").get_attribute("value")
print(t4)

#获取浏览器名称
print(driver.name)

driver.quit()