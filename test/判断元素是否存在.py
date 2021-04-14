# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#find_elements方法判断
def is_element_exist(xpath):
    s = driver.find_elements_by_xpath(xpath)
    if len(s) == 0:
        print("未找到元素：%s" % xpath)
        return False
    elif len(s) == 1:
        print("找到1个元素：%s" % xpath)
        return True
    else:
        print("找到%s个元素：%s" % (len(s),xpath))
        return True

if is_element_exist("//input[@id='kw']"):
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("hello dbb")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='kw']").clear()
if is_element_exist("//input"):
    driver.find_element_by_xpath("//input")
    time.sleep(3)
if is_element_exist("//p[7]/img[1]"):
    driver.find_element_by_xpath("//p[7]/img[1]").send_keys("hello")
    time.sleep(3)
    driver.find_element_by_xpath("//p[7]/img[1]").clear()
#driver.quit()

#捕获异常方法 无法判断数量
def isElementExist(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
print(isElementExist("//input"))
print(isElementExist("//p[7]/img[1]"))

driver.quit()