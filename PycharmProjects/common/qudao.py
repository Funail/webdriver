# coding:utf-8
import time
import common

def create_qudao(driver, dictory1, dictory2, dictory3, dictory4):
    # 第一步
    qd_name = driver.find_element_by_css_selector("label[for='name']+div>div>input")
    qd_name.send_keys(dictory1["name"])
    qd_short_name = driver.find_element_by_css_selector("label[for='short_name']+div>div>input")
    qd_short_name.send_keys(dictory1["short_name"])
    qd_legal_name = driver.find_element_by_css_selector("label[for='legal_name']+div>div>input")
    qd_legal_name.send_keys(dictory1["legal_name"])
    qd_legal_idnumber = driver.find_element_by_css_selector("label[for='legal_idnumber']+div>div>input")
    qd_legal_idnumber.send_keys(dictory1["legal_idnumber"])
    qd_mobile = driver.find_element_by_css_selector("label[for='mobile']+div>div>input")
    qd_mobile.send_keys(dictory1["mobile"])
    qd_email = driver.find_element_by_css_selector("label[for='email']+div>div>input")
    qd_email.send_keys(dictory1["email"])

    auth_province_btn = driver.find_element_by_css_selector("input[placeholder='请选择授权省份']")
    auth_province_btn.click()
    time.sleep(1)
    if dictory1["province"] == u"北京市":
        province_bj = driver.find_elements_by_css_selector("li[areaid='11']")[1]
        province_bj.click()
    auth_city_btn = driver.find_element_by_css_selector("input[placeholder='请选择授权城市']")
    auth_city_btn.click()
    time.sleep(1)
    if dictory1["city"] == u"北京市":
        city_bj = driver.find_elements_by_css_selector("li[cityid='181']")[1]
        city_bj.click()
    next_btn1 = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[1]
    next_btn1.click()
    time.sleep(1)

    # 第二步
    qd_slsm_mobile = driver.find_element_by_css_selector("label[for='slsm_mobile']+div>div>input")
    qd_slsm_mobile.send_keys(dictory2["slsm_mobile"])
    qd_business_name = driver.find_element_by_css_selector("label[for='business_name']+div>div>input")
    qd_business_name.send_keys(dictory2["business_name"])
    qd_business_mobile = driver.find_element_by_css_selector("label[for='business_mobile']+div>div>input")
    qd_business_mobile.send_keys(dictory2["business_mobile"])
    qd_business_email = driver.find_element_by_css_selector("label[for='business_email']+div>div>input")
    qd_business_email.send_keys(dictory2["business_email"])
    qd_finace_name = driver.find_element_by_css_selector("label[for='finace_name']+div>div>input")
    qd_finace_name.send_keys(dictory2["finace_name"])
    qd_finace_mobile = driver.find_element_by_css_selector("label[for='finace_mobile']+div>div>input")
    qd_finace_mobile.send_keys(dictory2["finace_mobile"])
    qd_finace_email = driver.find_element_by_css_selector("label[for='finace_email']+div>div>input")
    qd_finace_email.send_keys(dictory2["finace_email"])
    qd_manager_name = driver.find_element_by_css_selector("label[for='manager_name']+div>div>input")
    qd_manager_name.send_keys(dictory2["manager_name"])
    qd_manager_mobile = driver.find_element_by_css_selector("label[for='manager_mobile']+div>div>input")
    qd_manager_mobile.send_keys(dictory2["manager_mobile"])
    qd_service_manager_name = driver.find_element_by_css_selector(
        "label[for='service_manager_name']+div>div>input")
    qd_service_manager_name.send_keys(dictory2["service_manager_name"])
    qd_service_manager_mobile = driver.find_element_by_css_selector(
        "label[for='service_manager_mobile']+div>div>input")
    qd_service_manager_mobile.send_keys(dictory2["service_manager_mobile"])
    qd_logo = driver.find_element_by_css_selector("input[name='logo_url']")
    qd_logo.send_keys(dictory2["logo_url"])
    common.wait_until_loading_disappeared(driver)
    qd_icon = driver.find_element_by_css_selector("input[name='icon_url']")
    qd_icon.send_keys(dictory2["icon_url"])
    common.wait_until_loading_disappeared(driver)
    qd_business_license = driver.find_element_by_css_selector("input[name='business_license_url']")
    qd_business_license.send_keys(dictory2["business_license_url"])
    common.wait_until_loading_disappeared(driver)
    qd_bank_account = driver.find_element_by_css_selector("input[name='bank_account_url']")
    qd_bank_account.send_keys(dictory2["bank_account_url"])
    common.wait_until_loading_disappeared(driver)
    qd_address = driver.find_element_by_css_selector("label[for='address']+div>div>input")
    qd_address.send_keys(dictory2["address"])
    next_btn2 = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[2]
    next_btn2.click()
    time.sleep(1)

    # 第三步
    qd_bankuser = driver.find_element_by_css_selector("label[for='bankuser']+div>div>input")
    qd_bankuser.send_keys(dictory3["bankuser"])
    qd_bankaccount = driver.find_element_by_css_selector("label[for='bankaccount']+div>div>input")
    qd_bankaccount.send_keys(dictory3["bankaccount"])
    qd_wechat_fee = driver.find_element_by_css_selector("label[for='wechat_fee']+div>div>input")
    qd_wechat_fee.send_keys(dictory3["wechat_fee"])
    qd_alipay_fee = driver.find_element_by_css_selector("label[for='alipay_fee']+div>div>input")
    qd_alipay_fee.send_keys(dictory3["alipay_fee"])
    qd_qqwallet_fee = driver.find_element_by_css_selector("label[for='qqwallet_fee']+div>div>input")
    qd_qqwallet_fee.send_keys(dictory3["qqwallet_fee"])
    qd_jd_fee = driver.find_element_by_css_selector("label[for='jd_fee']+div>div>input")
    qd_jd_fee.send_keys(dictory3["jd_fee"])
    qd_swipecard_fee = driver.find_element_by_css_selector("label[for='swipecard_fee']+div>div>input")
    qd_swipecard_fee.send_keys(dictory3["swipecard_fee"])
    qd_default_mchnt_fee = driver.find_element_by_css_selector("label[for='default_mchnt_fee']+div>div>input")
    qd_default_mchnt_fee.send_keys(dictory3["default_mchnt_fee"])
    next_btn3 = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[3]
    next_btn3.click()
    time.sleep(1)
    # 第四步
    save_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[4]
    save_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(1)

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

