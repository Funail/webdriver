#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 15:30
# test_case/test_case_1/start_case_01.py

import unittest
from function.function_01 import *
# 用例
class Case_02(unittest.TestCase):
    u'''哇塞好玩'''
    def setUp(self):
        pass

    def test_zzk(self):
        u'''输入哇塞好玩后点击找找看'''
        search("哇塞好玩")
        print('打印方法名：test_zzk')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()