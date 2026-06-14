class Car:
    # __init__ :初始化方法,对象创建后自动调用,主要用于设置对象的初始状态
    # self 方法的第一个参数,表示创建的实例对象
    def __init__(self, model: str, make="Germany", year=None, cur_price=None):
        self.model = model
        self.make = make
        self.year = year
        self.cur_price = cur_price
        self.color = "Black"
        print("Car 初始化完成")

    def price(self, discount: float, rate: float = 0.1) -> float:
        return round(self.cur_price * discount + self.cur_price * rate, 2)


# __dict__ 会将对象中的所有属性以字典的形式输出出来
c1 = Car("E300", "Chinese", 2026, 500000)
print(c1)
print(c1.__dict__)
print(f"价格为: {c1.price(0.8, 0.1)}")
