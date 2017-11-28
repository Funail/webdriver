# coding:utf-8
import time
import common

def create_notifications(driver, title, content, qd_list = "", top = False):
    element_title = driver.find_element_by_css_selector("label[for='title']+div>div>input")
    element_title.send_keys(title)
    element_content = driver.find_element_by_css_selector("label[for='content']+div>div>textarea")
    element_content.send_keys(content)
    if not qd_list == "":
        element_qd_list = driver.find_element_by_css_selector("label[for='qd_list']+div>div>textarea")
        element_qd_list.send_keys(qd_list)
    if not top == False:
        element_set_top = driver.find_element_by_css_selector("div.el-switch__label.el-switch__label--right")
        element_set_top.click()

    sure_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    sure_btn.click()
    yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
    yes_btn.click()
    time.sleep(3)

def get_results_count(driver):
    search_results = driver.find_elements_by_css_selector("div.right_body tbody tr")
    return len(search_results)

def get_notification_title(driver, index):
    i = index - 1
    if get_results_count(driver) > 0:
        title = driver.find_elements_by_css_selector("td.el-table_1_column_1 > div.cell > button > span")[i].text
    else:
        title = ""
    return title

def delete_notification_by_title(driver, title):
    delete_btn = driver.find_element_by_xpath("//span[contains(text(), '" + title + "')]/../../../../td[3]/div/button")
    delete_btn.click()
    yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
    yes_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(0.5)

def find_notification_by_title(driver, title):
    try:
        return driver.find_element_by_xpath("//span[contains(text(),'" + title + "')]").is_displayed()
    except Exception, e:
        return False


def try_to_close_notification(driver):
    if driver.find_element_by_css_selector("div[id='app'] > div.bounced_my div.bounced_my_body.big_bounced").is_displayed():
        time.sleep(1)
        try:
            announce_closeBtn = driver.find_element_by_css_selector("div[id='app'] > div.bounced_my div.bounced_my_body.big_bounced header span i.close")
            announce_closeBtn.click()
            time.sleep(1)
        except Exception, e:
            print "可忽略：没有弹出公告"





