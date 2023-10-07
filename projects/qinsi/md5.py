import hashlib

def getmd5(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode("utf-8"))
    ans = md5.hexdigest()
    return ans.upper()

# passwd = "111"
# ans = getmd5(passwd) # 698D51A19D8A121CE581499D7B701668
# print(ans)

passwd = input("输入 密码: ")
ans = getmd5(passwd)
print("md5加密后: ",ans)
input("请输入任意键结束")