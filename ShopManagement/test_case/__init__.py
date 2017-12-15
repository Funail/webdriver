#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''把test_case目录添加到path下，这里使用的是相对路劲'''
sys.path.append("\\test_case")
from test_case import test01_home
from test_case import test02_member
from test_case import test03_redpoint
from test_case import test04_redpacket
from package import common

#导入测试文件
import test01_home,test02_member,test03_redpoint,test04_redpacket
