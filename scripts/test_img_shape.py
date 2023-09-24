from PIL import Image
import numpy as np
import os
"""
测试文件夹下的一系列图像哪个是数据维度不一样的图片?
"""

# 获取路径下的所有文件
def get_all(path):
    files = []
    for file in os.listdir(path):
        files.append(os.path.join(path, file))
    return files

# 检查一张图片的shape
def check(img):
    img = Image.open(img)
    img_array = np.array(img)
    shape = img_array.shape
    print("img:", shape)

path = "D:\my_soft\全网（百度）图片下载器\东方" # 输入你想要查询的图像文件夹
files = get_all(path)
for img in files:
    print(img)
    check(img)


    