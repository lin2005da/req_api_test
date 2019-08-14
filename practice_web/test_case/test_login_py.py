#-*-coding:utf-8-*-
# @time     :2019/7/29/029 12:16
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :test_login.py
# @Sofeware :PyCharm Community Edition


from data import data_login
import pytest
import time
from page import asserty_index

# @pytest.mark.all
class TestLogin_send():

    @pytest.mark.usefixture('init_driver')
    @pytest.mark.parametrize('data',data_login.user_error)
    @pytest.mark.login
    def test_login_fail(self,data,init_driver):
        self.loginpage,driver=init_driver
        self.loginpage.phone_clear()
        self.loginpage.pwd_clear()
        self.loginpage.submit(data["phone"], data["password"])
        assert data['expected'] == self.loginpage.error_login().text

    @pytest.mark.login
    @pytest.mark.parametrize('case', data_login.user_unthour)
    def test_login_error(self,case,init_driver):
        loginpage, driver = init_driver
        loginpage.phone_clear()
        loginpage.pwd_clear()
        loginpage.submit(case["phone"],case["password"])
        time.sleep(3)#target打开和关闭需要时间等待，如果没有强制时间会出现读取的数据是上一条用例的情况，造成断言出错
        user_ele=loginpage.author_login()
        assert case['expected'] == user_ele.text


    @pytest.mark.smoke
    # @pytest.mark.parametrize('case', data_login.user_correct)
    def test_login_success(self,init_driver):  #正常登录无法和登录失败一起调用，原因不明？？
        loginpage, driver = init_driver
        loginpage.phone_clear()
        loginpage.pwd_clear()
        # print(case["phone"], case["password"])
        # loginpage.submit(case["phone"], case["password"])
        loginpage.submit("18684720553","python")
        user_ele = asserty_index.index(driver).success_login
        assert 'python10' in user_ele.text



if __name__ == '__main__':
    # unittest.main()
    pytest.main()