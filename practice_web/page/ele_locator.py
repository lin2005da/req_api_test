#-*-coding:utf-8-*-
# @time     :2019/7/31/031 9:49
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :ele_locator.py
# @Sofeware :PyCharm Community Edition
from selenium.webdriver.common.by import By as by
class locator:
    #login
    phone_locator=(by.NAME,'phone')
    pwd_locator=(by.NAME,'password')
    correct_locator=(by.XPATH,'//div[@class="layui-layer-content"]')
    errormsg_locator=(by.CLASS_NAME,'form-error-info')
    successlogin_locator = (by.XPATH,' // a / img[ @class ="mr-5"] /..')
    #bid
    option_locator = (by.XPATH,'//div[@class="graph"]//a[contains(@class,"btn btn-special")]')
    invest_locator = (by.XPATH,'//input[contains(@class,"invest-unit-investinput")]')
    button_locator =(by.XPATH, '//button[contains(@class,"height_style")]')
    successbid_locator=(by.XPATH,'//div[@id="layui-layer1"]//div[contains(@class,"capital_font1")]')
    up_locator=(by.XPATH,'//ul/li[@class="color_sub"]')
    btn_locator=(by.XPATH,'//div[@class="layui-layer-content"]//button')
