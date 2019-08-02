#-*-coding:utf-8-*-
# @time     :2019/7/10/010 11:23
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :prac.py
# @Sofeware :PyCharm Community Edition
import requests
class reqq:
    def __init__(self):
        self.session=requests.session()#创建一个session，将res的cookie保存下来
    def login(self,phone,pwd):
        url_1='http://test.lemonban.com/futureloan/mvc/api/member/login'

        data_1={"mobilephone":phone,"pwd":pwd}

        res=self.session.post(url=url_1,params=data_1)

        print(res.json())
        return res
    def recharge(self,user,amount):
        url_2='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
        data_2={"mobilephone":user,"amount":amount}

        req=self.session.request(method='get',url=url_2,params=data_2)#调用同一个session，引用cookie可以执行同一账号的后续操作

        print(req.text)
        return req
# s=reqq()
# s.login("13653204562","111111")
# s.recharge('13653204562','50000')
# t=reqq()                            #不同session之间，  cookie不共享
# t.recharge('136252316241','500000')
# self.session=requests.session()#创建一个session，将res的cookie保存下来

# url_1='http://test.lemonban.com/futureloan/mvc/api/member/login'
# phone="13653204562"
# pwd="111111"
#
# data_1={"mobilephone":phone,"password":pwd}
# print(type(data_1))

# res=requests.post(url='http://test.lemonban.com/futureloan/mvc/api/member/register',data={"mobilephone":"13653204562","pwd":"111111"})
# #
# print(res.request.url)
# print(res.request.body)
# print(res.request.headers)
# # print(res.)
# # # print(data_1)
data = {'mobilephone':'15810447656',"pwd":"123456"}
resp =requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)  # data 表单 传参
print('请求url',resp.request.url)
print('请求参数',resp.request.body)
print('请求headers',resp.request.headers)
print('请求cookies',resp.request._cookies)
print('响应码', resp.status_code)
print('响应信息', resp.text)
print('响应cookies',resp.cookies) # 响应cookies是一个对象
print('响应headers',resp.headers)
