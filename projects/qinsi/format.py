"""
加深对format方法的使用
在复杂情况下
在 f-string 中，如果您要嵌入字典或其他复杂对象，可以使用花括号的双花括号形式来转义。
"""
passwd = 123
data = f'{{"user":"111","passwd":{passwd}}}'
print(data)