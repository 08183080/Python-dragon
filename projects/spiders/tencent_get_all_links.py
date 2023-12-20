import requests
from bs4 import BeautifulSoup

url = "https://v.qq.com/channel/movie/list"
data_url = "https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage?video_appid=3000010"

payload = {
    "page_context": {
        "page_index": "5"
    },
    "page_params": {
        "page_id": "channel_list_second_page",
        "page_type": "operation",
        "channel_id": "100173",
        "filter_params": "sort=75",
        "page": "5"
    },
    "page_bypass_params": {
        "params": {
            "page_id": "channel_list_second_page",
            "page_type": "operation",
            "channel_id": "100173",
            "filter_params": "sort=75",
            "page": "5",
            "caller_id": "3000010",
            "platform_id": "2",
            "data_mode": "default",
            "user_mode": "default"
        },
        "scene": "operation",
        "abtest_bypass_id": "24d0246cdbfebc53"
    }
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

# response = requests.post(url, json=payload, headers=headers).json()
# print(response)
"""
所有视频的超链接并不在异步加载的json中, 而是在异步加载的界面中的a标签中
"""

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")

