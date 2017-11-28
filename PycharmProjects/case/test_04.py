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

class Test04(unittest.TestCase):

    # 初始化变量
    site = "https://qudao.qfpay.com"
    username = "14777772223"
    password = "000006"
    merchant_name = u"小微商户测试用请忽略"
    mobile = "14700090011"
    serial_number = "20171116000100020000942107"
    order_number = "1507780696"
    salesman_name = u"刘畅"
    # 用于test01_search_by_time
    start_trade_date = "2017-11-16"
    start_trade_time = "00:00:00"
    end_trade_date = "2017-11-16"
    end_trade_time = "23:59:59"
    # 用于其他case
    start_trade_date2 = "2017-11-01"
    start_trade_time2 = "00:00:00"
    end_trade_date2 = "2017-11-17"
    end_trade_time2 = "23:59:59"

    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        #self.browser.maximize_window()
        time.sleep(1)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_search_by_time(self):
        print "交易管理：执行测试用例01"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date, self.start_trade_time, self.end_trade_date, self.end_trade_time)
        trade_date = common.trade.get_trade_time(self.browser, 1).split(' ')[0]
        self.assertTrue((self.start_trade_date == trade_date) or (self.end_trade_date == trade_date), "根据交易时间，查询结果错误！")
        common.common.logout(self.browser)

    def test02_search_by_merchant_name(self):
        print "交易管理：执行测试用例02"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_trade_by_merchant_name(self.browser, self.merchant_name)
        self.assertEqual(self.merchant_name, common.trade.get_merchant_name(self.browser, 1), "根据商户名称，查询结果错误！")
        common.common.logout(self.browser)

    def test03_search_by_mobile(self):
        print "交易管理：执行测试用例03"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_trade_by_mobile(self.browser, self.mobile)
        self.assertEqual(self.mobile, common.trade.get_mobile_number(self.browser, 1), "根据手机号，查询结果错误！")
        common.common.logout(self.browser)

    def test04_search_by_serial_number(self):
        print "交易管理：执行测试用例04"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_trade_by_serial_number(self.browser, self.serial_number)
        self.assertEqual(1, common.trade.get_results_count(self.browser), "根据交易流水号，查询结果错误！")
        self.assertEqual(self.serial_number, common.trade.get_serial_number(self.browser, 1), "根据交易流水号，查询结果错误！")
        common.common.logout(self.browser)

    def test05_search_by_order_number(self):
        print "交易管理：执行测试用例05"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_trade_by_order_number(self.browser, self.order_number)
        self.assertEqual(self.order_number, common.trade.get_order_number(self.browser, 1), "根据商户订单号，查询结果错误！")
        common.common.logout(self.browser)

    def test06_search_by_pay_status(self):
        print "交易管理：执行测试用例06"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        # 成功
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_by_pay_status(self.browser, u"成功")
        if not common.trade.get_results_count(self.browser) == 0:
            self.assertEqual(u"成功", common.trade.get_pay_status(self.browser, 1), "根据支付状态，查询结果错误！")
        else:
            print "根据支付状态'成功'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 失败
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_by_pay_status(self.browser, u"失败")
        if not common.trade.get_results_count(self.browser) == 0:
            self.assertEqual(u"失败", common.trade.get_pay_status(self.browser, 1), "根据支付状态，查询结果错误！")
        else:
            print "根据支付状态'失败'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 已撤销
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_by_pay_status(self.browser, u"已撤销")
        if not common.trade.get_results_count(self.browser) == 0:
            self.assertEqual(u"已撤销", common.trade.get_pay_status(self.browser, 1), "根据支付状态，查询结果错误！")
        else:
            print "根据支付状态'已撤销'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 已冲正
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_by_pay_status(self.browser, u"已冲正")
        if not common.trade.get_results_count(self.browser) == 0:
            self.assertEqual(u"已冲正", common.trade.get_pay_status(self.browser, 1), "根据支付状态，查询结果错误！")
        else:
            print "根据支付状态'已冲正'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 已退款
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_by_pay_status(self.browser, u"已退款")
        if not common.trade.get_results_count(self.browser) == 0:
            self.assertEqual(u"已退款", common.trade.get_pay_status(self.browser, 1), "根据支付状态，查询结果错误！")
        else:
            print "根据支付状态'已退款'，没有查询到任何结果，请手工再次检查！"

        common.common.logout(self.browser)

    def test07_search_by_salesman(self):
        print "交易管理：执行测试用例07"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.search_trade_by_salesman(self.browser, self.salesman_name)
        self.assertEqual(self.salesman_name, common.trade.get_salesman_name(self.browser, 1), "根据业务员名称，查询结果错误！")
        common.common.logout(self.browser)

    def test08_download_trade_list(self):
        print "业务员管理：执行测试用例08"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"交易管理", u"交易管理")
        common.trade.search_trade_by_time(self.browser, self.start_trade_date2, self.start_trade_time2, self.end_trade_date2, self.end_trade_time2)
        common.trade.download_trade_list(self.browser)
        common.common.logout(self.browser)



    if __name__ == "__main__":
        unittest.main()