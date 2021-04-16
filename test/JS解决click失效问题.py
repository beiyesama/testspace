#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\hsiacool\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com/")
mouse = driver.find_element_by_css_selector("#s-usersetting-top")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_css_selector(".setpref").click() #点击搜索设置
WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("nr_2")).click()
#用js执行点击恢复默认按钮的事件
js = "document.getElementsByClassName('prefpanelrestore setting-btn c-btn c-gap-right-large')[0].click()"
driver.execute_script(js)
time.sleep(2)
driver.switch_to.alert.accept()
driver.quit()