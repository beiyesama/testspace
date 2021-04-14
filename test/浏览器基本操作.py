import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome() #打开浏览器
driver.get("https://www.baidu.com") #打开百度
#等待时长10s，每1s询问一次,不指定默认0.5s
WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("kw")).send_keys("hello")

#判断id为kw元素是否消失 备注：此方法未调好，暂时放这
is_disappeared = WebDriverWait(driver,10,1).until_not(lambda x:x.find_element_by_id("kw").is_displayed())
print(is_disappeared)

driver.set_window_size(540,960) #设置窗口大小540*960
driver.implicitly_wait(5)
#implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
# time.sleep(5)表示必须等待5秒定位；
driver.maximize_window() #将浏览器窗口最大化
driver.get("http://aliyun.32.cn")
time.sleep(5) #设置休眠5s
driver.back() #返回上一页
time.sleep(3)
driver.forward()#切换到下一页
time.sleep(2)
driver.refresh() #刷新页面
time.sleep(2)
driver.get_screenshot_as_file("A:\\testspace\\32.jpg")
driver.quit() #关闭浏览器 driver.close()用于关闭当前窗口