# coding:utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("file:///A:/testspace/radio-checkbox.html")

#单选：radio
driver.find_element_by_id("boy").click()
time.sleep(3)
driver.find_element_by_id("girl").click()
time.sleep(3)

#复选框：checkbox
driver.find_element_by_id("c1").click() #单个勾选

#全部勾选
checkboxs = driver.find_elements_by_xpath("//*[@type='checkbox']") #find_elements不能click
for i in checkboxs:
    i.click()

#判断是否选中 is_selected()

#点击前判断是否选中 没点击返回False,点击过返回True
s = driver.find_element_by_id("boy").is_selected()
print(s)
time.sleep(3)
#点击
driver.find_element_by_id("boy").click()
#判断点击后是否选中
r = driver.find_element_by_id("boy").is_selected()
print(r)
time.sleep(3)

#复选框全选
checkboxs = driver.find_elements_by_xpath("//*[@type='checkbox']") #find_elements不能click
for i in checkboxs:
    if not i.is_selected():
        i.click()
time.sleep(5)
driver.quit()
