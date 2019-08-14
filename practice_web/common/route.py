#-*-coding:utf-8-*-
# @time     :2019/7/29/029 11:58
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :route.py
# @Sofeware :PyCharm Community Edition

import os
import time
r_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

common_dir=os.path.dirname(os.path.abspath(__file__))

conf_dir=os.path.join(r_dir,'conf')
g_conf=os.path.join(conf_dir,'global.conf')
en1_conf=os.path.join(conf_dir,'en_1.conf')
en2_conf=os.path.join(conf_dir,'en_2.conf')

data_dir=os.path.join(r_dir,'data')

log_dir=os.path.join(r_dir,'log')
png_log=os.path.join(log_dir,'{0}.png'.format(time.time()))
f_log=os.path.join(log_dir,'web.log')

result_dir=os.path.join(r_dir,'result')
xml_result=os.path.join(result_dir,'r.xml')
log_result=os.path.join(result_dir,'result.txt')
html_result=os.path.join(result_dir,'result.html')