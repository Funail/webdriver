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

        member.member_shopname_filter(self.driver,u"测试员工测试")
        member.member_shopname_filter(self.driver,u"测试分店")
        member.member_shopname_filter(self.driver,u"全部")

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()
