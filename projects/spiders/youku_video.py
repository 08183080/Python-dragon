import re
import time
import requests
import pandas as pd
from youku_get_links import get_all_links

one_url = "https://v.youku.com/v_show/id_XNDI0NzkwNTgyNA==.html?spm=a2hja.12701310.filter.2594&s=07b8722657364fa2a485&s=07b8722657364fa2a485"
comment_url = "https://acs.youku.com/h5/mtop.alidme.xtop.tv.order.status.get/1.0"
url = 'https://acs.youku.com/h5/mtop.youku.columbus.ycp.query/1.0/?jsv=2.6.1&appKey=24679788&t=1704726300934&sign=ce1278e095528c2db6d8333eca4e6b84&api=mtop.youku.columbus.ycp.query&type=originaljson&v=1.0&ecode=1&dataType=json&data=%7B%22ms_codes%22%3A%222019061000%22%2C%22system_info%22%3A%22%7B%7D%22%2C%22params%22%3A%22%7B%5C%22bizKey%5C%22%3A%5C%22ycp%5C%22%2C%5C%22pageSize%5C%22%3A10%2C%5C%22time%5C%22%3A1704726300934%2C%5C%22app%5C%22%3A%5C%225200-C2cNqy93%5C%22%2C%5C%22objectType%5C%22%3A1%2C%5C%22nodeKey%5C%22%3A%5C%22MAINPAGE_SUBPAGE%5C%22%2C%5C%22page%5C%22%3A2%2C%5C%22objectCode%5C%22%3A%5C%22XNjAzOTM3ODY2MA%3D%3D%5C%22%2C%5C%22utdid%5C%22%3A%5C%22xEjfHP4g7hYCAdvkhxssZXp0%5C%22%2C%5C%22gray%5C%22%3A0%2C%5C%22tabCode%5C%22%3A101%7D%22%2C%22debug%22%3A0%7D'

"""
UA伪装json模板
origion和referer字段是啥?
origin它指示请求的发起源,即发送请求的网页或者应用程序的源头
referer表示当前请求的上一个网页地址
"""

def get_comment():
    """
    获取视频的评论
    """
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "isI18n=false; cna=xEjfHP4g7hYCAdvkhxssZXp0; __ysuid=17040947675285Ra; youku_history_word=%5B%22%E6%97%A0%E9%97%B4%E9%81%93%22%5D; __ayft=1704158431897; __aysid=1704539138854hkh; __ayscnt=2; xlly_s=1; __arycid=dc-3-00; __arcms=dc-3-00; l=fBS_NpURPp3wZWupBO5ZKurza77tCLOf1sPzaNbMiIEGB6qsR3Q3JPKQVeYO3lT1WhQNesNwJ3S3hc2kBxYAZyIInxv9-Qy6XFHmndhyN3pR.; _m_h5_tk=e716162ff851dd1f47dccdfe4218aea4_1704727826654; _m_h5_tk_enc=3aa6f735a901cb95121fa1a0916c5197; __arpvid=1704724116959Z3jZIN-1704724116964; __aypstp=18; __ayspstp=16; __ayvstp=27; __aysvstp=27; tfstk=eczy7hsktaQPg4R_4m0E7StWnX3-BVB6-yMItWVnNYDoOWb3L5wJVDX-Pyy4_oL7d4T73wyTDpnKp8M0D7zwNYHL2w4YRjSoxyMQ86u8luTIFT3UtRgFCO_157F-k2X1CNCyrq0dP55KJNN8wIAyK1Zc5e5I7Tsb_ACHYUmOI5H0oOlGRi-kdxYH-zbK4A-Ipjh4uknrIm2w-maqa0kgZgzHpjbsWyEyKHooMjk1gskwYDVJOw0bIHKKmVhqC_GWvHnoGetz7FxpvmcrgA1WS; isg=BI-P9j-hNhprkjLo_fwgcvqXHiOZtOPWr_bvjqGbAf8icK1yqYfHJ_MmcqBOCLtO",
        "Host": "acs.youku.com",
        "Origin": "https://v.youku.com",
        "Referer": "https://v.youku.com/v_show/id_XNTk3NzEyOTIyMA==.html?lang=%E8%8B%B1%E8%AF%AD&spm=a2hje.13141534.1_4.d_1_21&scm=20140719.apircmd.239009.video_XNTk3NzEyOTIyMA==",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    } # headers伪装ok

    payload = {
        "jsv": "2.6.1",
        "appKey": "24679788",
        "t": "1704724129394",
        "sign": "5d680eaae12b7d35ee71456a3b1260d0",
        "api": "mtop.youku.ycp.comment.detailpage.module.get",
        "type": "originaljson",
        "v": "1.0",
        "ecode": "1",
        "dataType": "json",
        "data": '{"app":"100-DDwODVkv","time":1704724129393,"objectCode":"XNTk3NzEyOTIyMA==","objectType":1,"dataSource":"COMMENT_REPLY_LIST_DATASOURCE","page":1,"limit":2,"lastId":false,"bizParam":"{\"commentId\":1000907380228}","sign":"1cba82f56cf3300ed0218482dddd1dd2"}'
    }

    response = requests.get(url, headers=headers)
    print(response.text)

def get_conetent(url):
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
        
        print(f"{title}处理成功...")
        time.sleep(0.2)
        # print(roles)
        # if m5:
        #     director = m5.group()
        #     print(director)
    except Exception as e:
        print(f"处理{url}失败~")
    
    return title, intro, desc, heat, roles

def get_and_write(path):
    infos = []
    links = get_all_links()

    try:
        for link in links:
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
    # get_and_write("电影.xlsx")
    get_comment()