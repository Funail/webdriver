# coding:utf-8
import time
import common

def search_and_wait(driver):
    search_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    search_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(0.5)

def search_by_salesman_id(driver, id):
    slsm_id = driver.find_element_by_css_selector("label[for='slsm_uid']+div>div>input")
    slsm_id.send_keys(id)


def search_by_salesman_name(driver, name):
    slsm_name = driver.find_element_by_css_selector("label[for='slsm_name']+div>div>input")
    slsm_name.send_keys(name)
    search_and_wait(driver)

def search_by_salesman_mobile(driver, mobile):
    slsm_mobile = driver.find_element_by_css_selector("label[for='slsm_mobile']+div>div>input")
    slsm_mobile.send_keys(mobile)
    search_and_wait(driver)

def search_by_salesman_status(driver, status):
    salesman_status_btn = driver.find_elements_by_css_selector("input[placeholder='请选择']")[1]
    salesman_status_btn.click()
    time.sleep(2)

    if status == u"全部":
        status_all = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[3].find_elements_by_tag_name("li")[0]
        status_all.click()
    elif status == u"在职":
        status_working = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[3].find_elements_by_tag_name("li")[1]
        status_working.click()
    elif status == u"离职":
        status_leave = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[3].find_elements_by_tag_name("li")[2]
        status_leave.click()
    else:
        print "无此状态！"
        return 0

    search_and_wait(driver)

def get_salesman_id(driver, index):
    i = index - 1
    id = driver.find_elements_by_css_selector("td.el-table_1_column_1 > div.cell")[i].text
    return id

def get_salesman_name(driver, index):
    i = index - 1
    name = driver.find_elements_by_css_selector("td.el-table_1_column_2 > div.cell")[i].text
    return name

def get_salesman_mobile(driver, index):
    i = index - 1
    mobile = driver.find_elements_by_css_selector("td.el-table_1_column_3 > div.cell")[i].text
    return mobile

def get_salesman_status(driver, index):
    i = index -1
    status = driver.find_elements_by_css_selector("td.el-table_1_column_4 > div.cell")[i].text
    return status

def get_results_count(driver):
    search_results = driver.find_elements_by_css_selector("div.right_body tbody tr")
    return len(search_results)

def download_salesman_list(driver):
    download_btn = driver.find_element_by_css_selector("button.el-button.el-button--default")
    download_btn.click()
    time.sleep(5)

