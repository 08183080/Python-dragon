import requests
import time
url = "https://mp.weixin.qq.com/s/XRAabLIZu0UViRagfgcJkA"
"""
微信刷阅读量可不简单

手机端阅读量直只接入app端的浏览量
同一个微信id一天看多次, 最多只能刷5次浏览量
想刷阅读量, 谈何容易...
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

for i in range(50):
    response = requests.get(url, headers=headers)
    time.sleep(1)
    print("第{}次请求,响应码{}".format(i + 1 , response.status_code)) 