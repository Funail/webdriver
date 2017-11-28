# coding:utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

def login(driver, site, username, password):
    popup = False
    driver.get(site)
    time.sleep(2)
    name = driver.find_elements_by_css_selector("input.el-input__inner[type='text']")[1]
    psw = driver.find_elements_by_css_selector("input.el-input__inner[type='password']")[0]
    login_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    if name and psw and login_btn:
        name.click()
        name.send_keys(username)
        psw.click()
        psw.send_keys(password)
        login_btn.click()
        wait_until_loading_disappeared(driver)
    else:
        return 0, popup
    if check_announce_popup(driver):
        time.sleep(1)
        popup = True
        try:
            announce_closeBtn = driver.find_element_by_css_selector(
                "div[id='app'] > div.bounced_my div.bounced_my_body.big_bounced header span i.close")
            announce_closeBtn.click()
        except Exception, e:
            print "可忽略：没有弹出公告"
    quit_btn = driver.find_element_by_css_selector("div.manage_head_r span i.icon_quit")
    return quit_btn.is_displayed(), popup

def login_mis(driver, site, username, password):
    popup = False
    driver.get(site)
    time.sleep(2)
    name = driver.find_elements_by_css_selector("input.el-input__inner[type='text']")[0]
    psw = driver.find_elements_by_css_selector("input.el-input__inner[type='password']")[0]
    login_btn = driver.find_elements_by_css_selector("button.el-button.el-button--primary")[0]
    if name and psw and login_btn:
        name.click()
        name.send_keys(username)
        psw.click()
        psw.send_keys(password)
        login_btn.click()
        wait_until_loading_disappeared(driver)
    else:
        return 0, popup
    if check_announce_popup(driver):
        time.sleep(1)
        popup = True
        try:
            announce_closeBtn = driver.find_element_by_css_selector(
                "div[id='app'] > div.bounced_my div.bounced_my_body.big_bounced header span i.close")
            announce_closeBtn.click()
        except Exception, e:
            print "可忽略：没有弹出公告"
    quit_btn = driver.find_element_by_css_selector("div.manage_head_r span i.icon_quit")
    return quit_btn.is_displayed(), popup

def check_announce_popup(driver):
    try:
        return driver.find_element_by_css_selector("div[id='app'] > div.bounced_my div.bounced_my_body.big_bounced").is_displayed()
    except Exception, e:
        return False

def logout(driver):
    quit_btn = driver.find_element_by_css_selector("div.manage_head_r span i.icon_quit")
    quit_btn.click()
    time.sleep(1)
    name = driver.find_elements_by_css_selector("input.el-input__inner[type='text']")[1]
    if name:
        success = 1
    else:
        success =0
    return success

def logout_mis(driver):
    quit_btn = driver.find_element_by_css_selector("div.manage_head_r span i.icon_quit")
    quit_btn.click()
    time.sleep(1)
    name = driver.find_elements_by_css_selector("input.el-input__inner[type='text']")[0]
    if name:
        success = 1
    else:
        success =0
    return success

def get_left_menu_count(driver):
    menus = driver.find_elements_by_css_selector("ul.el-menu.el-menu-vertical-demo > li")
    return len(menus)

