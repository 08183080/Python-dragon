import time
import requests

# base_url = "https://youku.com/category/data?session=%7B%22subIndex%22%3A864%2C%22trackInfo%22%3A%7B%22parentdrawerid%22%3A%2234441%22%7D%2C%22spmA%22%3A%22a2h05%22%2C%22level%22%3A2%2C%22spmC%22%3A%22drawer3%22%2C%22spmB%22%3A%228165803_SHAIXUAN_ALL%22%2C%22index%22%3A1%2C%22pageName%22%3A%22page_channelmain_SHAIXUAN_ALL%22%2C%22scene%22%3A%22search_component_paging%22%2C%22scmB%22%3A%22manual%22%2C%22path%22%3A%22EP666420%22%2C%22scmA%22%3A%2220140719%22%2C%22scmC%22%3A%2234441%22%2C%22from%22%3A%22SHAIXUAN%22%2C%22id%22%3A227939%2C%22category%22%3A%22%E7%94%B5%E5%BD%B1%22%7D&params=%7B%22type%22%3A%22%E7%94%B5%E5%BD%B1%22%7D&pageNo=38"
base_url = "https://youku.com/category/data"

def get_all_links():
    headers= {
        "authority": "youku.com",
        "method": "GET",
        "scheme": "https",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Bx-V": "2.5.6",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "isI18n=false; cna=xEjfHP4g7hYCAdvkhxssZXp0; __ysuid=17040947675285Ra; youku_history_word=%5B%22%E6%97%A0%E9%97%B4%E9%81%93%22%5D; csrfToken=2jFXCSrB_4N1qHe8gv8rK2Eg; __ayft=1704158431897; __aysid=1704539138854hkh; __ayscnt=2; xlly_s=1; __arycid=dc-3-00; __arcms=dc-3-00; _m_h5_tk=934df264b78ec023299990fe8264b414_1704619012104; _m_h5_tk_enc=586f8b930c3a5ede9c602d4255aae18f; __arpvid=1704615316368Yybz1c-1704615316376; __aypstp=16; __ayspstp=14; __ayvstp=18; __aysvstp=18; l=fBS_NpURPp3wZ-WQBO5alurza77TrKdf1sPzaNbMiIEGB6StLFb3JPKQVevmv5-PWhQNesMJJ3S3hc2kBxYAZyI9Y5rftQy6XFHmndhyN3pR.; tfstk=e1IWxSqX_bcWHwuoG7wV1Pb8OdKBA_ZN2v9dI9nrp3K8v66NZ48LZ3SCG6C8EeWUEJ1fB1wHz3JUADOAMToyTM_mAOXh48xUE3XkxHFa_l5CETxnH8s7cluMBqXU_5ra0zHvA7NNzVMn7iHIzfrLLTVjmmoIrfIcm47Gxi9WkrWWMt6_LLLS9tRjv5dBFjAOeIiKvgombCtws2MXSD9X_-wj-2mrAd1E3EfILUpDFEybhbQHyKvXsMyjrw8JnLOLh-GRR; isg=BMfHJqWHbsS7BupA5dToWmIPVnuRzJuuJ14XZpmw3tV1CObKoJjP_xmGqshW4HMm",
        "Referer": "https://youku.com/channel/webmovie/list?filter=type_%E7%94%B5%E5%BD%B1&spm=a2hja.14919748_WEBMOVIE_JINGXUAN.drawer3.d_tags_1",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    payload = {
        "session": '{"subIndex":0,"trackInfo":{"parentdrawerid":"34441"},"spmA":"a2h05","level":2,"spmC":"drawer3","spmB":"8165803_SHAIXUAN_ALL","index":1,"pageName":"page_channelmain_SHAIXUAN_ALL","scene":"search_component_paging","scmB":"manual","path":"EP666420","scmA":"20140719","scmC":"34441","from":"SHAIXUAN","id":227939,"category":"电影"}',
        "params": '{"type":"电影"}',
        "pageNo": 123
    }

    for i in range(123):
        urls = []
        try:
            time.sleep(2)
            response = requests.get(base_url, headers=headers, params=payload)
            print(response.text)
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
        with open("youku.txt", "a") as f:
            for url in urls:
                print(url)
                f.write(url)
                f.write("\n")
    # return urls

if __name__ == "__main__":
    get_all_links()
    # get_all_links(base_url)