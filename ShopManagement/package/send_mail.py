# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import unittest
import HTMLTestRunner
import time, os
from email.header import Header

def send_mail(file_new):
    # 设置服务器
    mail_host = "smtp.exmail.qq.com"
    # 发件箱
    mail_from = 'wangfang@qfpay.com'
    # 收件箱
    mail_to = 'wangfang@qfpay.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['From'] = Header("Funail", 'utf-8')
    msg['To'] = Header("测试", 'utf-8')
    # 定义标题
    msg['Subject'] = u"自动化测试报告"
    # 定义发送时间
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器
    smtp.connect(mail_host)
    # 用户名密码mail_host
    smtp.login('wangfang@qfpay.com', 'Wangfang627')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print u'测试报告已发送!'

def send_report(testreport):
    result_dir = testreport
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+fn))
    # print (u'最新测试生成的报告: '+lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    # 调用发邮件模块
    send_mail(file_new)
