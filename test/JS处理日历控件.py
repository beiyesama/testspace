# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
time.sleep(5)

# <input type="text" class="input inp-txt_select" value="2018-07-21" id="train_date" readonly="">
#去掉元素的readonly属性就能输入了
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

#清空文本后输入内容
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2020-04-14")
time.sleep(5)

#用js方法输入日期 直接改掉输入框的value,不用去readonly
js_value = "document.getElementById('train_date').value='2020-04-15'"
driver.execute_script(js_value)
time.sleep(3)

driver.quit()