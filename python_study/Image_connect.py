#!/usr/bin/python3
# encoding=utf-8

import os
import scipy.misc as misc
import matplotlib.pyplot as plt
import matplotlib.image as image

#读入一个文件夹中的所有图片
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.png')]

filelist = get_imlist(r'path')

images = []

for i in filelist:
    img = image.imread(i)
    img_shape = img.shape
    x = img_shape[0]
    reimg = misc.imresize(img, size=(x, 32))

    images.append(img)

#排版显示
fig = plt.figure(figsize=(6, 1))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(3):
    axis = fig.add_subplot(1, 3, i + 1, xticks=[], yticks=[])
    axis.imshow(images[i])
plt.show()
