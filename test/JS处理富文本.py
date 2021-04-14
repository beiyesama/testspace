# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com")
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)

#js处理iframe问题 定位后用js直接输入，无需切换iframe，点击保存后也无需再切回来
body = "这里是通过js发的正文内容"
js = 'document.getElementById("Editor_Edit_EditorBody_ifr")' '.contentWindow.document.body.innerHTML="%s"' % body
driver.execute_script(js)

driver.find_element_by_id("Editor_Edit_lkbDraft").click()
