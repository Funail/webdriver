#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import unittest,time
# 引入HTMLTestRunner包
import HTMLTestRunner

# 导入公共的类
from package import common
from package import function
from package import m1_member
from data import testdata


class TestMember(unittest.TestCase):
    u'''会员管理'''
    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)


    def test01_member_shopname(self):

        u'''会员管理店铺名称筛选'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver,u"会员功能",u"会员管理")
        time.sleep(2)

        # 全部门店会员数判断
        m1_member.member_shopname_filter(self.driver, u"全部")
        time.sleep(2)
        member_list = common.findXpath(self.driver,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div").text
        self.assertTrue(member_list != "")
        self.driver.refresh()
        time.sleep(2)

        # 分店门店会员数判断
        m1_member.member_shopname_filter(self.driver, u"测试员工测试")
        time.sleep(2)
        member_list = common.findXpath(self.driver,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div").text
        self.assertTrue(member_list != "")
        self.driver.refresh()
        time.sleep(2)

        m1_member.member_shopname_filter(self.driver, u"业务员:二级业务员测试无默认")
        time.sleep(2)
        member_list = common.findXpath(self.driver,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div").text
        self.assertTrue(member_list != "")
        self.driver.refresh()
        time.sleep(2)

        m1_member.member_shopname_filter(self.driver, u"测试分店")
        time.sleep(2)
        member_list = common.findXpath(self.driver,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/span").text
        self.assertEqual(member_list,u"暂无数据")
        time.sleep(2)

        function.logout(self.driver)


    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()
