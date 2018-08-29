#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(low=0, high=20, size=(3, 10))   # 随机生成整数矩阵 3x10
list_1 = matrix[0, :]                                      # 切片
list_2 = matrix[1, :]
list_3 = matrix[2, :]

list_u = np.unique(list_1)                                 # 去除相同的值
list_s = np.sort(list_2)                                   # 升序
list_d = list_3[:: -1]                                     # 数列倒序

list_all = np.append(list_u, list_s)                       # 三个数列组合在一起
list_all = np.append(list_all, list_d)

length = len(list_u) + len(list_s) + len(list_d)           # 确定 x轴
x = np.linspace(start=1, stop=length, num=length)

# 绘图 alpha= 透明度。带有网格。
fig, ax = plt.subplots()
ax.fill(x, list_all, color='b', alpha=0.3)
ax.grid(True)
plt.show()

'''
要求：
1.随机产生整数矩阵 维度3x10
2.切片成三个数组
3.数组1 去除相同的值， 数组2 升序排列， 数组3 倒序处理
4.三个数组 组成一个数组
5.绘制填充图，带有网格，透明度 0.3
提示：
由于数组1 进行去除相同值的操作，所以最后数组中的值的个数是不确定的
确定 x轴 的时候要注意保持数值个数一致
'''