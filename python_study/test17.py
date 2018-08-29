#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt

# 读入三张图片
img = Image.open(fp="niuniu.jpg")
img2 = Image.open(fp="niuniu2.jpg")
img3 = Image.open(fp="niuniu33.jpg")

# 对 img2 进行裁剪 旋转操作
box = (220, 200, 500, 600)       # (左 上 右 下)
img2_crop = img2.crop(box)
img2_crop_r = img2_crop.rotate(15)
img.paste(img2_crop_r, (100, 100))

# img3 调整大小 img2 和 img3 粘到 img
img3_re = Image.Image.resize(img3, size=(400, 600))
img.paste(img3_re, (800, 1200))

plt.imshow(img)
plt.show()

'''
要求：
1.读入三张图片
2.图2 进行裁剪 旋转操作
3.图3 改变大小
4.将操作后的 图2 图3 粘到图1
'''




