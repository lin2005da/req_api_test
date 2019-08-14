#-*-coding:utf-8-*-
# @time     :2019/7/25/025 8:28
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :study_element.py
# @Sofeware :PyCharm Community Edition
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from  selenium.webdriver.support.ui import Select
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
wait=WebDriverWait(driver,15,1)#对象名，总时长，轮询周期

wait.until(EC.element_to_be_clickable("id","kw"))
wait.until(EC.element_to_be_clickable(By.ID,"kw"))  #until(判断条件）
                                                        #EC.方法名（定位方式，定位表达式）
el=driver.find_elements_by_xpath('//*[@id="adv-setting-5"]/select/option[text()="微软 Excel (.xls)"]')
w=Select(el)
print(w.options)
w=driver.find_element_by_id("kw")
w.send_keys('asd',Keys.DOWN)

action=ActionChains(driver)
el=driver.find_elements_by_xpath('//*[@id="adv-setting-5"]/select/option[text()="微软 Excel (.xls)"]')
wl=action.move_to_element_with_offset(el).click().double_click()
wl.perform()