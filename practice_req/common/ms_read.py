#-*-coding:utf-8-*-
# @time     :2019/7/12/012 17:33
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :ms_read.py
# @Sofeware :PyCharm Community Edition


import pymysql
from conf.r_conf  import ReadConfig
from common import route
import pymysql.cursors


class MSql:                        #调用数据库
    def __init__(self,result_dict=False):
    # def __init__(self):
        y=ReadConfig(route.read_conf())
        host=y.get_value('db','host')
        user=y.get_value('db','user')
        password=y.get_value('db','pwd')
        port=int(y.get_value('db','port'))
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        if result_dict:
            self.curser=self.mysql.cursor(pymysql.cursors.DictCursor)
        else:
            self.curser = self.mysql.cursor()
    def fetch_one(self,sql):
        self.curser.execute(sql)         #读取sql语句
        result=self.curser.fetchone()       #返回结果
        return result
    def fetch_all(self,sql):
        self.curser.execute(sql)         #读取sql语句
        result=self.curser.fetchall()       #返回结果
        return result
    def close(self):
        self.curser.close()
        self.mysql.close()
if __name__ == '__main__':
    from common import context
    # t=MSql()
    t=MSql(result_dict=True)
    # loan_member_id = getattr(context.re_json, 'loan_member_id')
    # print(loan_member_id)
    sql='SELECT * FROM future.loan WHERE ID = 102132 ORDER BY CreateTime DESC LIMIT 1;'
    print(sql)
    y=t.fetch_all(sql)
    # print(type(y[0]))
    print(y)
