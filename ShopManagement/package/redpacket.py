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



'''创建红包通知'''
def creat_redpacket_common(driver,dictory3):

    redpacket_creat_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/i")
    redpacket_creat_btn.click()
    time.sleep(2)
    redpacket_common_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[3]/div/div/div/div[1]/input")
    redpacket_common_amount.send_keys(dictory3["common_amount"])

    redpacket_common_requirement_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[4]/div/div/div/div[1]/input")
    redpacket_common_requirement_amount.send_keys(dictory3["common_requirement_amount"])

    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span")
    next_btn.click()
    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[4]/div/i")
    submit_btn.click()
    time.sleep(1)


'''创建消费返红包'''
def creat_redpacket_payment(driver,dictory4):
    redpacket_creat_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/i")
    redpacket_creat_btn.click()
    time.sleep(2)

    redpacket_payment_type = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[1]/div/div/div/label[2]/span[1]/span")
    redpacket_payment_type.click()

    redpacket_payment_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[1]/div/div[1]/input")
    redpacket_payment_name.send_keys(dictory4["payment_name"])

    redpacket_start_time = driver.find_element_by_css_selector("input[placeholder='请选择开始时间']")
    redpacket_start_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("td.available.today.current").click()

    redpacket_end_time = driver.find_element_by_css_selector("input[placeholder='请选结束时间']")
    redpacket_end_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("body > div:nth-child(7) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr > td.available.today.current").click()

    redpacket_payment_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[6]/div/div/div/div/input")
    redpacket_payment_amount.send_keys(dictory4["payment_amount"])

    redpacket_payment_number = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[7]/div/div/div/div/input")
    redpacket_payment_number.send_keys(dictory4["payment_number"])

    redpacket_payment_reveive_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[8]/div/div/div/div/input")
    redpacket_payment_reveive_amount.send_keys(dictory4["payment_reveive_amount"])

    redpacket_payment_requirement_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[9]/div/div/div/div/input")
    redpacket_payment_requirement_amount.send_keys(dictory4["payment_requirement_amount"])

    redpacket_payment_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[11]/div/div[1]/div/div[1]/input")
    redpacket_payment_date.send_keys(dictory4["payment_date"])

    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span")
    next_btn.click()

    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[5]/div/i")
    submit_btn.click()
    time.sleep(1)


'''创建分享红包'''
def creat_redpacket_share(driver,dictory5):
    redpacket_creat_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/i")
    redpacket_creat_btn.click()
    time.sleep(2)

    redpacket_share_type = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[1]/div/div/div/label[3]/span[1]/span")
    redpacket_share_type.click()

    redpacket_share_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[1]/div/div[1]/input")
    redpacket_share_name.send_keys(dictory5["share_name"])

    redpacket_start_time = driver.find_element_by_css_selector("input[placeholder='请选择开始时间']")
    redpacket_start_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("td.available.today.current").click()

    redpacket_end_time = driver.find_element_by_css_selector("input[placeholder='请选结束时间']")
    redpacket_end_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("body > div:nth-child(7) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr > td.available.today.current").click()

    redpacket_share_amount_type = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[5]/div/div/label[2]/span[1]/span")
    redpacket_share_amount_type.click()

    redpacket_share_amount1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[6]/div/div[1]/div/div/input")
    redpacket_share_amount1.send_keys(dictory5["share_amount1"])

    redpacket_share_amount2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[6]/div/div[2]/div/div/input")
    redpacket_share_amount2.send_keys(dictory5["share_amount2"])

    redpacket_share_total_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[7]/div/div/div/div/input")
    redpacket_share_total_amount.send_keys(dictory5["share_total_amount"])

    redpacket_share_reveive_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[8]/div/div/div/div[1]/input")
    redpacket_share_reveive_amount.send_keys(dictory5["share_reveive_amount"])

    redpacket_share_requirement_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[9]/div/div/div/div/input")
    redpacket_share_requirement_amount.send_keys(dictory5["share_requirement_amount"])

    redpacket_share_date_type = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[10]/div/div/label[2]/span[1]/span")
    redpacket_share_date_type.click()

    redpacket_share_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form[2]/div[11]/div/div[1]/div/div/input")
    redpacket_share_date.send_keys(dictory5["share_date"])

    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/span")
    next_btn.click()
    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[5]/div/i")
    submit_btn.click()
    time.sleep(1)


'''终止红包活动'''
def end_redpacket(driver):
    # 停止集点活动
    mouse = driver.find_element_by_css_selector("#memberredpacket > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_7 > div > div > span")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)
    redpacket_end_btn = driver.find_element_by_xpath("/html/body/ul/li")
    redpacket_end_btn.click()

    mouse = driver.find_element_by_css_selector("body > div.el-message-box__wrapper > div")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)

    redpacket_confirm_btn = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]/span")
    redpacket_confirm_btn.click()
    time.sleep(1)
