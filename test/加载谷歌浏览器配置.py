# coding:utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
#增加个人浏览器配置地址
options.add_argument(r"--user-data-dir=C:\Users\hsiacool\AppData\Local\Google\Chrome\User Data\Default")
#启动时安装crx扩展
#options.add_extension("C:\Users\hsiacoolxxx.crx")
#启动时安装本地插件
options.add_argument("load-extension=C:/Users/hsiacool/AppData/Local/Google/Chrome/User Data/Default/Extensions/hgimnogjllphhhkhlmebbmlgjoejdpjl/2.0.2_0")
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://aliyun.32.cn")
time.sleep(5)
driver.quit()