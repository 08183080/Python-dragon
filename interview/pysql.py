"""
请用Python完成这样的一个函数:
输入满2件打9折, 返回“满折\2\9;
输入满3件打8折, 返回“满折\3\8;
输入满2件打9折,满3件打8折”, 返回“满折\2\9;满折\3\8;
如果输入 满M1件打C1折,满M2件打C2折,……，返回 满折\M1\C1;满折\M2\C2;
……如何处理？"""



def process_discount_string(discount_string):
    discounts = []
    parts = discount_string.split(',')
    for part in parts:
        if '满' in part and '件打' in part and '折' in part:
            start_index = part.index('满') + 1
            end_index = part.index('件打')
            quantity = part[start_index:end_index]
            start_index = end_index + 2
            end_index = part.index('折')
            percentage = part[start_index:end_index]
            discounts.append(f'满折\\{quantity}\\{percentage};')
    return ''.join(discounts)

# 测试例子
discount_string = '满2件打9折,满3件打8折'
result = process_discount_string(discount_string)
print(result)