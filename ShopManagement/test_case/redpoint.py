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
from package import member
from data import testdata


class TestRedpoint(unittest.TestCase):
    u'''会员集点'''

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)

    def test01_redpoint_status(self):

        u'''会员集点活动状态筛选'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver,u"会员功能",u"会员集点")

        member.redpoint_status(self.driver,u"未开始")
        member.redpoint_status(self.driver,u"进行中")
        member.redpoint_status(self.driver,u"已结束")
        member.redpoint_status(self.driver,u"已终止")
        member.redpoint_status(self.driver,u"全部")

    def test02_redpoint_shopname(self):

        u'''会员集点店铺名称筛选'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        member.redpoint_shopname_filter(self.driver, u"测试员工测试")
        member.redpoint_shopname_filter(self.driver, u"测试分店")
        member.redpoint_shopname_filter(self.driver, u"全部")

    def test03_creat_redpoint(self):

        u'''创建集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        member.creat_redpoint(self.driver,testdata.dict1)
        time.sleep(1)

    def test04_edit_redpoint(self):

        u'''修改集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        member.edit_redpoint(self.driver,testdata.dict1)


    def test05_end_redpoint(self):

        u'''停止集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        member.end_redpoint(self.driver)

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()
