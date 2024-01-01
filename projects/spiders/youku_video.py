import re
import time
import requests

url = "https://www.youku.com/category/data?session=%7B%22subIndex%22%3A48%2C%22trackInfo%22%3A%7B%22parentdrawerid%22%3A%2234441%22%7D%2C%22spmA%22%3A%22a2h05%22%2C%22level%22%3A2%2C%22spmC%22%3A%22drawer3%22%2C%22spmB%22%3A%228165803_SHAIXUAN_ALL%22%2C%22index%22%3A1%2C%22pageName%22%3A%22page_channelmain_SHAIXUAN_ALL%22%2C%22scene%22%3A%22search_component_paging%22%2C%22scmB%22%3A%22manual%22%2C%22path%22%3A%22EP967584%22%2C%22scmA%22%3A%2220140719%22%2C%22scmC%22%3A%2234441%22%2C%22from%22%3A%22SHAIXUAN%22%2C%22id%22%3A227939%2C%22category%22%3A%22%E5%8A%A8%E6%BC%AB%22%7D&params=%7B%22type%22%3A%22%E5%8A%A8%E6%BC%AB%22%7D&pageNo=3"
one_url = "https://v.youku.com/v_show/id_XNTk4MDM2MTc4NA==.html?spm=a2hja.12701310.filter.4212&s=dcaed107ed44453089fe"

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
        response = requests.get(url, headers = headers).text
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
        # print(roles)
        # if m5:
        #     director = m5.group()
        #     print(director)
    except Exception as e:
        print(f"处理{url}失败~")
    
    return title, intro, desc, heat, roles

def get_all_links(url):
    payload = {
        "session": {"subIndex":48,"trackInfo":{"parentdrawerid":"34441"},"spmA":"a2h05","level":2,"spmC":"drawer3","spmB":"8165803_SHAIXUAN_ALL","index":1,"pageName":"page_channelmain_SHAIXUAN_ALL","scene":"search_component_paging","scmB":"manual","path":"EP400885","scmA":"20140719","scmC":"34441","from":"SHAIXUAN","id":227939,"category":"电影"},
        "params": {"type":"电影"},
        "pageNo": "1"
    }
    url = ""
    urls = []
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        videos = data['data']['filterData']['listData']
        for video in videos:
            url = "https:" + video['videoLink']
            print(url)
            urls.append(url)
    except Exception as e:
        print(f"处理{url}获取link时候出现问题...")
    return urls
    

if __name__ == "__main__":
    print(get_conetent(one_url))
    # get_all_links(url)