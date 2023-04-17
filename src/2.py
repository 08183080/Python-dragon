import time
import threading        # Python中的线程包，可以实现：多线程操作~

def callback():
    time.sleep(3)   # 休眠3秒
    print(2)

def test():
    print(1)
    timer=threading.Timer(3.0,callback) # 创建一个定时器，3s后调用callback函数
    timer.start()
    print(3)
    print(4)
    print(5)
    print(6)

test()

'''
【模拟callback流程】
【结果】
1
3
4
5
6
2

callback就像你在餐厅吃饭，服务员把菜单给你之后，继续进行接下来的操作，
等你点餐之后，服务员再来你这里响应你的请求，每一个顾客的处理函数就是回调函数（callback）~


'''