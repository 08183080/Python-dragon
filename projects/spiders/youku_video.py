import re
import time
import requests
from lxml import etree

one_url = "https://v.youku.com/v_show/id_XNTY0ODE0MzU2.html"

"""
UA伪装json模板
origion和referer字段是啥?
origin它指示请求的发起源,即发送请求的网页或者应用程序的源头
referer表示当前请求的上一个网页地址
"""

headers= {
    "authority": "v.youku.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "origin": "https://v.youku.com/",
    "referer": "https://v.youku.com/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

def get_conetent(url):
    title = None # 名称
    intro = "" # 地区+时间+类型
    desc = "" # 简介
    actors = "" # 演员
    directors = "" # 导演
    hot_trend  = "" # 热度

    title_pattern = r'"videoTitle":\s*"([^"]+)"'
    intro_pattern = r'"introSubTitle":\s*"([^"]+)"'
    desc_pattern = r'"desc":\s*"([^"]+)"'

    fuck_words = "<script>sessionStorage.x5referer = window.location.href;window.location.replace" 

    try:
        response = requests.get(url, headers = headers).text
        # print(response)
        
        if fuck_words in response:
            print("进入验证码校验界面了, fuck...") 
            time.sleep(1)

        m1 = re.search(title_pattern, response)
        if m1:
            title = m1.group(1)
            print(title)
        
        m2 = re.search(intro_pattern, response)
        if m2:
            intro = m2.group(1)
            print(intro)

        m3 = re.search(desc_pattern, response)
        if m3:
            desc = m3.group(1)
            print(desc) 
        
    except Exception as e:
        print(f"处理{url}失败~")
    
    return title, intro, desc

get_conetent(one_url)


