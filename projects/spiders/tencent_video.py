"""
【目标】爬取腾讯视频的介绍, 评论等信息
电影
"""
import base64
import json
import re
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

videos_url = "https://v.qq.com/channel/movie/list"
one_video_url = "https://v.qq.com/x/cover/jzibmktk53rsf58/l33395c4t69.html"  # 某电影的page


def get_response(html_url):
    """
    发送请求：
        1. url地址
        2. 请求方式<get post>
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    response = requests.get(url=html_url, headers=headers)
    # <Response [200]>
    # 自动识别编码（智能提示，不需要记...）
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
    ans = f"cid={cid}" #
    # print(ans)
    return ans


def get_comment(url):
    """
    通过xhr请求获得评论, 统计评论数量...
    关键是根据url拿到cid这个唯一参数!
    """
    ans = []
    page_index = 1
    page_size = 10
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
    for page_index in range(1, 10):
        time.sleep(0.2)
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
    print("****")
    print(ans)
    return ans


def get_content(html_url):
    """
    提取某个page中的关注字段内容
    需求: 视频名称, 视频类型(电影...), 视频类型或内容类型(爱情, 喜剧, ...), 视频简介, 视频语言或国家, 视频内容简介, 视频评分, 热度, 点评数, 用户评价内容
    简化: title, story, type, hot_trend(热度), score(腾讯评分), comment(评论), comment_num
    """
    categories = ""
    comments = []
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

        # soup 使用起来很简单的...
        soup = BeautifulSoup(response, "html.parser")
        script_content = soup.find_all("script")
        # print(script_content)
        score_pattern = r"\d+(\.\d+)?分"
        for script in script_content:
            match = re.search(score_pattern, str(script))
            if match:
                score = match.group()
                # print(score)
                break

        pattern = r'"main_genres":\s*"([^"]+)".*?"sub_genre":\s*"([^"]+)"'
        match = re.search(pattern, str(script))
        if match:
            main_genres = match.group(1)
            sub_genre = match.group(2)
            categories = main_genres + "," + sub_genre
            # print(categories)  # 输出: 爱情,喜剧,院线
        comments = get_comment(html_url)
        comments_num = len(comments)
    except Exception as e:
        print(e)
    return title, hot_trend, story, score, categories, comments, comments_num


print(get_content(one_video_url))
# get_comment(one_video_url)
# get_cid(one_video_url)