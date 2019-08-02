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
from ddt import ddt,data
from common import ms_read
import json
import random
from common import logg


logger=logg.logger('reg')
read = do_excel.doExcel(route.exc_1)
cases_2 = read.get_data('reg')
@ddt
class TestReg(unittest.TestCase):                               #测试注册
    @classmethod
    def setUpClass(cls):  # 每个测试类里面去运行的操作放到类方法里面
        cls.request = request_1.req() # 实例化对象
                                                # 在类里面使用session
        cls.ms=ms_read.MSql(result_dict=True)

    def tearDown(self):
        logger.info('__用例执行结束__')

    @data(*cases_2)
    def test_reg(self,item):
        logger.info('__开始第{0}条用例__'.format(item.case_id))
        logger.info('title:{0}'.format(item.case_title))

    #读取手机号，取新号注册
        item.case_data = json.loads(item.case_data)
        # phone_max = self.ms.read_base('select max(mobilephone) from future.member')[0]
        if item.case_data['mobilephone'] == "${mobile phone}":
            # item.case_data['mobilephone'] = str(int(phone_max) + 1)
            item.case_data['mobilephone']=str(13730000000+random.randint(1000000,9999999))
        # print(item.case_data['mobilephone'])


    # 读取配置文件获取url
    #     cf = r_conf.ReadConfig(route.read_conf())
    #     get_api =cf.get_value('api', 'pre_url')
    #     url_1 = str(get_api+item.case_url)

        res =self.request.reque(url=item.case_url, param=item.case_data, met=item.case_method)
        logger.info(item.case_url)
        logger.info(item.case_method)
        logger.info(item.case_data)
        result=res.text
        expect=item.case_expect
        try:
            if res.json()['msg']=='注册成功':
                print(item.case_data['mobilephone'])
                sql_1 = 'select * from future.member where MobilePhone={0}'.format(item.case_data['mobilephone'])
                results=self.ms.fetch_all(sql_1)
                print(sql_1)
                print(results)
                self.assertEqual(1,len(results))
                self.assertEqual(0,results[0]['LeaveAmount'])
            else:
                self.assertEqual(expect,result)
            logger.info('执行通过')
            read.write_data('reg',item.case_id+1,result,'pass')
        except AssertionError as e:
            logger.error('执行出错：{0}'.format(e))
            read.write_data('reg',item.case_id + 1, result, 'fall')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.request.close()
if __name__ == '__main__':
    unittest.main()
    # w = r_conf.ReadConfig(route.read_conf())
    # y = w.get_value('api', 'pre_url')
    # x = y.join(item.case_url)
    # print(x)