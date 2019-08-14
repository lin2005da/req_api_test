#-*-coding:utf-8-*-
# @time     :2019/7/31/031 9:45
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :bid.py
# @Sofeware :PyCharm Community Edition
from page.base_page import Base
from page.ele_locator import locator

class Bid(Base):
    # @property
    def option_button(self):#项目
        return self.element_wait(locator.option_locator)
    # @property
    def invest(self):#投资
        return self.element_wait(locator.invest_locator)
    # @property
    def bid_submit(self):#提交
        return self.element_wait(locator.button_locator)
    def option_click(self):
        return self.option_button().click()
    def invest_send(self,money):
        return self.invest().send_keys(money)
    def submit_click(self):
        return self.bid_submit().click()
    def ori_money(self):#投标前余额
        return float(self.invest().get_attribute('data-amount'))
    def up_money(self):#投标后余额
        ping=self.element_wait(locator.up_locator).text
        return float(ping[0:-1])
    def btn(self):#查看并激活
        return self.element_wait(locator.btn_locator)
    def btn_click(self):
        return self.btn().click()

if __name__ == '__main__':
    # a='2553577255.48元'
    # print(type(a))
    # print(a[0:-1])
    #
    from page import login
    from selenium import webdriver
    from common import read_conf
    cf = read_conf.Config()
    from page import asserty_index

    driver = webdriver.Chrome()
    login_page = login.LoginPage(driver)
    login_page.get()
    login_page.submit(cf.get_value('page', 'user1'), cf.get_value('page', 'pwd'))
    bid_page = Bid(driver)
    # 首页点击项目
    bid_page.option_click()
    x=bid_page.ori_money()
    print(x)
    bid_page.invest_send('100')

    bid_page.submit_click()
    # 校验成功
    asserty_index.index(driver).success_bidinfo
    bid_page.btn_click()
    y=bid_page.up_money()
    print(y)
    print(x-y)