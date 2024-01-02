import time
import requests

base_url = "https://youku.com/category/data?"

def get_all_links():
    page_index = 1
    url = r'https://youku.com/category/data?session={"subIndex":912,"trackInfo":{"parentdrawerid":"34441"},"spmA":"a2h05","level":2,"spmC":"drawer3","spmB":"8165803_SHAIXUAN_ALL","index":1,"pageName":"page_channelmain_SHAIXUAN_ALL","scene":"search_component_paging","scmB":"manual","path":"EP956583","scmA":"20140719","scmC":"34441","from":"SHAIXUAN","id":227939,"category":"电影"}&params={"type":"电影"}&pageNo=39'

    headers= {
        "authority": "youku.com",
        "accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "bx-v": "2.5.6",
        "content-type": "application/x-www-form-urlencoded",
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

    payload = {
        "session": {"subIndex":48,
                    "trackInfo":{"parentdrawerid":"34441"},
                    "spmA":"a2h05",
                    "level":2,
                    "spmC":"drawer3",
                    "spmB":"8165803_SHAIXUAN_ALL",
                    "index":1,
                    "pageName":"page_channelmain_SHAIXUAN_ALL",
                    "scene":"search_component_paging",
                    "scmB":"manual",
                    "path":"EP426561",
                    "scmA":"20140719",
                    "scmC":"34441",
                    "from":"SHAIXUAN",
                    "id":227939,
                    "category":"电影"},
        "params": {"type":"电影"},
        "pageNo": "3"
    }

    urls = []
    try:
        response = requests.get(url, headers=headers)
        # print(response.text)
        data = response.json()
        videos = data['data']['filterData']['listData']
        for video in videos:
            urls.append("https:" + video['videoLink'])
    except requests.exceptions.RequestException as e:
        print(f"处理{url}发生请求异常: ", e)
        time.sleep(1)
    except Exception as e:
        print(f"处理{url}获取link时候出现异常: ", e)
    print(urls[0])
    print(len(urls))
    return urls

if __name__ == "__main__":
    get_all_links()
    # get_all_links(base_url)