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

class Test03(unittest.TestCase):

    # 初始化变量
    site = "https://qudao.qa.qfpay.net"
    username = "14700001237"
    password = "237018"
    slsm_id = "11754"
    slsm_name = u"李巍"
    mobile = "13545454545"

    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        #self.browser.maximize_window()
        time.sleep(1)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_search_salesman_by_id(self):
        print "业务员管理：执行测试用例01"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"业务员管理", u"业务员管理")

        # 根据业务员编号查询
        common.salesman.search_by_salesman_id(self.browser, self.slsm_id)
        self.assertEqual(1, common.salesman.get_results_count(self.browser), "根据业务员编号，查询结果错误！")
        self.assertEqual(self.slsm_id, common.salesman.get_salesman_id(self.browser, 1), "根据业务员编号，查询结果错误！")

        common.common.logout(self.browser)

    def test02_search_salesman_by_name(self):
        print "业务员管理：执行测试用例02"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"业务员管理", u"业务员管理")

        # 根据业务员名称查询
        common.salesman.search_by_salesman_name(self.browser, self.slsm_name)
        self.assertEqual(1, common.salesman.get_results_count(self.browser), "根据业务员名称，查询结果错误！")
        self.assertEqual(self.slsm_name, common.salesman.get_salesman_name(self.browser, 1), "根据业务员名称，查询结果错误！")

        common.common.logout(self.browser)

    def test03_search_salesman_by_mobile(self):
        print "业务员管理：执行测试用例03"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"业务员管理", u"业务员管理")

        # 根据手机号查询
        common.salesman.search_by_salesman_mobile(self.browser, self.mobile)
        self.assertEqual(self.mobile, common.salesman.get_salesman_mobile(self.browser, 1), "根据业务员名称，查询结果错误！")

        common.common.logout(self.browser)

    def test04_search_salesman_by_status(self):
        print "业务员管理：执行测试用例04"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"业务员管理", u"业务员管理")

        # 根据业务员状态查询
        # 在职
        common.salesman.search_by_salesman_status(self.browser, u"在职")
        if not common.salesman.get_results_count(self.browser) == 0:
            self.assertEqual(u"在职", common.salesman.get_salesman_status(self.browser, 1), "根据业务员状态，查询结果错误！")
        else:
            print "根据业务员状态'在职'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 离职
        common.salesman.search_by_salesman_status(self.browser, u"离职")
        if not common.salesman.get_results_count(self.browser) == 0:
            self.assertEqual(u"离职", common.salesman.get_salesman_status(self.browser, 1), "根据业务员状态，查询结果错误！")
        else:
            print "根据业务员状态'在职'，没有查询到任何结果，请手工再次检查！"

        common.common.logout(self.browser)

    def test05_download_salesman_list(self):
        print "业务员管理：执行测试用例05"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"业务员管理", u"业务员管理")
        common.salesman.download_salesman_list(self.browser)
        common.common.logout(self.browser)





    if __name__ == "__main__":
        unittest.main()