def search_by_qudao_status(driver, status):
    qudao_status_btn = driver.find_elements_by_css_selector("input[placeholder='请选择']")[1]
    qudao_status_btn.click()
    time.sleep(2)

    if status == u"全部":
        status_all = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[0]
        status_all.click()
    elif status == u"正常":
        status_active = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[1]
        status_active.click()
    elif status == u"停用":
        status_inactive = driver.find_elements_by_css_selector("ul.el-scrollbar__view.el-select-dropdown__list")[2].find_elements_by_tag_name("li")[2]
        status_inactive.click()
    else:
        print "无此状态！"
        return 0

    search_and_wait(driver)

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

def get_qudao_status(driver, index):
    i = index - 1
    qudao_status = driver.find_elements_by_css_selector("td.el-table_1_column_4 > div.cell")[i].text
    return qudao_status

def change_qudao_status(driver, name, status):
    if status == u"停用":
        search_by_qudao_status(driver, u"正常")
        search_by_qudao_name(driver, name)
    elif status == u"开启":
        search_by_qudao_status(driver, u"停用")
        search_by_qudao_name(driver, name)
    else:
        return 0

    if get_results_count(driver) == 1:
        change_btn = driver.find_elements_by_css_selector("td.el-table_1_column_10 > div.cell > span > button")[0]
        change_btn.click()
        time.sleep(1)
        yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
        yes_btn.click()
        time.sleep(3)
    else:
        return 0

def download_qudao_list(driver):
    download_btn = driver.find_element_by_css_selector("button.el-button.el-button--default")
    download_btn.click()
    time.sleep(5)
    # driver.get("https://qudao.qa.qfpay.net/qudao/v1/api/qd/list/download?userid=&name=%E6%B8%A0%E9%81%933330&status=")

def check_basic_info(driver):
    qudao_id = get_qudao_id(driver, 1)
    basic_info_btn = driver.find_element_by_css_selector("a[href='#/channel_base/"+qudao_id+"']")
    basic_info_btn.click()
    common.wait_until_loading_disappeared(driver)

def check_account_info(driver):
    qudao_id = get_qudao_id(driver, 1)
    account_info_btn = driver.find_element_by_css_selector("a[href='#/channel_account/"+qudao_id+"']")
    account_info_btn.click()
    common.wait_until_loading_disappeared(driver)

def check_add_values_info(driver):
    qudao_id = get_qudao_id(driver, 1)
    add_values_info_btn = driver.find_element_by_css_selector("a[href='#/channel_pro/"+qudao_id+"']")
    add_values_info_btn.click()
    common.wait_until_loading_disappeared(driver)

def back_from_info_page(driver):
    back_btn = driver.find_element_by_css_selector("button.el-button.el-button--default")
    back_btn.click()
    common.wait_until_loading_disappeared(driver)
    driver.refresh()
    common.wait_until_loading_disappeared(driver)








