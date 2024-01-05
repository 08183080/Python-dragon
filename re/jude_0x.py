import re

text = r'0xaffe, 123, 0xFFFFF'
hex_pattern = r'0x[0-9a-fA-F]+'

m = re.findall(hex_pattern, text)
if m:
    print(m)