# coding:utf-8

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
# <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">
#通过id定位百度搜索框 输入“python”

#八种定位方式
#driver.find_element_by_id("kw").send_keys("python")
#driver.find_element_by_name("wd").send_keys("python") #会报错 说明这个搜索框的name属性不是唯一的
#driver.find_element_by_class_name("s_ipt").send_keys("python")
#driver.find_element_by_tag_name("input").send_keys("python") #会报错 通过标签定位
#driver.find_element_by_link_text("贴吧").click() #通过超链接文本定位 并点击
#driver.find_element_by_partial_link_text("ao123").click() #超链接字符串太长 输入部分模糊匹配
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python") #通过xpath定位
#driver.find_element_by_css_selector() #通过css定位

#xpath定位
driver.find_element_by_xpath('//*[@autocomplete="of"]').send_keys("python")#手写xpath 如//*[@a=1]

driver.find_element_by_xpath('//input[@name="wd"]').send_keys("python") #xpath通过标签筛选 *表示任意标签

driver.find_element_by_xpath('//span[@id="s_kw_wrap"]/input').send_keys("python") #层级关系定位 通过父亲标签来定位
driver.find_element_by_xpath('//form[@name="f"]/span/input').send_keys("python") #通过爷爷标签定位

driver.find_element_by_xpath('//select[@id="nr"]/option[1]').click() #兄弟元素多个无法层级定位 通过先后索引
driver.find_element_by_xpath('//select[@id="nr"]/option[2]').click()
driver.find_element_by_xpath('//select[@id="nr"]/option[3]').click()

#xpath逻辑运算与、或、非
driver.find_element_by_xpath('//*[@id="kw" and @name="wd"]').send_keys("python") #同时满足两个条件

#xpath模糊匹配功能
driver.find_element_by_xpath('//*[contains(text(),"hao123")]').click()
driver.find_element_by_xpath('//*[contains(@id,"kw")]').send_keys("python") #模糊匹配某个属性
driver.find_element_by_xpath('//*[starts-with(@id,"s_kw_")]').click() #模糊匹配以什么开头
driver.find_element_by_xpath('//*[ends-with(@id,"kw_wrap")]').click() #模糊匹配以什么结尾

#css定位

#通过元素的id、class、标签直接定位

#<input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd"/>
#css用#表示id属性，如#kw
#css用.表示class属性，如.s_ipt
#css直接用标签名称，如input
driver.find_element_by_css_selector("#kw").send_keys("python")
driver.find_element_by_css_selector(".s_ipt").send_keys("python")
driver.find_element_by_css_selector("input").send_keys("python")

#css通过其他属性定位
driver.find_element_by_css_selector('[name="wd"]').send_keys("python")
driver.find_element_by_css_selector('[type="text"]').send_keys("python")

#css通过标签与属性的组合定位
driver.find_element_by_css_selector("input#kw").send_keys("python") #与id class组合
driver.find_element_by_css_selector('input[name="wd"]').send_keys("python") #与其他属性组合

#css的层级关系
#xpath：//form[@id='form']/span/input
#xpath：//form[@class='form']/span/input
driver.find_element_by_css_selector('form#form>span>input').send_keys("python") #id
driver.find_element_by_css_selector('form.form>span>input').send_keys("python") #class

#css：索引
#例如css通过option:nth-child(1)来定位子元素 这里option是子元素标签
driver.find_element_by_css_selector('select#nr>option:nth-child(1)').click()
driver.find_element_by_css_selector('select#nr>option:nth-child(2)').click()
driver.find_element_by_css_selector('select#nr>option:nth-child(3)').click()

#css同时匹配两个属性
driver.find_element_by_css_selector('input#kw[name="wd"]').send_keys("python")