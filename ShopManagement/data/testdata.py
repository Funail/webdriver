#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random

'''大商户登录账号'''
login_url = "https://1.sh.qfpay.com"
# login_url = "https://sh.qfpay.com"
username = "14200000080"
password = "123456"

'''会员集点数据'''
dict1 = {"require_amount":str(random.randint(1,20)),
         "present_name":u"泰迪熊",
         "present_amount":str(random.randint(1,20))}
dict2 = {"require_amount":str(random.randint(1,20)),
         "present_name":u"泰迪狗",
         "present_amount":str(random.randint(1,20))}

'''会员红包数据'''
# 红包通知数据
dict3= {"common_amount":str(random.randint(1,5)),
        "common_requirement_amount":str(random.randint(5,20))}

# 消费返红包数据
dict4= {"payment_name":u"测试消费返红包",
        "payment_amount":str(random.randint(1,3)),
        "payment_number":str(random.randint(3,6)),
        "payment_reveive_amount":str(random.randint(1,3)),
        "payment_requirement_amount":str(random.randint(3,6)),
        "payment_date": str(random.randint(2,5))}

# 分享红包数据
dict5= {"share_name":u"测试分享红包",
        "share_amount1":str(random.randint(1,2)),
        "share_amount2":str(random.randint(3,4)),
        "share_total_amount":str(random.randint(10,20)),
        "share_reveive_amount":str(random.randint(1,3)),
        "share_requirement_amount":str(random.randint(5,8)),
        "share_date": str(random.randint(2,5))}


'''会员储值数据'''
dict6= {"store_amount":str(random.randint(10,20)),
        "extra_amount":str(random.randint(1,5)),
        "remark":u"测试储值活动备注",
        "phone_number": "150" + str(random.randint(0, 99999999)).zfill(8),
        "share_reveive_amount":str(random.randint(1,3)),
        "share_requirement_amount":str(random.randint(5,8)),
        "share_date": str(random.randint(2,5))}