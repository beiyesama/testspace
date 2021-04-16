# coding:utf-8
'''
title_is： 判断当前页面的title是否完全等于（==）预期字符串，返回布尔值

title_contains : 判断当前页面的title是否包含预期字符串，返回布尔值

presence_of_element_located : 判断某个元素是否被加到了dom树里，并不代表该元素一定可见

visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0

visibility_of : 跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了

presence_of_all_elements_located : 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True

text_to_be_present_in_element : 判断某个元素中的text是否 包含 了预期的字符串

text_to_be_present_in_element_value : 判断某个元素中的value属性是否 包含 了预期的字符串

frame_to_be_available_and_switch_to_it : 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False

invisibility_of_element_located : 判断某个元素中是否不存在于dom树或不可见

element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫clickable

staleness_of : 等某个元素从dom树中移除，注意，这个方法也是返回True或False

element_to_be_selected : 判断某个元素是否被选中了,一般用在下拉列表

element_selection_state_to_be : 判断某个元素的选中状态是否符合预期

element_located_selection_state_to_be : 跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator

alert_is_present : 判断页面上是否存在alert
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://aliyun.32.cn/")
time.sleep(3)

#判断title title_is()和title_contains() 返回的是布尔值：Ture和False
title = EC.title_is(u'商标注册_商标查询_商标交易就在知协网') #两种写法
print(title(driver))
r = EC.title_contains(u'知协')(driver) #两种写法
print(r)
driver.quit()

#判断弹出框是否存在 alert_is_present()
# 如果正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
mouse = driver.find_element_by_css_selector("#s-usersetting-top")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_css_selector(".setpref").click() #点击搜索设置
WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("nr_2")).click()
js = "document.getElementsByClassName('prefpanelrestore setting-btn c-btn c-gap-right-large')[0].click()"
driver.execute_script(js)
result = EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.accept()
else:
    print("alert未弹出")
driver.quit()

#判断文本是否存在 text_to_be_present_in_elememt(locator,text)
# 返回的是布尔值：Ture和False locator参数是定位的方法 text参数是期望的值
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
locator1 = ("xpath","//a[.='新闻']")
text1 = u"新闻"
result1 = EC.text_to_be_present_in_element(locator1,text1)(driver)
print(result1)
#text_to_be_present_in_element_value(locator,text) 判断value的值
locator2 = ("id","su")
text2 = u"百度一下"
result2 = EC.text_to_be_present_in_element_value(locator2,text2)(driver)
print(result2)
driver.quit()

