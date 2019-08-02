#-*-coding:utf-8-*-
# @time     :2019/7/11/011 9:50
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :route.py
# @Sofeware :PyCharm Community Edition
import os
from conf import r_conf
# r=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#[Errno 2] No such file or directory: 'E:\\Python_auto\\practice_req\\data\\proc_data.xlsx'
                                                              #os.path.realpath 属于软链接，无法读取路径内容
r_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#os.path.abspath 读取的是文件的绝对路径，能够读取内容

data_dir=os.path.join(r_dir,'data')
exc_1=os.path.join(data_dir,'su_data.xlsx')#excel相对路径

test_result = os.path.join(r_dir,'test_result')
html_dir=os.path.join(test_result,'html_report')
html_file=os.path.join(html_dir,'web.html')


log_dir=os.path.join(test_result,'log')
# print(log_dir)

test_case=os.path.join(r_dir,'test_case')

def read_conf():        #读取配置文件
    cf = os.path.join(r_dir, 'conf')
    conf_global = os.path.join(cf, 'global.conf')#总开关  决定都哪个配置文件
    conf_1 = os.path.join(cf, 'sql_1.conf')#开关1
    conf_2 = os.path.join(cf, 'sql_2.conf')#文件2

    t=r_conf.ReadConfig(conf_global).get_value('fi','switch')   #取值
    if t == '1':            #将连接路径替换为configparser.read,可直接读取配置文件
        x_conf = conf_1
    elif t == '2':
        x_conf = conf_2
    return x_conf       #返回配置文件路径    ms_read、用例request
# print(read_conf())




