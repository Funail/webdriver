#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from selenium.webdriver.common.action_chains import ActionChains
import common
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver



'''会员管理店铺名称筛选'''
def member_shopname_filter(driver, shopname):
    if shopname == u"全部":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[1]/span").click()

    elif shopname == u"测试分店":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]/span").click()

    elif shopname == u"业务员:二级业务员测试无默认":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[3]/span").click()

    elif shopname == u"测试员工测试":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[4]/span").click()

    else:
        print "会员管理，店铺名称筛选有误！"


'''会员管理会员数'''
def get_member_shopname_count(driver):
    try:
        common.findCss(driver,"body > div.top_content > div.main > div.redpacket > div.panel > div.pagination_wrapper > div > span.el-pagination__sizes > div > div.el-input > i")
        a = True
    except:
        a = False
    if a == True:
        member_page_btn = common.findCss(driver,"body > div.top_content > div.main > div.redpacket > div.panel > div.pagination_wrapper > div > span.el-pagination__sizes > div > div.el-input > i")
        member_page_btn.click()
        time.sleep(1)

        member_page100_btn = common.findXpath(driver, "/html/body/div[4]/div/div[1]/ul/li[6]/span")
        member_page100_btn.click()
        time.sleep(2)

        member_shopname_count = common.findsCss(driver,"body > div.top_content > div.main > div.redpacket > div.panel > div.panel-body > div > div.el-table__body-wrapper > table > tbody > tr")
        return len(member_shopname_count)
    elif a == False:
        member_shopname_count = common.findsCss(driver,"body > div.top_content > div.main > div.redpacket > div.panel > div.panel-body > div > div.el-table__body-wrapper > table > tbody > tr")
        return len(member_shopname_count)
    else:
        print u"会员数目错误！"

