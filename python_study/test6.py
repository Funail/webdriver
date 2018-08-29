#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

array_1 = np.random.randint(low=1, high=10,size=12)                 # 随机生成两个一维数组
array_2 = np.random.randint(low=0, high=10, size=12)
array_3 = np.unique(array_1)                                        # 去除数组1中重复的元素 得到数组3
array_4 = np.setdiff1d(array_2, array_3)                    # 找出存在于数组2但不在数组3中的元素

print('array1: ', '\n', array_1, '\n', 'array2: ', '\n', array_2)
print('array3: ', '\n', array_3)
print('array4: ', '\n', array_4)

'''
要求：
1.随机生成整数 数组1 数组2
2.去除数组1中重复的元素 得到数组3
3.找出存在于数组2但不在数组3中的元素，得到数组4
'''