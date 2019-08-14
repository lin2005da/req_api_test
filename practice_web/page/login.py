#-*-coding:utf-8-*-
# @time     :2019/7/29/029 12:16
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :login.py
# @Sofeware :PyCharm Community Edition


from page.base_page import Base
from page.ele_locator import locator

class LoginPage(Base):
    url='http://120.78.128.25:8765/Index/login.html'
    def get(self):
        return self.driver.get(self.url)
    @property
    def phone(self):
        return self.element_wait(locator.phone_locator)

    @property
    def pwd(self):
        return self.element_wait(locator.pwd_locator)
    def phone_send(self,msg):
        return self.phone.send_keys(msg)
    def pwd_send(self,msg):
        return self.pwd.send_keys(msg)
    def submit(self,phone,pwd):
        # self.get()
        # self.window_max()
        self.phone_send(phone)
        self.pwd_send(pwd)
        return self.phone.submit()
    def author_login(self):
        return  self.element_wait(locator.correct_locator)
    def phone_clear(self):
        return self.phone.clear()
    def pwd_clear(self):
        return self.pwd.clear
    def error_login(self):
        return self.element_wait(locator.errormsg_locator)
    def quit(self):
        return self.driver.quit()

