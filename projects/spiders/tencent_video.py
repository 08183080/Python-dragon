"""
【目标】爬取腾讯视频的介绍, 评论等信息
电影, 电视剧, 动漫, 综艺, 纪录片, 少儿
"""
import base64
import json
import re
import time
import random
import requests
import pandas as pd
import threading
import queue
from lxml import etree

# from tencent_get_all_links import *
from mul_threads_get_links import get_links_with_multithreading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

videos_url = "https://v.qq.com/channel/movie/list"
one_video_url = "https://v.qq.com/x/cover/znda81ms78okdwd/e00242bvw06.html" 


def get_response(html_url):
    """
    发送请求：
        1. url地址
        2. 请求方式<get post>
    """
    response = requests.get(url=html_url, headers=headers)
    response.encoding = response.apparent_encoding
    return response

def get_key(url):
    """
    通过视频url获得唯一参数data_key
    """
    strings = url.split('/')
    # print(strings)
    cid = strings[-2]
    vid = strings[-1].split('.')[0]
    # print(cid, vid)
    ans = f"cid={cid}&vid={vid}"
    # print(ans)
    return ans

def get_comment(url):
    """
    通过xhr请求获得评论, 统计评论数量...
    关键是根据url拿到cid这个唯一参数!
    """
    ans = []
    page_index = 1
    page_size = 30
    comment_url = "https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?video_appid=1000005&vversion_name=1.0.0&vplatform=2&guid=e819249d9650d486&video_omgid=e819249d9650d486"
    data_key = get_key(url)

    sdk_page_ctx = {
        "page_offset": page_index,
        "page_size": page_size,
        "used_module_num": 30,
    }
    payload = {
        "page_params": {
            "data_key": data_key,
            "page_id": "ip_doki_rec",
            "page_type": "channel_operation",
        },
        "page_context": {
            "view_ad_ssp_netmovie_remaining": "0",
            "view_ad_ssp_ad_count_send": "0",
            "view_ad_ssp_netmovie_ad_count_send": "0",
            "data_src_4633c604ae5c40208d634287ebd5b398_ids": "148618793053481233,148618793053721690,148618793044716715,148618793055904877,148618793053427716,148618793055850123,148618793053264201,148618793053253462,148618793170691770,148618793167064028",
            "data_src_4633c604ae5c40208d634287ebd5b398_count": "0",
            "data_src_4633c604ae5c40208d634287ebd5b398_pg_context": "roma_info_list:10901+RERANK+3608|10901+TRIGGER+3608|10901+TRIGGER-LIST+3608|10901+ROUTE-RULE+3608|10901+ACCESS+3608|10901+LOGIC+3608|10901+PROFILE+3608|10901+RANK+3608|&rec_session_id:e819249d9650d486_1702952554&has_next_page:true&page_turn_info:3",
            "view_ad_ssp_ctx_version": "1",
            "view_ad_ssp_netmovie_ctx_version": "1",
            "view_ad_ssp_remaining": "0",
            "view_ad_ssp_cards_consumed": "0",
            "sdk_page_ctx": json.dumps(sdk_page_ctx),
            "page_index": f"{page_index}",
            "view_ad_ssp_netmovie_cards_consumed": "0",
        },
        "has_cache": 0,
    }
    headers = {
        "authority": "pbaccess.video.qq.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": "https://v.qq.com",
        "referer": "https://v.qq.com/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    n = int(random.randint(15, 30))
    for page_index in range(1, n):
        try:
            response = requests.post(comment_url, json=payload, headers=headers).json()

            module_list_datas = response["data"]["module_list_datas"]
            for m in module_list_datas:
                module_datas = m["module_datas"]
                for md in module_datas:
                    item_datas = md["item_data_lists"]["item_datas"]
                    for idatas in item_datas:
                        complex_json = idatas["complex_json"]
                        cj = json.loads(complex_json)
                        # print(json.dumps(cj))
                        encoded_str = cj["content"]["content"]
                        decoded_bytes = base64.b64decode(encoded_str)
                        decoded_text = decoded_bytes.decode("utf-8")
                        # print(decoded_text)
                        ans.append(decoded_text)
        except Exception as e:
            print(e)
            # continue
    return ans


def get_content(html_url):
    """
    提取某个page中的关注字段内容
    需求: 视频名称, 视频类型(电影...), 视频类型或内容类型(爱情, 喜剧, ...), 视频简介, 视频语言或国家, 视频内容简介, 视频评分, 热度, 点评数, 用户评价内容
    """
    title = None
    hot_trend = None
    story = ""
    area = ""
    score = None
    categories = ""
    date = None
    comments_num = 0
    comments = []

    score_pattern = r"\d+(\.\d+)?分"
    type_pattern = r'"main_genres":\s*"([^"]+)"'  
    area_pattern = r'"area_name":\s*"([^"]+)"' 
    date_pattern = r'"publish_date":\s*"([^"]+)"'

    try:
        response = get_response(html_url).text
        # print(response)
        tree = etree.HTML(response)
        title = tree.xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/span/text()"
        )[0]
        hot_trend = tree.xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]/text()"
        )[0]
        story = tree.xpath("/html/head/meta[5]/@content")[0]

        m1 = re.search(score_pattern, response)
        if m1:
            score = m1.group()
            # print(score)

        m2 = re.search(type_pattern, response)
        if m2:
            main_genres = m2.group(1)
            categories = main_genres 
            # print(categories)  
        
        m3 = re.search(area_pattern, response)
        if m3:
            area = m3.group(1)
            # print(area)  

        m4 = re.search(date_pattern, response)
        if m4:
            date = m4.group(1)
            # print(date)      

        comments = get_comment(html_url) # start, end
        comments_num = len(comments)
        print(f"{title}获取完毕!")

    except Exception as e:
        print(f"处理{html_url}出现问题: ", e)
    return title, hot_trend, story, area, score, categories, date,  comments_num, comments


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录函数开始执行的时间
        result = func(*args, **kwargs)  # 执行被装饰的函数
        end_time = time.time()  # 记录函数执行结束的时间
        execution_time = end_time - start_time  # 计算函数的执行时间
        print(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
        return result
    return wrapper

# print(get_content(one_video_url))

def process_page(start, end, links, result_queue):
    infos = []

    for i in range(start, end):
        link = links[i]
        info = get_content(link)
        infos.append(info)
    
    result_queue.put(infos)

def get_and_download(start, end, path):
    links =get_links_with_multithreading(start, end)
    result_queue = queue.Queue()  # 创建一个队列用于存储子线程的结果
    threads = []

    # 分配每个线程要处理的URL数量
    step = len(links) // 12
    for i in range(12):
        start = i * step
        end = start + step if i < 11 else len(links)
        thread = threading.Thread(target=process_page, args=(start, end, links, result_queue))
        thread.start()
        threads.append(thread)

    # 等待所有子线程完成
    for thread in threads:
        thread.join()

    # 从队列中获取所有子线程的结果
    infos = []
    while not result_queue.empty():
        infos.extend(result_queue.get())
    # print(infos)

    data = pd.DataFrame(infos, columns=["title", "hot_trend", "story", "area", "score", "categories", "date", "comments", "comments_num"])
    # print(data)
    data.to_excel(path,index=False)
    print(f"{path}文件写入{len(data)}条数据!")


if __name__ == '__main__':
    # get_and_download(120, 200 "电影_3.xlsx") # 电影完全get
    # get_and_download(180, 200, "动漫_2.xlsx") # 动漫完全get
    # get_and_download(0, 200, "纪录片.xlsx") # 纪录片完全get
    get_and_download(0, 200, "少儿.xlsx") # 少儿