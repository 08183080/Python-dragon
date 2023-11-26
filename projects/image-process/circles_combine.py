"""
需求: 将裁剪得到的如是多的小圆拼接成一张图片
实现:
我统计了一下已总共有204张图片目前, 可以选取196张(14*14)
然后这些小正方形图片满足shape的min是36, max是58, 可以统一拉大为58
"""
import os
import math
import cv2 as cv
import numpy as np
from PIL import Image

def get_all(path):
    files = []
    for file in os.listdir(path):
        files.append(os.path.join(path, file))
    return files

def convertpng(in_path, ou_path, width, height):
    files = get_all(in_path)
    for file in files:
        img = Image.open(file)
        try:
            new_img = img.resize((width, height), Image.BILINEAR)
            if not os.path.exists(ou_path):
                os.mkdir(ou_path)
            # 强制性保证所有的图像文件是同一种shape
            # if np.array(img).shape != (width, height, 3):
            #     continue
            new_img.save(os.path.join(ou_path, os.path.basename(file)))    
        except Exception as e:
            print(e)

def combine_images(path):
    """
    将图片们都拼接起来
    """
    image_files = get_all(path)

    num_images = len(image_files)
    side_length = 14 # math.ceil(math.sqrt(num_images))
    adjust_size = 60

    combined_image = Image.new("RGB", (side_length * adjust_size, side_length * adjust_size))

    # 拼接图像
    x_offset = y_offset = 0
    for image_file in image_files:
        image = Image.open(image_file)
        image = image.resize((adjust_size, adjust_size), Image.BILINEAR)
        combined_image.paste(image, (x_offset, y_offset))
        x_offset += adjust_size
        if x_offset >= side_length * adjust_size:
            x_offset = 0
            y_offset += adjust_size

    # 保存拼接后的图像
    combined_image.save("all.png")


# in_path = "D:\Python\Python\projects\image-process\\tiny_circles"
ou_path = "D:\Python\Python\projects\image-process\\resize_circles"
# convertpng(in_path, ou_path, 100, 100)
combine_images(ou_path)



