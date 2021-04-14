# coding:utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://aliyun.32.cn")
driver.implicitly_wait(10)
#获取当前窗口的句柄
h = driver.current_window_handle
print(h)

#获取所有窗口的句柄
driver.find_element_by_css_selector("[href='http://i.aliyun.32.cn']").click()
all_h = driver.window_handles
print(all_h)

#切换窗口
#方法一：不等于首页就切换
for i in all_h:
    if i != h:
        driver.switch_to.window(i)
        print(driver.title)
#方法二：直接切换到all_h这个list里第二个handle的值:all_h[1]
driver.switch_to.window(all_h[1])
print(driver.title)
#关闭新窗口 driver.close()
driver.close()
#切回首页
driver.switch_to.window(h)
print(driver.title)

driver.quit()