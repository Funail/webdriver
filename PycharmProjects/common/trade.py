# coding:utf-8
import time
import common

def search_and_wait(driver):
    search_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    search_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(0.5)

def search_trade_by_time(driver, startdate, starttime, enddate, endtime):
    start_time_btn = driver.find_elements_by_css_selector("i.el-input__icon.el-icon-time + input")[0]
    start_time_btn.click()
    time.sleep(1)
    start_date_element = driver.find_elements_by_css_selector("input[placeholder='选择日期']")[0]
    start_date_element.clear()
    start_date_element.send_keys(startdate)
    start_time_element = driver.find_elements_by_css_selector("input[placeholder='选择时间']")[0]
    start_time_element.clear()
    start_time_element.send_keys(starttime)
    start_yes_btn = driver.find_elements_by_css_selector("button.el-picker-panel__btn")[0]
    start_yes_btn.click()

    end_time_btn = driver.find_elements_by_css_selector("i.el-input__icon.el-icon-time + input")[1]
    end_time_btn.click()
    time.sleep(1)
    end_date_element = driver.find_elements_by_css_selector("input[placeholder='选择日期']")[1]
    end_date_element.clear()
    end_date_element.send_keys(enddate)
    end_time_element = driver.find_elements_by_css_selector("input[placeholder='选择时间']")[1]
    end_time_element.clear()
    end_time_element.send_keys(endtime)
    end_yes_btn = driver.find_elements_by_css_selector("button.el-picker-panel__btn")[1]
    end_yes_btn.click()

    search_and_wait(driver)

def search_trade_by_merchant_name(driver, name):
    merchant_name = driver.find_element_by_css_selector("label[for='mchnt_name']+div>div>input")
    merchant_name.send_keys(name)
    search_and_wait(driver)

def search_trade_by_mobile(driver, number):
    mobile = driver.find_element_by_css_selector("label[for='mchnt_mobile']+div>div>input")
    mobile.send_keys(number)
    search_and_wait(driver)

def search_trade_by_serial_number(driver, number):
    serial = driver.find_element_by_css_selector("label[for='trade_syssn']+div>div>input")
    serial.send_keys(number)
    search_and_wait(driver)

def search_trade_by_order_number(driver, number):
    order = driver.find_element_by_css_selector("label[for='out_trade_no']+div>div>input")
    order.send_keys(number)
    search_and_wait(driver)

def search_by_pay_status(driver, status):
    pay_status_btn = driver.find_elements_by_css_selector("input[placeholder='请选择']")[1]
    pay_status_btn.click()
    time.sleep(2)

    if status == u"全部":
        status_all = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[0]
        status_all.click()
    elif status == u"成功":
        status_success = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[1]
        status_success.click()
    elif status == u"失败":
        status_failed = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[2]
        status_failed.click()
    elif status == u"已撤销":
        status_canceled = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[3]
        status_canceled.click()
    elif status == u"已冲正":
        status_abnormal = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[4]
        status_abnormal.click()
    elif status == u"已退款":
        status_refunded = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[5]
        status_refunded.click()
    else:
        print "无此状态！"
        return 0

    search_and_wait(driver)

def search_trade_by_salesman(driver, name):
    slsm_name = driver.find_element_by_css_selector("label[for='slsm_name']+div>div>input")
    slsm_name.send_keys(name)
    search_and_wait(driver)

def get_trade_time(driver, index):
    i = index - 1
    time = driver.find_elements_by_css_selector("td.el-table_1_column_9 > div.cell")[i].text
    return time

def get_merchant_name(driver, index):
    i = index - 1
    name = driver.find_elements_by_css_selector("td.el-table_1_column_2 > div.cell")[i].text
    return name

def get_mobile_number(driver, index):
    i = index - 1
    number = driver.find_elements_by_css_selector("td.el-table_1_column_4 > div.cell")[i].text
    return number

def get_serial_number(driver, index):
    i = index - 1
    number = driver.find_elements_by_css_selector("td.el-table_1_column_5 > div.cell")[i].text
    return number

def get_order_number(driver, index):
    i = index - 1
    number = driver.find_elements_by_css_selector("td.el-table_1_column_7 > div.cell")[i].text
    return number

def get_pay_status(driver, index):
    i = index - 1
    status = driver.find_elements_by_css_selector("td.el-table_1_column_11 > div.cell")[i].text
    return status

def get_salesman_name(driver, index):
    i = index - 1
    name = driver.find_elements_by_css_selector("td.el-table_1_column_3 > div.cell")[i].text
    return name

def get_results_count(driver):
    search_results = driver.find_elements_by_css_selector("div.right_body tbody tr")
    return len(search_results)

def download_trade_list(driver):
    download_btn = driver.find_element_by_css_selector("button.el-button.el-button--default")
    download_btn.click()
    time.sleep(5)





