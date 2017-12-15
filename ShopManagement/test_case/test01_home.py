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


class TestHome(unittest.TestCase):
    u'''首页'''
    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)


    def test01_home(self):

        u'''首页概览'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)

        # 断言判断登录后导航栏首页概览
        homepage = common.findXpath(self.driver, '/html/body/div[1]/div[1]/ul/li[1]/a').text
        self.assertEqual(homepage, "首页概览")

    def test02_menu(self):

        u'''左侧菜单检查'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)

        self.assertEqual(function.get_menu_count(self.driver),6)
        self.assertEqual(function.get_member_menu_count(self.driver),4)

        function.logout(self.driver)


    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()