from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

#driver.find_element_by_xpath('//*[contains(text(),"hao123")]').click() #支持正则表达式
#driver.find_element_by_xpath('//*[contains(@id,"kw")]').send_keys("python")
driver.find_element_by_css_selector('input#kw[name="wd"]').send_keys("python")