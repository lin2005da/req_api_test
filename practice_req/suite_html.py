#-*-coding:utf-8-*-
# @time     :2019/7/11/011 10:44
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :suite_html.py
# @Sofeware :PyCharm Community Edition
import HTMLTestRunnerNew
import unittest
from common import route
# from test_case import login,reg,recharge,withdraw,add,audit,invest

# suite_1=unittest.TestSuite()
# loader=unittest.TestLoader()
# suite_1.addTest(loader.loadTestsFromModule(login))
# suite_1.addTest(loader.loadTestsFromModule(reg))
# suite_1.addTest(loader.loadTestsFromModule(recharge))
# suite_1.addTest(loader.loadTestsFromModule(withdraw))
# suite_1.addTest(loader.loadTestsFromModule(add))
# suite_1.addTest(loader.loadTestsFromModule(audit))
# suite_1.addTest(loader.loadTestsFromModule(invest))

discover=unittest.defaultTestLoader.discover(start_dir=route.test_case, pattern='test_*.py')
with open('html_1.html','wb') as f:
    file_1=HTMLTestRunnerNew.HTMLTestRunner(stream=f, title='测试报告', verbosity=2,description=None,tester='cyl')
    file_1.run(discover)
# with open('1.txt','w') as file:
#     r=unittest.TextTestRunner(stream=file, verbosity=2,descriptions='测试登录')
#     r.run(suite_1)