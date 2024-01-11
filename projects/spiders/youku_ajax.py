import requests
"""
虫师 谢乾坤 建议:
1. code imported by python requests
2. 大佬帮我分析 归因到 时间戳问题timestamp
3. 我要学学js逆向, 逆向出sign 
"""
url = "https://acs.youku.com/h5/mtop.youku.columbus.ycp.query/1.0/?jsv=2.6.1&appKey=24679788&t=1704971068300&sign=c3d6dfddee1ec390f4d1fa886f2ce770&api=mtop.youku.columbus.ycp.query&type=originaljson&v=1.0&ecode=1&dataType=json&data=%7B%22ms_codes%22%3A%222019061000%22%2C%22system_info%22%3A%22%7B%7D%22%2C%22params%22%3A%22%7B%5C%22bizKey%5C%22%3A%5C%22ycp%5C%22%2C%5C%22pageSize%5C%22%3A10%2C%5C%22time%5C%22%3A1704971068297%2C%5C%22app%5C%22%3A%5C%225200-C2cNqy93%5C%22%2C%5C%22objectType%5C%22%3A1%2C%5C%22nodeKey%5C%22%3A%5C%22MAINPAGE_SUBPAGE%5C%22%2C%5C%22page%5C%22%3A5%2C%5C%22objectCode%5C%22%3A%5C%22XNTk3NzEyOTIyMA%3D%3D%5C%22%2C%5C%22utdid%5C%22%3A%5C%22xEjfHP4g7hYCAdvkhxssZXp0%5C%22%2C%5C%22gray%5C%22%3A0%2C%5C%22tabCode%5C%22%3A101%7D%22%2C%22debug%22%3A0%7D"

payload = {}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-type': 'application/x-www-form-urlencoded',
  'Cookie': 'isI18n=false; cna=xEjfHP4g7hYCAdvkhxssZXp0; __ysuid=17040947675285Ra; youku_history_word=%5B%22%E6%97%A0%E9%97%B4%E9%81%93%22%5D; l=fBS_NpURPp3wZWupBO5ZKurza77tCLOf1sPzaNbMiIEGB6qsR3Q3JPKQVeYO3lT1WhQNesNwJ3S3hc2kBxYAZyIInxv9-Qy6XFHmndhyN3pR.; __ayft=1704971020661; __aysid=1704971020661uVB; __ayscnt=1; _m_h5_tk=25ea0d967f01680bc0abb8f126959c67_1704975880517; _m_h5_tk_enc=ee0f32d06a6b501db1b106e240e931a5; xlly_s=1; __arpvid=17049710326508YgEfH-1704971032656; __arycid=dc-3-00; __arcms=dc-3-00; __aypstp=2; __ayspstp=2; __ayvstp=3; __aysvstp=3; isg=BFRUMYN2zZih_VnZ8hWrEx3-JZLGrXiXaC8En-4-FV7F2fcjFr9mJhkX2dHBIbDv; tfstk=eYcJ7njYsnxk2TjanQpD8QanvF80db3zl0u1tkqldmnxWobuqzmlOxnI08q7-QrCJmgaV4xeaZDqQ057L9YWOmkZwa2yFaGjH0u_EWcK86UIRD8zxUJmz4PUOhxivC0rziNa-oOiBpyKLWtMjIXcl8-uOYxx0MsbXGIWwO5SNX4WBtG-GkAcizy8fqpNO6L7mGqZPoCCOuHUew07D61IMgPtsfef-GqT-TTvk9WUFrSVFFQLA7KrBrEMyBBFL-84klYvk96CAEzYjULdL9y2u',
  'Origin': 'https://v.youku.com',
  'Referer': 'https://v.youku.com/v_show/id_XNTk3NzEyOTIyMA==.html?lang=%E8%8B%B1%E8%AF%AD&spm=a2hje.13141534.1_4.d_1_21&scm=20140719.apircmd.239009.video_XNTk3NzEyOTIyMA==',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
