#!/usr/bin/python
# -*- coding:utf-8 -*-

#冒泡排序法
import numpy as np

def bubble_sort(list):
    count = len(list)
    for i in range(0, count):
        for j in range(i+1, count):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

test = np.array([2, 1, 6, 3, 9, 6, 0])
print(bubble_sort(test))
