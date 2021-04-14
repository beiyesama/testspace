# coding:utf-8
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\hsiacool\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome(chrome_options=options)


#alert弹窗
driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
time.sleep(3)
driver.switch_to.frame("iframeResult")
driver.find_element_by_xpath("//input[@value='显示警告框']").click()
time.sleep(2)
a1 = driver.switch_to.alert
a1.accept()
'''
accept - 点击【确认】按钮
dismiss - 点击【取消】按钮（如有按钮）
send_keys - 输入内容（如有输入框）
'''
time.sleep(2)

#自定义弹窗
driver.get("https://sh.xsjedu.org/")
time.sleep(3)
js = "document.getElementById('doyoo_mon_inner').style.display='none'"
driver.execute_script(js)
time.sleep(3)
driver.quit()

