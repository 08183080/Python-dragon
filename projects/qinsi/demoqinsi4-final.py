import requests
import json
import time
import datetime
import pandas
import numpy as np
import jinja2
import xlrd

"""
2023-10-16
人生, 真是寂寞如雪呀...
【需求】帮客户解决好登录获取数据,数据处理, 存储excel问题
【难点】
1. 必须要和客户沟通, 了解清楚业务逻辑, 沟通第一, 客户第一
2. verify=False解决https的连接错误
3. 通过不断获取最新cookie解决登录问题
"""

proxy = {'http':"","https":""}

def login():
    headers = {
        "Referer":"https://web.qinsilk.com/is/admin/loginOut.ac?mid=1&",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Cookie":"lastUser=15100211300; lastAutoLoginCheck=true; JSESSIONID=3FA575B85460BB668BD60C3FF8E53CB5; _ati=3215790475175; qs_sys=is; p_h5_u=9C899F0C-AC26-4AE2-8C71-52A1AA78BA7D; _pk_id.1.bc87=cb5b1f4f2780bcf0.1696225744.; Hm_lvt_bf3296661a119dc2e4c3427b339b6d9e=1696225743,1696251315,1696297377,1696297587; Hm_lpvt_bf3296661a119dc2e4c3427b339b6d9e=1696297587; MMSSessionSID=F3A248F0A510FF2F1ADF652AA098499B; isLoginId=50e3517e-0a15-4373-97fe-0cbffc33658d; qs_cid=288709; qs_uid=465742; JXSessionSID=<SNAID>409A380FA8E1B86D54312151B9D4F3A8</SNAID>",
        "Content-Type":"application/json;charset=UTF-8",
    }

    params = (
        ('auto', 'true'),
    )
    # yy19921001
    data = '{"userName":15100211300,"password":"F67A34592FBD5616571BE0E5CF065D8A"}'

    response = requests.post('https://web.qinsilk.com/is/admin/login.ac', headers=headers, params=params, data=data, verify=False, proxies=proxy)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)
    return cookies


headers = {
    'authority': 'web.qinsilk.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://web.qinsilk.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://web.qinsilk.com/is/admin/inner/storehouse/goodsStoredList.ac?mid=3&',
    'accept-language': 'zh-CN,zh;q=0.9',
}
cookies = login()

def number(num):
    if num % 18 == 0:
        ccs = num/18
        print("总共有%d页"%ccs)
    else:
        ccs = num/18+1
        print("总共有%d页" % ccs)
    return int(ccs)

def get_time():
    nt = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    now_time = datetime.datetime.now()
    now_time = now_time + datetime.timedelta(days=1)
    now_time_1 = now_time.strftime("%Y-%m-%d 00:00:00")
    day_7 = now_time + datetime.timedelta(days=-7)
    day_7 = day_7.strftime("%Y-%m-%d 00:00:00")
    day_30 = now_time + datetime.timedelta(days=-30)
    day_30 = day_30.strftime("%Y-%m-%d 00:00:00")
    return now_time_1,day_7,day_30,nt

def data(page,id,house):
    data = {
      'page': page,
      'storehouseId': id,
      'categoryId': '',
      'operator': '3',
      'existsNumber': '1',
      'zeroNumber': '0',
      'warnNumber': '0',
      'listDataType': '2',
      'supplierId': '',
      'isOnSale': '1',
      'storehouseMerge': house,
      'search': 'false',
      'nd': '1620526812187',
      'rows': '18',
      'sidx': '',
      'sord': 'asc'
    }
    return data

def data2(id,day,now_time,page):
    data = {
        'storehouseId':id,
        'storeId': '',
        'searchKey': '',
        'beginTime': day,
        'endTime': now_time,
        'categoryId': '',
        'blandId': '',
        'colorId': '',
        'sizeId': '',
        'styleId': '',
        'materialId': '',
        'unit': '',
        'year': '',
        'seasonId': '',
        'orderStatus': '2',
        'businessType': '-1',
        'rows': '18',
        'sidx': '',
        'sord': 'asc',
        'page': page
    }
    return data

def get_alldatas(id,house,name):
    cookies = login()
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    data1 = data('1',id,house)  # 第1页
    response1 = requests.post('https://web.qinsilk.com/is/admin/inner/storehouse/getGoodsSkuStoredListJSON.ac', headers=headers,cookies=cookies, data=data1, timeout=5, verify=False, proxies=proxy)
    datas1 = json.loads(response1.text)
    pages = int(datas1["records"])
    pages = number(pages)
    for page in range(1,pages+1):
        cookies = login()
        data2 = data(page,id,house)
        response = requests.post('https://web.qinsilk.com/is/admin/inner/storehouse/getGoodsSkuStoredListJSON.ac',
                                 headers=headers,cookies=cookies, data=data2,timeout=5, verify=False, proxies=proxy)
        datas = json.loads(response.text)
        print(f'正在获取第{page}页的数据')
        # print(datas)
        time.sleep(1.2)
        # if "row" not in datas:
            # print("出现错误啦")
            # continue
        print(datas)
        for row in datas["rows"]:
            availableNumber = row["availableNumber"]
            goodsSn = row["goodsSn"]
            colorName = row["colorName"]
            hebing = f'{goodsSn}{colorName}'
            l1.append(goodsSn)
            l2.append(colorName)
            l3.append(availableNumber)
            l4.append(hebing)
    c ={'合并':l4,'货号':l1,'颜色':l2,name:l3}
    df1 = pandas.DataFrame(c)
    print(df1)
    return df1

