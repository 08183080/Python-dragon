import os
import pandas as pd

def clean(path):
    df = pd.read_excel(path)
    
    df = df[df['title'].notnull()]
    
    pth = path.split('_')
    print(f"{pth[0]}文件有{len(df)}条数据!")

    out = pth[0] + '_' + str(len(df)) + '条.xlsx'
    df.to_excel(out, index=False)
    print(f"{out}文件保存成功!")
    os.remove(path)

    return len(df)

if __name__ == "__main__":
    d1 = 2564 #clean("动漫_2715条.xlsx")
    d2 = clean("少儿_5048条.xlsx")
    d3 = clean("电影_5060条.xlsx")
    d4 = clean("纪录片_4594条.xlsx")
    d5 = clean("电视剧_3157条.xlsx")
    d6 = clean("综艺_2378条.xlsx")
    print(f"腾讯视频文件们总数据条数{d1+d2+d3+d4+d5+d6}!") # 腾讯视频文件们总数据条数21182!