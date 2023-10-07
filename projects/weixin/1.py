"""
我又接了个python的单
微信群关键词回复,抢单...

有哪些可以使用的包/工具?
itchat -> wxpy
"""
import wxpy
import os

"""
扫码登录你的wx网页版
【注意】1. 不要开代理, 2. 安装包  pip install itchat-uos==1.5.0.dev0
"""

# 微信登录
def login():
    # 登录微信
    bot = wxpy.Bot(cache_path=True) # Login successfully as xxx
    #本地缓存保存登录信息 
    return bot

# 微信 文件传输助手 发送消息
def wx_file_send(bot):
    bot.file_helper.send("你好,微信")

# 获取某个群的群主, 群成员
def get_group_info(group):
    nums = len(group)
    members = group.members
    owner = group.owner
    print(f"{group} 群主: ", owner)
    print(f"{group} 群成员数目: ", nums)
    for member in members:
        print(member)

bot = login()
wx_file_send(bot)

group = bot.groups().search("快乐")[0]     # 可以模糊搜索
print(group)
cnt = 0
for member in group:
    friend = bot.friends().search(member.name)
    if friend and friend[0] == member:
        print(f"你的好友{member.name}在群中")
        cnt += 1
        # print()
    # print(member.name)
print(cnt)

@bot.register()
def save_images(msg):
    print(msg)
    if msg.type in (wxpy.PICTURE):
        name = print(msg.file_name)
        path = "D:\技术学习\Python-dragon\projects\weixin\download"+ f"\{name}" + ".jpg"
        msg.get_file(path)
        print("下载成功")

wxpy.embed()



