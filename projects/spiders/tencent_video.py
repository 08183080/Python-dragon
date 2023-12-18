"""
【目标】爬取腾讯视频的介绍, 评论等信息
电影
"""
import re
import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

videos_url = "https://v.qq.com/channel/movie/list"
one_video_url = "https://v.qq.com/x/cover/mzc00200w2oazbl/c0047yg867a.html"  # 某电影的page

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

def get_comment(url):
    """
    通过xhr请求获得评论, 统计评论数量...
    """
    comment_url = "https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?video_appid=3000010&vplatform=2"
    data = {
        "page_params": {
            "req_from": "web",
            "page_type": "channel_operation",
            "page_id": "grade_hot_http",
            "data_key": "cid=mzc00200tfo3aaf",
            "lid": ""
        },
        "has_cache": 1
    }
    response = requests.post(comment_url, json=data, headers=headers).text
    print(response)

def get_content(html_url):
    """
    提取某个page中的关注字段内容
    需求: 视频名称, 视频类型(电影...), 视频类型或内容类型(爱情, 喜剧, ...), 视频简介, 视频语言或国家, 视频内容简介, 视频评分, 热度, 点评数, 用户评价内容
    简化: title, story, type, hot_trend(热度), score(腾讯评分), comment(评论), comment_num
    """
    try:
        response = get_response(html_url).text
        # print(response)
        tree = etree.HTML(response)
        title = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/span/text()")[0]
        hot_trend = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]/text()")[0]
        story = tree.xpath("/html/head/meta[5]/@content")[0]

        # soup 使用起来很简单的... 
        soup = BeautifulSoup(response, 'html.parser')
        script_content = soup.find_all('script')
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
    except Exception as e:
        print(e)
    return title, hot_trend, story, score, categories

print(get_content(one_video_url))
# get_comment(one_video_url)

