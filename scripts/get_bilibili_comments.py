"""
我想获取B站某个视频的所有评论,保存成csv文件
使用哪些库?
requests, time, pandas

2023/9/23
爬取到的评论还比较少,后续再改进
今晚学会了如何快速查看从后端来的json数据的格式
浏览器抓包的时候看Peview大概就能确定从后端来的json数据的格式了

后续建一个url池, 爬取更多的评论
"""
import requests
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

"""
从url返回数据...
"""
def get_response(url):
    res = requests.get(url, headers=headers)
    return res

"""
获取评论真实的发表时间
"""
def get_time(ctime):
    # ctime: 当前时间的时间戳（1970纪元后经过的浮点秒数）
    # 将其格式化为 2023-09-23 21:45类似的样子
    t = time.strftime("%Y-%M-%D %H:%M")
    return t


url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=931227300&type=1&mode=3&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:1,%5C%22direction%5C%22:1,%5C%22data%5C%22:%7B%5C%22pn%5C%22:9%7D%7D%22%7D&plat=1&web_location=1315875&w_rid=c44f283295daf4b3e52c76042b5e6786&wts=1695473739"
res = get_response(url) 
# print(type(res)) # <class 'requests.models.Response'>
res = res.json()
"""
json()方法和json.dumps()的区别
1. json.dumps(): 将Python对象编码成json字符串
2. 将对象json()化
"""
# print(res)


comments = res["data"]["replies"]
# print(comments)
time_list = []
comment_list = [] 
for comment in comments:
    ctime = comment["ctime"]
    t = get_time(ctime)
    message = comment["content"]["message"]
    # print(t, message)
    time_list.append(t)
    comment_list.append(message)

out_file = "./B站半佛评史玉柱.csv"
df = pd.DataFrame({"评论时间": time_list, "评论内容": comment_list})
df.to_csv(out_file, mode="a+", encoding="utf_8_sig", index=False)



