"""
我想把文件夹内所有的图片都转换成gif
用到的包是哪些?
Python图像处理的包:
Pillow, opencv-python
"""

import os
import imageio
from PIL import Image
import imageio.v2 as imageio
import numpy as np
import subprocess
"""
获得路径文件夹内所有的文件
"""
def get_all(path):
    files = []
    for file in os.listdir(path):
        files.append(os.path.join(path, file))
    return files


"""
将文件夹内的所有jpg文件大小调整一致
"""
def convertjpg(in_path, ou_path, width, height):
    files = get_all(in_path)
    for file in files:
        img = Image.open(file)
        try:
            new_img = img.resize((width, height), Image.BILINEAR)
            if not os.path.exists(ou_path):
                os.mkdir(ou_path)
            # 强制性保证所有的图像文件是同一种shape
            if np.array(img).shape != (width, height, 3):
                continue
            new_img.save(os.path.join(ou_path, os.path.basename(file)))    
        except Exception as e:
            print(e)




def images2gif(files):
    # 首先将所有文件的大小调整一致
    # 其次再将所有大小一一致的文件转换成gif
    images = []
    for file in files:
        images.append(imageio.imread(file))
    imageio.mimsave("./movie.gif", images)

# path = "D:\my_soft\全网（百度）图片下载器\东方淮竹与王权霸业"
# # print(get_all(path=path))
# convertjpg(path, "D:\my_soft\全网（百度）图片下载器\东方", 512, 512)
images2gif(get_all(path="D:\my_soft\全网（百度）图片下载器\东方"))


# windows上写入文件夹,权限问题
path = input("请输入你想要转换gif的图像文件夹: ")
width = int(input("请输入你想要看的gif的宽度: "))
height = int(input("请输入你想要看的gif的高度: "))
ou_path = os.path.join(path, "half")
if not os.path.exists(ou_path):
    os.mkdir(ou_path)
command = f"icacls {ou_path} /grant Everyone:(OI)(CI)F"
subprocess.run(command, shell=True)
convertjpg(path, ou_path, width, height)
images2gif(ou_path)
