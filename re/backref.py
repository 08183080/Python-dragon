import re

"""
Group capturing and backreference
"""

pattern = r'(\w)\1'
text = 'hello, dragon'

match = re.search(pattern, text)
if match:
    print('匹配到重复的字符:', match.group(0))
    print('捕获的字符:', match.group(1))