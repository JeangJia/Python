#
# class User:
#     def __init__(self,first_name,last_name,age):
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#     def describe(self):
#         print(f"{self.first}{self.last }{self.age}")
#     def greet(self):
#         print("Hello")
# user=User('jia','yi_hang','18')
# print(f"{user.first}")
# user.describe()
# user.greet()

num=int(input('请输入一个三位数:'))
a=num//100
c=num%10
b=(num//10)%10
x=c*100+b*10+a
print(f"输入三位数反为:{x}")