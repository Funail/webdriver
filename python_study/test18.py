#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open(fp='niuniu3.jpg')
img1 = img.convert('L')
img_array = np.array(img1)

img2 = 255 - img_array                   # 对图像进行反相处理
img3 = (100.0/255) * img_array + 100     # 将图像像素值变换到100 - 200 区间
img4 = 255.0 * (img_array/255.0)**2      # 对图像像素值求平方后得到的图像

image = [img1, img2, img3, img4]

fig = plt.figure(figsize=(11, 5))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(4):
    axis = fig.add_subplot(1, 4, i + 1, xticks=[], yticks=[])
    axis.imshow(image[i], plt.cm.gray)
plt.show()


'''
要求：
1.读入图片 由RGB 转换为 L （luminance 亮度）
2.对图片进行反相处理
3.将图片像素值变换到100 - 200 区间
4.对图片像素值求平方后得到图片
5.显示 4 张图片
'''












