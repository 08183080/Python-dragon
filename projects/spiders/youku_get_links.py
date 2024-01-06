import time
import requests

# base_url = "https://youku.com/category/data?session=%7B%22subIndex%22%3A48%2C%22trackInfo%22%3A%7B%22parentdrawerid%22%3A%2234441%22%7D%2C%22spmA%22%3A%22a2h05%22%2C%22level%22%3A2%2C%22spmC%22%3A%22drawer3%22%2C%22spmB%22%3A%228165803_SHAIXUAN_ALL%22%2C%22index%22%3A1%2C%22pageName%22%3A%22page_channelmain_SHAIXUAN_ALL%22%2C%22scene%22%3A%22search_component_paging%22%2C%22scmB%22%3A%22manual%22%2C%22path%22%3A%22EP254438%22%2C%22scmA%22%3A%2220140719%22%2C%22scmC%22%3A%2234441%22%2C%22from%22%3A%22SHAIXUAN%22%2C%22id%22%3A227939%2C%22category%22%3A%22%E7%94%B5%E5%BD%B1%22%7D&params=%7B%22type%22%3A%22%E7%94%B5%E5%BD%B1%22%7D&pageNo=3"
base_url = "https://youku.com/category/data"

def get_all_links():
    headers= {
        "authority": "youku.com",
        "method": "GET",
        "accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "bx-v": "2.5.6",
        "content-type": "application/x-www-form-urlencoded",
        "referer": "https://youku.com/channel/webmovie/list?filter=type_%E7%94%B5%E5%BD%B1&spm=a2hja.14919748_WEBMOVIE_JINGXUAN.drawer3.d_tags_1",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origion",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    payload = {
        "session": '{"subIndex":840,"trackInfo":{"parentdrawerid":"34441"},"spmA":"a2h05","level":2,"spmC":"drawer3","spmB":"8165803_SHAIXUAN_ALL","index":1,"pageName":"page_channelmain_SHAIXUAN_ALL","scene":"search_component_paging","scmB":"manual","path":"EP69977","scmA":"20140719","scmC":"34441","from":"SHAIXUAN","id":227939,"category":"电影"}',
        "params": '{"type":"电影"}',
        "pageNo": 36
    }

    urls = []
    try:
        response = requests.get(base_url, headers=headers, params=payload)
        # print(response.text)
        data = response.json()
        # print(data)
        videos = data['data']['filterData']['listData']
        for video in videos:
            urls.append("https:" + video['videoLink'])
    except requests.exceptions.RequestException as e:
        print(f"处理{base_url}发生请求异常: ", e)
        time.sleep(1)
    except Exception as e:
        print(f"处理{base_url}获取link时候出现异常: ", e)
    # print(urls[0])
    print(len(urls))
    for url in urls:
        print(url)
    return urls

if __name__ == "__main__":
    get_all_links()
    # get_all_links(base_url)