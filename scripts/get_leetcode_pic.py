""""
在刷今天的每日一题的时候
我想把题解的110张图片都爬下来合成gif
"""
import requests
import os
from images2gif import get_all, images2gif

dst = "./leetcode_pics"
if not os.path.exists(dst):
    os.mkdir(dst)

for i in range(10):
    url = f"https://assets.leetcode-cn.com/solution-static/146/{i+1}.PNG"
    pic = requests.get(url).content
    name = './leetcode_pics' + f'/{i+1}.png'
    f = open(name, "wb")
    f.write(pic)

images2gif(get_all(dst))
