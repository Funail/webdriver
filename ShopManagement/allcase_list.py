#!-*- coding:utf-8 -*-
'''
方法描述：用例集设置成数组的形式读取
'''
import sys
sys.path.append("\\test_case")
from test_case import *

#用例文件列表
def caselist():
    alltestnames=[
        home.TestHome,
        member.TestMember,
        redpoint.TestRedpoint]
    print "success read case list!"

    return alltestnames