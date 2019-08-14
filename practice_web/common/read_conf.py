#-*-coding:utf-8-*-
# @time     :2019/7/29/029 11:56
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :read_conf.py
# @Sofeware :将环境放进配置文件

from configparser import ConfigParser
from common import route

class Config:
    def __init__(self):
        self.cfg=ConfigParser()
        self.cfg.read(route.g_conf)
        if self.cfg.get('onto','switch'):
            self.cfg.read(route.en1_conf)
        else:
            self.cfg.read(route.en2_conf)

    def get_value(self,section,option):
        return self.cfg.get(section,option)

