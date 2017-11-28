# coding:utf-8
import time
import common

def search_and_wait(driver):
    search_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    search_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(0.5)

def search_by_qudao_id(driver, id):
    qd_id = driver.find_element_by_css_selector("label[for='id']+div>div>input")
    qd_id.send_keys(id)
    search_and_wait(driver)

def search_by_qudao_name(driver, name):
    qd_name = driver.find_element_by_css_selector("label[for='name']+div>div>input")
    qd_name.send_keys(name)
    search_and_wait(driver)

def search_by_shanghu_id(driver, id):
    shanghu_id = driver.find_element_by_css_selector("label[for='userid']+div>div>input")
    shanghu_id.send_keys(id)
    search_and_wait(driver)

def search_by_shanghu_name(driver, name):
    shanghu_name = driver.find_element_by_css_selector("label[for='shopname']+div>div>input")
    shanghu_name.send_keys(name)
    search_and_wait(driver)

def search_by_mobile(driver, number):
    mobile = driver.find_element_by_css_selector("label[for='mobile']+div>div>input")
    mobile.send_keys(number)
    search_and_wait(driver)

def search_by_slsm_name(driver, name):
    slsm_name = driver.find_element_by_css_selector("label[for='slsm_name']+div>div>input")
    slsm_name.send_keys(name)
    search_and_wait(driver)

def search_by_mchid(driver, id):
    mchid = driver.find_element_by_css_selector("label[for='mchid']+div>div>input")
    mchid.send_keys(id)
    search_and_wait(driver)

def search_by_audit_state(driver, status):
    audit_state_btn = driver.find_elements_by_css_selector("input[placeholder='']")[0]
    audit_state_btn.click()
    time.sleep(2)

    if status == u"拒绝":
        status_refuse = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[11].find_elements_by_tag_name("li")[0]
        status_refuse.click()
    elif status == u"成功":
        status_success = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[11].find_elements_by_tag_name("li")[1]
        status_success.click()
    elif status == u"失败":
        status_failed = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[11].find_elements_by_tag_name("li")[2]
        status_failed.click()
    elif status == u"审核中":
        status_review = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[11].find_elements_by_tag_name("li")[3]
        status_review.click()
    else:
        print "无此状态！"
        return 0

    search_and_wait(driver)

# def search_by_registration_time(driver, start, end):
#     js = "element=document.getElementsByClassName('el-date-editor.el-input.el-date-editor--daterange')[0];element2=element.getElementsByTagName('input')[0].removeAttribute('readonly');element2.value='2017-09-30';"
#     driver.execute_script(js)
#     # registration_time_btn = driver.find_elements_by_css_selector("input[placeholder='选择日期范围']")
#     # registration_time_btn.send_keys(start + " - " + end)
#     time.sleep(60)
#     search_and_wait(driver)

def get_results_count(driver):
    search_results = driver.find_elements_by_css_selector("div.right_body tbody tr")
    return len(search_results)

def get_qudao_id(driver, index):
    i = index - 1
    qudao_id = driver.find_elements_by_css_selector("td.el-table_1_column_1 > div.cell")[i].text
    return qudao_id

def get_qudao_name(driver, index):
    i = index - 1
    qudao_name = driver.find_elements_by_css_selector("td.el-table_1_column_2 > div.cell")[i].text
    return qudao_name

def get_shanghu_id(driver, index):
    i = index -1
    shanghu_id = driver.find_elements_by_css_selector("td.el-table_1_column_3 > div.cell")[i].text
    return shanghu_id

def get_shanghu_name(driver, index):
    i = index -1
    shanghu_name = driver.find_elements_by_css_selector("td.el-table_1_column_4 > div.cell")[i].text
    return shanghu_name

def get_mobile_number(driver, index):
    i = index -1
    mobile_number = driver.find_elements_by_css_selector("td.el-table_1_column_7 > div.cell")[i].text
    return mobile_number

def get_registration_time(driver, index):
    i = index -1
    registration_time = driver.find_elements_by_css_selector("td.el-table_1_column_8 > div.cell")[i].text
    return registration_time

def get_audit_state(driver, index):
    i = index -1
    audit_state = driver.find_elements_by_css_selector("td.el-table_1_column_9 > div.cell")[i].text
    return audit_state

def get_shanghu_status(driver, index):
    i = index - 1
    shanghu_status = driver.find_elements_by_css_selector("td.el-table_1_column_11 > div.cell > span")[i].text
    return shanghu_status

def get_salesman(driver, index):
    i = index -1
    salesman = driver.find_elements_by_css_selector("td.el-table_1_column_12 > div.cell")[i].text
    return salesman

def get_mchid(driver, index):
    i = index -1
    mchid = driver.find_elements_by_css_selector("td.el-table_1_column_13 > div.cell")[i].text
    return mchid

def download_shanghu_list(driver):
    download_btn = driver.find_element_by_css_selector("button.el-button.el-button--default")
    download_btn.click()
    time.sleep(5)

def change_shanghu_status(driver, id, operation):
    if operation == u"注销":
        search_by_shanghu_id(driver, id)
        time.sleep(2)
        if get_results_count(driver) == 1:
            deactive_btn = driver.find_element_by_css_selector("button.el-button.el-button--warning")
            deactive_btn.click()
        else:
            return 0
    elif operation == u"启用":
        search_by_shanghu_id(driver, id)
        time.sleep(2)
        if get_results_count(driver) == 1:
            active_btn = driver.find_element_by_css_selector("button.el-button.el-button--info")
            active_btn.click()
        else:
            return 0
    else:
        return 0

    time.sleep(1)
    yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
    yes_btn.click()
    time.sleep(3)