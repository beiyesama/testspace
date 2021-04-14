#iframe上的登录定位
# coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://you.163.com/u/login")
driver.implicitly_wait(10)

#先把定位器切换到iframe上 用switch_to_frame方法切换
#<iframe name="" frameborder="0" id="x-URS-iframe1617959575937.0173"......

#通过iframe的id定位 默认支持id和name
driver.switch_to.frame("x-URS-iframe1617959575937.0173")
driver.find_element_by_name("email").send_keys("123") #定位输入账号
driver.find_element_by_name("password").send_keys("dbb") #定位输入密码
#如果没有id和name 先定位iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

#iframe上操作完后想回到主页面上操作元素 用switch_to_default_content()方法返回到主页面
driver.switch_to.default_content()