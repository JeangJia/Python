class Dog:                                     #类的首字母要大写!!!
    def __init__(self, name, age):             #类中的函数称为方法(这个为特殊方法)
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting.")
my_dog=Dog('jojo','9')
you_dog=Dog('lili','6')
print(f"My dog's name is {you_dog.name}\nyour dog's {my_dog.age} years old")
my_dog.sit()                                      #调用方法
