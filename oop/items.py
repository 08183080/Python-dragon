"""
hello oop
我想要熟悉python中的oop编程
ref:  https://www.youtube.com/watch?v=Ej_02ICOIgs
https://github.com/jimdevops19/PythonOOP/tree/main

9-24 night 看了1h的视频了,循序渐进娓娓而谈很有收获
明晚继续补,从csv读取实例化的对象打印出来有点问题的...

9-25
已经解决 定义一个全局列表all
"""
import gc
import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greator than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    # represent an object
    def __repr__(self):
        # print(f"{self.name}")
        return self.name

    # 类方法
    @classmethod
    def insantiate_from_csv(cls):
        f = open("./items.csv", "r")
        # print("open~")
        reader = csv.DictReader(f)
        items = list(reader)   # dict -> list
        # print(items)

        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity"))
            )
            # print("success!")
            # print(item)
            
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

# Item.insantiate_from_csv()
# print(Item.all)
print(Item.is_integer(7.5))

