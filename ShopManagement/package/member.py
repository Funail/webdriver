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
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[1]").click()

    elif shopname == u"测试分店":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]").click()

    elif shopname == u"测试员工测试":
        shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/input")
        shopname_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[3]/span").click()

    else:
        print "会员管理，店铺名称筛选有误！"


'''会员集点活动状态筛选'''
def redpoint_status(driver, redpointstatus):
    if redpointstatus == u"全部":
        redpointstatus_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        redpointstatus_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[1]").click()

    elif redpointstatus == u"未开始":
        redpointstatus_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        redpointstatus_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]").click()

    elif redpointstatus == u"进行中":
        redpointstatus_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        redpointstatus_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[3]").click()

    elif redpointstatus == u"已结束":
        redpointstatus_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        redpointstatus_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[4]").click()

    elif redpointstatus == u"已终止":
        redpointstatus_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        redpointstatus_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[5]").click()

    else:
        print "会员集点，活动状态筛选有误！"


'''会员集点店铺名称筛选'''
def redpoint_shopname_filter(driver, redpoint_shopname):
    if redpoint_shopname == u"全部":
        redpoint_shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/input")
        redpoint_shopname_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[1]/span").click()

    elif redpoint_shopname == u"测试分店":
        redpoint_shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/input")
        redpoint_shopname_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]/span").click()

    elif redpoint_shopname == u"测试员工测试":
        redpoint_shopname_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/input")
        redpoint_shopname_btn.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/ul/li[3]/span").click()

    else:
        print "会员集点，店铺名称筛选有误！"


'''会员集点创建'''
def creat_redpoint(driver,dictory1):
    # 创建集点
    point_creat_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div")
    point_creat_btn.click()
    time.sleep(2)
    point_target_number = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div/span[5]/i")
    point_target_number.click()
    point_require_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div/div[1]/input")
    point_require_amount.send_keys(dictory1["require_amount"])
    point_once_multipoint = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/label/span[1]/span")
    point_once_multipoint.click()
    point_present_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div[1]/input")
    point_present_name.send_keys(dictory1["present_name"])
    point_present_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[5]/div/div[1]/input")
    point_present_amount.send_keys(dictory1["present_amount"])
    point_start_time = driver.find_element_by_css_selector("input[placeholder='请选择开始时间']")
    point_start_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("td.available.today.current").click()
    point_end_time = driver.find_element_by_css_selector("input[placeholder='请选结束时间']")
    point_end_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("body > div:nth-child(7) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr > td.available.today.current").click()
    point_shopname = driver.find_element_by_css_selector("input[placeholder='请选择门店']")
    point_shopname.click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[1]").click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/i")
    next_btn.click()
    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/span/i")
    submit_btn.click()

'''会员集点修改活动'''
def edit_redpoint(driver,dictory1):
    # 修改集点
    mouse = driver.find_element_by_css_selector("#memberredcollect > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_9 > div > div > span")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(2)
    point_edit_btn = driver.find_element_by_xpath("/html/body/ul/li[1]")
    point_edit_btn.click()
    time.sleep(2)
    point_require_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div/div[1]/input")
    point_require_amount.clear()
    point_require_amount.send_keys(dictory1["require_amount"])
    point_once_multipoint = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div/label/span[1]/span")
    point_once_multipoint.click()
    point_present_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div[1]/input")
    point_present_name.clear()
    point_present_name.send_keys(dictory1["present_name"])
    point_present_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[5]/div/div[1]/input")
    point_present_amount.clear()
    point_present_amount.send_keys(dictory1["present_amount"])
    # point_start_time = driver.find_element_by_css_selector("input[placeholder='请选择开始时间']")
    # point_start_time.click()
    # time.sleep(2)
    # driver.find_element_by_css_selector("td.available.today.current").click()
    # point_end_time = driver.find_element_by_css_selector("input[placeholder='请选结束时间']")
    # point_end_time.click()
    # time.sleep(2)
    # driver.find_element_by_css_selector("td.available:nth-child(4)").click()
    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/i")
    next_btn.click()
    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/span/i")
    submit_btn.click()

'''会员集点停止活动'''
def end_redpoint(driver):
    # 停止集点活动
    mouse = driver.find_element_by_css_selector("#memberredcollect > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_9 > div > div > span")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)
    point_end_btn = driver.find_element_by_xpath("/html/body/ul/li[2]")
    point_end_btn.click()
    mouse = driver.find_element_by_css_selector("body > div.el-message-box__wrapper > div")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)
    point_confirm_btn = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]/span")
    point_confirm_btn.click()
    time.sleep(1)

