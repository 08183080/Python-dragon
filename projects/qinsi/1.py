"""
目的: 模拟登录【秦丝】网站, 服务【服装】行业
y1s1,【秦丝】网站真拉跨, 登录卡的要死...
我还发现【秦丝】网站有些密码泄露了:   111,111

【谷歌浏览器 F12】按【preserve log】即便页面跳转, 仍然保留网络流量日志

我自己改了改,成功!
"""
import requests
import hashlib

def getmd5(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode("utf-8"))
    ans = md5.hexdigest()
    return ans.upper()

"""
登录,同时获取cookie...
"""
def login(passwd):
    url = "https://web.qinsilk.com/is/admin/login.ac?auto=true"
    headers = {
        "Referer":"https://web.qinsilk.com/is/admin/loginOut.ac?mid=1&",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Cookie":"lastAutoLoginCheck=true; lastUser=111; JSESSIONID=03704B33EA7AFCC8A84B5C3A5C8AC876; _ati=3215790475175; qs_sys=is; p_h5_u=9C899F0C-AC26-4AE2-8C71-52A1AA78BA7D; _pk_id.1.bc87=cb5b1f4f2780bcf0.1696225744.; MMSSessionSID=59B1FE1CFF58A547105071DDF38D245E; qs_cid=5781; qs_uid=104929; Hm_lvt_bf3296661a119dc2e4c3427b339b6d9e=1696225743,1696251315; Hm_lpvt_bf3296661a119dc2e4c3427b339b6d9e=1696251964; isLoginId=1362891c-888a-4afe-90aa-ec19bd4dc26e; JXSessionSID=<SNAID>5C0FBD10B037A7AB4CC6B96886642BD8</SNAID>",
        "Content-Type":"application/json;charset=UTF-8",

    }
    # 密码是加密的,md5算法
    data = f'{{"userName": "111","password": "{passwd}","nvcVal": "%7B%22a%22%3A%22FFFF0N0000000000827B%22%2C%22c%22%3A%22FFFF0N0000000000827B%3Anvc_login%3A1696252819687%3A0.8620000005677915%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22G820843D54D7EAC728C01DD3F9468D87D804D0BD561BC78E9F7%22%7D%2C%22b%22%3A%22226!M4Uz%2FPXZblM9zbbvVhnwuTJM2twZOGpzS3PncGpkNNV4WheiRExgtl7Gl8yDlAEKGOcU6Q55wXeSShnGcMQLoumHmWCSEUAIgMXC8zwFTXH7xaQG2Ynr1Hul0KzWoBig51Uc%2Bx6ZrP3P6RK68VHQ5qB7BM%2BWf%2FOYWSBbUgv88ijUoghB4UeFkYoYTK%2FfFgH7cxcnWyWj27JlWiBG8pXZ%2Ffm%2FX62%2FbvfYhOzhvydltZRegu1C9V9mFPtHYPaRKeCPte2dTt2i3ZHDl3sHPdzeyPAsRE21LrF412y9KVeH9fAhmfQgUxFDd3tWDo4RoW8OvcT9CupuGFGs33gFnP8QddZHh4dVqNQdUDPf7rUJzmlvUuOqbJ4lcc0GN2g26VmrluWY7Ecokg4hMZnTCZLdQNHy6NASnFPV3I73Oe44mZ%2Folcd%2FA9c%2BZqpPaPMTtJMpWzGoIlXPaybWj4UaQKfnv%2B0BxbZTcl4kHsKKInrmI7YQEsy9q4t47EFyY1uFz6FYwu4h%2Ffj3gC8CDpPJcQul8jEc%2FHjQv96DAnSAAJ0LW%2FVqGJGZy5cTJ0nKzz7%2BpsBTT%2BGgZzkykXYfTSauKLvQBB9MZff%2Fn1bJZKoy8G0J7baH4zH9JcI1cT0B%2Bze%2FHDk5mgovn0sOSpaj%2B3iV6ISRmiXc%2FfzdMpnQjz0roWtbCjfPe%2ByLgfuoiuyj%2B1Z%2Bq7kjURe8ibrQfEVw%2BFKj%2F7z04kPZqzMI%2FA5G3f%2FCrWUBj%2FPsamHoNEnGELJWcibGCmj%2FQlOBxRcfoJMn3gAM0B%2FDc6t4QGEZe9WDtmVymMGD61szen3n%2FmWtiliFTiOlruRVMxSdTqZYBtHW7YfqOZqcqF3xYiqRNVt9vIkvGP9yucfFOws8ho4DnKEm6FkplTUqBUwT7%2B1S2BjAZSAdAPytQoqH5kZ44xLvzFWFtBfmRW2HGDyAWkAzvANlFkEtDqlOW46XXXRxIACDHr9SfrVQ59Pbyk2VnIgtYHPvB7L2QRMga0RvKFiSojVbv%2BpZ5HRJq4CGMM0nEs690Sxm7zuNTrkiVohYGj3GZ%2FNPmhMP6jc5TQJRNLd%2Bfn4nUUBXbS%2BTzm%2FoLuBtFXbZg8%2FZyUkaneTR7JhV%2FtrLzm%2Fo3DaNyfGcexN9wDwQgXoAYfzsM%2FEy8eIMWAT69hc4e1H%2F6U3quvvt3golyVcczSAsUSkH9ugylzy9HDoeycWKV7ztqcr0IIYyKqMTleEhvaGJBbTMyWiAVrTheciHXql6hK5uymMvEnAq8DkEbvwWjznYqWi844GIV%2Fa%2FvbQIHiYRMvOXM9se1aDcsmEs4XS%2FV4aR0WMwl3lMdURT5huVc8Tl8IcozmM7cUR4wXb23B9ZyUNuLeUJr8TtnVkcOOEB3DNbqSvag8%2F2yDaa%2BZlv1BiHyVmVzm%2FW3Ualdj4Sg4pZyfowny5R3BQHDIccT59WhshWqOvBEMHjpUfk5VnR1f5kRyiRbcyDhsUWy5JB0MA0%2FZTQ5Iwh1LECyvhtJ9pMkKnWySeTg8XZOp02nyw838QesK77zx%2ByLWf%2F4U0b%2FstFY%2B%2FhQvvQ%2F6JeMceDb3MNXa0x7DLQkyrEVoLOD8FIMAYfd00DDUvmQYySkeVj78YA5d%2Bp5wC4sGZufqsJVvwpZ1P74jc1bfoS2o70DgcfGtfoyJ3ALjO1I0Hibh5Zuky1WlfOmSF10pgovF3nJcIiPTAa7MAy7CgdL51WoKdi3WuSzJ50L0%2Bo7iHXix3XQCn%2BWBKl4uMz9nONYBzMJkKqlvG06yyQGvfD7gA5uYgX%2Bcrwd%2B%2BHm2cdQbfXzp2f3P9fMj7mnnoz8JUsUSHUPW6mJmP9%2BTkPlOx2pXlPEQdEDOEYBpvBvBZVbARXEL6EwfEcUWYYvLLes5o957BizlES3shOJHIeCuzsJrUemHfaO0DO%2BUSyjdCnrPvbdZLMzmx67azNZ%2FUsxNi0Ttf7VzNsZLQ%2BrZwu6QKLm2NhxSqmVxbAbR04%2F8W%2Fp%2FUG%2BSm%2Fq4jIK2RKGj5vpggzkSgcmMADqbd2FstbYNemlMiWezrVNiy1XxVVYvxauUIomloG9VxCUfGaz7%2Fw66G3%2F0MqrguF8NjESuL6uyl5ajThO3yFsPKJuqICuyZRRlLc6Xz56lP9%22%2C%22e%22%3A%22B88R4ZYHK05FlYsJoiMOPHjscIzVS0JJAtE6zhOAG6COu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK8uwcStZ8e2-Jb9ewcXMyAVpj-R60jwupuq2sUfOi9-5%22%7D"}}'
    print(data)
    proxy = {'http':"","https":""}
    response = requests.post(url,data= data, headers= headers, verify= False, proxies=proxy)
    print(response.text)

    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)
    return cookies

passwd =  input("请输入密码: ")
print(passwd)
passwd = getmd5(passwd)
login(passwd)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Cookie":"lastAutoLoginCheck=true; lastUser=111; JSESSIONID=03704B33EA7AFCC8A84B5C3A5C8AC876; _ati=3215790475175; qs_sys=is; p_h5_u=9C899F0C-AC26-4AE2-8C71-52A1AA78BA7D; _pk_id.1.bc87=cb5b1f4f2780bcf0.1696225744.; MMSSessionSID=59B1FE1CFF58A547105071DDF38D245E; qs_cid=5781; qs_uid=104929; Hm_lvt_bf3296661a119dc2e4c3427b339b6d9e=1696225743,1696251315; Hm_lpvt_bf3296661a119dc2e4c3427b339b6d9e=1696251964; isLoginId=1362891c-888a-4afe-90aa-ec19bd4dc26e; JXSessionSID=<SNAID>5C0FBD10B037A7AB4CC6B96886642BD8</SNAID>",
    "Content-Type":"application/json;charset=UTF-8",
    "Referer":"https://web.qinsilk.com/is/admin/inner/storehouse/goodsStoredList.ac?mid=3&t=",
}

