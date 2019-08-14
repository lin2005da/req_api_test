#-*-coding:utf-8-*-
# @time     :2019/7/29/029 15:54
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :asserty_index.py
# @Sofeware :PyCharm Community Edition
from page.base_page import Base
from page.ele_locator import locator
class index(Base):
    @property
    def success_login(self):
        return self.element_wait(locator.successlogin_locator)
    @property
    def success_bidinfo(self):
        return self.element_wait(locator.successbid_locator)

