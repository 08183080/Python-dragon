import pandas as pd
# import sys
# sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

file = '.\A股公开市场数据.xlsx'
df = pd.read_excel(file, engine='openpyxl')
# print(df)
column_1 = df['证券代码']
column_2 = df['证券简称']
temp0 = [] # 存储市场代码
temp1 = [] # 存储证券代码前6位
temp2 = [] # 存储证券简称
for i in column_1:
    if (i[-2:] == 'SZ'):
        temp0.append('0' + '-')
    else:
        temp0.append('1' + '-')
for i in column_1:
    temp1.append(i[:6])
for i in column_2:
    temp2.append(i + "-")

# 题目2的数据列 
ans1 = [a + b + c for a, b, c in zip(temp0, temp2, temp1)]
print(ans1)
df['代码'] = ans1
with pd.ExcelWriter('.\A股公开市场数据.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

"""
省份一般 都是 两个字的, 除了 内蒙古, 以及一些特殊的 譬如 中国香港
"""
t1 = df['省份']
ans1 = []
for i in t1:
    p = i[:2]
    if i[:3] == '内蒙古':
        p = i[:3]
    if i[:4] == '中国香港':
        p = i[:5]
    # print(p)
    ans1.append(p)
print(ans1)
df['省份信息'] = ans1
with pd.ExcelWriter('.\A股公开市场数据.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False)
