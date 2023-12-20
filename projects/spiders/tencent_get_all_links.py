import requests
from bs4 import BeautifulSoup
"""
和zy进行腾讯会议, 他直接启发我就是拼接, 点点点...
"""

data_url = "https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage?video_appid=3000010"
detail_url = "https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?video_appid=3000010&vplatform=2&vversion_name=8.2.96"

page_index = 1

payload = {
    "page_context": {
        "page_index": f"{page_index}"
    },
    "page_params": {
        "page_id": "channel_list_second_page",
        "page_type": "operation",
        "channel_id": "100173",
        "filter_params": "sort=75",
        "page": f"{page_index}"
    },
    "page_bypass_params": {
        "params": {
            "page_id": "channel_list_second_page",
            "page_type": "operation",
            "channel_id": "100173",
            "filter_params": "sort=75",
            "page": f"{page_index}",
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


cids = []
for page_index in range(1, 10):
    response = requests.post(data_url, headers=headers, json=payload)
    data = response.json()
    cards = data['data']['CardList'][0]['children_list']['list']['cards']
    for card in cards:
        # print(card['params']['cid'])
        cids.append(card['params']['cid'])
    print(cids)
