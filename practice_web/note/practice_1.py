#-*-coding:utf-8-*-
# @time     :2019/7/25/025 17:12
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :practice_1.py
# @Sofeware :键盘、页面跳转、鼠标操作


# 要求
# 1、进入百度页面
# 2、在输入框中输入webservice，搜索
# 3、点击cdsn博客
# 4、进入博客页面，点击展开全文
# 5、滑到底部点击返回首页
# 6、进入首页后打印首页url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.implicitly_wait(30)#隐性等待30s

driver.get('http://www.baidu.com')

driver.maximize_window()#最大化窗口
in_1=driver.find_element_by_id('kw')#输入框
in_1.send_keys('webservice',Keys.ENTER)#键入文字，确认


u='//a[text()="手把手教你如何玩转"]'#发现元素
we=WebDriverWait(driver,5)#等待页面加载，最长30s
we.until(EC.element_to_be_clickable((By.XPATH,u)))#等待时间知道发现能点击元素为止


title=driver.find_elements_by_xpath(u)#返回是个列表
title[0].click()

WebDriverWait(driver,5)#等待页面加载，最长30s


handle=driver.window_handles

driver.switch_to.window(handle[-1])#切换到最新标签页

driver.find_elements_by_xpath('//div[@class="hide-article-box hide-article-pos text-center"]/a')[0].click()#展开全文

#遗留问题：鼠标滚动
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

driver.find_elements_by_xpath('//div[@class="recommend-end-box"]//a')[0].click()#点击返回首页
time.sleep(5)

driver.quit()#退出浏览器
