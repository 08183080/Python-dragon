import re
import time
import random
import requests
import pandas as pd
from youku_get_links import get_all_links

one_url = "https://v.youku.com/v_show/id_XNDI0NzkwNTgyNA==.html?spm=a2hja.12701310.filter.2594&s=07b8722657364fa2a485&s=07b8722657364fa2a485"

ip_pool = []

http_ip_pool = [
    '58.246.58.150:9002',
    '153.101.67.170:9002',
    '112.51.96.118:9001',
    '51.79.229.202:3128',
    '114.55.84.12:30001',
    '111.59.4.88:9002',
    '120.26.0.11:8880',
    '106.14.255.124:80',
    '183.215.23.242:9091',
    '218.57.210.186:9002'
]

https_ip_pool = [
    '111.225.153.13:8089'
]

def get_random_ip(ip_pool):
    return random.choice(ip_pool)

def get_urls(path):
    urls = []
    with open(path, 'r') as f:
        for line in f.readlines():
            urls.append(line.strip())
    # print(urls)
    return urls

def get_conetent(url):
    ip = get_random_ip(https_ip_pool)

    proxies = {
        'http': 'http://' + ip,
        'https': 'https://' + ip
    }

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
    title = None # 名称
    intro = "" # 地区+时间+类型
    desc = "" # 简介
    actors = "" # 演员
    director = "" # 导演
    roles = "" # 相关明星
    heat  = "" # 热度

    title_pattern = r'"videoTitle":\s*"([^"]+)"'
    intro_pattern = r'"introSubTitle":\s*"([^"]+)"'
    desc_pattern = r'"desc":\s*"([^"]+)"'
    heat_pattern = r'"heat"\s*:\s*(\d+)'
    directors_pattern = r'"title":\s*"([^"]+)"' # GG

    fuck_words = "<script>sessionStorage.x5referer = window.location.href;window.location.replace" 

    try:
        response = requests.get(url, headers = headers, proxies = proxies).text
        # print(response)
        
        if fuck_words in response:
            print("进入验证码校验界面了, fuck...") 
            # time.sleep(1)

        m1 = re.search(title_pattern, response)
        if m1:
            title = m1.group(1)
            # print(title)
        
        m2 = re.search(intro_pattern, response)
        if m2:
            intro = m2.group(1)
            # print(intro)

        m3 = re.search(desc_pattern, response)
        if m3:
            desc = m3.group(1)
            # print(desc) 
        
        m4 = re.search(heat_pattern, response)
        if m4:
            heat = m4.group(1)
            # print(heat)

        roles = re.findall(directors_pattern, response)
        roles = roles[2:14] # some data noise
        
        print(f"{title}处理成功...")
        time.sleep(0.2)
        # print(roles)
        # if m5:
        #     director = m5.group()
        #     print(director)
    except Exception as e:
        print(f"处理{url}失败{e}~")
    
    return title, intro, desc, heat, roles

def get_and_write(path, links):
    infos = []

    try:
        for link in links:
            time.sleep(1)
            info = get_conetent(link)
            infos.append(info)
    except Exception as e:
        print(f"处理{link}时候出现异常: ", e)
    
    df = pd.DataFrame(infos, columns = ["title", "intro", "desc", "heat", "roles"])

    try:
        df.to_excel(path,index=False)
        print(f"{path}文件写入{len(df)}条数据!")
    except Exception as e:
        print(f"写入{path}出现错误: ", e)

if __name__ == "__main__":
    # print(get_conetent(one_url))
    # get_urls("youku_film.txt")
    urls = get_urls("youku_film.txt")
    get_and_write("电影.xlsx", urls)
