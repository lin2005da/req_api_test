#-*-coding:utf-8-*-
# @time     :2019/7/11/011 10:02
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :reg.py
# @Sofeware :PyCharm Community Edition
from common import do_excel
import unittest
from common import route
from common import request_1
from  ddt import ddt,data
# from conf import r_conf
import json
from common import logg


logger=logg.logger('withdraw')
read = do_excel.doExcel(route.exc_1)
cases_2 = read.get_data('withdraw')

@ddt
class TestWithdraw(unittest.TestCase):                               #测试登录
    @classmethod
    def setUpClass(cls):  # 每个测试类里面去运行的操作放到类方法里面
        cls.request = request_1.req() # 实例化对象
                                        #在类里面使用session
    def tearDown(self):
        logger.info('__用例执行结束__')

    @data(*cases_2)
    def test_withdraw(self,item):
        logger.info('__开始第{0}条用例__'.format(item.case_id))
        logger.info('title:{0}'.format(item.case_title))

    # 读取配置文件获取url
    #     cf = r_conf.ReadConfig(route.read_conf())
    #     get_api =cf.get_value('api', 'pre_url')
    #     url_1 = str(get_api+item.case_url)

        res = self.request.reque(url=item.case_url, param=item.case_data, met=item.case_method)
        logger.info(item.case_url)
        logger.info(item.case_method)
        logger.info(item.case_data)
        result_1 = res.json()['code']
        expect_1 = json.loads(item.case_expect)['code']
        result_2=res.json()['msg']
        expect_2=json.loads(item.case_expect)['msg']
        result_3 = res.json()['status']
        expect_3 = json.loads(item.case_expect)['status']

        result=res.text
        try:
            self.assertEqual(expect_1,result_1)
            self.assertEqual(expect_2, result_2)
            self.assertEqual(expect_3, result_3)
            logger.info('执行通过')
            read.write_data('withdraw',item.case_id+1,result,'pass')
        except AssertionError as e:
            logger.error('执行出错：{0}'.format(e))
            read.write_data('withdraw',item.case_id + 1, result, 'fall')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.request.close()  # 关闭session
if __name__ == '__main__':
    unittest.main()