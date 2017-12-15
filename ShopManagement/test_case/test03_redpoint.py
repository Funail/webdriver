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
from package import m2_redpoint
from data import testdata


class TestRedpoint(unittest.TestCase):
    u'''会员集点'''

    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280,800)
        # 设置隐式时间等待
        self.driver.implicitly_wait(5)

    def test01_creat_redpoint(self):

        u'''创建集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        m2_redpoint.redpoint_status(self.driver, u"进行中")
        time.sleep(1)
        if m2_redpoint.get_redpoint_count(self.driver) ==1 :
            self.driver.refresh()
            m2_redpoint.end_redpoint(self.driver)
        self.driver.refresh()
        time.sleep(2)

        m2_redpoint.creat_redpoint(self.driver, testdata.dict1)
        time.sleep(2)

        # 判断创建的集点活动
        common.findXpath(self.driver,"/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/i").click()
        common.findXpath(self.driver,"/html/body/div[5]/div/div[1]/ul/li[3]").click()
        time.sleep(2)
        redpoint_check_count = common.findsCss(self.driver,"#memberredcollect > div.el-table__body-wrapper > table > tbody > tr")
        self.assertEqual(len(redpoint_check_count),1)

        function.logout(self.driver)


    def test02_redpoint_status(self):

        u'''会员集点活动状态筛选'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver,u"会员功能",u"会员集点")

        # 未开始
        m2_redpoint.redpoint_status(self.driver, u"未开始")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_count(self.driver), 0)
        self.driver.refresh()
        time.sleep(2)

        # 进行中
        m2_redpoint.redpoint_status(self.driver, u"进行中")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_count(self.driver), 1)
        self.driver.refresh()
        time.sleep(2)

        # 已结束
        m2_redpoint.redpoint_status(self.driver, u"已结束")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_count(self.driver), 4)
        self.driver.refresh()
        time.sleep(2)

        # 全部活动
        m2_redpoint.redpoint_status(self.driver, u"已终止")
        time.sleep(1)
        end_redpoint_count = m2_redpoint.get_redpoint_count(self.driver)
        self.driver.refresh()
        time.sleep(2)
        m2_redpoint.redpoint_status(self.driver, u"全部")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_count(self.driver), end_redpoint_count + 5)

        function.logout(self.driver)

    def test03_redpoint_shopname(self):

        u'''会员集点店铺名称筛选'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        m2_redpoint.redpoint_status(self.driver, u"已结束")
        m2_redpoint.redpoint_shopname_filter(self.driver, u"测试员工测试")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_shopname_count(self.driver), 3)
        self.driver.refresh()
        time.sleep(2)

        m2_redpoint.redpoint_status(self.driver, u"已结束")
        m2_redpoint.redpoint_shopname_filter(self.driver, u"测试分店")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_shopname_count(self.driver), 1)
        self.driver.refresh()
        time.sleep(2)

        m2_redpoint.redpoint_status(self.driver, u"已结束")
        m2_redpoint.redpoint_shopname_filter(self.driver, u"业务员:二级业务员测试无默认")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_shopname_count(self.driver), 0)
        self.driver.refresh()
        time.sleep(2)

        m2_redpoint.redpoint_status(self.driver, u"已结束")
        m2_redpoint.redpoint_shopname_filter(self.driver, u"全部")
        time.sleep(1)
        self.assertEqual(m2_redpoint.get_redpoint_shopname_count(self.driver), 4)
        self.driver.refresh()
        time.sleep(2)

        function.logout(self.driver)


    def test04_edit_redpoint(self):

        u'''修改集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        m2_redpoint.edit_redpoint(self.driver, testdata.dict2)
        time.sleep(2)
        edit_redpoint_text = common.findCss(self.driver,"#memberredcollect > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_3 > div > span").text
        self.assertEqual(edit_redpoint_text,u"满5点可兑换泰迪狗一份")

        function.logout(self.driver)


    def test05_end_redpoint(self):

        u'''停止集点活动'''
        function.login_shanghu(self.driver, testdata.login_url, testdata.username, testdata.password)
        time.sleep(2)
        function.open_menu(self.driver, u"会员功能", u"会员集点")

        m2_redpoint.end_redpoint(self.driver)
        end_redpoint_status = common.findCss(self.driver,"#memberredcollect > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_4 > div").text
        self.assertEqual(end_redpoint_status,u"已终止")

        function.logout(self.driver)

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__=='__main__':
    unittest.main()
