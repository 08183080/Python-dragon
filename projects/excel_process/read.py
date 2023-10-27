import pandas as pd

"""
2023/10/27
世人以不动心为耻，
pandas读取excel文件,乱码了。。。
"""
file = 'projects\excel_process\A股公开市场数据.xlsx'
df = pd.read_excel(file, engine='openpyxl')
print(df)