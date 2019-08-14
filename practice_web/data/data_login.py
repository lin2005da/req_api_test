#-*-coding:utf-8-*-
# @time     :2019/7/29/029 19:01
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :data_login.py
# @Sofeware :PyCharm Community Edition
#登录成功
user_correct=[{"phone":"18684720553","password":"python"}]
#登录失败

user_error=[{"phone":"18684720553","password":"","expected":"请输入密码"},{"phone":"","password":"python","expected":"请输入手机号"},{"phone":"1868473","password":"python","expected":"请输入正确的手机号"},{"phone":"aaaaaaa","password":"python","expected":"请输入正确的手机号"}]
#未注册登录
# //div[@class="layui-layer-content"]
user_unthour=[{"phone":"18684720552","password":"python","expected":"此账号没有经过授权，请联系管理员!"},{"phone":"18684720553","password":"on","expected":"帐号或密码错误!"}]
# user_unthour=[{"phone":"18684720553","password":"on","expected":"帐号或密码错误!"}]
