#!/usr/bin/python
# -*- coding:utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D       # 导入 3D 绘图工具。
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')                  # 获得当前坐标轴，3d形式

# 确定数据
x = np.linspace(start=0, stop=2, num=100)
y = 2 * x + 1
z = x + y

# 绘图
ax.plot(x, y, z, color='b', label='3D Line')
ax.legend()

plt.show()

'''
要求：
1.绘制3d图
2.满足 x范围（0,2），y = 2x + 1, z = x + y
提示：
from mpl_toolkits.mplot3d import Axes3D
'''