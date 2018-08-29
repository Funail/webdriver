#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)

fig, ax = plt.subplots()
# 曲线 dashes(破折号) 的顺序 50个点显示，5个不显示，100个点显示，5个点不显示
line1 = ax.plot(x, np.sin(x), linestyle='-', linewidth=2, color='b', dashes=[50, 5, 100, 5],
                 label='SIN')
# 曲线 dashes(破折号) 的顺序 30个点显示，5个不显示，10个点显示，5个点不显示
line2 = ax.plot(x, np.cos(x), linestyle='-', linewidth=2, color='r', dashes=[30, 5, 10, 5],
                 label='COS')
ax.legend(loc='best')
plt.show()

'''
要求：
绘制 sin cos 曲线，如图
sin：曲线 dashes(破折号) 的顺序 50个点显示，5个不显示，100个点显示，5个点不显示
cos：曲线 dashes(破折号) 的顺序 30个点显示，5个不显示，10个点显示，5个点不显示
'''