#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import common


'''登录'''
def login_shanghu(driver,login_url,username,password):
    driver.get(login_url)
    time.sleep(2)
    name = driver.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input")
    name.send_keys(username)
    pwd = driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div[1]/input")
    pwd.send_keys(password)
    login_btn = driver.find_element_by_xpath("/html/body/div/div/form/div[3]")
    login_btn.click()


'''退出'''
def logout(driver):
    logout_btn = driver.find_element_by_css_selector("div.user_operation i.icon-ic_logout")
    logout_btn.click()
    time.sleep(1)
    name = driver.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/input")
    if name:
        success = 1
    else:
        success = 0
    return success


'''主菜单数量'''
def get_menu_count(driver):
    menu_count = common.findsCss(driver,"ul.left-nav > li")
    return len(menu_count)


'''会员菜单数量'''
def get_member_menu_count(driver):
    member_menu_count = common.findsCss(driver,"body > div.top_content > div.sidebar > ul > li:nth-child(2) > ul > li")
    return len(member_menu_count)


'''菜单'''
def open_menu(driver,menu,submenu):
    if menu == u"首页概览" and submenu == "":
        home_btn = driver.find_element_by_css_selector("a[href*='/main/index")
        home_btn.click()
        time.sleep(1)

    elif menu == u"会员功能" and submenu == u"会员管理":
        if not driver.find_element_by_css_selector("a[href*='/main/memberctl").is_displayed():
            member_btn = driver.find_element_by_css_selector("i.icon-down_arrow")
            member_btn.click()
            time.sleep(1)
        memberctl_btn = driver.find_element_by_css_selector("a[href*='/main/memberctl")
        memberctl_btn.click()

    elif menu == u"会员功能" and submenu == u"会员集点":
        if not driver.find_element_by_css_selector("a[href*='/main/memberredpoint").is_displayed():
            member_btn = driver.find_element_by_css_selector("i.icon-down_arrow")
            member_btn.click()
            time.sleep(1)
        memberredpoint_btn = driver.find_element_by_css_selector("a[href*='/main/memberredpoint")
        memberredpoint_btn.click()

    elif menu == u"会员功能" and submenu == u"会员红包":
        if not driver.find_element_by_css_selector("a[href*='/main/memberredpacket").is_displayed():
            member_btn = driver.find_element_by_css_selector("i.icon-down_arrow")
            member_btn.click()
            time.sleep(1)
        memberredpacket_btn = driver.find_element_by_css_selector("a[href*='/main/memberredpacket")
        memberredpacket_btn.click()

    elif menu == u"会员功能" and submenu == u"会员储值":
        if not driver.find_element_by_css_selector("a[href*='/main/memberstorage").is_displayed():
            member_btn = driver.find_element_by_css_selector("i.icon-down_arrow")
            member_btn.click()
            time.sleep(1)
        memberstorage_btn = driver.find_element_by_css_selector("a[href*='/main/memberstorage")
        memberstorage_btn.click()

    elif menu == u"交易管理" and submenu == "":
        transctl_btn = driver.find_element_by_css_selector("a[href*='/main/transctl")
        transctl_btn.click()
        time.sleep(1)

    elif menu == u"账单管理" and submenu == "":
        billctl_btn = driver.find_element_by_css_selector("a[href*='/main/billctl")
        billctl_btn.click()
        time.sleep(1)

    elif menu == u"公众号授权" and submenu == "":
        publicauth_btn = driver.find_element_by_css_selector("a[href*='/main/publicauth")
        publicauth_btn.click()
        time.sleep(1)

    elif menu == u"账户信息" and submenu == "":
        chainmanage_btn = driver.find_element_by_css_selector("a[href*='/main/chainmanage")
        chainmanage_btn.click()
        time.sleep(1)
    else:
        print u"左侧菜单错误"
