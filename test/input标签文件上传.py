# coding:utf-8
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\hsiacool\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://aliyun.32.cn/zhuce/")
time.sleep(5)
#元素聚焦
'''
js = "window.scrollTo(0,800)"
driver.execute_script(js)
time.sleep(3)
'''
target = driver.find_element_by_xpath("//label[contains(.,'商标图样：')]")
driver.execute_script("arguments[0].scrollIntoView()",target)
r = driver.find_elements_by_class_name("el-upload__input")[1]
time.sleep(3)
r.send_keys(r"A:\testspace\32.jpg")
time.sleep(5)
driver.quit()
