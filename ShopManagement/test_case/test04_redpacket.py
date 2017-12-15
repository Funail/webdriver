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
from package import redpacket
from data import testdata


class TestRedpacket(unittest.TestCase):
    u'''会员红包'''

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)

    def test01_creat_redpacket_common(self):

        u'''创建会员通知'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员红包")

        if common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div"):
            creat_time1 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        redpacket.creat_redpacket_common(self.driver,testdata.dict3)
        time.sleep(2)
        creat_time2 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        self.assertTrue(creat_time1 < creat_time2)


    def test02_creat_redpacket_payment(self):

        u'''创建消费返红包'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员红包")

        if common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div"):
            creat_time1 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        redpacket.creat_redpacket_payment(self.driver,testdata.dict4)
        time.sleep(2)
        creat_time2 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        self.assertTrue(creat_time1 < creat_time2)


    def test03_creat_redpacket_share(self):

        u'''创建分享红包'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员红包")

        if common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div"):
            creat_time1 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        redpacket.creat_redpacket_share(self.driver,testdata.dict5)
        time.sleep(2)
        creat_time2 = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_1 > div").text
        self.assertTrue(creat_time1 < creat_time2)


    def test04_end_redpacket(self):

        u'''终止红包活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员红包")

        redpacket.end_redpacket(self.driver)
        end_redpoint_status = common.findCss(self.driver,"#memberredpacket > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_4 > div").text
        self.assertEqual(end_redpoint_status,u"已失效")

        function.logout(self.driver)


    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()
