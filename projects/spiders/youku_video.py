import re
import time
import requests
import pandas as pd
from youku_get_links import get_all_links

one_url = "https://v.youku.com/v_show/id_XNDI0NzkwNTgyNA==.html?spm=a2hja.12701310.filter.2594&s=07b8722657364fa2a485&s=07b8722657364fa2a485"
comment_url = "https://acs.youku.com/h5/mtop.youku.columbus.ycp.query/1.0"
url = "https://acs.youku.com/h5/mtop.youku.columbus.ycp.query/1.0/?jsv=2.6.1&appKey=24679788&t=1704971068300&sign=c3d6dfddee1ec390f4d1fa886f2ce770&api=mtop.youku.columbus.ycp.query&type=originaljson&v=1.0&ecode=1&dataType=json&data=%7B%22ms_codes%22%3A%222019061000%22%2C%22system_info%22%3A%22%7B%7D%22%2C%22params%22%3A%22%7B%5C%22bizKey%5C%22%3A%5C%22ycp%5C%22%2C%5C%22pageSize%5C%22%3A10%2C%5C%22time%5C%22%3A1704971068297%2C%5C%22app%5C%22%3A%5C%225200-C2cNqy93%5C%22%2C%5C%22objectType%5C%22%3A1%2C%5C%22nodeKey%5C%22%3A%5C%22MAINPAGE_SUBPAGE%5C%22%2C%5C%22page%5C%22%3A5%2C%5C%22objectCode%5C%22%3A%5C%22XNTk3NzEyOTIyMA%3D%3D%5C%22%2C%5C%22utdid%5C%22%3A%5C%22xEjfHP4g7hYCAdvkhxssZXp0%5C%22%2C%5C%22gray%5C%22%3A0%2C%5C%22tabCode%5C%22%3A101%7D%22%2C%22debug%22%3A0%7D"
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
        "Cookie": "isI18n=false; cna=xEjfHP4g7hYCAdvkhxssZXp0; __ysuid=17040947675285Ra; youku_history_word=%5B%22%E6%97%A0%E9%97%B4%E9%81%93%22%5D; l=fBS_NpURPp3wZWupBO5ZKurza77tCLOf1sPzaNbMiIEGB6qsR3Q3JPKQVeYO3lT1WhQNesNwJ3S3hc2kBxYAZyIInxv9-Qy6XFHmndhyN3pR.; __ayft=1704971020661; __aysid=1704971020661uVB; __ayscnt=1; _m_h5_tk=25ea0d967f01680bc0abb8f126959c67_1704975880517; _m_h5_tk_enc=ee0f32d06a6b501db1b106e240e931a5; xlly_s=1; __arpvid=17049710326508YgEfH-1704971032656; __arycid=dc-3-00; __arcms=dc-3-00; __aypstp=2; __ayspstp=2; __ayvstp=3; __aysvstp=3; isg=BFRUMYN2zZih_VnZ8hWrEx3-JZLGrXiXaC8En-4-FV7F2fcjFr9mJhkX2dHBIbDv; tfstk=eYcJ7njYsnxk2TjanQpD8QanvF80db3zl0u1tkqldmnxWobuqzmlOxnI08q7-QrCJmgaV4xeaZDqQ057L9YWOmkZwa2yFaGjH0u_EWcK86UIRD8zxUJmz4PUOhxivC0rziNa-oOiBpyKLWtMjIXcl8-uOYxx0MsbXGIWwO5SNX4WBtG-GkAcizy8fqpNO6L7mGqZPoCCOuHUew07D61IMgPtsfef-GqT-TTvk9WUFrSVFFQLA7KrBrEMyBBFL-84klYvk96CAEzYjULdL9y2u",
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
        "t": "1704971068300",
        "sign": "c3d6dfddee1ec390f4d1fa886f2ce770",
        "api": "mtop.youku.columbus.ycp.query",
        "type": "originaljson",
        "v": "1.0",
        "ecode": "1",
        "dataType": "json",
        "data": {"ms_codes":"2019061000","system_info":"{}","params":"{\"bizKey\":\"ycp\",\"pageSize\":10,\"time\":1704971068297,\"app\":\"5200-C2cNqy93\",\"objectType\":1,\"nodeKey\":\"MAINPAGE_SUBPAGE\",\"page\":5,\"objectCode\":\"XNTk3NzEyOTIyMA==\",\"utdid\":\"xEjfHP4g7hYCAdvkhxssZXp0\",\"gray\":0,\"tabCode\":101}","debug":0}
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
        print(f"处理{url}失败{e}~")
    
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

