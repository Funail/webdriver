#!-*- coding:utf-8 -*-

#使用相对路劲把test目录添加到path下
import time
import unittest

import HTMLTestRunner

import allcase_list
from package import send_mail

#创建测试容器
testunit=unittest.TestSuite()


#获取数组文件
alltestnames=allcase_list.caselist()

#循环读取数组中的用例
for db in alltestnames:
    testunit.addTest(unittest.makeSuite(db))


#获取现在的时间
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#定义报告存放路径
testreport = 'report/'
filename = testreport + now + '_all_Tests.html'
fp = file(filename,'wb')
#定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
        #报告写入的文件
        stream = fp,
        #报告标题
        title = u'商户管理后台测试报告',
        #报告的说明与描述
        description = u'用例执行情况')

#执行用例
runner.run(testunit)
fp.close()

# send_mail.send_report(testreport)

