# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
#鼠标悬停到设置上 点击搜索设置
mouse = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_class_name("setpref").click()
#先定位下拉框再定位选项
s = driver.find_element_by_id("nr")
s.find_element_by_xpath("//option[@value='50']").click()

#select模块 导入select方法 from selenium.webdriver.support.select import Select
s = driver.find_element_by_id("nr")
Select(s).select_by_index(2)
Select(s).select_by_value("50")
Select(s).select_by_visible_text("每页显示50条")
s.click()
"""
deselect_all()          ：取消所有选项
deselect_by_index()     ：取消对应index选项
deselect_by_value()      ：取消对应value选项
deselect_by_visible_text() ：取消对应文本选项
first_selected_option()  ：返回第一个选项
all_selected_options()   ：返回所有的选项
"""