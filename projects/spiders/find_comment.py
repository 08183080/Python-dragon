import base64
"""
腾讯视频的评论是base64编码的...
"""

encoded_str = "5b6L5biI5LuW5aaI6LCB5Y675pWR6LWO77yf"
decoded_bytes = base64.b64decode(encoded_str)
decoded_text = decoded_bytes.decode('utf-8')

print(decoded_text)