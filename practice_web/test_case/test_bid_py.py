#-*-coding:utf-8-*-
# @time     :2019/7/29/029 12:16
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :test_login.py
# @Sofeware :PyCharm Community Edition

import pytest
from page import asserty_index
from data import data_bid


class TestBid_ok:
    @pytest.mark.userfixture('baselogin')
    @pytest.mark.parametrize('case',data_bid.bid_ok)
    @pytest.mark.smoke
    def test_bid_success(self,baselogin,case):
        bid_page,driver=baselogin
        ori=bid_page.ori_money()#投资前金额
        print(ori)
        bid_page.invest_send(case['pay'])
        bid_page.submit_click()
        bid_ele=asserty_index.index(driver).success_bidinfo
        #校验成功
        assert case['expected'] == bid_ele.text
        bid_page.btn_click()
        later=bid_page.up_money()#投资成功后金额
        print(later)
        up=ori-later
        print(up)
        #校验前后金额
        assert (float(case['pay'])==up)



        #校验投资记录??

if __name__ == '__main__':
    pytest.main()