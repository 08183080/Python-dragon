import requests

url = "https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage"

params = {
    "video_appid": 3000010
}

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Length": "473",
    "Content-Type": "application/json",
    "Origin": "https://v.qq.com",
    "Referer": "https://v.qq.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

cookies = {
    "Cookie": "pac_uid=0_9a8a05230a96b; iip=0; _qimei_uuid42=17b1615163910059893aa9c38dcb253ccbd55d061e; _qimei_fingerprint=2b49e08118848b8d4d38f2818275a34e; _qimei_q36=; _qimei_h38=e1473c48893aa9c38dcb253c02000001217b16; pgv_pvid=734018209; qq_domain_video_guid_verify=65ffa94b4e3c21c2; video_platform=2; video_guid=65ffa94b4e3c21c2; _clck=3947319011|1|fhj|0; pgv_info=ssid=s8307550268; vversion_name=8.2.95; video_omgid=65ffa94b4e3c21c2"
}

payload = {
    "page_context": {
        "page_index": "130"
    },
    "page_params": {
        "page_id": "channel_list_second_page",
        "page_type": "operation",
        "channel_id": "100173",
        "filter_params": "sort=75",
        "page": "130"
    },
    "page_bypass_params": {
        "params": {
            "page_id": "channel_list_second_page",
            "page_type": "operation",
            "channel_id": "100173",
            "filter_params": "sort=75",
            "page": "130",
            "caller_id": "3000010",
            "platform_id": "2",
            "data_mode": "default",
            "user_mode": "default"
        },
        "scene": "operation",
        "abtest_bypass_id": "65ffa94b4e3c21c2"
    }
}

proxies = {
    "http_proxy": "http://127.0.0.1:7890"
}

response = requests.post(url=url, params=params, data=payload, cookies=cookies, headers=headers)
print(response.status_code)
print(response.json())