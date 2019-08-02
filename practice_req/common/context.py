#-*-coding:utf-8-*-
# @time     :2019/7/18/018 8:08
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :context.py
# @Sofeware :PyCharm Community Edition
import re
from conf import r_conf
from common import route
#s是字符串
#t是字典
# 便利字符串，查找相关的关键字
# 取出关键字，根据关键字在t中取值
class re_json:
    #管理员
    admin_user = r_conf.ReadConfig(route.read_conf()).get_value('data','admin_user')
    admin_pwd = r_conf.ReadConfig(route.read_conf()).get_value('data','admin_pwd')
    #项目人
    loan_user = r_conf.ReadConfig(route.read_conf()).get_value('data','loan_user')
    loan_pwd = r_conf.ReadConfig(route.read_conf()).get_value('data','loan_pwd')
    loan_member_id = r_conf.ReadConfig(route.read_conf()).get_value('data', 'loan_member_id')
    #普通用户
    member_user = r_conf.ReadConfig(route.read_conf()).get_value('data','member_user')
    member_pwd = r_conf.ReadConfig(route.read_conf()).get_value('data','member_pwd')
    member_id = r_conf.ReadConfig(route.read_conf()).get_value('data','member_id')



def str_re(s):
    d="\$\{(.*?)}"
    while re.search(d,s):       #结果非空
        r=re.search(d,s)        #关键字查找
        key=r.group(1)          #获取关键字
        if hasattr(re_json,key):#模块中含有key
            w=getattr(re_json,key)#取值
            s=re.sub(d,w,s,count=1)#替换
        else:
            return None
    return s
if __name__ == '__main__':
    from common import  ms_read
    ms=ms_read.MSql()
    s='{"id":"${loan_id}","status":"1"}'
    loan_member_id = getattr(re_json, 'loan_member_id')
    sql = 'SELECT Id from future.invest    ORDER BY CreateTime DESC LIMIT 1'.format(loan_member_id)
    x = ms.read_base(sql)[0]
    setattr(re_json, 'loan_id', str(x))
    print(str_re(s))


