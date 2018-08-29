#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-np.pi, stop=np.pi, num=256)          # 定义 -pi到 pi ， 区间内256个取值
y = np.sin(x)

plt.figure(figsize=(8, 6))           # 定义一个图， 面积 8x6
plt.subplot(1, 1, 1)   # 在 图中的子图为 一个
# 相关属性设置 曲线颜色  宽度 风格 图例  都是英文单词
plt.plot(x, y, color='blue', linewidth=2.5, linestyle='-', label='SIN')
plt.legend(loc='upper right')     # 设置图例的位置 ，右上角
plt.ylim(y.min() * 1.1, y.max() * 1.1)   # 设置 y轴的取值范围 -1.1 - 1.1
plt.show()

