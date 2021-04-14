# coding:utf-8
from selenium import webdriver
import random
import time

#百度“测试部落”并随机点击一个搜索结果

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
#输入测试部落
driver.find_element_by_id("kw").send_keys("测试部落")
#点击搜索
driver.find_element_by_xpath("//*[@id='su']").click()
#driver.find_element_by_id("kw").submit() #直接用回车键
#定位搜索结果 并输出链接
s = driver.find_elements_by_xpath("//h3[@class='t']/a")
for i in s:
    print(i.get_attribute("href"))
    print(i.text)
#模拟用户随机点击一个搜索结果
r = random.randint(0,9)
s[r].click()
time.sleep(5)
driver.quit()

