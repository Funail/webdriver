#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

img = Image.open(fp='niuniu3.jpg')
r, g, b = img.split()

img_r = r.filter(ImageFilter.GaussianBlur)     # 高斯滤波
img_g = g.filter(ImageFilter.DETAIL)           # 细节滤波
img_b = b.filter(ImageFilter.EDGE_ENHANCE)     # 边缘增强

bands = [img_r, img_g, img_b]
img_m = Image.merge(mode='RGB', bands=bands)      # 融合
image = [img, img_m]

fig = plt.figure(figsize=(6, 5))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(2):
    axis = fig.add_subplot(1, 2, i + 1, xticks=[], yticks=[])
    axis.imshow(image[i])
plt.show()


'''
要求：
1.分离 RGB 三通道
2.对 R 进行高斯滤波 G 进行细节滤波 B 进行边缘增强
3.融合 RGB 得到新的图片
提示：
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
'''