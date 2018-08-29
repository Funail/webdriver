#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 绘制 45度 对角线
h = plt.plot(np.arange(0, 10), np.arange(0, 10))

# 设置限制，使其不再在屏幕上看到45度
plt.xlim([-10, 20])

# 绘制文字的区域
l1 = np.array((1, 1))
l2 = np.array((5, 5))

# 旋转角度
angle = 45
trans_angle = plt.gca().transData.transform_angles(np.array((45,)),l2.reshape((1, 2)))[0]
plt.gca().transData.transform_angles()
# 绘制文字
th1 = plt.text(l1[0], l1[1], 'text not on the line', fontsize=16,
               rotation=angle, rotation_mode='anchor')
th2 = plt.text(l2[0], l2[1], 'text on the line', fontsize=16,
               rotation=trans_angle, rotation_mode='anchor')

plt.show()


'''
要求：
1.在图中画一条 y=x 的对角线
2.调整x轴坐标 改变曲线位置
3.使用gca()中的transform_angles 属性是文字在直线上
4.45度角 文字不在直线上
提示：
trans_angle = plt.gca().transData.transform_angles
'''