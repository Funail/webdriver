#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#定义字体的属性。
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 16,
        }

#数据和函数
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')

#字体命令。
plt.title('Damped exponential decay', fontdict=font)
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
plt.xlabel('time(s)', fontdict=font)
plt.ylabel('voltage(mV)', fontdict=font)

plt.subplots_adjust(left=0.15)
plt.show()
