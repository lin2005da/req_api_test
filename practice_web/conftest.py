#-*-coding:utf-8-*-
# @time     :2019/8/4/004 17:18
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :conftest.py
# @Sofeware :PyCharm Community Edition
import pytest
from selenium import webdriver
from page import login
from common import read_conf
from page import bid
cf =read_conf.Config()
@pytest.fixture(scope='class')
def init_driver():
    print("begin driver")
    driver=webdriver.Chrome()
    login_page=login.LoginPage(driver)
    login_page.get()
    yield (login_page,driver)
    print("quit driver")
    driver.quit()

@pytest.fixture(scope='class')
def baselogin():
    driver=webdriver.Chrome()
    login_page=login.LoginPage(driver)
    login_page.get()
    login_page.submit(cf.get_value('page', 'user1'), cf.get_value('page', 'pwd'))
    bid_page = bid.Bid(driver)
    bid_page.option_click()
    yield (bid_page,driver)
    driver.quit()