def add(a,b,callback):
    result=a+b
    callback(result)

def print_result(result):
    print('计算结果为：',result)

# f1 ——调用——> f2，f2 ——反馈——>f1，此之为callback~

add(2,3,print_result)   
print("继续奏乐继续舞")