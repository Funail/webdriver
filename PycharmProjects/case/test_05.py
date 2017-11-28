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
import random

class Test05(unittest.TestCase):

    # 初始化变量
    site = "https://qudao.qa.qfpay.net"
    username = "14700001237"
    password = "237018"
    notification_title_for_test01 = u"公告（一）" + str(random.randint(0, 9999)).zfill(4)
    notification_title_for_test02 = u"公告（二）" + str(random.randint(0, 9999)).zfill(4)
    notification_content = u"活动名称: 微信绿洲计划；活动申请时间：" + "\n" + u"2017年5月1日-2017年11月31日"
    # 发送给二级渠道和三级渠道
    qd_list = "21004745,21004742"
    # 二级渠道和三级渠道进行验证
    username1_for_test01 = "17705762504"
    username2_for_test01 = "17760424118"
    # 验证qd_list之外的渠道收不到公告
    username3_for_test01 = "17718360722"


    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        #self.browser.maximize_window()
        time.sleep(1)

    def tearDown(self):
        # 关闭浏览器
        self.browser.quit()

    def test01_create_notification_with_qdlist_and_pop(self):
        print "公告管理：执行测试用例01"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"公告管理", u"新增公告")
        common.notifications.create_notifications(self.browser, self.notification_title_for_test01, self.notification_content, self.qd_list, True)
        common.common.logout(self.browser)
        arr = common.common.login(self.browser, self.site, self.username1_for_test01, self.password)
        self.assertTrue(arr[1], "没有弹出公告！")
        self.browser.save_screenshot(
            "/Users/liuchang/PycharmProjects/" + "notification_popup_page(1)" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png")
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        self.assertEqual(self.notification_title_for_test01, common.notifications.get_notification_title(self.browser, 1), "置顶公告显示错误！")
        common.common.logout(self.browser)

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        arr = common.common.login(self.browser, self.site, self.username2_for_test01, self.password)
        self.assertTrue(arr[1], "没有弹出公告！")
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        self.assertEqual(self.notification_title_for_test01, common.notifications.get_notification_title(self.browser, 1), "置顶公告显示错误！")
        common.common.logout(self.browser)

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        arr = common.common.login(self.browser, self.site, self.username3_for_test01, self.password)
        self.assertFalse(arr[1], "不应该弹出公告！")
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        self.assertNotEqual(self.notification_title_for_test01, common.notifications.get_notification_title(self.browser, 1), "其他渠道也可以看到该公告！")
        common.common.logout(self.browser)

    def test02_create_notification_without_qdlist_and_not_pop(self):
        print "公告管理：执行测试用例02"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"公告管理", u"新增公告")
        common.notifications.create_notifications(self.browser, self.notification_title_for_test02, self.notification_content)
        common.common.logout(self.browser)

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        arr = common.common.login(self.browser, self.site, self.username1_for_test01, self.password)
        self.assertTrue(arr[1], "没有弹出公告！")
        self.browser.save_screenshot(
            "/Users/liuchang/PycharmProjects/" + "notification_popup_page(2)" + time.strftime("%Y%m%d%H%M%S",
                                                                                           time.localtime()) + ".png")
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        self.assertNotEqual(self.notification_title_for_test02, common.notifications.get_notification_title(self.browser, 1),
                         "新增公告显示错误！")
        common.common.logout(self.browser)

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        arr = common.common.login(self.browser, self.site, self.username3_for_test01, self.password)
        self.assertTrue(arr[1], "没有弹出公告！")
        self.browser.save_screenshot(
            "/Users/liuchang/PycharmProjects/" + "notification_popup_page(3)" + time.strftime("%Y%m%d%H%M%S",
                                                                                            time.localtime()) + ".png")
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        self.assertEqual(self.notification_title_for_test02, common.notifications.get_notification_title(self.browser, 1),
                            "新增公告显示错误！")
        common.common.logout(self.browser)

    def test03_delete_notification_of_test01(self):
        print "公告管理：执行测试用例03"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        common.notifications.delete_notification_by_title(self.browser, self.notification_title_for_test01)
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        common.notifications.try_to_close_notification(self.browser)
        self.assertFalse(common.notifications.find_notification_by_title(self.browser, self.notification_title_for_test01), "公告1没有删除成功！")

        common.common.logout(self.browser)

    def test04_delete_notification_of_test02(self):
        print "公告管理：执行测试用例04"
        common.common.login(self.browser, self.site, self.username, self.password)
        common.common.open_menu(self.browser, u"公告管理", u"公告管理")
        common.notifications.delete_notification_by_title(self.browser, self.notification_title_for_test02)
        self.browser.refresh()
        common.common.wait_until_loading_disappeared(self.browser)
        common.notifications.try_to_close_notification(self.browser)
        self.assertFalse(common.notifications.find_notification_by_title(self.browser, self.notification_title_for_test02), "公告2没有删除成功！")

        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1280, 800)
        arr = common.common.login(self.browser, self.site, self.username3_for_test01, self.password)
        self.assertFalse(arr[1], "不应该弹出公告！")
        common.common.logout(self.browser)


    if __name__ == "__main__":
        unittest.main()