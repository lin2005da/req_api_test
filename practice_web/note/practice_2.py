#-*-coding:utf-8-*-
# @time     :2019/7/26/026 8:56
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :practice_2.py
# @Sofeware :页面操作、鼠标操作
# 要求：
# 1、登录百度界面，页面最大化
# 2、点击用户登录，输入登录账号，登录成功


from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(30)#隐性等待
driver.get('http://www.baidu.com')
WebDriverWait(driver,3)
driver.find_elements_by_xpath('//div[@id="u1"]/a[@name="tj_login"]')[0].click()#登录
WebDriverWait(driver,3)
driver.find_elements_by_xpath('//p[text()="用户名登录"]')[0].click()#用户名登录
WebDriverWait(driver,3)
phone=driver.find_elements_by_xpath('//input[@class="pass-text-input pass-text-input-userName"]')[0]
phone.send_keys('13881842312')#用户名
driver.find_elements_by_xpath('//input[@class="pass-text-input pass-text-input-password"]')[0].send_keys('lin2005daABC')#密码
phone.submit()
# driver.find_elements_by_xpath('//input[@class="pass-button pass-button-submit"]')[0].click()#登录
WebDriverWait(driver,3)
driver.find_elements_by_xpath('//a[@class="forceverify-header-a"]')[0].click()#关闭安全验证
WebDriverWait(driver,3)
driver.quit()






