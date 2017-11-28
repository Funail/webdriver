# coding:utf-8
import time
import common

def create_training(driver, name, link, content):
    upload_btn = driver.find_elements_by_css_selector("button.el-button.el-button--default")[0]
    upload_btn.click()
    element_name = driver.find_elements_by_css_selector("label[for='name']+div>div>input")[1]
    element_name.send_keys(name)
    element_link = driver.find_element_by_css_selector("label[for='link']+div>div>input")
    element_link.send_keys(link)
    element_content = driver.find_element_by_css_selector("label[for='memo']+div>div>textarea")
    element_content.send_keys(content)
    create_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[1]
    create_btn.click()
    yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
    yes_btn.click()
    time.sleep(3)

def find_training_by_title(driver, title):
    try:
        return driver.find_element_by_xpath("//div[contains(text(), '" + title + "')]").is_displayed()
    except Exception, e:
        return False

def search_training_by_title(driver, title):
    element_title = driver.find_elements_by_css_selector("label[for='name']+div>div>input")[0]
    element_title.send_keys(title)
    search_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    search_btn.click()
    common.wait_until_loading_disappeared(driver)

def delete_training_by_title(driver, title):
    delete_btn = driver.find_element_by_xpath("//div[contains(text(), '" + title + "')]/../../td[3]/div/button[2]")
    delete_btn.click()
    yes_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sure")
    yes_btn.click()
    common.wait_until_loading_disappeared(driver)
    time.sleep(0.5)

def open_training_content(driver, title, link):
    info_btn = driver.find_element_by_xpath("//div[contains(text(), '" + title + "')]/../../td[3]/div/button[1]")
    info_btn.click()
    link_btn = driver.find_element_by_xpath("//a[contains(text(), '" + link + "')]")
    link_btn.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    return driver.current_url

def close_training_content(driver):
    close_btn = driver.find_elements_by_css_selector("i.close")[1]
    close_btn.click()

