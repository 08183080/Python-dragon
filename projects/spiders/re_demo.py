import re
"""
优酷视频
匹配相关明星的正则表达式不是很好设计
"""
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # print(text)
    return text

path = "text.txt"
text = read_file(path)
# print(text)

pattern = r'"subtitle":\s*"[^"]*导演[^"]*"[^"]*"title":\s*"([^"]+)"'
m = re.search(pattern, text)
print(m)
if m:
    print(m.group(1))