# coding:utf-8
import unittest
import time
from selenium import webdriver
import random
import sys
sys.path.append("/Users/liuchang/PycharmProjects/common")
import common.common
import common.qudao

class Test01(unittest.TestCase):

    # 初始化变量
    site = "https://qudao.qa.qfpay.net"
    username = "14700001237"
    password = "237018"
    qd_name_value = u"渠道" + str(random.randint(0, 9999)).zfill(4)
    qd_mobile_value = "177" + str(random.randint(0, 99999999)).zfill(8)
    qd_slsm_mobile = "13545454545"
    qudao_id = ""
    #qd_mobile_value = "17717218686"
    #qudao_id = "11112200"
    #qd_name_value = u"渠道3607"
    #qd_slsm_mobile = "14448888888"

    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_ceate_qudao(self):
        print "渠道管理：执行测试用例01"

        common.common.login(self.browser, self.site, self.username, self.password)

        # 创建渠道
        common.common.open_menu(self.browser, u"渠道管理", u"新增渠道")
        dict1 = {"type":"", "name":self.qd_name_value, "short_name":u"渠道", "legal_name":u"张三", "legal_idnumber":"633222123401237018", "mobile":self.qd_mobile_value, "country":"", "timezone":"", "currency":"", "email":self.qd_mobile_value + "@163.com","province":u"北京市", "city":u"北京市"}
        dict2 = {"slsm_mobile":self.qd_slsm_mobile, "province":"", "city":"", "business_name":u"李四", "business_mobile":self.qd_mobile_value, "business_email":self.qd_mobile_value + "@163.com", "finace_name":u"赵六", "finace_mobile":self.qd_mobile_value, "finace_email":self.qd_mobile_value + "@163.com", "manager_name":u"经理", "manager_mobile":self.qd_mobile_value, "service_manager_name":u"经理", "service_manager_mobile":self.qd_mobile_value, "logo_url":"/Users/liuchang/PycharmProjects/logo2.jpeg", "icon_url":"/Users/liuchang/PycharmProjects/logo2.jpeg", "business_license_url":"/Users/liuchang/PycharmProjects/logo2.jpeg", "bank_account_url":"/Users/liuchang/PycharmProjects/logo2.jpeg", "address":u"望京SOHO T3 A座17层"}
        dict3 = {"bankuser":u"王五", "bankaccount":str(random.randint(0, 9999999999999999)).zfill(16), "headbankname":"", "bankname":"", "banktype":"", "settle_cycle":"", "settle_base_amt":"", "wechat_fee":"1", "alipay_fee":"1", "qqwallet_fee":"1", "jd_fee":"1", "swipecard_fee":"1", "default_mchnt_fee":"1"}
        dict4 = {"chuzhi":"", "ads":""}
        common.qudao.create_qudao(self.browser, dict1, dict2, dict3, dict4)

        # 验证
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")
        try:
            first_qudao_name = common.qudao.get_qudao_name(self.browser, 1)

        except Exception, e:
            self.browser.refresh()
            time.sleep(3)
            first_qudao_name = common.qudao.get_qudao_name(self.browser, 1)

        Test01.qudao_id = common.qudao.get_qudao_id(self.browser, 1)
        self.assertEqual(self.qd_name_value, first_qudao_name, "渠道列表无新建渠道！")

        # 退出
        common.common.logout(self.browser)

    def test02_change_password(self):
        print "渠道管理：执行测试用例02"

        common.common.login(self.browser, self.site, self.qd_mobile_value, "237018")

        #截图，验证用户名、头像、昨日数据等
        self.browser.save_screenshot("/Users/liuchang/PycharmProjects/" + "main_page" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")

        self.assertTrue(common.common.change_password(self.browser, "237018", "000006"), "密码修改失败！")
        common.common.login(self.browser, self.site, self.qd_mobile_value, "000006")

        common.common.logout(self.browser)

    def test03_search_qudao(self):
        print "渠道管理：执行测试用例03"

        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")

        # 根据渠道编号查询
        common.qudao.search_by_qudao_id(self.browser, Test01.qudao_id)
        self.assertEqual(1, common.qudao.get_results_count(self.browser), "根据渠道编号，查询结果错误！")
        self.assertEqual(Test01.qudao_id, common.qudao.get_qudao_id(self.browser, 1), "根据渠道编号，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 根据渠道名称查询
        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        self.assertEqual(1, common.qudao.get_results_count(self.browser), "根据渠道名称，查询结果错误！")
        self.assertEqual(self.qd_name_value, common.qudao.get_qudao_name(self.browser, 1), "根据渠道名称，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 根据渠道状态查询（正常）
        common.qudao.search_by_qudao_status(self.browser, u"正常")
        if not common.qudao.get_results_count(self.browser) == 0:
            self.assertEqual(u"正常", common.qudao.get_qudao_status(self.browser, 1), "根据渠道状态，查询结果错误！")
        else:
            print "根据渠道状态'正常'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 根据渠道状态查询（停用）
        common.qudao.search_by_qudao_status(self.browser, u"停用")
        if not common.qudao.get_results_count(self.browser) == 0:
            self.assertEqual(u"停用", common.qudao.get_qudao_status(self.browser, 1), "根据渠道状态，查询结果错误！")
        else:
            print "根据渠道状态'停用'，没有查询到任何结果，请手工再次检查！"

        common.common.logout(self.browser)

    def test04_change_qudao_status_to_inactive(self):
        print "渠道管理：执行测试用例04"

        # 停用并验证
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")
        common.qudao.change_qudao_status(self.browser, self.qd_name_value, u"停用")
        self.browser.refresh()
        time.sleep(3)
        common.qudao.search_by_qudao_status(self.browser, u"停用")
        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        self.assertEqual(self.qd_name_value, common.qudao.get_qudao_name(self.browser, 1), "停用状态显示异常！")
        self.assertEqual(u"停用", common.qudao.get_qudao_status(self.browser, 1), "停用状态显示异常！")
        common.common.logout(self.browser)
        arr = common.common.login(self.browser, self.site, self.qd_mobile_value, "000006")
        self.assertFalse(arr[0], "停用功能失效！")

    def test05_change_qudao_status_to_active(self):
        print "渠道管理：执行测试用例05"

        # 启用并验证
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")
        common.qudao.change_qudao_status(self.browser, self.qd_name_value, u"开启")
        self.browser.refresh()
        time.sleep(3)
        common.qudao.search_by_qudao_status(self.browser, u"正常")
        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        self.assertEqual(self.qd_name_value, common.qudao.get_qudao_name(self.browser, 1), "正常状态显示异常！")
        self.assertEqual(u"正常", common.qudao.get_qudao_status(self.browser, 1), "停用状态显示异常！")
        common.common.logout(self.browser)
        arr = common.common.login(self.browser, self.site, self.qd_mobile_value, "000006")
        self.assertTrue(arr[0], "开启功能失效！")
        common.common.logout(self.browser)

    def test06_download_qudao_list(self):
        print "渠道管理：执行测试用例06"

        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")
        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        common.qudao.download_qudao_list(self.browser)
        common.common.logout(self.browser)

    def test07_check_qudao_info(self):
        print "渠道管理：执行测试用例07"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"渠道管理", u"渠道管理")

        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        common.qudao.check_basic_info(self.browser)
        # 截图，验证基本信息
        self.browser.save_screenshot("/Users/liuchang/PycharmProjects/" + "basic_info" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        common.qudao.back_from_info_page(self.browser)

        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        common.qudao.check_account_info(self.browser)
        # 截图，验证账户信息
        self.browser.save_screenshot("/Users/liuchang/PycharmProjects/" + "account_info" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        common.qudao.back_from_info_page(self.browser)

        common.qudao.search_by_qudao_name(self.browser, self.qd_name_value)
        common.qudao.check_add_values_info(self.browser)
        #截图，验证增值产品信息
        self.browser.save_screenshot("/Users/liuchang/PycharmProjects/" + "add_values_info" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")

        common.common.logout(self.browser)


if  __name__ == "__main__":
    unittest.main()