# coding:utf-8
import unittest
from selenium import webdriver
import sys
import time
sys.path.append("/Users/liuchang/PycharmProjects/common")
import common.common
import common.qudao
import common.shanghu
import common.salesman
import common.trade
import common.notifications
import common.training
import random

class Test06(unittest.TestCase):

    # 初始化变量
    site_mis = "https://qdmis.qa.qfpay.net"
    username_mis = "14700000291"
    password_mis = "000291"
    site = "https://qudao.qa.qfpay.net"
    username = "14700001237"
    password = "237018"
    training_name = u"培训资料" + str(random.randint(0, 9999)).zfill(4)
    training_link = "https://www.baidu.com/"
    training_content = u"培训资料: " + "\n" + u"这是一条测试数据，请忽略！"

    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        #self.browser.maximize_window()
        time.sleep(1)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_create_training(self):
        print "培训资料：执行测试用例01"
        common.common.login_mis(self.browser, self.site_mis, self.username_mis, self.password_mis)
        common.common.open_menu_mis(self.browser, u"培训资料", u"培训资料")
        common.training.create_training(self.browser, self.training_name, self.training_link, self.training_content)
        common.common.logout_mis(self.browser)

        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"培训资料", u"培训资料")
        self.assertTrue(common.training.find_training_by_title(self.browser, self.training_name), "培训资料创建失败！")
        common.common.logout(self.browser)

    def test02_search_training(self):
        print "培训资料：执行测试用例02"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"培训资料", u"培训资料")
        common.training.search_training_by_title(self.browser, self.training_name)
        self.assertTrue(common.training.find_training_by_title(self.browser, self.training_name), "培训资料查询失败！")
        common.common.logout(self.browser)

    def test03_check_training_content(self):
        print "培训资料：执行测试用例03"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"培训资料", u"培训资料")
        url = common.training.open_training_content(self.browser, self.training_name, self.training_link)
        self.assertEqual(self.training_link, url, "培训资料链接错误！")
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(2)
        common.training.close_training_content(self.browser)
        common.common.logout(self.browser)

    def test04_delete_training(self):
        print "培训资料：执行测试用例04"
        common.common.login_mis(self.browser, self.site_mis, self.username_mis, self.password_mis)
        common.common.open_menu_mis(self.browser, u"培训资料", u"培训资料")
        common.training.delete_training_by_title(self.browser, self.training_name)
        common.common.logout_mis(self.browser)

        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"培训资料", u"培训资料")
        self.assertFalse(common.training.find_training_by_title(self.browser, self.training_name), "培训资料删除失败！")
        common.common.logout(self.browser)





    if __name__ == "__main__":
        unittest.main()