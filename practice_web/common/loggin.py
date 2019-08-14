#-*-coding:utf-8-*-
# @time     :2019/7/29/029 15:21
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :loggin.py
# @Sofeware :PyCharm Community Edition
import logging
import logging.handlers
from common import route
import os
class logg:
    def __init__(self):
        self.log=logging.getLogger('web')
        self.log.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-line:%(lineno)d-日志信息:%(message)s')

        #文件日志
        file_log=logging.handlers.RotatingFileHandler(filename=route.f_log, maxBytes=20*1024*1024, backupCount=10, encoding='utf_8')
        file_log.setLevel('INFO')
        file_log.setFormatter(formatter)
        self.log.addHandler(file_log)

        #console日志
        stream_log=logging.StreamHandler()
        stream_log.setLevel('DEBUG')
        stream_log.setFormatter(formatter)
        self.log.addHandler(stream_log)
    def get_info(self,msg):
        return self.log.info(msg)
    def get_warning(self,msg):
        return self.log.warning(msg)
    def get_debug(self,msg):
        return self.log.debug(msg)
    def get_error(self,msg):
        return self.log.error(msg)
    def get_critical(self,msg):
        return self.log.critical(msg)