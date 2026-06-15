class Car:
    # 类属性
    wheel = 4

    # __init__ :初始化方法,对象创建后自动调用,主要用于设置对象的初始状态
    # self 方法的第一个参数,表示创建的实例对象
    def __init__(self, model: str, make="Germany", year=2026, cur_price=800000):
        # 实例属性
        self.model = model
        self.make = make
        self.year = year
        self.cur_price = cur_price
        self.color = "Black"
        # print("Car 初始化完成")

    # 实例方法
    def price(self, discount: float, rate: float = 0.1) -> float:
        """
        计算并返回优惠加上税后的价格
        Args:
            discount: 优惠(百分比)
            rate: 购置税(百分比)
        Returns:返回优惠加上税后的价格
        """
        return round(self.cur_price * discount + self.cur_price * rate, 2)

    # 魔法方法
    # print() 时调用,打印对象时显示的内容,默认输出内存地址
    def __str__(self):
        return f"{self.model} {self.make} {self.year} "

    # 判断 == 时调用,对比两个对象是否相等
    def __eq__(self, other):
        return self.model == other.model and self.year == other.year and self.cur_price == other.cur_price

    # 判断 < 时调用
    def __lt__(self, other):
        return self.cur_price < other.cur_price


c1 = Car("E300", "Chinese", 2022, 500000)
c2 = Car("718")
c3 = Car("911")

print(c1)
print(c1.__dict__)  # __dict__ 会将对象中的所有属性以字典的形式输出出来
print(f"价格为: {c1.price(0.8, 0.1)}")
print(c1 < c2)
