#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

s = np.arange(start=-5, stop=5, step=0.1, dtype=np.int) # 等比数列 （-5，5） 步长0.1
print(s)
mat_x, mat_y = np.meshgrid(s, s)          # meshgrid 生成两个矩阵
                                          # 接受两个一维数组并产生两个二维矩阵，其值对于两个数组的所有 (x, y) 对
print('matrix_x:', '\n', mat_x, '\n', 'matrix_x shape:', '\n', mat_x.shape)
print('matrix_y:', '\n', mat_y, '\n', 'matrix_y shape:', '\n', mat_y.shape)
z = np.sqrt(mat_x**2 + mat_y**2)          # 矩阵1的平方 加 矩阵2的平方 后 求平方根
plt.imshow(z)                             # 显示图片 带有 colorbar
plt.colorbar()
plt.title("$\sqrt{x^2 + y^2}$")
plt.show()

'''
要求：
1.生成等差数列 范围（-5，5） 步长0.1
2.利用网格函数将等比数列生成两个矩阵 matrix_x, matrix_y
3.将两个矩阵求平方和再求平方根
4.显示求得的矩阵，带有 colorbar 和 title
提示：
title 使用正则表达式写。
'''