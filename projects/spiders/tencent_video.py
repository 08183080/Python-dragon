"""
【目标】爬取腾讯视频的介绍, 评论等信息
电影
"""
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

videos_url = "https://v.qq.com/channel/movie/list"
one_video_url = "https://v.qq.com/x/cover/mzc00200is68204.html"  # 某电影的page

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

def get_content(html_url):
    """
    提取某个page中的关注字段内容
    需求: 视频名称, 视频类型(电影...), 视频类型或内容类型(爱情, 喜剧, ...), 视频简介, 视频语言或国家, 视频内容简介, 视频评分, 热度, 点评数, 用户评价内容
    简化: title, story, type, hot_trend(热度), score(腾讯评分), comment(评论), comment_num
    """
    try:
        url = "https://otheve.beacon.qq.com/analytics/v2_upload?appkey=JS0081LY3JY6J3"
        requests.post(url, headers=headers)
        response = get_response(html_url).text
        # print(response)
        tree = etree.HTML(response)
        title = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/span/text()")[0]
        hot_trend = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]/text()")[0]
        # type = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[3]")
        story = tree.xpath("/html/head/meta[5]/@content")[0]
        # score = tree.xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/div")

        # script = tree.xpath("/html/head/script[13]/text()")  # script中含有大量相关信息
        # print(script)
        
    except Exception as e:
        print(e)
    return title, hot_trend, story

print(get_content(one_video_url))
