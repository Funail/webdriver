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


'''会员储值创建'''
def creat_redstorage(driver,dictory6):
    # 创建集点
    creat_redstorage_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/i")
    creat_redstorage_btn.click()
    time.sleep(2)

    redstorage_start_time = driver.find_element_by_css_selector("input[placeholder='请选择开始时间']")
    redstorage_start_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("td.available.today.current").click()
    time.sleep(1)

    redstorage_end_time = driver.find_element_by_css_selector("input[placeholder='请选结束时间']")
    redstorage_end_time.click()
    time.sleep(1)
    driver.find_element_by_css_selector("body > div:nth-child(8) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(4) > td.available.today.current").click()

    redstorage_store_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/div[1]/div/div[1]/input")
    redstorage_store_amount.send_keys(dictory6["store_amount"])

    redstorage_extra_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/div[2]/div/div/input")
    redstorage_extra_amount.send_keys(dictory6["extra_amount"])

    redstorage_remark = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[5]/div/div[1]/div/div[1]/textarea")
    redstorage_remark.send_keys(dictory6["remark"])

    redstorage_phone_number = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[6]/div/div/input")
    redstorage_phone_number.send_keys(dictory6["phone_number"])

    next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/i")
    next_btn.click()

    submit_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/span/i")
    submit_btn.click()


'''会员储值修改'''
def edit_redstorage(driver,dictory6):
    # 修改储值
    mouse = driver.find_element_by_css_selector("#memberstorage > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_7 > div > div > span > i")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)

    redstorage_edit_btn = driver.find_element_by_css_selector("body > ul > li:nth-child(1)")
    redstorage_edit_btn.click()
    time.sleep(2)

    point_require_amount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div/div[1]/input")
    point_require_amount.clear()
    point_require_amount.send_keys(dictory2["require_amount"])


'''会员储值停止活动'''
def end_redstorage(driver):
    # 停止集点活动
    mouse = driver.find_element_by_css_selector("#memberstorage > div.el-table__body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_7 > div > div > span > i")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)

    redstorage_end_btn = driver.find_element_by_css_selector("body > ul > li:nth-child(2)")
    redstorage_end_btn.click()

    mouse = driver.find_element_by_css_selector("body > div.el-message-box__wrapper > div")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)

    redstorage_confirm_btn = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]/span")
    redstorage_confirm_btn.click()
    time.sleep(1)

