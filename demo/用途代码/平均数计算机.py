x = 0
y = 0
user_input = input('请输入数字(按q终止程序并开始计算):')
while user_input != 'q':
   number = float(user_input)
   x += number
   y += 1
   user_input = input('请输入数字(按q终止程序并开始计算)')
if y == 0:
   x = 0
else:
   price = x/y
print("平均数为;"+str(price))