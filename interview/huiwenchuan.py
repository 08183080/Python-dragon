def judge(s):
    # 字符串切片
    return s == s[::-1] 

if __name__ == "__main__":
    while 1:
        s = input("请输入字符串: ")
        if judge(s):
            print(s, "是回文字符串")
        else:
            print(s, "不是回文串~")
