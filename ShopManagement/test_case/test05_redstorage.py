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
from package import m4_redstorage
from data import testdata


class TestRedstorage(unittest.TestCase):
    u'''会员储值'''

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)

    def test01_creat_redstorage(self):

        u'''创建会员储值'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员储值")
        time.sleep(2)

        common.findCss(self.driver,"body > div.top_content > div.main > div:nth-child(2) > div > div.panel > div.panel-header > div > div.panel-select__wrapper > div > div.el-input.el-input--small > input").click()
        time.sleep(1)
        common.findXpath(self.driver,"/html/body/div[3]/div/div[1]/ul/li[3]").click()
        time.sleep(2)
        get_redstorage_count = common.findsCss(self.driver,"#memberstorage > div.el-table__body-wrapper > table > tbody > tr")
        if len(get_redstorage_count) ==1 :
            self.driver.refresh()
            time.sleep(2)
            m4_redstorage.end_redstorage(self.driver)
        else:
            self.driver.refresh()
        self.driver.refresh()
        time.sleep(2)
        m4_redstorage.creat_redstorage(self.driver, testdata.dict6)
        time.sleep(2)

        redstorage_status = common.findCss(self.driver,"#memberstorage > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_2 > div").text
        self.assertEqual(redstorage_status,u"进行中")

        function.logout(self.driver)


    def test02_end_redstorage(self):

        u'''终止会员储值活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员储值")

        m4_redstorage.end_redstorage(self.driver)
        end_redpoint_status = common.findCss(self.driver,"#memberstorage > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_2 > div").text
        self.assertEqual(end_redpoint_status,u"已终止")

        function.logout(self.driver)


    def test03_redstorage_member(self):

        u'''储值会员页面'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员储值")

        m4_redstorage.redstorage_member(self.driver)
        time.sleep(2)

        function.logout(self.driver)

    def test04_redstorage_bill(self):

        u'''储值账单页面'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员储值")

        m4_redstorage.redstorage_bill(self.driver)
        time.sleep(2)

        function.logout(self.driver)


    def tearDown(self):
        driver = self.driver
        # driver.close()


if __name__=='__main__':
    unittest.main()
