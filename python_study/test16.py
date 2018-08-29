#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(fp="niuniu.jpg")
# 输出图片属性
print('format:', img.format, '\n', 'size:', img.size, '\n', 'mode:', img.mode)
# 分割 RGB 通道
r, g, b = Image.Image.split(img)
image = [img, r, g, b]
fig = plt.figure(figsize=(11, 5))
# 调整子图在 figure中的位置 left right bottom top 取值均在（0 - 1）0表示最左最下 1表示最右最上
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(4):
    # 添加子图 1行4列，去除坐标轴的刻度
    axis = fig.add_subplot(1, 4, i + 1, xticks=[], yticks=[])
    axis.imshow(image[i])
plt.show()

'''
要求：
1.读入图片 输出图片属性
2.分 R G B 三通道显示
3.注意绘图的格式
提示：
from PIL import Image
import matplotlib.pyplot as plt
'''