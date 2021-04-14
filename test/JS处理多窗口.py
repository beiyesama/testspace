# coding:utf-8
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\hsiacool\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com")
time.sleep(5)

#JS通过 document.evaluate('...', document).iterateNext() 方法可以用 xpath 路径定位到元素节点 #暂时不会使用
js = "document.getElementsByClassName('mnav c-font-normal c-color-t')[5].target='';"
driver.execute_script(js)
driver.find_element_by_xpath("//a[@href='http://tieba.baidu.com']").click()
time.sleep(10)
driver.quit()