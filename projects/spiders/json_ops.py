import json
"""
json serialization and deserialization

"""

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# 将JSON字符串转换为Python对象
parsed_data = json.loads(json_string)

# 打印转换后的Python对象
print(parsed_data)