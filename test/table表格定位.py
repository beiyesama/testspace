# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///A:/testspace/table.html")

#xpath定位第二行第一列
t = driver.find_element_by_xpath("//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)
time.sleep(3)

driver.quit()