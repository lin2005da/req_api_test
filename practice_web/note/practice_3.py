#-*-coding:utf-8-*-
# @time     :2019/7/26/026 11:51
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :practice_3.py
# @Sofeware :select选择框、输入、鼠标操作、界面操作

# 要求：
# 1、登录百度界面，页面最大化
# 2、点击高级搜索，输入柠檬班，操作选择框进行高级搜索
# 3、进入柠檬班首页，点击登录

from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(30)#隐性等待
driver.get('http://www.baidu.com')

x=driver.find_elements_by_xpath('//div[@id="u1"]/a[@name="tj_settingicon"]')[0]#设置
                    # driver.find_element(By.XPATH,'//div[@id="u1"]/a[@name="tj_settingicon"]')
action=ActionChains(driver)
action.move_to_element(x).perform()

WebDriverWait(driver,3).until(EC.visibility_of_any_elements_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_elements_by_xpath('//a[text()="高级搜索"]')[0].click()#高级搜索
WebDriverWait(driver,2)
driver.find_elements_by_xpath('//input[@class="c-input"]')[0].send_keys('ningmengban')#elements返回的是列表
WebDriverWait(driver,1)
y=driver.find_element_by_xpath('//*[@id="adv-setting-5"]/select')#文档格式
Select(y).select_by_index(0)#选择所有格式
WebDriverWait(driver,1)
driver.find_element_by_xpath('//input[@type="submit"][@value="高级搜索"]').click()

handle_1=driver.window_handles#标签页出现变化后，需要重新统计句柄，无法使用之前的
driver.switch_to.window(handle_1[-1])


WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"主页")]')))
driver.find_element_by_xpath('//h3[@class="t"]/a[text()="软件测试面试题-"]').click()

handle_2=driver.window_handles
driver.switch_to.window(handle_2[-1])

driver.maximize_window()#屏幕最大化
w=WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,'//a[@title="登录"]')))#返回的是查找到的webelement
                                                                            # 等同于 w=driver.find_element_by_xpath('//a[@title="登录"]')
w.click()#登录
# print(w)
driver.close()

handle_3=driver.window_handles
driver.switch_to.window(handle_3[-1])
driver.close()

WebDriverWait(driver,3)
driver.quit()