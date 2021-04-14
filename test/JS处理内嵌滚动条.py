# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///A:/testspace/divscroll.html")

#纵向滚动
js1 = "document.getElementById('yoyoketang').scrollTop=10000" #底部
driver.execute_script(js1)
time.sleep(3)
js2 = "document.getElementById('yoyoketang').scrollTop=0" #顶部
driver.execute_script(js2)
time.sleep(3)

#横向滚动
js3 = "document.getElementsByClassName('scroll')[0].scrollLeft=10000" #最右端
driver.execute_script(js3)
time.sleep(3)
js4 = "document.getElementsByClassName('scroll')[0].scrollLeft=0" #最左端
driver.execute_script(js4)
time.sleep(3)

driver.quit()
