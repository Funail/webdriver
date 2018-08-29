#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=9, num=9)                  # 绘图时的 x轴 的值（1-9）
matrix1 = np.random.rand(3, 3)                           # 生成随机矩阵
matrix2 = np.random.normal(loc=0, scale=1, size=(3, 3))  # 生成服从 高斯分布(均值=0，方差=1) 的随机矩阵
matrix3 = np.matmul(matrix1, matrix2)                    # 两矩阵相乘 matmul = matrix multiply 的缩写

# 绝对值操作  abs = absolute 的缩写
matrix_abs1 = np.abs(matrix1)
matrix_abs2 = np.abs(matrix2)
matrix_abs3 = np.abs(matrix3)

# 使用 ravel 将二维矩阵变为一维数组。 reshape 也可以
matrix_1d1 = np.ravel(matrix_abs1)
matrix_1d2 = np.ravel(matrix_abs2)
matrix_1d3 = np.ravel(matrix_abs3)

# 绘图
plt.figure(figsize=(8, 6))
# 第一个子图 柱状图 width = 柱状图的宽
plt.subplot(1, 2, 1)
plt.bar(x, matrix_1d1, width=0.35, color='b')
plt.bar(x + 0.35, matrix_1d2, width=0.35, color='r')      # x + 0.35 移动 x 的值 避免重合。

# 第二个子图 散点图 c = color, s = size (散点的大小)， marker 散点的形状。
plt.subplot(1, 2, 2)
plt.scatter(x, matrix_1d1, color='r', s=100, marker='o')
plt.scatter(x, matrix_1d2, color='b', s=100, marker='s')
plt.scatter(x, matrix_1d3, color='y', s=100, marker='v')

plt.show()

'''
要求：
1.随机生成 矩阵1 维度3x3。
2.生成矩阵2 服从高斯分布 均值为0 方差为1 维度3x3。
3.矩阵1 与 矩阵2 相乘， 得到 矩阵3。
4.将三个矩阵取绝对值。
5.将三个矩阵 转变为一维数组。
6.x轴 范围（1-9），绘制 矩阵1 矩阵2 的柱状图
7.x轴 范围（1-9），绘制 三个矩阵的散点图。
提示：
import numpy as np
import matplotlib.pyplot as plt

矩阵变为一维数组 np.ravel()
散点图 plt.scatter()
柱状图 plt.bar()

'''