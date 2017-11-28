#coding:utf-8
import unittest
import os
import HTMLTestRunner
import sys

#用例路径
case_path = os.path.join(os.getcwd(), "case")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    filename = os.path.join(os.getcwd(), "result.html")
    f = open(filename, "wb")
    runner = unittest.TextTestRunner(stream=f)
    runner.run(all_case())
    f.close()

