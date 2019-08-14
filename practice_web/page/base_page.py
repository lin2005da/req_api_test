#-*-coding:utf-8-*-
# @time     :2019/7/29/029 15:11
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :base_page.py
# @Sofeware :PyCharm Community Edition
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from common import route
from common import loggin
log=loggin.logg()
class Base:
    def __init__(self,driver:Chrome):
        self.driver=driver
        self.driver.maximize_window()
    def element_wait(self,ele_locator,wtime=20):
        try:
            return WebDriverWait(self.driver,wtime).until(ec.visibility_of_element_located(ele_locator))
        except Exception as e:
            log.get_error('element_error:{0}'.format(e))
            self.driver.save_screenshot(route.png_log)
    def get_handle(self,name=None):
        if name is None:
            handle=self.driver.window_handles
            current=self.driver.current_window_handle
            WebDriverWait(self.driver, 20).until(ec.new_window_is_opened(current))
            return self.driver.switch_to.window(handle[-1])

        return self.driver.switch_to.window(name)
