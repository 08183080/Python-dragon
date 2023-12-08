import pandas as pd
import requests
from bs4 import BeautifulSoup

MGTV_URL = "https://www.mgtv.com"
MOVIE_URL = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"
COMMENT_URL = "https://comment.mgtv.com/v4/comment/getCommentList"
session = requests.Session()
movie_search_params = {
    "allowedRC": 1,
    "platform": "pcweb",
    "channelId": 3,
    "hudong": 1,
    "kind": "a1",
    "edition": "a1",
    "area": "a1",
    "year": "all",
    "chargeInfo": "a1",
    "sort": "c2",
    "pn": 1,
    "pc": 80,
}
res = session.get(MOVIE_URL, params=movie_search_params)
hit_docs = res.json()["data"]["hitDocs"]


def get_movie_comment(subject_id):
    comment_search_params = {
        "page": 1,
        "subjectType": "hunantv2014",
        "subjectId": subject_id,
    }
    res = session.get(COMMENT_URL, params=comment_search_params)
    # print(res.json())
    comments = res.json()["data"]["list"]
    com = []
    for comment in comments:
        com.append(comment["content"])
    return com


def get_movie_info(hit_doc):
    clip_id = hit_doc["clipId"]
    info = {
        "title": hit_doc["title"],
        "story": hit_doc["story"],
    }
    info_url = f"https://www.mgtv.com/b/{clip_id}.html?lastp=list_index"
    res = session.get(info_url)
    soup = BeautifulSoup(res.text, "html.parser")
    script_tags = soup.find_all("script")
    scr = script_tags[0].get_text()
    subject_id = scr.split("/")[-1].split(".")[0]
    info_detail_url = f"https://www.mgtv.com/b/{clip_id}/{subject_id}.html"
    res = session.get(info_detail_url)
    soup = BeautifulSoup(res.text, "html.parser")
    introduce_items = soup.find_all(class_="introduce-item")
    info["director"] = introduce_items[0].get_text(strip=True).split("：")[-1]
    info["actors"] = introduce_items[1].get_text(strip=True).split("：")[-1]
    info["area"] = introduce_items[2].get_text(strip=True).split("：")[-1]
    info["type"] = introduce_items[3].get_text(strip=True).split("：")[-1]
    info["comment"] = get_movie_comment(subject_id)
    # print(info)
    return info


movie_info_list = []
for hit_doc in hit_docs:
    t = get_movie_info(hit_doc)
    movie_info_list.append(t)
data = pd.DataFrame(movie_info_list)

# 将数据写入 Excel 文件
data.to_excel("movie_info.xlsx", index=False)