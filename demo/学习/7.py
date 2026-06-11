print(int(input('请输入你的身高:')) > 180)  # int()将字符串转换成浮点数即整数

key = int(input("请输入密码："))  # if-else 有一个分支   if-elif 可有多个分支
if key == 1900:
    print('密码正确')
else:
    print('密码错误')

# -----------------------------------------------------------------------------------------------------------

prompt = '请输入想输入的消息：（按q退出程序）'
message = ''
while message != 'q':
    message = input(prompt)
    if message != 'q':  # while循环结合if—else来终止循环
        print(f"您输入的消息是：{message}")
    else:
        print('您已退出程序')

# --------------------------------------------------------------------------------------------------------------

numbers = ['1', '2', '3', '1', '5', '1']
while '1' in numbers:
    numbers.remove('1')  # 剔除重复项
print(numbers)

# --------------------------------------------------------------------------------------------------------------

while True:  # 直接定义
    first_name = input("f_name:")
    last_name = input('l_name:')
    full_name = f"{first_name}{last_name}"
    print(full_name)
    if first_name == 'q':
        break  # 使用break打破循环
    if last_name == 'q':
        break

# --------------------------------------------------------------------------------------------------------------

print('哈喽呀！我是一个消息收集器 &>_<& ')
dictionary = {}
users_input = True  # 标志
while users_input:
    names = input('你的名字是?')
    message = input('请输入您想输入的消息:')
    dictionary[names] = message
    repeat = input('是否还有谁想输入消息？(yes/no)')
    if repeat == 'no':
        users_input = False
print('-------所有结果如下:------')
for name, message in dictionary.items():
    print(f"{name}输入的消息为：{message}")

# --------------------------------------------------------------------------------------------------------------

user_input = '请输入您的年龄：'
enter = True
while enter:
    number = input(user_input)
    if 0 < int(number) <= 3:
        print('免费')
    elif 3 < int(number) <= 12:
        print('需要付款10$')
    elif int(number) > 12:
        print('需要付款15$')
    elif int(number) <= 0:
        print("你还在娘胎里？")
