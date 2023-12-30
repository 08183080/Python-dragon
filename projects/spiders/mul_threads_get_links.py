import re
import requests
import threading

data_url = "https://pbaccess.video.qq.com/trpc.vector_layout.page_view.PageService/getPage?video_appid=3000010"

def process_page(start, end, result_list):
    """
    电影, 100173
    电视剧, 100113
    动漫, 100119
    纪录片, 100105
    少儿, 100150
    综艺, 100109   sort=46
    """
    cids = []
    urls = []
    urlss = []

    for page_index in range(start, end):
        payload = {
            "page_context": {
                "page_index": f"{page_index}"
            },
            "page_params": {
                "page_id": "channel_list_second_page",
                "page_type": "operation",
                "channel_id": "100150",
                "filter_params": "sort=75",
                "page": f"{page_index}"
            },
            "page_bypass_params": {
                "params": {
                    "page_id": "channel_list_second_page",
                    "page_type": "operation",
                    "channel_id": "100150",
                    "filter_params": "sort=75",
                    "page": f"{page_index}",
                    "caller_id": "3000010",
                    "platform_id": "2",
                    "data_mode": "default",
                    "user_mode": "default"
                },
                "scene": "operation",
                "abtest_bypass_id": "65ffa94b4e3c21c2"
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

        try:
            response = requests.post(data_url, headers=headers, json=payload)
            data = response.json()
            cards = data['data']['CardList'][0]['children_list']['list']['cards']
            for card in cards:
                cids.append(card['params']['cid'])
                url = "https://v.qq.com/x/cover/" + card['params']['cid'] + ".html"
                urls.append(url)
        except Exception as e:
            print(e)

    vid_pattern = r'"vid"\s*:\s*"([^"]+)"'
    for url in urls:
        try:
            response = requests.get(url, headers=headers).text
            match = re.search(vid_pattern, response)
            if match:
                vid = match.group(1)
                urll = url.split(".html")
                urll = urll[0] + "/" + str(vid) + ".html"
                urlss.append(urll)
        except Exception as e:
            print(e)

    result_list.extend(urlss)  # 将结果添加到共享的结果列表中


def get_links_with_multithreading(start, end):
    result_list = []  # 存储结果的列表
    threads = []

    step = (end - start) // 8  # 将区间四等分
    for i in range(8):
        sub_start = start + i * step
        sub_end = sub_start + step if i < 7 else end
        thread = threading.Thread(target=process_page, args=(sub_start, sub_end, result_list))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(result_list)
    return result_list

if __name__ == '__main__':
    links = get_links_with_multithreading(1, 10)
    print(links)