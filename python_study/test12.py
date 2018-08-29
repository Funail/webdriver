#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

matrix_value = np.random.randn(100, 3)               # 随机矩阵
X = matrix_value[:, 0]                               # 切片
Y = matrix_value[:, 1]
Z = matrix_value[:, 2]
label = np.random.randint(low=0, high=10, size=100)  # 标签 (0-9)

# 绘图
fig = plt.figure()
ax = Axes3D(fig=fig)
for x, y, z, s in zip(X, Y, Z, label):
    c = cm.rainbow(s/9)                              # s = label 除以9 会得到不同的值，显示不同的颜色
    ax.text(x=x, y=y, z=z, s=s, backgroundcolor=c)
ax.set_xlim(X.min()*1.1, X.max()*1.1)
ax.set_ylim(Y.min()*1.1, Y.max()*1.1)
ax.set_zlim(Z.min()*1.1, Z.max()*1.1)
plt.show()

'''
要求：
1.随机生成服从正态分布的矩阵 形状（100， 3）
2.将矩阵按列切片为 X,Y,Z 的值
3.使用（0-9）之间的数作为标签
4.绘制 3d 图
提示：
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
绘图使用这句：
ax.text(x=x, y=y, z=z, s=s, backgroundcolor=c)
已经不能再详细了哟
'''