"""
hello oop
我想要熟悉python中的oop编程
ref:  https://www.youtube.com/watch?v=Ej_02ICOIgs
https://github.com/jimdevops19/PythonOOP/tree/main

9-24 night 看了1h的视频了,循序渐进娓娓而谈很有收获
明晚继续补,从csv读取实例化的对象打印出来有点问题的...
"""
import gc
import csv

class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greator than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


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
        reader = csv.DictReader(f)
        items = list(reader)   # dict -> list
        # print(items)

        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity"))
            )


# item1 = Item("iphone", 100, 1)  
# # print(Item.pay_rate)
# # print(Item.__dict__) # All the attributes for Class level 
# # print(item1.__dict__) # All the attributes for instance level
# print(item1.apply_discount())

# item2 = Item("iphone", 100, 1)  
# item2.pay_rate = 0.7
# print(item2.apply_discount())

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)



Item.insantiate_from_csv()



for obj in gc.get_objects():
    if isinstance(obj, Item):
        print(obj)