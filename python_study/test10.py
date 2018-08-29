#!/usr/bin/python
# -*- coding:utf-8 -*-

s = [x**2 for x in range(10)]
list_t = [(x, y) for x in [1, 2, 3] for y in [2, 5, 8] if x != y]     # 创建成对的不相等的元组
list = [-4, -2, 0, 2, 4]
list_pow = [x**2 for x in list]                                              # 元素平方
list_abs = [abs(x) for x in list]                                            # 绝对值
list_ge = [x for x in list if x >= 0]                                       # 条件判断
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1d = [ele for i in matrix for ele in i]                              # 压缩成一维
matrix_t = [[row[i] for row in matrix] for i in range(3)]                    # 转置
print('list_1 :', '\n', s, '\n', 'list_2 :', '\n', list_t)
print('list :', '\n', list, '\n', 'list_pow :', '\n', list_pow)
print( 'list_abs :', '\n', list_abs)
print('list_ge :', '\n', list_ge)
print('matrix :', '\n', matrix)
print('matrix_1d :', '\n', matrix_1d)
print('matrix_t :', '\n', matrix_t)

'''
要求：
1.使用 for 生成 list_1
2.使用 for 生成 list_2
3.定义list=[-4, -2, 0, 2, 4] 求平方 绝对值 去除小于0的数
4.定义矩阵 matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 压缩成一维 转置
提示：
不能使用任何库 只使用Python中的语句
答案都在小薄书里哟。
'''