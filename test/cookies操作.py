# coding:utf-8
from selenium import webdriver
import time
import 登录案例

#获取cookies：driver.get_cookies()
driver = webdriver.Chrome()
#启动浏览器后获取cookies
print(driver.get_cookies())
#打开网页后获取cookies
driver.get("http://aliyun.32.cn")
time.sleep(2)
print(driver.get_cookies())
#登录后获取cookies
登录案例.login(driver,"15658678027","123456dbb")
print(driver.get_cookies())

#获取指定name的cookie：driver.getcookie(name)
print(driver.get_cookie(name='is_login'))

#清除指定cookie:driver.delete_cookie()
driver.delete_cookie(name='is_login')
driver.refresh()

#清除所有cookies：driver.delete_all_cookies()
driver.delete_all_cookies()
print(driver.get_cookies())

#add_cookie(cookie_dict)
cookie = {"domain": ".32.cn",
          "expiry": 1618496295,'httpOnly': False, 'name': 'is_login', 'path': '/', 'sameSite': 'Lax', 'secure': False,
          "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTExMTU0LCJtb2JpbGUiOiIxNTY1ODY3ODAyNyIsIndlYnNpdGVfaWQiOjAsInBvd2VyIjoxLCJpcCI6IjYxLjE2NC40My4yMzYiLCJpYXQiOjE2MTg0Njc0OTIsImV4cCI6MTYxODU1Mzg5Mn0.6MGJtWg4RixdLLeDmizmfg9Xc__lvgiTaRHkxubagoY"}
driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()