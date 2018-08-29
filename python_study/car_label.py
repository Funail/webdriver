#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.xls')]

filename_list = get_imlist(r'C:\Users\Damon\Desktop\car_labels')

all_month_gas = []
all_month_chun =[]
all_month_distance = []
all_month_proportion_gas = []
all_month_proportion_chun = []
month = np.arange(1,11)

for i in filename_list:
    car_labels = pd.read_excel(i)
    #car_labels = pd.read_excel(r'C:\Users\Damon\Desktop\car_labels\1.xls')

    #按车牌号索引的单月单车全部数据
    str = '陕CT8508'
    car_labels_select = car_labels[car_labels['车牌号码'].str.startswith(str)]

    #按燃料类型分类的汽油和甲醇数据
    car_labels_select_gas = car_labels_select[car_labels_select['燃料种类'].str.startswith('汽油')]
    car_labels_select_chun = car_labels_select[car_labels_select['燃料种类'].str.startswith('甲醇')]

    #单车单月汽油与甲醇总量
    single_month_gas = car_labels_select_gas['加注量(L)']
    single_month_gas = np.sum(single_month_gas)
    single_month_chun = car_labels_select_chun['加注量(L)']
    single_month_chun = np.sum(single_month_chun)

    #单车单月总里程数
    single_month_distance = car_labels_select['行驶里程(km)']
    single_month_distance = np.sum(single_month_distance)

    #单车单月甲醇里程数
    single_month_chun_distance = car_labels_select_chun['行驶里程(km)']
    single_month_chun_distance = np.sum(single_month_chun_distance)

    #单车单月汽油里程数
    single_month_gas_distance = car_labels_select_gas['行驶里程(km)']
    single_month_gas_distance = np.sum(single_month_gas_distance)

    #单车单月甲醇里程比
    proportion_gas = np.true_divide(single_month_gas, single_month_gas_distance)
    proportion_chun = np.true_divide(single_month_chun, single_month_chun_distance)

    #数据汇总
    all_month_distance.append(single_month_distance)
    all_month_gas.append(single_month_gas)
    all_month_chun.append(single_month_chun)
    all_month_proportion_gas.append(proportion_gas)
    all_month_proportion_chun.append(proportion_chun)

#绘图
fig, axes = plt.subplots(nrows=2, ncols=3)
ax0, ax1, ax2, ax3, ax4, _ = axes.flatten()

ax0.bar(month, all_month_gas, 0.5, color='red')
ax0.set_title('gas')

ax1.bar(month, all_month_chun, 0.5, color='blue')
ax1.set_title('chun')

ax2.bar(month, all_month_distance, 0.5, color='green')
ax2.set_title('distance')

ax3.bar(month, all_month_proportion_gas, 0.5, color='black')
ax3.set_title('proportion_gas')

ax4.bar(month, all_month_proportion_chun, 0.5, color='red')
ax4.set_title('proportion_chun')

fig.tight_layout()
plt.show()
