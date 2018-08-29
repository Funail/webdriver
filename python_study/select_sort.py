#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

#直接选择排序

def select_sort(list):
    count = len(list)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if list[min] > list[j]:
                min = j
        list[min], list[i] = list[i], list[min]
    return list

test = np.array([2, 4, 1, 9 , 1, 8, 6, 7, 3, 0])
result = select_sort(test)
print(result)

