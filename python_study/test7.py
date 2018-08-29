#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

#生成等比数列，变为3x3矩阵。转换数据类型为float型
matrix_1 = np.arange(0, 9).reshape((3, 3)).astype(float)
print('matrix_1:', '\n', matrix_1)
matrix_2 = np.random.randn(3, 3)          # 随机正态分布 3x3矩阵
matrix_2[matrix_2 < 0] = 0                # 小于0的元素变为0
print('matrix_2:', '\n', matrix_2)
for i in range(3):
    matrix_2[i] = i
print('matrix_3:', '\n', matrix_2)

'''
要求：
1.生成如图所示的矩阵1 注意是 float型
2.随机生成 3x3 服从正态分布的矩阵2，将小于0的元素变为0
3.生成如图所示的矩阵3.
'''