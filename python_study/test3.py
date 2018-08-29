#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.rand(3, 3)
matrix = matrix * 5

matrix_c = np.ceil(matrix)                     # 上取整
matrix_f = np.floor(matrix)                    # 下取整
matrix_r = np.round(matrix)                    # 四舍五入取整

matrix_l = np.log(matrix_c)                    # 自然数对数
matrix_s = np.square(matrix_f)                 # 平方
matrix_t = np.transpose(matrix_r)              # 转置

matrix_std = np.sum(np.std(matrix_l, 1))       # 标准差的和 （均为按行操作）
matrix_mean = np.sum(np.mean(matrix_s, 1))     # 平均值的和
matrix_med = np.sum(np.median(matrix_t, 1))    # 中位数的和

# 绘制饼状图
sizes = [matrix_std, matrix_mean, matrix_med]  # 计算的三个值 组成 list
labels = 'std', 'mean', 'median'             # 标签
explode = (0.1, 0, 0)                          # 饼图第一部分突出
fig1, ax1 = plt.subplots()
# explode 突出的部分， autopct = automatic percentage 的缩写 自动确定百分比
# 1.1f 表示 1.1 这种格式的浮点数。startangle 开始绘制的角度。
ax1.pie(x=sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')                             # 相等的长宽比确保饼图被绘制为一个圆
plt.show()



'''
要求：
1.随机产生3x3矩阵并乘以 5
2.对矩阵分别进行上取整，下取整，四舍五入取整，产生3个矩阵
3.对矩阵1求自然对数，矩阵2平方，矩阵3转置
4.然后按行，矩阵1求标准差后求和，矩阵2求平均后求和， 矩阵3求中位数后求和
5.以饼状图的形式显示出分布情况
'''

