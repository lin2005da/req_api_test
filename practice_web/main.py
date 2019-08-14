#-*-coding:utf-8-*-
# @time     :2019/8/1/001 9:57
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :main.py
# @Sofeware :PyCharm Community Edition
import pytest
from common import route
if  __name__ == '__main__':
    # pytest.main(['-m smoke',
    #              '--resultlog={0}'.format(route.log_result),
    #              '--junitxml={0}'.format(route.xml_result),
    #              '--html={0}'.format(route.html_result)])
    pytest.main(['-m smoke','--capture=no','--html={0}'.format(route.html_result),'--alluredir=allure'])