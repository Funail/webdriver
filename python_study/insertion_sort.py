#!/usr/bin/python
# -*- coding:utf-8 -*-

#插入排序法
import numpy as np

list = np.array([1, 2, 4, 9, 5, 2, 8, 6])
def insert_sort(list):
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j = j - 1

    return list
test = insert_sort(list=list)
print(test)
