import requests
import json
import time
import datetime
import pandas
import numpy as np
import jinja2
import xlrd
import hashlib

"""
客户的代码
"""
def getmd5(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode("utf-8"))
    ans = md5.hexdigest()
    return ans.upper()



def login():
    url = "https://web.qinsilk.com/is/admin/login.ac?auto=true"
    headers = {
        "Referer":"https://web.qinsilk.com/is/admin/loginOut.ac?mid=1&",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Cookie":"lastUser=15100211300; lastAutoLoginCheck=true; JSESSIONID=3FA575B85460BB668BD60C3FF8E53CB5; _ati=3215790475175; qs_sys=is; p_h5_u=9C899F0C-AC26-4AE2-8C71-52A1AA78BA7D; _pk_id.1.bc87=cb5b1f4f2780bcf0.1696225744.; Hm_lvt_bf3296661a119dc2e4c3427b339b6d9e=1696225743,1696251315,1696297377,1696297587; Hm_lpvt_bf3296661a119dc2e4c3427b339b6d9e=1696297587; MMSSessionSID=F3A248F0A510FF2F1ADF652AA098499B; isLoginId=50e3517e-0a15-4373-97fe-0cbffc33658d; qs_cid=288709; qs_uid=465742; JXSessionSID=<SNAID>409A380FA8E1B86D54312151B9D4F3A8</SNAID>",
        "Content-Type":"application/json;charset=UTF-8",
    }
    data = '{"userName": 15100211300,"password": "F67A34592FBD5616571BE0E5CF065D8A","nvcVal": "%7B%22a%22%3A%22FFFF0N0000000000827B%22%2C%22c%22%3A%22FFFF0N0000000000827B%3Anvc_login%3A1696252819687%3A0.8620000005677915%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22G820843D54D7EAC728C01DD3F9468D87D804D0BD561BC78E9F7%22%7D%2C%22b%22%3A%22226!M4Uz%2FPXZblM9zbbvVhnwuTJM2twZOGpzS3PncGpkNNV4WheiRExgtl7Gl8yDlAEKGOcU6Q55wXeSShnGcMQLoumHmWCSEUAIgMXC8zwFTXH7xaQG2Ynr1Hul0KzWoBig51Uc%2Bx6ZrP3P6RK68VHQ5qB7BM%2BWf%2FOYWSBbUgv88ijUoghB4UeFkYoYTK%2FfFgH7cxcnWyWj27JlWiBG8pXZ%2Ffm%2FX62%2FbvfYhOzhvydltZRegu1C9V9mFPtHYPaRKeCPte2dTt2i3ZHDl3sHPdzeyPAsRE21LrF412y9KVeH9fAhmfQgUxFDd3tWDo4RoW8OvcT9CupuGFGs33gFnP8QddZHh4dVqNQdUDPf7rUJzmlvUuOqbJ4lcc0GN2g26VmrluWY7Ecokg4hMZnTCZLdQNHy6NASnFPV3I73Oe44mZ%2Folcd%2FA9c%2BZqpPaPMTtJMpWzGoIlXPaybWj4UaQKfnv%2B0BxbZTcl4kHsKKInrmI7YQEsy9q4t47EFyY1uFz6FYwu4h%2Ffj3gC8CDpPJcQul8jEc%2FHjQv96DAnSAAJ0LW%2FVqGJGZy5cTJ0nKzz7%2BpsBTT%2BGgZzkykXYfTSauKLvQBB9MZff%2Fn1bJZKoy8G0J7baH4zH9JcI1cT0B%2Bze%2FHDk5mgovn0sOSpaj%2B3iV6ISRmiXc%2FfzdMpnQjz0roWtbCjfPe%2ByLgfuoiuyj%2B1Z%2Bq7kjURe8ibrQfEVw%2BFKj%2F7z04kPZqzMI%2FA5G3f%2FCrWUBj%2FPsamHoNEnGELJWcibGCmj%2FQlOBxRcfoJMn3gAM0B%2FDc6t4QGEZe9WDtmVymMGD61szen3n%2FmWtiliFTiOlruRVMxSdTqZYBtHW7YfqOZqcqF3xYiqRNVt9vIkvGP9yucfFOws8ho4DnKEm6FkplTUqBUwT7%2B1S2BjAZSAdAPytQoqH5kZ44xLvzFWFtBfmRW2HGDyAWkAzvANlFkEtDqlOW46XXXRxIACDHr9SfrVQ59Pbyk2VnIgtYHPvB7L2QRMga0RvKFiSojVbv%2BpZ5HRJq4CGMM0nEs690Sxm7zuNTrkiVohYGj3GZ%2FNPmhMP6jc5TQJRNLd%2Bfn4nUUBXbS%2BTzm%2FoLuBtFXbZg8%2FZyUkaneTR7JhV%2FtrLzm%2Fo3DaNyfGcexN9wDwQgXoAYfzsM%2FEy8eIMWAT69hc4e1H%2F6U3quvvt3golyVcczSAsUSkH9ugylzy9HDoeycWKV7ztqcr0IIYyKqMTleEhvaGJBbTMyWiAVrTheciHXql6hK5uymMvEnAq8DkEbvwWjznYqWi844GIV%2Fa%2FvbQIHiYRMvOXM9se1aDcsmEs4XS%2FV4aR0WMwl3lMdURT5huVc8Tl8IcozmM7cUR4wXb23B9ZyUNuLeUJr8TtnVkcOOEB3DNbqSvag8%2F2yDaa%2BZlv1BiHyVmVzm%2FW3Ualdj4Sg4pZyfowny5R3BQHDIccT59WhshWqOvBEMHjpUfk5VnR1f5kRyiRbcyDhsUWy5JB0MA0%2FZTQ5Iwh1LECyvhtJ9pMkKnWySeTg8XZOp02nyw838QesK77zx%2ByLWf%2F4U0b%2FstFY%2B%2FhQvvQ%2F6JeMceDb3MNXa0x7DLQkyrEVoLOD8FIMAYfd00DDUvmQYySkeVj78YA5d%2Bp5wC4sGZufqsJVvwpZ1P74jc1bfoS2o70DgcfGtfoyJ3ALjO1I0Hibh5Zuky1WlfOmSF10pgovF3nJcIiPTAa7MAy7CgdL51WoKdi3WuSzJ50L0%2Bo7iHXix3XQCn%2BWBKl4uMz9nONYBzMJkKqlvG06yyQGvfD7gA5uYgX%2Bcrwd%2B%2BHm2cdQbfXzp2f3P9fMj7mnnoz8JUsUSHUPW6mJmP9%2BTkPlOx2pXlPEQdEDOEYBpvBvBZVbARXEL6EwfEcUWYYvLLes5o957BizlES3shOJHIeCuzsJrUemHfaO0DO%2BUSyjdCnrPvbdZLMzmx67azNZ%2FUsxNi0Ttf7VzNsZLQ%2BrZwu6QKLm2NhxSqmVxbAbR04%2F8W%2Fp%2FUG%2BSm%2Fq4jIK2RKGj5vpggzkSgcmMADqbd2FstbYNemlMiWezrVNiy1XxVVYvxauUIomloG9VxCUfGaz7%2Fw66G3%2F0MqrguF8NjESuL6uyl5ajThO3yFsPKJuqICuyZRRlLc6Xz56lP9%22%2C%22e%22%3A%22B88R4ZYHK05FlYsJoiMOPHjscIzVS0JJAtE6zhOAG6COu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK8uwcStZ8e2-Jb9ewcXMyAVpj-R60jwupuq2sUfOi9-5%22%7D"}'
    proxy = {'http':"","https":""}
    response = requests.post(url,data= data, headers= headers,  verify= False, proxies=proxy)
    print(response.text)

    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)
    return cookies



headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Cookie":"lastUser=15100211300; lastAutoLoginCheck=true; JSESSIONID=3FA575B85460BB668BD60C3FF8E53CB5; _ati=3215790475175; qs_sys=is; p_h5_u=9C899F0C-AC26-4AE2-8C71-52A1AA78BA7D; _pk_id.1.bc87=cb5b1f4f2780bcf0.1696225744.; Hm_lvt_bf3296661a119dc2e4c3427b339b6d9e=1696225743,1696251315,1696297377,1696297587; Hm_lpvt_bf3296661a119dc2e4c3427b339b6d9e=1696297587; MMSSessionSID=F3A248F0A510FF2F1ADF652AA098499B; isLoginId=50e3517e-0a15-4373-97fe-0cbffc33658d; qs_cid=288709; qs_uid=465742; JXSessionSID=<SNAID>409A380FA8E1B86D54312151B9D4F3A8</SNAID>",
    "Content-Type":"application/json;charset=UTF-8",
    "Referer":"https://web.qinsilk.com/is/admin/inner/storehouse/goodsStoredList.ac?mid=3&t=",
}

# passwd = input("请输入你的密码:")
# passwd = getmd5(passwd)

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
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    data1 = data('1',id,house)
    proxy = {'http':"","https":""}
    response1 = requests.post('https://web.qinsilk.com/is/admin/inner/storehouse/getGoodsSkuStoredListJSON.ac', headers=headers,cookies=cookies, data=data1, timeout=10, verify=False, proxies=proxy)
    datas1 = json.loads(response1.text)
    print(datas1)
    pages = int(datas1["records"])
    pages = number(pages)
    for page in range(1,pages+1):
        data2 = data(page,id,house)
        response = requests.post('https://web.qinsilk.com/is/admin/inner/storehouse/getGoodsSkuStoredListJSON.ac',
                                 headers=headers,cookies=cookies, data=data2,timeout=10, verify= False, proxies=proxy)
        datas = json.loads(response.text)
        print(f'正在获取第{page}页的数据')
        time.sleep(1.2)
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
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    data1 = data2(id,day,now_time,'1')
    proxy = {'http':"","https":""}
    response1 = requests.post('https://web.qinsilk.com/is/admin/inner/report/sale/saleGroupBySkuListJSON.ac', headers=headers,cookies=cookies, data=data1,timeout=10, verify=False)
    print(response1.text)
    datas1 = json.loads(response1.text)
    pages = int(datas1["records"])
    pages = number(pages)
    for page in range(1,pages+1):
        data = data2(id,day,now_time,page)
        response = requests.post('https://web.qinsilk.com/is/admin/inner/report/sale/saleGroupBySkuListJSON.ac',
                                  headers=headers,cookies=cookies, data=data, timeout=10, verify=False)
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
input("请按任意键结束")








