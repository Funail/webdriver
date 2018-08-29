#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open(fp='niuniu3.jpg')
img_t = Image.Image.transpose(img, method=Image.FLIP_LEFT_RIGHT)    # 左右翻转
img_b = Image.blend(img, img_t, alpha=0.7)                          # 混合两张图片

# 合成两张图片
mask = np.random.randint(low=100, high=255, size=(900, 600))
mask = Image.fromarray(obj=mask, mode='L')
img_c = Image.composite(img, img_t, mask=mask)

image = [img, img_t, img_b, img_c]
fig = plt.figure(figsize=(11, 5))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(4):
    axis = fig.add_subplot(1, 4, i + 1, xticks=[], yticks=[])
    axis.imshow(image[i])
plt.show()

'''
要求：
1.读入图片 左右翻转
2.实现两张图片的混合
3.用另一种方法实现两张图片的混合 mask 为随机生成的整形矩阵
'''