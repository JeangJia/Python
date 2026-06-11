#1.if-else  2.if-elif  3.if-else-elif  4.if
users_input = input('请输入您的年龄：')
if float(users_input)<=18:
    print('您在正华正茂')
else:
    print('老了，老了')

#5.8                               #for与if结合
users=['a','b','c','d','e']
for user in users:
    if 'a' in user:
        print(f"Hello! {user.title()}")
    else:
        print('hello')

#5.10
current_users=['A','B','C','D','E']
new_users=['A','B','c','d','e']
for new_user in new_users:
    if new_user in current_users:
        print(f"抱歉'{new_user}'用户已被占用")
    else:
        print("此用户未被使用，您已注册成功！")

#5.11
digits=['1','2','3','4','5','6','7','8','9']
for digit in digits:
    if digit in '1':
        print('1st')
    elif digit in '2':
        print('2nd')
    elif digit in '3':
        print('3rd')
    else:
        print(f"{digit}th")