def get_allday(id,now_time,day,num):   #近30天销量数据
    cookies = login()
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    data1 = data2(id,day,now_time,'1')
    response1 = requests.post('https://web.qinsilk.com/is/admin/inner/report/sale/saleGroupBySkuListJSON.ac', headers=headers,cookies=cookies, data=data1,timeout=5, verify=False, proxies=proxy)
    datas1 = json.loads(response1.text)
    pages = int(datas1["records"])
    pages = number(pages)
    for page in range(1,pages+1):
        cookies = login()       # 我不断地获取最新的cookie,这下子你就不敢奈我何了吧hhh
        data = data2(id,day,now_time,page)
        response = requests.post('https://web.qinsilk.com/is/admin/inner/report/sale/saleGroupBySkuListJSON.ac',
                                  headers=headers,cookies=cookies, data=data, timeout=5, verify=False, proxies=proxy)
        datas = json.loads(response.text)
        print(f'正在获取第{page}页的数据')
        time.sleep(1.25)
        for row in datas["rows"]:
            quantity = row["quantity"]
            goodsSn = row["goodsSn"]
            colorName = row["colorName"]
            hebing2 = f'{goodsSn}{colorName}'
            l1.append(goodsSn)
            l2.append(colorName)
            l3.append(quantity)
            l4.append(hebing2)
    if id == '362011':
        key = '网供'
    else:
        key = ''
    c ={'合并':l4,'货号':l1,'颜色':l2,f'近{num}日{key}销量':l3}
    df3 = pandas.DataFrame(c)
    print(df3)
    return df3

df1 = get_alldatas('','true','合并仓库库存')  #合并仓库统计  #这是总的，以这个为基础
df2 = get_alldatas('1202211','','在生产库库存') # 在生产库存
df3 = get_alldatas('640298','','仓库库存')  #仓库
df4 = get_alldatas('362011','','网供库存')  # 网供
df5 = get_allday('',get_time()[0],get_time()[1],'7')  #近7天销售量
df6 = get_allday('',get_time()[0],get_time()[2],'30')  #近30天销售量
df7 = get_allday('362011',get_time()[0],get_time()[1],'7')  #近7日网供销量
r1 = pandas.merge(df1,df2.loc[:,['合并','在生产库库存']],how='left',on=['合并'])
r2 = pandas.merge(r1,df3.loc[:,['合并','仓库库存']],how='left',on=['合并'])
r3 = pandas.merge(r2,df4.loc[:,['合并','网供库存']],how='left',on=['合并'])
r4 = pandas.merge(r3,df5.loc[:,['合并','近7日销量']],how='left',on=['合并'])
r5 = pandas.merge(r4,df6.loc[:,['合并','近30日销量']],how='left',on=['合并'])
result = pandas.merge(r5,df7.loc[:,['合并','近7日网供销量']],how='left',on=['合并'])


result['仓库+网供'] = result['仓库库存'] + result['网供库存']
result['库存7天预警'] = result['仓库+网供']/(result['近7日销量']/7)
result['库存30天预警'] = result['仓库+网供']/(result['近30日销量']/30)
result['在生产30天预警'] = result['合并仓库库存']/(result['近30日销量']/30)
result['2天调拨参考'] = result['网供库存']-(result['近7日网供销量']/3.5)
result['库存充足情况'] = result['仓库库存']+result['2天调拨参考']

result1 = result


decimals = pandas.Series([0, 0, 0,0,0], index=['库存7天预警', '库存30天预警', '在生产30天预警','2天调拨参考','库存充足情况'])
result = result1.round(decimals)

result['库存7天预警'].replace([np.inf, -np.inf], 0, inplace=True)
result['库存30天预警'].replace([np.inf, -np.inf], 0, inplace=True)
result['在生产30天预警'].replace([np.inf, -np.inf], 0, inplace=True)

del result['合并']

def color_1(s):
    is_max = s < 7
    return ['background-color: red' if v else '' for v in is_max]

def color_2(s):
    is_max = s < 30
    return ['background-color: red' if v else '' for v in is_max]

def color_3(s):
    is_max = s < 10
    return ['background-color: red' if v else '' for v in is_max]

def color_4(s):
    is_max = s < 0
    return ['background-color: red' if v else '' for v in is_max]

result = result[['货号','颜色','合并仓库库存','在生产库库存','仓库库存','网供库存','近7日销量','近30日销量','仓库+网供','库存7天预警','库存30天预警','在生产30天预警','近7日网供销量','2天调拨参考','库存充足情况']]

def BMI(x):
    a = x['近7日网供销量']
    b = x['网供库存']
    bmi = a-b
    return bmi

result['7天调拨参考'] = result.apply(BMI,axis=1)

df_id = result['7天调拨参考']
result = result.drop('7天调拨参考',axis=1)
result.insert(2,'7天调拨参考',df_id)
result = result[['货号','颜色','7天调拨参考','2天调拨参考','近7日网供销量','合并仓库库存','在生产库库存','仓库库存','网供库存','近7日销量','近30日销量','仓库+网供','库存7天预警','库存30天预警','在生产30天预警','库存充足情况']]


df1 = result.style.apply(color_1,subset=['库存7天预警']).apply(color_2,subset=['库存30天预警','在生产30天预警']).apply(color_3,subset=['2天调拨参考']).apply(color_4,subset=['库存充足情况'])

df1.to_excel(f'分析结果{int(round(time.time() * 1000))}.xlsx',index=False)
time.sleep(3)
print('程序运行结束，请退出程序')








