#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random

'''大商户登录账号'''
login_url = "https://sh.qfpay.com"
username = "14200000060"
password = "1234567890"

'''会员集点数据'''
dict1 = {"require_amount":str(random.randint(1,20)),"present_name":u"泰迪熊","present_amount":str(random.randint(1,20))}