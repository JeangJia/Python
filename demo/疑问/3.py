user_input='请输入您的年龄：'
shuru=True
while shuru:
   numder = input(user_input)
   if 0< int(numder) <= 3:
        print('免费')
   elif 3<int(numder)<=12:
       print('需要付款10$')
   elif int(numder)>12 :
       print('需要付款15$')
   else:
       print("请输入您的年龄：")
