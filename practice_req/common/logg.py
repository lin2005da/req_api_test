#-*-coding:utf-8-*-
# @time     :2019/7/18/018 15:14
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :logg.py
# @Sofeware :PyCharm Community Edition

import logging
import logging.handlers
from common import route
import os
from conf import r_conf
from common import route
def logger(file_name):
    loger=logging.getLogger(file_name)
    loger.setLevel('DEBUG')
    fmatt='%(asctime)s-%(levelname)s-line:%(lineno)d-[日志信息]:%(message)s'
    formatter=logging.Formatter(fmatt)

    file_name=os.path.join(route.log_dir,file_name)#添加文件路径
    f_handle=logging.handlers.RotatingFileHandler(filename=file_name, maxBytes=20*1024*1024, backupCount=10, encoding='utf_8')

    Config=r_conf.ReadConfig(route.read_conf())
    #文件日志
    f_handle.setLevel(Config.get_value('log','file_handler'))
    f_handle.setFormatter(formatter)
    loger.addHandler(f_handle)
    #控制台日志
    s_handle=logging.StreamHandler()
    s_handle.setFormatter(formatter)
    s_handle.setLevel(Config.get_value('log','console_handler'))
    loger.addHandler(s_handle)

    return loger
