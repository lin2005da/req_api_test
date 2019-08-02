#-*-coding:utf-8-*-
# @time     :2019/7/10/010 16:19
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :request_1.py
# @Sofeware :封装http
import requests
from conf import r_conf
from common import route
class req:
    def __init__(self):
        self.session=requests.sessions.session()
    def reque(self,url,met,param=None):
        # 读取配置文件获取url               取代在用例中连接url
        cf = r_conf.ReadConfig(route.read_conf())
        get_api = cf.get_value('api', 'pre_url')
        url_1 = get_api + url
        print(url_1)
        method_1=met.upper()
        print((method_1))
        if param is not None and type(param) == str:
            param_1=eval(param)
        else:
            param_1=param
        if method_1 =='GET':
            res=self.session.get(url=url_1,params=param_1)
        elif method_1 == 'POST':
            res=self.session.post(url=url_1,data=param_1,headers={'Content-Type':'application/x-www-form-urlencoded'})
                                                    #POST,设置content-type为application/x-www-form-urlencoded,会自动编码
            print(res.json())
        else:
            print('http请求方法错误')
            res='http请求方法{0}错误'.format(met)
        return res
    def close(self):
        self.session.close()

if __name__ == '__main__':
    # from  common import do_excel
    # from common import route
    # x=do_excel.doExcel(route.exc_1)
    # t=x.get_data('login')
    # for i in t:
    #     print(i.case_method)
    #     # url = 'http://test.lemonban.com/futureloan/mvc/api' + i.case_url
    #     # print(url)
    #     q=req()
    #     x=q.reque(url=i.case_url,met='post',param=i.case_data)
    #     print(x.headers)
    #     # print(t['Content-Type']='application/x-www-form-urlencoded')
    #     # print(t)
    #
    url="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
    method='post'
    data='{"client_ip":"10.10.3.26","tmpl_id":"1","mobile":"13652325623"}'
    t=req().reque(url=url,met=method,param=data)
    print(t.text)
