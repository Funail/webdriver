#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''把test_case目录添加到path下，这里使用的是相对路劲'''
sys.path.append("\\test_case")
from test_case import home
from test_case import member
from test_case import redpoint
from package import common

#导入测试文件
import home,member,redpoint
