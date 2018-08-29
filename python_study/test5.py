#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

matrix_all = []
for i in range(3):
    seed = np.random.RandomState(1234)             # 使用种子的意思就是固定每次随机产生的矩阵都相同
    matrix = seed.rand(3, 3)                       # 产生随机矩阵，循环三次，得到三个完全相同的矩阵。
    matrix_all.append(matrix)                      # 将三个矩阵连接到一起。
    print('matrix ' + str(i) + ':', '\n', matrix)
print('matrix_all :', '\n', matrix_all, '\n', 'shape :', np.shape(matrix_all))

plt.imshow(matrix_all)
plt.show()

'''
要求：
1.随机产生三个完全相同的3x3矩阵
2.输出这三个矩阵
3.输出这三个矩阵形成的3x3x3的三维矩阵。
提示：
生成矩阵时，使用种子控制生成完全相同的矩阵
'''