def open_menu(driver, menu, submenu = ""):

    if menu == u"昨日数据" and submenu == "":
        pass

    elif menu == u"渠道管理" and submenu == u"渠道管理":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[0].is_displayed():
            qudao_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_qudao_w")
            qudao_manageBtn.click()
            time.sleep(1)
        qudao_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[0]
        qudao_listBtn.click()

    elif menu == u"渠道管理" and submenu == u"新增渠道":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[0].is_displayed():
            qudao_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_qudao_w")
            qudao_manageBtn.click()
            time.sleep(1)
        qudao_addBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[1]
        qudao_addBtn.click()

    elif menu == u"商户管理" and submenu == u"商户管理":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[1].is_displayed():
            shanghu_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_shanghu_w")
            shanghu_manageBtn.click()
            time.sleep(1)
        shanghu_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[2]
        shanghu_listBtn.click()

    elif menu == u"业务员管理" and submenu == u"业务员管理":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[2].is_displayed():
            salesman_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_slsm_w")
            salesman_manageBtn.click()
            time.sleep(1)
        salesman_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[3]
        salesman_listBtn.click()

    elif menu == u"交易管理" and submenu == u"交易管理":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[3].is_displayed():
            trade_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_trade_w")
            trade_manageBtn.click()
            time.sleep(1)
        trade_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[4]
        trade_listBtn.click()

    elif menu == u"公告管理" and submenu == u"公告管理":
        if (get_left_menu_count(driver) == 8) or (get_left_menu_count(driver) == 9):
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[6].is_displayed():
                notification_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_notice_w")
                notification_manageBtn.click()
                time.sleep(1)
            notification_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[13]
            notification_listBtn.click()
        elif get_left_menu_count(driver) == 10:
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[7].is_displayed():
                notification_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_notice_w")
                notification_manageBtn.click()
                time.sleep(1)
            notification_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[15]
            notification_listBtn.click()
        else:
            print "左侧菜单数量错误！"

    elif menu == u"公告管理" and submenu == u"新增公告":
        if (get_left_menu_count(driver) == 8) or (get_left_menu_count(driver) == 9):
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[6].is_displayed():
                notification_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_notice_w")
                notification_manageBtn.click()
                time.sleep(1)
            notification_addBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[14]
            notification_addBtn.click()
        elif get_left_menu_count(driver) == 10:
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[7].is_displayed():
                notification_manageBtn = driver.find_element_by_css_selector("i.icon_left.icon_notice_w")
                notification_manageBtn.click()
                time.sleep(1)
            notification_addBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[16]
            notification_addBtn.click()
        else:
            print "左侧菜单数量错误！"

    elif menu == u"培训资料" and submenu == u"培训资料":
        if (get_left_menu_count(driver) == 8) or (get_left_menu_count(driver) == 9):
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[7].is_displayed():
                training_manegeBtn = driver.find_element_by_css_selector("i.icon_left.icon_material_w")
                training_manegeBtn.click()
                time.sleep(1)
            training_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[15]
            training_listBtn.click()
        elif get_left_menu_count(driver) == 10:
            if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[8].is_displayed():
                training_manegeBtn = driver.find_element_by_css_selector("i.icon_left.icon_material_w")
                training_manegeBtn.click()
                time.sleep(1)
            training_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[17]
            training_listBtn.click()
        else:
            print "左侧菜单数量错误！"

    else:
        pass

    wait_until_loading_disappeared(driver)
    time.sleep(1)

def open_menu_mis(driver, menu, submenu = ""):
    if menu == u"培训资料" and submenu == u"培训资料":
        if not driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu")[7].is_displayed():
            training_manegeBtn = driver.find_element_by_css_selector("i.icon_left.icon_material_w")
            training_manegeBtn.click()
            time.sleep(1)
        training_listBtn = driver.find_elements_by_css_selector("li.el-submenu > ul.el-menu > li.el-menu-item")[10]
        training_listBtn.click()

    wait_until_loading_disappeared(driver)
    time.sleep(1)

def change_password(driver, old, new):
    name_btn = driver.find_element_by_css_selector("span.name_button")
    name_btn.click()
    change_password_btn = driver.find_element_by_css_selector("i.icon_password")
    change_password_btn.click()
    time.sleep(1)
    old_password = driver.find_element_by_css_selector("label[for='old_password'] + div > div > input")
    old_password.send_keys(old)
    new_password = driver.find_element_by_css_selector("label[for='new_password'] + div > div > input")
    new_password.send_keys(new)
    check_password = driver.find_element_by_css_selector("label[for='check_password'] + div > div > input")
    check_password.send_keys(new)
    check_password.send_keys(Keys.TAB)
    save_password_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_sub.bounced_sub_right")
    save_password_btn.click()
    time.sleep(1)
    back_dg = driver.find_elements_by_css_selector("div.bounced_my_body.big_bounced")[1].find_element_by_css_selector("main > p.bounced_text")
    message = back_dg.text
    confirm_btn = driver.find_element_by_css_selector("span.bounced_button.bounced_cancle")
    confirm_btn.click()
    time.sleep(1)
    name = driver.find_elements_by_css_selector("input.el-input__inner[type='text']")[1]
    if message == u"密码修改成功，请点击“确定”按钮进入登录页重新登陆!" and name :
        success = 1
    else:
        success =0

    return success

def wait_until_loading_disappeared(driver):
    WebDriverWait(driver, 20, 1).until_not(lambda x: x.find_elements_by_id("load_small")[0].is_displayed())


