#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

# 产生维度 （8，1，1）的3维随机整数矩阵
matrix_3d = np.random.randint(low=0, high=10, size=(8, 1, 1))
array = np.squeeze(matrix_3d)                         # 去除维度为 1 的两个维度 变为array
array_d = np.repeat(a=array, repeats=2)               # 重复每一个元素 变为16个元素
matrix = np.reshape(a=array_d, newshape=(4, 4))       # 变为 4x4 的矩阵
matrix_tra = np.trace(matrix)                         # 求 迹
matrix_dot = np.max(np.cumprod(matrix))               # 累积中的最大值 cumprod=cumulative product
print('matrix_3d:', '\n', matrix_3d)
print('arrar:', '\n', array)
print('array_d:', '\n', array_d)
print('matrix_4x4:', '\n', matrix)
print('trace:', matrix_tra)
print('dot_max:', matrix_dot)


'''
要求：
1.随机生成3维整数矩阵 形状（8，1,1）
2.将 两个为 1 的维度去掉变为 一维数组
3.重复每一个元素变为 16个元素，在变为 4x4的矩阵
4.求 生成的 4x4方阵的迹
5.求方阵累积中的最大值
'''