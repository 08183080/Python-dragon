"""
转发boss信息到微信助手
"""
from wxpy import *

bot = Bot(cache_path=True)

# 定位公司群
company_group = ensure_one(bot.groups().search('公司微信群'))

# 定位老板
boss = ensure_one(company_group.search('老板大名'))

# 将老板的消息转发到文件传输助手
@bot.register(company_group)
def forward_boss_message(msg):
    if msg.member == boss:
        msg.forward(bot.file_helper, prefix='老板发言')

# 堵塞线程
embed()