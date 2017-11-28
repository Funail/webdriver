# coding:utf-8
import unittest
from selenium import webdriver
import sys
sys.path.append("/Users/liuchang/PycharmProjects/common")
import common.common
import common.qudao
import common.shanghu

class Test02(unittest.TestCase):

    # 初始化变量
    site = "https://qudao.qa.qfpay.net"
    username = "14700001237"
    password = "237018"
    qudao_id = "11111789"
    qudao_name = u"新状态验证"
    shanghu_id = "10013362"
    shanghu_name = u"十五"
    mobile = "14710013362"
    salesman =u"李巍"
    mchtid = "08e5dnT3g0vx"


    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_search_shanghu_by_qudao(self):
        print "商户管理：执行测试用例01"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据渠道编号查询
        common.shanghu.search_by_qudao_id(self.browser, self.qudao_id)
        self.assertEqual(self.qudao_id, common.shanghu.get_qudao_id(self.browser, 1), "根据渠道编号，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 根据渠道名称查询
        common.shanghu.search_by_qudao_name(self.browser, self.qudao_name)
        self.assertEqual(self.qudao_name, common.shanghu.get_qudao_name(self.browser, 1), "根据渠道名称，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        common.common.logout(self.browser)

    def test02_search_shanghu_by_shanghu(self):
        print "商户管理：执行测试用例02"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据商户编号查询
        common.shanghu.search_by_shanghu_id(self.browser, self.shanghu_id)
        self.assertEqual(1, common.shanghu.get_results_count(self.browser), "根据商户编号，查询结果错误！")
        self.assertEqual(self.shanghu_id, common.shanghu.get_shanghu_id(self.browser, 1), "根据商户编号，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        # 根据商户名称查询
        common.shanghu.search_by_shanghu_name(self.browser, self.shanghu_name)
        self.assertEqual(self.shanghu_name, common.shanghu.get_shanghu_name(self.browser, 1), "根据商户名称，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        common.common.logout(self.browser)

    def test03_search_shanghu_by_mobile(self):
        print "商户管理：执行测试用例03"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据手机号查询
        common.shanghu.search_by_mobile(self.browser, self.mobile)
        self.assertEqual(self.mobile, common.shanghu.get_mobile_number(self.browser, 1), "根据手机号，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

    def test04_search_shanghu_by_id(self):
        print "商户管理：执行测试用例04"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据子商户号查询
        common.shanghu.search_by_mchid(self.browser, self.mchtid)
        self.assertEqual(self.mchtid, common.shanghu.get_mchid(self.browser, 1), "根据子商户号，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        common.common.logout(self.browser)

    def test05_search_shanghu_by_status(self):
        print "商户管理：执行测试用例05"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据审核状态查询
        # 拒绝
        common.shanghu.search_by_audit_state(self.browser, u"拒绝")
        if not common.shanghu.get_results_count(self.browser) == 0:
            self.assertEqual(u"拒绝", common.shanghu.get_audit_state(self.browser, 1), "根据审核状态，查询结果错误！")
        else:
            print "根据审核状态'拒绝'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 成功
        common.shanghu.search_by_audit_state(self.browser, u"成功")
        if not common.shanghu.get_results_count(self.browser) == 0:
            self.assertEqual(u"成功", common.shanghu.get_audit_state(self.browser, 1), "根据审核状态，查询结果错误！")
        else:
            print "根据审核状态'成功'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 失败
        common.shanghu.search_by_audit_state(self.browser, u"失败")
        if not common.shanghu.get_results_count(self.browser) == 0:
            self.assertEqual(u"失败", common.shanghu.get_audit_state(self.browser, 1), "根据审核状态，查询结果错误！")
        else:
            print "根据审核状态'失败'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        # 审核中
        common.shanghu.search_by_audit_state(self.browser, u"审核中")
        if not common.shanghu.get_results_count(self.browser) == 0:
            self.assertEqual(u"审核中", common.shanghu.get_audit_state(self.browser, 1), "根据审核状态，查询结果错误！")
        else:
            print "根据审核状态'审核中'，没有查询到任何结果，请手工再次检查！"
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        common.common.logout(self.browser)

    def test06_search_shanghu_by_salesman(self):
        print "商户管理：执行测试用例06"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        # 根据业务员查询
        common.shanghu.search_by_slsm_name(self.browser, self.salesman)
        self.assertEqual(self.salesman, common.shanghu.get_salesman(self.browser, 1), "根据业务员，查询结果错误！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)

        common.common.logout(self.browser)

    # def test07_search_shanghu_by_time(self):
    #     print "商户管理：执行测试用例07"
    #     common.common.login(self.browser, self.site, self.username, self.password)
    #     common.common.open_menu(self.browser, u"商户管理", u"商户管理")
    #
    #     #根据注册时间查询
    #     common.shanghu.search_by_registration_time(self.browser, "2017-09-30", "2017-09-30")
    #     time.sleep(60)
    #
    #     common.common.logout(self.browser)

    def test08_download_shanghu_list(self):
        print "商户管理：执行测试用例08"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")
        common.shanghu.download_shanghu_list(self.browser)
        common.common.logout(self.browser)

    def test09_change_shanghu_status(self):
        print "商户管理：执行测试用例09"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"商户管理", u"商户管理")

        common.shanghu.change_shanghu_status(self.browser, self.shanghu_id, u"注销")
        self.assertEqual(u"注销", common.shanghu.get_shanghu_status(self.browser, 1), "注销状态显示异常！")
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        common.shanghu.change_shanghu_status(self.browser, self.shanghu_id, u"启用")
        self.assertEqual(u"正常", common.shanghu.get_shanghu_status(self.browser, 1), "启用状态显示异常！")

        common.common.logout(self.browser)



    if __name__ == "__main__":
        unittest.main()