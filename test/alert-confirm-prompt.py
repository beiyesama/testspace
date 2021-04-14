# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
url="file:///A:/testspace/alter-confirm-prompt.html"
driver.get(url)
time.sleep(2)

#alert操作
driver.find_element_by_id("alert").click()
time.sleep(3)
t = driver.switch_to.alert
#打印警告框文本内容
print(t.text)
#点警告框确认按钮
t.accept()

#confirm操作
driver.find_element_by_id("confirm").click()
time.sleep(3)
t = driver.switch_to.alert
#打印警告框文本内容
print(t.text)
#点警告框确认按钮
t.accept()
#t.dismiss #相当于点x，取消

#prompt操作
driver.find_element_by_id("prompt").click()
time.sleep(3)
t = driver.switch_to.alert
#打印警告框文本内容 文本框输入
print(t.text)
t.send_keys("hello dbb")
#点警告框确认按钮
t.accept()
#t.dismiss #相当于点x，
