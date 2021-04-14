# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#send_keys() 输入字符串
driver.find_element_by_id("kw").send_keys("python")
time.sleep(2)
#clear() 清空输入框
driver.find_element_by_id("kw").clear()
#click() 鼠标左键点击
driver.find_element_by_xpath("//*[@id='su']").click()
#submit()提交 一般用于模拟回车
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").submit()

#键盘操作 from selenium.webdriver.common.keys import Keys
#模拟enter键 send_keys(Keys.ENTER)
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
#复制 Ctrl+C：send_keys(Keys.CONTROL,'c')
#粘贴 Ctrl+V：send_keys(Keys.CONTROL,'v')
#全选 Ctrl+A：send_keys(Keys.CONTROL,'a')
#剪切 Ctrl+X：send_keys(Keys.CONTROL,'x')
#制表键 Tab: send_keys(Keys.TAB)

#鼠标操作 from selenium.webdriver.common.action_chains import ActionChains
driver.back()
driver.back()
#定位悬停位置
mouse = driver.find_element_by_xpath("//*[@class='s-top-right-text c-font-normal c-color-t']")
#perform()执行所有ActionChains中的行为    move_to_element()鼠标悬停
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
#右击鼠标 context_click()
#双击鼠标 double_click()
#ActionChains.double_click(mouse).perform()
#ActionChains.context_click().perform()
