#-*-coding:utf-8-*-
# @time     :2019/7/12/012 17:37
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :r_conf.py
# @Sofeware :PyCharm Community Edition
from configparser import ConfigParser
class ReadConfig:
    def __init__(self,file):
        self.cf=ConfigParser()
        self.cf.read(file,encoding='utf_8')
    def get_value(self,section,option):
        return self.cf.get(section,option)
    def get_int(self,section,option):
        return self.cf.getint(section,option)
    def get_fload(self,section,option):
        return self.cf.getfloat(section,option)
    def get_booloan(self,section,option):
        return self.cf.getboolean(section,option)


# if __name__ == '__main__':


#直接读取配置开关，    可取代读取路径
    # from common import route
    #
    # # 在配置文件模块
    # *配置文件
    # global.conf——
    # *[fi]
    # *switch = True
    #
    # cf = os.path.join(route.r_dir, 'conf')
    # conf_global = os.path.join(cf, 'global.conf')  # 总开关  决定都哪个配置文件
    # conf_1 = os.path.join(cf, 'sql_1.conf')  # 开关1
    # conf_2 = os.path.join(cf, 'sql_2.conf')  # 文件2
    #
    #
    #
    # class ReadConfig:
    #     def __init__(self):
    #         self.cf = ConfigParser()
    #         self.cf.read(conf_global, encoding='utf_8')
    #         x=self.cf.getboolean('fi','switch')
    #         if x:
    #             self.cf.read(conf_1)
    #         else:
    #             self.cf.read(conf_2)
    #     def get_value(self, section, option):
    #         return self.cf.get(section, option)